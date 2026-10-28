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

"""GLB assets retain file coordinates, UVs and MJCF material ownership."""

import json
import struct

import bpy
import pytest
from Forge.core import function as funcs
from Forge.core.common import ensure_shader_nodes
from Forge.ops import imports as load
from mathutils import Vector

from .test_import import run_import


def _triangle_glb(tmp_path):
    mesh = bpy.data.meshes.new("OriginalGLBMesh")
    mesh.from_pydata([(0.2, 0.4, 0.6), (1.3, 0.4, 0.6), (0.2, 2.1, 3.7)], [], [(0, 1, 2)])
    layer = mesh.uv_layers.new(name="UVMap")
    for uv, value in zip(layer.uv, [(0.15, 0.25), (0.7, 0.35), (0.25, 0.9)]):
        uv.vector = value
    source = bpy.data.objects.new("OriginalGLBObject", mesh)
    bpy.context.collection.objects.link(source)
    source.location = (3, -2, 4)
    filename = funcs.export_assets(source, str(tmp_path), False, True)
    return source, filename


def test_glb_export_excludes_other_scenes_and_their_selected_objects(tmp_path):
    empty_scene = bpy.data.scenes.new("EmptyAttachedModel")
    other_scene = bpy.data.scenes.new("IncludedModel")
    other_obj = bpy.data.objects.new("UnrelatedIncludedNode", None)
    other_scene.collection.objects.link(other_obj)
    other_obj.select_set(True, view_layer=other_scene.view_layers[0])
    try:
        source, filename = _triangle_glb(tmp_path)
        data = (tmp_path / filename).read_bytes()
        length, chunk_type = struct.unpack_from("<II", data, 12)
        assert chunk_type == 0x4E4F534A
        document = json.loads(data[20 : 20 + length])
        assert document["scene"] == 0
        assert document["scenes"] == [{"name": bpy.context.scene.name, "nodes": [0]}]
        assert document["nodes"] == [{"mesh": 0, "name": source.name}]
        assert len(document["meshes"]) == 1
    finally:
        bpy.data.objects.remove(other_obj, do_unlink=True)
        bpy.data.scenes.remove(other_scene)
        bpy.data.scenes.remove(empty_scene)


@pytest.mark.parametrize("unit_scale", [1.0, 0.25])
def test_forge_glb_roundtrip_preserves_asset_coordinates_uv_and_scale(tmp_path, unit_scale):
    scene = bpy.context.scene
    previous_unit = scene.unit_settings.scale_length
    try:
        scene.unit_settings.scale_length = 1.0
        source, filename = _triangle_glb(tmp_path)
        scene.unit_settings.scale_length = unit_scale
        collection = bpy.data.collections.new("Mesh Assets")
        scene.collection.children.link(collection)
        collection.hide_viewport = True
        original_objects = set(bpy.data.objects)
        assets = {}
        load.import_mesh(
            bpy.context,
            lambda *_: None,
            {"name": "asset_alias", "file": filename, "scale": "2 3 4"},
            assets,
            tmp_path,
            collection,
            "model_",
        )

        obj = assets["asset_alias"]
        assert set(bpy.data.objects) - original_objects == {obj}
        assert obj.data.name == "model_asset_alias"
        assert obj.name == "model_asset_alias.glb"
        assert obj.users_collection[:] == (collection,)
        assert obj["FORMAT"] == ".glb"
        assert tuple(obj["SCALE"]) == (2, 3, 4)
        assert obj.parent is None
        assert tuple(obj.location) == (0, 0, 0)
        assert tuple(obj.scale) == (1, 1, 1)

        actual = {
            tuple(round(c, 5) for c in obj.data.vertices[loop.vertex_index].co): tuple(
                round(c, 5) for c in obj.data.uv_layers[0].uv[index].vector
            )
            for index, loop in enumerate(obj.data.loops)
        }
        expected = {
            tuple(round(c, 5) for c in vertex.co * Vector((2, 3, 4))): tuple(round(c, 5) for c in uv.vector)
            for vertex, uv in zip(source.data.vertices, source.data.uv_layers[0].uv)
        }
        assert actual == expected
        assert not any(c.name.startswith("_ForgeGLBImport") for c in bpy.data.collections)
    finally:
        scene.unit_settings.scale_length = previous_unit


def test_glb_single_mesh_ignores_other_elements_and_embedded_materials(tmp_path):
    bpy.ops.object.empty_add(location=(1, -2, 3))
    parent = bpy.context.object
    parent.rotation_euler = (0.2, 0.1, 0.3)
    material = bpy.data.materials.new("EmbeddedGLBMaterial")
    ensure_shader_nodes(material)
    bpy.ops.mesh.primitive_cube_add(size=1)
    source = bpy.context.object
    source.parent = parent
    source.location = (2, 3, 4)
    source.rotation_euler = (0.1, -0.2, 0.4)
    source.scale = (0.5, 0.7, 1.1)
    source["node_extra"] = "not an MJCF object property"
    source.data.materials.append(material)
    bpy.ops.object.camera_add()
    camera = bpy.context.object
    bpy.ops.object.light_add(type="POINT")
    light = bpy.context.object
    bpy.context.view_layer.update()
    expected = {tuple(round(c, 5) for c in source.matrix_world @ vertex.co) for vertex in source.data.vertices}
    bpy.ops.object.select_all(action="DESELECT")
    for obj in [parent, source, camera, light]:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = source
    filepath = tmp_path / "nodes.GLB"
    bpy.ops.export_scene.gltf(
        filepath=str(filepath),
        export_format="GLB",
        use_selection=True,
        export_yup=False,
        export_materials="EXPORT",
        export_animations=False,
        export_extras=True,
        export_cameras=True,
        export_lights=True,
    )
    collection = bpy.data.collections.new("Mesh Assets")
    bpy.context.scene.collection.children.link(collection)
    original_objects = set(bpy.data.objects)
    original_materials = set(bpy.data.materials)
    original_cameras = set(bpy.data.cameras)
    original_lights = set(bpy.data.lights)
    assets = {}

    load.import_mesh(
        bpy.context, lambda *_: None, {"name": "single", "file": filepath.name}, assets, tmp_path, collection
    )

    obj = assets["single"]
    assert set(bpy.data.objects) - original_objects == {obj}
    assert {tuple(round(c, 5) for c in vertex.co) for vertex in obj.data.vertices} == expected
    assert len(obj.data.polygons) == 12
    assert len(obj.data.materials) == 0
    assert {face.material_index for face in obj.data.polygons} == {0}
    assert set(bpy.data.materials) == original_materials
    assert set(bpy.data.cameras) == original_cameras
    assert set(bpy.data.lights) == original_lights
    assert obj.parent is None
    assert "node_extra" not in obj
    assert obj.animation_data is None


def test_glb_multiple_mesh_objects_are_rejected(tmp_path):
    meshes = []
    for _ in range(2):
        bpy.ops.mesh.primitive_cube_add()
        meshes.append(bpy.context.object)
    bpy.ops.object.select_all(action="DESELECT")
    for obj in meshes:
        obj.select_set(True)
    filepath = tmp_path / "multiple.glb"
    bpy.ops.export_scene.gltf(filepath=str(filepath), export_format="GLB", use_selection=True)
    collection = bpy.data.collections.new("Mesh Assets")
    bpy.context.scene.collection.children.link(collection)
    before = set(bpy.data.objects)
    assets = {}

    with pytest.raises(ValueError, match="exactly one mesh object"):
        load.import_mesh(
            bpy.context, lambda *_: None, {"name": "multiple", "file": filepath.name}, assets, tmp_path, collection
        )

    assert assets == {}
    assert set(bpy.data.objects) == before
    assert not any(c.name.startswith("_ForgeGLBImport") for c in bpy.data.collections)


def test_glb_asset_imports_as_mjcf_geometry_and_accepts_mjcf_material(registered_ops, tmp_path):
    bpy.context.scene.Forge_GlobalConfig.reset()
    bpy.context.scene.Forge_Props.import_material = True
    _source, filename = _triangle_glb(tmp_path)
    filepath = tmp_path / "glb_model.xml"
    filepath.write_text(
        '<mujoco><compiler meshdir="."/><asset>'
        f'<mesh name="alias" file="{filename}"/>'
        '<material name="mjcf_material" rgba="0.3 0.4 0.5 1"/></asset>'
        '<worldbody><body name="body"><geom name="glb_visual" type="mesh" mesh="alias" '
        'material="mjcf_material"/></body></worldbody></mujoco>',
        encoding="utf-8",
    )

    messages = run_import(bpy.context, str(filepath))

    assert not [message for kinds, message in messages if "ERROR" in kinds]
    obj = bpy.data.objects["glb_visual"]
    assert obj.Forge_Model_Type == "VISUAL"
    assert obj.parent.name == "body"
    assert len(obj.data.polygons) == 1
    assert obj.material_slots[0].material.name == "mjcf_material"
    assert load.cleanup_mesh_asset_loaders() == ["alias.glb"]
    assert obj.data.users == 1


def test_glb_without_mesh_fails_without_leaving_imported_objects(tmp_path):
    bpy.ops.object.empty_add()
    filepath = tmp_path / "empty.glb"
    bpy.ops.export_scene.gltf(filepath=str(filepath), export_format="GLB", use_selection=True)
    collection = bpy.data.collections.new("Mesh Assets")
    bpy.context.scene.collection.children.link(collection)
    before = set(bpy.data.objects)
    assets = {}

    with pytest.raises(ValueError, match="no mesh objects"):
        load.import_mesh(
            bpy.context, lambda *_: None, {"name": "empty", "file": filepath.name}, assets, tmp_path, collection
        )

    assert assets == {}
    assert set(bpy.data.objects) == before
    assert not any(c.name.startswith("_ForgeGLBImport") for c in bpy.data.collections)


@pytest.mark.parametrize("filename", ["missing.glb", "unsupported.ply"])
def test_unloadable_mesh_reports_asset_and_path(tmp_path, filename):
    if filename.endswith(".ply"):
        (tmp_path / filename).write_text("not supported", encoding="utf-8")
    collection = bpy.data.collections.new("Mesh Assets")
    bpy.context.scene.collection.children.link(collection)
    with pytest.raises((FileNotFoundError, ValueError), match="test_asset"):
        load.import_mesh(
            bpy.context, lambda *_: None, {"name": "test_asset", "file": filename}, {}, tmp_path, collection
        )
