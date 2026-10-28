# Copyright (C) 2020-2026 Motphys Technology Co., Ltd. All Rights Reserved.
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This file is part of Motrix Forge.
#
# Motrix Forge is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Motrix Forge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Motrix Forge. If not, see <https://www.gnu.org/licenses/>.
# ==============================================================================

"""Blender-side bootstrap for the e2e driver (run inside headless Blender).

Registers the Forge property groups and the operator subset that needs no asset
libraries (mirrors ``tests/forge/conftest.py``), then starts the MCP TCP
bridge and blocks serving requests until the process is killed.

Port comes from the ``FORGE_E2E_PORT`` env var (default ``9877`` — distinct from
the default live-session ``9876`` so e2e never touches a running Blender).
"""

import os
import sys
from pathlib import Path

ADDON_DIR = Path(__file__).resolve().parents[3] / "addon"
sys.path.insert(0, str(ADDON_DIR))

import bpy

# ── property groups (mirror conftest registered_props) ────────────────
from Forge.core import props as forge_props

if not hasattr(bpy.types.Object, "Forge_Model_Type"):
    for cls in forge_props.classes:
        try:
            bpy.utils.register_class(cls)
        except (RuntimeError, ValueError):
            pass
    forge_props.register_forge_model_props()

# ── operator subset that works without Shapes.blend / full prefs ───────
_OP_SOURCES = [
    ("Forge.ops.definition", "Forge_OT_Type_Define"),
    ("Forge.ops.utilities", "Forge_OT_Batch_Rename"),
    ("Forge.ops.creation", "Forge_OT_Link_Creation"),
    ("Forge.ops.creation", "Forge_OT_Link_MarkRoot"),
    ("Forge.ops.utilities", "Forge_OT_SelectByTAG"),
    ("Forge.ops.utilities", "Forge_OT_SelectHulls"),
    ("Forge.ops.creation", "Forge_OT_Change_Gizmo_Size"),
    ("Forge.ops.creation", "Forge_OT_Frame_Creation"),
    ("Forge.ops.definition", "Forge_OT_Parent_Define"),
    ("Forge.ops.creation", "Forge_OT_Mesh_Check"),
    ("Forge.ops.utilities", "Forge_OT_InstanceSet"),
    ("Forge.ops.creation", "Forge_OT_HeightField_Creation"),
    ("Forge.ops.creation", "Forge_OT_Plane_Creation"),
    ("Forge.ops.creation", "Forge_OT_Inertial_Creation"),
    ("Forge.ops.materials", "Forge_OT_Material_Creation"),
    ("Forge.ops.io_ops", "Forge_OT_Import"),
    ("Forge.ops.io_ops", "Forge_OT_Export"),
]
for mod_path, cls_name in _OP_SOURCES:
    try:
        mod = __import__(mod_path, fromlist=[cls_name])
        bpy.utils.register_class(getattr(mod, cls_name))
    except (RuntimeError, ValueError, ImportError, AttributeError):
        pass

# ── optional asset library (only ops adding geometry modifiers need it) ─
lib_path = ADDON_DIR / "Forge" / "lib" / "assets" / "Shapes.blend"
if lib_path.exists():
    libs = bpy.context.preferences.filepaths.asset_libraries
    if "Forge Library" not in libs:
        entry = libs.new(name="Forge Library", directory=str(lib_path.parent))
        libs.update()

# ── start the MCP TCP bridge and serve until killed ────────────────────
from Forge.mcp import command
from Forge.mcp.server import MCPServer
from Forge.mcp.utils import set_server

port = int(os.environ.get("FORGE_E2E_PORT", "9877"))
set_server(MCPServer())
print(f"Forge e2e bridge ready (port {port})", flush=True)
sys.exit(command.cli_exec(["--host", "localhost", "--port", str(port)]))
