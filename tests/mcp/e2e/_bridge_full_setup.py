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

"""Full Forge operator bootstrap for the MCP model matrix E2E test."""

import os
import sys
from pathlib import Path

ADDON_DIR = Path(__file__).resolve().parents[3] / "addon"
sys.path.insert(0, str(ADDON_DIR))

import bpy
from Forge.core import props as forge_props

if not hasattr(bpy.types.Object, "Forge_Model_Type"):
    for cls in forge_props.classes:
        try:
            bpy.utils.register_class(cls)
        except (RuntimeError, ValueError):
            pass
    forge_props.register_forge_model_props()

from Forge import settings as forge_settings
from Forge.ops import operator as forge_operator
from Forge.ui import panel as forge_panel

# `forge_operator.classes` is the operator registry, but it does not carry
# everything the addon registers — `Forge_OT_COACD` lives in `ui/panel.classes`,
# so registering only the operator tuple leaves `bpy.ops.forge.coacds` missing
# and every call to it fails with "could not be found".
failed = []
for cls in (*forge_operator.classes, *forge_panel.classes, *forge_settings.classes):
    try:
        bpy.utils.register_class(cls)
    except (RuntimeError, ValueError) as exc:
        # Reported rather than swallowed: a class that silently fails to
        # register shows up much later as a confusing "operator not found".
        failed.append(f"{cls.__name__}: {exc}")
if failed:
    print(f"Forge bootstrap: {len(failed)} class(es) failed to register: {failed}", flush=True)

lib_path = ADDON_DIR / "Forge" / "lib" / "assets" / "Shapes.blend"
if lib_path.exists():
    libs = bpy.context.preferences.filepaths.asset_libraries
    if "Forge Library" not in libs:
        libs.new(name="Forge Library", directory=str(lib_path.parent))
        libs.update()

from Forge.mcp import command
from Forge.mcp.server import MCPServer
from Forge.mcp.utils import set_server

port = int(os.environ.get("FORGE_E2E_PORT", "9878"))
set_server(MCPServer())
print(f"Forge full e2e bridge ready (port {port})", flush=True)
sys.exit(command.cli_exec(["--host", "localhost", "--port", str(port)]))
