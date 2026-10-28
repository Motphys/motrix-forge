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

import os

import bpy
from bpy.app.handlers import persistent
from bpy.props import PointerProperty

from . import mcp, settings
from .core import collider, inertial, props, selection
from .gizmo import gizmo
from .mcp import operator as mcp_ops
from .ops import operator
from .ui import panel, propspanel

_forge_library_created = False
_forge_library_previous_directory: str | None = None


def _bind_forge_library() -> None:
    """Ensure the Forge asset library points at this add-on's bundled assets."""
    global _forge_library_created, _forge_library_previous_directory

    expected = os.path.normcase(os.path.abspath(os.path.join(os.path.dirname(__file__), "lib", "assets")))
    libraries = bpy.context.preferences.filepaths.asset_libraries
    entry = libraries.get("Forge Library")
    if entry is None:
        libraries.new(name="Forge Library", directory=expected)
        _forge_library_created = True
        _forge_library_previous_directory = None
    else:
        # Blender 4.x exposes the configured asset-library location as
        # ``UserAssetLibrary.path`` (the old ``directory`` attribute no
        # longer exists).  Resolve it through bpy.path so relative entries
        # are compared consistently with the bundled absolute path.
        current = os.path.normcase(os.path.abspath(bpy.path.abspath(entry.path)))
        if current != expected:
            _forge_library_previous_directory = entry.path
            entry.path = expected
        _forge_library_created = False
    libraries.update()


def _unbind_forge_library() -> None:
    """Undo only the asset-library change made by this add-on instance."""
    global _forge_library_created, _forge_library_previous_directory

    libraries = bpy.context.preferences.filepaths.asset_libraries
    entry = libraries.get("Forge Library")
    if entry is not None:
        if _forge_library_created:
            libraries.remove(entry)
        elif _forge_library_previous_directory is not None:
            entry.path = _forge_library_previous_directory
    _forge_library_created = False
    _forge_library_previous_directory = None
    libraries.update()


# persistent is needed for handler to work in addons https://docs.blender.org/api/current/bpy.app.handlers.html
@persistent
def selection_change_handler(scene):
    """Handle selection changes in the depsgraph to update selection order.

    Args:
        scene: The Blender scene (unused, needed for handler signature).
    """
    if bpy.context.mode != "OBJECT":
        return

    # Any() function returns True if any element of an iterable is True. If not, it returns False.
    is_selection_update = any(
        not u.is_updated_geometry and not u.is_updated_transform and not u.is_updated_shading
        for u in bpy.context.view_layer.depsgraph.updates
    )
    if is_selection_update:
        selection.update_selection_order()


def register():
    """Register all Forge addon classes and initialize addon properties.

    Registers property groups, operators, UI panels, gizmos, MCP operators,
    and addon preferences. Also sets up the Forge Library asset directory,
    registers MJCF model properties on Blender objects, and initialises the
    MCP server state.
    """

    print("Initialling Forge ...")

    for cls in props.classes:
        bpy.utils.register_class(cls)
    for cls in mcp_ops.classes:
        bpy.utils.register_class(cls)
    for cls in panel.classes:
        bpy.utils.register_class(cls)
    for cls in propspanel.classes:
        bpy.utils.register_class(cls)
    for cls in gizmo.classes:
        bpy.utils.register_class(cls)
    for cls in operator.classes:
        bpy.utils.register_class(cls)
    for cls in settings.classes:
        bpy.utils.register_class(cls)
    bpy.types.Object.Forge_Matrix_Info = PointerProperty(type=propspanel.Forge_Object_MatrixInfo)
    props.register_forge_model_props()
    mcp.register_mcp()

    _bind_forge_library()
    settings.Load_Icon()
    _ = settings.get_addon_prefs()

    bpy.app.handlers.depsgraph_update_post.append(selection_change_handler)
    inertial.register_preview()
    collider.register_preview()
    print("""\033[1;31m
      ___  ___  ___  ___  ___
     /_   /  / /__/ / _  /_
    /    /__/ / \\  /__/ /__
    """)
    print("Initialling Forge Done\033[0m")


def unregister():
    """Unregister all Forge addon classes and clean up addon state.

    Removes the Forge Library asset directory, unregisters MJCF model
    properties, deletes the MatrixInfo pointer property, and unregisters
    all classes in reverse dependency order.
    """

    print("Unloading Forge ...")
    _unbind_forge_library()
    settings.Unload_Icon()

    mcp.unregister_mcp()
    inertial.unregister_preview()
    collider.unregister_preview()

    props.unregister_forge_model_props()
    del bpy.types.Object.Forge_Matrix_Info
    for cls in reversed(settings.classes):
        bpy.utils.unregister_class(cls)
    for cls in reversed(operator.classes):
        bpy.utils.unregister_class(cls)
    for cls in reversed(gizmo.classes):
        bpy.utils.unregister_class(cls)
    for cls in reversed(propspanel.classes):
        bpy.utils.unregister_class(cls)
    for cls in reversed(panel.classes):
        bpy.utils.unregister_class(cls)
    for cls in reversed(mcp_ops.classes):
        bpy.utils.unregister_class(cls)
    for cls in reversed(props.classes):
        bpy.utils.unregister_class(cls)

    bpy.app.handlers.depsgraph_update_post.remove(selection_change_handler)
    print("Unloading Forge Done")


if __name__ == "__main__":
    register()
