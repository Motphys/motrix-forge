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

"""Popup property-editor operators for forge model types.

Extracted from forge_operator.py to reduce that file's size.
Each class opens a popup dialog for editing a specific model type's properties.
"""

from math import ceil

import bpy
from bpy.types import Context, UILayout

from ..core import constants as cons
from ..core import props_data as def_props
from ..core.common import get_modifier_socket, prop_modifier_socket
from ..core.props import (
    ActuatorItem,
    CameraItem,
    ContactItem,
    EqualityItem,
    Forge_OT_TendonTargetItemAdd,
    Forge_OT_TendonTargetItemRemove,
    GeomItem,
    GlobalConfig,
    JointItem,
    LightItem,
    LinkItem,
    ReplicateItem,
    SensorItem,
    TendonItem,
    VisualConfig,
)


class Forge_OT_PROPERTIES_Global(bpy.types.Operator):
    """Click to change global properties"""

    bl_idname = "forge.properties_global"
    bl_label = "Global Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the global properties popup layout.

        Args:
            context: The active Blender context.
        """
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        data: GlobalConfig = context.scene.Forge_GlobalConfig
        layout.label(text="Global Properties")
        header, body = layout.panel("Props_Properties_Compiler", default_closed=False)
        header.label(text="Compiler Properties")
        if body:
            box = body.box()
            col = box.column()
            row = col.row().split(factor=0.4)
            row.use_property_split = False
            row.alignment = "RIGHT"
            row.label(text=f"{def_props.COMPILER_PROPS_NAME['autolimits']}:")
            active_text = "Activated" if data.g_compiler.autolimits else "Diactivated"
            row.prop(data.g_compiler, "autolimits", text=active_text, toggle=1)
            for prop in def_props.COMPILER_PROPS:
                if prop == "autolimits":
                    continue
                col.prop(data.g_compiler, prop)

        header, body = layout.panel("Props_Properties_Option", default_closed=True)
        header.label(text="Option Properties")
        if body:
            box = body.box()
            col = box.column()
            for prop in def_props.OPTION_PROPS:
                if prop == "flag":
                    continue
                col.prop(data.g_option, prop)
            cheader, cbody = layout.panel("Flag_Option", default_closed=True)
            cheader.label(text="Flag Option")
            if cbody:
                box = cbody.box()
                box.use_property_split = False
                col = box.column()
                col.label(text="Highlight to activated else diactivated")
                row = box.row().split(factor=0.4)
                row.alignment = "RIGHT"
                row.label(text=f"{def_props.FLAG_PROPS_NAME['override']}:")
                active_text = "Activated" if data.g_option.flag.override else "Diactivated"
                row.prop(data.g_option.flag, "override", text=active_text, toggle=1)

                row = box.grid_flow(
                    row_major=True,
                    columns=4,
                    even_columns=True,
                    even_rows=True,
                    align=True,
                )
                for prop in def_props.FLAG_PROPS[:4]:
                    row.prop(data.g_option.flag, prop, toggle=1)
                for prop in def_props.FLAG_PROPS[4:8]:
                    row.prop(data.g_option.flag, prop, toggle=1)

        header, body = layout.panel("Props_Properties_Statistic", default_closed=True)
        header.label(text="Statistic Properties")
        if body:
            box = body.box()
            col = box.column()
            for prop in def_props.STATISTIC_PROPS:
                col.prop(data.g_statistic, prop)

    def execute(self, context: Context):
        """Invoke the popup dialog for editing global properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)

    @classmethod
    def poll(cls, context: Context):
        """Only available when no objects are selected.

        Returns:
            True if nothing is selected, False otherwise.
        """
        return len(context.selected_objects) == 0


class Forge_OT_PROPERTIES_Visual(bpy.types.Operator):
    """Click to change visual properties"""

    bl_idname = "forge.properties_visual"
    bl_label = "Visual Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the visual properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        data: VisualConfig = context.scene.Forge_VisualConfig
        layout.label(text="Visual Properties")
        header, body = layout.panel("Props_Properties_Global", default_closed=False)
        header.label(text="Global Properties")
        if body:
            box = body.box()
            row = box.row().split(factor=0.4)
            row.use_property_split = False
            row.alignment = "RIGHT"
            row.label(text=f"{def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Global]['orthographic']}:")
            active_text = "Activated" if data.v_global.orthographic else "Diactivated"
            row.prop(data.v_global, "orthographic", text=active_text, toggle=1)
            col = box.column()
            for prop in def_props.VISUAL_CONFIG_PROPS[cons.VisualConfigTypes.Global]:
                if prop == "orthographic":
                    continue
                col.prop(data.v_global, prop)

        header, body = layout.panel("Props_Properties_Headlight", default_closed=False)
        header.label(text="Headlight Properties")
        if body:
            box = body.box()
            row = box.row().split(factor=0.4)
            row.use_property_split = False
            row.alignment = "RIGHT"
            row.label(text=f"{def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Headlight]['active']}:")
            active_text = "Activated" if bool(data.v_headlight.active) else "Diactivated"
            row.prop(data.v_headlight, "active", text=active_text, toggle=1)
            col = box.column()
            col.enabled = bool(data.v_headlight.active)
            for prop in def_props.VISUAL_CONFIG_PROPS[cons.VisualConfigTypes.Headlight]:
                if prop == "active":
                    continue
                col.prop(data.v_headlight, prop)

        header, body = layout.panel("Props_Properties_Map", default_closed=False)
        header.label(text="Map Properties")
        if body:
            box = body.box()
            col = box.column()
            for prop in def_props.VISUAL_CONFIG_PROPS[cons.VisualConfigTypes.Map]:
                col.prop(data.v_map, prop)

        header, body = layout.panel("Props_Properties_Rgba", default_closed=False)
        header.label(text="Rgba Properties")
        if body:
            box = body.box()
            col = box.column()
            for prop in def_props.VISUAL_CONFIG_PROPS[cons.VisualConfigTypes.Rgba]:
                col.prop(data.v_rgba, prop)

        header, body = layout.panel("Props_Properties_Quality", default_closed=True)
        header.label(text="Quality Properties")
        if body:
            box = body.box()
            col = box.column()
            for prop in def_props.VISUAL_CONFIG_PROPS[cons.VisualConfigTypes.Quality]:
                col.prop(data.v_quality, prop)

        header, body = layout.panel("Props_Properties_Ssgi", default_closed=True)
        header.label(text="SSGI Properties")
        if body:
            box = body.box()
            row = box.row().split(factor=0.4)
            row.use_property_split = False
            row.alignment = "RIGHT"
            row.label(text=f"{def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Ssgi]['active']}:")
            active_text = "Activated" if data.v_ssgi.active else "Diactivated"
            row.prop(data.v_ssgi, "active", text=active_text, toggle=1)
            col = box.column()
            col.enabled = data.v_ssgi.active
            for prop in def_props.VISUAL_CONFIG_PROPS[cons.VisualConfigTypes.Ssgi]:
                if prop == "active":
                    continue
                col.prop(data.v_ssgi, prop)

        header, body = layout.panel("Props_Properties_Tonemapping", default_closed=True)
        header.label(text="Tonemapping Properties")
        if body:
            box = body.box()
            col = box.column()
            for prop in def_props.VISUAL_CONFIG_PROPS[cons.VisualConfigTypes.Tonemapping]:
                col.prop(data.v_tonemapping, prop)

    def execute(self, context: Context):
        """Invoke the popup dialog for editing visual properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)

    @classmethod
    def poll(cls, context: Context):
        """Only available when no objects are selected."""
        return len(context.selected_objects) == 0


class Forge_OT_PROPERTIES_HeightField(bpy.types.Operator):
    """Click to change height field properties."""

    bl_idname = "forge.properties_hfield"
    bl_label = "Height Field Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the height field properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        obj = context.active_object
        modifier_name = cons.AdditionalShapeModifiers[obj.Forge_Model_Type]
        HS = cons.ModifierSockets.HField
        data = obj.modifiers[modifier_name]
        layout.label(text="Height Field Properties")
        box = layout.box()
        row = box.row().split(factor=0.4)
        rcol = row.column()
        rcol.alignment = "RIGHT"
        rcol.label(text="Nrow")
        rcol.label(text="Ncol")
        rcol.label(text="Elevation")
        rcol.label(text="Radius X")
        rcol.label(text="Radius Y")
        rcol.label(text="Elevation Z")
        rcol.label(text="Base Z")

        rcol = row.column()
        rcol.use_property_split = False
        prop_modifier_socket(rcol, data, HS.NROW, text="")
        prop_modifier_socket(rcol, data, HS.NCOL, text="")
        active_text = "Activated" if get_modifier_socket(data, HS.USE_ELEVATION) else "Diactivated"
        prop_modifier_socket(rcol, data, HS.USE_ELEVATION, text=active_text, toggle=1)
        prop_modifier_socket(rcol, data, HS.RADIUS_X, text="")
        prop_modifier_socket(rcol, data, HS.RADIUS_Y, text="")
        prop_modifier_socket(rcol, data, HS.ELEVATION_Z, text="")
        prop_modifier_socket(rcol, data, HS.BASE_Z, text="")

        row = box.row().split(factor=0.4)
        rcol = row.column(align=True)
        rcol.alignment = "RIGHT"
        rcol.label(text="Offset X")
        rcol.label(text="Y")
        rcol.label(text="Z")
        rcol = row.column()
        rcol.use_property_split = False
        prop_modifier_socket(rcol, data, HS.OFFSET, text="")

        row = box.row().split(factor=0.4)
        rcol = row.column()
        rcol.alignment = "RIGHT"
        rcol.label(text="Use Height Map")
        if get_modifier_socket(data, HS.USE_HEIGHT_MAP):
            rcol.label(text="Height Map")

        rcol = row.column()
        rcol.use_property_split = False
        active_text = "Activated" if get_modifier_socket(data, HS.USE_HEIGHT_MAP) else "Diactivated"
        prop_modifier_socket(rcol, data, HS.USE_HEIGHT_MAP, text=active_text, toggle=1)
        if get_modifier_socket(data, HS.USE_HEIGHT_MAP):
            prop_modifier_socket(rcol, data, HS.HEIGHT_MAP, text="")

        header, body = layout.panel("Props_Properties_Info", default_closed=False)
        header.label(text="Model Properties")
        if body:
            box = body.box()
            data: GeomItem = obj.Forge_Geometry
            col = box.column()
            col.prop(data, "group")
            col.prop(data, "condim")
            col.prop(data, "contype")
            col.prop(data, "conaffinity")
            col.prop(data, "priority")
            col.prop(data, "friction")
            col.prop(data, "margin")
            col.prop(data, "gap")
            col.prop(data, "solmix")
            col.prop(data, "solref")
            col.prop(data, "solimp")

    def execute(self, context: Context):
        """Invoke the popup dialog for editing height field properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)

    @classmethod
    def poll(cls, context: Context):
        obj = context.active_object
        if obj is None or obj.Forge_Model_Type != cons.ModelTypes.HFIELD:
            return False
        return cons.AdditionalShapeModifiers[cons.ModelTypes.HFIELD] in obj.modifiers


class Forge_OT_PROPERTIES_Plane(bpy.types.Operator):
    """Click to change plane properties."""

    bl_idname = "forge.properties_plane"
    bl_label = "Height Plane Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the plane properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        obj = context.active_object
        modifier_name = cons.AdditionalShapeModifiers[obj.Forge_Model_Type]
        PS = cons.ModifierSockets.Plane
        data = obj.modifiers[modifier_name]
        layout.label(text="Plane Properties")
        box = layout.box()
        row = box.row().split(factor=0.4)
        rcol = row.column()
        rcol.alignment = "RIGHT"
        rcol.label(text="Half Size X")
        rcol.label(text="Half Size Y")
        rcol.label(text="Infinite")

        rcol = row.column()
        rcol.use_property_split = False
        prop_modifier_socket(rcol, data, PS.HALF_SIZE_X, text="")
        prop_modifier_socket(rcol, data, PS.HALF_SIZE_Y, text="")
        active_text = "Activated" if get_modifier_socket(data, PS.INFINITE) else "Diactivated"
        prop_modifier_socket(rcol, data, PS.INFINITE, text=active_text, toggle=1)

        header, body = layout.panel("Props_Properties_Info", default_closed=False)
        header.label(text="Model Properties")
        if body:
            box = body.box()
            data: GeomItem = obj.Forge_Geometry
            col = box.column()
            col.prop(data, "group")
            col.prop(data, "condim")
            col.prop(data, "contype")
            col.prop(data, "conaffinity")
            col.prop(data, "priority")
            col.prop(data, "friction")
            col.prop(data, "margin")
            col.prop(data, "gap")
            col.prop(data, "solmix")
            col.prop(data, "solref")
            col.prop(data, "solimp")

    def execute(self, context: Context):
        """Invoke the popup dialog for editing plane properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)

    @classmethod
    def poll(cls, context: Context):
        obj = context.active_object
        if obj is None or obj.Forge_Model_Type != cons.ModelTypes.PLANE:
            return False
        return cons.AdditionalShapeModifiers[cons.ModelTypes.PLANE] in obj.modifiers


class Forge_OT_PROPERTIES_Shape(bpy.types.Operator):
    """Click to change general geometry/collider shape size."""

    bl_idname = "forge.properties_shape"
    bl_label = "Shape Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the shape properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        obj = context.active_object
        layout.label(text="Shape Properties")
        box = layout.box()
        col = box.column()
        row = col.row().split(factor=0.4)
        rcol = row.column()
        rcol.alignment = "RIGHT"
        if obj.Forge_Model_Type == cons.ModelTypes.VISUAL:
            if obj.Forge_Geometry.type not in cons.MeshGeometryTypes:
                match obj.Forge_Geometry.type:
                    case cons.GeometryTypes.BOX:
                        rcol.label(text="Size X")
                        rcol.label(text="Y")
                        rcol.label(text="Z")
                    case cons.GeometryTypes.SPHERE:
                        rcol.label(text="Radius")
                    case cons.GeometryTypes.CAPSULE | cons.GeometryTypes.CYLINDER:
                        rcol.label(text="Radius")
                        rcol.label(text="Height")
        if obj.Forge_Model_Type == cons.ModelTypes.COLLIDER:
            if obj.Forge_Geometry.type not in cons.MeshGeometryTypes:
                match obj.Forge_Geometry.type:
                    case cons.GeometryTypes.BOX:
                        rcol.label(text="Size X")
                        rcol.label(text="Y")
                        rcol.label(text="Z")
                    case cons.GeometryTypes.SPHERE:
                        rcol.label(text="Radius")
                    case cons.GeometryTypes.CAPSULE | cons.GeometryTypes.CYLINDER:
                        rcol.label(text="Radius")
                        rcol.label(text="Height")

        rcol = row.column()
        if obj.Forge_Model_Type == cons.ModelTypes.VISUAL:
            if obj.Forge_Geometry.type not in cons.MeshGeometryTypes:
                modifier_name = cons.GeometryShapeModifiers[obj.Forge_Geometry.type]
                modifier = obj.modifiers[modifier_name]
                VS = cons.ModifierSockets.Visual
                match obj.Forge_Geometry.type:
                    case cons.GeometryTypes.BOX:
                        prop_modifier_socket(rcol, modifier, VS.SIZE, text="")
                    case cons.GeometryTypes.SPHERE:
                        prop_modifier_socket(rcol, modifier, VS.SIZE, text="")
                    case cons.GeometryTypes.CAPSULE | cons.GeometryTypes.CYLINDER:
                        prop_modifier_socket(rcol, modifier, VS.SIZE, text="")
                        prop_modifier_socket(rcol, modifier, VS.HEIGHT, text="")
        if obj.Forge_Model_Type == cons.ModelTypes.COLLIDER:
            if obj.Forge_Geometry.type not in cons.MeshGeometryTypes:
                modifier_name = cons.ColliderShapeModifiers[obj.Forge_Geometry.type]
                modifier = obj.modifiers[modifier_name]
                CS = cons.ModifierSockets.Collider
                match obj.Forge_Geometry.type:
                    case cons.GeometryTypes.BOX:
                        prop_modifier_socket(rcol, modifier, CS.SIZE, text="")
                    case cons.GeometryTypes.SPHERE:
                        prop_modifier_socket(rcol, modifier, CS.SIZE, text="")
                    case cons.GeometryTypes.CAPSULE | cons.GeometryTypes.CYLINDER:
                        prop_modifier_socket(rcol, modifier, CS.SIZE, text="")
                        prop_modifier_socket(rcol, modifier, CS.HEIGHT, text="")

        header, body = layout.panel("Props_Properties_Info", default_closed=False)
        header.label(text="Model Properties")
        if body:
            box = body.box()
            row = box.row(align=True).split(factor=0.4)
            col = row.column()
            col.alignment = "RIGHT"
            if obj.Forge_Model_Type == cons.ModelTypes.VISUAL:
                col.label(text="Geometry Type")
            if obj.Forge_Model_Type == cons.ModelTypes.COLLIDER:
                col.label(text="Collider Type")
            col = row.column()
            if obj.Forge_Model_Type == cons.ModelTypes.VISUAL:
                col.label(text=f"{obj.Forge_Geometry.type}")
            if obj.Forge_Model_Type == cons.ModelTypes.COLLIDER:
                col.label(text=f"{obj.Forge_Geometry.type}")

            data: GeomItem = obj.Forge_Geometry
            col = box.column()
            col.prop(data, "group")
            col.prop(data, "condim")
            col.prop(data, "contype")
            col.prop(data, "conaffinity")
            col.prop(data, "priority")
            col.prop(data, "friction")
            col.prop(data, "mass")
            col.prop(data, "density")
            col.prop(data, "margin")
            col.prop(data, "gap")
            col.prop(data, "solmix")
            col.prop(data, "solref")
            col.prop(data, "solimp")

    def execute(self, context: Context):
        """Invoke the popup dialog for editing shape properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)


class Forge_OT_PROPERTIES_Shape_Site(bpy.types.Operator):
    """Click to change general site shape size."""

    bl_idname = "forge.properties_shape_site"
    bl_label = "Shape Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the site shape properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        obj = context.active_object
        layout.label(text="Shape Properties")
        box = layout.box()
        col = box.column()
        row = col.row().split(factor=0.4)
        rcol = row.column()
        rcol.alignment = "RIGHT"
        match obj.Forge_Geometry.type:
            case cons.GeometryTypes.BOX:
                rcol.label(text="Size X")
                rcol.label(text="Y")
                rcol.label(text="Z")
            case cons.GeometryTypes.SPHERE:
                rcol.label(text="Radius")
            case cons.GeometryTypes.CAPSULE | cons.GeometryTypes.CYLINDER:
                rcol.label(text="Radius")
                rcol.label(text="Height")
        rcol = row.column()
        modifier_name = cons.SiteShapeModifiers[obj.Forge_Geometry.type]
        modifier = obj.modifiers[modifier_name]
        SS = cons.ModifierSockets.Site

        match obj.Forge_Geometry.type:
            case cons.GeometryTypes.BOX:
                prop_modifier_socket(rcol, modifier, SS.SIZE, text="")
            case cons.GeometryTypes.SPHERE:
                prop_modifier_socket(rcol, modifier, SS.SIZE, text="")
            case cons.GeometryTypes.CAPSULE | cons.GeometryTypes.CYLINDER:
                prop_modifier_socket(rcol, modifier, SS.SIZE, text="")
                prop_modifier_socket(rcol, modifier, SS.HEIGHT, text="")

        header, body = layout.panel("Props_Properties_Info", default_closed=False)
        header.label(text="Model Properties")
        if body:
            box = body.box()
            row = box.row().split(factor=0.4)
            rcol = row.column()
            rcol.alignment = "RIGHT"
            rcol.label(text="Group")
            rcol = row.column()

            data: GeomItem = obj.Forge_Geometry
            rcol.prop(data, "group", text="")

    def execute(self, context: Context):
        """Invoke the popup dialog for editing site shape properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)


class Forge_OT_PROPERTIES_Link(bpy.types.Operator):
    """Click to change link properties."""

    bl_idname = "forge.properties_link"
    bl_label = "Link Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the link properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        obj = context.active_object
        data: LinkItem = obj.Forge_Link
        layout.label(text="Shape Properties")
        box = layout.box()
        row = box.row().split(factor=0.4)
        rcol = row.column()
        rcol.alignment = "RIGHT"
        rcol.label(text="Display Type")
        rcol.label(text="Display Size")
        rcol = row.column()
        active_text = "Activated" if data.mocap else "Diactivated"
        rcol.prop(obj, "empty_display_type", text="")
        rcol.prop(obj, "empty_display_size", text="")

        layout.label(text="Link Properties")
        box = layout.box()
        row = box.row().split(factor=0.4)
        rcol = row.column()
        rcol.alignment = "RIGHT"
        rcol.label(text=f"{def_props.LINK_PROPS_NAME['mocap']}:")
        rcol.label(text=f"{def_props.LINK_PROPS_NAME['gravcomp']}:")
        rcol = row.column()
        rcol.use_property_split = False
        rcol.prop(data, "mocap", text=active_text, toggle=1)
        rcol.prop(data, "gravcomp", text="")

    def execute(self, context: Context):
        """Invoke the popup dialog for editing link properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)


class Forge_OT_PROPERTIES_Joint(bpy.types.Operator):
    """Click to change joint properties."""

    bl_idname = "forge.properties_joint"
    bl_label = "Joint Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the joint properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        layout.label(text="Joint Properties")
        obj = context.active_object

        box = layout.box()
        col = box.column()
        modifier_name = cons.AdditionalShapeModifiers[cons.ModelTypes.JOINT]
        if modifier_name in obj.modifiers:
            prop_modifier_socket(
                col,
                obj.modifiers[modifier_name],
                cons.ModifierSockets.Gizmo.DISPLAY_SIZE,
                text="Display Size",
            )

        data: JointItem = obj.Forge_Joint
        box = layout.box()
        col = box.column()
        col.prop(data, "type")

        box = layout.box()
        col = box.column()

        if data.type != cons.JointTypes.FREE:
            col.prop(data, "springdamper")
            box = layout.box()
            col = box.column()
            col.label(text="Solver:")
            col.prop(data, "solreflimit")
            col.prop(data, "solimplimit")
            col.prop(data, "solreffriction")
            col.prop(data, "solimpfriction")
            box = layout.box()
            col = box.column()
            col.prop(data, "stiffness")
            box = layout.box()
            col = box.column(align=True)
            col.prop(data, "range")
            col.prop(data, "limited")
            if data.type != cons.JointTypes.BALL:
                box = layout.box()
                col = box.column(align=True)
                col.prop(data, "actuatorfrcrange")
                col.prop(data, "actuatorfrclimited")
            box = layout.box()
            col = box.column()
            col.prop(data, "margin")
            if data.type != cons.JointTypes.BALL:
                col.prop(data, "ref")
                col.prop(data, "springref")
            col.prop(data, "armature")
            col.prop(data, "damping")
            col.prop(data, "frictionloss")
        else:
            col.prop(data, "stiffness")
            col.prop(data, "armature")
            col.prop(data, "damping")
            col.prop(data, "frictionloss")

    def execute(self, context: Context):
        """Invoke the popup dialog for editing joint properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)


class Forge_OT_PROPERTIES_Actuator(bpy.types.Operator):
    """Click to change actuator properties."""

    bl_idname = "forge.properties_actuator"
    bl_label = "Actuator Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw_large_array(self, data, layout: UILayout, name: str, row_size: int = 5):
        """Draw a large array property spread across multiple rows."""
        attr = getattr(data, name)
        count = len(attr)
        colcount = int(ceil(count / row_size))
        for i in range(colcount):
            row = layout.row(align=True)
            for j in range(row_size):
                idx = i * row_size + j
                if idx < count:
                    row.prop(data, name, index=idx, text="")

    def draw(self, context: Context):
        """Draw the actuator properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        layout.label(text="Actuator Properties")
        obj = context.active_object

        box = layout.box()
        col = box.column()
        modifier_name = cons.AdditionalShapeModifiers[cons.ModelTypes.ACTUATOR]
        if modifier_name in obj.modifiers:
            prop_modifier_socket(
                col,
                obj.modifiers[modifier_name],
                cons.ModifierSockets.Gizmo.DISPLAY_SIZE,
                text="Display Size",
            )

        data: ActuatorItem = obj.Forge_Actuator
        box = layout.box()
        col = box.column(align=True)
        col.prop(data, "type")
        col.prop(data, "target")
        row = col.row().split(factor=0.4)
        rcol = row.column()
        rcol.alignment = "RIGHT"
        rcol.label(text="Target Type")
        rcol = row.column()
        rcol.alignment = "LEFT"
        rcol.label(text=f"  {data.target_type}")

        box = layout.box()
        col = box.column(align=True)
        col.prop(data, "ctrlrange")
        col.prop(data, "ctrllimited")
        box = layout.box()
        col = box.column(align=True)
        col.prop(data, "forcerange")
        col.prop(data, "forcelimited")
        box = layout.box()
        col = box.column(align=True)
        col.prop(data, "gaintype")
        col.prop(data, "biastype")
        if data.type == cons.ActuatorTypes.POSITION:
            box = layout.box()
            col = box.column()
            col.prop(data, "kp")
            col.prop(data, "kv")
            col.prop(data, "inheritrange")
        elif data.type == cons.ActuatorTypes.VELOCITY:
            box = layout.box()
            col = box.column()
            col.prop(data, "kv")

        box = layout.box()
        col = box.column(align=True)
        if data.type == cons.ActuatorTypes.ADHESION:
            col.prop(data, "gain")
        else:
            box.use_property_split = False
            col.label(text="Gear")
            self.draw_large_array(data, col, "gear", 6)
            box = layout.box()
            box.use_property_split = False
            col = box.column(align=True)
            col.label(text="Dynamics")
            self.draw_large_array(data, col, "dynprm")
            box = layout.box()
            box.use_property_split = False
            col = box.column(align=True)
            col.label(text="Gain")
            self.draw_large_array(data, col, "gainprm")
            box = layout.box()
            box.use_property_split = False
            col = box.column(align=True)
            col.label(text="Bias")
            self.draw_large_array(data, col, "biasprm")

    def execute(self, context: Context):
        """Invoke the popup dialog for editing actuator properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=480)


class Forge_OT_PROPERTIES_Tendon(bpy.types.Operator):
    """Click to change tendon properties."""

    bl_idname = "forge.properties_tendon"
    bl_label = "Tendon Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the tendon properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.label(text="Tendon Properties")
        obj = context.active_object

        box = layout.box()
        col = box.column()
        modifier_name = cons.AdditionalShapeModifiers[cons.ModelTypes.TENDON]
        if modifier_name in obj.modifiers:
            prop_modifier_socket(
                col,
                obj.modifiers[modifier_name],
                cons.ModifierSockets.Gizmo.DISPLAY_SIZE,
                text="Display Size",
            )

        data: TendonItem = obj.Forge_Tendon
        box = layout.box()
        col = box.column()
        col.prop(data, "type")

        row = box.row()
        row.template_list(
            "FORGE_UL_TendonTargetList",
            "",
            data.targets,
            "items",
            data.targets,
            "active_index",
            rows=3,
        )

        col = row.column(align=True)
        col.operator(Forge_OT_TendonTargetItemAdd.bl_idname, icon="ADD", text="")
        col.operator(Forge_OT_TendonTargetItemRemove.bl_idname, icon="REMOVE", text="")

        col = box.column(align=True)
        col.prop(data, "range")
        col.prop(data, "limited")
        col = box.column()
        col.prop(data, "solreflimit")
        col.prop(data, "solimplimit")
        col.prop(data, "springlength")
        col.prop(data, "stiffness")
        col.prop(data, "damping")

    def execute(self, context: Context):
        """Invoke the popup dialog for editing tendon properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)


class Forge_OT_PROPERTIES_Equality(bpy.types.Operator):
    """Click to change equality properties."""

    bl_idname = "forge.properties_equality"
    bl_label = "Equality Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the equality properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.label(text="Equality Properties")
        obj = context.active_object

        box = layout.box()
        col = box.column()
        modifier_name = cons.AdditionalShapeModifiers[cons.ModelTypes.EQUALITY]
        if modifier_name in obj.modifiers:
            prop_modifier_socket(
                col,
                obj.modifiers[modifier_name],
                cons.ModifierSockets.Gizmo.DISPLAY_SIZE,
                text="Display Size",
            )

        data: EqualityItem = obj.Forge_Equality
        row = layout.row().split(factor=0.4)
        rcol = row.column()
        rcol.alignment = "RIGHT"
        rcol.label(text="Active")
        rcol = row.column()
        rcol.use_property_split = False
        active_text = "Activated" if data.active else "Diactivated"
        rcol.prop(data, "active", text=active_text, toggle=1)

        box = layout.box()
        box.active = data.active
        col = box.column(align=True)
        col.prop(data, "type")
        col = box.column()
        col.prop(data, "target1")
        if data.target1:
            col.prop(data, "target2")
        row = col.row().split(factor=0.4)
        rcol = row.column()
        rcol.alignment = "RIGHT"
        rcol.label(text="Target Type")
        rcol = row.column()
        rcol.alignment = "LEFT"
        rcol.label(text=f"  {data.target_type}")

        col = box.column()
        for prop in def_props.EQUALITY_TYPE_PROPS[data.type]:
            if prop == "active":
                continue
            col.prop(data, prop)

    def execute(self, context: Context):
        """Invoke the popup dialog for editing equality properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)


class Forge_OT_PROPERTIES_Contact(bpy.types.Operator):
    """Click to change contact properties."""

    bl_idname = "forge.properties_contact"
    bl_label = "Contact Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the contact properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.label(text="Contact Properties")
        obj = context.active_object

        box = layout.box()
        col = box.column()
        modifier_name = cons.AdditionalShapeModifiers[cons.ModelTypes.CONTACT]
        if modifier_name in obj.modifiers:
            prop_modifier_socket(
                col,
                obj.modifiers[modifier_name],
                cons.ModifierSockets.Gizmo.DISPLAY_SIZE,
                text="Display Size",
            )

        data: ContactItem = obj.Forge_Contact
        box = layout.box()
        col = box.column()
        col.prop(data, "type")
        col.prop(data, "target1")
        col.prop(data, "target2")

        if data.type == cons.ContactTypes.PAIR:
            box = layout.box()
            col = box.column()
            col.prop(data, "condim")
            col.prop(data, "friction")
            box = layout.box()
            col = box.column()
            col.label(text="Solver:")
            col.prop(data, "solref")
            col.prop(data, "solreffriction")
            box = layout.box()
            col = box.column()
            col.prop(data, "margin")
            col.prop(data, "gap")

    def execute(self, context: Context):
        """Invoke the popup dialog for editing contact properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)


class Forge_OT_PROPERTIES_Sensor(bpy.types.Operator):
    """Click to change sensor properties."""

    bl_idname = "forge.properties_sensor"
    bl_label = "Sensor Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the sensor properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.label(text="Sensor Properties")
        obj = context.active_object

        box = layout.box()
        col = box.column()
        modifier_name = cons.AdditionalShapeModifiers[cons.ModelTypes.SENSOR]
        if modifier_name in obj.modifiers:
            prop_modifier_socket(
                col,
                obj.modifiers[modifier_name],
                cons.ModifierSockets.Gizmo.DISPLAY_SIZE,
                text="Display Size",
            )

        data: SensorItem = obj.Forge_Sensor
        box = layout.box()
        col = box.column()
        row = col.row().split(factor=0.4)
        rcol = row.column()
        rcol.alignment = "RIGHT"
        rcol.label(text="Sensor Type")
        rcol = row.column()
        rcol.alignment = "LEFT"
        rcol.label(text=f"  {data.type}")
        row = col.row().split(factor=0.4)
        rcol = row.column()
        rcol.alignment = "RIGHT"
        rcol.label(text="Target Type")
        rcol = row.column()
        rcol.alignment = "LEFT"
        rcol.label(text=f"  {data.target_type}")

        name = "Target"
        if data.type == cons.SensorTypes.Contact:
            if data.target_type == cons.SensorTargetTypes.BODY:
                name = "Link1"
            if data.target_type == cons.SensorTargetTypes.GEOM:
                name = "Geom1"
            if data.target_type == cons.SensorTargetTypes.SUBTREE:
                name = "Subtree1"
            if data.target_type == cons.SensorTargetTypes.SITE:
                name = "Site"

        col.prop(data, "target", text=name)

        if data.type in [
            cons.SensorTypes.Framepos,
            cons.SensorTypes.Framequat,
            cons.SensorTypes.Framexaxis,
            cons.SensorTypes.Frameyaxis,
            cons.SensorTypes.Framezaxis,
            cons.SensorTypes.Framelinvel,
            cons.SensorTypes.Frameangvel,
        ]:
            if data.target:
                col.prop(data, "ref")
                col.prop(data, "use_xbody")

        if data.type == cons.SensorTypes.Contact and data.target_type != cons.SensorTargetTypes.SITE:
            if data.target_type == cons.SensorTargetTypes.BODY:
                name = "Link2"
            if data.target_type == cons.SensorTargetTypes.GEOM:
                name = "Geom2"
            if data.target_type == cons.SensorTargetTypes.SUBTREE:
                name = "Subtree2"
            if data.target:
                col.prop(data, "ref", text=name)
                col.prop(data, "use_subtree")

        box = layout.box()
        col = box.column()
        col.prop(data, "noise")
        col.prop(data, "cutoff")

        if data.type == cons.SensorTypes.Contact:
            col = box.column()
            col.prop(data, "num")
            col.enabled = False

            col = box.column()
            col.prop(data, "data")
            col.prop(data, "reduce")

    def execute(self, context: Context):
        """Invoke the popup dialog for editing sensor properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)


class Forge_OT_PROPERTIES_Light(bpy.types.Operator):
    """Click to change light properties."""

    bl_idname = "forge.properties_light"
    bl_label = "Light Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the light properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        obj = context.active_object
        data: LightItem = obj.Forge_Light
        layout.label(text="Light Properties")
        box = layout.box()
        col = box.column()
        col.prop(data, "type")
        col.prop(data, "mode")
        if data.mode in [cons.TargetModes.TARGETBODY, cons.TargetModes.TARGETBODYCOM]:
            col.prop(data, "target")
        row = box.row().split(factor=0.4)
        rcol = row.column()
        rcol.alignment = "RIGHT"
        rcol.label(text="Cast Shadow")
        rcol = row.column()
        rcol.use_property_split = False
        active_text = "Activated" if obj.data.use_shadow else "Diactivated"
        rcol.prop(obj.data, "use_shadow", text=active_text, toggle=1)

        col = box.column()
        col.prop(obj.data, "color")
        col.prop(obj.data, "energy")
        if obj.data.type == cons.LightTypes.SPOT or obj.data.type == cons.LightTypes.POINT:
            col.prop(obj.data, "shadow_soft_size")
            col.prop(obj.data, "cutoff_distance")
        else:
            col.prop(obj.data, "angle")
        if obj.data.type == cons.LightTypes.SPOT:
            col.prop(obj.data, "spot_size")
            col.prop(obj.data, "spot_blend")

    def execute(self, context: Context):
        """Invoke the popup dialog for editing light properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)


class Forge_OT_PROPERTIES_Camera(bpy.types.Operator):
    """Click to change camera properties."""

    bl_idname = "forge.properties_camera"
    bl_label = "Camera Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the camera properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        obj = context.active_object
        data: CameraItem = obj.Forge_Camera
        layout.label(text="Camera Properties")
        box = layout.box()
        col = box.column()
        col.prop(data, "type")
        col.prop(data, "mode")
        if data.mode in [cons.TargetModes.TARGETBODY, cons.TargetModes.TARGETBODYCOM]:
            col.prop(data, "target")

        if data.type == cons.CameraTypes.PERSPECTIVE:
            col.prop(obj.data, "angle")
        else:
            col.prop(obj.data, "ortho_scale")
        col.prop(obj.data, "clip_start")
        col.prop(obj.data, "clip_end")

    def execute(self, context: Context):
        """Invoke the popup dialog for editing camera properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)


class Forge_OT_PROPERTIES_Replicate(bpy.types.Operator):
    """Click to change replicate properties."""

    bl_idname = "forge.properties_replicate"
    bl_label = "Replicate Properties"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw the replicate properties popup layout."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        layout.label(text="Replicate Properties")
        obj = context.active_object

        box = layout.box()
        col = box.column()
        modifier_name = cons.AdditionalShapeModifiers[cons.ModelTypes.REPLICATE]
        RS = cons.ModifierSockets.Replicate

        if modifier_name in obj.modifiers:
            modifier = obj.modifiers[modifier_name]
            prop_modifier_socket(col, modifier, RS.COUNT, text="Count")
            prop_modifier_socket(col, modifier, RS.OFFSET, text="Offset")
            prop_modifier_socket(col, modifier, RS.EULER, text="Euler")

        data: ReplicateItem = obj.Forge_Replicate
        box = layout.box()
        col = box.column()
        col.prop(data, "sep", text="Separator")

    def execute(self, context: Context):
        """Invoke the popup dialog for editing replicate properties."""
        wm = context.window_manager
        return wm.invoke_popup(self, width=400)


classes = (
    Forge_OT_PROPERTIES_Global,
    Forge_OT_PROPERTIES_Visual,
    Forge_OT_PROPERTIES_HeightField,
    Forge_OT_PROPERTIES_Plane,
    Forge_OT_PROPERTIES_Shape,
    Forge_OT_PROPERTIES_Shape_Site,
    Forge_OT_PROPERTIES_Link,
    Forge_OT_PROPERTIES_Joint,
    Forge_OT_PROPERTIES_Actuator,
    Forge_OT_PROPERTIES_Tendon,
    Forge_OT_PROPERTIES_Equality,
    Forge_OT_PROPERTIES_Contact,
    Forge_OT_PROPERTIES_Sensor,
    Forge_OT_PROPERTIES_Light,
    Forge_OT_PROPERTIES_Camera,
    Forge_OT_PROPERTIES_Replicate,
)
