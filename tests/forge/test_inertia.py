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

"""Tests for Forge's mass-property and inertia tensor implementation."""

from types import SimpleNamespace

import numpy as np
import pytest
from Forge.ops import inertia
from mathutils import Matrix, Quaternion, Vector


def _rows(matrix):
    return [[float(matrix[row][column]) for column in range(3)] for row in range(3)]


def test_inertial_draw_reuses_shader_and_unit_box(monkeypatch):
    import gpu
    from Forge.core import inertial
    from gpu_extras import batch

    shaders = []
    batches = []

    def make_shader(name):
        shader = object()
        shaders.append(shader)
        return shader

    def make_batch(shader, mode, vertices, indices):
        result = object()
        batches.append(result)
        return result

    monkeypatch.setattr(gpu.shader, "from_builtin", make_shader)
    monkeypatch.setattr(batch, "batch_for_shader", make_batch)
    inertial._clear_draw_resources()
    try:
        first = inertial._get_draw_resources()
        for _ in range(100):
            assert inertial._get_draw_resources() is first
        assert len(shaders) == 1
        assert len(batches) == 2
    finally:
        inertial._clear_draw_resources()


def test_inertial_sync_ignores_unrelated_changes(registered_props, monkeypatch):
    import bpy
    from Forge.core import function as funcs
    from Forge.core import inertial

    parent = bpy.data.objects.new("PreviewLink", None)
    bpy.context.scene.collection.objects.link(parent)
    parent.Forge_Model_Type = "LINK"
    obj = funcs.add_inertial(
        bpy.context,
        lambda *_: None,
        bpy.context.scene.collection,
        parent,
        (Vector((1, 2, 3)), Matrix.Identity(3).to_quaternion(), 3.0, Vector((13, 10, 5))),
    )
    bpy.ops.mesh.primitive_cube_add()
    unrelated = bpy.context.object
    bpy.context.view_layer.update()
    updates = []
    update_display = inertial.update_empty_display

    def record_update(target):
        updates.append(target)
        update_display(target)

    monkeypatch.setattr(inertial, "update_empty_display", record_update)
    bpy.app.handlers.depsgraph_update_post.append(inertial._sync_empty_displays)
    try:
        unrelated.location.x = 5
        bpy.context.view_layer.update()
        assert updates == []

        parent.scale = (2, 3, 4)
        bpy.context.view_layer.update()
        assert obj in updates
        np.testing.assert_allclose(np.asarray(obj.matrix_world), np.asarray(inertial.preview_matrix(obj)), atol=1e-5)
    finally:
        bpy.app.handlers.depsgraph_update_post.remove(inertial._sync_empty_displays)


class TestMatrixHelpers:
    def test_numpy_matrix_roundtrip(self):
        source = np.array(((1, 2, 3), (4, 5, 6), (7, 8, 9)), dtype=np.float64)

        result = inertia.matrix_to_numpy(inertia.matrix_from_numpy(source))

        assert np.array_equal(result, source)

    def test_outer_product_and_scale(self):
        outer = inertia.matrix_outer(Vector((1, 2, 3)), Vector((4, 5, 6)))

        assert _rows(outer) == [[4, 5, 6], [8, 10, 12], [12, 15, 18]]
        assert _rows(inertia.matrix_scale(outer, 0.5)) == [[2, 2.5, 3], [4, 5, 6], [6, 7.5, 9]]

    def test_parallel_axis_shift(self):
        shifted = inertia.inertia_shift(2.0, Vector((3, 0, 0)))

        np.testing.assert_allclose(_rows(shifted), [[0, 0, 0], [0, 18, 0], [0, 0, 18]])

    def test_normalized_zero_vector_uses_world_up(self):
        assert tuple(inertia.normalized(Vector())) == (0, 0, 1)

    def test_stable_axes_are_right_handed_and_orthonormal(self):
        axes = inertia.stable_axes_from_z(Vector((0, 0, 1)))

        assert axes.determinant() == pytest.approx(1.0)
        np.testing.assert_allclose(_rows(axes.transposed() @ axes), _rows(Matrix.Identity(3)))

    def test_stable_axes_for_non_axis_aligned_vector(self):
        axes = inertia.stable_axes_from_z(Vector((1, 2, 3)))

        assert axes.determinant() == pytest.approx(1.0)
        np.testing.assert_allclose(_rows(axes.transposed() @ axes), _rows(Matrix.Identity(3)), atol=1e-6)

    @pytest.mark.parametrize("noise", [(1.3e-8, 7.4e-9, 1), (-2e-8, 4e-8, 1)])
    def test_stable_axes_near_world_z_do_not_amplify_noise(self, noise):
        axes = inertia.stable_axes_from_z(Vector(noise))
        np.testing.assert_allclose(_rows(axes), _rows(Matrix.Identity(3)), atol=1e-6)


class TestMassProperties:
    @pytest.mark.parametrize("part_count", [1, 2])
    def test_full_tensor_reaches_created_inertial_in_link_axes(self, registered_props, monkeypatch, part_count):
        import bpy
        from Forge.core import function as funcs

        parent = bpy.data.objects.new("TensorLink", None)
        bpy.context.scene.collection.objects.link(parent)
        parent.Forge_Model_Type = "LINK"
        parent.matrix_world = Matrix.Translation((3, 4, 5)) @ Matrix.Rotation(0.7, 4, "X")
        bpy.context.view_layer.update()
        parts = [
            SimpleNamespace(
                name=f"Part{index}",
                type="EMPTY",
                Forge_Geometry=SimpleNamespace(type="BOX", density=2.0),
                matrix_world=Matrix.Translation((index * 2, 1, 3)) @ Matrix.Rotation(0.4, 4, "Y"),
            )
            for index in range(part_count)
        ]
        monkeypatch.setattr(inertia, "get_size", lambda _: (1, 2, 3))
        computed = inertia.compute_inertia(None, lambda *_: None, parts)
        assert len(computed) == 5
        world_tensor = np.asarray(computed[4])
        frame = np.asarray(computed[1].to_matrix())
        np.testing.assert_allclose(frame @ np.diag(computed[3]) @ frame.T, world_tensor, atol=1e-4)

        obj = funcs.add_inertial(bpy.context, lambda *_: None, bpy.context.scene.collection, parent, computed)
        xx, yy, zz, xy, xz, yz = obj.Forge_Inertial.fullinertia
        stored = np.array(((xx, xy, xz), (xy, yy, yz), (xz, yz, zz)))
        body_axes = np.asarray(parent.matrix_world.to_quaternion().to_matrix())
        np.testing.assert_allclose(stored, body_axes.T @ world_tensor @ body_axes, atol=1e-4)
        assert np.any(np.abs(stored - np.diag(np.diag(stored))) > 1.0)

    @pytest.mark.parametrize("use_diagonal", [True, False])
    def test_export_uses_one_inertia_representation(self, use_diagonal):
        import xml.etree.ElementTree as ET

        from Forge.ops import exports

        obj = SimpleNamespace(
            matrix_local=Matrix.Rotation(0.4, 4, "Y"),
            matrix_basis=Matrix.Rotation(0.4, 4, "Y"),
            matrix_parent_inverse=Matrix.Identity(4),
            Forge_Inertial=SimpleNamespace(
                mass=3.0,
                diaginertia=(5, 6, 7) if use_diagonal else (0, 0, 0),
                fullinertia=(5.3, 6.0, 6.7, 0.0, 0.7, 0.0),
            ),
        )
        root = ET.Element("body")
        exports.set_inertial_tags(root, obj)
        attrs = root.find("inertial").attrib
        assert ("diaginertia" in attrs) == use_diagonal
        assert ("quat" in attrs) == use_diagonal
        assert ("fullinertia" in attrs) != use_diagonal

    def test_axisymmetric_preview_follows_object_reference_axes(self, monkeypatch):
        rotation = Matrix.Rotation(0.8, 4, "Z") @ Matrix.Rotation(0.4, 4, "Y")
        obj = SimpleNamespace(
            name="Symmetric",
            type="EMPTY",
            matrix_world=rotation,
            Forge_Geometry=SimpleNamespace(type="CYLINDER", density=1.0),
        )
        monkeypatch.setattr(inertia, "get_size", lambda _: (0.5, 1.0))
        props = inertia.process_object(None, lambda *_: None, obj)["props"]
        np.testing.assert_allclose(_rows(props["inertial_frame_axes"]), _rows(rotation.to_3x3()), atol=1e-6)
        axes = np.asarray(props["inertial_frame_quat_world"].to_matrix())
        reconstructed = axes @ np.diag(props["inertial_frame_diaginertia"]) @ axes.T
        np.testing.assert_allclose(reconstructed, _rows(props["inertia_com"]), atol=1e-6)

    def test_small_anisotropic_inertia_preserves_eigenvectors(self):
        rotation = Matrix.Rotation(0.6, 3, "X")
        tensor = rotation @ Matrix.Diagonal((1e-8, 2e-8, 2.5e-8)) @ rotation.transposed()
        moments, _, frame_moments, frame_axes, degenerate = inertia.principal_axis_properties(lambda *_: None, tensor)
        assert not degenerate
        assert not inertia.has_three_equal_moments(moments)
        axes = np.asarray(frame_axes)
        np.testing.assert_allclose(axes @ np.diag(frame_moments) @ axes.T, _rows(tensor), atol=1e-14)

    def test_inertial_preview_preserves_world_axes_and_size(self, registered_props):
        import bpy
        from Forge.core import function as funcs
        from Forge.core.inertial import _sync_empty_displays, local_frame, preview_matrix

        parent = bpy.data.objects.new("Link", None)
        bpy.context.scene.collection.objects.link(parent)
        parent.Forge_Model_Type = "LINK"
        parent.matrix_world = (
            Matrix.Translation((3, 4, 5)) @ Matrix.Rotation(0.7, 4, "X") @ Matrix.Diagonal((2, 3, 4, 1))
        )
        rotation = Matrix.Rotation(0.4, 3, "Y").to_quaternion()
        com = Vector((1, 2, 3))
        bpy.context.scene.Forge_Props.gizmo_scale = 3.0
        # Uniform box of half-extents (1, 2, 3), mass 3.
        obj = funcs.add_inertial(
            bpy.context,
            lambda *_: None,
            bpy.context.scene.collection,
            parent,
            (com, rotation, 3.0, Vector((13, 10, 5))),
        )
        bpy.context.view_layer.update()
        expected = Matrix.LocRotScale(com, rotation, Vector((1, 2, 3)))
        displayed = preview_matrix(obj)
        np.testing.assert_allclose(np.asarray(displayed), np.asarray(expected), atol=1e-5)
        assert obj.empty_display_type == "CUBE"
        assert obj.empty_display_size == pytest.approx(1.0)
        assert tuple(obj.scale) == pytest.approx((1, 2, 3))
        np.testing.assert_allclose(np.asarray(obj.matrix_world), np.asarray(expected), atol=1e-5)

        obj.Forge_Inertial.mass = 12.0
        bpy.context.view_layer.update()
        displayed = preview_matrix(obj)
        expected = Matrix.LocRotScale(com, rotation, Vector((0.5, 1, 1.5)))
        np.testing.assert_allclose(np.asarray(displayed), np.asarray(expected), atol=1e-5)

        assert tuple(obj.scale) == pytest.approx((0.5, 1, 1.5))
        np.testing.assert_allclose(np.asarray(obj.matrix_world), np.asarray(expected), atol=1e-5)
        # Editing the physical frame remains link-local after preview sizing.
        obj.location = (1, 0, 0)
        obj.rotation_euler = (0, 0, 0.6)
        _sync_empty_displays(bpy.context.scene, None)
        bpy.context.view_layer.update()
        np.testing.assert_allclose(obj.matrix_world.translation, parent.matrix_world @ Vector((1, 0, 0)), atol=1e-6)
        expected_local = Matrix.Rotation(0.6, 3, "Z")
        np.testing.assert_allclose(_rows(local_frame(obj).to_3x3()), _rows(expected_local), atol=1e-6)
        np.testing.assert_allclose(np.asarray(obj.matrix_world), np.asarray(preview_matrix(obj)), atol=1e-5)

        parent.scale = (4, 2, 3)
        parent.rotation_euler = (0.2, 0.4, 0.1)
        bpy.context.view_layer.update()
        _sync_empty_displays(bpy.context.scene, None)
        bpy.context.view_layer.update()
        np.testing.assert_allclose(np.asarray(obj.matrix_world), np.asarray(preview_matrix(obj)), atol=1e-5)

    def test_full_tensor_edits_update_principal_frame_and_export(self, registered_props):
        import xml.etree.ElementTree as ET

        import bpy
        from Forge.core import function as funcs
        from Forge.core.inertial import full_tensor, preview_matrix
        from Forge.ops import exports

        obj = funcs.add_inertial(
            bpy.context,
            lambda *_: None,
            bpy.context.scene.collection,
            inertia_data=(Vector((1, 2, 3)), Matrix.Identity(3).to_quaternion(), 3.0, Vector((13, 10, 5))),
        )
        obj.Forge_Inertial.fullinertia = (10, 13, 5, 0, 0, 0)
        np.testing.assert_allclose(_rows(full_tensor(obj)), np.diag((10, 13, 5)), atol=1e-5)
        assert tuple(obj.location) == pytest.approx((1, 2, 3))
        assert preview_matrix(obj) is not None
        root = ET.Element("body")
        exports.set_inertial_tags(root, obj)
        attrs = root.find("inertial").attrib
        axes = np.asarray(Quaternion(tuple(map(float, attrs["quat"].split()))).to_matrix())
        diagonal = tuple(map(float, attrs["diaginertia"].split()))
        np.testing.assert_allclose(axes @ np.diag(diagonal) @ axes.T, np.diag((10, 13, 5)), atol=1e-4)

        # Readback is derived, so edits to either diagonal inertia or pose
        # cannot leave a previously stored full tensor behind.
        obj.Forge_Inertial.diaginertia = (9, 8, 7)
        obj.rotation_euler = (0.4, 0.2, 0.6)
        xx, yy, zz, xy, xz, yz = obj.Forge_Inertial.fullinertia
        stored = ((xx, xy, xz), (xy, yy, yz), (xz, yz, zz))
        axes = np.asarray(obj.rotation_euler.to_matrix())
        np.testing.assert_allclose(stored, axes @ np.diag((9, 8, 7)) @ axes.T, atol=1e-5)

    @pytest.mark.parametrize("orientation", [{"quat": "0.9238795 0 0 0.3826834"}, {"axisangle": "0 0 1 45"}])
    def test_import_box_matches_preview_under_scaled_parent(self, registered_props, orientation):
        import bpy
        from Forge.core.inertial import _sync_empty_displays, local_frame, preview_matrix
        from Forge.ops import imports

        parent = bpy.data.objects.new("ScaledLink", None)
        bpy.context.scene.collection.objects.link(parent)
        parent.Forge_Model_Type = "LINK"
        parent.scale = (2, 3, 4)
        bpy.context.view_layer.update()
        imports.add_inertial(
            bpy.context,
            lambda *_: None,
            bpy.context.scene.collection,
            {"mass": "3", "pos": "1 2 3", "diaginertia": "13 10 5", **orientation},
            parent,
        )
        obj = bpy.context.active_object
        bpy.context.view_layer.update()
        np.testing.assert_allclose(_rows(local_frame(obj)), _rows(Matrix.Rotation(np.pi / 4, 3, "Z")), atol=1e-5)
        np.testing.assert_allclose(np.asarray(obj.matrix_world), np.asarray(preview_matrix(obj)), atol=1e-5)

        bpy.app.handlers.depsgraph_update_post.append(_sync_empty_displays)
        try:
            parent.scale = (4, 2, 3)
            obj.location = (3, 2, 1)
            bpy.context.view_layer.update()
            np.testing.assert_allclose(np.asarray(obj.matrix_world), np.asarray(preview_matrix(obj)), atol=1e-5)
        finally:
            bpy.app.handlers.depsgraph_update_post.remove(_sync_empty_displays)

    def test_import_full_tensor_initializes_principal_preview(self, registered_props):
        import bpy
        from Forge.core.inertial import preview_matrix
        from Forge.ops import imports

        imports.add_inertial(
            bpy.context,
            lambda *_: None,
            bpy.context.scene.collection,
            {"mass": "3", "pos": "1 2 3", "fullinertia": "10 13 5 1 0.5 0.25"},
        )
        obj = bpy.context.active_object
        assert tuple(obj.location) == pytest.approx((1, 2, 3))
        assert tuple(obj.Forge_Inertial.fullinertia) == pytest.approx((10, 13, 5, 1, 0.5, 0.25), abs=1e-5)
        assert all(value > 0 for value in obj.Forge_Inertial.diaginertia)
        assert preview_matrix(obj) is not None

    @pytest.mark.parametrize(
        "shape,size,volume,diagonal",
        [
            ("BOX", (1, 2, 3), 48.0, (208, 160, 80)),
            ("SPHERE", 2.0, 32 * np.pi / 3, (256 * np.pi / 15,) * 3),
            ("CYLINDER", (2, 3), 24 * np.pi, (96 * np.pi, 96 * np.pi, 48 * np.pi)),
            ("CAPSULE", (2, 3), 104 * np.pi / 3, (3856 * np.pi / 15, 3856 * np.pi / 15, 976 * np.pi / 15)),
            ("CAPSULE", (2, 0), 32 * np.pi / 3, (256 * np.pi / 15,) * 3),
        ],
    )
    def test_shapes_use_parameters_without_mesh(self, monkeypatch, shape, size, volume, diagonal):
        obj = SimpleNamespace(
            name="Shape",
            type="EMPTY",
            Forge_Geometry=SimpleNamespace(type=shape, density=1.0),
            matrix_world=Matrix.Identity(4),
        )
        monkeypatch.setattr(inertia, "get_size", lambda _: size)
        monkeypatch.setattr(inertia, "tetgen", None)

        def reject_mesh(*_):
            pytest.fail("Primitive shapes must not use mesh computation")

        monkeypatch.setattr(inertia, "evaluated_triangle_mesh", reject_mesh)
        monkeypatch.setattr(inertia, "set_collider_to_mesh", reject_mesh)
        result = inertia.process_object(None, reject_mesh, obj)

        assert result["props"]["volume"] == pytest.approx(volume)
        assert result["props"]["mass"] == pytest.approx(volume)
        np.testing.assert_allclose(_rows(result["props"]["inertia_com"]), np.diag(diagonal), rtol=1e-6)
        assert result["nodes"].shape == (0, 3)
        assert result["tets"].shape == (0, 4)

    def test_shape_world_transform_and_density(self, monkeypatch):
        transform = Matrix.Translation((4, 5, 6)) @ Matrix.Rotation(np.pi / 2, 4, "Z") @ Matrix.Diagonal((-2, 3, 4, 1))
        obj = SimpleNamespace(name="Scaled", Forge_Geometry=SimpleNamespace(type="SPHERE"), matrix_world=transform)
        monkeypatch.setattr(inertia, "get_size", lambda _: 1.0)

        props = inertia.compute_shape_mass_properties(lambda *_: None, obj, 2.0)

        mass = 64 * np.pi
        assert props["mass"] == pytest.approx(mass)
        assert tuple(props["com"]) == pytest.approx((4, 5, 6))
        expected = np.diag(np.array((20, 25, 13)) * mass / 5)
        np.testing.assert_allclose(_rows(props["inertia_com"]), expected, atol=1e-4)
        np.testing.assert_allclose(
            _rows(props["inertia_origin"]),
            expected + np.asarray(inertia.inertia_shift(mass, props["com"])),
            rtol=1e-6,
        )

    @pytest.mark.parametrize("geometry_type", ["MESH", "SDF"])
    def test_process_object_uses_material_density(self, registered_props, monkeypatch, geometry_type):
        import bpy

        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Geometry.type = geometry_type
        material = bpy.data.materials.new("Dense")
        material["density"] = 2700.0
        obj.data.materials.append(material)
        captured = []
        monkeypatch.setattr(inertia, "evaluated_triangle_mesh", lambda *_: (np.zeros((3, 3)), np.zeros((1, 3))))
        monkeypatch.setattr(inertia, "tetrahedralize", lambda *_: (np.zeros((4, 3)), np.zeros((1, 4))))
        monkeypatch.setattr(
            inertia,
            "compute_mass_properties",
            lambda _context, _report, _nodes, _tets, density: captured.append(density) or {},
        )
        monkeypatch.setattr(inertia, "prefer_object_rotation_for_spherical_inertia", lambda *_: None)

        assert inertia.process_object(None, lambda *_: None, obj) is not None
        assert captured == [2700.0]

    def test_compute_inertia_rejects_empty_selection(self):
        reports = []

        result = inertia.compute_inertia(None, lambda level, message: reports.append((level, message)), [])

        assert result is None
        assert reports == [({"ERROR"}, "No visual meshes selected for inertia computation")]

    @pytest.fixture
    def unit_tetrahedron(self):
        nodes = np.array(((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)), dtype=np.float64)
        tets = np.array(((0, 1, 2, 3),), dtype=np.int32)
        return nodes, tets

    def test_tetrahedron_volume(self, unit_tetrahedron):
        nodes, tets = unit_tetrahedron
        points = inertia.tetra_points(nodes, tets[0])

        assert inertia.tetra_volume(*points) == pytest.approx(1 / 6)

    def test_compute_unit_tetrahedron(self, unit_tetrahedron):
        nodes, tets = unit_tetrahedron
        reports = []

        props = inertia.compute_mass_properties(
            None, lambda level, message: reports.append((level, message)), nodes, tets, 6.0
        )

        assert reports == []
        assert props["volume"] == pytest.approx(1 / 6)
        assert props["mass"] == pytest.approx(1.0)
        assert tuple(props["com"]) == pytest.approx((0.25, 0.25, 0.25))
        assert all(moment > 0 for moment in props["principal_moments"])
        assert props["inertial_frame_axes"].determinant() == pytest.approx(1.0)

    def test_zero_volume_reports_error(self):
        nodes = np.zeros((4, 3), dtype=np.float64)
        tets = np.array(((0, 1, 2, 3),), dtype=np.int32)
        reports = []

        result = inertia.compute_mass_properties(
            None, lambda level, message: reports.append((level, message)), nodes, tets, 1.0
        )

        assert result is None
        assert reports == [({"ERROR"}, "Tetrahedral mesh has zero volume")]

    def test_principal_axes_put_smallest_moment_on_z(self):
        reports = []

        moments, _axes, frame_moments, frame_axes, degenerate = inertia.principal_axis_properties(
            lambda level, message: reports.append((level, message)), Matrix.Diagonal((3, 2, 1))
        )

        assert tuple(moments) == pytest.approx((1, 2, 3))
        assert tuple(frame_moments) == pytest.approx((3, 2, 1))
        assert frame_axes.determinant() == pytest.approx(1.0)
        assert degenerate is False
        assert reports == []

    def test_principal_axes_report_degenerate_moments(self):
        reports = []

        moments, _axes, _frame_moments, _frame_axes, degenerate = inertia.principal_axis_properties(
            lambda level, message: reports.append((level, message)), Matrix.Identity(3)
        )

        assert tuple(moments) == pytest.approx((1, 1, 1))
        assert degenerate is True
        assert reports == []

    def test_combine_uses_parallel_axis_theorem(self):
        parts = [
            {"volume": 1.0, "mass": 1.0, "com": Vector((-1, 0, 0)), "inertia_com": Matrix.Identity(3)},
            {"volume": 1.0, "mass": 1.0, "com": Vector((1, 0, 0)), "inertia_com": Matrix.Identity(3)},
        ]

        result = inertia.combine_mass_properties(None, lambda *_: None, parts)

        assert result["volume"] == pytest.approx(2.0)
        assert result["mass"] == pytest.approx(2.0)
        assert tuple(result["com"]) == pytest.approx((0, 0, 0))
        np.testing.assert_allclose(_rows(result["inertia_com"]), [[2, 0, 0], [0, 4, 0], [0, 0, 4]])

    def test_combine_rejects_zero_mass(self):
        reports = []

        result = inertia.combine_mass_properties(None, lambda level, message: reports.append((level, message)), [])

        assert result is None
        assert reports == [({"ERROR"}, "Combined selection has zero mass")]
