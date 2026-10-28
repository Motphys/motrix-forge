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

"""
Selection and type-checking utilities for forge objects.

Extracted from forge_function.py to reduce file size and consolidate
duplicate poll-function definitions.
"""

import bpy
from bpy.types import Context

from . import constants as cons

# ── Poll helpers (used by PropertyGroup PointerProperty fields) ──────


def link_only_poll(self, obj):
    """Return True only for objects with Forge_Model_Type == LINK.

    Args:
        self: The owner of the PointerProperty (unused).
        obj: The object being considered for the pointer assignment.

    Returns:
        True if *obj* is a link model, False otherwise.
    """

    return obj.Forge_Model_Type == cons.ModelTypes.LINK


def instance_link_only_poll(self, obj):
    """Return True only for LINK objects marked as an instance link.

    Args:
        self: The owner of the PointerProperty (unused).
        obj: The object being considered for the pointer assignment.

    Returns:
        True if *obj* is a link model carrying the INSTANCE_LINK mark.
    """

    return obj.Forge_Model_Type == cons.ModelTypes.LINK and bool(obj.get("INSTANCE_LINK"))


def joint_only_poll(self, obj):
    """Return True only for objects with Forge_Model_Type == JOINT.

    Args:
        self: The owner of the PointerProperty (unused).
        obj: The object being considered for the pointer assignment.

    Returns:
        True if *obj* is a joint model, False otherwise.
    """

    return obj.Forge_Model_Type == cons.ModelTypes.JOINT


def tendon_only_poll(self, obj):
    """Return True only for objects with Forge_Model_Type == TENDON.

    Args:
        self: The owner of the PointerProperty (unused).
        obj: The object being considered for the pointer assignment.

    Returns:
        True if *obj* is a tendon model, False otherwise.
    """

    return obj.Forge_Model_Type == cons.ModelTypes.TENDON


def site_only_poll(self, obj):
    """Return True only for objects with Forge_Model_Type == SITE.

    Args:
        self: The owner of the PointerProperty (unused).
        obj: The object being considered for the pointer assignment.

    Returns:
        True if *obj* is a site model, False otherwise.
    """

    return obj.Forge_Model_Type == cons.ModelTypes.SITE


def actuator_target_poll(self, obj):
    """Return True for objects that can be actuator targets (JOINT, TENDON, LINK, SITE).

    Args:
        self: The owner of the PointerProperty (unused).
        obj: The object being considered for the pointer assignment.

    Returns:
        True if *obj* is a joint, tendon, link, or site model.
    """

    return obj.Forge_Model_Type in (
        cons.ModelTypes.JOINT,
        cons.ModelTypes.TENDON,
        cons.ModelTypes.LINK,
        cons.ModelTypes.SITE,
    )


def tendon_target_only_poll(self, obj):
    """Return True only for SLIDE or HINGE type joints (tendon-compatible targets).

    Args:
        self: The owner of the PointerProperty (unused).
        obj: The object being considered for the pointer assignment.

    Returns:
        True if *obj* is a joint with sub-type SLIDE or HINGE.
    """

    return obj.Forge_Model_Type == cons.ModelTypes.JOINT and obj.Forge_Joint.type in (
        cons.JointTypes.SLIDE,
        cons.JointTypes.HINGE,
    )


# ── General selection helpers ────────────────────────────────────────


def clear_select():
    """Deselect all objects and clear the active object in the current view layer."""

    for obj in list(bpy.context.selected_objects):
        obj.select_set(False)
    bpy.context.view_layer.objects.active = None


def get_ordered_selection_objects(context: Context):
    """Return selected objects sorted by their ``selection_order`` custom property.

    Objects without a ``selection_order`` property (or with a negative value)
    are excluded from the result.

    Args:
        context: The active Blender context.

    Returns:
        Sorted list of selected objects that have a valid ``selection_order``.
    """

    tagged_objects = []
    untagged_objects = []
    for o in context.selected_objects:
        order_index = o.get("selected_order", -1)
        if order_index >= 0:
            tagged_objects.append((order_index, o))
        else:
            untagged_objects.append(o)
    tagged_objects = sorted(tagged_objects, key=lambda item: item[0])
    return [o for _, o in tagged_objects] + untagged_objects


# ── Type checks ──────────────────────────────────────────────────────


def check_selected_object_types(context: Context, target_type: list[str], exclude_active: bool = False):
    """Check that every selected object is one of *target_type* Blender types.

    Args:
        context: The active Blender context.
        target_type: List of acceptable Blender type strings (e.g. ``["MESH", "ARMATURE"]``).
        exclude_active: If True, skip the active object (default False).

    Returns:
        True if every selected object (excluding active when requested) matches
        one of the given types; False otherwise.
    """

    selected = context.selected_objects
    if not selected:
        return False
    roles = set()
    for obj in selected:
        if exclude_active and obj == context.active_object:
            continue
        roles.add("===" if obj.type in target_type else "---")
    return roles == {"==="}


def check_have_model_types_in_selected(context: Context, target_type: list[str], exclude_active: bool = False):
    """Return True if **any** selected object has one of *target_type* Forge_Model_Type.

    Args:
        context: The active Blender context.
        target_type: List of acceptable Forge_Model_Type strings (e.g. ``["JOINT", "LINK"]``).
        exclude_active: If True, skip the active object (default False).

    Returns:
        True if at least one selected object has a matching Forge_Model_Type.
    """

    selected = context.selected_objects
    if not selected:
        return False
    for obj in selected:
        if exclude_active and obj == context.active_object:
            continue
        if obj.Forge_Model_Type in target_type:
            return True
    return False


def check_selected_model_types(context: Context, target_type: list[str], exclude_active: bool = False):
    """Check that every selected object has one of *target_type* Forge_Model_Type.

    Args:
        context: The active Blender context.
        target_type: List of acceptable Forge_Model_Type strings.
        exclude_active: If True, skip the active object (default False).

    Returns:
        True if every selected object has a matching Forge_Model_Type.
    """

    selected = context.selected_objects
    if not selected:
        return False
    roles = set()
    for obj in selected:
        if exclude_active and obj == context.active_object:
            continue
        roles.add("===" if obj.Forge_Model_Type in target_type else "---")
    return roles == {"==="}


def check_joint_sub_types(context: Context, prop: str, target_type: list[str], exclude_active: bool = False):
    """Check that every selected object's joint *prop* is in *target_type*.

    Args:
        context: The active Blender context.
        prop: Name of the attribute on ``Forge_Joint`` to inspect (e.g. ``"type"``).
        target_type: List of acceptable values for the given property.
        exclude_active: If True, skip the active object (default False).

    Returns:
        True if every selected object's joint property matches one of the
        given values; False otherwise.
    """

    selected = context.selected_objects
    roles = set()
    for obj in selected:
        if exclude_active and obj == context.active_object:
            continue
        attr = getattr(obj.Forge_Joint, prop)
        roles.add("===" if attr in target_type else "---")
    return roles == {"==="}


def get_selected_objects_ordered():
    """Return all objects with a ``selected_order`` property, sorted by order.

    Returns:
        List of objects sorted by their ``selected_order`` value.
    """
    tagged_objects = []
    for o in bpy.data.objects:
        order_index = o.get("selected_order", -1)
        if order_index >= 0:
            tagged_objects.append((order_index, o))
    tagged_objects = sorted(tagged_objects, key=lambda item: item[0])
    return [o for i, o in tagged_objects]


def clear_order_flag(obj):
    """Remove the ``selected_order`` custom property from *obj*.

    Args:
        obj: The Blender object to clear the property from.
    """
    try:
        del obj["selected_order"]
    except KeyError:
        pass


def update_selection_order():
    """Update ``selected_order`` properties to reflect current selection state.

    Clears properties from deselected objects and assigns order indices
    to newly selected objects.
    """
    if not bpy.context.selected_objects:
        for o in bpy.data.objects:
            clear_order_flag(o)
        return
    selection_order = get_selected_objects_ordered()
    idx = 0
    for o in list(selection_order):
        if not o.select_get():
            selection_order.remove(o)
            clear_order_flag(o)
        else:
            o["selected_order"] = idx

            idx += 1
    for o in bpy.context.selected_objects:
        if o not in selection_order:
            o["selected_order"] = len(selection_order)
            selection_order.append(o)
