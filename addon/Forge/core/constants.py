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
Pure constants, enums, and type-agnostic helpers for the Forge addon.

This module holds:

* Enum classes (StrEnum) for every entity type, shape, mode, etc.
* ``_enum_items()`` — helper to turn a ``StrEnum`` into Blender
  ``EnumProperty`` ``items`` tuples.
* Module-level constants derived from those enums (``Model_Types``,
  ``Joint_Types``, …).
* Miscellaneous constant dicts, lists, and tuples
  (``GeometryShapeModifiers``, ``Active_Types``, …).
* ``ModifierSockets`` — named socket aliases for Geometry Nodes modifiers.
* MJCF section lists.
"""

from __future__ import annotations

from collections.abc import Callable
from enum import StrEnum

# ═══════════════════════════════════════════════════════════════════════
# Helper — StrEnum → Blender EnumProperty items
# ═══════════════════════════════════════════════════════════════════════


def _enum_items(
    enum_cls: type[StrEnum],
    name_fn: Callable[[StrEnum], str] | None = None,
) -> tuple[tuple[str, str, str], ...]:
    """Generate Blender ``EnumProperty`` items from a :class:`StrEnum`.

    Item order follows the enum definition order, so callers that use
    numeric slices (e.g. ``Model_Types[3:5]``) continue to work as long
    as the enum members are declared in the same sequence.

    Args:
        enum_cls: A StrEnum subclass whose members define the enum items.
        name_fn: Optional callable that receives an enum member and returns
            the display name string.  Defaults to ``v.value.capitalize()``.

    Returns:
        A tuple of ``(identifier, name, description)`` triples suitable
        for use as a Blender ``EnumProperty`` ``items`` argument.
    """

    if name_fn is None:

        def name_fn(v):
            """Format an enum member's value as a capitalized display name.

            Args:
                v: An enum member from the StrEnum.

            Returns:
                The capitalized string of the member's value.
            """
            return v.value.capitalize()

    return tuple((v.value, name_fn(v), "") for v in enum_cls)


# ═══════════════════════════════════════════════════════════════════════
# Numeric / sentinel constants
# ═══════════════════════════════════════════════════════════════════════


class GeometryGroup:
    """Numeric group values for ``obj.Forge_Geometry.group``."""

    VISUAL = 2
    COLLIDER = 3


class LockAxis:
    """Convenience constants for lock_scale / lock_location / lock_rotation.

    Usage::

        obj.lock_scale = LockAxis.LOCKED
        obj.lock_scale = LockAxis.UNLOCKED
    """

    LOCKED = [True, True, True]
    UNLOCKED = [False, False, False]


# ═══════════════════════════════════════════════════════════════════════
# Enums — file path sections
# ═══════════════════════════════════════════════════════════════════════


class GSubPaths(StrEnum):
    """Subdirectory name constants for export asset/mesh/texture paths."""

    ASSET = "ASSET"
    MESH = "MESH"
    TEXTURE = "TEXTURE"


# ═══════════════════════════════════════════════════════════════════════
# Enums — MJCF model element types
# ═══════════════════════════════════════════════════════════════════════


class ObjectTypes(StrEnum):
    """Blender object type strings used in type defines."""

    MESH = "MESH"
    EMPTY = "EMPTY"
    LIGHT = "LIGHT"
    CAMERA = "CAMERA"


class ModelTypes(StrEnum):
    """Mad model type classification for MJCF element kinds.

    Maps to the ``Forge_Model_Type`` enum property on Blender objects.
    """

    UNDEFINED = "UNDEFINED"
    LINK = "LINK"
    INERTIAL = "INERTIAL"
    VISUAL = "VISUAL"
    COLLIDER = "COLLIDER"
    HFIELD = "HFIELD"
    PLANE = "PLANE"
    JOINT = "JOINT"
    SITE = "SITE"
    ACTUATOR = "ACTUATOR"
    TENDON = "TENDON"
    EQUALITY = "EQUALITY"
    CONTACT = "CONTACT"
    SENSOR = "SENSOR"
    LIGHT = "LIGHT"
    CAMERA = "CAMERA"
    FRAME = "FRAME"
    REPLICATE = "REPLICATE"
    ATTACH = "ATTACH"
    INCLUDE = "INCLUDE"


class CollectionNames(StrEnum):
    """Standard collection names used to organise MJCF elements in the scene."""

    MESH_ASSETS = "Mesh_Assets"
    WORLD = "World"
    LINK = "Link"
    INERTIAL = "Inertial"
    VISUAL = "Visual"
    COLLIDER = "Collider"
    JOINT = "Joint"
    SITE = "Site"
    ACTUATOR = "Actuator"
    TENDON = "Tendon"
    EQUALITY = "Equality"
    CONTACT = "Contact"
    SENSOR = "Sensor"
    LIGHT = "Light"
    CAMERA = "Camera"
    FRAME = "Frame"
    REPLICATE = "Replicate"
    ATTACH = "Attach"
    INCLUDE = "Include"


# Model type → collection holding objects of that type. Objects without a parent
# live in CollectionNames.WORLD whatever their type, so the root-only types
# (UNDEFINED, HFIELD, PLANE) have no entry here; every other type has one.
Model_Collection_Names = {
    ModelTypes.LINK: CollectionNames.LINK,
    ModelTypes.INERTIAL: CollectionNames.INERTIAL,
    ModelTypes.VISUAL: CollectionNames.VISUAL,
    ModelTypes.COLLIDER: CollectionNames.COLLIDER,
    ModelTypes.JOINT: CollectionNames.JOINT,
    ModelTypes.SITE: CollectionNames.SITE,
    ModelTypes.ACTUATOR: CollectionNames.ACTUATOR,
    ModelTypes.TENDON: CollectionNames.TENDON,
    ModelTypes.EQUALITY: CollectionNames.EQUALITY,
    ModelTypes.CONTACT: CollectionNames.CONTACT,
    ModelTypes.SENSOR: CollectionNames.SENSOR,
    ModelTypes.LIGHT: CollectionNames.LIGHT,
    ModelTypes.CAMERA: CollectionNames.CAMERA,
    ModelTypes.FRAME: CollectionNames.FRAME,
    ModelTypes.REPLICATE: CollectionNames.REPLICATE,
    ModelTypes.ATTACH: CollectionNames.ATTACH,
    ModelTypes.INCLUDE: CollectionNames.INCLUDE,
}


# ═══════════════════════════════════════════════════════════════════════
# Enums — geometry shapes
# ═══════════════════════════════════════════════════════════════════════


class GeometryTypes(StrEnum):
    """Supported primitive geometry shapes for Visual / Collider / Site elements."""

    BOX = "BOX"
    CAPSULE = "CAPSULE"
    CYLINDER = "CYLINDER"
    SPHERE = "SPHERE"
    MESH = "MESH"
    SDF = "SDF"


class JointTypes(StrEnum):
    """MJCF joint degrees-of-freedom types."""

    FREE = "FREE"
    BALL = "BALL"
    SLIDE = "SLIDE"
    HINGE = "HINGE"


class ActuatorTypes(StrEnum):
    """Actuator control models supported by MJCF."""

    GENERAL = "GENERAL"
    MOTOR = "MOTOR"
    POSITION = "POSITION"
    VELOCITY = "VELOCITY"
    ADHESION = "ADHESION"


class TendonTypes(StrEnum):
    """Tendon types (spatial/fixed) supported by MJCF."""

    FIXED = "FIXED"


class ActuatorTargetTypes(StrEnum):
    """Valid target model types that an actuator can control."""

    JOINT = "JOINT"
    TENDON = "TENDON"
    LINK = "LINK"
    SITE = "SITE"


class EqualityTypes(StrEnum):
    """Equality constraint type identifiers (connect, weld, joint)."""

    CONNECT = "CONNECT"
    WELD = "WELD"
    JOINT = "JOINT"


class EqualityTargetTypes(StrEnum):
    """Valid target model types for equality constraints."""

    LINK = "LINK"
    SITE = "SITE"
    JOINT = "JOINT"


class CreateColliderMethod(StrEnum):
    """Strategies for creating collider geometry from visual shapes."""

    GEOMETRY_TYPE = "GEOMETRY_TYPE"
    COLLIDER_TYPE = "COLLIDER_TYPE"


class SensorTypes(StrEnum):
    """MJCF sensor measurement types.

    .. important::

       The definition order here determines the index used by
       ``Sensor_Target_Type_Range`` slicing.  Keep it in sync with the
       range values in that dict.
    """

    Jointpos = "Jointpos"
    Jointvel = "Jointvel"
    Touch = "Touch"
    Accelerometer = "Accelerometer"
    Velocimeter = "Velocimeter"
    Gyro = "Gyro"
    Framepos = "Framepos"
    Framequat = "Framequat"
    Framexaxis = "Framexaxis"
    Frameyaxis = "Frameyaxis"
    Framezaxis = "Framezaxis"
    Framelinvel = "Framelinvel"
    Frameangvel = "Frameangvel"
    Contact = "Contact"
    Subtreecom = "Subtreecom"
    Subtreelinvel = "Subtreelinvel"
    Subtreeangmom = "Subtreeangmom"


class SensorTargetTypes(StrEnum):
    """Valid target model types for sensor attachments."""

    BODY = "BODY"
    XBODY = "XBODY"
    GEOM = "GEOM"
    SITE = "SITE"
    CAMERA = "CAMERA"
    JOINT = "JOINT"
    SUBTREE = "SUBTREE"


# ═══════════════════════════════════════════════════════════════════════
# Enums — light & camera
# ═══════════════════════════════════════════════════════════════════════
LC_Modes = ["FIXED", "TRACK", "TRACKCOM", "TARGETBODY", "TARGETBODYCOM"]


class LightTypes(StrEnum):
    """Light source types supported by MJCF."""

    DIRECTIONAL = "DIRECTIONAL"
    SPOT = "SPOT"
    POINT = "POINT"


class TargetModes(StrEnum):
    """Tracking/follow modes for light sources.

    … keep UI-compatible order (TARGETBODY, TARGETBODYCOM, FIXED, TRACK, TRACKCOM)
    so that ``Target_Modes[2:5]`` continues to yield ``(FIXED, TRACK, TRACKCOM)``.
    """

    TARGETBODY = "TARGETBODY"
    TARGETBODYCOM = "TARGETBODYCOM"
    FIXED = "FIXED"
    TRACK = "TRACK"
    TRACKCOM = "TRACKCOM"


class CameraTypes(StrEnum):
    """Camera projection types."""

    PERSPECTIVE = "PERSPECTIVE"
    ORTHOGRAPHIC = "ORTHOGRAPHIC"


class ContactTypes(StrEnum):
    """Contact exclusion / pair types."""

    EXCLUDE = "EXCLUDE"
    PAIR = "PAIR"


class TonemappingMethods(StrEnum):
    """Tonemapping methods for visual post-processing."""

    NONE = "none"
    ACES = "aces"


class VisualConfigTypes(StrEnum):
    """Visual-config subgroup keys."""

    Global = "Global"
    Headlight = "Headlight"
    Map = "Map"
    Rgba = "Rgba"
    Quality = "Quality"
    Ssgi = "Ssgi"
    Tonemapping = "Tonemapping"


# ═══════════════════════════════════════════════════════════════════════
# Enums — shader / node-graph names
# ═══════════════════════════════════════════════════════════════════════


class ShaderPropName(StrEnum):
    """Shader property node names used in the material node graph."""

    PRINCIPLED = "Principled BSDF"
    COLORTEX = "Base Color Tex"
    ALPHATEX = "Base Alpha Tex"
    NORMALTEX = "Base Normal Tex"
    ROUGHNESSTEX = "Base Roughness Tex"
    METALLICTEX = "Base Metallic Tex"
    EMISSIONTEX = "Base Emission Tex"
    TILING = "Tiling"
    CHECKER = "Checker"
    BACKGROUND = "BACKGROUND"
    ENV = "ENV"


class NodeInputName(StrEnum):
    """Named input socket identifiers for shader node graphs."""

    COLOR = "Base Color"
    EMISSION = "Emission Color"
    EMISSIONST = "Emission Strength"
    ROUGHNESS = "Roughness"
    METALLIC = "Metallic"
    NORMAL = "Normal"
    NCOLOR = "Color"
    SCALE = "Scale"
    ALPHA = "Alpha"
    VECTOR = "Vector"
    FACTOR = "Factor"
    COLORA = "A"
    COLORB = "B"


class NodeOpTypeName(StrEnum):
    """Node operation type identifiers for shader node graph construction."""

    NORMALMAP = "NORMAL_MAP"
    COMBINEXYZ = "COMBXYZ"
    SEPARATEXYZ = "SEPXYZ"
    SEPARATERGB = "SEPARATE_COLOR"
    MAPPING = "MAPPING"
    VECTMATH = "VECT_MATH"
    SCALE = "SCALE"
    MULTIPLY = "MULTIPLY"
    MIX = "MIX"
    TEX_IMAGE = "TEX_IMAGE"
    TEX_CHECKER = "TEX_CHECKER"
    RGB = "RGB"
    MATH = "MATH"
    VALUE = "VALUE"


# ═══════════════════════════════════════════════════════════════════════
# Enums — MJCF/XML tag names
# ═══════════════════════════════════════════════════════════════════════


class ReferenceType(StrEnum):
    """MJCF file reference types (Root, Attach, Include)."""

    ROOT = "Root"
    ATTACH = "Attach"
    INCLUDE = "Include"


class MJCFTags(StrEnum):
    """MJCF/XML element tag name constants for all supported element types."""

    MESH = "mesh"
    MATERIAL = "material"
    BODY = "body"
    INERTIAL = "inertial"
    GEOM = "geom"
    HFIELD = "hfield"
    PLANE = "plane"
    JOINT = "joint"
    FJOINT = "freejoint"
    SITE = "site"
    TENDON = "tendon"
    EQUALITY = "equality"
    CONTACT = "contact"
    ACTUATOR = "actuator"
    SENSOR = "sensor"
    LIGHT = "light"
    CAMERA = "camera"
    FRAME = "frame"
    REPLICATE = "replicate"
    ATTACH = "attach"
    INCLUDE = "include"
    COMPILER = "compiler"
    OPTION = "option"
    STATISTIC = "statistic"
    VISUAL = "visual"
    DEFAULT = "default"
    ASSET = "asset"
    WORLDBODY = "worldbody"


# ═══════════════════════════════════════════════════════════════════════
# Generated Blender EnumProperty item tuples  (from StrEnums above)
# ═══════════════════════════════════════════════════════════════════════

Model_Types = _enum_items(ModelTypes)

Joint_Types = _enum_items(JointTypes)

Site_Types = tuple(item for item in _enum_items(GeometryTypes) if item[0] not in {"MESH", "SDF"})

Actuator_Types = _enum_items(ActuatorTypes)

Tendon_Types = _enum_items(TendonTypes)

Actuator_Target_Types = _enum_items(ActuatorTargetTypes)

Equality_Types = _enum_items(EqualityTypes)

Equality_Target_Types = _enum_items(EqualityTargetTypes)

_COLLIDER_METHOD_NAMES = {
    CreateColliderMethod.GEOMETRY_TYPE: "Geometry type based",
    CreateColliderMethod.COLLIDER_TYPE: "Collider type based",
}
Create_Collider_Method = _enum_items(
    CreateColliderMethod, name_fn=lambda v: _COLLIDER_METHOD_NAMES.get(v, v.value.capitalize())
)

Geometry_Types = _enum_items(GeometryTypes)
Collider_Types = Geometry_Types
MeshGeometryTypes = frozenset({GeometryTypes.MESH, GeometryTypes.SDF})

# ── Duplicated tuples (kept for backward compat; prefer enum + _enum_items) ──

Gain_Types = (
    ("FIXED", "Fixed", ""),
    ("AFFINE", "Affine", ""),
)

Bias_Types = (
    ("NONE", "None", ""),
    ("AFFINE", "Affine", ""),
)

Sensor_Types = _enum_items(SensorTypes)

Contact_Types = _enum_items(ContactTypes)

Sensor_Target_Types = _enum_items(SensorTargetTypes)

Light_Types = _enum_items(LightTypes)

Target_Modes = _enum_items(TargetModes)

Camera_Types = _enum_items(CameraTypes)

Tonemapping_Methods = _enum_items(TonemappingMethods)


# ═══════════════════════════════════════════════════════════════════════
# Non-enum constant tuples / dicts for UI filtering & setup
# ═══════════════════════════════════════════════════════════════════════

Active_Types = (
    ("FALSE", "False", ""),
    ("TRUE", "True", ""),
    ("AUTO", "Auto", ""),
)

Link_Child_Type_List = [
    "LINK",
    "VISUAL",
    "COLLIDER",
    "JOINT",
    "SITE",
    "LIGHT",
    "CAMERA",
    "FRAME",
    "REPLICATE",
    "ATTACH",
]

JointShapeModifiers = {
    "NAME": "Shape_Joint",
    "FREE": 0,
    "BALL": 1,
    "SLIDE": 2,
    "HINGE": 3,
}

GeometryShapeModifiers = {
    "BOX": "Geometry_Box",
    "CAPSULE": "Geometry_Capsule",
    "CYLINDER": "Geometry_Cylinder",
    "SPHERE": "Geometry_Sphere",
}

AdditionalShapeModifiers = {
    "HFIELD": "Geometry_Height_Field",
    "PLANE": "Geometry_Plane",
    "JOINT": "Shape_Joint",
    "CONTACT": "Shape_Contact",
    "EQUALITY": "Shape_Equality",
    "TENDON": "Shape_Tendon",
    "ACTUATOR": "Shape_Actuator",
    "SENSOR": "Shape_Sensor",
    "REPLICATE": "Replicate",
}

GeometryShapeModifiers_list = [
    "Geometry_Box",
    "Geometry_Capsule",
    "Geometry_Cylinder",
    "Geometry_Sphere",
]

ColliderShapeModifiers = {
    "BOX": "Collider_Box",
    "CAPSULE": "Collider_Capsule",
    "CYLINDER": "Collider_Cylinder",
    "SPHERE": "Collider_Sphere",
    "MESH": "Collider_Convex",
}

ColliderShapeModifiers_list = [
    "Collider_Box",
    "Collider_Capsule",
    "Collider_Cylinder",
    "Collider_Sphere",
]

SiteShapeModifiers = {
    "BOX": "Site_Box",
    "CAPSULE": "Site_Capsule",
    "CYLINDER": "Site_Cylinder",
    "SPHERE": "Site_Sphere",
}

Sensor_Target_Type_Range = {
    "BODY": [6, 17],
    "XBODY": [6, 13],
    "GEOM": [6, 14],
    "CAMERA": [6, 13],
    "SITE": [2, 14],
    "JOINT": [0, 2],
    "REF": [6, 14],
}


# ═══════════════════════════════════════════════════════════════════════
# ModifierSockets — named aliases for Geometry Nodes modifier socket keys
# ═══════════════════════════════════════════════════════════════════════


class ModifierSockets:
    """Named aliases for Geometry Nodes modifier socket keys.

    Different modifier groups use different socket indices for the same
    conceptual property (e.g. Visual uses Socket_0 for size, Collider
    uses Socket_3). These constants make the intent clear at the call site.
    """

    class Visual(StrEnum):
        """Socket keys for visual geometry modifiers."""

        SIZE = "Socket_0"  # Box: full size; Capsule/Cylinder: sphere radius
        HEIGHT = "Socket_2"  # Capsule/Cylinder: height
        MATERIAL = "Socket_4"  # Material reference
        MAT_BOX = "Socket_2"
        MAT_SPHERE = "Socket_3"
        MAT_CYLINDER = "Socket_4"

    class Collider(StrEnum):
        """Socket keys for collider geometry modifiers."""

        REF_OBJ = "Socket_0"  # Reference Object for auto
        SIZE = "Socket_3"  # Box: full size; Capsule/Cylinder: sphere radius
        HEIGHT = "Socket_4"  # Capsule/Cylinder: height
        USE_MESH_A = "Socket_4"
        USE_MESH_B = "Socket_5"
        USE_MESH_C = "Socket_2"

    class Site(StrEnum):
        """Socket keys for site geometry modifiers."""

        SIZE = "Socket_3"
        HEIGHT = "Socket_4"

    class Joint(StrEnum):
        """Socket keys for joint shape modifiers."""

        DISPLAY_SIZE = "Socket_0"
        JOINT_TYPE = "Socket_2"
        RANGE = "Socket_3"

    class HField(StrEnum):
        """Socket keys for height field geometry modifiers."""

        NROW = "Socket_0"
        NCOL = "Socket_2"
        USE_ELEVATION = "Socket_3"
        RADIUS_X = "Socket_4"
        RADIUS_Y = "Socket_5"
        ELEVATION_Z = "Socket_6"
        BASE_Z = "Socket_7"
        HEIGHT_MAP = "Socket_8"
        USE_HEIGHT_MAP = "Socket_10"
        OFFSET = "Socket_11"
        MATERIAL = "Socket_12"

    class Plane(StrEnum):
        """Socket keys for plane geometry modifiers."""

        HALF_SIZE_X = "Socket_2"
        HALF_SIZE_Y = "Socket_3"
        INFINITE = "Socket_4"
        MATERIAL = "Socket_5"

    class Replicate(StrEnum):
        """Socket keys for replicate modifiers."""

        COUNT = "Socket_0"
        OFFSET = "Socket_2"
        EULER = "Socket_3"
        COLLECTION = "Socket_4"

    class Convex(StrEnum):
        """Socket keys for convex hull collider modifiers."""

        TARGET = "Socket_0"
        TOMESH = "Socket_2"

    class Gizmo(StrEnum):
        """Socket keys for gizmo display modifiers."""

        DISPLAY_SIZE = "Socket_0"


# ═══════════════════════════════════════════════════════════════════════
# MJCF section lists
# ═══════════════════════════════════════════════════════════════════════

MJCF_SECTIONS = [
    "include",
    "compiler",
    "option",
    "statistic",
    "visual",
    "default",
    "asset",
    "worldbody",
    "contact",
    "equality",
    "tendon",
    "actuator",
    "sensor",
]

MJCF_ASSET_SUB_SECTIONS = [
    "texture",
    "material",
    "mesh",
    "hfield",
    "model",
]

MJCF_ACTUATOR_SUB_SECTIONS = [
    "general",
    "motor",
    "position",
    "velocity",
    "adhesion",
]

MJCF_BODY_SUB_SECTIONS = [
    "inertial",
    "body",
    "joint",
    "geom",
    "site",
    "light",
    "camera",
]

MJCF_DEFAULT_SUB_SECTIONS = [
    "mesh",
    "material",
    "joint",
    "geom",
    "site",
    "camera",
    "light",
    "pair",
    "equality",
    "tendon",
    "general",
    "motor",
    "position",
    "velocity",
    "adhesion",
]
