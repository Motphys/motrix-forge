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
Utility / helper operators.

Each class provides general-purpose functionality (rename, select, …).
Registered via ``forge_operator.classes``.
"""

from __future__ import annotations

import re

import bpy
from bpy.props import StringProperty
from bpy.types import Context, Operator

from .. import settings
from ..core import constants as cons
from ..core import function as funcs
from ..core import selection as sel
from ..core.props import Forge_Props

# ═══════════════════════════════════════════════════════════════════════
# Batch Rename
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Batch_Rename(Operator):
    """Batch rename selected objects with prefix and numbering."""

    bl_idname = "forge.batch_rename"
    bl_label = "Batch Rename"
    bl_options = {"REGISTER", "UNDO"}

    new_name: StringProperty(name="New Name", default="")  # type: ignore
    numerate: StringProperty(name="Numerate", default="###")  # type: ignore

    def execute(self, context: Context):
        """Execute the operator, renaming selected objects with prefix and numbering."""
        digits = len(self.numerate)
        i = 0
        for obj in context.selected_objects:
            obj.name = self.new_name + "_" + ("{num:{fill}{width}}".format(num=i, fill="0", width=digits))
            i += 1
        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected objects."""
        return context.selected_objects

    def draw(self, context: Context):
        """Draw operator UI elements for name prefix and numbering format."""
        layout = self.layout

        box = layout.box()
        col = box.column(align=True)

        row = col.row(align=True)
        split = row.split(factor=0.75, align=True)
        split.prop(self, "new_name", text="name")
        split.prop(self, "numerate", text="")

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the batch rename dialog."""
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Instance Set
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Instance_Mark(Operator):
    """Toggle the instance-link mark on selected link objects."""

    bl_idname = "forge.mark_instance_link"
    bl_label = "Mark Instance Link"
    bl_description = (
        "Mark selected link(s) as instance link: it exports only asset data and its children"
        " are written under every INSTANCE_IDNAME link. Run again to unmark"
    )
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link objects."""
        return sel.check_selected_model_types(context, [cons.ModelTypes.LINK])

    def execute(self, context: Context):
        """Toggle the INSTANCE_LINK mark on every selected link object."""
        marked = 0
        unmarked = 0
        for obj in context.selected_objects:
            if obj.Forge_Model_Type != cons.ModelTypes.LINK:
                self.report({"WARNING"}, f"{obj.name} is not a LINK")
                continue
            if "INSTANCE_LINK" in obj:
                del obj["INSTANCE_LINK"]
                unmarked += 1
            else:
                obj["INSTANCE_LINK"] = True
                marked += 1
        if marked:
            self.report({"INFO"}, f"Instance link marked on {marked} link(s)")
        elif unmarked:
            self.report({"INFO"}, f"Instance link unmarked on {unmarked} link(s)")
        funcs.update_ui(context)
        return {"FINISHED"}


class Forge_OT_InstanceSet(Operator):
    """Set body instance ID name on selected objects."""

    bl_idname = "forge.set_instance_idname"
    bl_label = "Set instance idname"
    bl_description = "Set link instance idname only for link(s)"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected objects."""
        return sel.check_selected_model_types(
            context, [cons.ModelTypes.LINK, cons.ModelTypes.FRAME, cons.ModelTypes.VISUAL]
        )

    def execute(self, context: Context):
        """Execute the operator, setting instance ID names for selected objects."""
        funcs.set_instance_idname(context, self.report)
        return {"FINISHED"}


# ═══════════════════════════════════════════════════════════════════════
# Select By TAG / Model Type / Select Hulls
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_SelectByTAG(Operator):
    """Select objects by a special define tag in the scene."""

    bl_idname = "forge.select_by_tag"
    bl_label = "Select By Speical Define Tag"
    bl_description = "Select any Object by speical define tag in the scene"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run (only in object mode)."""
        return context.mode == "OBJECT"

    def execute(self, context: Context):
        """Execute the operator, selecting objects matching the configured tag."""
        scene = context.scene
        forge_props: Forge_Props = bpy.data.scenes[scene.Main_Scene].Forge_Props
        for obj in context.scene.objects:
            if forge_props.select_tag in obj.name:
                obj.select_set(True)

        return {"FINISHED"}


class Forge_OT_SelectByModelType(Operator):
    """Select objects matching the configured Forge model type."""

    bl_idname = "forge.select_by_model_type"
    bl_label = "Select By Model Type"
    bl_description = "Select selectable objects of the chosen Forge model type"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context: Context):
        """Only select objects in object mode."""
        return context.mode == "OBJECT"

    def execute(self, context: Context):
        """Add matching objects to the current selection."""
        scene = context.scene
        forge_props: Forge_Props = bpy.data.scenes[scene.Main_Scene].Forge_Props
        for obj in context.selectable_objects:
            if obj.Forge_Model_Type == forge_props.select_model_type:
                obj.select_set(True)
        return {"FINISHED"}


class Forge_OT_SelectHulls(Operator):
    """Select convex hull objects in the scene by name template."""

    bl_idname = "forge.select_hulls"
    bl_label = "Select Hulls"
    bl_description = "Select any convex hulls in the scene"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run (only in object mode)."""
        return context.mode == "OBJECT"

    def execute(self, context: Context):
        """Execute the operator, selecting convex hull objects based on name template."""
        prefs = settings.get_addon_prefs()
        # Headless sessions register the operators without an add-on entry, so
        # the preferences can be missing; match against the property's default
        # rather than failing to select anything.
        template = prefs.coacd_name_template if prefs else settings.DEFAULT_COACD_NAME_TEMPLATE
        pattern = re.escape(template)
        pattern = pattern.replace(r"\?", ".+?").replace(r"\#", r"\d+")
        hull_pattern = re.compile(f"^{pattern}$")
        for obj in context.scene.objects:
            if hull_pattern.fullmatch(obj.name):
                obj.select_set(True)

        return {"FINISHED"}
