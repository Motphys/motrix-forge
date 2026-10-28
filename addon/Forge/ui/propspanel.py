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

from math import degrees
from typing import Any

import bpy
from bpy.props import FloatVectorProperty
from bpy.types import Context, Image, Object, Panel, PropertyGroup, UILayout, bpy_prop_array
from mathutils import Matrix

from ..core import constants as cons
from ..core import props_data as def_props
from ..core.common import get_modifier_socket
from ..core.props import (
    ActuatorItem,
    AttachItem,
    ContactItem,
    EqualityItem,
    GeomItem,
    IncludeItem,
    InertialItem,
    JointItem,
    LightItem,
    LinkItem,
    SensorItem,
    TendonItem,
)
from ..settings import Get_Logo_Icon_ID


def getMatrixData(space, method, obj: Object | None = None):
    """Get transformation matrix data of the active object.

    Args:
        space: Coordinate space ("local" for local space, "world" for world space).
        method: Type of data to retrieve ("translation", "rotation" or "dimensions").

    Returns:
        Translation vector, euler rotation, or dimension values.
    """

    obj = obj if obj is not None else bpy.context.active_object
    if space == "local":
        matrix = obj.matrix_local if obj else Matrix.Identity(4)
    elif space == "world":
        matrix = obj.matrix_world if obj else Matrix.Identity(4)
    else:
        matrix = Matrix.Identity(4)

    if method == "translation":
        return matrix.to_translation()
    elif method == "rotation":
        return matrix.to_euler()
    elif method == "dimensions":
        return obj.dimensions if obj else (0.0, 0.0, 0.0)


class Forge_Object_MatrixInfo(PropertyGroup):
    """Stores matrix information (translation, rotation, dimensions) of the active object.
    Used to display local/world space transform data in the Blender properties panel.
    """

    translation_local: FloatVectorProperty(
        name="Translation local",
        get=lambda self: getMatrixData("local", "translation", self.id_data),
        unit="LENGTH",
        subtype="TRANSLATION",
        description="Translation in the local space",
        precision=5,
    )  # type: ignore

    translation_world: FloatVectorProperty(
        name="Translation world",
        get=lambda self: getMatrixData("world", "translation", self.id_data),
        unit="LENGTH",
        subtype="TRANSLATION",
        description="Translation in the world space",
        precision=5,
    )  # type: ignore

    rotation_local: FloatVectorProperty(
        name="Rotation local",
        get=lambda self: getMatrixData("local", "rotation", self.id_data),
        unit="ROTATION",
        subtype="EULER",
        description="Rotation in the local space",
        precision=5,
    )  # type: ignore

    rotation_world: FloatVectorProperty(
        name="Rotation world",
        get=lambda self: getMatrixData("world", "rotation", self.id_data),
        unit="ROTATION",
        subtype="EULER",
        description="Rotation in the world space",
        precision=5,
    )  # type: ignore

    dimensions: FloatVectorProperty(
        name="Dimensions",
        get=lambda self: getMatrixData("", "dimensions", self.id_data),
        unit="LENGTH",
        subtype="TRANSLATION",
        description="Dimensions",
        precision=5,
    )  # type: ignore


class Forge_Object_Properties_Panel(Panel):
    """Forge object properties panel.
    Displays object transform matrix info in the Blender Properties editor,
    and shows model-specific properties based on object type (Link, Joint, Geom, etc.).
    """

    bl_label = "Forge Properties"
    bl_idname = "FORGE_OBJECT_PROPERTIES_PT_PANEL"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"
    bl_category = "Forge"

    def draw_header(self, context: Context):
        """Draw the panel header with a preferences icon."""
        layout = self.layout
        layout.label(icon_value=Get_Logo_Icon_ID())

    def draw(self, context: Context):
        """Draw the panel content.

        Renders matrix transform info (translation, rotation, dimensions in
        local and world space) and model-type-specific properties depending
        on the active object's Forge_Model_Type (Link, Joint, Geom, etc.).
        """
        # scene = context.scene
        layout = self.layout
        cold = layout.column(align=True)
        cold.label(text="Object Properties ")

        obj = context.active_object
        if obj is None:
            return

        header, body = layout.panel("Props_Matrix_Info", default_closed=False)
        header.label(text="Matrix Info", icon="TRANSFORM_ORIGINS")
        if body:
            box = body.box()
            row = box.row(align=True).split(factor=0.35)
            col = row.column(align=True)
            col.alignment = "RIGHT"
            col.label(text="Space")
            col.label(text="Location X")
            col.label(text="Y")
            col.label(text="Z")
            col = row.column(align=True)
            col.alignment = "RIGHT"
            col.label(text="Local")
            col.prop(obj.Forge_Matrix_Info, "translation_local", text="", index=0)
            col.prop(obj.Forge_Matrix_Info, "translation_local", text="", index=1)
            col.prop(obj.Forge_Matrix_Info, "translation_local", text="", index=2)
            col = row.column(align=True)
            col.alignment = "RIGHT"
            col.label(text="World")
            col.prop(obj.Forge_Matrix_Info, "translation_world", text="", index=0)
            col.prop(obj.Forge_Matrix_Info, "translation_world", text="", index=1)
            col.prop(obj.Forge_Matrix_Info, "translation_world", text="", index=2)
            row = box.row(align=True).split(factor=0.35)
            col = row.column(align=True)
            col.alignment = "RIGHT"
            col.label(text="Rotation X")
            col.label(text="Y")
            col.label(text="Z")
            col = row.column(align=True)
            col.prop(obj.Forge_Matrix_Info, "rotation_local", text="", index=0)
            col.prop(obj.Forge_Matrix_Info, "rotation_local", text="", index=1)
            col.prop(obj.Forge_Matrix_Info, "rotation_local", text="", index=2)
            col = row.column(align=True)
            col.prop(obj.Forge_Matrix_Info, "rotation_world", text="", index=0)
            col.prop(obj.Forge_Matrix_Info, "rotation_world", text="", index=1)
            col.prop(obj.Forge_Matrix_Info, "rotation_world", text="", index=2)
            box = body.box()
            row = box.row(align=True).split(factor=0.35)
            col = row.column(align=True)
            col.alignment = "RIGHT"
            col.label(text="Dimensions X")
            col.label(text="Y")
            col.label(text="Z")
            col = row.column(align=True)
            col.prop(obj.Forge_Matrix_Info, "dimensions", text="", index=0)
            col.prop(obj.Forge_Matrix_Info, "dimensions", text="", index=1)
            col.prop(obj.Forge_Matrix_Info, "dimensions", text="", index=2)

            box = body.box()
            row = box.row(align=True).split(factor=0.35)
            col = row.column(align=True)
            col.alignment = "RIGHT"
            col.label(text="Parent")
            col = row.column(align=True)
            col.enabled = False
            col.prop(obj, "parent", text="")

        header, body = layout.panel("Props_Properties_Info", default_closed=False)
        header.label(text="Properties Info", icon="INFO_LARGE")
        if body:
            box = body.box()
            row = box.row(align=True).split(factor=0.35)
            col = row.column(align=True)
            col.alignment = "RIGHT"
            col.label(text="Mode Type:")

            col = row.column(align=True)
            col.label(text=f"{obj.Forge_Model_Type}")

            match obj.Forge_Model_Type:
                case cons.ModelTypes.LINK:
                    draw_link_props(body, context)
                case cons.ModelTypes.INERTIAL:
                    draw_inertial_props(body, context)
                case cons.ModelTypes.VISUAL | cons.ModelTypes.COLLIDER:
                    draw_geom_props(body, context)
                case cons.ModelTypes.HFIELD:
                    draw_hfield_props(body, context)
                case cons.ModelTypes.PLANE:
                    draw_plane_props(body, context)
                case cons.ModelTypes.JOINT:
                    draw_joint_props(body, context)
                case cons.ModelTypes.ACTUATOR:
                    draw_actuator_props(body, context)
                case cons.ModelTypes.TENDON:
                    draw_tendon_props(body, context)
                case cons.ModelTypes.EQUALITY:
                    draw_equality_props(body, context)
                case cons.ModelTypes.SITE:
                    draw_site_props(body, context)
                case cons.ModelTypes.SENSOR:
                    draw_sensor_props(body, context)
                case cons.ModelTypes.CONTACT:
                    draw_contact_props(body, context)
                case cons.ModelTypes.LIGHT:
                    draw_light_props(body, context)
                case cons.ModelTypes.CAMERA:
                    draw_camera_props(body, context)
                case cons.ModelTypes.ATTACH:
                    draw_attach_props(body, context)
                case cons.ModelTypes.INCLUDE:
                    draw_include_props(body, context)


def draw_array_label(layout: UILayout, attr: Any, name: str):
    """Draw a label for an array field in the layout; first row shows the name,
    subsequent rows are empty to align with array values.
    """

    layout.label(text=name)
    for i in range(1, len(attr)):
        layout.label(text="")


def draw_list_items(layout: UILayout, attr: Any):
    """Draw a list of collection property item names in the layout."""

    values = ", ".join([f"{v.target.name if v.target else 'None'}" for v in attr.items])
    layout.label(text=f"{values}")


def draw_array_values(layout: UILayout, attr: Any):
    """Draw array values as a comma-separated string in the layout
    (integers shown as-is, floats with 4 decimal places).
    """

    values = ", ".join([f"{v}" if isinstance(v, int) else f"{v:.4f}" for v in attr])
    layout.label(text=f"{values}")


def draw_array_string(layout: UILayout, attr: Any):
    """Draw array values as a comma-separated string in the layout"""

    values = ", ".join([f"{v}" for v in attr])
    layout.label(text=f"{values}")


def draw_value(layout: UILayout, attr: Any):
    """Draw a property value in the layout based on its type.
    Supports str, bool, float, int, Object, Image, bpy_prop_array and list types.
    """

    if isinstance(attr, str):
        layout.label(text=f"{attr}")
    elif isinstance(attr, bool):
        layout.label(text=f"{attr}")
    elif isinstance(attr, float):
        layout.label(text=f"{attr:.4f}")
    elif isinstance(attr, int):
        layout.label(text=f"{attr}")
    elif isinstance(attr, Object) or isinstance(attr, Image):
        if attr:
            layout.label(text=f"{attr.name}")
        else:
            layout.label(text="None")
    elif isinstance(attr, bpy_prop_array) or isinstance(attr, list):
        draw_array_values(layout, attr)
    elif isinstance(attr, set):
        draw_array_string(layout, attr)
    else:
        layout.label(text="None")


def draw_link_props(layout: UILayout, context: Context):
    """Draw the Link properties panel, displaying all property fields in LinkItem."""

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    header, body = layout.panel("Props_Link_Info", default_closed=False)
    header.label(text="Link Info")
    if body:
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        for prop in def_props.LINK_PROPS:
            col.label(text=f"{def_props.LINK_PROPS_NAME[prop]}:")

        data: LinkItem = obj.Forge_Link
        col = row.column(align=True)
        for prop in def_props.LINK_PROPS:
            draw_value(col, getattr(data, prop))


def draw_inertial_props(layout: UILayout, context: Context):
    """Draw the Inertial properties panel, displaying all property fields in InertialItem."""

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    header, body = layout.panel("Props_Inertial_Info", default_closed=False)
    header.label(text="Inertial Info")
    if body:
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        for prop in def_props.INERTIAL_PROPS:
            col.label(text=f"{def_props.INERTIAL_PROPS_NAME[prop]}:")

        data: InertialItem = obj.Forge_Inertial
        col = row.column(align=True)
        for prop in def_props.INERTIAL_PROPS:
            draw_value(col, getattr(data, prop))


def draw_geom_props(layout: UILayout, context: Context):
    """Draw the geometry properties panel, showing geometry type and all GeomItem fields.
    Displays as "Geometry Type" or "Collider Type" depending on model type.
    """

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    header, body = layout.panel("Props_Geom_Info", default_closed=False)
    header.label(text="Geom Info")
    if body:
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        if obj.Forge_Model_Type == cons.ModelTypes.VISUAL:
            col.label(text="Geometry Type:")
        else:
            col.label(text="Collider Type:")

        col = row.column(align=True)
        draw_value(col, obj.Forge_Geometry.type)

        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        for prop in def_props.GEOM_PROPS:
            col.label(text=f"{def_props.GEOM_PROPS_NAME[prop]}:")

        data: GeomItem = obj.Forge_Geometry
        col = row.column(align=True)
        for prop in def_props.GEOM_PROPS:
            draw_value(col, getattr(data, prop))


def draw_hfield_props(layout: UILayout, context: Context):
    """Draw the height field (Hfield) properties panel, showing modifier terrain data
    (nrow, ncol, elevation, size) and GeomItem properties.
    """

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    modifier_name = cons.AdditionalShapeModifiers[obj.Forge_Model_Type]
    if modifier_name in obj.modifiers:
        data = obj.modifiers[modifier_name]
        header, body = layout.panel("Props_Hfield_Info", default_closed=False)
        header.label(text="Hfield Info")
        if body:
            box = body.box()
            row = box.row(align=True).split(factor=0.35)
            col = row.column(align=True)
            col.alignment = "RIGHT"
            col.label(text="Nrow | Ncol:")
            col.label(text="Use Elevation:")
            col.label(text="Radius X | Y:")
            col.label(text="Elevation Z:")
            col.label(text="Base Z:")

            col = row.column(align=True)
            col.use_property_split = False
            draw_value(col, [get_modifier_socket(data, "Socket_0"), get_modifier_socket(data, "Socket_2")])
            draw_value(col, get_modifier_socket(data, "Socket_3"))
            draw_value(col, [get_modifier_socket(data, "Socket_4"), get_modifier_socket(data, "Socket_5")])
            draw_value(col, get_modifier_socket(data, "Socket_6"))
            draw_value(col, get_modifier_socket(data, "Socket_7"))

            box = body.box()
            row = box.row(align=True).split(factor=0.35)
            col = row.column(align=True)
            col.alignment = "RIGHT"
            for prop in def_props.GEOM_PROPS:
                col.label(text=f"{def_props.GEOM_PROPS_NAME[prop]}:")

            data: GeomItem = obj.Forge_Geometry
            col = row.column(align=True)
            for prop in def_props.GEOM_PROPS:
                draw_value(col, getattr(data, prop))


def draw_plane_props(layout: UILayout, context: Context):
    """Draw the plane properties panel, showing modifier plane size and infinite flag,
    along with GeomItem properties.
    """

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    modifier_name = cons.AdditionalShapeModifiers[obj.Forge_Model_Type]
    if modifier_name in obj.modifiers:
        data = obj.modifiers[modifier_name]
        header, body = layout.panel("Props_Plane_Info", default_closed=False)
        header.label(text="Plane Info")
        if body:
            box = body.box()
            row = box.row(align=True).split(factor=0.35)
            col = row.column(align=True)
            col.alignment = "RIGHT"
            col.label(text="Size:")
            col.label(text="Infinite:")

            col = row.column(align=True)
            col.use_property_split = False
            draw_value(col, [get_modifier_socket(data, "Socket_2"), get_modifier_socket(data, "Socket_3")])
            draw_value(col, get_modifier_socket(data, "Socket_4"))

            box = body.box()
            row = box.row(align=True).split(factor=0.35)
            col = row.column(align=True)
            col.alignment = "RIGHT"
            for prop in def_props.GEOM_PROPS:
                col.label(text=f"{def_props.GEOM_PROPS_NAME[prop]}:")

            data: GeomItem = obj.Forge_Geometry
            col = row.column(align=True)
            for prop in def_props.GEOM_PROPS:
                draw_value(col, getattr(data, prop))


def draw_joint_props(layout: UILayout, context: Context):
    """Draw the joint properties panel, showing the joint type and type-specific JointItem fields."""

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    data: JointItem = obj.Forge_Joint
    header, body = layout.panel("Props_Joint_Info", default_closed=False)
    header.label(text="Joint Info")
    if body:
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        col.label(text="Joint Type:")

        col = row.column(align=True)
        draw_value(col, data.type)

        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        for prop in def_props.JOINT_TYPE_PROPS[data.type]:
            col.label(text=f"{def_props.JOINT_PROPS_NAME[prop]}:")

        col = row.column(align=True)
        for prop in def_props.JOINT_TYPE_PROPS[data.type]:
            draw_value(col, getattr(data, prop))


def draw_actuator_props(layout: UILayout, context: Context):
    """Draw the actuator properties panel, showing type, target info, and type-specific ActuatorItem fields."""

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    data: ActuatorItem = obj.Forge_Actuator
    header, body = layout.panel("Props_Actuator_Info", default_closed=False)
    header.label(text="Actuator Info")
    if body:
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        col.label(text="Actuator type:")
        col.label(text="Target type:")
        col.label(text="Target:")

        col = row.column(align=True)
        draw_value(col, data.type)
        draw_value(col, data.target_type)
        draw_value(col, data.target)

        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        for prop in def_props.ACTUATOR_TYPE_PROPS[data.type]:
            col.label(text=f"{def_props.ACTUATOR_PROPS_NAME[prop]}:")

        col = row.column(align=True)
        for prop in def_props.ACTUATOR_TYPE_PROPS[data.type]:
            draw_value(col, getattr(data, prop))


def draw_tendon_props(layout: UILayout, context: Context):
    """Draw the tendon properties panel, showing type, target list, and type-specific TendonItem fields."""

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    data: TendonItem = obj.Forge_Tendon
    header, body = layout.panel("Props_Tendon_Info", default_closed=False)
    header.label(text="Tendon Info")
    if body:
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        col.label(text="Tendon type:")
        col.label(text="Targets:")

        col = row.column(align=True)
        draw_value(col, data.type)
        draw_list_items(col, data.targets)

        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        for prop in def_props.TENDON_TYPE_PROPS[data.type]:
            col.label(text=f"{def_props.TENDON_PROPS_NAME[prop]}:")

        col = row.column(align=True)
        for prop in def_props.TENDON_TYPE_PROPS[data.type]:
            draw_value(col, getattr(data, prop))


def draw_equality_props(layout: UILayout, context: Context):
    """Draw the equality constraint properties panel, showing type, targets, and type-specific EqualityItem fields."""

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    data: EqualityItem = obj.Forge_Equality
    header, body = layout.panel("Props_Equality_Info", default_closed=False)
    header.label(text="Equality Info")
    if body:
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        col.label(text="Equality type:")
        col.label(text="Target1:")
        col.label(text="Target2:")
        col.label(text="Target type:")

        col = row.column(align=True)
        draw_value(col, data.type)
        draw_value(col, data.target1)
        draw_value(col, data.target2)
        draw_value(col, data.target_type)

        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        for prop in def_props.EQUALITY_TYPE_PROPS[data.type]:
            col.label(text=f"{def_props.EQUALITY_PROPS_NAME[prop]}:")

        col = row.column(align=True)
        for prop in def_props.EQUALITY_TYPE_PROPS[data.type]:
            draw_value(col, getattr(data, prop))


def draw_site_props(layout: UILayout, context: Context):
    """Draw the site properties panel, showing site type and group information."""

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    header, body = layout.panel("Props_Site_Info", default_closed=False)
    header.label(text="Site Info")
    if body:
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        col.label(text="Site type:")
        col.label(text="Group:")

        col = row.column(align=True)
        draw_value(col, obj.Forge_Geometry.type)
        data: GeomItem = obj.Forge_Geometry
        draw_value(col, data.group)


def draw_sensor_props(layout: UILayout, context: Context):
    """Draw the sensor properties panel, showing type, target info, and optional reference type/value."""

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    header, body = layout.panel("Props_Sensor_Info", default_closed=False)
    header.label(text="Sensor Info")
    if body:
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        col.label(text="Sensor type:")
        col.label(text="Target type:")
        col.label(text="Target:")
        data: SensorItem = obj.Forge_Sensor
        if data.ref:
            col.label(text="Reference type:")
            col.label(text="Reference:")
        if data.type == cons.SensorTypes.Contact:
            col.label(text="Num:")
            col.label(text="Data:")
            col.label(text="Reduce:")

        col = row.column(align=True)
        draw_value(col, data.type)
        draw_value(col, data.target_type)
        draw_value(col, data.target)
        if data.ref:
            draw_value(col, data.ref_type)
            draw_value(col, data.ref)

        if data.type == cons.SensorTypes.Contact:
            draw_value(col, data.num)
            draw_value(col, data.data)
            draw_value(col, data.reduce)


def draw_contact_props(layout: UILayout, context: Context):
    """Draw the contact properties panel, showing contact type and two target objects."""

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    header, body = layout.panel("Props_Contact_Info", default_closed=False)
    header.label(text="Contact Info")
    if body:
        data: ContactItem = obj.Forge_Contact
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        col.label(text="Contact type:")
        col.label(text="Target1:")
        col.label(text="Target2:")
        if data.type == cons.ContactTypes.PAIR:
            col.label(text=def_props.CONTACT_PROPS_NAME["condim"])
            col.label(text=def_props.CONTACT_PROPS_NAME["friction"])
            col.label(text=def_props.CONTACT_PROPS_NAME["solref"])
            col.label(text=def_props.CONTACT_PROPS_NAME["solreffriction"])
            col.label(text=def_props.CONTACT_PROPS_NAME["margin"])
            col.label(text=def_props.CONTACT_PROPS_NAME["gap"])

        col = row.column(align=True)

        draw_value(col, data.type)
        draw_value(col, data.target1)
        draw_value(col, data.target2)
        if data.type == cons.ContactTypes.PAIR:
            draw_value(col, data.condim)
            draw_value(col, data.friction)
            draw_value(col, data.solref)
            draw_value(col, data.solreffriction)
            draw_value(col, data.margin)
            draw_value(col, data.gap)


def draw_light_props(layout: UILayout, context: Context):
    """Draw the light properties panel, showing light type, mode, color, intensity,
    and spot parameters (for spot lights).

    Displays different properties based on light type (point, spot, directional, etc.).
    """

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    data: LightItem = obj.Forge_Light
    header, body = layout.panel("Props_Light_Info", default_closed=False)
    header.label(text="Light Info")
    if body:
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        col.label(text="Light type:")
        col.label(text="Light model:")
        if data.mode in [cons.TargetModes.TARGETBODY, cons.TargetModes.TARGETBODYCOM]:
            col.label(text="Target:")

        col.label(text="Color:")
        col.label(text="Intensity:")
        if obj.data.type == cons.LightTypes.SPOT or obj.data.type == cons.LightTypes.POINT:
            col.label(text="Radius:")
            col.label(text="Distance:")
        else:
            col.label(text="Angle:")
        if obj.data.type == cons.LightTypes.SPOT:
            col.label(text="Spot size:")
            col.label(text="Spot blend:")

        col = row.column(align=True)
        draw_value(col, data.type)
        draw_value(col, data.mode)
        if data.mode in [cons.TargetModes.TARGETBODY, cons.TargetModes.TARGETBODYCOM]:
            draw_value(col, data.target)

        draw_array_values(col, obj.data.color)
        draw_value(col, obj.data.energy)
        if obj.data.type == cons.LightTypes.SPOT or obj.data.type == cons.LightTypes.POINT:
            draw_value(col, obj.data.shadow_soft_size)
            draw_value(col, obj.data.cutoff_distance)
        else:
            draw_value(col, obj.data.angle)
        if obj.data.type == cons.LightTypes.SPOT:
            draw_value(col, obj.data.spot_size)
            draw_value(col, obj.data.spot_blend)


def draw_camera_props(layout: UILayout, context: Context):
    """Draw the camera properties panel, showing camera type, mode, target (if in TargetBody mode),
    angle/orthographic scale, near/far clip planes, and other parameters.
    """

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    data: LightItem = obj.Forge_Camera
    header, body = layout.panel("Props_Camera_Info", default_closed=False)
    header.label(text="Camera Info")
    if body:
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        col.label(text="Camera type:")
        col.label(text="Camera model:")
        if data.mode in [cons.TargetModes.TARGETBODY, cons.TargetModes.TARGETBODYCOM]:
            col.label(text="Target:")

        if data.type == cons.CameraTypes.PERSPECTIVE:
            col.label(text="Angle:")
        else:
            col.label(text="Ortho scale:")
        col.label(text="Clip start:")
        col.label(text="Clip end:")

        col = row.column(align=True)
        draw_value(col, data.type)
        draw_value(col, data.mode)
        if data.mode in [cons.TargetModes.TARGETBODY, cons.TargetModes.TARGETBODYCOM]:
            draw_value(col, data.target)

        if data.type == cons.CameraTypes.PERSPECTIVE:
            draw_value(col, degrees(obj.data.angle))
        else:
            draw_value(col, obj.data.ortho_scale)
        draw_value(col, obj.data.clip_start)
        draw_value(col, obj.data.clip_end)


def draw_attach_props(layout: UILayout, context: Context):
    """Draw the attach properties panel, showing model name, file path, link, and prefix."""

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    header, body = layout.panel("Props_Attach_Info", default_closed=False)
    header.label(text="Attach Info")
    if body:
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        col.label(text="Model:")
        col.label(text="File:")
        col.label(text="Link:")
        col.label(text="Prefix:")

        col = row.column(align=True)
        data: AttachItem = obj.Forge_Attach

        draw_value(col, data.model)
        draw_value(col, data.file)
        draw_value(col, data.link)
        draw_value(col, data.prefix)


def draw_include_props(layout: UILayout, context: Context):
    """Draw the include properties panel, showing the file and raw file paths."""

    layout.use_property_split = True
    layout.use_property_decorate = False
    obj = context.active_object
    header, body = layout.panel("Props_Include_Info", default_closed=False)
    header.label(text="Include Info")
    if body:
        box = body.box()
        row = box.row(align=True).split(factor=0.35)
        col = row.column(align=True)
        col.alignment = "RIGHT"
        col.label(text="File:")

        col = row.column(align=True)
        data: IncludeItem = obj.Forge_Include

        draw_value(col, data.file)
        draw_value(col, data.rawfile)


classes = (
    Forge_Object_MatrixInfo,
    Forge_Object_Properties_Panel,
)
