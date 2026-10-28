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

"""Mesh-backed SDF type conversion and MJCF asset roundtrip."""

import xml.etree.ElementTree as ET
from types import SimpleNamespace

import bpy
import pytest
from Forge.core import constants as cons
from Forge.core import function as funcs
from Forge.ops import exports, imports

from .mjcf_helpers import headless_shape_modifiers, run_export


@pytest.mark.parametrize("model_type", ["VISUAL", "COLLIDER"])
def test_mesh_sdf_conversion_preserves_geometry(registered_ops, model_type):
    bpy.ops.mesh.primitive_cube_add()
    obj = bpy.context.object
    obj.Forge_Model_Type = model_type
    obj.Forge_Geometry.type = cons.GeometryTypes.MESH
    mesh = obj.data
    modifier = obj.modifiers.new("Subdivision", "SUBSURF")

    for target in ("SDF", "MESH", "SDF"):
        if model_type == "COLLIDER":
            result = bpy.ops.forge.define_collider_type(collider_type=target)
        else:
            result = bpy.ops.forge.define_geometry_type(geometry_type=target)
        assert result == {"FINISHED"}
        assert obj.Forge_Geometry.type == target
        assert obj.data == mesh
        assert len(obj.data.vertices) == 8
        assert obj.modifiers[0] == modifier
        assert tuple(obj.lock_scale) == (False, False, False)


def test_primitive_sdf_conversion(registered_ops):
    with headless_shape_modifiers():
        bpy.ops.forge.create_geometry(geometry_type="BOX", size_box=(2, 4, 6))
        obj = bpy.context.object
        assert bpy.ops.forge.define_geometry_type(geometry_type="SDF") == {"FINISHED"}
        assert len(obj.data.polygons) == 6
        assert not obj.modifiers
        assert tuple(obj.dimensions) == pytest.approx((2, 4, 6))
        assert bpy.ops.forge.define_geometry_type(geometry_type="BOX") == {"FINISHED"}
        assert obj.Forge_Geometry.type == "BOX"
        assert tuple(obj.dimensions) == pytest.approx((2, 4, 6))


@pytest.mark.parametrize("group", [2, 3])
def test_sdf_export_import(registered_props, tmp_path, group):
    world = bpy.data.collections.new(cons.CollectionNames.WORLD)
    bpy.context.scene.collection.children.link(world)
    bpy.ops.mesh.primitive_cube_add()
    obj = bpy.context.object
    funcs.link_collection(obj, world)
    obj.Forge_Model_Type = cons.ModelTypes.VISUAL
    obj.Forge_Geometry.type = cons.GeometryTypes.SDF
    obj.Forge_Geometry.group = group

    _, root = run_export(bpy.context, str(tmp_path / "sdf.xml"))
    geom = root.find("worldbody/geom")
    assert geom is not None
    assert geom.get("type") == "sdf"
    assert "size" not in geom.attrib
    asset = root.find("asset/mesh")
    assert asset is not None
    assert geom.get("mesh") == asset.get("name")
    assert asset.get("file").endswith(".obj")

    assets = SimpleNamespace(
        objects={geom.get("mesh"): obj},
        materials_map={geom.get("material"): bpy.data.materials[geom.get("material")]},
    )
    imports.add_geom(bpy.context, lambda *_: None, world, {}, assets, dict(geom.attrib))
    imported = bpy.context.object
    assert imported.Forge_Geometry.type == "SDF"
    assert imported.Forge_Geometry.group == group
    assert imported.Forge_Model_Type == ("COLLIDER" if group == 3 else "VISUAL")
    assert imported.data == obj.data
    parent = ET.Element("worldbody")
    exports.set_geom_tags(parent, imported)
    assert parent.find("geom").get("type") == "sdf"


def test_empty_sdf_omits_geom(registered_props):
    obj = bpy.data.objects.new("EmptySDF", bpy.data.meshes.new("EmptySDF"))
    obj.Forge_Model_Type = cons.ModelTypes.VISUAL
    obj.Forge_Geometry.type = cons.GeometryTypes.SDF
    parent = ET.Element("worldbody")
    exports.set_geom_tags(parent, obj)
    assert parent.find("geom") is None


@pytest.mark.parametrize("method", ["GEOMETRY_TYPE", "COLLIDER_TYPE"])
def test_sdf_collider_creation_preserves_concave_mesh(registered_ops, method):
    from Forge.core.utils import set_collider_to_mesh

    bpy.ops.mesh.primitive_torus_add()
    source = bpy.context.object
    source.Forge_Model_Type = cons.ModelTypes.VISUAL
    source.Forge_Geometry.type = cons.GeometryTypes.SDF
    source.location = (1, 2, 3)
    source.rotation_euler = (0.1, 0.2, 0.3)
    source.scale = (2, 3, 4)
    source.modifiers.new("Visual subdivision", "SUBSURF")
    source_mesh = source.data
    mesh_count = len(bpy.data.meshes)
    with headless_shape_modifiers():
        assert bpy.ops.forge.create_collider(create_method=method, collider_type="SDF") == {"FINISHED"}
    collider = next(obj for obj in bpy.context.selected_objects if obj.Forge_Model_Type == "COLLIDER")
    assert collider.Forge_Geometry.type == "SDF"
    assert collider.data == source_mesh
    assert source.data == source_mesh
    assert len(bpy.data.meshes) == mesh_count
    assert not collider.modifiers
    assert collider.parent == source.parent
    for actual, expected in zip(collider.matrix_basis, source.matrix_basis):
        assert tuple(actual) == pytest.approx(tuple(expected))
    assert len(collider.data.polygons) == len(source.data.polygons)
    assert [tuple(v.co) for v in collider.data.vertices] == [tuple(v.co) for v in source.data.vertices]
    source.data.vertices[0].co.x += 0.25
    assert collider.data.vertices[0].co.x == source.data.vertices[0].co.x
    set_collider_to_mesh(collider, True)
    set_collider_to_mesh(collider, False)
    assert len(funcs.get_gizmo_offset(collider)) == 3


@pytest.mark.parametrize("shape", ["BOX", "SPHERE", "CAPSULE", "CYLINDER"])
@pytest.mark.parametrize("parented", [False, True])
def test_shape_sdf_collider_bakes_evaluated_geometry(registered_ops, tmp_path, shape, parented):
    with headless_shape_modifiers():
        assert bpy.ops.forge.create_geometry(
            geometry_type=shape, size_box=(2, 4, 6), size_radius=1.25, size_height=4
        ) == {"FINISHED"}
        source = bpy.context.object
        if parented:
            parent = bpy.data.objects.new("ShapeParent", None)
            bpy.context.collection.objects.link(parent)
            parent.Forge_Model_Type = cons.ModelTypes.LINK
            parent.location = (3, -2, 1)
            parent.rotation_euler = (0.3, 0.2, 0.1)
            source.parent = parent
            source.matrix_parent_inverse = parent.matrix_world.inverted()
        source.location = (1, 2, 3)
        source.rotation_euler = (0.1, 0.2, 0.3)
        source.scale = (2, 3, 4)
        bpy.context.view_layer.update()
        source_mesh = source.data
        source_modifiers = list(source.modifiers)
        evaluated = source.evaluated_get(bpy.context.evaluated_depsgraph_get())
        expected_vertices = [tuple(v.co) for v in evaluated.data.vertices]
        expected_faces = len(evaluated.data.polygons)
        expected_world = source.matrix_world.copy()
        assert expected_faces > 0

        assert bpy.ops.forge.create_collider(create_method="COLLIDER_TYPE", collider_type="SDF") == {"FINISHED"}

    collider = next(obj for obj in bpy.context.selected_objects if obj.Forge_Model_Type == "COLLIDER")
    assert collider.Forge_Geometry.type == "SDF"
    assert collider.data != source_mesh
    assert not collider.modifiers
    assert len(collider.data.polygons) == expected_faces
    assert len(collider.data.vertices) == len(expected_vertices)
    for vertex, expected in zip(collider.data.vertices, expected_vertices):
        assert tuple(vertex.co) == pytest.approx(expected)
    bpy.context.view_layer.update()
    assert collider.parent == source.parent
    for actual, expected in zip(collider.matrix_world, expected_world):
        assert tuple(actual) == pytest.approx(tuple(expected))
    assert source.data == source_mesh
    assert list(source.modifiers) == source_modifiers
    assert source.Forge_Geometry.type == shape
    filename = funcs.export_collider(collider, str(tmp_path), False)
    collider.data.calc_loop_triangles()
    stl = (tmp_path / filename).read_bytes()
    assert int.from_bytes(stl[80:84], "little") == len(collider.data.loop_triangles)
    assert len(stl) == 84 + 50 * len(collider.data.loop_triangles)


def test_linked_sdf_collider_exports_one_mesh_asset(registered_ops, tmp_path):
    world = bpy.data.collections.new(cons.CollectionNames.WORLD)
    bpy.context.scene.collection.children.link(world)
    bpy.ops.mesh.primitive_cube_add()
    source = bpy.context.object
    funcs.link_collection(source, world)
    source.Forge_Model_Type = cons.ModelTypes.VISUAL
    source.Forge_Geometry.type = cons.GeometryTypes.MESH
    with headless_shape_modifiers():
        bpy.ops.forge.create_collider(create_method="COLLIDER_TYPE", collider_type="SDF")
    collider = next(obj for obj in bpy.context.selected_objects if obj.Forge_Model_Type == "COLLIDER")
    assert collider.data == source.data
    _, root = run_export(bpy.context, str(tmp_path / "linked_sdf.xml"))
    assets = root.findall("asset/mesh")
    assert len(assets) == 1
    geoms = root.findall("worldbody/geom")
    assert {geom.get("type") for geom in geoms} == {"mesh", "sdf"}
    assert all(geom.get("mesh") == assets[0].get("name") for geom in geoms)


def test_collider_primitive_sdf_roundtrip(registered_ops):
    with headless_shape_modifiers():
        bpy.ops.forge.create_collider(collider_type="BOX", size_box=(2, 4, 6))
        obj = bpy.context.object
        assert bpy.ops.forge.define_collider_type(collider_type="SDF") == {"FINISHED"}
        assert obj.Forge_Geometry.type == "SDF"
        assert len(obj.data.polygons) == 6
        assert not obj.modifiers
        assert tuple(obj.dimensions) == pytest.approx((2, 4, 6))
        assert bpy.ops.forge.define_collider_type(collider_type="BOX") == {"FINISHED"}
        assert obj.Forge_Geometry.type == "BOX"
        assert tuple(obj.dimensions) == pytest.approx((2, 4, 6))


def test_sdf_collider_export_asset(registered_props, tmp_path):
    world = bpy.data.collections.new(cons.CollectionNames.WORLD)
    bpy.context.scene.collection.children.link(world)
    bpy.ops.mesh.primitive_cube_add()
    obj = bpy.context.object
    funcs.link_collection(obj, world)
    obj.Forge_Model_Type = cons.ModelTypes.COLLIDER
    obj.Forge_Geometry.type = cons.GeometryTypes.SDF
    obj.Forge_Geometry.group = 3
    _, root = run_export(bpy.context, str(tmp_path / "sdf_collider.xml"))
    geom = root.find("worldbody/geom")
    asset = root.find("asset/mesh")
    assert geom.get("type") == "sdf"
    assert geom.get("mesh") == asset.get("name")
    assert asset.get("file").endswith(".stl")
    funcs.export_collider(obj, str(tmp_path), False)
    assert (tmp_path / f"{obj.data.name}.stl").is_file()
