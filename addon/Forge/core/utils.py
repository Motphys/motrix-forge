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

from __future__ import annotations

import math
import os
import typing
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import TypeAlias

import bmesh
import bpy
from bpy.types import Collection, Context, Image, Material, Mesh, Object, Panel, Scene
from bpy_extras import object_utils
from mathutils import Matrix, Vector

from . import constants as cons
from .common import set_modifier_socket

BVH_OVERLAP_EPSILON: float = 1e-6
MAX_LEAF_SIZE: int = 2
MAX_AUTO_DEPTH: int = 32
Vec2: TypeAlias = tuple[float, float]
Triangle: TypeAlias = tuple[int, int, int]
Polygon: TypeAlias = tuple[int, ...]
Edge: TypeAlias = tuple[int, int]
FacePair: TypeAlias = tuple[int, int]
BoxRecord: TypeAlias = tuple[Vector, Vector, int]
ColorRGB: TypeAlias = tuple[float, float, float]
ColorRGBA: TypeAlias = tuple[float, float, float, float]


class Generic_PT_SubPanel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED"}

    def get_obj_and_property(self):
        """Return the data collection, property group, and property name for this panel.

        Subclasses must override this to provide the correct context-specific values.
        """

        return None

    def draw_impl(self, context: Context, item, col):
        """Draw additional panel content beneath the main property field.

        Subclasses override this to render custom controls in the provided column layout.
        """

        return None

    def draw_header(self, context: Context):
        """Draw the panel header with an active toggle checkbox.

        Retrieves the data and property from get_obj_and_property, then draws the
        active checkbox for the currently selected item.
        """

        data, props, prop = self.get_obj_and_property(context)
        if len(data.items) > 0:
            if data.active_index >= 0 and data.active_index < len(data.items):
                if prop in props:
                    item = data.items[data.active_index]
                    layout = self.layout
                    active = getattr(item, prop + "_active")
                    if "active" in item:
                        parent_active = getattr(item, "active")
                        layout.active = active and parent_active
                    else:
                        layout.active = active
                    layout.prop(item, prop + "_active", text="")

    def draw(self, context: Context):
        """Draw the panel body including the main property field and delegated sub-controls.

        Uses get_obj_and_property to resolve the active item, renders its property
        with split layout, then calls draw_impl for subclass-specific content.
        """

        data, props, prop = self.get_obj_and_property(context)
        if len(data.items) > 0:
            if data.active_index >= 0 and data.active_index < len(data.items):
                if prop in props:
                    layout = self.layout
                    item = data.items[data.active_index]
                    active = getattr(item, prop + "_active")
                    if "active" in item:
                        parent_active = getattr(item, "active")
                        layout.active = active and parent_active
                    else:
                        layout.active = active
                    layout.use_property_split = True
                    layout.use_property_decorate = False
                    col = layout.column()
                    col.prop(item, prop)

                    self.draw_impl(context, item, col)


class ListFloat_PT_SubPanel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED"}

    def get_obj_and_property(self):
        """Return the data collection, property group, property name, and max size for this panel.

        Subclasses must override this to provide the correct context-specific values.
        """

        return None

    def draw_impl(self, context: Context, item, col):
        """Draw additional panel content beneath the float list controls.

        Subclasses override this to render custom controls in the provided column layout.
        """

        return None

    def draw_header(self, context: Context):
        """Draw the panel header with an active toggle checkbox for a float list property.

        Retrieves the data and property from get_obj_and_property, then draws the
        active checkbox for the currently selected item.
        """

        data, props, prop, _ = self.get_obj_and_property(context)
        if len(data.items) > 0:
            if data.active_index >= 0 and data.active_index < len(data.items):
                if prop in props:
                    item = data.items[data.active_index]
                    layout = self.layout
                    active = getattr(item, prop + "_active")
                    if "active" in item:
                        parent_active = getattr(item, "active")
                        layout.active = active and parent_active
                    else:
                        layout.active = active
                    layout.prop(item, prop + "_active", text="")

    def draw(self, context: Context):
        """Draw the panel body with a float list, add/remove buttons, and delegated sub-controls.

        Uses get_obj_and_property to resolve the active item, renders its float
        collection via a template_list with add/remove operators, then calls
        draw_impl for subclass-specific content.
        """

        data, props, prop, maxsize = self.get_obj_and_property(context)
        if len(data.items) > 0:
            if data.active_index >= 0 and data.active_index < len(data.items):
                if prop in props:
                    layout = self.layout
                    item = data.items[data.active_index]
                    active = getattr(item, prop + "_active")
                    if "active" in item:
                        parent_active = getattr(item, "active")
                        layout.active = active and parent_active
                    else:
                        layout.active = active
                    layout.use_property_split = True
                    layout.use_property_decorate = False
                    listItems = getattr(item, prop)
                    row = layout.row()
                    row.label(text=f"Size: {len(listItems.items)} / {maxsize}")

                    row = layout.row()
                    row.template_list(
                        "Forge_UL_FloatList",
                        prop,
                        listItems,
                        "items",
                        listItems,
                        "active_index",
                        rows=3,
                    )

                    col = row.column(align=True)
                    row = col.column(align=True)
                    row.enabled = len(listItems.items) < maxsize
                    row.operator(props.Forge_OT_FloatItemAdd.bl_idname, icon="ADD", text="").target = prop
                    row = col.column(align=True)
                    row.operator(props.Forge_OT_FloatItemRemove.bl_idname, icon="REMOVE", text="").target = prop

                    self.draw_impl(context, item, col)


class Link:
    """Represents a link (body) with its child classes during import/export."""

    object: Object | None
    childclass: dict | None

    def __init__(self, object: Object | None, childclass: dict | None):
        """Initialize a Link with an optional object and child class dictionary.

        Args:
            object: The Blender object, or None.
            childclass: Dictionary of child class mappings, or None.
        """
        self.object = object
        self.childclass = childclass


class Section:
    """Container for parsed MJCF section elements with a count."""

    count: int
    elements: list[tuple[int, ET.Element],]

    def __init__(self):
        """Initialize an empty Section with zero count."""
        self.count = 0
        self.elements = []


class Scene_Data:
    """Container for a list of scene data items (objects, meshes, etc.) with a count."""

    count: int
    data: list[Object | Mesh | Image | Material | Collection | Scene | str]

    def __init__(self, data: list[Object | Mesh | Image | Material | Collection | Scene] | None = None):
        """Initialize Scene_Data with a list of scene items.

        Args:
            data: List of scene data items (objects, meshes, images, etc.).
        """
        self.data = [] if data is None else data
        self.count = len(self.data)


class Sections:
    """Container for all parsed MJCF sections (compiler, option, worldbody, etc.)."""

    compiler: Section
    option: Section
    statistic: Section
    visual: Section
    asset: Section
    worldbody: Section
    contact: Section
    equality: Section
    tendon: Section
    actuator: Section
    sensor: Section
    defaults: dict
    includes: list
    attachs: dict
    replicates: Scene_Data
    links: dict[int, Link]
    file: str
    base_dir: str
    assets_data: AssetsData

    def __init__(self):
        """Initialize all MJCF sections as empty containers."""
        self.compiler = Section()
        self.option = Section()
        self.statistic = Section()
        self.visual = Section()
        self.asset = Section()
        self.worldbody = Section()
        self.contact = Section()
        self.equality = Section()
        self.tendon = Section()
        self.actuator = Section()
        self.sensor = Section()
        self.defaults = {}
        self.includes = []
        self.attachs = {}
        self.replicates = Scene_Data()
        self.links = {}
        self.file = ""
        self.base_dir = ""
        self.assets_data = AssetsData()


class AssetsData:
    """Container for gathered asset data used during import and export."""

    images: dict
    checker_textures: dict
    objects: dict
    materials_map: dict
    models: dict
    include: dict

    def __init__(self):
        """Initialize an empty AssetsData instance with dicts for all asset categories.

        Creates empty dictionaries for images, checker_textures, objects, materials_map,
        defaults, models, and include entries.
        """

        self.images = {}
        self.checker_textures = {}
        self.objects = {}
        self.materials_map = {}
        self.models = {}
        self.include = {}


class DirectionData:
    """Container for export directory paths (asset, mesh, texture)."""

    basedir: Path | None
    assetdir: str
    meshdir: str
    texturedir: str

    def __init__(self, basedir: Path | None = None, assetdir: str = "", meshdir: str = "", texturedir: str = ""):
        """Initialize a DirectionData instance with paths to asset, mesh, and texture directories.

        Args:
            basedir: Optional base directory path.
            assetdir: Relative path to the assets subdirectory.
            meshdir: Relative path to the meshes subdirectory.
            texturedir: Relative path to the textures subdirectory.
        """

        self.basedir = basedir
        self.assetdir = assetdir
        self.meshdir = meshdir
        self.texturedir = texturedir


class AttachData:
    """Describes a file attachment (model, file, link, prefix) for attach elements."""

    file: Path | None
    model: str
    link: str
    prefix: str

    def __init__(self, file: Path | None = None, model: str = "", link: str = "", prefix: str = ""):
        """Initialize an AttachData instance describing a file attachment for a model.

        Args:
            file: Optional path to the attachment file.
            model: Name of the model.
            link: Link or attachment type identifier.
            prefix: String prefix applied to the attachment.
        """

        self.file = file
        self.model = model
        self.link = link
        self.prefix = prefix

    def copy(self):
        """Return a shallow copy of this AttachData instance.

        Returns:
            A new AttachData with the same file, model, link, and prefix values.
        """

        data = AttachData(self.file, self.model, self.link, self.prefix)
        return data


class AABB:
    """Axis-aligned bounding box with union, surface area, and centroid operations."""

    __slots__ = ("bmin", "bmax")

    def __init__(self, bmin: Vector | None = None, bmax: Vector | None = None) -> None:
        """Initialize an axis-aligned bounding box from optional min and max vectors.

        Args:
            bmin: Minimum corner of the box, or None for an empty AABB.
            bmax: Maximum corner of the box, or None for an empty AABB.
        """

        self.bmin: Vector | None = bmin
        self.bmax: Vector | None = bmax

    def union(self, other: AABB) -> AABB:
        """Expand this AABB in-place to encompass another AABB.

        If this AABB is empty (bmin/bmax is None), it takes on the other's bounds.
        If the other AABB is empty, this AABB is returned unchanged.

        Args:
            other: The AABB to union with this one.

        Returns:
            This AABB after expansion (self).
        """

        if other.bmin is None or other.bmax is None:
            return self
        if self.bmin is None or self.bmax is None:
            self.bmin = other.bmin.copy()
            self.bmax = other.bmax.copy()
            return self
        for i in range(3):
            self.bmin[i] = min(self.bmin[i], other.bmin[i])
            self.bmax[i] = max(self.bmax[i], other.bmax[i])
        return self

    def surface_area(self) -> float:
        """Compute the surface area of this AABB.

        Returns 0.0 if the AABB is empty (bmin or bmax is None).

        Returns:
            The surface area as a float.
        """

        if self.bmin is None or self.bmax is None:
            return 0.0
        d = self.bmax - self.bmin
        return 2.0 * (d.x * d.y + d.y * d.z + d.z * d.x)

    def centroid(self) -> Vector:
        """Return the geometric center (centroid) of this AABB.

        Returns the zero vector if the AABB is empty.

        Returns:
            A Vector representing the midpoint of the AABB.
        """

        if self.bmin is None or self.bmax is None:
            return Vector((0.0, 0.0, 0.0))
        return (self.bmin + self.bmax) * 0.5

    @staticmethod
    def polygon_aabb(vertices: list[Vector], polygon: Polygon) -> AABB:
        """Compute the axis-aligned bounding box for a polygon defined by vertex indices.

        Args:
            vertices: The full list of vertex positions.
            polygon: A tuple of vertex indices forming the polygon.

        Returns:
            An AABB tightly enclosing the polygon.
        """

        points = [vertices[i] for i in polygon]
        bmin = Vector(
            (
                min(v.x for v in points),
                min(v.y for v in points),
                min(v.z for v in points),
            )
        )
        bmax = Vector(
            (
                max(v.x for v in points),
                max(v.y for v in points),
                max(v.z for v in points),
            )
        )
        return AABB(bmin, bmax)


class BVHNode:
    """Bounding Volume Hierarchy node for spatial acceleration queries."""

    __slots__ = ("aabb", "left", "right", "face_indices")

    def __init__(self) -> None:
        """Initialize an empty BVH node with no AABB bounds and no children.

        The AABB starts empty, left/right children are None, and face_indices
        is None (indicating an internal node until assigned).
        """

        self.aabb: AABB = AABB()
        self.left: BVHNode | None = None
        self.right: BVHNode | None = None
        self.face_indices: list[int] | None = None  # None = internal; list = leaf

    # ── SAH-based BVH Build ────────────────────────────────────────
    @staticmethod
    def get_max_depth(face_count: int, max_depth: int, max_leaf_size: int = 2) -> int:
        """Compute the maximum allowed depth for a BVH tree given the number of faces.

        If max_depth is explicitly provided (non-None) it is used directly.
        Otherwise the depth is estimated from the target leaf count based on
        face_count and max_leaf_size, clamped to MAX_AUTO_DEPTH.

        Args:
            face_count: Total number of faces in the mesh.
            max_depth: Explicit maximum depth, or None to auto-calculate.
            max_leaf_size: Maximum number of faces per leaf node (default 2).

        Returns:
            The computed maximum tree depth.
        """

        if max_depth is not None:
            return max(0, int(max_depth))
        if face_count <= max_leaf_size:
            return 0

        target_leaf_count: int = math.ceil(face_count / max_leaf_size)
        return min(MAX_AUTO_DEPTH, max(1, math.ceil(math.log2(target_leaf_count))))

    @staticmethod
    def build(
        polygons: list[Polygon],
        aabbs: list[AABB],
        indices: list[int],
        depth: int,
        max_leaf_size: int = 2,
    ) -> BVHNode:
        """Build a top-down BVH using SAH (Surface Area Heuristic) splitting."""
        node = BVHNode()

        # Compute combined AABB
        combined = AABB()
        for i in indices:
            combined.union(aabbs[i])
        node.aabb = combined

        # Leaf condition
        if len(indices) <= max_leaf_size or depth <= 0:
            node.face_indices = list(indices)
            return node

        # SAH: try each axis, pick best split
        best_cost: float = float("inf")
        best_axis: int = 0
        best_mid: int = len(indices) // 2

        for axis in range(3):
            indices.sort(key=lambda i: aabbs[i].centroid()[axis])
            # Sweep left→right to accumulate AABB
            n: int = len(indices)
            left_aabbs: list[AABB | None] = [None] * n
            right_aabbs: list[AABB | None] = [None] * n

            acc = AABB()
            for i in range(n):
                acc = AABB(acc.bmin.copy(), acc.bmax.copy()) if acc.bmin is not None else AABB()
                acc.union(aabbs[indices[i]])
                left_aabbs[i] = AABB(acc.bmin.copy(), acc.bmax.copy())

            acc = AABB()
            for i in range(n - 1, -1, -1):
                acc = AABB(acc.bmin.copy(), acc.bmax.copy()) if acc.bmin is not None else AABB()
                acc.union(aabbs[indices[i]])
                right_aabbs[i] = AABB(acc.bmin.copy(), acc.bmax.copy())

            parent_sa: float = combined.surface_area()
            if parent_sa < 1e-12:
                continue

            for i in range(1, n):
                left_n = i
                right_n = n - i
                cost: float = (
                    left_n * left_aabbs[i - 1].surface_area() + right_n * right_aabbs[i].surface_area()
                ) / parent_sa
                if cost < best_cost:
                    best_cost = cost
                    best_axis = axis
                    best_mid = i

        # Fallback: if SAH didn't improve, just split at median on longest axis
        extent: Vector = combined.bmax - combined.bmin
        longest: int = max(range(3), key=lambda i: extent[i])
        indices.sort(key=lambda i: aabbs[i].centroid()[longest])
        mid: int = len(indices) // 2
        if best_cost < float("inf"):
            indices.sort(key=lambda i: aabbs[i].centroid()[best_axis])
            mid = best_mid

        if mid == 0 or mid == len(indices):
            node.face_indices = list(indices)
            return node

        node.left = BVHNode.build(polygons, aabbs, indices[:mid], depth - 1, max_leaf_size)
        node.right = BVHNode.build(polygons, aabbs, indices[mid:], depth - 1, max_leaf_size)
        return node


class ObjectBVHData:
    """BVH acceleration data for a mesh object (verts, polygons, triangles, root node)."""

    __slots__ = (
        "obj",
        "verts",
        "polygons",
        "face_triangles",
        "root",
        "build_depth",
    )

    def __init__(
        self,
        obj: Object,
        verts: list[Vector],
        polygons: list[Polygon],
        face_triangles: list[list[Triangle]],
        root: BVHNode,
        build_depth: int,
    ) -> None:
        """Initialize BVH acceleration data for a mesh object.

        Stores the object reference, vertex list, polygon definitions,
        per-face triangle tessellations, the root BVH node, and the
        depth at which the BVH was built.

        Args:
            obj: The Blender mesh object.
            verts: List of vertex positions.
            polygons: List of polygon vertex-index tuples.
            face_triangles: Per-face list of triangle index tuples.
            root: Root node of the constructed BVH tree.
            build_depth: Depth at which the BVH was built.
        """

        self.obj: Object = obj
        self.verts: list[Vector] = verts
        self.polygons: list[Polygon] = polygons
        self.face_triangles: list[list[Triangle]] = face_triangles
        self.root: BVHNode = root
        self.build_depth: int = build_depth


WmReportItems = typing.Literal[
    "DEBUG",  # Debug.
    "INFO",  # Info.
    "OPERATOR",  # Operator.
    "PROPERTY",  # Property.
    "WARNING",  # Warning.
    "ERROR",  # Error.
    "ERROR_INVALID_INPUT",  # Invalid Input.
    "ERROR_INVALID_CONTEXT",  # Invalid Context.
    "ERROR_OUT_OF_MEMORY",  # Out of Memory.
]


# ═══════════════════════════════════════════════════════════════════════
# Shared utility functions (moved from function.py)
# ═══════════════════════════════════════════════════════════════════════


def create_empty_mesh_object(context: Context, mesh_name: str) -> Object:
    """Create a new object using a reusable empty mesh.

    If a mesh named *mesh_name* already exists in ``bpy.data.meshes`` it
    is reused; otherwise a fresh one-vertex mesh is created, used, and the
    vertex is immediately deleted (leaving an empty mesh for future reuse).
    Returns the newly created active object.
    """

    if mesh_name in bpy.data.meshes:
        mesh = bpy.data.meshes[mesh_name]
        object_utils.object_data_add(context, mesh, operator=None)
    else:
        mesh = bpy.data.meshes.new(mesh_name)
        mesh.vertices.add(1)
        object_utils.object_data_add(context, mesh, operator=None)
        # Remove the single vertex using bmesh (avoids 3 bpy.ops calls)
        import bmesh

        bm = bmesh.new()
        bm.from_mesh(mesh)
        bm.verts.ensure_lookup_table()
        if bm.verts:
            bm.verts.remove(bm.verts[0])
        bm.to_mesh(mesh)
        bm.free()
    return context.active_object


def parent_under(
    obj: Object, parent_obj: Object | None, location: Vector | None = None, rotation: Vector | None = None
):
    """Parent *obj* under *parent_obj*, preserving world transform.

    After parenting, zeroes out the local position (or sets it to
    *location* if provided) and rotation, then resets the parent inverse
    so the child aligns with the parent.  A no-op when *parent_obj* is
    ``None``.
    """

    if parent_obj is None:
        return
    obj.parent = parent_obj
    obj.matrix_local = obj.matrix_parent_inverse @ obj.matrix_local
    obj.matrix_parent_inverse = Matrix.Identity(4)
    obj.rotation_euler = rotation if rotation is not None else (0, 0, 0)
    obj.location = location if location is not None else (0, 0, 0)


def update_modifiers(obj: Object):
    """Update all geometry node modifiers on an object.

    Calls ``interface_update`` on every modifier's node group to ensure
    the UI and internal state reflect the latest parameter changes.

    Args:
        obj: The Blender object whose modifiers to update.
    """

    for modifier in obj.modifiers:
        modifier.node_group.interface_update(bpy.context)


def get_unique_object_name(obj: Object, base_name: str, separator: str = "_", max_attempts: int = 10000):
    """Generate a unique object name by appending a numbered suffix.

    If *base_name* is already unique (or belongs to *obj*), return it as-is.
    Otherwise append ``_001``, ``_002``, etc. until an available name is found.

    Args:
        obj: The Blender object requesting the name.
        base_name: The desired base name.
        separator: String to use between name and number (default ``"_"``).
        max_attempts: Maximum number of numbering attempts (default 10000).

    Returns:
        A unique object name string.
    """

    if "." not in base_name and base_name not in bpy.data.objects:
        return base_name
    fixed_name = base_name.replace(".", separator)
    if fixed_name not in bpy.data.objects:
        return fixed_name
    if fixed_name in bpy.data.objects and bpy.data.objects[fixed_name] == obj:
        return fixed_name

    # Strip trailing suffix like .001 if present
    name_base = base_name[:-4] if "." in base_name else base_name
    index = 1
    while index <= max_attempts:
        new_name = f"{name_base}{separator}{str(index).zfill(3)}"
        if new_name not in bpy.data.objects:
            return new_name
        index += 1

    # Fallback: append raw number as last resort
    return f"{name_base}{separator}{index}"


def update_unique_name(obj: Object, prefix: str = ""):
    """Update an object's name to be unique, optionally adding a prefix.

    Prepends *prefix* if not already present, then calls
    :func:`get_unique_object_name` to ensure the name is unique in the scene.

    func:`get_unique_object_name`

    Args:
        obj: The Blender object to rename.
        prefix: Optional prefix string (e.g. ``"GEO_"``, ``"COL_"``).
    """

    new_name = prefix + obj.name if obj.name[0:4] != prefix else obj.name
    new_name = get_unique_object_name(obj, new_name)
    obj.name = new_name


def name_string_replace(obj: Object, old: str, new: str):
    """Replace a substring in an object's name.

    Simple string replacement on ``obj.name``.

    Args:
        obj: The Blender object.
        old: The substring to replace.
        new: The replacement string.
    """

    obj.name = obj.name.replace(old, new)


def get_collection(context: Context, coll_tag: str, parent_coll: Collection | None = None):
    """Get or create a collection by tag name, optionally under a parent.

    If a collection with the given tag already exists in ``bpy.data.collections``
    it is returned directly. Otherwise a new collection is created and linked
    under *parent_coll* or the scene root.

    Args:
        context: The Blender context.
        coll_tag: The collection name/tag to look up or create.
        parent_coll: Optional parent collection to link the new collection under.

    Returns:
        The existing or newly created Collection.
    """

    if coll_tag in bpy.data.collections:
        return bpy.data.collections[coll_tag]
    else:
        collection = bpy.data.collections.new(coll_tag)
        if parent_coll:
            parent_coll.children.link(collection)
        else:
            context.scene.collection.children.link(collection)
        return collection


def check_libs():
    """Check and initialize the Forge Library asset library.

    If the "Forge Library" asset library does not exist in Blender's preferences,
    create it pointing to the ``lib`` subdirectory relative to this file, then
    update the asset library list.
    """

    if "Forge Library" not in bpy.context.preferences.filepaths.asset_libraries:
        bpy.context.preferences.filepaths.asset_libraries.new(
            name="Forge Library",
            directory=os.path.join(os.path.dirname(os.path.dirname(__file__)), "lib\\assets"),
        )
        bpy.context.preferences.filepaths.asset_libraries.update()


def get_bound_center(obj: Object):
    """Calculate the center of an object's bounding box in local coordinates.

    Iterates through the 8 corner vertices of the object's ``bound_box``
    to find the min and max extents, then returns the midpoint.

    Args:
        obj: The Blender object.

    Returns:
        A Vector representing the center of the bounding box.
    """

    max_b = [-math.inf] * 3
    min_b = [math.inf] * 3
    for co in obj.bound_box:
        max_b[0] = max(co[0], max_b[0])
        max_b[1] = max(co[1], max_b[1])
        max_b[2] = max(co[2], max_b[2])
        min_b[0] = min(co[0], min_b[0])
        min_b[1] = min(co[1], min_b[1])
        min_b[2] = min(co[2], min_b[2])
    center = Vector(max_b) + Vector(min_b)
    return center * 0.5


def set_collider_to_mesh(obj: Object, to_mesh: bool):
    """If compute inertia based by collider and have collider shapes,

    Args:
        obj: Collider object to change shape state.
        to_mesh: Enbale or Disable to change shape output with mesh or wireframe.
    """

    if obj.Forge_Model_Type != cons.ModelTypes.COLLIDER:
        return

    modifier_name = cons.ColliderShapeModifiers.get(obj.Forge_Geometry.type)
    if modifier_name and modifier_name in obj.modifiers:
        CS = cons.ModifierSockets.Collider
        match obj.Forge_Geometry.type:
            case cons.GeometryTypes.BOX:
                set_modifier_socket(obj.modifiers[modifier_name], CS.USE_MESH_A, to_mesh)
            case cons.GeometryTypes.CAPSULE | cons.GeometryTypes.CYLINDER:
                set_modifier_socket(obj.modifiers[modifier_name], CS.USE_MESH_B, to_mesh)
            case cons.GeometryTypes.SPHERE:
                set_modifier_socket(obj.modifiers[modifier_name], CS.USE_MESH_A, to_mesh)
            case cons.GeometryTypes.MESH:
                set_modifier_socket(obj.modifiers[modifier_name], CS.USE_MESH_C, to_mesh)

        update_modifiers(obj)


def bmesh_copy_from_object(obj: Object, transform=True, triangulate=True, apply_modifiers=False) -> bmesh.types.BMesh:
    """Returns a transformed, triangulated copy of the mesh.

    Args:
        obj: The source mesh object to copy from.
        transform: When True, the mesh is transformed by the object's
            world matrix so vertices are in global coordinates.
        triangulate: When True, all faces are triangulated in the result.
        apply_modifiers: When True, modifiers on the object are evaluated
            and the result is used instead of the base mesh data.

    Returns:
        A new BMesh containing the mesh data with the requested
        transformations applied.
    """

    assert obj.type == "MESH"

    if apply_modifiers and obj.modifiers:
        depsgraph = bpy.context.evaluated_depsgraph_get()
        obj_eval = obj.evaluated_get(depsgraph)
        me = obj_eval.to_mesh()
        bm = bmesh.new()
        bm.from_mesh(me)
        obj_eval.to_mesh_clear()
    else:
        me = obj.data
        if obj.mode == "EDIT":
            bm_orig = bmesh.from_edit_mesh(me)
            bm = bm_orig.copy()
        else:
            bm = bmesh.new()
            bm.from_mesh(me)

    if transform:
        matrix = obj.matrix_world.copy()
        if not matrix.is_identity:
            bm.transform(matrix)
            # Update normals if the matrix has no rotation.
            matrix.translation.zero()
            if not matrix.is_identity:
                bm.normal_update()

    if triangulate:
        bmesh.ops.triangulate(bm, faces=bm.faces)

    return bm


def fix_object(obj: Object):
    """Fix an object's rotation mode and parent inverse matrix.

    Sets rotation mode to QUATERNION and applies the parent inverse
    matrix to the local matrix, then resets it.

    Args:
        obj: The Blender object to fix.
    """
    obj.rotation_mode = "QUATERNION"
    obj.matrix_local = obj.matrix_parent_inverse @ obj.matrix_local
    obj.matrix_parent_inverse = Matrix.Identity(4)


def find_shape_modifier(obj: Object, tag):
    """Find the shape modifier for a given geometry type on an object.

    Looks up the modifier name from ``GeometryShapeModifiers`` and returns
    it only if it exists and is the sole modifier on the object.

    Args:
        obj: The Blender object.
        tag: The geometry type to look up.

    Returns:
        The modifier if found and unique, otherwise None.
    """
    from .constants import GeometryShapeModifiers

    if GeometryShapeModifiers.get(tag) in obj.modifiers and len(obj.modifiers) == 1:
        return obj.modifiers[GeometryShapeModifiers[tag]]
    return None


def get_height_axis_index(dims: Vector, min_is_height: bool = False) -> int:
    """Get the dimension-axis index that becomes the shape's local Z (height).

    CAPSULE / CYLINDER span their height along local Z, so the reference
    bounding-box axis picked here must be the same one
    ``GeometryHandler.set_size`` uses for radius/height: the largest axis
    normally, the smallest when *min_is_height* is set.

    Ties resolve to the LOWEST index either way, because both ``max`` and
    ``min`` return the first extremum. A tie cannot contradict the size --
    ``set_size`` derives radius/height from the values themselves -- only the
    chosen world axis (X rather than Y for a round shape).

    Args:
        dims: A Vector of dimensions (x, y, z).
        min_is_height: Pick the smallest axis instead of the largest.

    Returns:
        0, 1 or 2 for the X, Y or Z axis.
    """
    if min_is_height:
        return min(range(3), key=lambda i: dims[i])
    return max(range(3), key=lambda i: dims[i])


def get_max_dimension_axis(obj, dims: Vector, min_is_height: bool = False):
    """Get the Euler rotation to align Z with the height axis.

    Returns a hard-coded Euler angle for each axis: X rotates 90 degrees
    around Y, Y rotates -90 degrees around X, Z returns zero rotation. Equal
    dimensions return zero rotation, matching
    :func:`get_matrix_by_dimension_axis_local`.

    Args:
        obj: The Blender object (unused, kept for API consistency).
        dims: A Vector of dimensions (x, y, z).
        min_is_height: Use the smallest axis as the height instead of the
            largest, matching ``GeometryHandler.set_size``.

    Returns:
        A Vector Euler rotation.
    """
    if dims.x == dims.y and dims.x == dims.z:
        return Vector()
    axis_index = get_height_axis_index(dims, min_is_height)
    return [Vector((0.0, math.pi * 0.5, 0.0)), Vector((-math.pi * 0.5, 0.0, 0.0)), Vector()][axis_index]


def get_matrix_by_dimension_axis_local(obj: Object, dims: Vector, min_is_height: bool = False):
    """Get a modified local matrix that reorients the Z axis to the height axis.

    If all dimensions are equal or Z already is the height axis, returns the
    original local matrix. Otherwise swaps columns so the height axis aligns
    with the Z axis.

    Args:
        obj: The Blender object.
        dims: A Vector of dimensions (x, y, z).
        min_is_height: Align Z with the smallest dimension axis instead of the
            largest, matching ``GeometryHandler.set_size``.

    Returns:
        The adjusted local Matrix.
    """
    if dims.x == dims.y and dims.x == dims.z:
        return obj.matrix_local
    axis = ["X", "Y", "Z"][get_height_axis_index(dims, min_is_height)]

    if axis == "Z":
        return obj.matrix_local

    mat = obj.matrix_local.copy()
    if axis == "X":
        tmp = mat.col[2].copy()
        mat.col[2] = mat.col[0].copy()
        mat.col[0] = -tmp
    elif axis == "Y":
        tmp = mat.col[2].copy()
        mat.col[2] = mat.col[1].copy()
        mat.col[1] = -tmp
    return mat
