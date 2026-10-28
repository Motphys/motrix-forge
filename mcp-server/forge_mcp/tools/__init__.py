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

"""Register all Forge MCP tools on the shared FastMCP instance.

Importing this package pulls in every tool module so their ``@mcp.tool()``
decorators run. See ``forge_mcp/skills/forge_create.md`` and
``forge_mcp/skills/forge_modify.md``
for the command specifications. :func:`apply_tool_filter` lets ``FORGE_TOOLS``
limit which tools are served to an agent.
"""

from __future__ import annotations

import os

from . import blendfile, capture, create, docs, geometry, io, modify, scene, skill, utilities  # noqa: F401

# Category -> name prefixes / exact names. Kept in sync with the tool modules.
_CATEGORIES: dict[str, tuple[str, ...]] = {
    "create": ("forge_create_",),
    "modify": (
        "forge_define_",
        "forge_mark_root_link",
        "forge_mark_instance_link",
        "forge_mesh_check",
        "forge_scale_gizmo_size",
    ),
    "edit": (
        "forge_object_info",
        "forge_measure",
        "forge_scene_config",
        "forge_set_transform",
        "forge_set_shape_size",
        "forge_set_property",
        "forge_set_scene_property",
        "forge_set_tendon_targets",
        "forge_rename",
        "forge_delete",
        "forge_execute",
    ),
    "utilities": (
        "forge_scene_info",
        "forge_batch_rename",
        "forge_set_instance_idname",
        "forge_select_by_tag",
        "forge_select_hulls",
    ),
    "capture": ("forge_screenshot",),
    "blendfile": ("forge_blendfile_summary",),
    "geometry": ("forge_coacd",),
    "io": ("forge_import_mjcf", "forge_export_mjcf", "forge_save_blendfile"),
    "docs": ("forge_search_docs",),
    "skill": ("forge_skill",),
}

_CATEGORY_ALIASES = {
    "util": "utilities",
    "screenshot": "capture",
    "search": "docs",
    "blend_file": "blendfile",
    "import": "io",
    "export": "io",
    "save": "io",
    "coacd": "geometry",
    "read-only": "readonly",
    "query": "readonly",
}


def _tool_read_only(manager, name: str) -> bool:
    tool = manager.get_tool(name)
    return bool(tool and tool.annotations and tool.annotations.read_only_hint)


def apply_tool_filter(server) -> list[str]:
    """Remove tools not selected by the ``FORGE_TOOLS`` env var; return the removed names.

    The value is a comma/space-separated list of category names (``create``,
    ``modify``, ``edit``, ``utilities``, ``capture``, ``blendfile``, ``geometry``,
    ``io``, ``docs``, ``skill``) or tool-name substrings. The special token ``readonly`` restricts
    the result to tools annotated read-only. Unset / empty keeps everything;
    invalid specifications raise instead of silently exposing every tool.
    """
    spec = os.environ.get("FORGE_TOOLS", "").strip()
    if not spec:
        return []
    manager = server._tool_manager
    names = list(manager._tools)

    keep: set[str] = set()
    readonly_only = False
    for token in spec.replace(",", " ").split():
        token = token.lower()
        category = _CATEGORY_ALIASES.get(token, token)
        if category == "readonly":
            readonly_only = True
        elif category in _CATEGORIES:
            keep |= {n for n in names if n.startswith(_CATEGORIES[category])}
        else:
            keep |= {n for n in names if token in n}

    if readonly_only:
        read_only = {n for n in names if _tool_read_only(manager, n)}
        keep = read_only if not keep else keep & read_only

    # Skills are the contract for Blender operations and must remain discoverable
    # whenever an operation category is exposed.
    if getattr(server, "_forge_enforce_skill", False) and any(name != "forge_skill" for name in keep):
        keep.add("forge_skill")

    if not keep:
        raise ValueError(f"FORGE_TOOLS={spec!r} matched no tools")

    removed = [n for n in names if n not in keep]
    for name in removed:
        manager.remove_tool(name)
    return removed
