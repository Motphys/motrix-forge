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

"""Focused tests for Forge core helpers and geometry behavior."""

from types import SimpleNamespace

import bpy
import pytest
from Forge.core import common, function, selection, utils
from Forge.core import constants as cons
from Forge.core import serialization as ser
from Forge.core.geometry_handler import GeometryHandler
from mathutils import Euler, Matrix, Vector

from .mjcf_helpers import collector, headless_shape_modifiers


class TestCommonAndObjectUtilities:
    def test_equality_target_setter_accepts_one_target(self, registered_props):
        target = bpy.data.objects.new("Target", None)
        target.Forge_Model_Type = cons.ModelTypes.JOINT
        bpy.context.collection.objects.link(target)
        equality = utils.create_empty_mesh_object(bpy.context, "Equality")
        equality.Forge_Model_Type = cons.ModelTypes.EQUALITY

        with headless_shape_modifiers():
            function.set_equality_targets(bpy.context, cons.EqualityTypes.JOINT, equality, [target])

        assert equality.Forge_Equality.target1 is target
        assert equality.Forge_Equality.target2 is None

    def test_selection_order_removes_all_deselected_entries(self):
        objects = []
        for index in range(4):
            obj = bpy.data.objects.new(f"ordered-{index}", None)
            bpy.context.collection.objects.link(obj)
            obj["selected_order"] = index
            obj.select_set(index == 3)
            objects.append(obj)

        selection.update_selection_order()

        assert [obj.get("selected_order") for obj in objects] == [None, None, None, 0]

    def test_get_socket(self):
        assert common.get_socket("Socket_0") == '["Socket_0"]'

    def test_link_collection_moves_object(self):
        obj = bpy.data.objects.new("MoveMe", None)
        source = bpy.data.collections.new("Source")
        target = bpy.data.collections.new("Target")
        bpy.context.scene.collection.children.link(source)
        bpy.context.scene.collection.children.link(target)
        source.objects.link(obj)

        common.link_collection(obj, target)

        assert list(obj.users_collection) == [target]

    def test_create_empty_mesh_reuses_data(self):
        first = utils.create_empty_mesh_object(bpy.context, "ReusableEmpty")
        second = utils.create_empty_mesh_object(bpy.context, "ReusableEmpty")

        assert first is not second
        assert first.data is second.data
        assert len(first.data.vertices) == 0

    def test_parent_under_applies_local_transform(self):
        parent = bpy.data.objects.new("Parent", None)
        child = bpy.data.objects.new("Child", None)
        bpy.context.scene.collection.objects.link(parent)
        bpy.context.scene.collection.objects.link(child)

        utils.parent_under(child, parent, Vector((1, 2, 3)), Vector((0.1, 0.2, 0.3)))

        assert child.parent is parent
        assert tuple(child.location) == pytest.approx((1, 2, 3))
        assert tuple(child.rotation_euler) == pytest.approx((0.1, 0.2, 0.3))
        assert child.matrix_parent_inverse == Matrix.Identity(4)

    def test_link_parent_preserves_world_transform_with_rotated_scaled_parent(self):
        parent = bpy.data.objects.new("Parent", None)
        child = bpy.data.objects.new("Child", None)
        bpy.context.collection.objects.link(parent)
        bpy.context.collection.objects.link(child)
        parent.location = (2.0, -1.0, 3.0)
        parent.rotation_euler = (0.4, -0.3, 0.7)
        parent.scale = (2.0, 0.5, 1.5)
        child.location = (-4.0, 5.0, 6.0)
        child.rotation_euler = (-0.2, 0.8, 0.1)
        expected = child.matrix_world.copy()

        function.link_parent(bpy.context, child, parent)

        assert child.parent is parent
        assert child.matrix_parent_inverse == Matrix.Identity(4)
        for row in range(4):
            assert tuple(child.matrix_world[row]) == pytest.approx(tuple(expected[row]))

    def test_link_gizmo_matrix_falls_back_without_3d_region(self):
        from Forge.gizmo.gizmo import _link_matrix

        obj = bpy.data.objects.new("Link", None)
        bpy.context.collection.objects.link(obj)
        obj.location = (1.0, 2.0, 3.0)

        result = _link_matrix(obj, SimpleNamespace(region_data=None))

        assert result == obj.matrix_world.normalized()

    def test_unique_name_normalizes_blender_suffix(self):
        existing = bpy.data.objects.new("Part", None)
        candidate = bpy.data.objects.new("Candidate", None)

        assert utils.get_unique_object_name(candidate, "Part") == "Part_001"
        assert utils.get_unique_object_name(candidate, "Wheel.003") == "Wheel_003"
        assert utils.get_unique_object_name(existing, "Part") == "Part"

    def test_get_collection_creates_and_reuses_child(self):
        parent = bpy.data.collections.new("ParentCollection")
        bpy.context.scene.collection.children.link(parent)

        created = utils.get_collection(bpy.context, "ChildCollection", parent)

        assert created in parent.children.values()
        assert utils.get_collection(bpy.context, "ChildCollection") is created

    def test_bound_center_and_dimension_axis(self):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object

        assert tuple(utils.get_bound_center(obj)) == pytest.approx((0, 0, 0))
        assert tuple(utils.get_max_dimension_axis(obj, Vector((4, 2, 1)))) == pytest.approx(
            (0, pytest.approx(1.5707963268), 0)
        )
        assert tuple(utils.get_max_dimension_axis(obj, Vector((1, 2, 4)))) == pytest.approx((0, 0, 0))

    @pytest.mark.parametrize(
        ("dims", "largest", "smallest"),
        [
            ((4, 2, 1), 0, 2),
            ((1, 4, 2), 1, 0),
            ((2, 1, 4), 2, 1),
            ((2, 2, 6), 2, 0),
            ((6, 6, 2), 0, 2),
            ((2, 2, 2), 0, 0),
        ],
    )
    def test_height_axis_index_follows_the_height_mode(self, dims, largest, smallest):
        """`min_is_height` flips which axis becomes the shape's local Z; a tie
        resolves to the lowest index in either mode."""
        dims = Vector(dims)

        assert utils.get_height_axis_index(dims) == largest
        assert utils.get_height_axis_index(dims, min_is_height=True) == smallest

    def test_max_dimension_axis_honours_min_is_height(self):
        obj = bpy.data.objects.new("Axis", None)

        assert tuple(utils.get_max_dimension_axis(obj, Vector((4, 2, 1)))) == pytest.approx(
            (0, pytest.approx(1.5707963268), 0)
        )
        # (4, 2, 1) is smallest on Z, so a min-height shape needs no rotation.
        assert tuple(utils.get_max_dimension_axis(obj, Vector((4, 2, 1)), True)) == pytest.approx((0, 0, 0))
        assert tuple(utils.get_max_dimension_axis(obj, Vector((1, 4, 2)), True)) == pytest.approx(
            (0, pytest.approx(1.5707963268), 0)
        )
        assert tuple(utils.get_max_dimension_axis(obj, Vector((2, 1, 4)), True)) == pytest.approx(
            (pytest.approx(-1.5707963268), 0, 0)
        )
        # A tie resolves to X (index 0) in both modes.
        assert tuple(utils.get_max_dimension_axis(obj, Vector((2, 2, 6)), True)) == pytest.approx(
            (0, pytest.approx(1.5707963268), 0)
        )

    def test_max_dimension_axis_leaves_equal_dimensions_alone(self):
        """Equal dimensions must not twist the shape. A LINK/FRAME parent is an
        Empty reporting (0, 0, 0), which used to rotate an auto-sized capsule
        90 degrees about Y for no reason."""
        obj = bpy.data.objects.new("Axis", None)

        assert tuple(utils.get_max_dimension_axis(obj, Vector((2, 2, 2)))) == (0, 0, 0)
        assert tuple(utils.get_max_dimension_axis(obj, Vector((2, 2, 2)), True)) == (0, 0, 0)
        assert tuple(utils.get_max_dimension_axis(obj, Vector((0, 0, 0)))) == (0, 0, 0)

    def test_matrix_by_dimension_axis_local_swaps_to_the_height_axis(self):
        obj = bpy.data.objects.new("Axis", None)

        largest = utils.get_matrix_by_dimension_axis_local(obj, Vector((4, 2, 1)))
        assert tuple(largest.col[0]) == pytest.approx((0, 0, -1, 0))
        assert tuple(largest.col[1]) == pytest.approx((0, 1, 0, 0))
        assert tuple(largest.col[2]) == pytest.approx((1, 0, 0, 0))
        assert largest.determinant() == pytest.approx(1.0)

        # Nothing to swap when Z is already the height axis, or when every axis
        # measures the same.
        assert utils.get_matrix_by_dimension_axis_local(obj, Vector((4, 2, 1)), True) == obj.matrix_local
        assert utils.get_matrix_by_dimension_axis_local(obj, Vector((2, 2, 2))) == obj.matrix_local

    @pytest.mark.parametrize(
        ("dims", "min_is_height"),
        [((4, 2, 1), False), ((4, 2, 1), True), ((1, 4, 2), False), ((1, 4, 2), True), ((2, 1, 4), True)],
    )
    def test_matrix_axis_and_euler_table_agree(self, dims, min_is_height):
        """The column swap and the `get_max_dimension_axis` table describe the
        same rotation. If they disagree the collider is sized along one axis
        but oriented along another — the bug this pins down."""
        obj = bpy.data.objects.new("Axis", None)
        dims = Vector(dims)

        local = utils.get_matrix_by_dimension_axis_local(obj, dims, min_is_height)
        world = function.get_matrix_by_dimension_axis_world(obj, dims, min_is_height)
        euler = Euler(utils.get_max_dimension_axis(obj, dims, min_is_height))

        expected = tuple(euler.to_matrix().col[2])
        # `to_matrix()` leaves float noise where a column entry is exactly zero.
        assert tuple(local.col[2].to_3d()) == pytest.approx(expected, abs=1e-6)
        assert tuple(world.col[2].to_3d()) == pytest.approx(expected, abs=1e-6)
        assert local.determinant() == pytest.approx(1.0)
        assert world.determinant() == pytest.approx(1.0)

    def test_bmesh_copy_transforms_and_triangulates(self):
        bpy.ops.mesh.primitive_cube_add(location=(3, 0, 0))
        obj = bpy.context.active_object

        mesh = utils.bmesh_copy_from_object(obj, transform=True, triangulate=True)
        try:
            assert len(mesh.faces) == 12
            assert min(vertex.co.x for vertex in mesh.verts) == pytest.approx(2.0)
        finally:
            mesh.free()


class TestColliderAlignment:
    """A CAPSULE/CYLINDER collider must orient along the same axis it measured."""

    @staticmethod
    def _asymmetric_visual():
        """A cube stretched to dims (1, 4, 2) through mesh data, so object scale --
        and therefore the matrix the collider copies -- stays identity."""
        bpy.ops.mesh.primitive_cube_add()
        visual = bpy.context.active_object
        visual.Forge_Model_Type = cons.ModelTypes.VISUAL
        visual.data.transform(Matrix.Diagonal((0.5, 2.0, 1.0, 1.0)))
        bpy.context.view_layer.update()
        return visual

    @pytest.mark.parametrize(
        ("min_is_height", "radius", "height", "z_axis", "euler"),
        [
            (False, 0.5, 4.0, (0.0, 1.0, 0.0), (-1.5707963, 0.0, 0.0)),
            (True, 2.0, 1.0, (1.0, 0.0, 0.0), (0.0, 1.5707963, 0.0)),
        ],
    )
    def test_cylinder_measures_and_orients_on_the_same_axis(
        self, registered_props, min_is_height, radius, height, z_axis, euler
    ):
        visual = self._asymmetric_visual()
        assert tuple(visual.dimensions) == pytest.approx((1.0, 4.0, 2.0))

        with headless_shape_modifiers():
            collider = function.add_collider(
                bpy.context,
                collector([]),
                bpy.context.collection,
                cons.GeometryTypes.CYLINDER,
                visual,
                True,
                None,
                min_is_height,
            )

        sockets = cons.ModifierSockets.Collider
        modifier = collider.modifiers[cons.ColliderShapeModifiers[cons.GeometryTypes.CYLINDER]]
        assert common.get_modifier_socket(modifier, sockets.SIZE) == pytest.approx(radius)
        assert common.get_modifier_socket(modifier, sockets.HEIGHT) == pytest.approx(height)
        # `matrix_local` is depsgraph-cached: the assignment inside add_collider
        # lands in matrix_basis immediately, but reading the matrix back needs an
        # update. `rotation_euler` would have been readable either way.
        bpy.context.view_layer.update()
        # Local Z lands on the measured axis -- max (Y) by default, min (X) when
        # the flag is set -- rather than staying put and leaving the shape askew.
        # abs=1e-6: Blender stores rotation as float32, so a column entry that
        # should be exactly zero comes back as ~1e-7.
        assert tuple(collider.matrix_local.col[2].to_3d()) == pytest.approx(z_axis, abs=1e-6)
        assert tuple(collider.matrix_local.to_euler()) == pytest.approx(euler, abs=1e-6)


class TestSerializationBranches:
    def test_vector_scaling_and_rotation(self):
        assert ser.parse_vector_array_to_xml((1, 2, 3), scale=0.5, usescale=True) == "0.5 1.0 1.5"
        assert ser.parse_vector_array_to_xml((0.1,), scale=3.0, usescale=True) == "0.3"
        euler_xml = ser.parse_rotation_euler_to_xml((0, 1.5707963267948966, 3.141592653589793))
        assert [float(v) for v in euler_xml.split()] == pytest.approx((0, 90, 180), abs=1e-5)

    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            (-4.3711e-08, -0.0),  # small physical values are retained by default
            (1.19e-07, 0.0000001),
            (-0.0, 0.0),
            (0.0, 0.0),
            (1.0, 1.0),
            (0.12345671, 0.1234567),
        ],
    )
    def test_round_float_preserves_small_values_by_default(self, value, expected):
        assert ser.round_float(value) == expected

    def test_round_float_can_snap_derived_noise(self):
        assert ser.round_float(1.19e-7, zero_tolerance=1e-6) == 0.0
        assert ser.parse_vector_array_to_xml((1.19e-7, 1.0), zero_tolerance=1e-6) == "0.0 1.0"

    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            ("HINGE", "hinge"),
            ((1, 2.5), "1 2.5"),
            (Vector((1, 2, 3)), "1.0 2.0 3.0"),
            (object(), ""),
        ],
    )
    def test_parse_value_types(self, value, expected):
        assert ser.parse_value_by_attr(value) == expected

    @pytest.mark.parametrize(
        ("value", "precision", "expected"),
        [
            (1.23456789, 3, "1.235"),
            (1.23456789, 8, "1.23456789"),
            (1.75, 0, "2.0"),
            (123.45, -1, "120.0"),
            ([1.23456, 2.34567], 3, "1.235 2.346"),
            ((1.23456, 2.34567), 3, "1.235 2.346"),
            (Vector((1.23456, 2.34567)), 3, "1.235 2.346"),
            (Euler((1.23456, 2.34567, 3.45678)), 3, "1.235 2.346 3.457"),
            (42, 0, "42"),
            (True, 0, "true"),
        ],
    )
    def test_parse_value_precision(self, value, precision, expected):
        assert ser.parse_value_by_attr(value, precision=precision) == expected

    def test_vector_precision_after_scaling(self):
        assert ser.parse_vector_array_to_xml((1.23456,), scale=2, usescale=True, precision=3) == "2.469"

    def test_blender_array_precision(self, registered_props):
        obj = bpy.data.objects.new("Precision", None)
        obj.location = (1.23456, 2.34567, 3.45678)
        assert ser.parse_value_by_attr(obj.location, precision=3) == "1.235 2.346 3.457"
        obj.Forge_Geometry.friction = (1.23456, 2.34567, 3.45678)
        assert ser.parse_value_by_attr(obj.Forge_Geometry.friction, precision=3) == "1.235 2.346 3.457"
        assert ser.parse_value_by_attr(1.23456789) == "1.2345679"

    @pytest.mark.parametrize(
        ("current", "text", "expected"),
        [
            (False, "enable", True),
            (1.0, "2.5", 2.5),
            (1, "7", 7),
            ("hinge", "slide", "SLIDE"),
            (Vector((0, 0, 0)), "1 2 3", [1.0, 2.0, 3.0]),
        ],
    )
    def test_parse_attr_types(self, current, text, expected):
        item = SimpleNamespace(value=current)
        assert ser.parse_attr_from_xml(item, "value", {"value": text}) == expected

    def test_set_vector_property_from_xml(self):
        item = SimpleNamespace(value=Vector((0, 0, 0)))

        ser.set_props_from_xml(item, "value", {"value": "1 2 3"})

        assert tuple(item.value) == pytest.approx((1, 2, 3))

    def test_rna_string_preserves_case_and_short_array_resets_tail(self, registered_props):
        props = bpy.context.scene.Forge_Props
        props.import_file_path = "C:/Models/MyRobot.XML"
        assert ser.parse_prop_by_type(props, "import_file_path") == "C:/Models/MyRobot.XML"

        bpy.ops.mesh.primitive_cube_add()
        geom = bpy.context.active_object.Forge_Geometry
        geom.solref = (9.0, 9.0)
        ser.set_props_from_xml(geom, "solref", {"solref": "3"})
        assert tuple(geom.solref) == pytest.approx((3.0, 1.0))

    def test_scene_data_defaults_are_not_shared(self):
        first = utils.Scene_Data()
        second = utils.Scene_Data()
        first.data.append("value")

        assert second.data == []

    def test_plane_gizmo_fallback_uses_half_dimensions(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.name = "Plane"
        obj.Forge_Model_Type = cons.ModelTypes.PLANE
        obj.dimensions = (4.0, 6.0, 0.0)
        bpy.context.view_layer.update()

        assert function.get_gizmo_offset(obj) == pytest.approx((2.0, 3.0, 0.0))

    def test_zero_scale_normalized_matrix_is_finite(self):
        from Forge.gizmo.gizmo_factory import normalized_object_matrix

        obj = bpy.data.objects.new("ZeroScale", None)
        bpy.context.collection.objects.link(obj)
        obj.location = (1.0, 2.0, 3.0)
        obj.scale = (0.0, 0.0, 0.0)
        bpy.context.view_layer.update()

        matrix = normalized_object_matrix(obj)

        assert all(value == value for row in matrix for value in row)
        assert tuple(matrix.translation) == pytest.approx((1.0, 2.0, 3.0))

    def test_fix_object_name_updates_mesh_name(self):
        mesh = bpy.data.meshes.new("Mesh.001")
        obj = bpy.data.objects.new("Object.001", mesh)

        ser.fix_object_name(obj)

        assert "." not in obj.name
        assert "." not in mesh.name


class TestGeometryHandlerBranches:
    @pytest.mark.parametrize(
        ("shape", "expected_size", "expected_offset", "expected_dimensions"),
        [
            ("BOX", (1, 2, 3), [1, 2, 3], (2, 4, 6)),
            ("CAPSULE", (2, 3), [2, 2, 5], (4, 4, 10)),
            ("CYLINDER", (2, 3), [2, 2, 3], (4, 4, 6)),
            ("SPHERE", 2, [2, 2, 2], (4, 4, 4)),
        ],
    )
    def test_read_shape_sockets(self, shape, expected_size, expected_offset, expected_dimensions):
        sockets = cons.ModifierSockets.Visual
        modifier = {sockets.SIZE: (2, 4, 6) if shape == "BOX" else 2, sockets.HEIGHT: 6}
        handler = GeometryHandler.for_visual(shape)

        size = handler.get_size(modifier)
        if isinstance(expected_size, tuple):
            assert tuple(size) == pytest.approx(expected_size)
        else:
            assert size == pytest.approx(expected_size)
        assert handler.get_gizmo_offset(modifier) == pytest.approx(expected_offset)
        assert tuple(handler.get_dimensions(modifier)) == pytest.approx(expected_dimensions)

    @pytest.mark.parametrize(
        ("shape", "dimensions", "radius", "height"),
        [
            ("CAPSULE", Vector((2, 2, 6)), 1, 4),
            ("CYLINDER", Vector((2, 2, 6)), 1, 6),
        ],
    )
    def test_set_round_shape_from_dimensions(self, shape, dimensions, radius, height):
        sockets = cons.ModifierSockets.Visual
        modifier = {}

        GeometryHandler.for_visual(shape).set_size(modifier, dimensions)

        assert common.get_modifier_socket(modifier, sockets.SIZE) == pytest.approx(radius)
        assert common.get_modifier_socket(modifier, sockets.HEIGHT) == pytest.approx(height)

    def test_unknown_shape_has_safe_defaults(self):
        handler = GeometryHandler("UNKNOWN", cons.ModifierSockets.Visual)

        assert tuple(handler.get_size({})) == (0, 0, 0)
        assert handler.get_gizmo_offset({}) == [0, 0, 0]
        assert tuple(handler.get_dimensions({})) == (0, 0, 0)
        assert handler.modifier_name({"BOX": "Box"}) is None
