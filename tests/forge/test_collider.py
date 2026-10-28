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

"""Collider viewport surfaces use evaluated shapes without changing the scene."""

from collections import Counter

import bpy
import numpy as np
import pytest
from Forge.core import collider
from Forge.core import constants as cons
from Forge.core import function as funcs
from Forge.core.common import set_modifier_socket
from mathutils import Vector

from .mjcf_helpers import attach_shape_modifier


@pytest.mark.parametrize("shape", ["BOX", "SPHERE", "CYLINDER", "CAPSULE", "MESH"])
def test_wire_collider_has_closed_surface(registered_props, shape):
    obj = bpy.data.objects.new("ColliderPreview", bpy.data.meshes.new("ColliderPreview"))
    bpy.context.scene.collection.objects.link(obj)
    obj.Forge_Model_Type = cons.ModelTypes.COLLIDER
    obj.Forge_Geometry.type = shape
    attach_shape_modifier(obj, cons.ColliderShapeModifiers[shape])
    modifier = obj.modifiers[cons.ColliderShapeModifiers[shape]]
    if shape == "MESH":
        bpy.ops.mesh.primitive_cube_add(size=2)
        source = bpy.context.object
        set_modifier_socket(modifier, cons.ModifierSockets.Convex.TARGET, source)
        modifier.node_group.interface_update(bpy.context)
    else:
        size = (2, 4, 6) if shape == "BOX" else 2.0 if shape == "SPHERE" else (2, 3)
        funcs.set_collider_size(obj, shape, Vector(size) if isinstance(size, tuple) else size, False)
    bpy.context.view_layer.update()
    depsgraph = bpy.context.evaluated_depsgraph_get()
    evaluated = obj.evaluated_get(depsgraph)
    mesh = evaluated.to_mesh()
    try:
        assert not mesh.polygons
        wire_vertices = np.array([tuple(v.co) for v in mesh.vertices])
    finally:
        evaluated.to_mesh_clear()
    objects_before = len(bpy.data.objects)
    meshes_before = len(bpy.data.meshes)

    vertices, triangles = collider.surface_geometry(obj, depsgraph)

    assert triangles
    edges = Counter(tuple(sorted((a, b))) for t in triangles for a, b in zip(t, (*t[1:], t[0])))
    assert set(edges.values()) == {2}
    np.testing.assert_allclose(np.min(vertices, axis=0), wire_vertices.min(axis=0), atol=1e-5)
    np.testing.assert_allclose(np.max(vertices, axis=0), wire_vertices.max(axis=0), atol=1e-5)
    assert len(bpy.data.objects) == objects_before
    assert len(bpy.data.meshes) == meshes_before
    assert not obj.data.vertices


def test_surface_preserves_existing_faces(registered_props):
    mesh = bpy.data.meshes.new("ConcaveSurface")
    mesh.from_pydata([(0, 0, 0), (3, 0, 0), (1, 1, 0), (0, 3, 0)], [], [(0, 1, 2), (0, 2, 3)])
    obj = bpy.data.objects.new("ConcaveCollider", mesh)
    bpy.context.scene.collection.objects.link(obj)
    bpy.context.view_layer.update()

    vertices, triangles = collider.surface_geometry(obj, bpy.context.evaluated_depsgraph_get())

    assert len(vertices) == 4
    assert triangles == [(0, 1, 2), (0, 2, 3)]


@pytest.mark.parametrize("vertices", [[], [(0, 0, 0), (1, 0, 0)], [(0, 0, 0), (1, 0, 0), (2, 0, 0)]])
def test_degenerate_collider_has_no_surface(registered_props, vertices):
    mesh = bpy.data.meshes.new("Degenerate")
    mesh.from_pydata(vertices, [], [])
    obj = bpy.data.objects.new("DegenerateCollider", mesh)
    bpy.context.scene.collection.objects.link(obj)
    bpy.context.view_layer.update()

    _, triangles = collider.surface_geometry(obj, bpy.context.evaluated_depsgraph_get())

    assert triangles == []


def test_preview_registration_and_cache_invalidation(registered_props):
    collider.register_preview()
    try:
        handle = collider._draw_handle
        collider.register_preview()
        assert collider._draw_handle == handle
        assert bpy.app.handlers.depsgraph_update_post.count(collider._invalidate_batches) == 1
        collider._batches[123] = object()
        collider._clear_batches()
        assert not collider._batches
    finally:
        collider.unregister_preview()
    assert collider._draw_handle is None
    assert collider._invalidate_batches not in bpy.app.handlers.depsgraph_update_post
    assert collider._clear_batches not in bpy.app.handlers.load_post
    assert collider._clear_batches not in bpy.app.handlers.undo_post
    assert collider._clear_batches not in bpy.app.handlers.redo_post


@pytest.fixture
def cached_surfaces(registered_props, monkeypatch):
    from gpu_extras import batch

    # Exercise real dependency-graph updates and geometry extraction without a
    # graphics context. Each stand-in batch keeps the uploaded vertex data.
    builds = []

    def build(shader, mode, vertices, indices):
        result = (vertices["pos"], indices)
        builds.append(result)
        return result

    monkeypatch.setattr(batch, "batch_for_shader", build)
    collider._clear_batches()
    collider.register_preview()
    try:
        yield builds
    finally:
        collider.unregister_preview()


def _cube_collider():
    bpy.ops.mesh.primitive_cube_add()
    obj = bpy.context.object
    obj.Forge_Model_Type = cons.ModelTypes.COLLIDER
    obj.Forge_Geometry.type = cons.GeometryTypes.MESH
    bpy.context.view_layer.update()
    return obj


def test_cache_survives_selection_transforms_and_unrelated_geometry(cached_surfaces):
    obj = _cube_collider()
    other = _cube_collider()
    depsgraph = bpy.context.evaluated_depsgraph_get()
    original = collider._get_batch(obj, depsgraph, None)

    obj.select_set(False)
    obj.location = (3, 2, 1)
    obj.rotation_euler = (0.2, 0.3, 0.4)
    obj.scale = (2, 3, 4)
    bpy.context.view_layer.update()
    assert collider._get_batch(obj, depsgraph, None) is original

    other.data.vertices[0].co.x += 1
    other.data.update()
    bpy.context.view_layer.update()
    assert collider._get_batch(obj, depsgraph, None) is original
    assert len(cached_surfaces) == 1


def test_shared_mesh_edit_invalidates_only_its_users(cached_surfaces):
    first = _cube_collider()
    second = bpy.data.objects.new("SharedCollider", first.data)
    bpy.context.scene.collection.objects.link(second)
    other = _cube_collider()
    bpy.context.view_layer.update()
    depsgraph = bpy.context.evaluated_depsgraph_get()
    original = [collider._get_batch(obj, depsgraph, None) for obj in (first, second, other)]

    first.data.vertices[0].co.x -= 1
    first.data.update()
    bpy.context.view_layer.update()

    assert collider._get_batch(first, depsgraph, None) is not original[0]
    assert collider._get_batch(second, depsgraph, None) is not original[1]
    assert collider._get_batch(other, depsgraph, None) is original[2]
    assert len(cached_surfaces) == 5


def test_reference_geometry_edit_invalidates_convex_surface(cached_surfaces):
    source = _cube_collider()
    obj = bpy.data.objects.new("ConvexPreview", bpy.data.meshes.new("ConvexPreview"))
    bpy.context.scene.collection.objects.link(obj)
    obj.Forge_Model_Type = cons.ModelTypes.COLLIDER
    obj.Forge_Geometry.type = cons.GeometryTypes.MESH
    attach_shape_modifier(obj, cons.ColliderShapeModifiers[cons.GeometryTypes.MESH])
    modifier = obj.modifiers[cons.ColliderShapeModifiers[cons.GeometryTypes.MESH]]
    set_modifier_socket(modifier, cons.ModifierSockets.Convex.TARGET, source)
    modifier.node_group.interface_update(bpy.context)
    bpy.context.view_layer.update()
    depsgraph = bpy.context.evaluated_depsgraph_get()
    original = collider._get_batch(obj, depsgraph, None)

    source.data.vertices[0].co.x = -4
    source.data.update()
    bpy.context.view_layer.update()
    updated = collider._get_batch(obj, depsgraph, None)

    assert updated is not original
    assert min(v[0] for v in updated[0]) == pytest.approx(-4)
    assert len(cached_surfaces) == 2

    modifier.node_group = modifier.node_group.copy()
    modifier.node_group.nodes["Object Info"].transform_space = "RELATIVE"
    bpy.context.view_layer.update()
    before_move = collider._get_batch(obj, depsgraph, None)
    source.location.x = 3
    bpy.context.view_layer.update()
    after_move = collider._get_batch(obj, depsgraph, None)
    assert after_move is not before_move
    assert max(v[0] for v in after_move[0]) == pytest.approx(4)
