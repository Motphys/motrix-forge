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

"""Translucent viewport surfaces for wireframe collider geometry."""

import math

import bmesh
import bpy
from bpy.app.handlers import persistent

from ..settings import get_addon_prefs
from . import constants as cons

_draw_handle = None
_batches = {}
_batch_sources = {}
_shader = None


def _rounded_surface(mesh, capsule):
    """Tessellate round shapes; sparse wire rings alone give a coarse hull."""
    lower = [min(v.co[i] for v in mesh.vertices) for i in range(3)]
    upper = [max(v.co[i] for v in mesh.vertices) for i in range(3)]
    center = [(a + b) * 0.5 for a, b in zip(lower, upper)]
    radius = (upper[0] - lower[0]) * 0.5
    half_height = max(0.0, (upper[2] - lower[2]) * 0.5 - radius) if capsule else 0.0
    if radius <= 0:
        return [], []
    segments = 32
    rings = [(i * math.pi / 16, -half_height) for i in range(-7, 1)]
    rings += [(i * math.pi / 16, half_height) for i in range(0 if half_height > 0 else 1, 8)]
    vertices = [(center[0], center[1], center[2] - radius - half_height)]
    for latitude, offset in rings:
        for j in range(segments):
            longitude = j * 2 * math.pi / segments
            vertices.append(
                (
                    center[0] + radius * math.cos(latitude) * math.cos(longitude),
                    center[1] + radius * math.cos(latitude) * math.sin(longitude),
                    center[2] + radius * math.sin(latitude) + offset,
                )
            )
    top = len(vertices)
    vertices.append((center[0], center[1], center[2] + radius + half_height))
    triangles = []
    for j in range(segments):
        next_j = (j + 1) % segments
        triangles.append((0, 1 + next_j, 1 + j))
        for ring in range(len(rings) - 1):
            a, b = 1 + ring * segments + j, 1 + ring * segments + next_j
            triangles.extend(((a, b, b + segments), (a, b + segments, a + segments)))
        last = 1 + (len(rings) - 1) * segments
        triangles.append((last + j, last + next_j, top))
    return vertices, triangles


def surface_geometry(obj, depsgraph):
    """Read evaluated local geometry, closing wire-only convex shapes."""
    evaluated = obj.evaluated_get(depsgraph)
    mesh = evaluated.to_mesh()
    try:
        if mesh is None or len(mesh.vertices) < 3:
            return [], []
        if mesh.polygons:
            mesh.calc_loop_triangles()
            return [tuple(v.co) for v in mesh.vertices], [tuple(t.vertices) for t in mesh.loop_triangles]
        shape = obj.Forge_Geometry.type
        if (
            shape in {cons.GeometryTypes.SPHERE, cons.GeometryTypes.CAPSULE}
            and cons.ColliderShapeModifiers[shape] in obj.modifiers
        ):
            return _rounded_surface(mesh, shape == cons.GeometryTypes.CAPSULE)

        # Collider node groups normally strip faces for their native wire
        # display. Their evaluated vertices still describe the convex surface,
        # including reference-object bounds and the generated mesh hull.
        bm = bmesh.new()
        try:
            for vertex in mesh.vertices:
                bm.verts.new(vertex.co)
            bmesh.ops.convex_hull(bm, input=list(bm.verts), use_existing_faces=False)
            bmesh.ops.triangulate(bm, faces=list(bm.faces))
            bm.verts.index_update()
            return [tuple(v.co) for v in bm.verts], [tuple(v.index for v in f.verts) for f in bm.faces]
        finally:
            bm.free()
    finally:
        evaluated.to_mesh_clear()


@persistent
def _clear_batches(*_args):
    global _shader

    _batches.clear()
    _batch_sources.clear()
    _shader = None


@persistent
def _invalidate_batches(scene, depsgraph):
    """Keep local-space batches through selection and transform-only updates."""
    changed_objects = set()
    changed_meshes = set()
    geometry_changed = False
    for update in depsgraph.updates:
        if not update.is_updated_geometry:
            continue
        geometry_changed = True
        data = update.id.original
        if isinstance(data, bpy.types.Object):
            changed_objects.add(data.as_pointer())
        elif isinstance(data, bpy.types.Mesh):
            changed_meshes.add(data.as_pointer())
    if not geometry_changed:
        return
    for key, (obj, mesh) in tuple(_batch_sources.items()):
        try:
            invalid = (
                not obj.as_pointer()
                or not mesh.as_pointer()
                or obj.as_pointer() in changed_objects
                or mesh.as_pointer() in changed_meshes
            )
        except ReferenceError:
            invalid = True
        if invalid:
            _batches.pop(key, None)
            _batch_sources.pop(key, None)


def _get_shader():
    global _shader
    if _shader is None:
        import gpu

        _shader = gpu.shader.from_builtin("UNIFORM_COLOR")
    return _shader


def _get_batch(obj, depsgraph, shader):
    from gpu_extras.batch import batch_for_shader

    # Different view layers can evaluate the same object differently.
    key = (depsgraph.as_pointer(), obj.as_pointer())
    if key not in _batches:
        vertices, triangles = surface_geometry(obj, depsgraph)
        _batches[key] = batch_for_shader(shader, "TRIS", {"pos": vertices}, indices=triangles) if triangles else None
        _batch_sources[key] = (obj, obj.data)
    return _batches[key]


def _draw_previews():
    prefs = get_addon_prefs()
    if prefs is not None and not prefs.show_collider_preview:
        return

    import gpu

    context = bpy.context
    space = context.space_data
    if not space.overlay.show_overlays or not space.overlay.show_extras:
        return
    shader = _get_shader()
    depsgraph = context.evaluated_depsgraph_get()
    depth_test = gpu.state.depth_test_get()
    depth_mask = gpu.state.depth_mask_get()
    blend = gpu.state.blend_get()
    try:
        gpu.state.blend_set("ALPHA")
        gpu.state.depth_test_set("LESS_EQUAL")
        gpu.state.depth_mask_set(False)
        for obj in context.visible_objects:
            if obj.type != "MESH" or obj.Forge_Model_Type != cons.ModelTypes.COLLIDER:
                continue
            batch = _get_batch(obj, depsgraph, shader)
            if batch is None:
                continue
            color = (1.0, 0.6, 0.1, 0.4) if obj.select_get() else (0.2, 0.6, 1.0, 0.05)
            shader.bind()
            shader.uniform_float("color", color)
            with gpu.matrix.push_pop():
                gpu.matrix.multiply_matrix(obj.matrix_world)
                batch.draw(shader)
    finally:
        gpu.state.depth_mask_set(depth_mask)
        gpu.state.depth_test_set(depth_test)
        gpu.state.blend_set(blend)


def register_preview():
    global _draw_handle
    if _draw_handle is None:
        _draw_handle = bpy.types.SpaceView3D.draw_handler_add(_draw_previews, (), "WINDOW", "POST_VIEW")
    if _invalidate_batches not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(_invalidate_batches)
    for handlers in (bpy.app.handlers.load_post, bpy.app.handlers.undo_post, bpy.app.handlers.redo_post):
        if _clear_batches not in handlers:
            handlers.append(_clear_batches)


def unregister_preview():
    global _draw_handle
    if _draw_handle is not None:
        bpy.types.SpaceView3D.draw_handler_remove(_draw_handle, "WINDOW")
        _draw_handle = None
    if _invalidate_batches in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(_invalidate_batches)
    for handlers in (bpy.app.handlers.load_post, bpy.app.handlers.undo_post, bpy.app.handlers.redo_post):
        if _clear_batches in handlers:
            handlers.remove(_clear_batches)
    _clear_batches()
