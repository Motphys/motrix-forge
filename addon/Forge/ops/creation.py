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
Element-creation operators.

Each class creates one or more MJCF model elements from selected objects
or from scratch.  Registered via ``operator.classes``.
"""

from __future__ import annotations

import bpy
from bpy.props import BoolProperty, EnumProperty, FloatProperty, FloatVectorProperty, IntProperty, StringProperty
from bpy.types import Context, Object, Operator

from ..core import constants as cons
from ..core import function as funcs
from ..core import props_data as def_props
from ..core import selection as sel
from .base_operator import BaseCreationOperator
from .inertia import compute_inertia
from .mesh_check import check_mesh

# ═══════════════════════════════════════════════════════════════════════
# Geometry
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Geometry_Creation(Operator):
    """Create geometry by selected type, optionally based on selected existing object(s)"""

    bl_idname = "forge.create_geometry"
    bl_label = "Create geometry(s)"
    bl_options = {"REGISTER", "UNDO"}

    geometry_type: EnumProperty(
        items=cons.Site_Types,
        name="Geometry Type",
        default="BOX",
        description="Geometry Type",
    )  # type: ignore

    # ── Size properties ─────────────────────────────────────────────────
    size_box: FloatVectorProperty(
        name="Size", default=(1.0, 1.0, 1.0), size=3, min=0.001, precision=5, subtype="TRANSLATION"
    )  # type: ignore
    size_radius: FloatProperty(name="Radius", default=0.5, min=0.001, precision=5, subtype="DISTANCE")  # type: ignore
    size_height: FloatProperty(name="Height", default=1.0, min=0.001, precision=5, subtype="DISTANCE")  # type: ignore

    def draw(self, context: Context):
        """Draw operator UI elements for geometry type and size selection."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        box = layout.box()
        col = box.column(align=True)
        col.prop(self, "geometry_type")
        col.separator()

        gt = self.geometry_type
        if gt == cons.GeometryTypes.BOX:
            col.prop(self, "size_box")
        elif gt == cons.GeometryTypes.SPHERE:
            col.prop(self, "size_radius")
        else:
            col.prop(self, "size_radius")
            col.prop(self, "size_height")

    def _get_size(self):
        """Build (size_value, based_on_dimensions) from the active type + user input."""
        from mathutils import Vector

        match self.geometry_type:
            case cons.GeometryTypes.BOX:
                return self.size_box, True
            case cons.GeometryTypes.SPHERE:
                return self.size_radius, False
            case cons.GeometryTypes.CAPSULE | cons.GeometryTypes.CYLINDER:
                return Vector((self.size_radius, self.size_height * 0.5)), False
        return None, True

    def execute(self, context: Context):
        """Execute the operator, creating geometry objects based on selected type."""
        size, based_on = self._get_size()

        coll_tag = cons.CollectionNames.VISUAL if context.selected_objects else cons.CollectionNames.WORLD
        collection = funcs.get_collection(context, coll_tag)

        if context.selected_objects:
            objs = [obj for obj in context.selected_objects]
            new_objs = []
            for obj in objs:
                sel.clear_select()
                new_objs.append(
                    funcs.add_geometry(
                        context,
                        self.report,
                        collection,
                        self.geometry_type,
                        obj,
                        size=size,
                        based_on_dimensions=based_on,
                    )
                )
            for obj in new_objs:
                obj.select_set(True)
        else:
            sel.clear_select()
            new_obj: Object = funcs.add_geometry(
                context, self.report, collection, self.geometry_type, size=size, based_on_dimensions=based_on
            )
            new_obj.select_set(True)
        # funcs.update_ui(context)
        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link, frame, replicate, or no selection."""
        return (
            sel.check_selected_model_types(
                context, [cons.ModelTypes.LINK, cons.ModelTypes.FRAME, cons.ModelTypes.REPLICATE]
            )
            or len(context.selected_objects) == 0
        )

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the geometry creation dialog."""
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Collider
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Collider_Creation(Operator):
    """Create collider for selected geometry(s)"""

    bl_idname = "forge.create_collider"
    bl_label = "Create collider(s)"
    bl_options = {"REGISTER", "UNDO"}

    def type_enum_items(self, context: Context):
        if context.selected_objects and sel.check_selected_model_types(context, [cons.ModelTypes.VISUAL]):
            return cons.Collider_Types
        else:
            return cons.Site_Types

    collider_type: EnumProperty(
        items=type_enum_items,
        name="Collider Type",
        default=0,
        description="Collider Type",
    )  # type: ignore

    create_method: EnumProperty(
        items=cons.Create_Collider_Method,
        name="Method",
        default="COLLIDER_TYPE",
        description="Collider create method",
    )  # type: ignore

    auto_size: BoolProperty(
        name="Auto size",
        default=False,
        description="Automatic calculate size by selected visual object",
    )  # type: ignore

    use_min_as_height: BoolProperty(
        name="Use Min As Height",
        default=False,
        description="Use min axis as capsule and cylinder height",
    )  # type: ignore

    # ── Size properties ─────────────────────────────────────────────────
    size_box: FloatVectorProperty(
        name="Size", default=(1.0, 1.0, 1.0), size=3, min=0.001, precision=5, subtype="TRANSLATION"
    )  # type: ignore
    size_radius: FloatProperty(name="Radius", default=0.5, min=0.001, precision=5, subtype="DISTANCE")  # type: ignore
    size_height: FloatProperty(name="Height", default=1.0, min=0.001, precision=5, subtype="DISTANCE")  # type: ignore

    def _draw_size(self, gt: str):
        """Draw size input fields for the given geometry type."""
        if gt in cons.MeshGeometryTypes:
            return

        layout = self.layout

        box = layout.box()
        col = box.column(align=True)
        col.separator()

        if gt == cons.GeometryTypes.BOX:
            col.prop(self, "size_box")
        elif gt == cons.GeometryTypes.SPHERE:
            col.prop(self, "size_radius")
        else:
            col.prop(self, "size_radius")
            col.prop(self, "size_height")

    def draw(self, context: Context):
        """Draw operator UI elements for collider type, method, and size selection."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        box = layout.box()
        col = box.column(align=True)
        if context.selected_objects:
            if sel.check_selected_model_types(
                context, [cons.ModelTypes.LINK, cons.ModelTypes.FRAME, cons.ModelTypes.REPLICATE]
            ):
                col.label(text="None visual geometry selected create single collider by type")
                col.prop(self, "collider_type", text="Type")
                self.create_method = cons.CreateColliderMethod.COLLIDER_TYPE
                self._draw_size(self.collider_type)
            else:
                col.prop(self, "create_method")
                if self.create_method == cons.CreateColliderMethod.COLLIDER_TYPE:
                    col.prop(self, "collider_type", text="Type")
                    if self.collider_type not in cons.MeshGeometryTypes:
                        col.prop(self, "auto_size")
                    if self.collider_type in [cons.GeometryTypes.CAPSULE, cons.GeometryTypes.CYLINDER]:
                        col.prop(self, "use_min_as_height")
                    if not self.auto_size:
                        self._draw_size(self.collider_type)
        else:
            col.label(text="None visual geometry selected create single collider by type")
            col.prop(self, "collider_type", text="Type")
            self._draw_size(self.collider_type)

    def _get_size(self, gt: str):
        """Build (size_value, based_on_dimensions) from the active type + user input."""
        from mathutils import Vector

        match gt:
            case cons.GeometryTypes.BOX:
                return self.size_box, True
            case cons.GeometryTypes.SPHERE:
                return self.size_radius, False
            case cons.GeometryTypes.CAPSULE | cons.GeometryTypes.CYLINDER:
                return Vector((self.size_radius, self.size_height * 0.5)), False
        return None, True

    def execute(self, context: Context):
        """Execute the operator, creating collider objects for selected geometry."""
        funcs.update_ui(context)

        coll_tag = cons.CollectionNames.COLLIDER if context.selected_objects else cons.CollectionNames.WORLD
        collection = funcs.get_collection(context, coll_tag)
        collider_type = self.collider_type
        if context.selected_objects:
            objs = [obj for obj in context.selected_objects]
            new_objs = []
            if self.create_method == cons.CreateColliderMethod.COLLIDER_TYPE:
                size, based_on = (None, True) if self.auto_size else self._get_size(collider_type)
                for obj in objs:
                    sel.clear_select()
                    new_objs.append(
                        funcs.add_collider(
                            context, self.report, collection, collider_type, obj, based_on, size, self.use_min_as_height
                        )
                    )
            else:
                for obj in objs:
                    sel.clear_select()
                    gt = obj.Forge_Geometry.type
                    new_objs.append(funcs.add_collider(context, self.report, collection, gt, obj))
            for obj in new_objs:
                obj.select_set(True)
        else:
            sel.clear_select()
            size, based_on = self._get_size(collider_type)
            new_obj: Object = funcs.add_collider(
                context, self.report, collection, collider_type, size=size, based_on_dimensions=based_on
            )
            new_obj.select_set(True)

        funcs.update_ui(context)
        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link, frame, visual, or no selection."""
        return (
            sel.check_selected_model_types(context, [cons.ModelTypes.LINK, cons.ModelTypes.FRAME])
            or sel.check_selected_model_types(context, [cons.ModelTypes.VISUAL])
            or len(context.selected_objects) == 0
        )

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the collider creation dialog."""
        if self.properties.get("collider_type", 0) >= len(self.type_enum_items(context)):
            # Reset an out-of-range stored ID before reading the dynamic enum.
            self.properties["collider_type"] = 0
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# HeightField / Plane (scene-level elements)
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_HeightField_Creation(BaseCreationOperator):
    """Create height field"""

    bl_idname = "forge.create_height_field"
    bl_label = "Create height field"
    collection_tag = cons.CollectionNames.WORLD

    def create_single(self, context: Context, report, collection, parent_obj):
        """Create a single height field instance."""
        return funcs.add_height_field(context, report, collection)

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run (only when nothing is selected)."""
        return not context.selected_objects


class Forge_OT_Plane_Creation(BaseCreationOperator):
    """Create plane"""

    bl_idname = "forge.create_plane"
    bl_label = "Create plane"
    collection_tag = cons.CollectionNames.WORLD

    def create_single(self, context: Context, report, collection, parent_obj):
        """Create a single plane instance."""
        return funcs.add_plane(context, report, collection)

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run (only when nothing is selected)."""
        return not context.selected_objects


# ═══════════════════════════════════════════════════════════════════════
# Site
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Site_Creation(BaseCreationOperator):
    """Create site(s), based on selected existing link(s)"""

    bl_idname = "forge.create_site"
    bl_label = "Create site(s)"
    collection_tag = cons.CollectionNames.SITE
    show_dialog = True

    site_type: EnumProperty(items=cons.Site_Types, name="Site Type", default="SPHERE")  # type: ignore

    # ── Size properties ─────────────────────────────────────────────────
    size_box: FloatVectorProperty(
        name="Size", default=(0.2, 0.2, 0.2), size=3, min=0.001, precision=5, subtype="TRANSLATION"
    )  # type: ignore
    size_radius: FloatProperty(name="Radius", default=0.1, min=0.001, precision=5, subtype="DISTANCE")  # type: ignore
    size_height: FloatProperty(name="Height", default=0.2, min=0.001, precision=5, subtype="DISTANCE")  # type: ignore

    def draw(self, context: Context):
        """Draw operator UI elements for site type and size selection."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        box = layout.box()
        col = box.column(align=True)
        col.prop(self, "site_type")
        col.separator()

        gt = self.site_type
        if gt == cons.GeometryTypes.BOX:
            col.prop(self, "size_box")
        elif gt == cons.GeometryTypes.SPHERE:
            col.prop(self, "size_radius")
        else:
            col.prop(self, "size_radius")
            col.prop(self, "size_height")

    def _get_size(self):
        """Build (size_value, based_on_dimensions) from the active type + user input."""
        from mathutils import Vector

        match self.site_type:
            case cons.GeometryTypes.BOX:
                return self.size_box, True
            case cons.GeometryTypes.SPHERE:
                return self.size_radius, False
            case cons.GeometryTypes.CAPSULE | cons.GeometryTypes.CYLINDER:
                return Vector((self.size_radius, self.size_height * 0.5)), False
        return None, True

    def create_single(self, context: Context, report, collection, parent_obj):
        """Create a single site instance on the given parent object."""
        size, based_on = self._get_size()
        return funcs.add_site(
            context, report, collection, self.site_type, parent_obj, size=size, based_on_dimensions=based_on
        )

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link objects."""
        return sel.check_selected_model_types(context, [cons.ModelTypes.LINK])


# ═══════════════════════════════════════════════════════════════════════
# Link
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Link_Creation(BaseCreationOperator):
    """Create link(s), optionally based on selected existing object(s)
    Shift + Click will use Link as parent"""

    bl_idname = "forge.create_link"
    bl_label = "Create link(s)"

    reverse_parent: bool = False

    def create_single(self, context: Context, report, collection, parent_obj):
        """Create a single link instance on the given parent object."""
        return funcs.add_link(context, report, collection, parent_obj, self.reverse_parent)

    # collection depends on selection state → computed in execute
    collection_tag = ""

    def execute(self, context: Context):
        """Execute the operator, creating link objects and setting the collection tag."""
        self.collection_tag = cons.CollectionNames.LINK if context.selected_objects else cons.CollectionNames.WORLD
        return super().execute(context)

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link, frame, visual, collider, or no selection."""
        return (
            sel.check_selected_model_types(
                context, [cons.ModelTypes.LINK, cons.ModelTypes.FRAME, cons.ModelTypes.REPLICATE]
            )
            or sel.check_selected_model_types(context, [cons.ModelTypes.VISUAL, cons.ModelTypes.COLLIDER])
            or not context.selected_objects
        )

    def invoke(self, context: Context, event):
        """Invoke the operator, checking for shift-click to toggle reverse parent mode."""
        if event.shift:
            self.reverse_parent = True

        return self.execute(context)


# ═══════════════════════════════════════════════════════════════════════
# Joint
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Joint_Creation(BaseCreationOperator):
    """Create joint(s), based on selected existing link(s)"""

    bl_idname = "forge.create_joint"
    bl_label = "Create joint(s)"
    collection_tag = cons.CollectionNames.JOINT
    show_dialog = True

    joint_type: EnumProperty(items=cons.Joint_Types, name="Joint Type", default="HINGE")  # type: ignore

    def create_single(self, context: Context, report, collection, parent_obj):
        """Create a single joint instance on the given parent object."""
        return funcs.add_joint(context, report, collection, self.joint_type, parent_obj)

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link objects."""
        return sel.check_selected_model_types(context, [cons.ModelTypes.LINK])


# ═══════════════════════════════════════════════════════════════════════
# Actuator
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Actuator_Creation(BaseCreationOperator):
    """Create actuator(s), based on selected existing link(s) | joint(s) | tendon(s)"""

    bl_idname = "forge.create_actuator"
    bl_label = "Create actuator(s)"
    collection_tag = cons.CollectionNames.ACTUATOR
    show_dialog = True

    actuator_type: EnumProperty(items=cons.Actuator_Types, name="Actuator Type", default="POSITION")  # type: ignore

    def create_single(self, context: Context, report, collection, parent_obj):
        """Create a single actuator instance on the given parent object."""
        return funcs.add_actuator(context, report, collection, self.actuator_type, parent_obj)

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link, joint, or tendon objects."""
        return sel.check_selected_model_types(
            context, [cons.ModelTypes.LINK, cons.ModelTypes.JOINT, cons.ModelTypes.TENDON]
        )


# ═══════════════════════════════════════════════════════════════════════
# Tendon
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Tendon_Creation(BaseCreationOperator):
    """Create tendon, based on selected existing joint(s), curent only support fixed tendon"""

    bl_idname = "forge.create_tendon"
    bl_label = "Create tendon"
    collection_tag = cons.CollectionNames.TENDON
    show_dialog = True

    tendon_type: EnumProperty(items=cons.Tendon_Types, name="Tendon Type", default="FIXED")  # type: ignore

    def execute(self, context: Context):
        """Execute the operator, creating a tendon from selected joints."""
        collection = funcs.get_collection(context, self.collection_tag)
        if context.selected_objects:
            objs = sel.get_ordered_selection_objects(context)
            sel.clear_select()
            new_obj = funcs.add_tendon(context, self.report, collection, self.tendon_type, objs)
            if new_obj:
                new_obj.select_set(True)
            funcs.update_ui(context)
            return {"FINISHED"}
        else:
            return {"CANCELLED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected joints with valid subtypes."""
        if len(context.selected_objects) < 2:
            return False
        if not sel.check_selected_model_types(context, [cons.ModelTypes.JOINT]):
            return False
        return sel.check_joint_sub_types(context, "type", [cons.JointTypes.SLIDE, cons.JointTypes.HINGE])


# ═══════════════════════════════════════════════════════════════════════
# Equality
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Equality_Creation(Operator):
    """Create equality, based on selected existing link(s) | joint(s) | site(s)"""

    bl_idname = "forge.create_equality"
    bl_label = "Create equality"
    bl_options = {"REGISTER", "UNDO"}

    def type_enum_items(self, context: Context):
        if context.selected_objects and sel.check_selected_model_types(context, [cons.ModelTypes.JOINT]):
            return cons.Equality_Types[-1:]
        else:
            return cons.Equality_Types[0:2]

    equality_type: EnumProperty(
        items=type_enum_items,
        name="Equality Type",
        default=0,
        description="Equality Type",
    )  # type: ignore

    def draw(self, context: Context):
        """Draw operator UI elements for equality type selection."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column(align=True)
        col.prop(self, "equality_type")

    def execute(self, context: Context):
        """Execute the operator, creating an equality constraint from selected objects."""
        collection = funcs.get_collection(context, cons.CollectionNames.EQUALITY)

        if context.selected_objects:
            equality_type = self.equality_type
            objs = sel.get_ordered_selection_objects(context)
            new_objs = []
            sel.clear_select()
            new_objs.append(funcs.add_equality(context, self.report, collection, equality_type, objs))
            for obj in new_objs:
                obj.select_set(True)
            funcs.update_ui(context)
            return {"FINISHED"}
        else:
            return {"CANCELLED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on exactly 2 selected objects of supported types."""
        if len(context.selected_objects) != 2:
            return False
        if sel.check_selected_model_types(context, [cons.ModelTypes.LINK]):
            return True
        elif sel.check_selected_model_types(context, [cons.ModelTypes.JOINT]):
            return True
        elif sel.check_selected_model_types(context, [cons.ModelTypes.SITE]):
            return True
        else:
            return False

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the equality creation dialog."""
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Sensor
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Sensor_Creation(Operator):
    """Create sensor(s), based on selected existing link(s) | joint(s) | site(s) | geom(s) | camera(s)"""

    bl_idname = "forge.create_sensor"
    bl_label = "Create sensor(s)"
    bl_options = {"REGISTER", "UNDO"}

    def sensor_enum_items(self, context: Context):
        """Generate enum items for sensor type selection based on selected object types."""
        range_ = []
        if sel.check_selected_model_types(context, [cons.ModelTypes.LINK]):
            if self.set_subtree:
                range_ = [13, 14]
            else:
                key = (
                    "REF"
                    if self.set_ref
                    else cons.SensorTargetTypes.XBODY
                    if self.set_xbody
                    else cons.SensorTargetTypes.BODY
                )
                range_ = cons.Sensor_Target_Type_Range[key].copy()
                if self.set_ref and self.set_xbody:
                    range_[1] -= 1
        elif sel.check_selected_model_types(context, [cons.ModelTypes.JOINT]):
            range_ = cons.Sensor_Target_Type_Range[cons.SensorTargetTypes.JOINT].copy()
        elif sel.check_selected_model_types(context, [cons.ModelTypes.SITE]):
            key = "REF" if self.set_ref else cons.SensorTargetTypes.SITE
            range_ = cons.Sensor_Target_Type_Range[key].copy()
            if self.set_ref:
                range_[1] -= 1
        elif sel.check_selected_model_types(context, [cons.ModelTypes.VISUAL, cons.ModelTypes.COLLIDER]):
            key = "REF" if self.set_ref else cons.SensorTargetTypes.GEOM
            range_ = cons.Sensor_Target_Type_Range[key].copy()
        elif sel.check_selected_model_types(context, [cons.ModelTypes.CAMERA]):
            range_ = cons.Sensor_Target_Type_Range[cons.SensorTargetTypes.CAMERA].copy()
        elif sel.check_selected_model_types(
            context,
            [
                cons.ModelTypes.LINK,
                cons.ModelTypes.SITE,
                cons.ModelTypes.VISUAL,
                cons.ModelTypes.COLLIDER,
                cons.ModelTypes.CAMERA,
            ],
        ):
            range_ = cons.Sensor_Target_Type_Range["REF"].copy()
        return tuple(cons.Sensor_Types[range_[0] : range_[1]]) if range_ else (("NONE", "None", ""),)

    def update_type(self, context: Context):
        """Reset sensor type selection when reference or xbody options change."""
        self["Sensor_Type"] = 0

    # The three flags are declared *before* ``Sensor_Type`` on purpose.  Blender
    # assigns operator arguments in RNA declaration order, not call order, so
    # declaring the enum last makes it the final assignment: the reset above
    # always runs first and can no longer clobber a requested type.  That keeps
    # ``create_sensor(set_xbody=True, Sensor_Type='Frameangvel')`` — the shape
    # MCP emits — correct for every flag combination, not just all-defaults.
    set_ref: BoolProperty(
        name="Use Reference",
        default=False,
        description="Add Sensor Reference",
        update=update_type,
    )  # type: ignore

    set_xbody: BoolProperty(
        name="Use Xbody",
        default=False,
        description="Xbody instead body",
        update=update_type,
    )  # type: ignore

    set_subtree: BoolProperty(
        name="Use Subtree",
        default=False,
        description="Subtree instead body",
        update=update_type,
    )  # type: ignore

    Sensor_Type: EnumProperty(
        items=sensor_enum_items,
        name="Sensor Type",
        default=0,
        description="Sensor Type",
    )  # type: ignore

    def draw(self, context: Context):
        """Draw operator UI elements for sensor type, reference, and xbody options."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        box = layout.box()
        col = box.column()
        if sel.check_selected_model_types(
            context,
            [
                cons.ModelTypes.LINK,
                cons.ModelTypes.SITE,
                cons.ModelTypes.VISUAL,
                cons.ModelTypes.COLLIDER,
                cons.ModelTypes.CAMERA,
            ],
        ):
            if sel.check_have_model_types_in_selected(context, [cons.ModelTypes.LINK]):
                if not self.set_subtree:
                    col.prop(self, "set_xbody")
                if not self.set_xbody:
                    col.prop(self, "set_subtree")
            if len(context.selected_objects) == 2:
                col.prop(self, "set_ref")
        col.prop(self, "Sensor_Type")
        if self.Sensor_Type == "NONE":
            col.label(text="None sensor type selected", icon="NOT_FOUND")

    def execute(self, context: Context):
        """Execute the operator, creating sensors for selected objects."""
        sensor_type = self.Sensor_Type
        collection = funcs.get_collection(context, cons.CollectionNames.SENSOR)

        def sensor_target_type(obj, use_xbody=False, use_subtree=False):
            model_type = obj.Forge_Model_Type
            if model_type == cons.ModelTypes.LINK:
                if use_xbody:
                    return cons.SensorTargetTypes.XBODY
                if use_subtree:
                    return cons.SensorTargetTypes.SUBTREE
                return cons.SensorTargetTypes.BODY
            if model_type in [cons.ModelTypes.VISUAL, cons.ModelTypes.COLLIDER]:
                return cons.SensorTargetTypes.GEOM
            return model_type

        if context.selected_objects:
            objs = sel.get_ordered_selection_objects(context)
            if self.set_ref and any(obj.Forge_Model_Type == cons.ModelTypes.JOINT for obj in objs):
                self.report({"ERROR"}, "Joints cannot be used as frame sensor targets or references")
                return {"CANCELLED"}
            if len(context.selected_objects) == 2 and self.set_ref:
                target_type = sensor_target_type(objs[0], self.set_xbody, self.set_subtree)
                ref_type = sensor_target_type(objs[1], self.set_xbody, False)
                sel.clear_select()
                new_obj = funcs.add_sensor(
                    context, self.report, collection, sensor_type, target_type, objs, ref_type=ref_type
                )
                new_obj.select_set(True)
            else:
                new_objs = []
                for obj in objs:
                    target_type = sensor_target_type(obj, self.set_xbody, self.set_subtree)

                    sel.clear_select()
                    new_objs.append(funcs.add_sensor(context, self.report, collection, sensor_type, target_type, obj))
                for obj in new_objs:
                    obj.select_set(True)

            funcs.update_ui(context)
            return {"FINISHED"}
        else:
            return {"CANCELLED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link/joint/site/visual/collider/camera objects."""
        if sel.check_selected_model_types(context, [cons.ModelTypes.LINK]):
            return True
        elif sel.check_selected_model_types(context, [cons.ModelTypes.JOINT]):
            return True
        elif sel.check_selected_model_types(context, [cons.ModelTypes.SITE]):
            return True
        elif sel.check_selected_model_types(context, [cons.ModelTypes.VISUAL, cons.ModelTypes.COLLIDER]):
            return True
        elif sel.check_selected_model_types(
            context,
            [
                cons.ModelTypes.LINK,
                cons.ModelTypes.SITE,
                cons.ModelTypes.VISUAL,
                cons.ModelTypes.COLLIDER,
                cons.ModelTypes.CAMERA,
            ],
        ):
            return True
        else:
            # A joint may only be a lone target — MJCF's reftype has no `joint`
            # entry, so it can never be a reference. Say so instead of leaving
            # the bare "poll() failed, context is incorrect".
            cls.poll_message_set(
                "select one link/joint/site/visual/collider/camera, or two objects from "
                "link/site/visual/collider/camera for a target + reference sensor; a joint "
                "cannot be combined with another selected object"
            )
            return False

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the sensor creation dialog with default options."""
        self.set_ref = False
        self.set_xbody = False
        self.set_subtree = False
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Contact
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Contact_Creation(BaseCreationOperator):
    """Create contact, based on selected existing link(s)"""

    bl_idname = "forge.create_contact"
    bl_label = "Create contact(s)"
    collection_tag = cons.CollectionNames.CONTACT
    show_dialog = True

    def contact_enum_items(self, context: Context):
        """Generate enum items for contact type selection based on selected object types."""

        if sel.check_selected_model_types(context, [cons.ModelTypes.LINK]):
            return tuple(cons.Contact_Types[0:1])
        elif sel.check_selected_model_types(
            context, [cons.ModelTypes.VISUAL, cons.ModelTypes.COLLIDER, cons.ModelTypes.PLANE, cons.ModelTypes.HFIELD]
        ):
            return tuple(cons.Contact_Types[1:])
        return (("NONE", "None", ""),)

    contact_type: EnumProperty(items=contact_enum_items, name="Contact Type", default=0)  # type: ignore

    def execute(self, context: Context):
        """Execute the operator, creating contact pairs from selected objects."""
        collection = funcs.get_collection(context, self.collection_tag)
        if context.selected_objects:
            type = self.contact_type
            objs = sel.get_ordered_selection_objects(context)
            sel.clear_select()
            new_objs = []
            for i in range(len(objs) - 1):
                for j in range(i + 1, len(objs)):
                    new_objs.append(funcs.add_contact(context, self.report, collection, type, [objs[i], objs[j]]))
            for obj in new_objs:
                obj.select_set(True)
            funcs.update_ui(context)
            return {"FINISHED"}
        else:
            return {"CANCELLED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on at least 2 selected link/geom objects."""
        if len(context.selected_objects) < 2:
            return False
        if sel.check_selected_model_types(context, [cons.ModelTypes.LINK]):
            return True
        if sel.check_selected_model_types(
            context, [cons.ModelTypes.VISUAL, cons.ModelTypes.COLLIDER, cons.ModelTypes.PLANE, cons.ModelTypes.HFIELD]
        ):
            return True


# ═══════════════════════════════════════════════════════════════════════
# Light
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Light_Creation(Operator):
    """Create light(s), optionally based on selected existing link(s)"""

    bl_idname = "forge.create_light"
    bl_label = "Create light(s)"
    bl_options = {"REGISTER", "UNDO"}

    def type_enum_items(self, context: Context):
        """Generate enum items for light type selection based on selection state."""
        if not context.selected_objects:
            return cons.Light_Types
        else:
            return cons.Light_Types[1:3]

    def mode_enum_items(self, context: Context):
        """Generate enum items for light mode selection based on selection count."""
        if len(context.selected_objects) == 2 or len(context.selected_objects) == 1:
            return cons.Target_Modes
        else:
            return cons.Target_Modes[2:5]

    light_type: EnumProperty(
        items=type_enum_items,
        name="Light Type",
        default=0,
        description="Light Type",
    )  # type: ignore

    light_mode: EnumProperty(
        items=mode_enum_items,
        name="Light Mode",
        default=0,
        description="Light Mode",
    )  # type: ignore

    def draw(self, context: Context):
        """Draw operator UI elements for light type and mode selection."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column(align=True)
        col.prop(self, "light_type")
        col.prop(self, "light_mode")

    def execute(self, context: Context):
        """Execute the operator, creating light objects for selected links."""
        light_type = self.light_type
        light_mode = self.light_mode

        coll_tag = cons.CollectionNames.LIGHT if context.selected_objects else cons.CollectionNames.WORLD
        collection = funcs.get_collection(context, coll_tag)

        if context.selected_objects:
            objs = sel.get_ordered_selection_objects(context)
            new_objs = []
            if (len(context.selected_objects) == 2 or len(context.selected_objects) == 1) and light_mode in [
                cons.TargetModes.TARGETBODY,
                cons.TargetModes.TARGETBODYCOM,
            ]:
                if len(context.selected_objects) == 1:
                    objs.insert(0, None)
                sel.clear_select()
                new_obj = funcs.add_light(context, self.report, collection, light_type, light_mode, objs)
                new_obj.select_set(True)
            else:
                for obj in objs:
                    sel.clear_select()
                    new_objs.append(funcs.add_light(context, self.report, collection, light_type, light_mode, obj))
                for obj in new_objs:
                    obj.select_set(True)
        else:
            new_obj = funcs.add_light(context, self.report, collection, light_type, light_mode)
            new_obj.select_set(True)
        funcs.update_ui(context)
        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link objects or no selection."""
        return sel.check_selected_model_types(context, [cons.ModelTypes.LINK]) or not context.selected_objects

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the light creation dialog."""
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Camera
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Camera_Creation(Operator):
    """Create camera(s), optionally based on selected existing link(s)"""

    bl_idname = "forge.create_camera"
    bl_label = "Create camera(s)"
    bl_options = {"REGISTER", "UNDO"}

    def mode_enum_items(self, context: Context):
        """Generate enum items for camera mode selection based on selection count."""
        if len(context.selected_objects) == 2 or len(context.selected_objects) == 1:
            return cons.Target_Modes
        else:
            return cons.Target_Modes[2:5]

    camera_type: EnumProperty(
        items=cons.Camera_Types,
        name="Camera Type",
        default=0,
        description="Camera Type",
    )  # type: ignore

    camera_mode: EnumProperty(
        items=mode_enum_items,
        name="Camera Mode",
        default=0,
        description="Camera Mode",
    )  # type: ignore

    def draw(self, context: Context):
        """Draw operator UI elements for camera type and mode selection."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column(align=True)
        col.prop(self, "camera_type")
        col.prop(self, "camera_mode")

    def execute(self, context: Context):
        """Execute the operator, creating camera objects for selected links."""
        camera_type = self.camera_type
        camera_mode = self.camera_mode

        coll_tag = cons.CollectionNames.CAMERA if context.selected_objects else cons.CollectionNames.WORLD
        collection = funcs.get_collection(context, coll_tag)

        if context.selected_objects:
            objs = sel.get_ordered_selection_objects(context)
            new_objs = []
            if (len(context.selected_objects) == 2 or len(context.selected_objects) == 1) and camera_mode in [
                cons.TargetModes.TARGETBODY,
                cons.TargetModes.TARGETBODYCOM,
            ]:
                if len(context.selected_objects) == 1:
                    objs.insert(0, None)
                sel.clear_select()
                new_obj = funcs.add_camera(context, self.report, collection, camera_type, camera_mode, objs)
                new_obj.select_set(True)
            else:
                for obj in objs:
                    sel.clear_select()
                    new_objs.append(funcs.add_camera(context, self.report, collection, camera_type, camera_mode, obj))
                for obj in new_objs:
                    obj.select_set(True)
        else:
            new_obj = funcs.add_camera(context, self.report, collection, camera_type, camera_mode)
            new_obj.select_set(True)
        funcs.update_ui(context)
        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link objects or no selection."""
        return sel.check_selected_model_types(context, [cons.ModelTypes.LINK]) or not context.selected_objects

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the camera creation dialog."""
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Frame / Replicate
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Frame_Creation(Operator):
    """Create frame(s), optionally based on selected existing frame(s) | link(s) | replicate(s)
    Shift + Click will use Frame as parent"""

    bl_idname = "forge.create_frame"
    bl_label = "Create frame(s)"
    bl_options = {"REGISTER", "UNDO"}

    reverse_parent: bool = False

    def execute(self, context: Context):
        """Execute the operator, creating frame objects for selected parents."""
        coll_tag = (
            cons.CollectionNames.FRAME
            if context.selected_objects and not self.reverse_parent
            else cons.CollectionNames.WORLD
        )
        collection = funcs.get_collection(context, coll_tag)

        if context.selected_objects:
            objs = [obj for obj in context.selected_objects]
            new_objs = []
            for obj in objs:
                sel.clear_select()
                new_objs.append(funcs.add_frame(context, self.report, collection, obj, self.reverse_parent))
            for obj in new_objs:
                obj.select_set(True)
        else:
            sel.clear_select()
            new_obj: Object = funcs.add_frame(context, self.report, collection)
            new_obj.select_set(True)

        funcs.update_ui(context)
        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link, replicate, frame, or no selection."""
        return (
            sel.check_selected_model_types(
                context, [cons.ModelTypes.LINK, cons.ModelTypes.REPLICATE, cons.ModelTypes.FRAME]
            )
            or not context.selected_objects
        )

    def invoke(self, context: Context, event):
        """Invoke the operator, checking for shift-click to toggle reverse parent mode."""
        if event.shift:
            self.reverse_parent = True

        return self.execute(context)


class Forge_OT_Replicate_Creation(Operator):
    """Create replicate, based on selected existing frame(s) | link(s) | replicate(s)"""

    bl_idname = "forge.create_replicate"
    bl_label = "Create replicate"
    bl_options = {"REGISTER", "UNDO"}

    count: IntProperty(
        name=def_props.REPLICATE_PROPS_NAME["count"],
        default=def_props.REPLICATE_PROPS_DEFAULT["count"],
        subtype="UNSIGNED",
    )  # type: ignore
    sep: StringProperty(name=def_props.REPLICATE_PROPS_NAME["sep"], default=def_props.REPLICATE_PROPS_DEFAULT["sep"])  # type: ignore
    offset: FloatVectorProperty(
        name=def_props.REPLICATE_PROPS_NAME["offset"],
        default=def_props.REPLICATE_PROPS_DEFAULT["offset"],
        size=len(def_props.REPLICATE_PROPS_DEFAULT["offset"]),
        subtype="TRANSLATION",
    )  # type: ignore
    euler: FloatVectorProperty(
        name=def_props.REPLICATE_PROPS_NAME["euler"],
        default=def_props.REPLICATE_PROPS_DEFAULT["euler"],
        size=len(def_props.REPLICATE_PROPS_DEFAULT["euler"]),
        subtype="EULER",
    )  # type: ignore

    def draw(self, context: Context):
        """Draw operator UI elements for replicate count, separation, offset, and rotation."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column()
        col.prop(self, "count")
        col.prop(self, "sep")
        col.prop(self, "offset")
        col.prop(self, "euler")

    def execute(self, context: Context):
        """Execute the operator, creating a replicate from selected objects."""
        coll_tag = cons.CollectionNames.WORLD
        collection = funcs.get_collection(context, coll_tag)

        replicate_obj = context.selected_objects

        sel.clear_select()
        new_obj: Object = funcs.add_replicate(
            context, self.report, self.count, self.sep, self.offset, self.euler, collection, replicate_obj
        )
        new_obj.select_set(True)

        funcs.update_ui(context)
        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected objects of compatible model types."""
        return sel.check_selected_model_types(
            context,
            [
                cons.ModelTypes.CAMERA,
                cons.ModelTypes.LIGHT,
                cons.ModelTypes.VISUAL,
                cons.ModelTypes.COLLIDER,
                cons.ModelTypes.SITE,
                cons.ModelTypes.LINK,
                cons.ModelTypes.FRAME,
                cons.ModelTypes.ATTACH,
                cons.ModelTypes.REPLICATE,
            ],
        )

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the replicate creation dialog."""
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Inertial (compute from visual children)
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Inertial_Creation(Operator):
    """Compute Inertial for link(s)"""

    bl_idname = "forge.create_inertial"
    bl_label = "Compute Inertial"
    bl_options = {"REGISTER", "UNDO"}

    inertial_model_type: EnumProperty(
        items=(
            (cons.ModelTypes.VISUAL, "Visual", ""),
            (cons.ModelTypes.COLLIDER, "Collider", ""),
        ),
        name="Inertial Model Type",
        default=cons.ModelTypes.VISUAL,
        description="Compute inertial by selected object model type",
    )  # type: ignore

    check_mesh_valid: BoolProperty(
        name="Check Geometry",
        default=False,
        description="Whether or not check geometry valid",
    )  # type: ignore

    def _get_objects(self, obj: Object, inertial_objs: list):
        """Recursively collect geometry objects for inertia computation.

        Args:
            obj: The root object to search from.
            inertial_objs: List to append found objects to compute inertial.
        """
        for child in obj.children:
            if child.Forge_Model_Type == cons.ModelTypes.FRAME:
                self._get_objects(child, inertial_objs)
            if child.Forge_Model_Type != self.inertial_model_type:
                continue
            inertial_objs.append(child)

    def execute(self, context: Context):
        """Execute the operator, computing and creating inertial data for selected links."""
        coll_tag = cons.CollectionNames.INERTIAL
        collection = funcs.get_collection(context, coll_tag)

        print(self.inertial_model_type)
        if context.selected_objects:
            link_objs = [obj for obj in context.selected_objects]

            new_objs = []

            for obj in link_objs:
                sel.clear_select()
                if obj.Forge_Model_Type != cons.ModelTypes.LINK:
                    continue
                if not obj.children:
                    continue

                inertial_objs = []
                for child in obj.children:
                    if child.Forge_Model_Type == cons.ModelTypes.FRAME:
                        self._get_objects(child, inertial_objs)
                    if child.Forge_Model_Type != self.inertial_model_type:
                        continue
                    inertial_objs.append(child)

                if not inertial_objs:
                    self.report({"ERROR"}, f"Compute {obj.name}'s inertia cancelled: no visual meshes found.")
                    continue
                if self.check_mesh_valid and not check_mesh(context, self.report, inertial_objs):
                    self.report({"ERROR"}, f"Compute {obj.name}'s inertia cancelled, see previous error.")
                    continue
                else:
                    inertia = compute_inertia(context, self.report, inertial_objs)
                    if inertia is None:
                        self.report({"ERROR"}, f"Compute {obj.name}'s inertia cancelled, see previous error.")
                        continue
                    new_obj = funcs.add_inertial(context, self.report, collection, obj, inertia)
                    new_objs.append(new_obj)
            for obj in new_objs:
                obj.select_set(True)
            return {"FINISHED"}
        else:
            return {"CANCELLED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link objects."""
        return sel.check_selected_model_types(context, [cons.ModelTypes.LINK])

    def invoke(self, context: Context, event):
        """Show a property dialog if show_dialog is set, otherwise execute directly."""
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Change Gizmo Size
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Change_Gizmo_Size(Operator):
    """Apply to change gizmo display size"""

    bl_idname = "forge.scale_gizmo_size"
    bl_label = "Scale Gizmo"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context: Context):
        """Execute the operator, scaling gizmo display size for all relevant objects."""
        if context.selected_objects:
            objs = list(context.selected_objects)
        else:
            objs = list(bpy.data.objects)
        for obj in objs:
            funcs.scale_gizmo(context, obj)

        funcs.update_ui(context)
        return {"FINISHED"}


# ═══════════════════════════════════════════════════════════════════════
# Link Mark Root
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Link_MarkRoot(Operator):
    """Mark link(s) as root link"""

    bl_idname = "forge.mark_root_link"
    bl_label = "Mark root"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context: Context):
        """Execute the operator, marking selected parentless links as root."""
        if context.selected_objects:
            for obj in context.selected_objects:
                if obj.parent is None:
                    obj["Root Link"] = True
                else:
                    matrix_world = obj.matrix_world
                    self.report({"WARNING"}, f"{obj.name} is unlinked from {obj.parent.name} and mark as root")
                    obj.parent = None
                    obj.matrix_world = matrix_world
                    obj["Root Link"] = True

            funcs.update_ui(context)
            return {"FINISHED"}
        else:
            return {"CANCELLED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link or frame objects."""
        return sel.check_selected_model_types(
            context,
            [
                cons.ModelTypes.LINK,
                cons.ModelTypes.FRAME,
                cons.ModelTypes.REPLICATE,
            ],
        )


# ═══════════════════════════════════════════════════════════════════════
# Mesh Check
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Mesh_Check(Operator):
    """Check mesh validation"""

    bl_idname = "forge.mesh_check"
    bl_label = "Check Mesh(s)"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context: Context):
        """Execute the operator, checking mesh validity for selected visual objects."""
        if context.selected_objects:
            inertial_objs = []
            for obj in context.selected_objects:
                inertial_objs.append(obj)

            import time

            start_time = time.time()
            check_mesh(context, self.report, inertial_objs)
            end_time = time.time()
            execution_time = end_time - start_time
            self.report({"INFO"}, f"Check Mesh Time: {execution_time} seconds")

            return {"FINISHED"}
        else:
            return {"CANCELLED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected visual objects."""
        return sel.check_selected_model_types(context, [cons.ModelTypes.VISUAL])
