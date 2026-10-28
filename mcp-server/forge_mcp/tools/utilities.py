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

"""Utility commands — mirror ``bpy.ops.forge.batch_rename``, selection helpers and the scene query
(see forge_mcp/skills/forge_modify.md).

Every op tool takes ``select`` (object names): selection is replaced with that
list (order matters — first becomes active) before the operator runs. ``None``
leaves the current selection untouched.
"""

from __future__ import annotations

from .. import call_blender, mcp
from ..blender import op_call
from ._hints import READ_ONLY, WRITE

# Return all objects with their Forge model type (enum name) and parent, plus
# counts per type, current selection and the blend file path.
_SCENE_INFO_CODE = """
import bpy
from collections import Counter

def model_type(obj):
    return str(getattr(obj, "Forge_Model_Type", "UNDEFINED"))


objects = [
    {"name": o.name, "type": model_type(o), "parent": o.parent.name if o.parent else None}
    for o in bpy.context.scene.objects
]
result = {
    "scene": bpy.context.scene.name,
    "blend_file": bpy.data.filepath or "(unsaved)",
    "object_count": len(objects),
    "objects_by_model_type": dict(Counter(o["type"] for o in objects)),
    "objects": sorted(objects, key=lambda o: o["name"]),
    "selected": [o.name for o in bpy.context.selected_objects],
    "active": bpy.context.active_object.name if bpy.context.active_object else None,
}
"""


@mcp.tool(annotations=READ_ONLY, name="forge_scene_info")
def scene_info() -> dict:
    """Get scene info: blend file, object count, per-type counts, every object with its Forge model type and parent,
    and current selection.
    """
    return call_blender(_SCENE_INFO_CODE)


@mcp.tool(annotations=WRITE, name="forge_batch_rename")
def batch_rename(new_name: str = "", numerate: str = "###", select: list[str] | None = None) -> dict:
    """Rename selected objects to `{new_name}_{index}`, zero-padded to `numerate` length, index starts from 0."""
    return call_blender(op_call("batch_rename", select=select, new_name=new_name, numerate=numerate))


@mcp.tool(annotations=WRITE, name="forge_set_instance_idname")
def set_instance_idname(select: list[str] | None = None) -> dict:
    """Mark selected `LINK` objects as instances of `Forge_Props.instance_body`.

    Writes `INSTANCE_IDNAME = <instance_body>` (a reference to the instance-body
    object, so the marker survives renames) on the selected links (or removes
    the marker when no instance body is set). Links already marked `INSTANCE_LINK`
    are refused. At export the instance body link is the asset-only source (marked
    `INSTANCE_LINK`, never a `<body>`); its children are written into every
    INSTANCE_IDNAME link with names prefixed by that link's name. Set the instance
    body first via `forge_set_scene_property(group="forge_props")`.
    """
    return call_blender(op_call("set_instance_idname", select=select))


@mcp.tool(annotations=WRITE, name="forge_select_by_tag")
def select_by_tag() -> dict:
    """Select objects whose name contains scene `Forge_Props.select_tag`; only in object mode.

    - **Adds** matches to the current selection instead of replacing it — deselect first to get only the matches.
      The returned `objects` list is the resulting selection, not the matched set.
    - An empty `select_tag` matches every object name (`""` is contained in any string), so it selects the whole
      scene.
    """
    return call_blender(op_call("select_by_tag"))


@mcp.tool(annotations=WRITE, name="forge_select_hulls")
def select_hulls() -> dict:
    """Select convex hull objects by name template from addon preferences (`coacd_name_template`); only in object
    mode.
    """
    return call_blender(op_call("select_hulls"))
