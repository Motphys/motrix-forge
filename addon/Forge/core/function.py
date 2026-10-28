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

import math
import os
from collections.abc import Callable
from pathlib import Path

import bpy
from bpy.types import Collection, Context, Object
from mathutils import Matrix, Quaternion, Vector

from . import constants as cons
from . import selection as sel
from . import serialization as serialize
from .common import ensure_shader_nodes, get_modifier_socket, link_collection, set_modifier_socket
from .dependency import require_gltf_addon
from .geometry_handler import GeometryHandler, add_shape_modifier
from .props import (
    ActuatorItem,
    AttachItem,
    CameraItem,
    CompilerItem,
    ContactItem,
    EqualityItem,
    Forge_Props,
    IncludeItem,
    InertialItem,
    JointItem,
    LightItem,
    ReplicateItem,
    SensorItem,
    TendonItem,
    TendonTargetItem,
)
from .utils import (
    AttachData,
    WmReportItems,
    bmesh_copy_from_object,
    create_empty_mesh_object,
    find_shape_modifier,
    get_bound_center,
    get_collection,
    get_height_axis_index,
    get_matrix_by_dimension_axis_local,
    get_max_dimension_axis,
    get_unique_object_name,
    name_string_replace,
    parent_under,
    update_modifiers,
    update_unique_name,
)

get_active = serialize.get_active
get_bool_str = serialize.get_bool_str
ZERO_TOLERANCE = serialize.ZERO_TOLERANCE
round_float = serialize.round_float
parse_vector_array_to_xml = serialize.parse_vector_array_to_xml
parse_list_array_to_xml = serialize.parse_list_array_to_xml
parse_rotation_euler_to_xml = serialize.parse_rotation_euler_to_xml
parse_value_by_attr = serialize.parse_value_by_attr
parse_prop_by_type = serialize.parse_prop_by_type
fix_object_name = serialize.fix_object_name
fix_image_name = serialize.fix_image_name
parse_float_list = serialize.parse_float_list


def scale_gizmo(context: Context, obj: Object):
    """Scale the display gizmo of *obj* based on the global gizmo_scale setting.

    Args:
        context: The Blender context.
        obj: The object whose gizmo should be scaled.
    """
    forge_props: Forge_Props = context.scene.Forge_Props

    match obj.Forge_Model_Type:
        case (
            cons.ModelTypes.JOINT
            | cons.ModelTypes.CONTACT
            | cons.ModelTypes.EQUALITY
            | cons.ModelTypes.TENDON
            | cons.ModelTypes.ACTUATOR
            | cons.ModelTypes.SENSOR
        ):
            modifier_name = cons.AdditionalShapeModifiers[obj.Forge_Model_Type]
            if modifier_name in obj.modifiers:
                base_key = "_forge_gizmo_base_size"
                if base_key not in obj:
                    obj[base_key] = get_modifier_socket(obj.modifiers[modifier_name], "Socket_0")
                set_modifier_socket(
                    obj.modifiers[modifier_name],
                    "Socket_0",
                    obj[base_key] * forge_props.gizmo_scale,
                )
                obj.modifiers[modifier_name].node_group.interface_update(context)
        case cons.ModelTypes.LINK | cons.ModelTypes.FRAME | cons.ModelTypes.ATTACH:
            base_key = "_forge_gizmo_base_size"
            if base_key not in obj:
                obj[base_key] = obj.empty_display_size
            obj.empty_display_size = obj[base_key] * forge_props.gizmo_scale


def get_size(obj: Object):
    """Get the size of a geometry modifier on an object.

    Retrieves the size parameter from the appropriate shape modifier based
    on the object's model type (VISUAL, COLLIDER, SITE, PLANE).

    Args:
        obj: The Blender object to query.

    Returns:
        A Vector representing the size, or None if no size modifier is found.
    """

    geo_type = obj.Forge_Geometry.type

    if (
        obj.Forge_Model_Type in (cons.ModelTypes.VISUAL, cons.ModelTypes.COLLIDER)
        and geo_type not in cons.MeshGeometryTypes
    ):
        if obj.Forge_Model_Type == cons.ModelTypes.VISUAL:
            handler = GeometryHandler.for_visual(geo_type)
            mod_name = cons.GeometryShapeModifiers.get(geo_type)
        else:
            handler = GeometryHandler.for_collider(geo_type)
            mod_name = cons.ColliderShapeModifiers.get(geo_type)
        if mod_name and mod_name in obj.modifiers:
            return handler.get_size(obj.modifiers[mod_name])

    if obj.Forge_Model_Type == cons.ModelTypes.SITE:
        handler = GeometryHandler.for_site(geo_type)
        mod_name = cons.SiteShapeModifiers.get(geo_type)
        if mod_name and mod_name in obj.modifiers:
            return handler.get_size(obj.modifiers[mod_name])

    if obj.Forge_Model_Type == cons.ModelTypes.PLANE:
        modifier_name = cons.AdditionalShapeModifiers[obj.Forge_Model_Type]
        if modifier_name in obj.modifiers:
            x = get_modifier_socket(obj.modifiers[modifier_name], cons.ModifierSockets.Plane.HALF_SIZE_X)
            y = get_modifier_socket(obj.modifiers[modifier_name], cons.ModifierSockets.Plane.HALF_SIZE_Y)
            return Vector((x, y, 0.0))
        else:
            return obj.dimensions * Vector((0.5, 0.5, 1.0))


def get_gizmo_offset(obj: Object):
    """Get the gizmo display offset for an object based on its type.

    Returns an offset vector suitable for positioning the transform gizmo
    relative to the object. Handles VISUAL, COLLIDER, SITE, HFIELD, and
    PLANE model types with their respective geometry handlers.

    Args:
        obj: The Blender object.

    Returns:
        A list of 3 floats ``[x, y, z]`` representing the gizmo offset.
    """

    geo_type = obj.Forge_Geometry.type

    if obj.Forge_Model_Type == cons.ModelTypes.VISUAL:
        if geo_type in cons.MeshGeometryTypes:
            diff = get_bound_center(obj)
            offset = [v * 0.5 for v in obj.dimensions]
            return [offset[i] + diff[i] for i in range(3)]
        handler = GeometryHandler.for_visual(geo_type)
        mod_name = cons.GeometryShapeModifiers.get(geo_type)
        if mod_name and mod_name in obj.modifiers:
            return handler.get_gizmo_offset(obj.modifiers[mod_name])

    if obj.Forge_Model_Type == cons.ModelTypes.COLLIDER:
        if geo_type in cons.MeshGeometryTypes:
            diff = get_bound_center(obj)
            offset = [v * 0.5 for v in obj.dimensions]
            return [offset[i] + diff[i] for i in range(3)]
        handler = GeometryHandler.for_collider(geo_type)
        mod_name = cons.ColliderShapeModifiers.get(geo_type)
        if mod_name and mod_name in obj.modifiers:
            return handler.get_gizmo_offset(obj.modifiers[mod_name])

    if obj.Forge_Model_Type == cons.ModelTypes.SITE:
        handler = GeometryHandler.for_site(geo_type)
        mod_name = cons.SiteShapeModifiers.get(geo_type)
        if mod_name and mod_name in obj.modifiers:
            return handler.get_gizmo_offset(obj.modifiers[mod_name])

    if obj.Forge_Model_Type == cons.ModelTypes.HFIELD:
        modifier_name = cons.AdditionalShapeModifiers[obj.Forge_Model_Type]
        if modifier_name in obj.modifiers:
            S = cons.ModifierSockets.HField
            x = get_modifier_socket(obj.modifiers[modifier_name], S.RADIUS_X)
            y = get_modifier_socket(obj.modifiers[modifier_name], S.RADIUS_Y)
            z = get_modifier_socket(obj.modifiers[modifier_name], S.ELEVATION_Z)
            return [x, y, z]
        else:
            return [v for v in obj.dimensions]

    if obj.Forge_Model_Type == cons.ModelTypes.PLANE:
        modifier_name = cons.AdditionalShapeModifiers[obj.Forge_Model_Type]
        if modifier_name in obj.modifiers:
            S = cons.ModifierSockets.Plane
            x = get_modifier_socket(obj.modifiers[modifier_name], S.HALF_SIZE_X)
            y = get_modifier_socket(obj.modifiers[modifier_name], S.HALF_SIZE_Y)
            return [x, y, 0.0]
        else:
            return [obj.dimensions.x * 0.5, obj.dimensions.y * 0.5, 0.0]


def get_matrix_by_dimension_axis_world(obj: Object, dims: Vector, min_is_height: bool = False):
    """Get a modified world matrix that reorients the Z axis to the height axis.

    Same logic as :func:`get_matrix_by_dimension_axis_local` but operates
    on the world matrix.

    Args:
        obj: The Blender object.
        dims: A Vector of dimensions (x, y, z).
        min_is_height: Align Z with the smallest dimension axis instead of the
            largest, matching ``GeometryHandler.set_size``.

    Returns:
        The adjusted world Matrix.
    """

    if dims.x == dims.y and dims.x == dims.z:
        return obj.matrix_world
    axis = ["X", "Y", "Z"][get_height_axis_index(dims, min_is_height)]

    if axis == "Z":
        return obj.matrix_world

    match axis:
        case "X":
            mat = obj.matrix_world.copy()
            tmp = mat.col[2].copy()
            mat.col[2] = mat.col[0].copy()
            mat.col[0] = -tmp
            return mat
        case "Y":
            mat = obj.matrix_world.copy()
            tmp = mat.col[2].copy()
            mat.col[2] = mat.col[1].copy()
            mat.col[1] = -tmp
            return mat


def set_geometry_size(
    obj: Object,
    geometry_type: cons.GeometryTypes,
    size: float | Vector,
    based_on_dimensions: bool = True,
    min_is_height: bool = False,
):
    """Set the size of a visual geometry modifier.

    Uses the appropriate :class:`GeometryHandler` to set the size on the
    shape modifier identified by *geometry_type*.

    Args:
        obj: The Blender object.
        geometry_type: The geometry type (e.g. BOX, SPHERE, CAPSULE).
        size: The size value or Vector to set.
        based_on_dimensions: If True, interpret *size* as a multiplier of object dimensions.
    """

    modifier_name = cons.GeometryShapeModifiers[geometry_type]
    if modifier_name not in obj.modifiers:
        return
    handler = GeometryHandler.for_visual(geometry_type)
    handler.set_size(obj.modifiers[modifier_name], size, based_on_dimensions, min_is_height)
    obj.modifiers[modifier_name].node_group.interface_update(bpy.context)


def set_geometry_shape(
    obj: Object,
    geometry_type: str,
    size: Vector | None = None,
    based_on_dimensions: bool = True,
):
    """Set the shape modifier for visual geometry and optionally set its size.

    Adds a shape modifier via :func:`add_shape_modifier`, then sets the
    size if provided.

    Args:
        obj: The Blender object.
        geometry_type: The geometry type string.
        size: Optional size to pass to :func:`set_geometry_size`.
        based_on_dimensions: Whether size is based on object dimensions.
    """

    add_shape_modifier(obj, "Visual", geometry_type)
    if size is not None:
        set_geometry_size(obj, geometry_type, size, based_on_dimensions)


def set_collider_size_by_ref(
    obj: Object,
    collider_type: cons.GeometryTypes,
    ref_obj: Object,
    based_on_dimensions: bool = False,
    min_is_height: bool = False,
):
    """Set collider size based on a reference object's visual geometry.

    For MESH colliders, directly sets the target. For primitive colliders
    (BOX, SPHERE, CAPSULE, CYLINDER), copies size parameters from the
    reference object's shape modifier or falls back to dimension-based sizing.

    Args:
        obj: The collider object to configure.
        collider_type: The collider geometry type.
        ref_obj: The reference visual object.
        based_on_dimensions: If True, use the reference object's dimensions instead of its modifier parameters.
    """

    CV = cons.ModifierSockets.Convex
    if collider_type == cons.GeometryTypes.SDF:
        return
    modifier_name = cons.ColliderShapeModifiers[collider_type]
    if collider_type == cons.GeometryTypes.MESH:
        set_modifier_socket(obj.modifiers[modifier_name], CV.TARGET, ref_obj)
        obj.modifiers[modifier_name].node_group.interface_update(bpy.context)
        return

    if modifier_name not in obj.modifiers:
        return

    VS = cons.ModifierSockets.Visual
    CS = cons.ModifierSockets.Collider
    set_modifier_socket(obj.modifiers[modifier_name], CS.REF_OBJ, None)
    ref_modifier = find_shape_modifier(ref_obj, cons.GeometryTypes(collider_type))
    if ref_modifier and not based_on_dimensions:
        match collider_type:
            case cons.GeometryTypes.BOX:
                set_modifier_socket(
                    obj.modifiers[modifier_name],
                    CS.SIZE,
                    get_modifier_socket(ref_modifier, VS.SIZE),
                )
            case cons.GeometryTypes.CAPSULE | cons.GeometryTypes.CYLINDER:
                set_modifier_socket(
                    obj.modifiers[modifier_name],
                    CS.SIZE,
                    get_modifier_socket(ref_modifier, VS.SIZE),
                )
                set_modifier_socket(
                    obj.modifiers[modifier_name],
                    CS.HEIGHT,
                    get_modifier_socket(ref_modifier, VS.HEIGHT),
                )
            case cons.GeometryTypes.SPHERE:
                set_modifier_socket(
                    obj.modifiers[modifier_name],
                    CS.SIZE,
                    get_modifier_socket(ref_modifier, VS.SIZE),
                )
    else:
        handler = GeometryHandler.for_collider(collider_type)
        update_modifiers(ref_obj)
        handler.set_size(obj.modifiers[modifier_name], ref_obj.dimensions, True, min_is_height)

    obj.modifiers[modifier_name].node_group.interface_update(bpy.context)


def set_collider_size(
    obj: Object,
    collider_type: cons.GeometryTypes,
    size: float | Vector,
    based_on_dimensions: bool = True,
    min_is_height: bool = False,
):
    """Set the size of a collider geometry modifier.

    Args:
        obj: The collider object.
        collider_type: The collider geometry type.
        size: The size value or Vector to set.
        based_on_dimensions: If True, interpret *size* as a multiplier of object dimensions.
    """

    if collider_type == cons.GeometryTypes.SDF:
        return
    modifier_name = cons.ColliderShapeModifiers[collider_type]
    if modifier_name not in obj.modifiers:
        return
    handler = GeometryHandler.for_collider(collider_type)
    handler.set_size(obj.modifiers[modifier_name], size, based_on_dimensions, min_is_height)
    obj.modifiers[modifier_name].node_group.interface_update(bpy.context)


def set_collider_shape(
    obj: Object,
    collider_type: cons.GeometryTypes,
    ref_obj: Object = None,
    based_on_dimensions: bool = False,
    size: float | Vector | None = None,
    min_is_height: bool = False,
):
    """Set the shape modifier for a collider and optionally configure its size.

    Adds a collider shape modifier, then sizes it from a reference object,
    explicit size, or default.

    Args:
        obj: The collider object.
        collider_type: The collider geometry type.
        ref_obj: Optional reference object to copy size from.
        based_on_dimensions: If True, size is based on dimensions.
        size: Optional explicit size value.
    """

    if collider_type == cons.GeometryTypes.SDF:
        if ref_obj is not None:
            if ref_obj.Forge_Geometry.type in cons.GeometryShapeModifiers:
                # Shape geometry lives in its modifiers; the shared base mesh
                # does not contain the generated surface or its configured size.
                bpy.context.view_layer.update()
                depsgraph = bpy.context.evaluated_depsgraph_get()
                obj.data = bpy.data.meshes.new_from_object(ref_obj.evaluated_get(depsgraph), depsgraph=depsgraph)
                obj.data.name = obj.name
            else:
                obj.data = ref_obj.data
        obj.display_type = "WIRE"
        obj.lock_scale = cons.LockAxis.UNLOCKED
        return
    add_shape_modifier(obj, "Collider", collider_type)
    obj.display_type = "WIRE"
    if ref_obj:
        set_collider_size_by_ref(obj, collider_type, ref_obj, based_on_dimensions, min_is_height)
    elif size is not None:
        set_collider_size(obj, collider_type, size, based_on_dimensions, min_is_height)


def set_site_size(
    obj: Object,
    site_type: cons.GeometryTypes,
    size: float | Vector = Vector((0.05, 0.05, 0.05)),
    based_on_dimensions: bool = True,
    min_is_height: bool = False,
):
    """Set the size of a site geometry modifier.

    Args:
        obj: The site object.
        site_type: The site type.
        size: The size value or Vector (default 0.05 for all axes).
        based_on_dimensions: If True, interpret *size* as a multiplier of object dimensions.
    """

    modifier_name = cons.SiteShapeModifiers[site_type]
    if modifier_name not in obj.modifiers:
        return
    handler = GeometryHandler.for_site(site_type)
    handler.set_size(obj.modifiers[modifier_name], size, based_on_dimensions, min_is_height)
    obj.modifiers[modifier_name].node_group.interface_update(bpy.context)


def set_site_shape(obj: Object, site_type: cons.GeometryTypes):
    """Set the shape modifier for a site.

    Args:
        obj: The site object.
        site_type: The site type to configure.
    """

    add_shape_modifier(obj, "Site", site_type)


def change_geometry(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    geometry_type: str,
    obj: Object,
):
    """Change the geometry type of a visual object, preserving size and materials.

    When switching to/from MESH type, applies modifiers or clears them
    as needed. Size is preserved across the transition where possible.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        geometry_type: The target geometry type.
        obj: The object to modify.
    """

    if obj.Forge_Geometry.type == geometry_type:
        return

    modifier_name = (
        cons.GeometryShapeModifiers[obj.Forge_Geometry.type]
        if obj.Forge_Geometry.type in cons.GeometryShapeModifiers
        else ""
    )
    if modifier_name not in obj.modifiers and obj.Forge_Geometry.type not in cons.MeshGeometryTypes:
        report({"WARNING"}, f"{obj.name} Missing shape modifier")
        return

    if geometry_type in cons.MeshGeometryTypes:
        if obj.Forge_Geometry.type not in cons.MeshGeometryTypes:
            data_materials = list(obj.data.materials)
            material_slots = [(slot.link, slot.material) for slot in obj.material_slots]
            active_material_index = obj.active_material_index
            obj.data = bpy.data.meshes.new("Mesh_Geometry")
            bpy.ops.object.modifier_apply(modifier=modifier_name)
            # Replacing the source mesh and baking Geometry Nodes can discard
            # both data slots and object-level overrides. Restore them after
            # baking without changing other objects sharing the source mesh.
            obj.data.materials.clear()
            for material in data_materials:
                obj.data.materials.append(material)
            for slot, (link, material) in zip(obj.material_slots, material_slots, strict=True):
                slot.link = link
                slot.material = material
            obj.active_material_index = active_material_index
        obj.Forge_Geometry.type = geometry_type
        obj.lock_scale = cons.LockAxis.UNLOCKED
        return

    size = None
    if obj.Forge_Geometry.type in cons.MeshGeometryTypes:
        for modifier in obj.modifiers:
            bpy.ops.object.modifier_apply(modifier=modifier.name)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        size = obj.dimensions.copy()
    else:
        old_type = obj.Forge_Geometry.type
        modifier_name = cons.GeometryShapeModifiers[old_type]
        handler = GeometryHandler.for_visual(old_type)
        if modifier_name in obj.modifiers:
            size = handler.get_dimensions(obj.modifiers[modifier_name])
        obj.modifiers.clear()
    obj.lock_scale = cons.LockAxis.LOCKED

    if geometry_type == cons.GeometryTypes.CAPSULE or geometry_type == cons.GeometryTypes.CYLINDER:
        obj.matrix_local = get_matrix_by_dimension_axis_local(obj, size)

    set_geometry_shape(obj, geometry_type, size)
    obj.Forge_Geometry.type = geometry_type


def add_geometry(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    geometry_type: str,
    parent_obj: Object | None = None,
    size: float | Vector | None = None,
    based_on_dimensions: bool = True,
) -> Object:
    """Create and add a new visual geometry object.

    Creates an empty mesh, configures it with the given geometry type,
    links it to the target collection, and optionally parents it under
    a link/replicate/frame object.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection to link the object into.
        geometry_type: The geometry type (BOX, SPHERE, CAPSULE, etc.).
        parent_obj: Optional parent object.
        size: Optional size value.
        based_on_dimensions: If True, size is based on object dimensions.

    Returns:
        The newly created geometry object.
    """

    obj = create_empty_mesh_object(context, "Geom")
    name_string_replace(obj, "Geom", geometry_type.capitalize())
    update_unique_name(obj, "GEO_")

    obj.Forge_Model_Type = cons.ModelTypes.VISUAL
    obj.Forge_Geometry.type = geometry_type
    obj.Forge_Geometry.group = cons.GeometryGroup.VISUAL
    obj.lock_scale = cons.LockAxis.LOCKED

    if len(obj.data.materials) == 0:
        obj.data.materials.append(None)

    obj.material_slots[0].link = "OBJECT"

    link_collection(obj, collection)
    set_geometry_shape(obj, geometry_type, size, based_on_dimensions)

    if parent_obj:
        if parent_obj.Forge_Model_Type in [
            cons.ModelTypes.LINK,
            cons.ModelTypes.REPLICATE,
            cons.ModelTypes.FRAME,
        ]:
            parent_under(obj, parent_obj)
        elif parent_obj.parent:
            if parent_obj.parent.Forge_Model_Type in [
                cons.ModelTypes.LINK,
                cons.ModelTypes.REPLICATE,
                cons.ModelTypes.FRAME,
            ]:
                parent_under(obj, parent_obj.parent, parent_obj.location)
        else:
            obj.location = parent_obj.location
    return obj


def add_height_field(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
) -> Object:
    """Create and add a new height field (HFIELD) object.

    Creates a height field object with the "Geometry_Height_Field" node
    group modifier from the Forge Library.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection to link the object into.

    Returns:
        The newly created height field object.
    """

    obj = create_empty_mesh_object(context, "Geom")
    update_unique_name(obj, "HFG_")
    obj.data = obj.data.copy()
    obj.data.name = obj.name
    obj.Forge_Model_Type = cons.ModelTypes.HFIELD
    obj.Forge_Geometry.group = cons.GeometryGroup.VISUAL
    obj.lock_scale = cons.LockAxis.LOCKED

    if len(obj.data.materials) == 0:
        obj.data.materials.append(None)

    obj.material_slots[0].link = "OBJECT"

    link_collection(obj, collection)

    bpy.ops.object.modifier_add_node_group(
        asset_library_type="CUSTOM",
        asset_library_identifier="Forge Library",
        relative_asset_identifier="Shapes.blend/NodeTree/Geometry_Height_Field",
    )
    return obj


def add_plane(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
) -> Object:
    """Create and add a new plane (PLANE) object.

    Creates a plane object with the "Geometry_Plane" node group modifier
    from the Forge Library.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection to link the object into.

    Returns:
        The newly created plane object.
    """

    obj = create_empty_mesh_object(context, "Geom")
    name_string_replace(obj, "Geom", "Plane")
    update_unique_name(obj, "FLG_")
    obj.Forge_Model_Type = cons.ModelTypes.PLANE
    obj.Forge_Geometry.group = cons.GeometryGroup.VISUAL
    obj.lock_scale = cons.LockAxis.LOCKED

    if len(obj.data.materials) == 0:
        obj.data.materials.append(None)

    obj.material_slots[0].link = "OBJECT"

    link_collection(obj, collection)

    bpy.ops.object.modifier_add_node_group(
        asset_library_type="CUSTOM",
        asset_library_identifier="Forge Library",
        relative_asset_identifier="Shapes.blend/NodeTree/Geometry_Plane",
    )
    return obj


def change_collider(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collider_type: str,
    obj: Object,
):
    """Change the collider geometry type on an object.

    Handles transitions between MESH and primitive collider types,
    preserving size where possible.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collider_type: The target collider type.
        obj: The object to modify.
    """

    obj.display_type = "WIRE"
    if obj.Forge_Geometry.type == collider_type:
        return

    modifier_name = (
        cons.ColliderShapeModifiers[obj.Forge_Geometry.type]
        if obj.Forge_Geometry.type in cons.ColliderShapeModifiers
        else ""
    )

    if modifier_name not in obj.modifiers and obj.Forge_Geometry.type not in cons.MeshGeometryTypes:
        report({"WARNING"}, f"{obj.name} Missing shape modifier")
        return

    for modifier in obj.modifiers:
        if modifier.type == "NODES" and modifier.node_group:
            modifier.node_group.interface_update(bpy.context)

    CS = cons.ModifierSockets.Collider
    if collider_type in cons.MeshGeometryTypes:
        if obj.Forge_Geometry.type not in cons.MeshGeometryTypes:
            obj.data = bpy.data.meshes.new("COL_" + obj.name if "COL_" not in obj.name else obj.name)
        match obj.Forge_Geometry.type:
            case cons.GeometryTypes.BOX:
                set_modifier_socket(obj.modifiers[modifier_name], CS.USE_MESH_A, True)
            case cons.GeometryTypes.CAPSULE | cons.GeometryTypes.CYLINDER:
                set_modifier_socket(obj.modifiers[modifier_name], CS.USE_MESH_B, True)
            case cons.GeometryTypes.SPHERE:
                set_modifier_socket(obj.modifiers[modifier_name], CS.USE_MESH_A, True)
        if modifier_name in obj.modifiers:
            if obj.Forge_Geometry.type == cons.GeometryTypes.MESH:
                set_modifier_socket(obj.modifiers[modifier_name], cons.ModifierSockets.Convex.TOMESH, True)
            bpy.ops.object.modifier_apply(modifier=modifier_name)
        obj.Forge_Geometry.type = collider_type
        obj.lock_scale = cons.LockAxis.UNLOCKED
        return

    size = None
    if obj.Forge_Geometry.type in cons.MeshGeometryTypes:
        size = obj.dimensions.copy()
        mesh = obj.data
        obj.data = bpy.data.meshes.new("Mesh_Collider")
        for modifier in obj.modifiers:
            bpy.ops.object.modifier_apply(modifier=modifier.name)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        temp_mesh = obj.data
        obj.data = mesh
        bpy.data.meshes.remove(temp_mesh)
    else:
        old_type = obj.Forge_Geometry.type
        handler = GeometryHandler.for_collider(old_type)
        if modifier_name in obj.modifiers:
            size = handler.get_dimensions(obj.modifiers[modifier_name])
        obj.modifiers.clear()
    obj.lock_scale = cons.LockAxis.LOCKED

    if collider_type == cons.GeometryTypes.CAPSULE or collider_type == cons.GeometryTypes.CYLINDER:
        obj.matrix_local = get_matrix_by_dimension_axis_local(obj, size)

    set_collider_shape(obj, collider_type)
    set_collider_size(obj, collider_type, size)
    obj.Forge_Geometry.type = collider_type


def add_collider(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    collider_type: str,
    parent_obj: Object | None = None,
    based_on_dimensions: bool = False,
    size: float | Vector | None = None,
    min_is_height: bool = False,
) -> Object:
    """Create and add a new collider object.

    Creates an empty mesh, configures it with the given collider type,
    links it to the target collection, and optionally sizes and parents it.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection.
        collider_type: The collider geometry type.
        parent_obj: Optional parent object.
        based_on_dimensions: If True, size is based on parent dimensions.
        size: Optional explicit size.
        min_is_height: If True, take the height from the parent's smallest
            dimension axis instead of its largest. CAPSULE / CYLINDER only, and
            honored only on the paths that measure a parent (see
            ``set_collider_size_by_ref``).

    Returns:
        The newly created collider object.
    """

    if collider_type == cons.GeometryTypes.SDF and parent_obj is not None:
        obj = bpy.data.objects.new("COL_" + parent_obj.name, parent_obj.data)
        context.collection.objects.link(obj)
        obj.select_set(True)
        context.view_layer.objects.active = obj
    elif collider_type in cons.MeshGeometryTypes and parent_obj is not None:
        obj = create_empty_mesh_object(context, "COL_" + parent_obj.name)
    else:
        obj = create_empty_mesh_object(context, "Collider")
    name_string_replace(obj, "Geom", collider_type.capitalize())
    update_unique_name(obj, "COL_")
    obj.Forge_Model_Type = cons.ModelTypes.COLLIDER
    obj.Forge_Geometry.type = collider_type
    obj.Forge_Geometry.group = cons.GeometryGroup.COLLIDER
    obj.lock_scale = cons.LockAxis.LOCKED

    link_collection(obj, collection)
    if size is not None:
        set_collider_shape(obj, collider_type, size=size, based_on_dimensions=based_on_dimensions)
    elif parent_obj and parent_obj.Forge_Model_Type in [
        cons.ModelTypes.LINK,
        cons.ModelTypes.REPLICATE,
        cons.ModelTypes.FRAME,
    ]:
        set_collider_shape(obj, collider_type)
    else:
        set_collider_shape(
            obj,
            collider_type,
            parent_obj,
            based_on_dimensions,
            min_is_height=min_is_height,
        )

    if collider_type == cons.GeometryTypes.SDF and parent_obj and parent_obj.Forge_Model_Type == cons.ModelTypes.VISUAL:
        obj.parent = parent_obj.parent
        obj.matrix_parent_inverse = parent_obj.matrix_parent_inverse.copy()
        obj.matrix_basis = parent_obj.matrix_basis.copy()
        return obj

    if parent_obj:
        if parent_obj.Forge_Model_Type in [
            cons.ModelTypes.LINK,
            cons.ModelTypes.REPLICATE,
            cons.ModelTypes.FRAME,
        ]:
            if collider_type not in cons.MeshGeometryTypes:
                update_modifiers(parent_obj)
                # A LINK/REPLICATE/FRAME parent is an Empty, whose dimensions are
                # all zero, so min_is_height is inert on this line; it is threaded
                # anyway so every alignment call reads the axis the same way.
                obj.matrix_world = get_matrix_by_dimension_axis_world(parent_obj, parent_obj.dimensions, min_is_height)
            parent_under(obj, parent_obj)

            if based_on_dimensions and (
                collider_type == cons.GeometryTypes.CAPSULE or collider_type == cons.GeometryTypes.CYLINDER
            ):
                update_modifiers(parent_obj)
                obj.rotation_euler = get_max_dimension_axis(parent_obj, parent_obj.dimensions, min_is_height)
        elif parent_obj.parent:
            if parent_obj.parent.Forge_Model_Type in [
                cons.ModelTypes.LINK,
                cons.ModelTypes.REPLICATE,
                cons.ModelTypes.FRAME,
            ]:
                obj.parent = parent_obj.parent
                obj.matrix_local = obj.matrix_parent_inverse @ obj.matrix_local
                obj.matrix_parent_inverse = Matrix.Identity(4)
                obj.location = parent_obj.location
                obj.rotation_euler = parent_obj.rotation_euler
                if based_on_dimensions and (
                    collider_type == cons.GeometryTypes.CAPSULE or collider_type == cons.GeometryTypes.CYLINDER
                ):
                    update_modifiers(parent_obj)
                    obj.matrix_local = get_matrix_by_dimension_axis_local(
                        parent_obj, parent_obj.dimensions, min_is_height
                    )
        else:
            obj.location = parent_obj.location
            obj.rotation_euler = parent_obj.rotation_euler
            if based_on_dimensions and (
                collider_type == cons.GeometryTypes.CAPSULE or collider_type == cons.GeometryTypes.CYLINDER
            ):
                update_modifiers(parent_obj)
                obj.matrix_local = get_matrix_by_dimension_axis_local(parent_obj, parent_obj.dimensions, min_is_height)
    return obj


def change_site(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    site_type: cons.GeometryTypes,
    obj: Object,
):
    """Change the site geometry type on an object.

    Preserves size when switching between site types and re-applies the
    shape modifier.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        site_type: The target site type.
        obj: The object to modify.
    """

    if obj.Forge_Geometry.type == site_type:
        return

    size = None
    old_type = obj.Forge_Geometry.type
    modifier_name = cons.SiteShapeModifiers[old_type]
    if modifier_name not in obj.modifiers:
        report({"WARNING"}, "Missing shape modifier")
        return
    handler = GeometryHandler.for_site(old_type)
    if modifier_name in obj.modifiers:
        size = handler.get_dimensions(obj.modifiers[modifier_name])
    obj.modifiers.clear()
    obj.lock_scale = cons.LockAxis.LOCKED
    obj.show_in_front = True

    if site_type == cons.GeometryTypes.CAPSULE or site_type == cons.GeometryTypes.CYLINDER:
        obj.matrix_local = get_matrix_by_dimension_axis_local(obj, size)

    set_site_shape(obj, site_type)
    set_site_size(obj, site_type, size)
    obj.Forge_Geometry.type = site_type


def add_site(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    site_type: cons.GeometryTypes,
    parent_obj: Object | None = None,
    size: float | Vector | None = None,
    based_on_dimensions: bool = True,
) -> Object:
    """Create and add a new site object.

    Creates a site (reference frame/point) with the given type and size,
    optionally parenting it under a link.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection.
        site_type: The site type.
        parent_obj: Optional parent link object.
        size: Optional size (default 0.05).
        based_on_dimensions: If True, size is based on object dimensions.

    Returns:
        The newly created site object.
    """

    obj = create_empty_mesh_object(context, "Site")
    update_unique_name(obj, "SIT_")
    obj.Forge_Model_Type = cons.ModelTypes.SITE
    obj.Forge_Geometry.type = site_type
    obj.lock_scale = cons.LockAxis.LOCKED
    obj.show_in_front = True

    link_collection(obj, collection)

    set_site_shape(obj, site_type)
    if size is not None:
        set_site_size(obj, site_type, size, based_on_dimensions)
    else:
        set_site_size(obj, site_type)

    if parent_obj:
        if parent_obj.Forge_Model_Type == cons.ModelTypes.LINK:
            parent_under(obj, parent_obj)

    return obj


def set_parent(
    context: Context,
    obj: Object,
    collection: Collection,
    parent_obj: Object | None = None,
):
    """Set the parent of an object, handling different model types.

    If *parent_obj* is a LINK, REPLICATE, or FRAME, parents directly.
    If *parent_obj*'s parent is one of those, parents under the grandparent.
    Otherwise sets location and marks as root link.

    Args:
        context: The Blender context.
        obj: The child object.
        collection: The target collection (may be reassigned for root links).
        parent_obj: Optional parent object.
    """

    if parent_obj:
        if parent_obj.Forge_Model_Type in [
            cons.ModelTypes.LINK,
            cons.ModelTypes.REPLICATE,
            cons.ModelTypes.FRAME,
        ]:
            parent_under(obj, parent_obj)
        elif parent_obj.parent:
            if parent_obj.parent.Forge_Model_Type in [
                cons.ModelTypes.LINK,
                cons.ModelTypes.REPLICATE,
                cons.ModelTypes.FRAME,
            ]:
                obj.parent = parent_obj.parent
                obj.matrix_parent_inverse = Matrix.Identity(4)
                obj.matrix_local = Matrix.Translation(parent_obj.location)
        else:
            obj.location = parent_obj.location
            obj["Root Link"] = True
            coll_tag = cons.CollectionNames.WORLD
            if coll_tag in bpy.data.collections:
                collection = bpy.data.collections[coll_tag]
            else:
                collection = bpy.data.collections.new(coll_tag)
                context.scene.collection.children.link(collection)
            link_collection(obj, collection)
    else:
        obj["Root Link"] = True


def add_link(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    parent_obj: Object | None = None,
    reverse_parent: bool = False,
) -> Object:
    """Create and add a new link (body) object.

    Adds an empty PLAIN_AXES object configured as a MuJoCo link/body,
    optionally parented under another object.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection.
        parent_obj: Optional parent object.
        reverse_parent: If True, parent *parent_obj* under the new link.

    Returns:
        The newly created link object.
    """

    bpy.ops.object.empty_add(
        type="PLAIN_AXES",
        radius=1,
        align="WORLD",
        location=context.scene.cursor.location,
        rotation=(0, 0, 0),
        scale=(1, 1, 1),
    )
    obj = context.active_object

    name_string_replace(obj, "Empty", "Link")
    update_unique_name(obj, "LNK_")
    obj.Forge_Model_Type = cons.ModelTypes.LINK
    link_collection(obj, collection)
    obj.lock_scale = cons.LockAxis.LOCKED
    obj.show_in_front = True
    scale_gizmo(context, obj)

    if reverse_parent and parent_obj is not None:
        obj.location = parent_obj.matrix_world.to_translation()
        obj.rotation_euler = parent_obj.matrix_world.to_euler()
        set_parent(
            context,
            parent_obj,
            collection,
            obj,
        )
        return obj

    set_parent(
        context,
        obj,
        collection,
        parent_obj,
    )

    return obj


def set_joint_shape(context: Context, joint_type: str, obj: Object):
    """Set the joint shape modifier parameters.

    Updates the joint type in the joint shape modifier and refreshes the UI.

    Args:
        context: The Blender context.
        joint_type: The joint type string.
        obj: The joint object.
    """

    modifier_name = cons.AdditionalShapeModifiers[cons.ModelTypes.JOINT]
    if modifier_name not in obj.modifiers:
        return
    set_modifier_socket(
        obj.modifiers[modifier_name],
        cons.ModifierSockets.Joint.JOINT_TYPE,
        cons.JointShapeModifiers[joint_type],
    )
    obj.modifiers[modifier_name].node_group.interface_update(context)


def set_joint(
    context: Context,
    joint_type: str,
    obj: Object,
):
    """Configure a joint object with type and shape.

    Updates the name, sets the MAD joint properties, adds the joint
    shape modifier, and applies the joint shape.

    Args:
        context: The Blender context.
        joint_type: The joint type.
        obj: The object to configure as a joint.
    """

    update_unique_name(obj, "JNT_")
    data: JointItem = obj.Forge_Joint
    data.joint = bpy.data.objects.get(obj.name)
    data.type = joint_type

    bpy.ops.object.modifier_add_node_group(
        asset_library_type="CUSTOM",
        asset_library_identifier="Forge Library",
        relative_asset_identifier="Shapes.blend/NodeTree/Shape_Joint",
    )
    scale_gizmo(context, obj)

    obj.show_in_front = True

    set_joint_shape(context, joint_type, obj)


def add_joint(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    joint_type: str,
    parent_obj: Object,
) -> Object:
    """Create and add a new joint object.

    Creates a joint (hinge, slide, ball, etc.) parented under a link.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection.
        joint_type: The joint type.
        parent_obj: Parent link object.

    Returns:
        The newly created joint object.
    """

    obj = create_empty_mesh_object(context, "Joint")
    obj.Forge_Model_Type = cons.ModelTypes.JOINT
    obj.lock_scale = cons.LockAxis.LOCKED

    link_collection(obj, collection)
    set_joint(context, joint_type, obj)

    parent_under(obj, parent_obj)
    return obj


def set_actuator(
    context: Context,
    actuator_type: str,
    obj: Object,
    target: Object | None = None,
):
    """Configure an actuator object with type and target.

    Args:
        context: The Blender context.
        actuator_type: The actuator type.
        obj: The object to configure.
        target: The target object the actuator acts upon.
    """

    update_unique_name(obj, "ACT_")
    data: ActuatorItem = obj.Forge_Actuator
    data.target = target
    data.type = actuator_type

    bpy.ops.object.modifier_add_node_group(
        asset_library_type="CUSTOM",
        asset_library_identifier="Forge Library",
        relative_asset_identifier="Shapes.blend/NodeTree/Shape_Actuator",
    )
    scale_gizmo(context, obj)

    obj.show_in_front = True


def add_actuator(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    actuator_type: str,
    target: Object | None = None,
) -> Object:
    """Create and add a new actuator object.

    Creates an actuator (motor, position, velocity control) parented
    under its target.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection.
        actuator_type: The actuator type.
        target: The target object the actuator controls.

    Returns:
        The newly created actuator object.
    """

    obj = create_empty_mesh_object(context, "Actuator")
    obj.Forge_Model_Type = cons.ModelTypes.ACTUATOR
    obj.lock_scale = cons.LockAxis.LOCKED

    link_collection(obj, collection)
    set_actuator(context, actuator_type, obj, target)

    parent_obj = target
    parent_under(obj, parent_obj)
    return obj


def set_tendon_joints(
    context: Context,
    tendon_type: str,
    obj: Object,
    targets: list[Object],
):
    """Configure a tendon object with type and target joints.

    Args:
        context: The Blender context.
        tendon_type: The tendon type.
        obj: The object to configure as a tendon.
        targets: List of target joint/site objects.
    """

    update_unique_name(obj, "TND_")
    data: TendonItem = obj.Forge_Tendon
    data.type = tendon_type
    for target in targets:
        target_item: TendonTargetItem = data.targets.items.add()
        target_item.target = target

    bpy.ops.object.modifier_add_node_group(
        asset_library_type="CUSTOM",
        asset_library_identifier="Forge Library",
        relative_asset_identifier="Shapes.blend/NodeTree/Shape_Tendon",
    )
    scale_gizmo(context, obj)

    obj.show_in_front = True


def add_tendon(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    tendon_type: str,
    targets: list[Object],
) -> Object:
    """Create and add a new tendon object.

    Creates a tendon connecting multiple joints/sites, parented under
    the first target.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection.
        tendon_type: The tendon type.
        targets: List of target objects.

    Returns:
        The newly created tendon object.
    """

    obj = create_empty_mesh_object(context, "Tendon")
    obj.Forge_Model_Type = cons.ModelTypes.TENDON
    obj.lock_scale = cons.LockAxis.LOCKED

    link_collection(obj, collection)
    set_tendon_joints(context, tendon_type, obj, targets)

    parent_obj = targets[0]
    parent_under(obj, parent_obj)
    return obj


def set_equality_targets(
    context: Context,
    equality_type: str,
    obj: Object,
    targets: list[Object],
):
    """Configure an equality constraint object with type and targets.

    Args:
        context: The Blender context.
        equality_type: The equality type (CONNECT, JOINT, etc.).
        obj: The object to configure.
        targets: One or two target objects. The second target is optional for
            body/world and fixed-joint constraints.
    """

    update_unique_name(obj, "EQU_")
    data: EqualityItem = obj.Forge_Equality
    data.equality = bpy.data.objects.get(obj.name)
    data.type = equality_type
    data.old_target_size = 2 if equality_type != cons.EqualityTypes.JOINT else 1
    data.target1 = targets[0]
    data.target2 = targets[1] if len(targets) > 1 else None
    data.target_type = targets[0].Forge_Model_Type

    bpy.ops.object.modifier_add_node_group(
        asset_library_type="CUSTOM",
        asset_library_identifier="Forge Library",
        relative_asset_identifier="Shapes.blend/NodeTree/Shape_Equality",
    )
    scale_gizmo(context, obj)

    obj.show_in_front = True


def add_equality(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    equality_type: str,
    targets: list[Object],
) -> Object:
    """Create and add a new equality constraint object.

    Creates an equality constraint between two objects (e.g. weld, connect),
    parented under the first target.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection.
        equality_type: The equality type.
        targets: List of two target objects.

    Returns:
        The newly created equality object.
    """

    obj = create_empty_mesh_object(context, "Equality")
    obj.Forge_Model_Type = cons.ModelTypes.EQUALITY
    obj.lock_scale = cons.LockAxis.LOCKED

    link_collection(obj, collection)
    set_equality_targets(context, equality_type, obj, targets)

    parent_obj = targets[0]
    parent_under(obj, parent_obj)
    return obj


def set_sensor_targets(
    context: Context,
    sensor_type: str,
    target_type: str,
    obj: Object,
    targets: Object | list[Object],
    ref_type: str | None = None,
):
    """Configure a sensor object with type, target type, and targets.

    Args:
        context: The Blender context.
        sensor_type: The sensor type.
        target_type: The target type string or list of strings.
        obj: The object to configure.
        targets: Target object or list of [target, reference] objects.
        ref_type: Optional reference object's MJCF type when targets includes a reference.
    """

    update_unique_name(obj, "SEN_")
    data: SensorItem = obj.Forge_Sensor
    data.type = sensor_type
    if target_type == cons.SensorTargetTypes.XBODY:
        data.use_xbody = True
    if target_type == cons.SensorTargetTypes.SUBTREE:
        data.use_subtree = True
    if isinstance(targets, list):
        data.target = targets[0]
        data.target_type = target_type

        data.ref = targets[1]
        data.ref_type = ref_type or target_type
    else:
        data.target_type = target_type
        data.target = targets

    bpy.ops.object.modifier_add_node_group(
        asset_library_type="CUSTOM",
        asset_library_identifier="Forge Library",
        relative_asset_identifier="Shapes.blend/NodeTree/Shape_Sensor",
    )
    scale_gizmo(context, obj)

    obj.show_in_front = True


def add_sensor(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    sensor_type: str,
    target_type: str,
    targets: Object | list[Object],
    ref_type: str | None = None,
) -> Object:
    """Create and add a new sensor object.

    Creates a sensor (touch, accelerometer, force, etc.) tracking
    the given target.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection.
        sensor_type: The sensor type.
        target_type: The target type.
        targets: Target object or [target, reference] list.
        ref_type: Optional reference object's MJCF type.

    Returns:
        The newly created sensor object.
    """

    obj = create_empty_mesh_object(context, "Sensor")
    obj.Forge_Model_Type = cons.ModelTypes.SENSOR
    obj.lock_scale = cons.LockAxis.LOCKED

    link_collection(obj, collection)
    set_sensor_targets(context, sensor_type, target_type, obj, targets, ref_type)

    parent_obj = targets[0] if isinstance(targets, list) else targets
    parent_under(obj, parent_obj)
    return obj


def set_contact_targets(
    context: Context,
    contact_type: str,
    obj: Object,
    targets: list[Object],
):
    """Configure a contact pair object with type and targets.

    Args:
        context: The Blender context.
        contact_type: The contact type.
        obj: The object to configure.
        targets: List of two target geometry objects.
    """

    update_unique_name(obj, "CON_")
    data: ContactItem = obj.Forge_Contact

    data.type = contact_type
    data.target1 = targets[0]
    data.target2 = targets[1]

    bpy.ops.object.modifier_add_node_group(
        asset_library_type="CUSTOM",
        asset_library_identifier="Forge Library",
        relative_asset_identifier="Shapes.blend/NodeTree/Shape_Contact",
    )
    scale_gizmo(context, obj)

    obj.show_in_front = True


def add_contact(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    contact_type: str,
    targets: list[Object],
) -> Object:
    """Create and add a new contact pair object.

    Creates a contact pair between two geometries, parented under
    the first target.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection.
        contact_type: The contact type.
        targets: List of two target geometry objects.

    Returns:
        The newly created contact object.
    """

    obj = create_empty_mesh_object(context, "Contact")
    obj.Forge_Model_Type = cons.ModelTypes.CONTACT
    obj.lock_scale = cons.LockAxis.LOCKED

    link_collection(obj, collection)
    set_contact_targets(context, contact_type, obj, targets)

    parent_obj = targets[0]
    parent_under(obj, parent_obj)
    return obj


def set_light_props(
    light_type: str,
    light_mode: str,
    obj: Object,
    target: Object | None = None,
):
    """Set light properties on an object.

    Args:
        light_type: The light type (DIRECTIONAL, POINT, SPOT, etc.).
        light_mode: The light rendering mode.
        obj: The light object.
        target: Optional target object the light points at.
    """

    data: LightItem = obj.Forge_Light
    data.type = light_type
    data.mode = light_mode
    if target:
        data.target = target


def add_light(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    light_type: str,
    light_mode: str,
    targets: Object | list[Object] | None = None,
) -> Object:
    """Create and add a new light object.

    Creates a Blender light configured as a MuJoCo light source,
    parented under the target object.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection.
        light_type: The light type.
        light_mode: The light rendering mode.
        targets: Parent object or [parent, target] list.

    Returns:
        The newly created light object.
    """

    bpy.ops.object.light_add(
        type="SUN" if light_type == cons.LightTypes.DIRECTIONAL else light_type,
        radius=1,
        align="WORLD",
        location=context.scene.cursor.location,
        rotation=(0, 0, 0),
        scale=(1, 1, 1),
    )

    obj = context.active_object
    obj.Forge_Model_Type = cons.ModelTypes.LIGHT
    obj.lock_scale = cons.LockAxis.LOCKED
    obj.show_in_front = True
    obj.data.use_custom_distance = True
    obj.data.energy = 1000
    if light_type == cons.LightTypes.DIRECTIONAL:
        obj.data.energy = 10
    update_unique_name(obj, "LIT_")

    link_collection(obj, collection)
    set_light_props(light_type, light_mode, obj, targets[1] if isinstance(targets, list) else None)

    parent_obj = targets[0] if isinstance(targets, list) else targets
    parent_under(obj, parent_obj)
    return obj


def set_camera_props(
    camera_type: str,
    camera_mode: str,
    obj: Object,
    target: Object | None = None,
):
    """Set camera properties on an object.

    Args:
        camera_type: The camera type.
        camera_mode: The camera rendering mode.
        obj: The camera object.
        target: Optional target object the camera looks at.
    """

    obj.data.type = camera_type[0:5].upper()
    obj.data.lens_unit = "FOV"

    data: CameraItem = obj.Forge_Camera
    data.type = camera_type
    data.mode = camera_mode
    if target:
        data.target = target


def add_camera(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    camera_type: str,
    camera_mode: str,
    targets: Object | list[Object] | None = None,
) -> Object:
    """Create and add a new camera object.

    Creates a Blender camera configured as a MuJoCo camera,
    parented under the target object.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection.
        camera_type: The camera type.
        camera_mode: The camera rendering mode.
        targets: Parent object or [parent, target] list.

    Returns:
        The newly created camera object.
    """

    bpy.ops.object.camera_add(
        align="WORLD",
        location=context.scene.cursor.location,
        rotation=(math.pi * 0.5, 0.0, 0.0),
        scale=(1, 1, 1),
    )

    obj = context.active_object
    obj.Forge_Model_Type = cons.ModelTypes.CAMERA
    obj.lock_scale = cons.LockAxis.LOCKED
    obj.show_in_front = True
    update_unique_name(obj, "CAM_")

    link_collection(obj, collection)
    set_camera_props(camera_type, camera_mode, obj, targets[1] if isinstance(targets, list) else None)

    parent_obj = targets[0] if isinstance(targets, list) else targets
    parent_under(obj, parent_obj)
    return obj


def add_frame(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    parent_obj: Object | None = None,
    reverse_parent: bool = False,
) -> Object:
    """Create and add a new frame object.

    Creates a frame (reference coordinate frame) optionally parented under
    another object. If *reverse_parent* is True, the *parent_obj* is
    parented under the new frame instead.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection.
        parent_obj: Optional parent object.
        reverse_parent: If True, parent *parent_obj* under the new frame.

    Returns:
        The newly created frame object.
    """

    bpy.ops.object.empty_add(
        type="CUBE",
        radius=1,
        align="WORLD",
        location=context.scene.cursor.location,
        rotation=(0, 0, 0),
        scale=(1, 1, 1),
    )
    obj = context.active_object

    name_string_replace(obj, "Empty", "Frame")
    update_unique_name(obj, "FRM_")
    obj.Forge_Model_Type = cons.ModelTypes.FRAME
    link_collection(obj, collection)
    obj.lock_scale = cons.LockAxis.LOCKED
    obj.show_in_front = True
    scale_gizmo(context, obj)

    if reverse_parent:
        set_parent(
            context,
            parent_obj,
            collection,
            obj,
        )
        return obj

    set_parent(
        context,
        obj,
        collection,
        parent_obj,
    )

    return obj


def set_replicate(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    count: int,
    sep: str,
    offset: Vector,
    euler: Vector,
    replicate: Object,
    source_objs: list[Object],
):
    """Configure a replicate modifier with source objects.

    Parents source objects under the replicate object, creates a hidden
    replicate collection, and sets the replicate modifier parameters
    (count, offset, euler angles).

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        count: Number of copies.
        sep: Separator string for naming.
        offset: Offset Vector between copies.
        euler: Euler rotation between copies.
        replicate: The replicate object.
        source_objs: List of source objects to replicate.
    """

    name = ""
    for child in source_objs:
        child.parent = replicate
        name += child.name

    rep_coll = get_collection(context, cons.CollectionNames.REPLICATE)

    replicated_coll = get_collection(context, "REP_" + name, rep_coll)
    replicated_coll.hide_viewport = True

    RS = cons.ModifierSockets.Replicate
    modifier_name = cons.AdditionalShapeModifiers[cons.ModelTypes.REPLICATE]
    if modifier_name not in replicate.modifiers:
        return
    set_modifier_socket(replicate.modifiers[modifier_name], RS.COUNT, count)
    set_modifier_socket(replicate.modifiers[modifier_name], RS.OFFSET, offset)
    set_modifier_socket(replicate.modifiers[modifier_name], RS.EULER, euler)
    set_modifier_socket(replicate.modifiers[modifier_name], RS.COLLECTION, replicated_coll)
    replicate.modifiers[modifier_name].node_group.interface_update(bpy.context)

    modifier_name = cons.AdditionalShapeModifiers[cons.ModelTypes.REPLICATE]
    for source_obj in source_objs:
        link_collection(source_obj, replicated_coll)

        if source_obj.Forge_Model_Type == cons.ModelTypes.REPLICATE:
            if modifier_name not in source_obj.modifiers:
                report({"ERROR"}, f"{source_obj.name} missing {modifier_name} modifier")
                return
            coll: Collection = get_modifier_socket(source_obj.modifiers[modifier_name], RS.COLLECTION)
            coll.hide_viewport = False

            for child_coll in bpy.data.collections:
                if coll.name not in child_coll.children:
                    continue
                child_coll.children.unlink(coll)
            replicated_coll.children.link(coll)
        elif source_obj.Forge_Model_Type == cons.ModelTypes.FRAME:
            link_collection(source_obj, replicated_coll)
            for child in source_obj.children:
                link_collection(child, replicated_coll)
                if child.Forge_Model_Type == cons.ModelTypes.REPLICATE:
                    if modifier_name not in child.modifiers:
                        report({"ERROR"}, f"{child.name} missing {modifier_name} modifier")
                        return
                    coll: Collection = get_modifier_socket(
                        child.modifiers[modifier_name],
                        cons.ModifierSockets.Replicate.COLLECTION,
                    )
                    coll.hide_viewport = False

                    for child_coll in bpy.data.collections:
                        if coll.name not in child_coll.children:
                            continue
                        child_coll.children.unlink(coll)
                    replicated_coll.children.link(coll)
                else:
                    for iter_child in child.children_recursive:
                        link_collection(iter_child, replicated_coll)
        else:
            for child in source_obj.children_recursive:
                link_collection(child, replicated_coll)


def add_replicate(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    count: int,
    sep: str,
    offset: Vector,
    euler: Vector,
    collection: Collection,
    source_objs: list[Object] | None = None,
    parent_obj: Object | None = None,
) -> Object:
    """Create and add a new replicate object.

    Creates a replicate (array/copy pattern) with configurable count,
    offset, and rotation between copies.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        count: Number of copies.
        sep: Separator string.
        offset: Offset Vector between copies.
        euler: Euler rotation between copies.
        collection: Target collection.
        source_objs: Optional list of source objects to replicate.
        parent_obj: Optional parent object.

    Returns:
        The newly created replicate object.
    """

    replicate = create_empty_mesh_object(context, "Replicate")
    replicate.location = (0, 0, 0)
    update_unique_name(replicate, "REP_")
    replicate.Forge_Model_Type = cons.ModelTypes.REPLICATE
    link_collection(replicate, collection)
    replicate.lock_location = cons.LockAxis.LOCKED
    replicate.lock_scale = cons.LockAxis.LOCKED

    data: ReplicateItem = replicate.Forge_Replicate
    data.count = count
    data.sep = sep
    data.offset = offset
    data.euler = euler

    bpy.ops.object.modifier_add_node_group(
        asset_library_type="CUSTOM",
        asset_library_identifier="Forge Library",
        relative_asset_identifier="Shapes.blend/NodeTree/Replicate",
    )

    if source_objs:
        set_replicate(
            context,
            report,
            count,
            sep,
            offset,
            euler,
            replicate,
            source_objs,
        )

    set_parent(
        context,
        replicate,
        collection,
        parent_obj,
    )

    return replicate


def add_inertial(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    parent_obj: Object | None = None,
    inertia_data: tuple[Vector, Quaternion, float, Vector]
    | tuple[Vector, Quaternion, float, Vector, Matrix]
    | None = None,
) -> Object:
    """Create and add a new inertial object.

    Creates an inertial element (mass and inertia tensor) for a link.
    Only supports LINK type parents.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        collection: Target collection.
        parent_obj: Parent link object (required, must be LINK type).
        inertia_data: (pos_world, quat_world, mass, diaginertia), optionally
            followed by the full COM inertia tensor in world axes.

    Returns:
        The newly created inertial object, or None if parent is invalid.
    """

    if parent_obj and parent_obj.Forge_Model_Type != cons.ModelTypes.LINK:
        report({"ERROR"}, "inertial's parent is only support link type")
        return None

    bpy.ops.object.empty_add(
        type="CUBE",
        radius=1.0,
        align="WORLD",
        location=parent_obj.matrix_world.translation if parent_obj else (0, 0, 0),
        rotation=(0, 0, 0),
        scale=(1, 1, 1),
    )
    obj = context.active_object

    name_string_replace(obj, "Empty", "INE_" + (parent_obj.name if parent_obj else "Inertial"))
    update_unique_name(obj)
    obj.Forge_Model_Type = cons.ModelTypes.INERTIAL
    link_collection(obj, collection)
    obj.lock_scale = cons.LockAxis.LOCKED
    obj.show_in_front = True
    obj.parent = parent_obj
    obj.matrix_parent_inverse = Matrix.Identity(4)
    obj.matrix_basis = Matrix.Identity(4)

    if inertia_data is not None:
        location, rotation = inertia_data[:2]
        body_axes = parent_obj.matrix_world.to_quaternion().to_matrix() if parent_obj else Matrix.Identity(3)
        if parent_obj:
            location = parent_obj.matrix_world.inverted() @ location
            rotation = body_axes.to_quaternion().inverted() @ rotation
        obj.matrix_basis = Matrix.LocRotScale(location, rotation, (1, 1, 1))
        inertial_data: InertialItem = obj.Forge_Inertial
        inertial_data.mass = inertia_data[2]
        inertial_data.diaginertia = inertia_data[3]
        if len(inertia_data) == 5:
            inertia_world = inertia_data[4]
            inertia_body = body_axes.transposed() @ inertia_world @ body_axes
            inertial_data.fullinertia = (
                inertia_body[0][0],
                inertia_body[1][1],
                inertia_body[2][2],
                inertia_body[0][1],
                inertia_body[0][2],
                inertia_body[1][2],
            )

    from .inertial import update_empty_display

    update_empty_display(obj)
    return obj


def add_attach(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    attach: AttachData,
    collection: Collection,
    attach_name: str = "",
    parent_obj: Object | None = None,
) -> Object:
    """Create and add a new attach (collection instance) object.

    Instantiates an external collection as an attach element,
    used to include pre-built models.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        attach: AttachData containing model, file, link, prefix info.
        collection: Target collection.
        attach_name: Optional custom name for the instance.
        parent_obj: Optional parent object.

    Returns:
        The newly created attach object.
    """

    sel.clear_select()

    bpy.ops.object.empty_add(
        type="CIRCLE",
        radius=0.8,
        align="WORLD",
        location=(0, 0, 0),
        rotation=(0, 0, 0),
        scale=(1, 1, 1),
    )

    obj = context.active_object
    obj.name = get_unique_object_name(obj, "ATT_" + attach_name)
    obj.Forge_Model_Type = cons.ModelTypes.ATTACH
    obj.lock_location = cons.LockAxis.LOCKED
    obj.lock_rotation = cons.LockAxis.LOCKED
    obj.lock_scale = cons.LockAxis.LOCKED
    scale_gizmo(context, obj)

    data: AttachItem = obj.Forge_Attach
    data.model = attach.model
    data.file = str(attach.file)
    data.link = attach.link
    data.prefix = attach.prefix

    link_collection(obj, collection)

    parent_under(obj, parent_obj)

    return obj


def add_include(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    file: str,
    base_dir: Path,
    collection: Collection,
    include_coll: Collection,
    include_name: str = "",
) -> Object:
    """Create and add a new include (collection instance) object.

    Instantiates an external collection as an include element for
    referencing external MJCF XML files.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
        file: The MJCF file path to include.
        base_dir: Base directory for resolving the file path.
        collection: Target collection.
        include_coll: The source collection to instance.
        include_name: Optional custom name.

    Returns:
        The newly created include object.
    """

    bpy.ops.object.collection_instance_add(
        collection=include_coll.name, align="WORLD", location=(0, 0, 0), scale=(1, 1, 1)
    )
    obj = context.active_object
    if include_name != "":
        obj.name = include_name
    update_unique_name(obj, "INC_")
    obj.Forge_Model_Type = cons.ModelTypes.INCLUDE
    obj.lock_location = cons.LockAxis.LOCKED
    obj.lock_rotation = cons.LockAxis.LOCKED
    obj.lock_scale = cons.LockAxis.LOCKED

    data: IncludeItem = obj.Forge_Include
    data.file = str(file)
    data.rawfile = str(Path(base_dir / file))

    link_collection(obj, collection)

    return obj


def link_parent(
    context: Context,
    obj: Object,
    parent_obj: Object,
):
    """Parent an object under another while preserving world translation.

    Sets the parent and adjusts local transform so the world position
    is maintained.

    Args:
        context: The Blender context.
        obj: The child object.
        parent_obj: The parent object.
    """

    matrix_world = obj.matrix_world.copy()
    obj.parent = parent_obj
    obj.matrix_parent_inverse = Matrix.Identity(4)
    obj.matrix_world = matrix_world


def update_model_collection(context: Context, obj: Object):
    """Move an object into the collection that matches its model type.

    A parented object belongs in the collection named after its model type
    (see *cons.Model_Collection_Names*); an object without a parent belongs in
    the World collection. Objects of a type without a mapped collection — the
    root-only types — are left where they are.

    Args:
        context: The Blender context.
        obj: The object to place.
    """

    coll_tag = cons.Model_Collection_Names.get(obj.Forge_Model_Type)
    if coll_tag is None:
        return
    if not obj.parent:
        coll_tag = cons.CollectionNames.WORLD
    link_collection(obj, get_collection(context, coll_tag))


def update_ui(context: Context):
    """Force a UI redraw for all PROPERTIES panel areas.

    Args:
           context: The Blender context.
    """

    if context is None or context.screen is None:
        return
    for area in context.screen.areas:
        if area.type == "PROPERTIES":
            area.tag_redraw()


# (serialization functions moved to forge_serialization.py — re-exported above)


def set_instance_idname(context: Context, report: Callable[[set[WmReportItems] | None, str], None]):
    """Set the instance ID name on selected body objects.

    Sets the ``INSTANCE_IDNAME`` custom property on selected BODY-type
    objects from the scene property, or removes it if no body is selected.
    On export a marked link receives a copy of the template link's subtree,
    while the template link itself is not exported directly.

    Args:
        context: The Blender context.
        report: Callback for reporting warnings/errors.
    """

    scene = context.scene
    Forge_Props = bpy.data.scenes[scene.Main_Scene].Forge_Props
    applied = 0
    cleared = 0
    # Iterate through all objects in the scene
    for obj in context.selected_objects:
        if obj.Forge_Model_Type == cons.ModelTypes.LINK:
            if Forge_Props.instance_body is not None:
                if "INSTANCE_LINK" in obj:
                    report(
                        {"WARNING"},
                        f"{obj.name} is marked as instance link, skip setting instance idname",
                    )
                    continue
                obj["INSTANCE_IDNAME"] = Forge_Props.instance_body
                applied += 1
            else:
                if "INSTANCE_IDNAME" in obj:
                    del obj["INSTANCE_IDNAME"]
                    cleared += 1
        else:
            report({"WARNING"}, f"{obj.name} is not a BODY")
    if applied:
        report(
            {"INFO"},
            f"Instance '{Forge_Props.instance_body.name}' set on {applied} link(s)",
        )
    elif cleared:
        report({"INFO"}, f"Instance cleared on {cleared} link(s)")
    update_ui(context)


def collect_instance_templates(
    report: Callable[[set[WmReportItems] | None, str], None],
) -> dict[str, Object]:
    """Resolve ``INSTANCE_IDNAME`` markers to their template link objects.

    A link marked with ``INSTANCE_IDNAME`` exports a copy of the template
    link's subtree instead of its own children, and the template link itself
    is not exported directly (it only exists as the copy source).

    Args:
        report: Callback for reporting warnings/info messages.

    Returns:
        Mapping of instance link names to their template link objects.
    """

    templates: dict[str, Object] = {}
    for obj in bpy.data.objects:
        if obj.Forge_Model_Type != cons.ModelTypes.LINK:
            continue
        marker = obj.get("INSTANCE_IDNAME")
        if not marker:
            continue
        # Older files stored the template's name instead of a reference.
        template = bpy.data.objects.get(marker) if isinstance(marker, str) else marker
        if template is None or template == obj or template.Forge_Model_Type != cons.ModelTypes.LINK:
            report(
                {"WARNING"},
                f"{obj.name} instance template '{getattr(template, 'name', marker)}' is invalid,"
                " export it as a normal link",
            )
            continue
        templates[obj.name] = template

    for template in dict.fromkeys(templates.values()):
        report(
            {"INFO"},
            f"'{template.name}' is an instance template, it is not exported directly",
        )

    for name in get_unreferenced_instance_links(templates):
        report(
            {"WARNING"},
            f"Instance link '{name}' is not referenced by any INSTANCE_IDNAME link, skip it for export",
        )
    return templates


def get_unreferenced_instance_links(instance_templates: dict[str, Object]) -> set[str]:
    """Return names of marked instance links referenced by no ``INSTANCE_IDNAME`` link.

    Such links export nothing at all — no body and no assets.

    Args:
        instance_templates: Mapping of instance link names to their template
            link objects (see :func:`collect_instance_templates`).

    Returns:
        Names of marked instance links without any reference.
    """

    referenced_names = {template.name for template in instance_templates.values()}
    return {
        obj.name
        for obj in bpy.data.objects
        if obj.Forge_Model_Type == cons.ModelTypes.LINK
        and obj.get("INSTANCE_LINK")
        and obj.name not in referenced_names
    }


# (fix_image_name moved to forge_serialization.py — re-exported above)


custom_order = [
    "INERTIAL",
    "CAMERA",
    "LIGHT",
    "JOINT",
    "HFIELD",
    "PLANE",
    "VISUAL",
    "COLLIDER",
    "SITE",
    "LINK",
]
order_map = {char: i for i, char in enumerate(custom_order)}


def find_geometry_collections(report: Callable[[set[WmReportItems] | None, str], None]):
    """Find all geometry-related collections for export.

    Gathers the WORLD, VISUAL, COLLIDER, and REPLICATE collections and
    their children.

    Args:
        report: Callback for reporting info messages.

    Returns:
        A list of collections containing geometry objects.
    """

    colls: list[Collection] = []
    if cons.CollectionNames.WORLD in bpy.data.collections:
        colls.append(bpy.data.collections[cons.CollectionNames.WORLD])
    else:
        report({"INFO"}, f"Not find {cons.CollectionNames.WORLD} collection")

    if cons.CollectionNames.LINK in bpy.data.collections:
        colls.append(bpy.data.collections[cons.CollectionNames.LINK])
    else:
        report({"INFO"}, f"Not find {cons.CollectionNames.LINK} collection")

    if cons.CollectionNames.FRAME in bpy.data.collections:
        colls.append(bpy.data.collections[cons.CollectionNames.FRAME])
    else:
        report({"INFO"}, f"Not find {cons.CollectionNames.FRAME} collection")

    if cons.CollectionNames.VISUAL in bpy.data.collections:
        colls.append(bpy.data.collections[cons.CollectionNames.VISUAL])
    else:
        report({"INFO"}, f"Not find {cons.CollectionNames.VISUAL} collection")

    if cons.CollectionNames.COLLIDER in bpy.data.collections:
        colls.append(bpy.data.collections[cons.CollectionNames.COLLIDER])
    else:
        report({"INFO"}, f"Not find {cons.CollectionNames.COLLIDER} collection")

    if cons.CollectionNames.REPLICATE in bpy.data.collections:
        rep_coll = bpy.data.collections[cons.CollectionNames.REPLICATE]
        colls.append(rep_coll)
        for child in rep_coll.children_recursive:
            colls.append(child)

    return colls


def has_exportable_mesh(obj: Object) -> bool:
    """Return whether a mesh object contains at least one exportable triangle.

    Blender can keep an empty mesh datablock attached to a Forge visual or
    collider while the rest of the model remains valid.  Treat that object as
    absent during export.  Rebuilding ``loop_triangles`` here also avoids
    relying on a stale cached value after procedural mesh edits.

    A mesh collider is the exception: ``create_collider`` stores its hull in the
    ``Collider_Convex`` node group and leaves ``obj.data`` empty, so inspecting
    the base datablock alone makes every mesh collider look empty.  The hull only
    yields faces while that node group's ``TO_MESH`` socket is on — which is
    exactly what ``export_collider`` toggles around the STL write — so the
    evaluated mesh is judged with the same toggle applied.

    Args:
        obj: Blender object to inspect.

    Returns:
        ``True`` when the object has mesh data with vertices and triangles.
    """
    if obj.type != "MESH" or obj.data is None:
        return False

    if obj.Forge_Model_Type == cons.ModelTypes.COLLIDER and obj.Forge_Geometry.type == cons.GeometryTypes.MESH:
        modifier_name = cons.ColliderShapeModifiers[cons.GeometryTypes.MESH]
        if modifier_name in obj.modifiers:
            modifier = obj.modifiers[modifier_name]
            convex = cons.ModifierSockets.Convex
            previous = get_modifier_socket(modifier, convex.TOMESH)
            evaluated = None
            try:
                set_modifier_socket(modifier, convex.TOMESH, True)
                modifier.node_group.interface_update(bpy.context)
                evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
                mesh = evaluated.to_mesh()
                mesh.calc_loop_triangles()
                return bool(mesh.vertices) and bool(mesh.loop_triangles)
            finally:
                # Both the temporary evaluated mesh and the modifier socket
                # must be restored when dependency-graph evaluation fails.
                # Keep the socket restoration in an inner finally so a cleanup
                # failure cannot leave the modifier enabled.
                try:
                    if evaluated is not None:
                        evaluated.to_mesh_clear()
                finally:
                    set_modifier_socket(modifier, convex.TOMESH, previous)
                    modifier.node_group.interface_update(bpy.context)
        else:
            mesh = obj.data
            mesh.calc_loop_triangles()
            return bool(mesh.vertices) and bool(mesh.loop_triangles)

    mesh = obj.data
    mesh.calc_loop_triangles()
    return bool(mesh.vertices) and bool(mesh.loop_triangles)


def find_valide_objects(
    obj: Object,
    objects: list[Object],
    report: Callable[[set[WmReportItems] | None, str], None],
    instance_links: set[str] | None = None,
):
    """Recursively collect geometry objects (VISUAL, COLLIDER, PLANE, HFIELD) from *obj*.

    Args:
        obj: The root object to search from.
        objects: List to append found geometry objects to.
        report: Callback used to report skipped empty mesh objects.
        instance_links: Names of links marked as instances; their own subtree
            is replaced by the template copy at export, so it gathers no assets.
    """
    if obj.Forge_Model_Type == cons.ModelTypes.LINK and instance_links and obj.name in instance_links:
        return
    for child in obj.children:
        if child.Forge_Model_Type in [
            cons.ModelTypes.LINK,
            cons.ModelTypes.FRAME,
            cons.ModelTypes.REPLICATE,
        ]:
            if child.Forge_Model_Type == cons.ModelTypes.LINK and instance_links and child.name in instance_links:
                continue
            find_valide_objects(child, objects, report, instance_links)
            continue
        if child.Forge_Model_Type in [
            cons.ModelTypes.VISUAL,
            cons.ModelTypes.COLLIDER,
            cons.ModelTypes.PLANE,
            cons.ModelTypes.HFIELD,
        ]:
            if child.Forge_Geometry.type in cons.MeshGeometryTypes and not has_exportable_mesh(child):
                report(
                    {"WARNING"},
                    f"{child.name} contain zero triangles, exclude for export",
                )
                continue
            objects.append(child)


def find_valide_attachs(obj: Object, objects: list[Object], instance_links: set[str] | None = None):
    """Recursively collect ATTACH type objects from *obj*.

    Args:
        obj: The root object to search from.
        objects: List to append found attach objects to.
        instance_links: Names of links marked as instances; their own subtree
            is replaced by the template copy at export, so it gathers no assets.
    """
    if obj.Forge_Model_Type == cons.ModelTypes.LINK and instance_links and obj.name in instance_links:
        return
    for child in obj.children:
        if child.Forge_Model_Type in [
            cons.ModelTypes.LINK,
            cons.ModelTypes.FRAME,
            cons.ModelTypes.REPLICATE,
        ]:
            if child.Forge_Model_Type == cons.ModelTypes.LINK and instance_links and child.name in instance_links:
                continue
            find_valide_attachs(child, objects, instance_links)
            continue
        if child.Forge_Model_Type == cons.ModelTypes.ATTACH:
            objects.append(child)


def get_sub_paths(context: Context, parent_path):
    """Get or create subdirectory paths for export (assets, mesh, texture).

    Reads compiler configuration from the scene and creates the necessary
    subdirectory structure under *parent_path* for organizing exported files.

    Args:
        context: The Blender context.
        parent_path: The base export directory path.

    Returns:
        A dictionary mapping GSubPaths keys (ASSET, MESH, TEXTURE) to paths.
    """

    scene = context.scene
    dir = {}
    g_compiler: CompilerItem = scene.Forge_GlobalConfig.g_compiler
    if g_compiler.assetdir != "":
        assets_dir = os.path.join(parent_path, g_compiler.assetdir)
        os.makedirs(assets_dir, exist_ok=True)
        dir[cons.GSubPaths.ASSET] = assets_dir
        if g_compiler.meshdir != "":
            meshdir = os.path.join(assets_dir, g_compiler.meshdir)
            os.makedirs(meshdir, exist_ok=True)
            dir[cons.GSubPaths.MESH] = meshdir
        else:
            dir[cons.GSubPaths.MESH] = assets_dir

        if g_compiler.texturedir != "":
            texturedir = os.path.join(assets_dir, g_compiler.texturedir)
            os.makedirs(texturedir, exist_ok=True)
            dir[cons.GSubPaths.TEXTURE] = texturedir
        else:
            dir[cons.GSubPaths.TEXTURE] = assets_dir
    elif g_compiler.meshdir != "" or g_compiler.texturedir != "":
        if g_compiler.meshdir != "":
            meshdir = os.path.join(parent_path, g_compiler.meshdir)
            os.makedirs(meshdir, exist_ok=True)
            dir[cons.GSubPaths.MESH] = meshdir
        else:
            dir[cons.GSubPaths.MESH] = parent_path

        if g_compiler.texturedir != "":
            texturedir = os.path.join(parent_path, g_compiler.texturedir)
            os.makedirs(texturedir, exist_ok=True)
            dir[cons.GSubPaths.TEXTURE] = texturedir
        else:
            dir[cons.GSubPaths.TEXTURE] = parent_path
    else:
        dir[cons.GSubPaths.ASSET] = parent_path
        dir[cons.GSubPaths.MESH] = parent_path
        dir[cons.GSubPaths.TEXTURE] = parent_path

    return dir


def find_attach_collections(report: Callable[[set[WmReportItems] | None, str], None]):
    """Find all attach-related collections for export.

    Gathers the WORLD, ATTACH, and REPLICATE collections and their children.

    Args:
        report: Callback for reporting info messages.

    Returns:
        A list of collections containing attach objects.
    """

    colls: list[Collection] = []
    if cons.CollectionNames.WORLD in bpy.data.collections:
        colls.append(bpy.data.collections[cons.CollectionNames.WORLD])
    else:
        report({"INFO"}, f"Not find {cons.CollectionNames.WORLD} collection")

    if cons.CollectionNames.ATTACH in bpy.data.collections:
        colls.append(bpy.data.collections[cons.CollectionNames.ATTACH])
    else:
        report({"INFO"}, f"Not find {cons.CollectionNames.ATTACH} collection")

    if cons.CollectionNames.REPLICATE in bpy.data.collections:
        rep_coll = bpy.data.collections[cons.CollectionNames.REPLICATE]
        colls.append(rep_coll)
        for child in rep_coll.children_recursive:
            colls.append(child)
    return colls


def find_attach_model(
    obj: Object,
    dir_path: str,
    attach_model_map: dict,
    report: Callable[[set[WmReportItems] | None, str], None],
):
    """Record attach model file path in a mapping.

    Extracts the file path from an attach object and maps it to its model name.

    Args:
        obj: The attach object.
        dir_path: The base directory path for relative path calculation.
        attach_model_map: Dictionary mapping model names to file paths.
        report: Callback for reporting warnings/errors.
    """

    data: AttachItem = obj.Forge_Attach
    file = str(data.file)
    if data.model not in attach_model_map:
        if dir_path in file:
            file = file.replace(dir_path, "")
            attach_model_map[data.model] = "." + file.replace("\\", "/")
        else:
            attach_model_map[data.model] = file.replace("\\", "/")


def parse_attach_model(
    dir_path: str,
    attach_model_map: dict,
    report: Callable[[set[WmReportItems] | None, str], None],
    instance_links: set[str] | None = None,
):
    """Parse all attach models in collections for export.

    Iterates through attach collections, finds all ATTACH type objects,
    and records their model file paths.

    Args:
        dir_path: The base directory path.
        attach_model_map: Dictionary mapping model names to file paths.
        report: Callback for reporting warnings/errors.
        instance_links: Names of links marked as instances; their own subtree
            is replaced by the template copy at export, so it gathers no assets.
    """

    colls = find_attach_collections(report)
    if not colls:
        report(
            {"WARNING"},
            "No attach collection find, make sure World, Attach is set correct, Export canceled",
        )
        return

    root_objects: list[Object] = []
    for coll in colls:
        root_objects.extend([obj for obj in coll.objects if not obj.parent])

    objects: list[Object] = []
    for obj in root_objects:
        if obj.Forge_Model_Type == cons.ModelTypes.ATTACH:
            objects.append(obj)
            continue

        if obj.Forge_Model_Type in [
            cons.ModelTypes.LINK,
            cons.ModelTypes.FRAME,
            cons.ModelTypes.REPLICATE,
        ]:
            find_valide_attachs(obj, objects, instance_links)

    for obj in objects:
        if obj.hide_viewport:
            continue
        find_attach_model(obj, dir_path, attach_model_map, report)


def find_assets(
    context: Context,
    geometry_map: dict,
    attach_model_map: dict,
    hfield_map: dict,
    collider_map: dict,
    geo_materials_map: dict,
    materials_map: dict,
    materials_props_map: dict,
    report: Callable[[set[WmReportItems] | None, str], None],
    instance_templates: dict[str, Object] | None = None,
):
    """Top-level function to gather all assets for export.

    Orchestrates the gathering of geometry data, material data, and
    attach model data by calling the respective parse functions.

    Args:
        context: The Blender context.
        geometry_map: Map of mesh names to exported file paths.
        attach_model_map: Map of model names to attach file paths.
        hfield_map: Map of height field names to exported file paths.
        collider_map: Map of collider names to exported file paths.
        geo_materials_map: Map of object names to material names.
        materials_map: Map of material names to Material objects.
        materials_props_map: Map of material names to material parameters.
        report: Callback for reporting warnings/errors.
        instance_templates: Mapping of instance link names to their template
            link objects; instance subtrees gather no assets. Computed with
            :func:`collect_instance_templates` when omitted.

    Returns:
        True if all data was gathered successfully, False otherwise.
    """

    scene = context.scene
    Forge_Props = bpy.data.scenes[scene.Main_Scene].Forge_Props
    export_glb = Forge_Props.use_glb
    update_xml_only = Forge_Props.update_forge_only
    filepath = bpy.path.abspath(Forge_Props.export_path) if Forge_Props.rel_path else Forge_Props.export_path
    dir_path = os.path.dirname(filepath)
    sub_paths = get_sub_paths(context, dir_path)

    if instance_templates is None:
        instance_templates = collect_instance_templates(report)
    # Instance subtrees gather no assets; unreferenced marked instance links
    # gather none either — they export nothing at all.
    instance_links = set(instance_templates)
    instance_links.update(get_unreferenced_instance_links(instance_templates))

    if not parse_geometry(
        sub_paths,
        geometry_map,
        hfield_map,
        collider_map,
        geo_materials_map,
        materials_map,
        report,
        update_xml_only,
        export_glb,
        instance_links,
    ):
        report({"WARNING"}, "Gather empty geometry data")

    if not parse_material(sub_paths, materials_map, materials_props_map, report):
        report({"WARNING"}, "Gather empty material data")

    parse_attach_model(dir_path, attach_model_map, report, instance_links)

    return True


def get_template_material():
    """Get or create a template material for objects without materials.

    Creates a new "template" material with node-based shading if it does not
    already exist. Like every other material it carries no fake user, so it is
    rebuilt on demand rather than kept alive when nothing references it.


    Returns:
        The template Material object.
    """

    if "template" not in bpy.data.materials:
        mat = bpy.data.materials.new("template")
        ensure_shader_nodes(mat)
        return mat
    else:
        return bpy.data.materials["template"]


def report_missing_material(
    obj: Object,
    report: Callable[[set[WmReportItems] | None, str], None],
):
    """Report a warning about a missing material on an object.

    Args:
        obj: The object missing a material.
        report: Callback for reporting warnings/errors.
    """

    report({"WARNING"}, f"{obj.name} missing material, will export with template material")


def parse_visual(
    obj: Object,
    sub_paths: dict,
    geometry_map: dict,
    geo_materials_map: dict,
    materials_map: dict,
    report: Callable[[set[WmReportItems] | None, str], None],
    update_xml_only: bool = False,
    export_glb: bool = False,
):
    """Parse a visual geometry object for export.

    Exports the mesh or shape geometry, resolves its material, and records
    the material mapping.

    Args:
        obj: The visual geometry object.
        sub_paths: Dictionary of export subdirectory paths.
        geometry_map: Map of mesh names to exported file paths.
        geo_materials_map: Map of object names to material names.
        materials_map: Map of material names to Material objects.
        report: Callback for reporting warnings/errors.
        update_xml_only: If True, skip mesh file export.
        export_glb: If True, export as GLB format instead of OBJ.
    """

    fix_object_name(obj)
    obj_name = obj.name
    mesh_name = obj.data.name
    mat = None
    if obj.Forge_Geometry.type in [
        cons.GeometryTypes.MESH,
        cons.GeometryTypes.SDF,
        cons.GeometryTypes.BOX,
        cons.GeometryTypes.SPHERE,
        cons.GeometryTypes.CAPSULE,
        cons.GeometryTypes.CYLINDER,
    ]:
        if len(obj.material_slots) == 0 or obj.material_slots[0].material is None:
            mat = get_template_material()
            report_missing_material(obj, report)
        else:
            mat = obj.material_slots[0].material
        # Shape primitives serialize by type + size and share one empty
        # "Geom" datablock — only real mesh geometries ship a mesh file.
        if obj.Forge_Geometry.type in cons.MeshGeometryTypes and mesh_name not in geometry_map:
            geometry_map[mesh_name] = [
                f"{obj.data.name}{'.glb' if export_glb else '.obj'}",
                obj,
                sub_paths[cons.GSubPaths.MESH],
            ]

    mat_name = mat.name
    if mat_name not in materials_map:
        materials_map[mat_name] = mat
    geo_materials_map[obj_name] = mat_name


def parse_addition_visual(
    obj: Object,
    sub_paths: dict,
    hfield_map: dict,
    geo_materials_map: dict,
    materials_map: dict,
    report: Callable[[set[WmReportItems] | None, str], None],
    update_xml_only: bool = False,
):
    """Parse additional visual objects (PLANE, HFIELD) for export.

    Exports height field data and resolves materials for non-standard
    visual geometry types.

    Args:
        obj: The plane or height field object.
        sub_paths: Dictionary of export subdirectory paths.
        hfield_map: Map of height field names to exported file paths.
        geo_materials_map: Map of object names to material names.
        materials_map: Map of material names to Material objects.
        report: Callback for reporting warnings/errors.
        update_xml_only: If True, skip file export.
    """

    fix_object_name(obj)
    obj_name = obj.name
    mat = obj.material_slots[0].material if len(obj.material_slots) > 0 else None

    modifier_name = cons.AdditionalShapeModifiers[obj.Forge_Model_Type]
    if modifier_name in obj.modifiers:
        if obj.Forge_Model_Type == cons.ModelTypes.HFIELD:
            if obj_name not in hfield_map:
                hfield_map[obj_name] = [
                    f"{obj.data.name}.hfield",
                    obj,
                    sub_paths[cons.GSubPaths.TEXTURE],
                ]
    else:
        report(
            {"WARNING"},
            f"Not find {obj.Forge_Model_Type} {obj.name} Modifiers {modifier_name}",
        )
        return

    if mat is None:
        mat = get_template_material()
        report_missing_material(obj, report)

    mat_name = mat.name
    if mat_name not in materials_map:
        materials_map[mat_name] = mat
    geo_materials_map[obj_name] = mat_name


def parse_collider(
    obj: Object,
    sub_paths: dict,
    collider_map: dict,
    report: Callable[[set[WmReportItems] | None, str], None],
    update_xml_only: bool = False,
):
    """Parse a collider object for export.

    Exports collider mesh data to STL format and records the mapping.

    Args:
        obj: The collider object.
        sub_paths: Dictionary of export subdirectory paths.
        collider_map: Map of mesh names to exported file paths.
        report: Callback for reporting warnings/errors.
        update_xml_only: If True, skip file export.
    """

    fix_object_name(obj)
    mesh_name = obj.data.name
    if obj.Forge_Geometry.type in cons.MeshGeometryTypes:
        if mesh_name not in collider_map:
            collider_map[mesh_name] = [
                f"{obj.data.name}.stl",
                obj,
                sub_paths[cons.GSubPaths.MESH],
            ]


def parse_geometry(
    sub_paths: dict,
    geometry_map: dict,
    hfield_map: dict,
    collider_map: dict,
    geo_materials_map: dict,
    materials_map: dict,
    report: Callable[[set[WmReportItems] | None, str], None],
    update_xml_only: bool = False,
    export_glb: bool = False,
    instance_links: set[str] | None = None,
):
    """Parse all geometry objects in collections for export.

    Iterates through geometry collections, dispatches each object to
    the appropriate parse function based on its model type.

    Args:
        sub_paths: Dictionary of export subdirectory paths.
        geometry_map: Map of mesh names to exported file paths.
        hfield_map: Map of height field names to exported file paths.
        collider_map: Map of collider names to exported file paths.
        geo_materials_map: Map of object names to material names.
        materials_map: Map of material names to Material objects.
        report: Callback for reporting warnings/errors.
        update_xml_only: If True, skip file export.
        export_glb: If True, export as GLB instead of OBJ.
        instance_links: Names of links marked as instances; their own subtree
            is replaced by the template copy at export, so it gathers no assets.

    Returns:
        True if parsing succeeded, False if no geometry collections found.
    """

    colls = find_geometry_collections(report)
    if not colls:
        report(
            {"WARNING"},
            "No geometry collection find, Export none geometry",
        )
        return False
    root_objects: list[Object] = []
    for coll in colls:
        root_objects.extend([obj for obj in coll.objects if not obj.parent])

    objects: list[Object] = []
    for obj in root_objects:
        if obj.Forge_Model_Type in [
            cons.ModelTypes.VISUAL,
            cons.ModelTypes.COLLIDER,
            cons.ModelTypes.PLANE,
            cons.ModelTypes.HFIELD,
        ]:
            if obj.Forge_Geometry.type in cons.MeshGeometryTypes and not has_exportable_mesh(obj):
                report(
                    {"WARNING"},
                    f"{obj.name} contain zero triangles, exclude for export",
                )
                continue
            objects.append(obj)
            continue

        if obj.Forge_Model_Type in [
            cons.ModelTypes.LINK,
            cons.ModelTypes.FRAME,
            cons.ModelTypes.REPLICATE,
        ]:
            find_valide_objects(obj, objects, report, instance_links)

    for obj in objects:
        if obj.hide_viewport:
            continue
        match obj.Forge_Model_Type:
            case cons.ModelTypes.VISUAL:
                parse_visual(
                    obj,
                    sub_paths,
                    geometry_map,
                    geo_materials_map,
                    materials_map,
                    report,
                    update_xml_only,
                    export_glb,
                )
            case cons.ModelTypes.COLLIDER:
                parse_collider(obj, sub_paths, collider_map, report, update_xml_only)
            case cons.ModelTypes.PLANE | cons.ModelTypes.HFIELD:
                parse_addition_visual(
                    obj,
                    sub_paths,
                    hfield_map,
                    geo_materials_map,
                    materials_map,
                    report,
                    update_xml_only,
                )
            case _:
                continue

    return len(objects) > 0


def get_tiling(node, material_parameters: dict):
    """Extract tiling parameters from a shader node tree.

    Traces the vector input of a texture node to find MAPPING or VECTMATH
    nodes and extracts the tiling/scale value.

    Args:
        node: The texture node whose tiling to extract.
        material_parameters: Dictionary to populate with the TILING value.
    """

    if node.inputs[cons.NodeInputName.VECTOR].is_linked:
        tiling = node.inputs[cons.NodeInputName.VECTOR].links[0].from_node
        match tiling.type:
            case cons.NodeOpTypeName.MAPPING:
                material_parameters[cons.ShaderPropName.TILING] = tiling.inputs[cons.NodeInputName.SCALE].default_value[
                    0:2
                ]
            case cons.NodeOpTypeName.VECTMATH:
                if tiling.operation == cons.NodeOpTypeName.SCALE:
                    material_parameters[cons.ShaderPropName.TILING] = [
                        tiling.inputs[cons.NodeInputName.SCALE].default_value
                    ] * 2
                elif tiling.operation == cons.NodeOpTypeName.MULTIPLY:
                    id = 1 if tiling.inputs[0].is_linked else 0
                    material_parameters[cons.ShaderPropName.TILING] = tiling.inputs[id].default_value[0:2]


def parse_material_tex(node, texture_dir: str, material_parameters: dict, tex_tag):
    """Parse and export a material texture.

    Saves the texture image to the texture directory and records the
    file name in the material parameters dictionary.

    Args:
        node: The texture node to export.
        texture_dir: The texture output directory.
        material_parameters: Dictionary to populate with texture info.
        tex_tag: The key to use in *material_parameters* (e.g. COLORTEX).
    """

    image_name = node.image.name
    fimage_name = fix_image_name(image_name)
    img = bpy.data.images.get(image_name)
    output_path = os.path.join(texture_dir, fimage_name)
    img.file_format = "PNG"
    material_parameters[tex_tag] = [fimage_name, img, output_path]

    if cons.ShaderPropName.TILING in material_parameters:
        return

    get_tiling(node, material_parameters)


def parse_material(
    sub_paths: dict,
    materials_map: dict,
    materials_props_map: dict,
    report: Callable[[set[WmReportItems] | None, str], None],
):
    """Parse all materials for export.

    Iterates through the materials map, extracts shader parameters
    (color, alpha, roughness, metallic, emission, normal, tiling)
    from each material's node tree, and stores them in the properties map.

    Args:
        sub_paths: Dictionary of export subdirectory paths.
        materials_map: Map of material names to Material objects.
        materials_props_map: Output map of material names to parameter dicts.
        report: Callback for reporting warnings/errors.

    Returns:
        True if all materials were parsed successfully, False on error.
    """

    texture_dir = sub_paths[cons.GSubPaths.TEXTURE]

    material_parameters = {}
    material_parameters[cons.ShaderPropName.BACKGROUND] = [None, None, None]
    if "World" in bpy.data.worlds:
        world = bpy.data.worlds["World"]
        if "World Output" in world.node_tree.nodes:
            surface = world.node_tree.nodes["World Output"].inputs["Surface"]
            if surface.is_linked:
                if surface.links[0].from_node.type == cons.ShaderPropName.BACKGROUND:
                    node = surface.links[0].from_node
                    if node.inputs[0].is_linked:
                        image_node = node.inputs[0]
                        if image_node.links[0].from_node.image:
                            image_name = image_node.links[0].from_node.image.name
                            img = bpy.data.images.get(image_name)
                            image_name = bpy.path.ensure_ext(image_name, ".hdr")
                            output_path = os.path.join(texture_dir, image_name)
                            img.file_format = "HDR"
                            material_parameters[cons.ShaderPropName.BACKGROUND] = [
                                image_name,
                                img,
                                output_path,
                            ]
    materials_props_map[cons.ShaderPropName.ENV] = material_parameters

    color = (0.8, 0.8, 0.8, 1.0)
    alpha = 1.0
    emission = (0.8, 0.8, 0.8, 1.0)
    emission_int = 0
    roughness = 0.5
    metallic = 0.0
    for key, mat in materials_map.items():
        material_parameters = {}
        if cons.ShaderPropName.PRINCIPLED not in mat.node_tree.nodes:
            report(
                {"ERROR"},
                f"{mat.name} shader node is not {cons.ShaderPropName.PRINCIPLED}",
            )
            return False
        shader = mat.node_tree.nodes[cons.ShaderPropName.PRINCIPLED]
        if shader.inputs[cons.NodeInputName.COLOR].is_linked:
            node = (
                mat.node_tree.nodes[cons.ShaderPropName.PRINCIPLED].inputs[cons.NodeInputName.COLOR].links[0].from_node
            )
            match node.type:
                case cons.NodeOpTypeName.MIX:
                    colora = node.inputs[cons.NodeInputName.COLORA]
                    colorb = node.inputs[cons.NodeInputName.COLORB]
                    if colora.is_linked:
                        link_node = colora.links[0].from_node
                        if link_node.type != cons.NodeOpTypeName.TEX_IMAGE:
                            report(
                                {"ERROR"},
                                f"{node.name} color A link type is not image texture",
                            )
                            return False

                        parse_material_tex(
                            link_node,
                            texture_dir,
                            material_parameters,
                            cons.ShaderPropName.COLORTEX,
                        )
                    else:
                        report(
                            {"ERROR"},
                            f"{node.name} color A link is empty, link a image texture to it",
                        )
                        return False

                    if colorb.is_linked:
                        link_node = colorb.links[0].from_node
                        if link_node.type != cons.NodeOpTypeName.RGB:
                            report({"ERROR"}, f"{node.name} color B link type is not rgb")
                            return False
                    else:
                        color = colorb.default_value

                case cons.NodeOpTypeName.RGB:
                    material_parameters[cons.ShaderPropName.COLORTEX] = [
                        None,
                        None,
                        None,
                    ]
                    color = node.outputs[0].default_value

                case cons.NodeOpTypeName.TEX_IMAGE:
                    parse_material_tex(
                        node,
                        texture_dir,
                        material_parameters,
                        cons.ShaderPropName.COLORTEX,
                    )
                    color = (1.0, 1.0, 1.0, 1.0)
                case cons.NodeOpTypeName.TEX_CHECKER:
                    # MJCF has a native procedural checker texture
                    # (<texture type="2d" builtin="checker" rgb1 rgb2>); map the
                    # Blender Checker Texture node's two colors onto it.
                    material_parameters[cons.ShaderPropName.COLORTEX] = [None, None, None]
                    material_parameters[cons.ShaderPropName.CHECKER] = [
                        tuple(linear_to_srgb(node.inputs["Color1"].default_value[0:3])),
                        tuple(linear_to_srgb(node.inputs["Color2"].default_value[0:3])),
                    ]
                    if cons.ShaderPropName.TILING not in material_parameters:
                        get_tiling(node, material_parameters)
                    color = (1.0, 1.0, 1.0, 1.0)
        else:
            material_parameters[cons.ShaderPropName.COLORTEX] = [None, None, None]
            color = shader.inputs[cons.NodeInputName.COLOR].default_value

        if shader.inputs[cons.NodeInputName.ALPHA].is_linked:
            node = (
                mat.node_tree.nodes[cons.ShaderPropName.PRINCIPLED].inputs[cons.NodeInputName.ALPHA].links[0].from_node
            )
            match node.type:
                case cons.NodeOpTypeName.MATH:
                    valuea = node.inputs[0]
                    valueb = node.inputs[1]
                    if valuea.is_linked:
                        link_node = valuea.links[0].from_node
                        if link_node.type != cons.NodeOpTypeName.TEX_IMAGE:
                            report(
                                {"ERROR"},
                                f"{node.name} input A link type is not image texture",
                            )
                            return False

                        image_name = link_node.image.name
                        fimage_name = fix_image_name(image_name)
                        if fimage_name != material_parameters[cons.ShaderPropName.COLORTEX][0]:
                            report(
                                {"ERROR"},
                                f"{link_node.name} input A link is not from the color texture nodes alpha",
                            )
                            return False

                        material_parameters[cons.ShaderPropName.ALPHATEX] = material_parameters[
                            cons.ShaderPropName.COLORTEX
                        ]
                    else:
                        report(
                            {"ERROR"},
                            f"{node.name} input A link is empty, link the color texture nodes alpha to it",
                        )
                        return False

                    if valueb.is_linked:
                        link_node = valueb.links[0].from_node
                        if link_node.type != cons.NodeOpTypeName.VALUE:
                            report({"ERROR"}, f"{node.name} input B link type is not value")
                            return False
                    else:
                        alpha = valueb.default_value

                case cons.NodeOpTypeName.VALUE:
                    material_parameters[cons.ShaderPropName.ALPHATEX] = [
                        None,
                        None,
                        None,
                    ]
                    alpha = node.outputs[0].default_value

                case cons.NodeOpTypeName.TEX_IMAGE:
                    image_name = node.image.name
                    fimage_name = fix_image_name(image_name)
                    if fimage_name != material_parameters[cons.ShaderPropName.COLORTEX][0]:
                        report(
                            {"ERROR"},
                            f"{node.name} input A link is not from the color texture nodes alpha",
                        )
                        return False

                    material_parameters[cons.ShaderPropName.ALPHATEX] = material_parameters[
                        cons.ShaderPropName.COLORTEX
                    ]
                    alpha = 1.0
        else:
            material_parameters[cons.ShaderPropName.ALPHATEX] = [None, None, None]
            alpha = shader.inputs[cons.NodeInputName.ALPHA].default_value

        if shader.inputs[cons.NodeInputName.NORMAL].is_linked:
            normal_map = (
                mat.node_tree.nodes[cons.ShaderPropName.PRINCIPLED].inputs[cons.NodeInputName.NORMAL].links[0].from_node
            )
            if normal_map.type == cons.NodeOpTypeName.NORMALMAP:
                if normal_map.inputs[cons.NodeInputName.NCOLOR].is_linked:
                    link_node = normal_map.inputs[cons.NodeInputName.NCOLOR].links[0].from_node
                    image_name = ""
                    if link_node.type == cons.NodeOpTypeName.COMBINEXYZ:
                        image_name = (
                            link_node.inputs["X"]
                            .links[0]
                            .from_node.inputs[cons.NodeInputName.VECTOR]
                            .links[0]
                            .from_node.image.name
                        )
                    else:
                        image_name = link_node.image.name
                    img = bpy.data.images.get(image_name)
                    fimage_name = fix_image_name(image_name)
                    output_path = os.path.join(texture_dir, fimage_name)
                    img.file_format = "PNG"
                    # img.save(filepath=output_path, save_copy=True)
                    material_parameters[cons.ShaderPropName.NORMALTEX] = [
                        fimage_name,
                        img,
                        output_path,
                    ]
                    if cons.ShaderPropName.TILING not in material_parameters:
                        get_tiling(link_node, material_parameters)
                else:
                    material_parameters[cons.ShaderPropName.NORMALTEX] = [
                        None,
                        None,
                        None,
                    ]
            else:
                material_parameters[cons.ShaderPropName.NORMALTEX] = [None, None, None]
        else:
            material_parameters[cons.ShaderPropName.NORMALTEX] = [None, None, None]

        if shader.inputs[cons.NodeInputName.ROUGHNESS].is_linked:
            input = mat.node_tree.nodes[cons.ShaderPropName.PRINCIPLED].inputs[cons.NodeInputName.ROUGHNESS]
            node = input.links[0].from_node
            match node.type:
                case cons.NodeOpTypeName.MATH:
                    valuea = node.inputs[0]
                    valueb = node.inputs[1]
                    if valuea.is_linked:
                        link_node = valuea.links[0].from_node
                        if link_node.type not in [
                            cons.NodeOpTypeName.SEPARATEXYZ,
                            cons.NodeOpTypeName.SEPARATERGB,
                        ]:
                            report(
                                {"ERROR"},
                                f"{node.name} input A link type is not separate xyz or separate color rgb",
                            )
                            return False

                        image_node = link_node.inputs[0].links[0].from_node
                        parse_material_tex(
                            image_node,
                            texture_dir,
                            material_parameters,
                            cons.ShaderPropName.ROUGHNESSTEX,
                        )
                    else:
                        report(
                            {"ERROR"},
                            f"""{node.name} input A link is empty,
link a separate xyz node's output y which use orm texture to it""",
                        )
                        return False

                    if valueb.is_linked:
                        link_node = valueb.links[0].from_node
                        if link_node.type != cons.NodeOpTypeName.VALUE:
                            report({"ERROR"}, f"{node.name} input B link type is not value")
                            return False
                    else:
                        roughness = valueb.default_value

                case cons.NodeOpTypeName.VALUE:
                    material_parameters[cons.ShaderPropName.ROUGHNESSTEX] = [
                        None,
                        None,
                        None,
                    ]
                    roughness = node.outputs[0].default_value

                case cons.NodeOpTypeName.SEPARATEXYZ | cons.NodeOpTypeName.SEPARATERGB:
                    image_node = node.inputs[0].links[0].from_node
                    parse_material_tex(
                        image_node,
                        texture_dir,
                        material_parameters,
                        cons.ShaderPropName.ROUGHNESSTEX,
                    )
                    roughness = 1.0

                case _:
                    report(
                        {"ERROR"},
                        f"""Link a separate xyz node's output y which use orm texture or a value node
to {input}: {node.type} not support for export""",
                    )
                    return False
        else:
            material_parameters[cons.ShaderPropName.ROUGHNESSTEX] = [None, None, None]
            roughness = shader.inputs[cons.NodeInputName.ROUGHNESS].default_value

        if shader.inputs[cons.NodeInputName.METALLIC].is_linked:
            node = (
                mat.node_tree.nodes[cons.ShaderPropName.PRINCIPLED]
                .inputs[cons.NodeInputName.METALLIC]
                .links[0]
                .from_node
            )
            match node.type:
                case cons.NodeOpTypeName.MATH:
                    valuea = node.inputs[0]
                    valueb = node.inputs[1]
                    if valuea.is_linked:
                        link_node = valuea.links[0].from_node
                        if link_node.type not in [
                            cons.NodeOpTypeName.SEPARATEXYZ,
                            cons.NodeOpTypeName.SEPARATERGB,
                        ]:
                            report(
                                {"ERROR"},
                                f"{node.name} input A link type is not separate xyz",
                            )
                            return False

                        image_node = link_node.inputs[0].links[0].from_node
                        image_name = image_node.image.name
                        fimage_name = fix_image_name(image_name)
                        if fimage_name != material_parameters[cons.ShaderPropName.ROUGHNESSTEX][0]:
                            report(
                                {"ERROR"},
                                f"{link_node.name} input vector link is not from the ORM texture nodes",
                            )
                            return False

                        material_parameters[cons.ShaderPropName.METALLICTEX] = material_parameters[
                            cons.ShaderPropName.ROUGHNESSTEX
                        ]
                    else:
                        report(
                            {"ERROR"},
                            f"""{node.name} input A link is empty,
link the same separate xyz node's output z which node the roughness linked to it""",
                        )
                        return False

                    if valueb.is_linked:
                        link_node = valueb.links[0].from_node
                        if link_node.type != cons.NodeOpTypeName.VALUE:
                            report({"ERROR"}, f"{node.name} input B link type is not value")
                            return False
                    else:
                        metallic = valueb.default_value

                case cons.NodeOpTypeName.VALUE:
                    material_parameters[cons.ShaderPropName.METALLICTEX] = [
                        None,
                        None,
                        None,
                    ]
                    metallic = node.outputs[0].default_value

                case cons.NodeOpTypeName.SEPARATEXYZ | cons.NodeOpTypeName.SEPARATERGB:
                    image_node = node.inputs[0].links[0].from_node
                    image_name = image_node.image.name
                    fimage_name = fix_image_name(image_name)
                    if fimage_name != material_parameters[cons.ShaderPropName.ROUGHNESSTEX][0]:
                        report(
                            {"ERROR"},
                            f"{link_node.name} input vector link is not from the ORM texture nodes",
                        )
                        return False

                    material_parameters[cons.ShaderPropName.METALLICTEX] = material_parameters[
                        cons.ShaderPropName.ROUGHNESSTEX
                    ]
                    metallic = 1.0

                case _:
                    report(
                        {"ERROR"},
                        f"""Link the same separate xyz node's output z which node the roughness linked or a value node
to {input}: {node.type} not support for export""",
                    )
                    return False
        else:
            material_parameters[cons.ShaderPropName.METALLICTEX] = [None, None, None]
            metallic = shader.inputs[cons.NodeInputName.METALLIC].default_value

        if shader.inputs[cons.NodeInputName.EMISSION].is_linked:
            node = (
                mat.node_tree.nodes[cons.ShaderPropName.PRINCIPLED]
                .inputs[cons.NodeInputName.EMISSION]
                .links[0]
                .from_node
            )
            match node.type:
                case cons.NodeOpTypeName.MIX:
                    colora = node.inputs[cons.NodeInputName.COLORA]
                    colorb = node.inputs[cons.NodeInputName.COLORB]
                    if colora.is_linked:
                        link_node = colora.links[0].from_node
                        if link_node.type != cons.NodeOpTypeName.TEX_IMAGE:
                            report(
                                {"ERROR"},
                                f"{node.name} color A link type is not image texture",
                            )
                            return False
                        image_name = link_node.image.name
                        fimage_name = fix_image_name(image_name)
                        if fimage_name != material_parameters[cons.ShaderPropName.COLORTEX][0]:
                            parse_material_tex(
                                link_node,
                                texture_dir,
                                material_parameters,
                                cons.ShaderPropName.EMISSIONTEX,
                            )
                        else:
                            material_parameters[cons.ShaderPropName.EMISSIONTEX] = material_parameters[
                                cons.ShaderPropName.COLORTEX
                            ]
                    else:
                        report(
                            {"ERROR"},
                            f"{node.name} color A link is empty, link a image texture to it",
                        )
                        return False

                    if colorb.is_linked:
                        link_node = colorb.links[0].from_node
                        if link_node.type != cons.NodeOpTypeName.RGB:
                            report({"ERROR"}, f"{node.name} color B link type is not rgb")
                            return False
                    else:
                        emission = colorb.default_value

                case cons.NodeOpTypeName.RGB:
                    material_parameters[cons.ShaderPropName.EMISSIONTEX] = [
                        None,
                        None,
                        None,
                    ]
                    emission = node.outputs[0].default_value

                case cons.NodeOpTypeName.TEX_IMAGE:
                    image_name = node.image.name
                    fimage_name = fix_image_name(image_name)
                    if fimage_name != material_parameters[cons.ShaderPropName.COLORTEX][0]:
                        parse_material_tex(
                            node,
                            texture_dir,
                            material_parameters,
                            cons.ShaderPropName.EMISSIONTEX,
                        )
                    else:
                        material_parameters[cons.ShaderPropName.EMISSIONTEX] = material_parameters[
                            cons.ShaderPropName.COLORTEX
                        ]
                    emission = (1.0, 1.0, 1.0, 1.0)
            emission_int = shader.inputs[cons.NodeInputName.EMISSIONST].default_value
        else:
            material_parameters[cons.ShaderPropName.EMISSIONTEX] = [None, None, None]
            emission = shader.inputs[cons.NodeInputName.EMISSION].default_value
            emission_int = shader.inputs[cons.NodeInputName.EMISSIONST].default_value

        if cons.ShaderPropName.TILING not in material_parameters:
            material_parameters[cons.ShaderPropName.TILING] = None

        srgba = list(color[:])
        if alpha < 1.0 and material_parameters[cons.ShaderPropName.ALPHATEX][0] is None:
            srgba[-1] = alpha

        srgba[0:3] = list(linear_to_srgb(srgba[0:3]))[:]
        material_parameters[cons.NodeInputName.COLOR] = srgba
        material_parameters[cons.NodeInputName.ALPHA] = alpha
        material_parameters[cons.NodeInputName.ROUGHNESS] = roughness
        material_parameters[cons.NodeInputName.METALLIC] = metallic
        material_parameters[cons.NodeInputName.EMISSION] = emission
        material_parameters[cons.NodeInputName.EMISSIONST] = emission_int

        materials_props_map[key] = material_parameters
    return True


def Flip_UV_V(obj: Object):
    """Flip the V coordinate of UV maps (1.0 - v).

    Used when exporting to GLB format which has different UV orientation.

    Args:
        obj: The object whose UV layer to flip.
    """

    for uv in obj.data.uv_layers[0].uv:
        uv.vector.y = 1.0 - uv.vector.y


def export_hfield(obj: Object, dir: str, update_xml_only):
    """Export a height field to a binary file.

    Writes the height field data (Nrow, Ncol, and elevation values)
    as a binary file for use in MuJoCo.

    Args:
        obj: The height field object.
        dir: The texture directory path.
        update_xml_only: If True, skip file export.

    Returns:
        The basename of the exported file.
    """

    import struct

    filepath = os.path.join(dir, f"{obj.data.name}.hfield")
    if update_xml_only:
        return os.path.basename(filepath)

    sel.clear_select()
    obj.select_set(True)
    bm = bmesh_copy_from_object(obj, True, False, True)
    try:
        bm.verts.ensure_lookup_table()
        modifier_name = cons.AdditionalShapeModifiers[obj.Forge_Model_Type]

        HS = cons.ModifierSockets.HField
        Nrow = int(get_modifier_socket(obj.modifiers[modifier_name], HS.NROW))
        Ncol = int(get_modifier_socket(obj.modifiers[modifier_name], HS.NCOL))
        if Nrow <= 0 or Ncol <= 0 or Nrow * Ncol > len(bm.verts):
            raise ValueError(
                f"Invalid height-field grid {Nrow}x{Ncol} for evaluated mesh with {len(bm.verts)} vertices"
            )

        hfield = []
        for j in range(Nrow):
            for i in range(Ncol):
                n = i * Nrow + j
                hfield.append(bm.verts[n].co.z)

        with open(filepath, "wb") as file:
            file.write(struct.pack("<i", Nrow))
            file.write(struct.pack("<i", Ncol))
            file.writelines(struct.pack("<f", val) for val in hfield)
    finally:
        bm.free()

    return os.path.basename(filepath)


def export_assets(obj: Object, dir: str, update_xml_only, export_glb):
    """Export a mesh object to GLB or OBJ format.

    Selects the object, resets its world matrix for export, exports the
    mesh in the chosen format, then restores the original transform.

    Args:
        obj: The mesh object to export.
        dir: The mesh output directory path.
        update_xml_only: If True, skip file export.
        export_glb: If True, export as GLB; otherwise export as OBJ.

    Returns:
        The basename of the exported file.
    """

    if export_glb:
        if not update_xml_only:
            require_gltf_addon("export")
        filepath = os.path.join(dir, f"{obj.data.name}.glb")
    else:
        filepath = os.path.join(dir, f"{obj.data.name}.obj")

    if not update_xml_only:
        sel.clear_select()
        obj.select_set(True)

        matrix_world = obj.matrix_world.copy()
        obj.matrix_world = Matrix.Identity(4)
        if export_glb:
            Flip_UV_V(obj)
        obj.data.update()

        if export_glb:
            bpy.ops.export_scene.gltf(
                filepath=filepath,
                export_format="GLB",
                use_selection=True,
                use_active_scene=True,
                export_materials="NONE",
                export_tangents=True,
                export_yup=False,
                export_vertex_color="NONE",
                export_animations=False,
                export_skins=False,
                export_morph=False,
            )
        else:
            bpy.ops.wm.obj_export(
                filepath=filepath,
                export_selected_objects=True,
                export_materials=False,
                forward_axis="Y",
                up_axis="Z",
            )

        obj.matrix_world = matrix_world
        if export_glb:
            Flip_UV_V(obj)
        obj.data.update()

    return os.path.basename(filepath)


def export_collider(obj: Object, dir: str, update_xml_only):
    """Export a collider mesh to STL format.

    Applies the convex hull modifier, exports the mesh as STL, then
    restores the original transform and resets the convex modifier.

    Args:
        obj: The collider object.
        dir: The mesh output directory path.
        update_xml_only: If True, skip file export.

    Returns:
        The basename of the exported file.
    """

    filepath = os.path.join(dir, f"{obj.data.name}.stl")

    modifier_name = cons.ColliderShapeModifiers["MESH"]
    if modifier_name in obj.modifiers:
        set_modifier_socket(obj.modifiers[modifier_name], cons.ModifierSockets.Convex.TOMESH, True)

    if not update_xml_only:
        sel.clear_select()
        obj.select_set(True)

        matrix_world = obj.matrix_world.copy()
        obj.matrix_world = Matrix.Identity(4)
        obj.data.update()
        bpy.ops.wm.stl_export(
            filepath=filepath,
            export_selected_objects=True,
        )
        obj.matrix_world = matrix_world
        obj.data.update()

    if modifier_name in obj.modifiers:
        set_modifier_socket(obj.modifiers[modifier_name], cons.ModifierSockets.Convex.TOMESH, False)

    return os.path.basename(filepath)


def srgb_to_linear(c):
    """Convert an sRGB color value to linear color space.

    Applies the standard sRGB gamma expansion curve. Supports both
    scalar values and tuples/lists (recursive).

    Args:
        c: A single float or a tuple/list of floats in sRGB space.

    Returns:
        The color value(s) in linear space.
    """

    if isinstance(c, (tuple, list)):
        return tuple(srgb_to_linear(v) for v in c)

    if c <= 0.04045:
        return c / 12.92
    else:
        return ((c + 0.055) / 1.055) ** 2.4


def linear_to_srgb(c):
    """Convert a linear color value to sRGB color space.

    Applies the standard sRGB gamma compression curve. Supports both
    scalar values and tuples/lists (recursive).

    Args:
        c: A single float or a tuple/list of floats in linear space.

    Returns:
        The color value(s) in sRGB space.
    """

    if isinstance(c, (tuple, list)):
        return tuple(linear_to_srgb(v) for v in c)

    if c <= 0.0031308:
        return 12.92 * c
    else:
        return 1.055 * (c ** (1 / 2.4)) - 0.055
