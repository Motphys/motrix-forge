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
Define / type-change / parenting operators.

Each class changes the type or parent of selected objects.
Registered via ``operator.classes``.
"""

from __future__ import annotations

from bpy.props import BoolProperty, EnumProperty
from bpy.types import Context, Operator

from ..core import constants as cons
from ..core import function as funcs
from ..core import selection as sel
from ..core.props import ActuatorItem, JointItem
from .base_operator import BaseDefineOperator

# ═══════════════════════════════════════════════════════════════════════
# Type Define — set Forge_Model_Type on an object
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Type_Define(Operator):
    """Define model type of selected object(s)"""

    bl_idname = "forge.define_model_type"
    bl_label = "Define model"
    bl_options = {"REGISTER", "UNDO"}

    def model_enum_items(self, context: Context):
        """Dynamically generate enum items for model type selection based on selected object type."""
        if sel.check_selected_object_types(context, [cons.ObjectTypes.EMPTY]):
            return cons.Model_Types[1:2]
        elif sel.check_selected_object_types(context, [cons.ObjectTypes.MESH]):
            return cons.Model_Types[3:5]
        elif sel.check_selected_object_types(context, [cons.ObjectTypes.LIGHT]):
            return cons.Model_Types[14:15]
        elif sel.check_selected_object_types(context, [cons.ObjectTypes.CAMERA]):
            return cons.Model_Types[15:16]
        else:
            return (("NONE", "None", ""),)

    Model_Type: EnumProperty(
        items=model_enum_items,
        name="Model Type",
        description="Model Type",
    )  # type: ignore

    def execute(self, context: Context):
        """Execute the operator, defining the model type for selected objects."""
        model_type = self.Model_Type

        unsupported = []
        if model_type == cons.ModelTypes.LIGHT:
            unsupported = [obj for obj in context.selected_objects if obj.data.type == "AREA"]
        elif model_type == cons.ModelTypes.CAMERA:
            unsupported = [obj for obj in context.selected_objects if obj.data.type not in {"ORTHO", "PERSP"}]
        if unsupported:
            self.report({"WARNING"}, f"Unsupported objects: {', '.join(obj.name for obj in unsupported)}")
            return {"CANCELLED"}

        if model_type == cons.ModelTypes.UNDEFINED:
            self.report({"WARNING"}, "Setting type 'Undefined' for selected objects.")

        for obj in context.selected_objects:
            match model_type:
                case cons.ModelTypes.VISUAL:
                    obj.Forge_Geometry.type = cons.GeometryTypes.MESH
                    obj.Forge_Geometry.group = 2
                    obj.Forge_Geometry.contype = 0
                    obj.Forge_Geometry.conaffinity = 0
                    obj.Forge_Model_Type = model_type
                    funcs.update_model_collection(context, obj)
                    funcs.update_unique_name(obj, "GEO_")

                case cons.ModelTypes.COLLIDER:
                    obj.Forge_Geometry.type = cons.GeometryTypes.MESH
                    obj.Forge_Geometry.group = 3
                    obj.Forge_Model_Type = model_type
                    obj.display_type = "WIRE"
                    funcs.update_model_collection(context, obj)
                    funcs.update_unique_name(obj, "COL_")

                case cons.ModelTypes.LINK:
                    obj.Forge_Model_Type = model_type
                    obj.show_in_front = True
                    funcs.update_model_collection(context, obj)
                    funcs.update_unique_name(obj, "LNK_")

                case cons.ModelTypes.LIGHT:
                    light_type = cons.LightTypes.DIRECTIONAL if obj.data.type == "SUN" else obj.data.type
                    funcs.set_light_props(light_type, cons.TargetModes.FIXED, obj)
                    obj.Forge_Model_Type = model_type
                    funcs.update_model_collection(context, obj)
                    funcs.update_unique_name(obj, "LIT_")

                case cons.ModelTypes.CAMERA:
                    camera_type = (
                        cons.CameraTypes.ORTHOGRAPHIC if obj.data.type == "ORTHO" else cons.CameraTypes.PERSPECTIVE
                    )
                    funcs.set_camera_props(camera_type, cons.TargetModes.FIXED, obj)
                    obj.Forge_Model_Type = model_type
                    funcs.update_model_collection(context, obj)
                    funcs.update_unique_name(obj, "CAM_")

        funcs.update_ui(context)
        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected model types."""
        return sel.check_selected_model_types(context, [cons.ModelTypes.UNDEFINED])

    def invoke(self, context: Context, event):
        """Invoke the operator, setting up initial UI state with model type dialog."""
        self.Model_Type = self.model_enum_items(context)[0][0]
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Geometry Define
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Geometry_Define(BaseDefineOperator):
    """Define geometry type of selected object(s)"""

    bl_idname = "forge.define_geometry_type"
    bl_label = "Define geometry(s)"
    poll_model_types = [cons.ModelTypes.VISUAL]

    geometry_type: EnumProperty(items=cons.Geometry_Types, name="Geometry Type", default="MESH")  # type: ignore

    type = ""

    def apply_type(self, context: Context, obj, new_type):
        """Apply the selected geometry type to the given object."""
        funcs.change_geometry(context, self.report, new_type, obj)

    def execute(self, context: Context):
        """Execute the operator, applying the geometry type to selected objects."""
        self.type = self.geometry_type
        return super().execute(context)

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the geometry type definition dialog."""
        obj = context.active_object
        if obj:
            self.geometry_type = obj.Forge_Geometry.type
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Collider Define
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Collider_Define(Operator):
    """Define collider type of selected collider(s)"""

    bl_idname = "forge.define_collider_type"
    bl_label = "Define collider(s)"
    bl_options = {"REGISTER", "UNDO"}

    apply_to_all: BoolProperty(
        name="Apply to all selected",
        default=False,
        description="Default only apply to active collider, Enable to apply to all select collider",
    )  # type: ignore
    collider_type: EnumProperty(
        items=cons.Collider_Types,
        name="Collider Type",
        default="SPHERE",
        description="Collider Type",
    )  # type: ignore

    def execute(self, context: Context):
        """Execute the operator, changing the collider type of selected objects."""
        if self.apply_to_all:
            objs = [obj for obj in context.selected_objects]
            for obj in objs:
                sel.clear_select()
                obj.select_set(True)
                context.view_layer.objects.active = obj
                funcs.change_collider(context, self.report, self.collider_type, obj)
            for obj in objs:
                obj.select_set(True)
        else:
            obj = context.active_object
            if obj is None:
                self.report({"WARNING"}, "No active collider selected")
                return {"CANCELLED"}
            obj.select_set(True)
            context.view_layer.objects.active = obj
            funcs.change_collider(context, self.report, self.collider_type, obj)
        funcs.update_ui(context)
        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected collider objects."""
        return sel.check_selected_model_types(context, [cons.ModelTypes.COLLIDER])

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the collider type definition dialog."""
        obj = context.active_object
        if obj:
            self.collider_type = obj.Forge_Geometry.type

        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Site Define
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Site_Define(BaseDefineOperator):
    """Define site type of selected site(s)"""

    bl_idname = "forge.define_site_type"
    bl_label = "Define site(s)"
    poll_model_types = [cons.ModelTypes.SITE]

    site_type: EnumProperty(items=cons.Site_Types, name="Site Type", default="SPHERE")  # type: ignore

    type = ""

    def apply_type(self, context: Context, obj, new_type):
        """Apply the selected site type to the given object."""
        funcs.change_site(context, self.report, new_type, obj)

    def execute(self, context: Context):
        """Execute the operator, applying the site type to selected objects."""
        self.type = self.site_type
        return super().execute(context)

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the site type definition dialog."""
        obj = context.active_object
        if obj:
            self.site_type = obj.Forge_Geometry.type
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Joint Define
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Joint_Define(BaseDefineOperator):
    """Define joint type of selected joint(s)"""

    bl_idname = "forge.define_joint_type"
    bl_label = "Define joint(s)"
    poll_model_types = [cons.ModelTypes.JOINT]

    joint_type: EnumProperty(items=cons.Joint_Types, name="Joint Type", default="HINGE")  # type: ignore

    type = ""

    def apply_type(self, context: Context, obj, new_type):
        """Apply the selected joint type to the given object and update its shape."""
        data: JointItem = obj.Forge_Joint
        data.type = new_type
        funcs.set_joint_shape(context, new_type, obj)

    def execute(self, context: Context):
        """Execute the operator, applying the joint type to selected objects."""
        self.type = self.joint_type
        return super().execute(context)

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the joint type definition dialog."""
        obj = context.active_object
        if obj:
            self.joint_type = obj.Forge_Joint.type
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Actuator Define
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Actuator_Define(BaseDefineOperator):
    """Define actuator type of selected actuator(s)"""

    bl_idname = "forge.define_actuator_type"
    bl_label = "Define actuator(s)"
    poll_model_types = [cons.ModelTypes.ACTUATOR]

    actuator_type: EnumProperty(items=cons.Actuator_Types, name="Actuator Type", default="POSITION")  # type: ignore

    type = ""

    def apply_type(self, context: Context, obj, new_type):
        """Apply the selected actuator type to the given object."""
        data: ActuatorItem = obj.Forge_Actuator
        data.type = new_type

    def execute(self, context: Context):
        """Execute the operator, applying the actuator type to selected objects."""
        self.type = self.actuator_type
        return super().execute(context)

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the actuator type definition dialog."""
        obj = context.active_object
        if obj:
            self.actuator_type = obj.Forge_Actuator.type
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Parent Define
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Parent_Define(Operator):
    """Change parent of selected objects to active object (last selected):
    1. Parent selected objects to the active link, frame or replicate.
    2. Move every reparented object into the collection of its model type.
    3. A visual can not be a parent: a collider under a visual is not exported."""

    bl_idname = "forge.define_parent"
    bl_label = "Link Parent"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context: Context):
        """Execute the operator, reparenting selected objects to the active object."""
        for obj in context.selected_objects:
            if obj == context.active_object:
                continue
            if obj.Forge_Model_Type == cons.ModelTypes.VISUAL:
                # Lift the visual's children first: the exporter never descends into a
                # visual, so anything left inside one is dropped from the MJCF.
                for cobj in obj.children:
                    funcs.link_parent(context, cobj, context.active_object)
                    funcs.update_model_collection(context, cobj)
            if "Root Link" in obj:
                del obj["Root Link"]
            funcs.link_parent(context, obj, context.active_object)
            funcs.update_model_collection(context, obj)

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected objects and active object type."""
        if context.active_object is None:
            return False

        if len(context.selected_objects) == 0:
            return False

        if context.active_object.Forge_Model_Type == cons.ModelTypes.VISUAL:
            cls.poll_message_set(
                "A visual can not be a parent: a collider under a visual is not exported,"
                " parent the collider to the link instead"
            )
            return False
        elif context.active_object.Forge_Model_Type in [
            cons.ModelTypes.LINK,
            cons.ModelTypes.FRAME,
            cons.ModelTypes.REPLICATE,
        ]:
            if sel.check_selected_model_types(context, cons.Link_Child_Type_List, True):
                return True
            else:
                return False
        else:
            return False
