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

import bpy
from bpy.types import Collection, NodesModifier, Object, UILayout, bpy_struct


def link_collection(obj: Object, collection: Collection):
    """Move an object to a target collection.

    Removes from all current collections, then links to the target.

    Args:
        obj: The object to move.
        collection: The target collection.
    """

    for c in obj.users_collection:
        c.objects.unlink(obj)
    collection.objects.link(obj)


def get_socket(prop: str):
    """Wrap a property name into Blender node socket index format.

    Args:
        prop: The property name.

    Returns:
        Socket identity string like ``'["prop"]'``.
    """

    return f'["{prop}"]'


def ensure_shader_nodes(id_data) -> None:
    """Enable shader nodes on Blender 4.x data-blocks.

    Blender 5.x always creates a node tree and deprecated ``use_nodes``, so
    assigning it there only produces a deprecation warning.
    """

    if bpy.app.version < (5, 0, 0) and not id_data.use_nodes:
        id_data.use_nodes = True


def _modifier_input_interface(modifier: NodesModifier):
    """Return the Blender 5.2+ modifier input interface, if available.

    Blender 5.2 moved Geometry Nodes modifier socket values out of the
    ``modifier["Socket_N"]`` ID-property mapping and into
    ``modifier.properties.inputs``.  Older releases only expose the
    ID-property mapping, so callers must go through the helpers below.
    """
    properties = getattr(modifier, "properties", None)
    # The ``bpy_struct`` check keeps test doubles (e.g. ``MagicMock``) on the
    # legacy path instead of silently mirroring arbitrary attributes.
    if not isinstance(properties, bpy_struct):
        return None
    return getattr(properties, "inputs", None)


def get_modifier_socket(modifier: NodesModifier, socket: str):
    """Read a Geometry Nodes modifier input socket value.

    Works with both the legacy ID-property API (Blender 4.x/5.0-5.1) and the
    RNA interface introduced in Blender 5.2.
    """

    inputs = _modifier_input_interface(modifier)
    if inputs is not None and hasattr(inputs, socket):
        return getattr(inputs, socket).value
    return modifier[socket]


def set_modifier_socket(modifier: NodesModifier, socket: str, value) -> None:
    """Write a Geometry Nodes modifier input socket value.

    Works with both the legacy ID-property API (Blender 4.x/5.0-5.1) and the
    RNA interface introduced in Blender 5.2.
    """

    inputs = _modifier_input_interface(modifier)
    if inputs is None or not hasattr(inputs, socket):
        modifier[socket] = value
        return

    input_socket = getattr(inputs, socket)
    if isinstance(value, int) and not isinstance(value, bool):
        # Menu sockets used to store the enum index as an ID property; the
        # 5.2 RNA interface expects the enum item name instead.
        value_prop = input_socket.bl_rna.properties.get("value")
        enum_items = getattr(value_prop, "enum_items", None)
        if enum_items and 0 <= value < len(enum_items):
            value = enum_items[value].name
    input_socket.value = value


def prop_modifier_socket(layout: UILayout, modifier: NodesModifier, socket: str, *args, **kwargs) -> None:
    """Draw a Geometry Nodes modifier input socket editor in *layout*.

    Blender 5.2 exposes each socket as an RNA struct, so the editor must target
    the socket's ``value`` property directly.  ``UILayout.prop`` cannot resolve
    a nested path such as ``properties.inputs.Socket_N.value``.
    """

    inputs = _modifier_input_interface(modifier)
    if inputs is not None and hasattr(inputs, socket):
        layout.prop(getattr(inputs, socket), "value", *args, **kwargs)
    else:
        layout.prop(modifier, get_socket(socket), *args, **kwargs)
