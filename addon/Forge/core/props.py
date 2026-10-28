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
from bpy.props import (
    BoolProperty,
    CollectionProperty,
    EnumProperty,
    FloatProperty,
    FloatVectorProperty,
    IntProperty,
    PointerProperty,
    StringProperty,
)
from bpy.types import Collection, Context, Object, Operator, PropertyGroup, Scene, UIList
from mathutils import Matrix

from . import constants as cons
from . import props_data as def_props
from . import selection as select
from .common import link_collection, set_modifier_socket
from .description import Description

_temp_links_by_owner: dict[int, dict] = {}


def _reset_from(prop_group, defaults: dict, skip_keys: frozenset[str] = frozenset()) -> None:
    """Reset every property listed in *defaults* to its default value.

    Handles both scalar and array (``FloatVectorProperty`` etc.) properties.
    Keys in *skip_keys* are not touched (useful for sub-object PointerProperties
    that need their own ``.reset()`` call).
    """

    for key, value in defaults.items():
        if key in skip_keys or not hasattr(prop_group, key):
            continue
        try:
            setattr(prop_group, key, value)
        except TypeError:
            # Blender array property — set element by element.
            attr = getattr(prop_group, key)
            for i, v in enumerate(value):
                attr[i] = v


def update_ui(context):
    """Redraw all PROPERTIES areas in the current screen."""
    if context is None or context.screen is None:
        return
    for area in context.screen.areas:
        if area.type == "PROPERTIES":
            area.tag_redraw()


class LinkItem(PropertyGroup):
    """Represents a MuJoCo link (body) with motion capture and gravity compensation settings."""

    mocap: BoolProperty(
        name=def_props.LINK_PROPS_NAME["mocap"],
        default=def_props.LINK_PROPS_DEFAULT["mocap"],
        description=Description.BodyDesc["Mocap"],
    )  # type: ignore
    gravcomp: FloatProperty(
        name=def_props.LINK_PROPS_NAME["gravcomp"],
        default=def_props.LINK_PROPS_DEFAULT["gravcomp"],
        precision=5,
        description=Description.BodyDesc["GravComp"],
    )  # type: ignore


class GeomItem(PropertyGroup):
    """Represents a MuJoCo geometry (collision shape) with type and physical contact properties."""

    type: EnumProperty(
        name="Geometry Type",
        items=cons.Geometry_Types,
        default="SPHERE",
        description=Description.GeomDesc["Type"],
    )  # type: ignore

    group: IntProperty(
        name=def_props.GEOM_PROPS_NAME["group"],
        default=def_props.GEOM_PROPS_DEFAULT["group"],
        description=Description.GeomDesc["Group"],
    )  # type: ignore
    condim: IntProperty(
        name=def_props.GEOM_PROPS_NAME["condim"],
        default=def_props.GEOM_PROPS_DEFAULT["condim"],
        description=Description.GeomDesc["ConDim"],
    )  # type: ignore
    contype: IntProperty(
        name=def_props.GEOM_PROPS_NAME["contype"],
        default=def_props.GEOM_PROPS_DEFAULT["contype"],
        description=Description.GeomDesc["Contype"],
    )  # type: ignore
    conaffinity: IntProperty(
        name=def_props.GEOM_PROPS_NAME["conaffinity"],
        default=def_props.GEOM_PROPS_DEFAULT["conaffinity"],
        description=Description.GeomDesc["ConAffinity"],
    )  # type: ignore
    priority: IntProperty(
        name=def_props.GEOM_PROPS_NAME["priority"],
        default=def_props.GEOM_PROPS_DEFAULT["priority"],
        description=Description.GeomDesc["Priority"],
    )  # type: ignore
    friction: FloatVectorProperty(
        name=def_props.GEOM_PROPS_NAME["friction"],
        default=def_props.GEOM_PROPS_DEFAULT["friction"],
        size=len(def_props.GEOM_PROPS_DEFAULT["friction"]),
        precision=5,
        description=Description.GeomDesc["Friction"],
    )  # type: ignore
    mass: FloatProperty(
        name=def_props.GEOM_PROPS_NAME["mass"],
        default=def_props.GEOM_PROPS_DEFAULT["mass"],
        precision=5,
        description=Description.GeomDesc["Mass"],
    )  # type: ignore
    density: FloatProperty(
        name=def_props.GEOM_PROPS_NAME["density"],
        default=def_props.GEOM_PROPS_DEFAULT["density"],
        precision=5,
        description=Description.GeomDesc["Density"],
    )  # type: ignore
    solmix: FloatProperty(
        name=def_props.GEOM_PROPS_NAME["solmix"],
        default=def_props.GEOM_PROPS_DEFAULT["solmix"],
        precision=5,
        description=Description.GeomDesc["SolMix"],
    )  # type: ignore
    solref: FloatVectorProperty(
        name=def_props.GEOM_PROPS_NAME["solref"],
        default=def_props.GEOM_PROPS_DEFAULT["solref"],
        size=len(def_props.GEOM_PROPS_DEFAULT["solref"]),
        precision=5,
        description=Description.GeomDesc["SolRef"],
    )  # type: ignore
    solimp: FloatVectorProperty(
        name=def_props.GEOM_PROPS_NAME["solimp"],
        default=def_props.GEOM_PROPS_DEFAULT["solimp"],
        size=len(def_props.GEOM_PROPS_DEFAULT["solimp"]),
        precision=5,
        description=Description.GeomDesc["SolImp"],
    )  # type: ignore
    margin: FloatProperty(
        name=def_props.GEOM_PROPS_NAME["margin"],
        default=def_props.GEOM_PROPS_DEFAULT["margin"],
        description=Description.GeomDesc["Margin"],
    )  # type: ignore
    gap: FloatProperty(
        name=def_props.GEOM_PROPS_NAME["gap"],
        default=def_props.GEOM_PROPS_DEFAULT["gap"],
        description=Description.GeomDesc["Gap"],
    )  # type: ignore


# JointItem
class JointItem(PropertyGroup):
    """Represents a MuJoCo joint with type, range, and dynamic properties (spring, damper, friction, etc.)."""

    def set_joint_shape(self, context: Context):
        """Update the joint's visual modifier shape when its type changes.

        Args:
            context: The active Blender context.
        """
        obj = self.id_data
        joint_type = self.type
        modifier_name = cons.AdditionalShapeModifiers[cons.ModelTypes.JOINT]
        if modifier_name in obj.modifiers:
            set_modifier_socket(
                obj.modifiers[modifier_name],
                cons.ModifierSockets.Joint.JOINT_TYPE,
                cons.JointShapeModifiers[joint_type],
            )
            obj.modifiers[modifier_name].node_group.interface_update(context)

    def set_angle(self, context: Context):
        """Update the joint range angle in the geometry modifier.

        Args:
            context: The active Blender context.
        """
        obj = self.id_data

        modifier_name = cons.AdditionalShapeModifiers[cons.ModelTypes.JOINT]
        if modifier_name in obj.modifiers:
            set_modifier_socket(obj.modifiers[modifier_name], cons.ModifierSockets.Joint.RANGE, self.range)
            obj.modifiers[modifier_name].node_group.interface_update(context)

    type: EnumProperty(
        name="Joint Type",
        items=cons.Joint_Types,
        default="HINGE",
        description=Description.JointDesc["Type"],
        update=set_joint_shape,
    )  # type: ignore

    # (spring, damper)
    springdamper: FloatVectorProperty(
        name=def_props.JOINT_PROPS_NAME["springdamper"],
        default=def_props.JOINT_PROPS_DEFAULT["springdamper"],
        size=len(def_props.JOINT_PROPS_DEFAULT["springdamper"]),
        precision=5,
        description=Description.JointDesc["SpringDamper"],
    )  # type: ignore
    solreflimit: FloatVectorProperty(
        name=def_props.JOINT_PROPS_NAME["solreflimit"],
        default=def_props.JOINT_PROPS_DEFAULT["solreflimit"],
        size=len(def_props.JOINT_PROPS_DEFAULT["solreflimit"]),
        precision=5,
        description=Description.JointDesc["SolRefLimit"],
    )  # type: ignore
    solimplimit: FloatVectorProperty(
        name=def_props.JOINT_PROPS_NAME["solimplimit"],
        default=def_props.JOINT_PROPS_DEFAULT["solimplimit"],
        size=len(def_props.JOINT_PROPS_DEFAULT["solimplimit"]),
        precision=5,
        description=Description.JointDesc["SolImpLimit"],
    )  # type: ignore
    solreffriction: FloatVectorProperty(
        name=def_props.JOINT_PROPS_NAME["solreffriction"],
        default=def_props.JOINT_PROPS_DEFAULT["solreffriction"],
        size=len(def_props.JOINT_PROPS_DEFAULT["solreffriction"]),
        precision=5,
        description=Description.JointDesc["SolRefFriction"],
    )  # type: ignore
    solimpfriction: FloatVectorProperty(
        name=def_props.JOINT_PROPS_NAME["solimpfriction"],
        default=def_props.JOINT_PROPS_DEFAULT["solimpfriction"],
        size=len(def_props.JOINT_PROPS_DEFAULT["solimpfriction"]),
        precision=5,
        description=Description.JointDesc["SolImpFriction"],
    )  # type: ignore
    stiffness: FloatProperty(
        name=def_props.JOINT_PROPS_NAME["stiffness"],
        default=def_props.JOINT_PROPS_DEFAULT["stiffness"],
        precision=5,
        description=Description.JointDesc["Stiffness"],
    )  # type: ignore
    range: FloatVectorProperty(
        name=def_props.JOINT_PROPS_NAME["range"],
        default=def_props.JOINT_PROPS_DEFAULT["range"],
        size=len(def_props.JOINT_PROPS_DEFAULT["range"]),
        precision=5,
        update=set_angle,
        description=Description.JointDesc["Range"],
    )  # type: ignore
    limited: EnumProperty(
        name=def_props.JOINT_PROPS_NAME["limited"],
        items=cons.Active_Types,
        default=def_props.JOINT_PROPS_DEFAULT["limited"],
        description=Description.JointDesc["Limited"],
    )  # type: ignore
    actuatorfrcrange: FloatVectorProperty(
        name=def_props.JOINT_PROPS_NAME["actuatorfrcrange"],
        default=def_props.JOINT_PROPS_DEFAULT["actuatorfrcrange"],
        size=len(def_props.JOINT_PROPS_DEFAULT["actuatorfrcrange"]),
        precision=5,
        description=Description.JointDesc["ActuatorFrcRange"],
    )  # type: ignore
    actuatorfrclimited: EnumProperty(
        name=def_props.JOINT_PROPS_NAME["actuatorfrclimited"],
        items=cons.Active_Types,
        default=def_props.JOINT_PROPS_DEFAULT["actuatorfrclimited"],
        description=Description.JointDesc["ActuatorFrcLimited"],
    )  # type: ignore
    margin: FloatProperty(
        name=def_props.JOINT_PROPS_NAME["margin"],
        default=def_props.JOINT_PROPS_DEFAULT["margin"],
        precision=5,
        description=Description.JointDesc["Margin"],
    )  # type: ignore
    ref: FloatProperty(
        name=def_props.JOINT_PROPS_NAME["ref"],
        default=def_props.JOINT_PROPS_DEFAULT["ref"],
        precision=5,
        description=Description.JointDesc["Ref"],
    )  # type: ignore
    springref: FloatProperty(
        name=def_props.JOINT_PROPS_NAME["springref"],
        default=def_props.JOINT_PROPS_DEFAULT["springref"],
        precision=5,
        description=Description.JointDesc["SpringRef"],
    )  # type: ignore
    armature: FloatProperty(
        name=def_props.JOINT_PROPS_NAME["armature"],
        default=def_props.JOINT_PROPS_DEFAULT["armature"],
        precision=5,
        description=Description.JointDesc["Armature"],
    )  # type: ignore
    damping: FloatProperty(
        name=def_props.JOINT_PROPS_NAME["damping"],
        default=def_props.JOINT_PROPS_DEFAULT["damping"],
        precision=5,
        description=Description.JointDesc["Damping"],
    )  # type: ignore
    frictionloss: FloatProperty(
        name=def_props.JOINT_PROPS_NAME["frictionloss"],
        default=def_props.JOINT_PROPS_DEFAULT["frictionloss"],
        precision=5,
        description=Description.JointDesc["FrictionLoss"],
    )  # type: ignore


# Contact
class ContactItem(PropertyGroup):
    """Represents a MuJoCo contact pair (exclude or pair) between two bodies."""

    def exclude_exist_poll1(self, obj):
        """Poll function to filter valid objects for the first target slot.

        Args:
            obj: The Blender object being considered.

        Returns:
            True if *obj* is a valid target for slot 1, False otherwise.
        """
        if self.target2 == obj:
            return False
        if self.type == cons.ContactTypes.EXCLUDE:
            return obj.Forge_Model_Type == cons.ModelTypes.LINK
        else:
            return obj.Forge_Model_Type in [
                cons.ModelTypes.VISUAL,
                cons.ModelTypes.COLLIDER,
                cons.ModelTypes.PLANE,
                cons.ModelTypes.HFIELD,
            ]

    def exclude_exist_poll2(self, obj):
        """Poll function to filter valid objects for the second target slot.

        Args:
            obj: The Blender object being considered.

        Returns:
            True if *obj* is a valid target for slot 2, False otherwise.
        """
        if self.target1 == obj:
            return False
        if self.type == cons.ContactTypes.EXCLUDE:
            return obj.Forge_Model_Type == cons.ModelTypes.LINK
        else:
            return obj.Forge_Model_Type in [
                cons.ModelTypes.VISUAL,
                cons.ModelTypes.COLLIDER,
                cons.ModelTypes.PLANE,
                cons.ModelTypes.HFIELD,
            ]

    def update_target_set(self, context: Context):
        """Clear target references when contact type changes.

        Args:
            context: The active Blender context.
        """
        if self.old_target_type == self.type:
            return

        self.target1 = None
        self.target2 = None
        self["old_target_type"] = self.type

    old_target_type: StringProperty(default="", description="Stores previous target type to detect changes")  # type: ignore

    type: EnumProperty(
        name="Contact Type",
        items=cons.Contact_Types,
        default="EXCLUDE",
        update=update_target_set,
        description=Description.ContactDesc["Type"],
    )  # type: ignore

    target1: PointerProperty(
        name="Target 1",
        type=Object,
        poll=exclude_exist_poll1,
        description=Description.ContactDesc["Target1"],
    )  # type: ignore
    target2: PointerProperty(
        name="Target 2",
        type=Object,
        poll=exclude_exist_poll2,
        description=Description.ContactDesc["Target2"],
    )  # type: ignore

    condim: IntProperty(
        name=def_props.CONTACT_PROPS_NAME["condim"],
        default=def_props.CONTACT_PROPS_DEFAULT["condim"],
        description=Description.ContactDesc["Condim"],
    )  # type: ignore
    friction: FloatVectorProperty(
        name=def_props.CONTACT_PROPS_NAME["friction"],
        default=def_props.CONTACT_PROPS_DEFAULT["friction"],
        size=len(def_props.CONTACT_PROPS_DEFAULT["friction"]),
        precision=5,
        description=Description.ContactDesc["Friction"],
    )  # type: ignore
    solref: FloatVectorProperty(
        name=def_props.CONTACT_PROPS_NAME["solref"],
        default=def_props.CONTACT_PROPS_DEFAULT["solref"],
        size=len(def_props.CONTACT_PROPS_DEFAULT["solref"]),
        precision=5,
        description=Description.ContactDesc["SolRef"],
    )  # type: ignore
    solreffriction: FloatVectorProperty(
        name=def_props.CONTACT_PROPS_NAME["solreffriction"],
        default=def_props.CONTACT_PROPS_DEFAULT["solreffriction"],
        size=len(def_props.CONTACT_PROPS_DEFAULT["solreffriction"]),
        precision=5,
        description=Description.ContactDesc["SolRefFriction"],
    )  # type: ignore
    margin: FloatProperty(
        name=def_props.CONTACT_PROPS_NAME["margin"],
        default=def_props.CONTACT_PROPS_DEFAULT["margin"],
        precision=5,
        description=Description.ContactDesc["Margin"],
    )  # type: ignore
    gap: FloatProperty(
        name=def_props.CONTACT_PROPS_NAME["gap"],
        default=def_props.CONTACT_PROPS_DEFAULT["gap"],
        precision=5,
        description=Description.ContactDesc["Gap"],
    )  # type: ignore


class SensorItem(PropertyGroup):
    """Represents a MuJoCo sensor with type, target, reference, and noise settings."""

    contact_reduce_types = (
        ("NONE", "None", ""),
        ("MINDIST", "Minimal distance", ""),
        ("MAXFORCE", "Maximal force", ""),
        ("NETFORCE", "Net force", ""),
    )

    contact_data = (
        ("found", "Found", ""),
        ("force", "Force", ""),
        ("torque", "Torque", ""),
        ("dist", "Dist", ""),
        ("pos", "Pos", ""),
        ("normal", "Normal", ""),
        ("tangent", "Tangent", ""),
    )

    def target_poll(self, obj):
        """Return True only for objects with Forge_Model_Type.

        Args:
            self: The owner of the PointerProperty (unused).
            obj: The object being considered for the pointer assignment.

        Returns:
            True if *obj* is a link model, False otherwise.
        """
        if self.type in [
            cons.SensorTypes.Framepos,
            cons.SensorTypes.Framequat,
            cons.SensorTypes.Framexaxis,
            cons.SensorTypes.Frameyaxis,
            cons.SensorTypes.Framezaxis,
            cons.SensorTypes.Framelinvel,
            cons.SensorTypes.Frameangvel,
        ]:
            if not self.use_xbody:
                return obj.Forge_Model_Type in [
                    cons.ModelTypes.LINK,
                    cons.ModelTypes.VISUAL,
                    cons.ModelTypes.COLLIDER,
                    cons.ModelTypes.SITE,
                    cons.ModelTypes.CAMERA,
                ]
            else:
                return obj.Forge_Model_Type == cons.ModelTypes.LINK

        if self.type in [
            cons.SensorTypes.Jointpos,
            cons.SensorTypes.Jointvel,
        ]:
            return obj.Forge_Model_Type == cons.ModelTypes.JOINT

        if self.type in [
            cons.SensorTypes.Touch,
            cons.SensorTypes.Accelerometer,
            cons.SensorTypes.Velocimeter,
            cons.SensorTypes.Gyro,
        ]:
            return obj.Forge_Model_Type == cons.ModelTypes.SITE

        if self.type in [
            cons.SensorTypes.Subtreecom,
            cons.SensorTypes.Subtreelinvel,
            cons.SensorTypes.Subtreeangmom,
        ]:
            return obj.Forge_Model_Type == cons.ModelTypes.LINK

        if self.type == cons.SensorTypes.Contact:
            if not self.use_subtree:
                return obj.Forge_Model_Type in [
                    cons.ModelTypes.LINK,
                    cons.ModelTypes.VISUAL,
                    cons.ModelTypes.COLLIDER,
                    cons.ModelTypes.SITE,
                ]
            else:
                return obj.Forge_Model_Type == cons.ModelTypes.LINK

    def ref_poll(self, obj):
        """Return whether *obj* is a valid reference for this sensor.

        Args:
            self: The owner of the PointerProperty (unused).
            obj: The object being considered for the pointer assignment.

        Returns:
            True if *obj* is a link model, False otherwise.
        """
        frame_sensor_types = {
            cons.SensorTypes.Framepos,
            cons.SensorTypes.Framequat,
            cons.SensorTypes.Framexaxis,
            cons.SensorTypes.Frameyaxis,
            cons.SensorTypes.Framezaxis,
            cons.SensorTypes.Framelinvel,
            cons.SensorTypes.Frameangvel,
        }
        if self.type in frame_sensor_types:
            # MuJoCo frame sensors only accept body/xbody/geom/site/camera
            # frames; joints do not define a spatial frame.
            return obj.Forge_Model_Type in {
                cons.ModelTypes.LINK,
                cons.ModelTypes.CAMERA,
                cons.ModelTypes.SITE,
                cons.ModelTypes.VISUAL,
                cons.ModelTypes.COLLIDER,
            }

        if self.type == cons.SensorTypes.Contact:
            if self.target_type in {
                cons.SensorTargetTypes.BODY,
                cons.SensorTargetTypes.XBODY,
                cons.SensorTargetTypes.SUBTREE,
            }:
                return obj.Forge_Model_Type == cons.ModelTypes.LINK
            if self.target_type == cons.SensorTargetTypes.GEOM:
                return obj.Forge_Model_Type in {cons.ModelTypes.VISUAL, cons.ModelTypes.COLLIDER}

        return False

    def check_target(self, context: Context):
        """Auto-detect and set the target type based on the first selected target object.

        Args:
            context: The active Blender context.
        """
        if self.target is None:
            return
        if self.use_xbody or self.use_subtree:
            return

        match self.target.Forge_Model_Type:
            case cons.ModelTypes.LINK:
                self.target_type = cons.SensorTargetTypes.BODY
            case cons.ModelTypes.SITE:
                self.target_type = cons.SensorTargetTypes.SITE
            case cons.ModelTypes.JOINT:
                self.target_type = cons.SensorTargetTypes.JOINT
            case cons.ModelTypes.CAMERA:
                self.target_type = cons.SensorTargetTypes.CAMERA
            case cons.ModelTypes.VISUAL | cons.ModelTypes.COLLIDER:
                self.target_type = cons.SensorTargetTypes.GEOM

    def check_ref(self, context: Context):
        """Auto-detect the independent MJCF reference type."""
        if self.ref is None:
            return
        if not self.ref_poll(self.ref):
            self.ref = None
            return
        match self.ref.Forge_Model_Type:
            case cons.ModelTypes.LINK:
                self.ref_type = cons.SensorTargetTypes.BODY
            case cons.ModelTypes.SITE:
                self.ref_type = cons.SensorTargetTypes.SITE
            case cons.ModelTypes.CAMERA:
                self.ref_type = cons.SensorTargetTypes.CAMERA
            case cons.ModelTypes.VISUAL | cons.ModelTypes.COLLIDER:
                self.ref_type = cons.SensorTargetTypes.GEOM

    def update_type(self, context: Context):
        """Drop targets that are invalid for the newly selected sensor type."""
        if self.target is not None and not self.target_poll(self.target):
            self.target = None
        if self.ref is not None and not self.ref_poll(self.ref):
            self.ref = None

    def update_contact_num(self, context: Context):
        self.num = 0
        for tag in self.data:
            self.num += def_props.SENSOR_CONTACT_DATA[tag]

    def update_xbody_type(self, context: Context):
        if self.use_xbody:
            self.target_type = cons.SensorTargetTypes.XBODY
            if self.target is None:
                return
            if self.target.Forge_Model_Type != cons.ModelTypes.LINK:
                self.target = None
                self.ref = None
        else:
            self.target_type = cons.SensorTargetTypes.BODY
            if self.target is None:
                return
            if self.target.Forge_Model_Type != cons.ModelTypes.LINK:
                self.target = None
                self.ref = None

    def update_subtree_type(self, context: Context):
        if self.use_subtree:
            self.target_type = cons.SensorTargetTypes.SUBTREE
            if self.target is None:
                return
            if self.target.Forge_Model_Type != cons.ModelTypes.LINK:
                self.target = None
                self.ref = None
        else:
            self.target_type = cons.SensorTargetTypes.BODY
            if self.target is None:
                return
            if self.target.Forge_Model_Type != cons.ModelTypes.LINK:
                self.target = None
                self.ref = None

    use_xbody: BoolProperty(
        name="Use Xbody",
        default=False,
        description="Xbody instead body",
        update=update_xbody_type,
    )  # type: ignore

    use_subtree: BoolProperty(
        name="Use Subtree",
        default=False,
        description="Subtree instead body",
        update=update_subtree_type,
    )  # type: ignore

    type: EnumProperty(
        name="Sensor Type",
        items=cons.Sensor_Types,
        default="Framepos",
        update=update_type,
        description=Description.SensorDesc["Type"],
    )  # type: ignore
    target_type: EnumProperty(
        name="Target Type",
        items=cons.Sensor_Target_Types,
        default="BODY",
        description=Description.SensorDesc["TargetType"],
    )  # type: ignore
    target: PointerProperty(
        name="Target",
        type=Object,
        poll=target_poll,
        update=check_target,
        description=Description.SensorDesc["Target"],
    )  # type: ignore

    ref_type: EnumProperty(
        name="Reference Type",
        items=cons.Sensor_Target_Types,
        default="BODY",
        description=Description.SensorDesc["RefType"],
    )  # type: ignore
    ref: PointerProperty(
        name="Reference",
        type=Object,
        poll=ref_poll,
        update=check_ref,
        description=Description.SensorDesc["Ref"],
    )  # type: ignore

    noise: FloatProperty(
        name=def_props.SENSOR_PROPS_NAME["noise"],
        default=def_props.SENSOR_PROPS_DEFAULT["noise"],
        precision=5,
        description=Description.SensorDesc["Noise"],
    )  # type: ignore
    cutoff: FloatProperty(
        name=def_props.SENSOR_PROPS_NAME["cutoff"],
        default=def_props.SENSOR_PROPS_DEFAULT["cutoff"],
        precision=5,
        description=Description.SensorDesc["Cutoff"],
    )  # type: ignore

    num: IntProperty(
        name=def_props.SENSOR_PROPS_NAME["num"],
        default=def_props.SENSOR_PROPS_DEFAULT["num"],
        description=Description.SensorDesc["Num"],
    )  # type: ignore
    data: EnumProperty(
        name=def_props.SENSOR_PROPS_NAME["data"],
        items=contact_data,
        options={"ENUM_FLAG"},
        default=def_props.SENSOR_PROPS_DEFAULT["data"],
        update=update_contact_num,
        description=Description.SensorDesc["Data"],
    )  # type: ignore
    reduce: EnumProperty(
        name=def_props.SENSOR_PROPS_NAME["reduce"],
        items=contact_reduce_types,
        default=def_props.SENSOR_PROPS_DEFAULT["reduce"],
        description=Description.SensorDesc["Reduce"],
    )  # type: ignore


# EqualityItem
class EqualityItem(PropertyGroup):
    """Represents a MuJoCo equality constraint (connect, weld, joint, tendon) between two objects."""

    def target_enum_size(self, context: Context):
        """Get the number of target slots needed for the current equality type.

        Args:
            context: The active Blender context (unused, required by Blender API).

        Returns:
            2 for CONNECT/WELD types, 1 for JOINT type.
        """
        return 2 if self.type != cons.EqualityTypes.JOINT else 1

    def exclude_exist_poll1(self, obj):
        """Poll function to filter valid objects for the first target slot.

        Args:
            obj: The Blender object being considered.

        Returns:
            True if *obj* is a valid target for slot 1, False otherwise.
        """
        if self.target2 == obj:
            return False
        if self.type != cons.EqualityTypes.JOINT:
            return obj.Forge_Model_Type in [cons.EqualityTargetTypes.LINK, cons.EqualityTargetTypes.SITE]
        else:
            return obj.Forge_Model_Type == cons.EqualityTargetTypes.JOINT

    def exclude_exist_poll2(self, obj):
        """Poll function to filter valid objects for the second target slot.

        Args:
            obj: The Blender object being considered.

        Returns:
            True if *obj* is a valid target for slot 2, False otherwise.
        """
        if self.target1 == obj:
            return False
        return obj.Forge_Model_Type == self.target_type

    def update_target_set(self, context: Context):
        """Clear target references when equality type changes and target count differs.

        Args:
            context: The active Blender context.
        """
        if self.type == cons.EqualityTypes.JOINT:
            self.target_type = cons.EqualityTargetTypes.JOINT
        elif self.target_type == cons.EqualityTargetTypes.JOINT:
            self.target_type = cons.EqualityTargetTypes.LINK

        num_enum = self.target_enum_size(context)
        if self.old_target_size == num_enum:
            return

        self.target1 = None
        self.target2 = None
        self["old_target_size"] = num_enum

    def check_target(self, context: Context):
        """Auto-detect and set the target type based on the first selected target object.

        Args:
            context: The active Blender context.
        """
        if self.target1 is None:
            return

        match self.target1.Forge_Model_Type:
            case cons.ModelTypes.LINK:
                self.target_type = cons.EqualityTargetTypes.LINK
            case cons.ModelTypes.SITE:
                self.target_type = cons.EqualityTargetTypes.SITE
            case cons.ModelTypes.JOINT:
                self.target_type = cons.EqualityTargetTypes.JOINT

        if self.target2 is None:
            return

        if self.target2.Forge_Model_Type != self.target1.Forge_Model_Type:
            self.target2 = None

    old_target_size: IntProperty(default=2, description="Stores previous target count to detect changes")  # type: ignore

    type: EnumProperty(
        name="Equality Type",
        items=cons.Equality_Types,
        default="CONNECT",
        update=update_target_set,
        description=Description.EqualityDesc["Type"],
    )  # type: ignore

    target_type: EnumProperty(
        name="Target Type",
        items=cons.Equality_Target_Types,
        default=0,
        description=Description.EqualityDesc["TargetType"],
    )  # type: ignore

    active: BoolProperty(name="Active", default=True, description=Description.EqualityDesc["Active"])  # type: ignore

    target1: PointerProperty(
        name="Target 1",
        type=Object,
        poll=exclude_exist_poll1,
        update=check_target,
        description=Description.EqualityDesc["Body1"],
    )  # type: ignore
    target2: PointerProperty(
        name="Target 2",
        type=Object,
        poll=exclude_exist_poll2,
        description=Description.EqualityDesc["Body2"],
    )  # type: ignore

    anchor: FloatVectorProperty(
        name=def_props.EQUALITY_PROPS_NAME["anchor"],
        default=def_props.EQUALITY_PROPS_DEFAULT["anchor"],
        size=len(def_props.EQUALITY_PROPS_DEFAULT["anchor"]),
        precision=5,
        description=Description.EqualityDesc["Anchor"],
    )  # type: ignore
    solref: FloatVectorProperty(
        name=def_props.EQUALITY_PROPS_NAME["solref"],
        default=def_props.EQUALITY_PROPS_DEFAULT["solref"],
        size=len(def_props.EQUALITY_PROPS_DEFAULT["solref"]),
        precision=5,
        description=Description.EqualityDesc["SolRef"],
    )  # type: ignore
    solimp: FloatVectorProperty(
        name=def_props.EQUALITY_PROPS_NAME["solimp"],
        default=def_props.EQUALITY_PROPS_DEFAULT["solimp"],
        size=len(def_props.EQUALITY_PROPS_DEFAULT["solimp"]),
        precision=5,
        description=Description.EqualityDesc["SolImp"],
    )  # type: ignore
    relpose: FloatVectorProperty(
        name=def_props.EQUALITY_PROPS_NAME["relpose"],
        default=def_props.EQUALITY_PROPS_DEFAULT["relpose"],
        size=len(def_props.EQUALITY_PROPS_DEFAULT["relpose"]),
        precision=5,
        description=Description.EqualityDesc["RelPose"],
    )  # type: ignore
    polycoef: FloatVectorProperty(
        name=def_props.EQUALITY_PROPS_NAME["polycoef"],
        default=def_props.EQUALITY_PROPS_DEFAULT["polycoef"],
        size=len(def_props.EQUALITY_PROPS_DEFAULT["polycoef"]),
        precision=5,
        description=Description.EqualityDesc["PolyCoef"],
    )  # type: ignore


# Tendon
class TendonTargetItem(PropertyGroup):
    """Represents a single target site in a tendon path with its weighting coefficient."""

    target: PointerProperty(
        name="Target",
        type=Object,
        poll=select.tendon_target_only_poll,
        description=Description.TendonTargetDesc["Target"],
    )  # type: ignore
    coef: FloatProperty(name="Coef", default=0.5, description=Description.TendonTargetDesc["Coef"])  # type: ignore


class TendonTargetList(PropertyGroup):
    """Collection of tendon target items that form a complete tendon path."""

    items: CollectionProperty(type=TendonTargetItem, description="List of tendon target site items")  # type: ignore
    active_index: IntProperty(description="Index of the active tendon target item")  # type: ignore


class FORGE_UL_TendonTargetList(UIList):
    """Custom UIList for displaying tendon target site items."""

    def draw_item(self, context: Context, layout, data, item, icon, active_data, active_propname, index):
        """Draw each tendon target item row in the list UI."""
        row = layout.row().split(factor=0.6)
        row.prop(item, "target", text="")
        row.prop(item, "coef", text="")


class Forge_OT_TendonTargetItemAdd(Operator):
    """Operator to add a new target site to the active tendon's path."""

    bl_idname = "forge.add_tendon_target_item"
    bl_label = "Add Tendon Target"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context: Context):
        """Execute the add tendon target item operation."""
        data = context.active_object.Forge_Tendon.targets
        _item = data.items.add()
        data.active_index = len(data.items) - 1
        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        obj = context.active_object
        return obj is not None and obj.Forge_Model_Type == cons.ModelTypes.TENDON


class Forge_OT_TendonTargetItemRemove(Operator):
    """Operator to remove the active target site from the active tendon's path."""

    bl_idname = "forge.remove_tendon_target_item"
    bl_label = "Remove Tendon Target"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context: Context):
        """Execute the remove tendon target item operation."""
        data = context.active_object.Forge_Tendon.targets
        if 0 <= data.active_index < len(data.items):
            data.items.remove(data.active_index)
            data.active_index = max(0, data.active_index - 1)
        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        obj = context.active_object
        return obj is not None and obj.Forge_Model_Type == cons.ModelTypes.TENDON


class TendonItem(PropertyGroup):
    """Represents a MuJoCo tendon with target path, range, stiffness, damping, and solver properties."""

    # Target_Types: site only
    Target_Types = (("SITE", "Site", ""),)

    type: EnumProperty(
        name="Tendon Type", items=cons.Tendon_Types, default="FIXED", description=Description.TendonDesc["Type"]
    )  # type: ignore
    targets: PointerProperty(name="Targets", type=TendonTargetList, description=Description.TendonDesc["Targets"])  # type: ignore

    range: FloatVectorProperty(
        name=def_props.TENDON_PROPS_NAME["range"],
        default=def_props.TENDON_PROPS_DEFAULT["range"],
        size=len(def_props.TENDON_PROPS_DEFAULT["range"]),
        precision=5,
        description=Description.TendonDesc["Range"],
    )  # type: ignore
    limited: EnumProperty(
        name=def_props.TENDON_PROPS_NAME["limited"],
        items=cons.Active_Types,
        default=def_props.TENDON_PROPS_DEFAULT["limited"],
        description=Description.TendonDesc["Limited"],
    )  # type: ignore
    solreflimit: FloatVectorProperty(
        name=def_props.TENDON_PROPS_NAME["solreflimit"],
        default=def_props.TENDON_PROPS_DEFAULT["solreflimit"],
        size=len(def_props.TENDON_PROPS_DEFAULT["solreflimit"]),
        precision=5,
        description=Description.TendonDesc["SolRefLimit"],
    )  # type: ignore
    solimplimit: FloatVectorProperty(
        name=def_props.TENDON_PROPS_NAME["solimplimit"],
        default=def_props.TENDON_PROPS_DEFAULT["solimplimit"],
        size=len(def_props.TENDON_PROPS_DEFAULT["solimplimit"]),
        precision=5,
        description=Description.TendonDesc["SolImpLimit"],
    )  # type: ignore
    springlength: FloatVectorProperty(
        name=def_props.TENDON_PROPS_NAME["springlength"],
        default=def_props.TENDON_PROPS_DEFAULT["springlength"],
        size=len(def_props.TENDON_PROPS_DEFAULT["springlength"]),
        precision=5,
        description=Description.TendonDesc["SpringLength"],
    )  # type: ignore
    stiffness: FloatProperty(
        name=def_props.TENDON_PROPS_NAME["stiffness"],
        default=def_props.TENDON_PROPS_DEFAULT["stiffness"],
        precision=5,
        description=Description.TendonDesc["Stiffness"],
    )  # type: ignore
    damping: FloatProperty(
        name=def_props.TENDON_PROPS_NAME["damping"],
        default=def_props.TENDON_PROPS_DEFAULT["damping"],
        precision=5,
        description=Description.TendonDesc["Damping"],
    )  # type: ignore


# ActuatorItem
class ActuatorItem(PropertyGroup):
    """Represents a MuJoCo actuator with type, target, gain, bias, and force settings."""

    def target_enum_items(self, context: Context):
        """Build a dynamic enum list of valid target objects matching the current target type.

        Args:
            context: The active Blender context.

        Returns:
            A list of enum item tuples ``(identifier, name, description)``.
        """
        items = []
        for t in bpy.data.objects:
            if t.Forge_Model_Type == self.target_type:
                items.append(t)
        return [(item.name, item.name, "") for item in items] or [("NONE", "None", "")]

    def check_target(self, context: Context):
        """Auto-detect the target type from the selected target object.

        Args:
            context: The active Blender context.
        """
        if self.target is None:
            return
        match self.target.Forge_Model_Type:
            case cons.ModelTypes.JOINT:
                self.target_type = cons.ActuatorTargetTypes.JOINT
            case cons.ModelTypes.TENDON:
                self.target_type = cons.ActuatorTargetTypes.TENDON
            case cons.ModelTypes.LINK:
                self.target_type = cons.ActuatorTargetTypes.LINK
            case cons.ModelTypes.SITE:
                self.target_type = cons.ActuatorTargetTypes.SITE

    type: EnumProperty(
        name="Actuator Type",
        items=cons.Actuator_Types,
        default="POSITION",
        description=Description.ActuatorDesc["Type"],
    )  # type: ignore
    target_type: EnumProperty(
        name="Target Type",
        items=cons.Actuator_Target_Types,
        default="JOINT",
        description=Description.ActuatorDesc["TargetType"],
    )  # type: ignore

    target: PointerProperty(
        name="Target",
        type=Object,
        poll=select.actuator_target_poll,
        update=check_target,
        description=Description.ActuatorDesc["Target"],
    )  # type: ignore

    ctrllimited: EnumProperty(
        name=def_props.ACTUATOR_PROPS_NAME["ctrllimited"],
        items=cons.Active_Types,
        default=def_props.ACTUATOR_PROPS_DEFAULT["ctrllimited"],
        description=Description.ActuatorDesc["CtrlLimited"],
    )  # type: ignore
    forcelimited: EnumProperty(
        name=def_props.ACTUATOR_PROPS_NAME["forcelimited"],
        items=cons.Active_Types,
        default=def_props.ACTUATOR_PROPS_DEFAULT["forcelimited"],
        description=Description.ActuatorDesc["ForceLimited"],
    )  # type: ignore
    ctrlrange: FloatVectorProperty(
        name=def_props.ACTUATOR_PROPS_NAME["ctrlrange"],
        default=def_props.ACTUATOR_PROPS_DEFAULT["ctrlrange"],
        size=len(def_props.ACTUATOR_PROPS_DEFAULT["ctrlrange"]),
        precision=5,
        description=Description.ActuatorDesc["CtrlRange"],
    )  # type: ignore
    forcerange: FloatVectorProperty(
        name=def_props.ACTUATOR_PROPS_NAME["forcerange"],
        default=def_props.ACTUATOR_PROPS_DEFAULT["forcerange"],
        size=len(def_props.ACTUATOR_PROPS_DEFAULT["forcerange"]),
        precision=5,
        description=Description.ActuatorDesc["ForceRange"],
    )  # type: ignore
    gear: FloatVectorProperty(
        name=def_props.ACTUATOR_PROPS_NAME["gear"],
        default=def_props.ACTUATOR_PROPS_DEFAULT["gear"],
        size=len(def_props.ACTUATOR_PROPS_DEFAULT["gear"]),
        precision=5,
        description=Description.ActuatorDesc["Gear"],
    )  # type: ignore
    gaintype: EnumProperty(
        name=def_props.ACTUATOR_PROPS_NAME["gaintype"],
        items=cons.Gain_Types,
        default=def_props.ACTUATOR_PROPS_DEFAULT["gaintype"],
        description=Description.ActuatorDesc["GainType"],
    )  # type: ignore
    biastype: EnumProperty(
        name=def_props.ACTUATOR_PROPS_NAME["biastype"],
        items=cons.Bias_Types,
        default=def_props.ACTUATOR_PROPS_DEFAULT["biastype"],
        description=Description.ActuatorDesc["BiasType"],
    )  # type: ignore
    dynprm: FloatVectorProperty(
        name=def_props.ACTUATOR_PROPS_NAME["dynprm"],
        default=def_props.ACTUATOR_PROPS_DEFAULT["dynprm"],
        size=len(def_props.ACTUATOR_PROPS_DEFAULT["dynprm"]),
        precision=5,
        description=Description.ActuatorDesc["DynPrm"],
    )  # type: ignore
    gainprm: FloatVectorProperty(
        name=def_props.ACTUATOR_PROPS_NAME["gainprm"],
        default=def_props.ACTUATOR_PROPS_DEFAULT["gainprm"],
        size=len(def_props.ACTUATOR_PROPS_DEFAULT["gainprm"]),
        precision=5,
        description=Description.ActuatorDesc["GainPrm"],
    )  # type: ignore
    biasprm: FloatVectorProperty(
        name=def_props.ACTUATOR_PROPS_NAME["biasprm"],
        default=def_props.ACTUATOR_PROPS_DEFAULT["biasprm"],
        size=len(def_props.ACTUATOR_PROPS_DEFAULT["biasprm"]),
        precision=5,
        description=Description.ActuatorDesc["BiasPrm"],
    )  # type: ignore
    kp: FloatProperty(
        name=def_props.ACTUATOR_PROPS_NAME["kp"],
        default=def_props.ACTUATOR_PROPS_DEFAULT["kp"],
        precision=5,
        description=Description.ActuatorDesc["Kp"],
    )  # type: ignore
    kv: FloatProperty(
        name=def_props.ACTUATOR_PROPS_NAME["kv"],
        default=def_props.ACTUATOR_PROPS_DEFAULT["kv"],
        precision=5,
        description=Description.ActuatorDesc["Kv"],
    )  # type: ignore
    inheritrange: FloatProperty(
        name=def_props.ACTUATOR_PROPS_NAME["inheritrange"],
        default=def_props.ACTUATOR_PROPS_DEFAULT["inheritrange"],
        precision=5,
        description=Description.ActuatorDesc["InheritRange"],
    )  # type: ignore
    gain: FloatProperty(
        name=def_props.ACTUATOR_PROPS_NAME["gain"],
        default=def_props.ACTUATOR_PROPS_DEFAULT["gain"],
        precision=5,
        description=Description.ActuatorDesc["Gain"],
    )  # type: ignore


# Lights
class LightItem(PropertyGroup):
    """Represents a MuJoCo light source with type and tracking mode."""

    def set_light_type(self, context: Context):
        """Update the Blender light object type based on the selected MuJoCo light type.

        Args:
            context: The active Blender context.
        """
        obj = self.id_data
        match self.type:
            case cons.LightTypes.DIRECTIONAL:
                obj.data.type = "SUN"
                if obj.parent:
                    obj.parent = None
                    coll_tag = "World"
                    collection = None
                    if coll_tag in bpy.data.collections:
                        collection = bpy.data.collections[coll_tag]
                    else:
                        collection = bpy.data.collections.new(coll_tag)
                        context.scene.collection.children.link(collection)
                    link_collection(obj, collection)
            case _:
                obj.data.type = self.type

    def set_light_mode(self, context: Context):
        """Clear the target when switching to fixed or track mode.

        Args:
            context: The active Blender context.
        """
        if self.mode in [cons.TargetModes.FIXED, cons.TargetModes.TRACK]:
            self.target = None

    type: EnumProperty(
        name="Type",
        items=cons.Light_Types,
        default=0,
        update=set_light_type,
        description=Description.LightDesc["Type"],
    )  # type: ignore
    mode: EnumProperty(
        name="Mode",
        items=cons.Target_Modes,
        default="FIXED",
        update=set_light_mode,
        description=Description.LightDesc["Mode"],
    )  # type: ignore
    target: PointerProperty(
        name="Target",
        type=Object,
        poll=select.link_only_poll,
        description=Description.LightDesc["Target"],
    )  # type: ignore


# Camera
class CameraItem(PropertyGroup):
    """Represents a MuJoCo camera with projection type and tracking mode."""

    def set_camera_type(self, context: Context):
        """Update the Blender camera type based on the selected MuJoCo camera type.

        Args:
            context: The active Blender context.
        """
        obj = self.id_data
        obj.data.type = self.type[0:5].upper()

    def set_camera_mode(self, context: Context):
        """Clear the target when switching to fixed or track mode.

        Args:
            context: The active Blender context.
        """
        if self.mode in [cons.TargetModes.FIXED, cons.TargetModes.TRACK]:
            self.target = None

    type: EnumProperty(
        name="Camera Type",
        items=cons.Camera_Types,
        default="PERSPECTIVE",
        update=set_camera_type,
        description=Description.CameraDesc["Type"],
    )  # type: ignore
    mode: EnumProperty(
        name="Mode",
        items=cons.Target_Modes,
        default="FIXED",
        update=set_camera_mode,
        description=Description.CameraDesc["Mode"],
    )  # type: ignore
    target: PointerProperty(
        name="Target",
        type=Object,
        poll=select.link_only_poll,
        description=Description.CameraDesc["Target"],
    )  # type: ignore


# Inertial
class InertialItem(PropertyGroup):
    """Represents the inertial properties (mass, diagonal inertia, full inertia) of a body."""

    def update_display(self, context):
        from .inertial import update_empty_display

        update_empty_display(self.id_data)

    def get_fullinertia(self):
        from .inertial import full_tensor

        tensor = full_tensor(self.id_data)
        return tuple(tensor[i][j] for i, j in ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)))

    def set_fullinertia(self, values):
        """Convert a link-frame tensor into the editable principal frame."""
        from ..ops.inertia import has_three_equal_moments, principal_axis_properties, stable_axes_from_z
        from .inertial import local_frame

        xx, yy, zz, xy, xz, yz = values
        tensor = Matrix(((xx, xy, xz), (xy, yy, yz), (xz, yz, zz)))
        moments, _, diagonal, axes, degenerate = principal_axis_properties(lambda *_: None, tensor)
        if any(value <= 0 for value in moments):
            if not any(values):
                self.diaginertia = (0.0, 0.0, 0.0)
                return
            raise ValueError("Full inertia must be positive definite")
        obj = self.id_data
        frame = local_frame(obj)
        if degenerate:
            reference = frame.to_quaternion().to_matrix()
            axes = reference if has_three_equal_moments(moments) else stable_axes_from_z(axes.col[2], reference)
        # Keep the physical pose parent-relative; no preview scale enters it.
        obj.matrix_parent_inverse = Matrix.Identity(4)
        obj.matrix_basis = Matrix.LocRotScale(frame.translation, axes.to_quaternion(), (1, 1, 1))
        self.diaginertia = diagonal

    mass: FloatProperty(
        name=def_props.INERTIAL_PROPS_NAME["mass"],
        default=def_props.INERTIAL_PROPS_DEFAULT["mass"],
        precision=5,
        description=Description.InertialDesc["Mass"],
        update=update_display,
    )  # type: ignore
    diaginertia: FloatVectorProperty(
        name=def_props.INERTIAL_PROPS_NAME["diaginertia"],
        default=def_props.INERTIAL_PROPS_DEFAULT["diaginertia"],
        size=len(def_props.INERTIAL_PROPS_DEFAULT["diaginertia"]),
        precision=5,
        description=Description.InertialDesc["DiagInertia"],
        update=update_display,
    )  # type: ignore
    fullinertia: FloatVectorProperty(
        name=def_props.INERTIAL_PROPS_NAME["fullinertia"],
        default=def_props.INERTIAL_PROPS_DEFAULT["fullinertia"],
        size=len(def_props.INERTIAL_PROPS_DEFAULT["fullinertia"]),
        precision=5,
        description=Description.InertialDesc["FullInertia"],
        get=get_fullinertia,
        set=set_fullinertia,
    )  # type: ignore


class AttachItem(PropertyGroup):
    """Represents an attachment configuration for including external models into the scene."""

    model: StringProperty(name="Model", default="", description=Description.AttachDesc["Model"])  # type: ignore
    file: StringProperty(name="File", default="", subtype="FILE_PATH", description=Description.AttachDesc["File"])  # type: ignore
    link: StringProperty(name="Body", default="", description=Description.AttachDesc["Body"])  # type: ignore
    prefix: StringProperty(name="Prefix", default="ATT_", description=Description.AttachDesc["Prefix"])  # type: ignore


class ReplicateItem(PropertyGroup):
    """Represents replication settings for creating patterned copies of objects."""

    count: IntProperty(
        name=def_props.REPLICATE_PROPS_NAME["count"],
        default=def_props.REPLICATE_PROPS_DEFAULT["count"],
        subtype="UNSIGNED",
        description=Description.ReplicateDesc["Count"],
    )  # type: ignore
    sep: StringProperty(
        name=def_props.REPLICATE_PROPS_NAME["sep"],
        default=def_props.REPLICATE_PROPS_DEFAULT["sep"],
        description=Description.ReplicateDesc["Sep"],
    )  # type: ignore
    offset: FloatVectorProperty(
        name=def_props.REPLICATE_PROPS_NAME["offset"],
        default=def_props.REPLICATE_PROPS_DEFAULT["offset"],
        size=len(def_props.REPLICATE_PROPS_DEFAULT["offset"]),
        subtype="TRANSLATION",
        description=Description.ReplicateDesc["Offset"],
    )  # type: ignore
    euler: FloatVectorProperty(
        name=def_props.REPLICATE_PROPS_NAME["euler"],
        default=def_props.REPLICATE_PROPS_DEFAULT["euler"],
        size=len(def_props.REPLICATE_PROPS_DEFAULT["euler"]),
        subtype="EULER",
        description=Description.ReplicateDesc["Euler"],
    )  # type: ignore


class IncludeItem(PropertyGroup):
    """Represents a reference to include an external XML or raw file in the model."""

    file: StringProperty(name="File", default="", subtype="FILE_PATH", description=Description.IncludeDesc["File"])  # type: ignore
    rawfile: StringProperty(
        name="Raw File", default="", subtype="FILE_PATH", description=Description.IncludeDesc["RawFile"]
    )  # type: ignore


class CompilerItem(PropertyGroup):
    """Compiler configuration controlling how the model is compiled during export."""

    angle_types = (
        ("RADIAN", "Radian", ""),
        ("DEGREE", "Degree", ""),
    )

    euler_sequence = (
        ("XYZ", "XYZ", ""),
        ("XZY", "XZY", ""),
        ("YXZ", "YXZ", ""),
        ("YZX", "YZX", ""),
        ("ZXY", "ZXY", ""),
        ("ZYX", "ZYX", ""),
    )

    autolimits: BoolProperty(name="Auto limits", default=True, description=Description.CompilerDesc["AutoLimits"])  # type: ignore
    angle: EnumProperty(
        name="Angle Type",
        items=angle_types,
        default="DEGREE",
        description=Description.CompilerDesc["Angle"],
    )  # type: ignore
    eulerseq: EnumProperty(
        name="Euler Sequence",
        items=euler_sequence,
        default="XYZ",
        description=Description.CompilerDesc["EulerSeq"],
    )  # type: ignore
    assetdir: StringProperty(name="Asset path", default="", description=Description.CompilerDesc["AssetDir"])  # type: ignore
    meshdir: StringProperty(name="Mesh path", default="", description=Description.CompilerDesc["MeshDir"])  # type: ignore
    texturedir: StringProperty(name="Texture path", default="", description=Description.CompilerDesc["TextureDir"])  # type: ignore

    def reset(self):
        """Reset all compiler properties to their default values."""
        _reset_from(self, def_props.COMPILER_PROPS_DEFAULT)


class GlobalItem(PropertyGroup):
    """Global visualization settings including projection, field of view, and camera angles."""

    orthographic: BoolProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Global]["orthographic"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Global]["orthographic"],
        description=Description.VisualDesc["Orthographic"],
    )  # type: ignore
    fovy: FloatProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Global]["fovy"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Global]["fovy"],
        subtype="ANGLE",
        description=Description.VisualDesc["Fovy"],
    )  # type: ignore
    azimuth: FloatProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Global]["azimuth"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Global]["azimuth"],
        subtype="ANGLE",
        description=Description.VisualDesc["Azimuth"],
    )  # type: ignore
    elevation: FloatProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Global]["elevation"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Global]["elevation"],
        subtype="ANGLE",
        description=Description.VisualDesc["Elevation"],
    )  # type: ignore

    def reset(self):
        """Reset all global visual properties to their default values."""
        _reset_from(self, def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Global])


class HeadlightItem(PropertyGroup):
    """Headlight visualization settings controlling ambient, diffuse, and specular lighting."""

    active: BoolProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Headlight]["active"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Headlight]["active"],
        description=Description.VisualDesc["Active"],
    )  # type: ignore
    ambient: FloatVectorProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Headlight]["ambient"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Headlight]["ambient"],
        min=0.0,
        max=1.0,
        size=3,
        subtype="COLOR",
        description=Description.VisualDesc["Ambient"],
    )  # type: ignore
    diffuse: FloatVectorProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Headlight]["diffuse"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Headlight]["diffuse"],
        min=0.0,
        max=1.0,
        size=3,
        subtype="COLOR",
        description=Description.VisualDesc["Diffuse"],
    )  # type: ignore
    specular: FloatVectorProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Headlight]["specular"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Headlight]["specular"],
        min=0.0,
        max=1.0,
        size=3,
        subtype="COLOR",
        description=Description.VisualDesc["Specular"],
    )  # type: ignore

    def reset(self):
        """Reset all headlight properties to their default values."""
        _reset_from(self, def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Headlight])


class MapItem(PropertyGroup):
    """Visual map settings for fog start / end distances and near / far clipping planes."""

    fogstart: FloatProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Map]["fogstart"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Map]["fogstart"],
        precision=5,
        description=Description.VisualDesc["FogStart"],
    )  # type: ignore
    fogend: FloatProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Map]["fogend"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Map]["fogend"],
        precision=5,
        description=Description.VisualDesc["FogEnd"],
    )  # type: ignore
    znear: FloatProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Map]["znear"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Map]["znear"],
        precision=5,
        description=Description.VisualDesc["ZNear"],
    )  # type: ignore
    zfar: FloatProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Map]["zfar"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Map]["zfar"],
        precision=5,
        description=Description.VisualDesc["ZFar"],
    )  # type: ignore

    def reset(self):
        """Reset all map properties to their default values."""
        _reset_from(self, def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Map])


class RgbaItem(PropertyGroup):
    """Color (RGBA) settings for various visualization elements (fog, haze, joint, bound volume, contact force)."""

    fog: FloatVectorProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Rgba]["fog"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Rgba]["fog"],
        min=0.0,
        max=1.0,
        size=4,
        subtype="COLOR",
        description=Description.VisualDesc["Fog"],
    )  # type: ignore
    haze: FloatVectorProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Rgba]["haze"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Rgba]["haze"],
        min=0.0,
        max=1.0,
        size=4,
        subtype="COLOR",
        description=Description.VisualDesc["Haze"],
    )  # type: ignore
    joint: FloatVectorProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Rgba]["joint"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Rgba]["joint"],
        min=0.0,
        max=1.0,
        size=4,
        subtype="COLOR",
        description=Description.VisualDesc["Joint"],
    )  # type: ignore
    bv: FloatVectorProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Rgba]["bv"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Rgba]["bv"],
        min=0.0,
        max=1.0,
        size=4,
        subtype="COLOR",
        description=Description.VisualDesc["BV"],
    )  # type: ignore
    contactforce: FloatVectorProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Rgba]["contactforce"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Rgba]["contactforce"],
        min=0.0,
        max=1.0,
        size=4,
        subtype="COLOR",
        description=Description.VisualDesc["ContactForce"],
    )  # type: ignore

    def reset(self):
        """Reset all RGBA color properties to their default values."""
        _reset_from(self, def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Rgba])


class QualityItem(PropertyGroup):
    """Quality settings affecting rendering fidelity and performance."""

    shadowsize: IntProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Quality]["shadowsize"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Quality]["shadowsize"],
        description=Description.QualityDesc["ShadowSize"],
    )  # type: ignore
    pointshadowsize: IntProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Quality]["pointshadowsize"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Quality]["pointshadowsize"],
        description=Description.QualityDesc["PointShadowSize"],
    )  # type: ignore

    def reset(self):
        """Reset all quality properties to their default values."""
        _reset_from(self, def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Quality])


class TonemappingItem(PropertyGroup):
    """Tonemapping settings controlling the method applied during rendering."""

    method: EnumProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Tonemapping]["method"],
        items=cons.Tonemapping_Methods,
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Tonemapping]["method"],
        description=Description.TonemappingDesc["Method"],
    )  # type: ignore

    def reset(self):
        """Reset all tonemapping properties to their default values."""
        _reset_from(self, def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Tonemapping])


class SsgiItem(PropertyGroup):
    """Screen-space global illumination (SSGI) post-processing settings."""

    active: BoolProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Ssgi]["active"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Ssgi]["active"],
        description=Description.SsgiDesc["Active"],
    )  # type: ignore
    resolutionscale: IntProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Ssgi]["resolutionscale"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Ssgi]["resolutionscale"],
        description=Description.SsgiDesc["ResolutionScale"],
    )  # type: ignore
    raycount: IntProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Ssgi]["raycount"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Ssgi]["raycount"],
        description=Description.SsgiDesc["RayCount"],
    )  # type: ignore
    stepcount: IntProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Ssgi]["stepcount"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Ssgi]["stepcount"],
        description=Description.SsgiDesc["StepCount"],
    )  # type: ignore
    thickness: FloatProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Ssgi]["thickness"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Ssgi]["thickness"],
        precision=5,
        description=Description.SsgiDesc["Thickness"],
    )  # type: ignore
    intensity: FloatProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Ssgi]["intensity"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Ssgi]["intensity"],
        precision=5,
        description=Description.SsgiDesc["Intensity"],
    )  # type: ignore
    gidenoiseoffset: IntProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Ssgi]["gidenoiseoffset"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Ssgi]["gidenoiseoffset"],
        description=Description.SsgiDesc["GiDenoiseOffset"],
    )  # type: ignore
    rraycount: IntProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Ssgi]["rraycount"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Ssgi]["rraycount"],
        description=Description.SsgiDesc["RRayCount"],
    )  # type: ignore
    rdenoiseoffset: IntProperty(
        name=def_props.VISUAL_PROPS_NAME[cons.VisualConfigTypes.Ssgi]["rdenoiseoffset"],
        default=def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Ssgi]["rdenoiseoffset"],
        description=Description.SsgiDesc["RDenoiseOffset"],
    )  # type: ignore

    def reset(self):
        """Reset all SSGI properties to their default values."""
        _reset_from(self, def_props.VISUAL_PROPS_DEFAULT[cons.VisualConfigTypes.Ssgi])


class FlagItem(PropertyGroup):
    """Physics engine visualization flags for enabling or disabling various debug renders."""

    constraint: BoolProperty(
        name=def_props.FLAG_PROPS_NAME["constraint"],
        default=def_props.FLAG_PROPS_DEFAULT["constraint"],
        description=Description.OptionFlagDesc["Constraint"],
    )  # type: ignore
    equality: BoolProperty(
        name=def_props.FLAG_PROPS_NAME["equality"],
        default=def_props.FLAG_PROPS_DEFAULT["equality"],
        description=Description.OptionFlagDesc["Equality"],
    )  # type: ignore
    frictionloss: BoolProperty(
        name=def_props.FLAG_PROPS_NAME["frictionloss"],
        default=def_props.FLAG_PROPS_DEFAULT["frictionloss"],
        description=Description.OptionFlagDesc["FrictionLoss"],
    )  # type: ignore
    limit: BoolProperty(
        name=def_props.FLAG_PROPS_NAME["limit"],
        default=def_props.FLAG_PROPS_DEFAULT["limit"],
        description=Description.OptionFlagDesc["Limit"],
    )  # type: ignore
    contact: BoolProperty(
        name=def_props.FLAG_PROPS_NAME["contact"],
        default=def_props.FLAG_PROPS_DEFAULT["contact"],
        description=Description.OptionFlagDesc["Contact"],
    )  # type: ignore
    gravity: BoolProperty(
        name=def_props.FLAG_PROPS_NAME["gravity"],
        default=def_props.FLAG_PROPS_DEFAULT["gravity"],
        description=Description.OptionFlagDesc["Gravity"],
    )  # type: ignore
    actuation: BoolProperty(
        name=def_props.FLAG_PROPS_NAME["actuation"],
        default=def_props.FLAG_PROPS_DEFAULT["actuation"],
        description=Description.OptionFlagDesc["Actuation"],
    )  # type: ignore
    refsafe: BoolProperty(
        name=def_props.FLAG_PROPS_NAME["refsafe"],
        default=def_props.FLAG_PROPS_DEFAULT["refsafe"],
        description=Description.OptionFlagDesc["RefSafe"],
    )  # type: ignore
    override: BoolProperty(
        name=def_props.FLAG_PROPS_NAME["override"],
        default=def_props.FLAG_PROPS_DEFAULT["override"],
        description=Description.OptionFlagDesc["Override"],
    )  # type: ignore

    def reset(self):
        """Reset all flag properties to their default values."""
        _reset_from(self, def_props.FLAG_PROPS_DEFAULT)


class OptionItem(PropertyGroup):
    """Physics engine option settings: timestep, solver iterations, tolerance, gravity, and solver parameters."""

    timestep: FloatProperty(
        name=def_props.OPTION_PROPS_NAME["timestep"],
        default=def_props.OPTION_PROPS_DEFAULT["timestep"],
        precision=5,
        description=Description.OptionDesc["TimeStep"],
    )  # type: ignore
    iterations: IntProperty(
        name=def_props.OPTION_PROPS_NAME["iterations"],
        default=def_props.OPTION_PROPS_DEFAULT["iterations"],
        description=Description.OptionDesc["Iterations"],
    )  # type: ignore
    tolerance: FloatProperty(
        name=def_props.OPTION_PROPS_NAME["tolerance"],
        default=def_props.OPTION_PROPS_DEFAULT["tolerance"],
        precision=10,
        description=Description.OptionDesc["Tolerance"],
    )  # type: ignore
    gravity: FloatVectorProperty(
        name=def_props.OPTION_PROPS_NAME["gravity"],
        default=def_props.OPTION_PROPS_DEFAULT["gravity"],
        size=len(def_props.OPTION_PROPS_DEFAULT["gravity"]),
        precision=5,
        description=Description.OptionDesc["Gravity"],
    )  # type: ignore
    o_solref: FloatVectorProperty(
        name=def_props.OPTION_PROPS_NAME["o_solref"],
        default=def_props.OPTION_PROPS_DEFAULT["o_solref"],
        size=len(def_props.OPTION_PROPS_DEFAULT["o_solref"]),
        precision=5,
        description=Description.OptionDesc["OSolRef"],
    )  # type: ignore
    o_solimp: FloatVectorProperty(
        name=def_props.OPTION_PROPS_NAME["o_solimp"],
        default=def_props.OPTION_PROPS_DEFAULT["o_solimp"],
        size=len(def_props.OPTION_PROPS_DEFAULT["o_solimp"]),
        precision=5,
        description=Description.OptionDesc["OSolImp"],
    )  # type: ignore
    o_friction: FloatVectorProperty(
        name=def_props.OPTION_PROPS_NAME["o_friction"],
        default=def_props.OPTION_PROPS_DEFAULT["o_friction"],
        size=len(def_props.OPTION_PROPS_DEFAULT["o_friction"]),
        precision=5,
        description=Description.OptionDesc["OFriction"],
    )  # type: ignore
    o_margin: FloatProperty(
        name=def_props.OPTION_PROPS_NAME["o_margin"],
        default=def_props.OPTION_PROPS_DEFAULT["o_margin"],
        precision=5,
        description=Description.OptionDesc["OMargin"],
    )  # type: ignore
    flag: PointerProperty(
        name=def_props.OPTION_PROPS_NAME["flag"], type=FlagItem, description=Description.OptionFlagDesc["Element"]
    )  # type: ignore

    def reset(self):
        """Reset all option properties to their default values."""
        _reset_from(self, def_props.OPTION_PROPS_DEFAULT, skip_keys=frozenset({"flag"}))
        self.flag.reset()


class StatisticItem(PropertyGroup):
    """Model statistics including extent (bounding radius) and center position."""

    extent: FloatProperty(
        name=def_props.STATISTIC_PROPS_NAME["extent"],
        default=def_props.STATISTIC_PROPS_DEFAULT["extent"],
        precision=5,
        description=Description.StatisticDesc["Extent"],
    )  # type: ignore
    center: FloatVectorProperty(
        name=def_props.STATISTIC_PROPS_NAME["center"],
        default=def_props.STATISTIC_PROPS_DEFAULT["center"],
        size=len(def_props.STATISTIC_PROPS_DEFAULT["center"]),
        precision=5,
        description=Description.StatisticDesc["Center"],
    )  # type: ignore

    def reset(self):
        """Reset all statistic properties to their default values."""
        _reset_from(self, def_props.STATISTIC_PROPS_DEFAULT)


class GlobalConfig(PropertyGroup):
    """Top-level container holding the compiler, option, and statistic sub-configurations."""

    g_compiler: PointerProperty(name="Compiler", type=CompilerItem, description=Description.CompilerDesc["Element"])  # type: ignore
    g_option: PointerProperty(name="Option", type=OptionItem, description=Description.OptionDesc["Element"])  # type: ignore
    g_statistic: PointerProperty(name="Statistic", type=StatisticItem, description=Description.StatisticDesc["Element"])  # type: ignore

    def reset(self):
        """Reset all child configurations to their default values."""
        self.g_compiler.reset()
        self.g_option.reset()
        self.g_statistic.reset()


class VisualConfig(PropertyGroup):
    """Top-level container holding the global, headlight, map, RGBA, SSGI, and tonemapping visual sub-configurations."""

    v_global: PointerProperty(name="Global", type=GlobalItem, description=Description.VisualDesc["Element"])  # type: ignore
    v_headlight: PointerProperty(name="Headlight", type=HeadlightItem, description=Description.VisualDesc["Element"])  # type: ignore
    v_map: PointerProperty(name="Map", type=MapItem, description=Description.VisualDesc["Element"])  # type: ignore
    v_rgba: PointerProperty(name="Rgba", type=RgbaItem, description=Description.VisualDesc["Element"])  # type: ignore
    v_quality: PointerProperty(name="Quality", type=QualityItem, description=Description.QualityDesc["Element"])  # type: ignore
    v_tonemapping: PointerProperty(
        name="Tonemapping", type=TonemappingItem, description=Description.TonemappingDesc["Element"]
    )  # type: ignore
    v_ssgi: PointerProperty(name="Ssgi", type=SsgiItem, description=Description.SsgiDesc["Element"])  # type: ignore

    def reset(self):
        """Reset all visual sub-configurations to their default values."""
        self.v_global.reset()
        self.v_headlight.reset()
        self.v_map.reset()
        self.v_rgba.reset()
        self.v_quality.reset()
        self.v_tonemapping.reset()
        self.v_ssgi.reset()


class Temp_Props(PropertyGroup):
    """Temporary properties used during model import and attach workflows."""

    def update_file(self, context: Context):
        """Update temporary model name, link, prefix when the file path changes."""
        filepath, _ = os.path.splitext(self.tmp_file)
        model = os.path.basename(filepath)
        self.tmp_model = model
        self.tmp_link = "None"
        self.tmp_prefix = model + "_"
        self.tmp_links_class.clear()

    @property
    def tmp_links_class(self) -> dict:
        """Return temporary link metadata isolated to this owning scene."""
        owner = self.id_data
        key = owner.as_pointer() if owner is not None else id(self)
        return _temp_links_by_owner.setdefault(key, {})

    tmp_include: StringProperty(
        name="Temp File",
        default="*.xml",
        description="Path to a *.xml file",
        subtype="NONE",
    )  # type: ignore

    tmp_file: StringProperty(
        name="Temp File",
        default="*.xml",
        description="Path to a *.xml file",
        subtype="NONE",
        update=update_file,
    )  # type: ignore

    tmp_model: StringProperty(
        name="Temp Model",
        default="",
        description="Model from tmp file",
    )  # type: ignore

    tmp_link: StringProperty(
        name="Temp Link",
        default="None",
        description="Link from tmp file",
    )  # type: ignore

    tmp_prefix: StringProperty(
        name="Temp Prefix",
        default="ATT_",
        description="Prefix for avoid name collider",
    )  # type: ignore

    def reset(self):
        """Reset all temporary properties to their default values."""
        self.tmp_include = "*.xml"
        self.tmp_file = "*.xml"
        self.tmp_link = "None"
        self.tmp_links_class.clear()
        self.tmp_model = ""
        self.tmp_prefix = "ATT_"


class Forge_Props(PropertyGroup):
    """Main Forge property group attached to the scene, containing import / export settings and object references."""

    def Path(self):
        """Get the directory path of the Forge add-on."""
        return os.path.dirname(__file__)

    def ResLib(self):
        """Get the file path to the built-in shape library blend file."""
        return os.path.join(os.path.dirname(self.Path()), "lib", "assets", "Shapes.blend")

    scale_factors = (
        ("0.25", "0.25", ""),
        ("0.5", "0.5", ""),
        ("1.0", "1.0", ""),
        ("1.5", "1.5", ""),
        ("2.0", "2.0", ""),
        ("4.0", "4.0", ""),
    )

    def set_gizmo_scale(self, context: Context):
        """Update the gizmo display scale when the scale factor enum changes."""
        self.gizmo_scale = float(self.scale_factor)

    root_scene: PointerProperty(type=Scene)  # type: ignore

    cancel_requested: BoolProperty(
        name="Cancel Requested",
        default=False,
        options={"HIDDEN", "SKIP_SAVE"},
        description="Internal cancellation signal for modal Forge operations",
    )  # type: ignore

    modal_operation_active: BoolProperty(
        name="Modal Operation Active",
        default=False,
        options={"HIDDEN", "SKIP_SAVE"},
        description="Whether a long-running Forge modal operation currently owns the scene",
    )  # type: ignore
    modal_operation_name: StringProperty(
        name="Modal Operation Name",
        default="",
        options={"HIDDEN", "SKIP_SAVE"},
        description="Identifier of the current or most recent Forge modal operation",
    )  # type: ignore
    modal_operation_token: StringProperty(
        name="Modal Operation Token",
        default="",
        options={"HIDDEN", "SKIP_SAVE"},
        description="Internal ownership token for the active Forge modal operation",
    )  # type: ignore
    modal_operation_deferred: BoolProperty(
        name="Modal Operation Deferred",
        default=False,
        options={"HIDDEN", "SKIP_SAVE"},
        description="Keep the operation slot until its deferred MCP response is collected",
    )  # type: ignore
    modal_operation_status: StringProperty(
        name="Modal Operation Status",
        default="IDLE",
        options={"HIDDEN", "SKIP_SAVE"},
        description="Final status of the current or most recent Forge modal operation",
    )  # type: ignore
    modal_operation_message: StringProperty(
        name="Modal Operation Message",
        default="",
        options={"HIDDEN", "SKIP_SAVE"},
        description="Error or cancellation message from the most recent Forge modal operation",
    )  # type: ignore

    scale_factor: EnumProperty(
        name="Scale Factor",
        items=scale_factors,
        default="0.25",
        update=set_gizmo_scale,
        description="World scale factor for the exported model",
    )  # type: ignore
    gizmo_scale: FloatProperty(
        name="Scale",
        default=0.25,
        min=0.01,
        max=10,
        precision=3,
        subtype="FACTOR",
        description="Gizmo display scale in the viewport",
    )  # type: ignore

    rel_path: BoolProperty(
        name="Rel path", default=False, description="Use relative file paths when exporting XML references"
    )  # type: ignore

    select_tag: StringProperty(
        name="Select tag",
        default="",
        description="Some tag in object name eg. collider or convex...",
    )  # type: ignore

    select_model_type: EnumProperty(
        name="Model Type",
        items=cons.Model_Types,
        default=cons.ModelTypes.LINK,
        description="Forge model type to select",
    )  # type: ignore

    import_file_path: StringProperty(
        name="Import File Path",
        default="*.xml",
        description="Path to a *.xml file",
        subtype="NONE",
    )  # type: ignore

    export_path: StringProperty(
        name="Export Path",
        default="*.xml",
        description="Define the export path of the mjcf file",
        subtype="NONE",
    )  # type: ignore

    is_importing: BoolProperty(
        name="Is Importing",
        default=False,
        description="Flag indicating an import operation is currently in progress",
    )  # type: ignore

    is_exporting: BoolProperty(
        name="Is Exporting",
        default=False,
        description="Flag indicating an export operation is currently in progress",
    )  # type: ignore

    is_attaching: BoolProperty(
        name="Is Attaching",
        default=False,
        description="Flag indicating an attach operation is currently in progress",
    )  # type: ignore

    is_including: BoolProperty(
        name="Is Including",
        default=False,
        description="Flag indicating an include operation is currently in progress",
    )  # type: ignore

    progress: FloatProperty(default=0.0, subtype="PERCENTAGE")  # type: ignore
    progress_info: StringProperty(
        default="Initialling...",
    )  # type: ignore

    sub_progress: FloatProperty(default=0.0, subtype="PERCENTAGE")  # type: ignore
    sub_progress_info: StringProperty(
        default="Initialling...",
    )  # type: ignore

    import_material: BoolProperty(
        name="Import material", default=True, description="Import materials along with the model geometry"
    )  # type: ignore
    update_forge_only: BoolProperty(
        name="Update mjcf only", default=False, description="Only update mjcf properties without a full re-export"
    )  # type: ignore
    instance_body: PointerProperty(
        name="Instance Body",
        type=Object,
        poll=select.instance_link_only_poll,
        description=(
            "Link marked as an instance link (forge.mark_instance_link): exports only asset data, and its children are"
            " written under every INSTANCE_IDNAME link"
        ),
    )  # type: ignore
    world_collection: PointerProperty(
        name="World to export",
        type=Collection,
        description="Blender collection containing the world to export",
    )  # type: ignore

    use_glb: BoolProperty(name="Export GLB", default=False, description="Export a GLB file alongside the XML output")  # type: ignore


def register_forge_model_props():
    """Register all Forge model property groups onto Blender Scene and Object types."""

    bpy.types.Scene.Main_Scene = StringProperty(default="Scene")
    bpy.types.Scene.Forge_Props = PointerProperty(
        type=Forge_Props, description="Main Forge scene properties for import/export and configuration"
    )
    bpy.types.Scene.Forge_GlobalConfig = PointerProperty(
        name="Global Config", type=GlobalConfig, description="Global configuration (compiler, options, statistics)"
    )  # type: ignore
    bpy.types.Scene.Forge_VisualConfig = PointerProperty(
        name="Visual Config", type=VisualConfig, description="Visual configuration (global, headlight, map, rgba)"
    )  # type: ignore
    bpy.types.Scene.Forge_Temp_Props = PointerProperty(
        type=Temp_Props, description="Temporary properties used during import/attach workflows"
    )
    bpy.types.Object.Forge_Model_Type = EnumProperty(
        name="Model Type", items=cons.Model_Types, default="UNDEFINED", description="Forge Model Types"
    )
    bpy.types.Object.Forge_Link = PointerProperty(
        name="Link", type=LinkItem, description=Description.BodyDesc["Element"]
    )  # type: ignore
    bpy.types.Object.Forge_Geometry = PointerProperty(
        name="Geometry", type=GeomItem, description=Description.GeomDesc["Element"]
    )  # type: ignore
    bpy.types.Object.Forge_Joint = PointerProperty(
        name="Joint", type=JointItem, description=Description.JointDesc["Element"]
    )  # type: ignore
    bpy.types.Object.Forge_Equality = PointerProperty(
        name="Equality", type=EqualityItem, description=Description.EqualityDesc["Element"]
    )  # type: ignore
    bpy.types.Object.Forge_Tendon = PointerProperty(
        name="Tendon", type=TendonItem, description=Description.TendonDesc["Element"]
    )  # type: ignore
    bpy.types.Object.Forge_Actuator = PointerProperty(
        name="Actuator", type=ActuatorItem, description=Description.ActuatorDesc["Element"]
    )  # type: ignore
    bpy.types.Object.Forge_Contact = PointerProperty(
        name="Contact", type=ContactItem, description=Description.ContactDesc["Element"]
    )  # type: ignore
    bpy.types.Object.Forge_Sensor = PointerProperty(
        name="Sensor", type=SensorItem, description=Description.SensorDesc["Element"]
    )  # type: ignore
    bpy.types.Object.Forge_Inertial = PointerProperty(
        name="Inertial", type=InertialItem, description=Description.InertialDesc["Element"]
    )  # type: ignore
    bpy.types.Object.Forge_Light = PointerProperty(
        name="Light", type=LightItem, description=Description.LightDesc["Element"]
    )  # type: ignore
    bpy.types.Object.Forge_Camera = PointerProperty(
        name="Camera", type=CameraItem, description=Description.CameraDesc["Element"]
    )  # type: ignore
    bpy.types.Object.Forge_Attach = PointerProperty(
        name="Attach", type=AttachItem, description=Description.AttachDesc["Element"]
    )  # type: ignore
    bpy.types.Object.Forge_Replicate = PointerProperty(
        name="Replicate", type=ReplicateItem, description=Description.ReplicateDesc["Element"]
    )  # type: ignore
    bpy.types.Object.Forge_Include = PointerProperty(
        name="Include", type=IncludeItem, description=Description.IncludeDesc["Element"]
    )  # type: ignore


def unregister_forge_model_props():
    """Unregister all Forge model property groups from Blender Scene and Object types."""
    del bpy.types.Object.Forge_Include
    del bpy.types.Object.Forge_Replicate
    del bpy.types.Object.Forge_Attach
    del bpy.types.Object.Forge_Camera
    del bpy.types.Object.Forge_Light
    del bpy.types.Object.Forge_Inertial
    del bpy.types.Object.Forge_Sensor
    del bpy.types.Object.Forge_Contact
    del bpy.types.Object.Forge_Actuator
    del bpy.types.Object.Forge_Tendon
    del bpy.types.Object.Forge_Equality
    del bpy.types.Object.Forge_Joint
    del bpy.types.Object.Forge_Geometry
    del bpy.types.Object.Forge_Link
    del bpy.types.Object.Forge_Model_Type
    del bpy.types.Scene.Forge_Temp_Props
    del bpy.types.Scene.Forge_VisualConfig
    del bpy.types.Scene.Forge_GlobalConfig
    del bpy.types.Scene.Forge_Props
    del bpy.types.Scene.Main_Scene


classes = (
    LinkItem,
    LightItem,
    CameraItem,
    JointItem,
    InertialItem,
    ContactItem,
    SensorItem,
    EqualityItem,
    TendonTargetItem,
    TendonTargetList,
    FORGE_UL_TendonTargetList,
    Forge_OT_TendonTargetItemAdd,
    Forge_OT_TendonTargetItemRemove,
    TendonItem,
    ActuatorItem,
    GeomItem,
    AttachItem,
    ReplicateItem,
    IncludeItem,
    CompilerItem,
    GlobalItem,
    HeadlightItem,
    MapItem,
    RgbaItem,
    QualityItem,
    TonemappingItem,
    SsgiItem,
    FlagItem,
    OptionItem,
    StatisticItem,
    GlobalConfig,
    VisualConfig,
    Temp_Props,
    Forge_Props,
)
