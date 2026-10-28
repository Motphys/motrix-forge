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

"""Mesh validation tests — BVH self/inter-object intersection detection (ops/mesh_check.py)."""

import bmesh
import bpy
import pytest
from Forge.core.common import set_modifier_socket
from Forge.core.utils import AABB
from Forge.ops import mesh_check as mc
from mathutils import Vector

from .mjcf_helpers import attach_shape_modifier


def _collector(messages):
    def report(kind, message):
        messages.append((tuple(kind), message))

    return report


def _add_cube(location=(0.0, 0.0, 0.0), size=2.0, visual=True):
    """Add a cube, optionally typed as a MESH visual for the operator poll."""
    bpy.ops.mesh.primitive_cube_add(location=location, size=size)
    obj = bpy.context.active_object
    if visual:
        obj.Forge_Model_Type = "VISUAL"
        obj.Forge_Geometry.type = "MESH"
    return obj


def _add_forge_unit_box(location=(0.0, 0.0, 0.0)):
    """Add the evaluated Geometry_Box used by Forge, rather than a Blender cube."""
    mesh = bpy.data.meshes.new("ForgeUnitBoxMesh")
    obj = bpy.data.objects.new("ForgeUnitBox", mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    obj.Forge_Model_Type = "VISUAL"
    obj.Forge_Geometry.type = "BOX"
    attach_shape_modifier(obj, "Geometry_Box")
    set_modifier_socket(obj.modifiers["Geometry_Box"], "Socket_0", (1.0, 1.0, 1.0))
    return obj


def _select(objects):
    # Only ever select the objects under test — the startup scene may contain
    # a default camera/light that would fail the operator polls.
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
    for obj in objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0] if objects else None


class TestCheckMesh:
    def test_separate_cubes_are_valid(self, registered_props):
        """Non-overlapping objects pass validation."""
        cubes = [_add_cube((-5.0, 0.0, 0.0)), _add_cube((5.0, 0.0, 0.0))]

        messages = []
        assert mc.check_mesh(bpy.context, _collector(messages), cubes) is True
        assert any("All object are validate" in m for _, m in messages)

    def test_overlapping_cubes_report_object_intersection(self, registered_props):
        """Two overlapping objects report an inter-object intersection."""
        cubes = [_add_cube((-0.5, 0.0, 0.0)), _add_cube((0.5, 0.0, 0.0))]

        messages = []
        assert mc.check_mesh(bpy.context, _collector(messages), cubes) is False
        assert any("Object intersection" in m for kind, m in messages if "ERROR" in kind)

    def test_joined_overlapping_cubes_report_self_intersection(self, registered_props):
        """Overlapping shells inside a single object report a self intersection."""
        _add_cube((-0.5, 0.0, 0.0))
        _add_cube((0.5, 0.0, 0.0))
        cubes = list(bpy.context.scene.objects)[-2:]
        _select(cubes)
        bpy.ops.object.join()
        joined = bpy.context.active_object

        messages = []
        assert mc.check_mesh(bpy.context, _collector(messages), [joined]) is False
        assert any("Self intersection" in m for kind, m in messages if "ERROR" in kind)

    def test_touching_cubes_without_penetration_are_valid(self, registered_props):
        """Surface contact without any incident geometry crossing is valid."""
        touching = [_add_cube((-1.0, 0.0, 0.0)), _add_cube((1.0, 0.0, 0.0))]
        messages = []
        assert mc.check_mesh(bpy.context, _collector(messages), touching) is True
        assert not any("Object intersection" in m for kind, m in messages if "ERROR" in kind)

        # With a small gap the same pair validates.
        for obj in bpy.data.objects:
            if obj in touching:
                bpy.data.objects.remove(obj, do_unlink=True)
        gapped = [_add_cube((-1.005, 0.0, 0.0)), _add_cube((1.005, 0.0, 0.0))]
        messages = []
        assert mc.check_mesh(bpy.context, _collector(messages), gapped) is True

    def test_aligned_touching_forge_unit_boxes_are_valid(self, registered_props, asset_lib_available):
        """Forge's evaluated unit-box geometry may share a face without penetration."""
        assert asset_lib_available
        boxes = [_add_forge_unit_box((0.0, 0.0, 0.0)), _add_forge_unit_box((1.0, 0.0, 0.0))]

        messages = []
        assert mc.check_mesh(bpy.context, _collector(messages), boxes) is True
        assert not any("intersection" in message.lower() for _, message in messages)

    def test_aligned_touching_boxes_do_not_depend_on_winding(self, registered_props):
        """A separating contact plane is valid even if imported face winding differs."""
        boxes = [_add_cube((0.0, 0.0, 0.0), size=1.0), _add_cube((1.0, 0.0, 0.0), size=1.0)]
        bm = bmesh.new()
        bm.from_mesh(boxes[1].data)
        bmesh.ops.reverse_faces(bm, faces=list(bm.faces))
        bm.to_mesh(boxes[1].data)
        bm.free()

        messages = []
        assert mc.check_mesh(bpy.context, _collector(messages), boxes) is True
        assert not any("intersection" in message.lower() for _, message in messages)

    def test_open_mesh_reports_non_manifold(self, registered_props):
        """A plane (open mesh, boundary edges) is rejected as non-manifold."""
        bpy.ops.mesh.primitive_plane_add(size=2)
        plane = bpy.context.active_object

        messages = []
        assert mc.check_mesh(bpy.context, _collector(messages), [plane]) is False
        assert any("not manifold" in m for kind, m in messages if "ERROR" in kind)

    def test_empty_mesh_reports_no_faces(self, registered_props):
        """An object with no faces is rejected instead of crashing."""
        mesh = bpy.data.meshes.new("Empty")
        obj = bpy.data.objects.new("EmptyObj", mesh)
        bpy.context.scene.collection.objects.link(obj)

        messages = []
        assert mc.check_mesh(bpy.context, _collector(messages), [obj]) is False
        assert any("has no faces" in m for kind, m in messages if "ERROR" in kind)

    def test_mesh_check_operator_reports_intersection(self, registered_ops):
        """The forge.mesh_check operator surfaces the intersection error."""
        cubes = [_add_cube((-0.5, 0.0, 0.0)), _add_cube((0.5, 0.0, 0.0))]
        _select(cubes)

        with pytest.raises(RuntimeError) as excinfo:
            bpy.ops.forge.mesh_check()
        # The operator reports ERROR -> bpy.ops raises RuntimeError with the report text.
        assert "Object intersection" in str(excinfo.value)


class TestIntersectionPredicates:
    """Unit tests for the low-level geometry predicates."""

    def test_aabb_overlaps(self):
        a = AABB(Vector((0.0, 0.0, 0.0)), Vector((1.0, 1.0, 1.0)))
        hit = AABB(Vector((0.5, 0.5, 0.5)), Vector((2.0, 2.0, 2.0)))
        miss = AABB(Vector((1.5, 0.0, 0.0)), Vector((2.0, 1.0, 1.0)))
        assert mc.aabb_overlaps(a, hit) is True
        assert mc.aabb_overlaps(a, miss) is False

    def test_triangles_intersect(self):
        verts = [
            # Triangle A in the z=0 plane.
            Vector((0.0, 0.0, 0.0)),
            Vector((1.0, 0.0, 0.0)),
            Vector((0.0, 1.0, 0.0)),
            # Triangle B crossing the plane through A's interior.
            Vector((0.25, 0.25, -1.0)),
            Vector((0.25, 0.25, 1.0)),
            Vector((0.5, 0.5, 0.0)),
            # A triangle far away.
            Vector((5.0, 5.0, 5.0)),
            Vector((6.0, 5.0, 5.0)),
            Vector((5.0, 6.0, 5.0)),
        ]
        assert mc.triangles_intersect(verts, (0, 1, 2), (3, 4, 5)) is True
        assert mc.triangles_intersect(verts, (0, 1, 2), (6, 7, 8)) is False

    def test_coplanar_overlap_and_separation(self):
        a = (Vector((0, 0, 0)), Vector((2, 0, 0)), Vector((0, 2, 0)))
        overlap = (Vector((0.25, 0.25, 0)), Vector((1.5, 0.25, 0)), Vector((0.25, 1.5, 0)))
        separate = (Vector((3, 3, 0)), Vector((4, 3, 0)), Vector((3, 4, 0)))

        assert mc.coplanar_triangles_overlap_area(a, overlap, Vector((0, 0, 1))) is True
        assert mc.coplanar_triangles_overlap_area(a, separate, Vector((0, 0, 1))) is False

    def test_opposite_normals_on_overlapping_faces_are_not_an_intersection(self):
        """Coincident back-to-back faces represent a shell, not penetration."""
        vertices = [
            Vector((0, 0, 0)),
            Vector((2, 0, 0)),
            Vector((0, 2, 0)),
            Vector((0, 0, 0)),
            Vector((0, 2, 0)),
            Vector((2, 0, 0)),
        ]
        assert mc.triangles_intersect(vertices, (0, 1, 2), (3, 4, 5)) is False

    def test_same_normals_on_overlapping_faces_are_still_an_intersection(self):
        vertices = [
            Vector((0, 0, 0)),
            Vector((2, 0, 0)),
            Vector((0, 2, 0)),
            Vector((0.25, 0.25, 0)),
            Vector((1.5, 0.25, 0)),
            Vector((0.25, 1.5, 0)),
        ]
        assert mc.triangles_intersect(vertices, (0, 1, 2), (3, 4, 5)) is True

    def test_degenerate_triangle_is_not_an_intersection(self):
        verts = [Vector((0, 0, 0)), Vector((1, 0, 0)), Vector((2, 0, 0))]
        assert mc.triangles_intersect(verts, (0, 1, 2), (0, 1, 2)) is False

    def test_edge_on_other_face_is_contact_not_intersection(self):
        """An edge resting on the interior of another face is not penetration."""
        vertices = [
            # Face B in z=0.
            Vector((0, 0, 0)),
            Vector((2, 0, 0)),
            Vector((0, 2, 0)),
            # Face A has one edge resting in B's interior and extends to one side.
            Vector((0.4, 0.4, 0)),
            Vector((0.8, 0.4, 0)),
            Vector((0.4, 0.4, 1)),
        ]
        assert mc.triangles_intersect(vertices, (0, 1, 2), (3, 4, 5)) is False

    def test_edge_on_other_face_boundary_is_not_intersection(self):
        vertices = [
            Vector((0, 0, 0)),
            Vector((2, 0, 0)),
            Vector((0, 2, 0)),
            Vector((0.4, 0, 0)),
            Vector((0.8, 0, 0)),
            Vector((0.4, 0, 1)),
        ]
        assert mc.triangles_intersect(vertices, (0, 1, 2), (3, 4, 5)) is False

    def test_vertex_on_other_face_without_crossing_is_not_intersection(self):
        """A face touching another face at one point is not penetration."""
        vertices = [
            # Face B in z=0.
            Vector((0, 0, 0)),
            Vector((2, 0, 0)),
            Vector((0, 2, 0)),
            # Only A's first vertex touches B; its incident edges stay above B.
            Vector((0.4, 0.4, 0)),
            Vector((0.4, 0.4, 1)),
            Vector((0.8, 0.4, 1)),
        ]
        assert mc.triangles_intersect(vertices, (0, 1, 2), (3, 4, 5)) is False

    def test_vertex_on_other_face_with_crossing_is_intersection(self):
        """Point contact does not hide incident geometry crossing the other face."""
        vertices = [
            Vector((0, 0, 0)),
            Vector((2, 0, 0)),
            Vector((0, 2, 0)),
            # The first vertex is on B, while the other two straddle its plane.
            Vector((0.4, 0.4, 0)),
            Vector((0.6, 0.4, 1)),
            Vector((0.4, 0.6, -1)),
        ]
        assert mc.triangles_intersect(vertices, (0, 1, 2), (3, 4, 5)) is True

    def test_line_line_overlap_is_not_intersection(self):
        """Two non-coplanar faces sharing only boundary lines do not penetrate."""
        vertices = [
            Vector((0, 0, 0)),
            Vector((1, 0, 0)),
            Vector((0, 1, 0)),
            Vector((0, 0, 0)),
            Vector((1, 0, 0)),
            Vector((0.5, 0, 1)),
        ]
        assert mc.triangles_intersect(vertices, (0, 1, 2), (3, 4, 5)) is False

    def test_point_point_contact_is_not_intersection(self):
        """Two faces meeting only vertex-to-vertex do not penetrate."""
        vertices = [
            Vector((0, 0, 0)),
            Vector((1, 0, 0)),
            Vector((0, 1, 0)),
            Vector((0, 0, 0)),
            Vector((0, -1, 1)),
            Vector((0, -1, -1)),
        ]
        assert mc.triangles_intersect(vertices, (0, 1, 2), (3, 4, 5)) is False

    def test_point_line_contact_is_not_intersection(self):
        """A vertex resting on another face's boundary edge does not penetrate."""
        vertices = [
            Vector((0, 0, 0)),
            Vector((1, 1, 0)),
            Vector((-1, 1, 0)),
            Vector((-1, 0, 0)),
            Vector((1, 0, 0)),
            Vector((0, 0, 1)),
        ]
        assert mc.triangles_intersect(vertices, (0, 1, 2), (3, 4, 5)) is False

    def test_polygon_edges_and_projection_helpers(self):
        assert mc.polygon_edges((3, 1, 2)) == [(1, 3), (1, 2), (2, 3)]
        assert mc.polygon_area([(0, 0), (2, 0), (0, 2)]) == pytest.approx(2.0)
        assert mc.line_intersection_2d((0, 0), (1, 1), (0, 1), (1, 0)) == pytest.approx((0.5, 0.5))
