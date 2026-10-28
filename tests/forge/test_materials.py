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

"""Tests for the Forge material library loader, builder, and create operator."""

import bpy
import pytest
from Forge.core import materials as matlib
from Forge.core.constants import NodeInputName, ShaderPropName
from Forge.ops.materials import Forge_OT_Checker_Material_Creation, Forge_OT_Material_Assign, Forge_OT_Material_Creation

from .mjcf_helpers import attach_shape_modifier, headless_shape_modifiers


def _shader(mat):
    return mat.node_tree.nodes[ShaderPropName.PRINCIPLED]


def _create_visual_mesh():
    """Create and select an operator-compatible visual mesh."""
    bpy.ops.mesh.primitive_cube_add()
    obj = bpy.context.active_object
    obj.Forge_Model_Type = "VISUAL"
    obj.Forge_Geometry.type = "MESH"
    return obj


def _create_renderable(model_type):
    """Create a mesh carrying a material-capable Forge model type."""
    mesh = bpy.data.meshes.new(f"{model_type.lower()}_mesh")
    obj = bpy.data.objects.new(model_type.title(), mesh)
    bpy.context.collection.objects.link(obj)
    obj.Forge_Model_Type = model_type
    return obj


class TestLibraryLoader:
    def test_categories(self):
        assert matlib.get_categories() == ["Crystal", "Human", "Liquid", "Manmade", "Metal", "Organic", "Plastic"]

    def test_global_unique_names(self):
        """Enum identifiers are raw material names — they must be unique across categories."""
        names = [name for category in matlib.get_categories() for name in matlib.get_material_names(category)]
        assert len(names) == len(set(names))

    def test_load_material(self):
        assert matlib.load_material("Crystal", "Diamond")["ior"] == 2.4168
        assert matlib.load_material("Crystal", "Nope") is None
        assert matlib.get_material_names("Nope") == []


@pytest.mark.parametrize("shape", ["BOX", "SPHERE", "CYLINDER", "CAPSULE"])
@pytest.mark.parametrize("target", ["MESH", "SDF"])
@pytest.mark.parametrize("slot_link", ["OBJECT", "DATA"])
def test_shape_to_mesh_preserves_materials(registered_ops, shape, target, slot_link):
    from Forge.core import constants as cons

    with headless_shape_modifiers():
        bpy.ops.forge.create_geometry(geometry_type=shape)
    obj = bpy.context.object
    attach_shape_modifier(obj, cons.GeometryShapeModifiers[shape])
    first = matlib.build_checker_material((0.1, 0.2, 0.3, 1), (0.8, 0.7, 0.6, 1), 4)
    second = bpy.data.materials.new("Additional material")
    obj.data.materials[0] = bpy.data.materials.new("Underlying mesh material")
    obj.material_slots[0].link = slot_link
    obj.material_slots[0].material = first
    obj.data.materials.append(second)
    obj.data.materials.append(None)
    obj.active_material_index = 1
    mesh = obj.data
    original_data_materials = list(mesh.materials)
    original_slots = [(slot.link, slot.material) for slot in obj.material_slots]
    instance = bpy.data.objects.new("Unconverted instance", mesh)
    bpy.context.collection.objects.link(instance)

    assert bpy.ops.forge.define_geometry_type(geometry_type=target) == {"FINISHED"}

    assert obj.Forge_Geometry.type == target
    assert obj.data.polygons
    assert list(obj.data.materials) == original_data_materials
    assert [(slot.link, slot.material) for slot in obj.material_slots] == original_slots
    assert obj.active_material_index == 1
    assert all(obj.material_slots[face.material_index].material == first for face in obj.data.polygons)
    assert instance.data == mesh
    assert list(instance.data.materials) == original_data_materials


class TestAssignMaterial:
    @pytest.mark.parametrize("model_type", ["VISUAL", "HFIELD", "PLANE"])
    def test_assigns_existing_material_without_copying_or_rebuilding(self, registered_ops, model_type):
        first = _create_visual_mesh()
        second = _create_renderable(model_type)
        second.select_set(True)
        material = matlib.build_checker_material((0.1, 0.2, 0.3, 1), (0.8, 0.7, 0.6, 1), 5)
        material.name = "Existing checker 材质"
        material["keep"] = "unchanged"
        nodes = set(material.node_tree.nodes)
        materials = set(bpy.data.materials)

        assert bpy.ops.forge.assign_material(material=material.name) == {"FINISHED"}

        for obj in (first, second):
            assert obj.material_slots[0].material == material
            assert obj.material_slots[0].link == "OBJECT"
        assert set(bpy.data.materials) == materials
        assert set(material.node_tree.nodes) == nodes
        assert material["keep"] == "unchanged"

    def test_replaces_first_slot_preserving_other_slots_and_unselected_instances(self, registered_ops):
        obj = _create_visual_mesh()
        original = bpy.data.materials.new("Original")
        extra = bpy.data.materials.new("Second slot")
        obj.data.materials.append(original)
        obj.data.materials.append(extra)
        instance = bpy.data.objects.new("Unselected instance", obj.data)
        bpy.context.collection.objects.link(instance)
        replacement = bpy.data.materials.new("Replacement")

        assert bpy.ops.forge.assign_material(material=replacement.name) == {"FINISHED"}

        assert len(obj.material_slots) == 2
        assert obj.material_slots[0].material == replacement
        assert obj.material_slots[1].material == extra
        assert instance.material_slots[0].material == original

    @pytest.mark.parametrize("material_name", ["", "Missing material"])
    def test_missing_material_does_not_modify_selection(self, registered_ops, material_name):
        obj = _create_visual_mesh()
        materials = set(bpy.data.materials)

        with pytest.raises(RuntimeError, match="Choose an existing material"):
            bpy.ops.forge.assign_material(material=material_name)

        assert len(obj.material_slots) == 0
        assert set(bpy.data.materials) == materials

    def test_poll_rejects_empty_and_mixed_unsupported_selection(self, registered_ops):
        assert not Forge_OT_Material_Assign.poll(bpy.context)
        _create_visual_mesh()
        assert Forge_OT_Material_Assign.poll(bpy.context)
        unsupported = _create_renderable("COLLIDER")
        unsupported.select_set(True)
        assert not Forge_OT_Material_Assign.poll(bpy.context)


class TestCreateCheckerMaterial:
    def test_create_node_graph_and_parameters(self, registered_ops):
        obj = _create_visual_mesh()
        color1 = (0.1, 0.2, 0.3, 1.0)
        color2 = (0.7, 0.8, 0.9, 1.0)

        assert bpy.ops.forge.create_checker_material(color1=color1, color2=color2, repeat=3) == {"FINISHED"}

        mat = obj.material_slots[0].material
        shader = _shader(mat)
        checker = shader.inputs[NodeInputName.COLOR].links[0].from_node
        assert checker.bl_idname == "ShaderNodeTexChecker"
        assert tuple(checker.inputs["Color1"].default_value) == pytest.approx(color1)
        assert tuple(checker.inputs["Color2"].default_value) == pytest.approx(color2)
        assert checker.inputs["Scale"].default_value == pytest.approx(2.0)
        mapping = checker.inputs["Vector"].links[0].from_node
        assert mapping.bl_idname == "ShaderNodeMapping"
        assert tuple(mapping.inputs["Scale"].default_value) == pytest.approx((3, 3, 1))
        coordinate_link = mapping.inputs["Vector"].links[0]
        assert coordinate_link.from_node.bl_idname == "ShaderNodeTexCoord"
        assert coordinate_link.from_socket.name == "UV"
        output = mat.node_tree.nodes["Material Output"]
        assert output.inputs["Surface"].links[0].from_node == shader

        default = bpy.data.materials.new("Default PBR")
        matlib.ensure_shader_nodes(default)
        for name in (NodeInputName.METALLIC, NodeInputName.ROUGHNESS, "IOR", "Transmission Weight"):
            assert shader.inputs[name].default_value == pytest.approx(_shader(default).inputs[name].default_value)

    @pytest.mark.parametrize("model_type", ["VISUAL", "HFIELD", "PLANE"])
    def test_assigns_one_new_material_to_selection(self, registered_ops, model_type):
        first = _create_visual_mesh()
        old = bpy.data.materials.new("Previous")
        first.data.materials.append(old)
        second = _create_renderable(model_type)
        second.select_set(True)

        assert bpy.ops.forge.create_checker_material() == {"FINISHED"}
        material = first.material_slots[0].material
        assert material != old
        assert second.material_slots[0].material == material
        assert len(first.material_slots) == 1

        assert bpy.ops.forge.create_checker_material(repeat=7) == {"FINISHED"}
        assert first.material_slots[0].material != material
        assert second.material_slots[0].material == first.material_slots[0].material
        mapping = next(node for node in material.node_tree.nodes if node.bl_idname == "ShaderNodeMapping")
        assert tuple(mapping.inputs["Scale"].default_value) == pytest.approx((4, 4, 1))
        new_material = first.material_slots[0].material
        new_mapping = next(node for node in new_material.node_tree.nodes if node.bl_idname == "ShaderNodeMapping")
        assert tuple(new_mapping.inputs["Scale"].default_value) == pytest.approx((7, 7, 1))

    def test_poll_rejects_empty_or_unsupported_selection(self, registered_ops):
        assert not Forge_OT_Checker_Material_Creation.poll(bpy.context)
        obj = _create_visual_mesh()
        assert Forge_OT_Checker_Material_Creation.poll(bpy.context)
        obj.Forge_Model_Type = "COLLIDER"
        assert not Forge_OT_Checker_Material_Creation.poll(bpy.context)


@pytest.mark.parametrize("image_name", ["environment", "environment.hdr", "environment.HDR", "environment.hdr.001"])
def test_export_environment_hdr_extension(tmp_path, image_name):
    from Forge.core import constants as cons
    from Forge.core import function as funcs

    existing_world = bpy.data.worlds.get("World")
    if existing_world:
        existing_world.name = "World_before_hdr_test"
    try:
        world = bpy.data.worlds.new("World")
        matlib.ensure_shader_nodes(world)
        image = bpy.data.images.new(image_name, width=1, height=1, float_buffer=True)
        texture = world.node_tree.nodes.new("ShaderNodeTexEnvironment")
        texture.image = image
        world.node_tree.links.new(texture.outputs["Color"], world.node_tree.nodes["Background"].inputs["Color"])

        props = {}
        assert funcs.parse_material({cons.GSubPaths.TEXTURE: str(tmp_path)}, {}, props, lambda *a: None)
        filename, exported_image, path = props[cons.ShaderPropName.ENV][cons.ShaderPropName.BACKGROUND]

        expected = image_name if image_name.lower().endswith(".hdr") else image_name + ".hdr"
        assert filename == expected
        assert path == str(tmp_path / expected)
        exported_image.save(filepath=path, save_copy=True)
        assert (tmp_path / filename).read_bytes().startswith(b"#?RADIANCE")
    finally:
        if existing_world:
            bpy.data.worlds.remove(world)
            existing_world.name = "World"


@pytest.mark.parametrize("image_name", ["texture", "texture.png", "texture.PNG", "texture.jpg", "texture.png.001"])
def test_export_material_png_extensions(tmp_path, image_name):
    from Forge.core import constants as cons
    from Forge.core import function as funcs
    from Forge.ops import exports

    material = bpy.data.materials.new("png_export")
    matlib.ensure_shader_nodes(material)
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    shader = nodes[cons.ShaderPropName.PRINCIPLED]
    texture = nodes.new("ShaderNodeTexImage")
    texture.image = bpy.data.images.new(image_name, width=1, height=1)
    links.new(texture.outputs["Color"], shader.inputs[NodeInputName.COLOR])
    links.new(texture.outputs["Alpha"], shader.inputs[NodeInputName.ALPHA])
    links.new(texture.outputs["Color"], shader.inputs[NodeInputName.EMISSION])
    normal = nodes.new("ShaderNodeNormalMap")
    links.new(texture.outputs["Color"], normal.inputs["Color"])
    links.new(normal.outputs["Normal"], shader.inputs[NodeInputName.NORMAL])
    separate = nodes.new("ShaderNodeSeparateXYZ")
    links.new(texture.outputs["Color"], separate.inputs["Vector"])
    links.new(separate.outputs["Y"], shader.inputs[NodeInputName.ROUGHNESS])
    links.new(separate.outputs["Z"], shader.inputs[NodeInputName.METALLIC])

    props = {}
    assert funcs.parse_material(
        {cons.GSubPaths.TEXTURE: str(tmp_path)}, {material.name: material}, props, lambda *a: None
    )
    exported = props[material.name]
    expected = {
        "texture": "texture.png",
        "texture.png": "texture.png",
        "texture.PNG": "texture.png",
        "texture.jpg": "texture.png",
        "texture.png.001": "texture.png.001.png",
    }[image_name]
    for tag in [
        cons.ShaderPropName.COLORTEX,
        cons.ShaderPropName.ALPHATEX,
        cons.ShaderPropName.NORMALTEX,
        cons.ShaderPropName.ROUGHNESSTEX,
        cons.ShaderPropName.METALLICTEX,
        cons.ShaderPropName.EMISSIONTEX,
    ]:
        filename, image, path = exported[tag]
        assert filename == expected
        assert path == str(tmp_path / expected)
        assert image.file_format == "PNG"
    exports.export_images(exported, update_xml_only=False)
    assert (tmp_path / expected).read_bytes().startswith(b"\x89PNG\r\n\x1a\n")


class TestCreateMaterial:
    def test_create_basic(self, registered_ops):
        obj = _create_visual_mesh()
        bpy.ops.forge.create_material(category="Crystal", material="Diamond")

        mat = bpy.data.materials["Diamond"]
        assert obj.material_slots[0].material == mat
        shader = _shader(mat)
        assert mat.node_tree is not None
        # Library color is linear — set directly without conversion.
        assert list(shader.inputs[NodeInputName.COLOR].default_value) == [1.0, 1.0, 1.0, 1.0]
        assert shader.inputs[NodeInputName.METALLIC].default_value == pytest.approx(0.0)
        assert shader.inputs[NodeInputName.ROUGHNESS].default_value == pytest.approx(0.0)
        assert shader.inputs["IOR"].default_value == pytest.approx(2.4168)
        assert shader.inputs["Transmission Weight"].default_value == pytest.approx(1.0)

    def test_linear_color_preserved(self, registered_ops):
        _create_visual_mesh()
        bpy.ops.forge.create_material(category="Metal", material="Gold")

        mat = bpy.data.materials["Gold"]
        shader = _shader(mat)
        assert list(shader.inputs[NodeInputName.COLOR].default_value) == pytest.approx([1.059, 0.773, 0.307, 1.0])

    def test_custom_props(self, registered_ops):
        _create_visual_mesh()
        bpy.ops.forge.create_material(category="Liquid", material="Water")

        mat = bpy.data.materials["Water"]
        assert mat["density"] == 1000
        assert list(mat["viscosity"]) == [1.002]
        assert mat["surfaceTension"] == 72
        assert list(mat["category"]) == ["Liquid"]
        assert list(mat["tags"]) == ["acoustics", "audio"]
        assert mat["transmissionDispersion"] == pytest.approx(55.78)
        # Nested dict is stored as an IDPropertyGroup — check the structure survived.
        assert "absorption" in mat["volumeCoefficients"]
        assert "scattering" in mat["volumeCoefficients"]

    def test_subsurface(self, registered_ops):
        _create_visual_mesh()
        bpy.ops.forge.create_material(category="Human", material="Skin I")

        shader = _shader(bpy.data.materials["Skin I"])
        assert shader.inputs["Subsurface Weight"].default_value == pytest.approx(1.0)
        assert tuple(shader.inputs["Subsurface Radius"].default_value) == pytest.approx((0.482, 0.169, 0.109))

    def test_thin_film(self, registered_ops):
        _create_visual_mesh()
        bpy.ops.forge.create_material(category="Metal", material="Titanium (Anodized)")

        shader = _shader(bpy.data.materials["Titanium (Anodized)"])
        assert shader.inputs["Thin Film Thickness"].default_value == pytest.approx(300)
        assert shader.inputs["Thin Film IOR"].default_value == pytest.approx(2.488)

    def test_poll_requires_visual_selection(self, registered_ops):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        # A plain mesh object is UNDEFINED — poll must reject the selection.
        assert not Forge_OT_Material_Creation.poll(bpy.context)

        obj.Forge_Model_Type = "VISUAL"
        assert Forge_OT_Material_Creation.poll(bpy.context)

        # The operator creates and assigns in one action, so empty selection is invalid.
        obj.select_set(False)
        assert not Forge_OT_Material_Creation.poll(bpy.context)

    @pytest.mark.parametrize("model_type", ["HFIELD", "PLANE"])
    def test_poll_and_assign_support_height_field_and_plane(self, registered_ops, model_type):
        obj = _create_renderable(model_type)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        assert Forge_OT_Material_Creation.poll(bpy.context)
        bpy.ops.forge.create_material(category="Metal", material="Gold")

        assert len(obj.material_slots) == 1
        assert obj.material_slots[0].material.name == "Gold"
        assert obj.material_slots[0].link == "OBJECT"

    def test_primitive_visual_uses_first_material_slot(self, registered_ops):
        obj = _create_renderable("VISUAL")
        obj.Forge_Geometry.type = "BOX"
        obj.data.materials.append(bpy.data.materials.new("Old"))
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        bpy.ops.forge.create_material(category="Metal", material="Gold")

        assert obj.material_slots[0].material.name == "Gold"

    def test_assign_to_mesh(self, registered_ops):
        obj = _create_visual_mesh()
        bpy.ops.forge.create_material(category="Metal", material="Gold")

        assert obj.material_slots[0].material.name == "Gold"

    def test_assign_replaces_first_material_slot(self, registered_ops):
        obj = _create_visual_mesh()
        old_material = bpy.data.materials.new("Old")
        obj.data.materials.append(old_material)

        bpy.ops.forge.create_material(category="Metal", material="Gold")

        assert len(obj.data.materials) == 1
        assert obj.material_slots[0].material.name == "Gold"

    def test_assign_supports_plain_mesh_directly(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        material = matlib.build_material(matlib.load_material("Metal", "Gold"))

        assert obj.Forge_Model_Type == "UNDEFINED"
        assert matlib.assign_material(bpy.context, obj, material) is True
        assert obj.material_slots[0].material is material

    def test_assign_skips_unsupported_model_type(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "COLLIDER"
        material = matlib.build_material(matlib.load_material("Metal", "Gold"))

        assert matlib.assign_material(bpy.context, obj, material) is False
        assert len(obj.data.materials) == 0

    def test_build_restores_missing_principled_shader(self, registered_props):
        params = matlib.load_material("Metal", "Gold")
        material = matlib.build_material(params)
        material.node_tree.nodes.remove(_shader(material))

        rebuilt = matlib.build_material(params)

        assert rebuilt is material
        assert _shader(material) is not None
        assert any(link.to_node.name == "Material Output" for link in material.node_tree.links)

    def test_duplicate_idempotent(self, registered_ops):
        _create_visual_mesh()
        bpy.ops.forge.create_material(category="Metal", material="Gold")
        count = len(bpy.data.materials)
        bpy.ops.forge.create_material(category="Metal", material="Gold")

        assert len(bpy.data.materials) == count
        shader = _shader(bpy.data.materials["Gold"])
        assert shader.inputs[NodeInputName.METALLIC].default_value == pytest.approx(1.0)

    def test_use_existing_reuses_without_rebuild(self, registered_ops):
        obj = _create_visual_mesh()
        bpy.ops.forge.create_material(category="Metal", material="Gold")

        # Simulate a user tweak — a re-run with use_existing must not rebuild it.
        mat = bpy.data.materials["Gold"]
        _shader(mat).inputs[NodeInputName.ROUGHNESS].default_value = 0.9

        count = len(bpy.data.materials)
        bpy.ops.forge.create_material(category="Metal", material="Gold", use_existing=True)

        assert len(bpy.data.materials) == count  # no duplicate created
        assert obj.material_slots[0].material is mat
        assert _shader(mat).inputs[NodeInputName.ROUGHNESS].default_value == pytest.approx(0.9)

    def test_use_existing_false_creates_new_material(self, registered_ops):
        obj = _create_visual_mesh()
        bpy.ops.forge.create_material(category="Metal", material="Gold")

        bpy.ops.forge.create_material(category="Metal", material="Gold", use_existing=False)

        assert bpy.data.materials["Gold.001"]  # Blender suffixes the taken name
        assert obj.material_slots[0].material.name == "Gold.001"
        assert _shader(bpy.data.materials["Gold.001"]).inputs[NodeInputName.METALLIC].default_value == pytest.approx(
            1.0
        )

    def test_export_roundtrip(self, registered_ops):
        """Created materials parse cleanly through the MJCF export pipeline."""
        from Forge.core import constants as cons
        from Forge.core import function as funcs

        _create_visual_mesh()
        bpy.ops.forge.create_material(category="Metal", material="Gold")
        mat = bpy.data.materials["Gold"]

        materials_props_map = {}
        result = funcs.parse_material(
            {cons.GSubPaths.TEXTURE: "textures"},
            {"Gold": mat},
            materials_props_map,
            lambda *a: None,
        )
        assert result is True

        props = materials_props_map["Gold"]
        assert props[NodeInputName.METALLIC] == pytest.approx(1.0)
        assert props[NodeInputName.ROUGHNESS] == pytest.approx(0.0)
        assert props[cons.ShaderPropName.COLORTEX] == [None, None, None]
        # Linear library color is converted to sRGB on export.
        assert props[NodeInputName.COLOR] == pytest.approx(list(funcs.linear_to_srgb([1.059, 0.773, 0.307])) + [1.0])

        import xml.etree.ElementTree as ET

        from Forge.ops import exports

        root = ET.Element("asset")
        exports.set_material_tags(root, "Gold", props)
        rgba = [float(value) for value in root.find("material").get("rgba").split()]
        assert rgba == pytest.approx([1.0, *funcs.linear_to_srgb([0.773, 0.307]), 1.0])
        assert _shader(mat).inputs[NodeInputName.COLOR].default_value[0] == pytest.approx(1.059)

    def test_export_roughness_math_with_linked_b_input(self, registered_props, tmp_path):
        """A linked Math B input must be read from the value socket, not an unrelated color socket."""
        from Forge.core import constants as cons
        from Forge.core import function as funcs

        material = bpy.data.materials.new("linked-b")
        matlib.ensure_shader_nodes(material)
        nodes = material.node_tree.nodes
        links = material.node_tree.links
        shader = nodes.get(cons.ShaderPropName.PRINCIPLED)
        image = bpy.data.images.new("orm.png", width=1, height=1)
        texture = nodes.new("ShaderNodeTexImage")
        texture.image = image
        separate = nodes.new("ShaderNodeSeparateXYZ")
        multiply = nodes.new("ShaderNodeMath")
        multiply.operation = "MULTIPLY"
        value = nodes.new("ShaderNodeValue")
        links.new(texture.outputs["Color"], separate.inputs["Vector"])
        links.new(separate.outputs["Y"], multiply.inputs[0])
        links.new(value.outputs["Value"], multiply.inputs[1])
        links.new(multiply.outputs["Value"], shader.inputs[NodeInputName.ROUGHNESS])

        props = {}
        messages = []
        result = funcs.parse_material(
            {cons.GSubPaths.TEXTURE: str(tmp_path)},
            {material.name: material},
            props,
            lambda level, message: messages.append((level, message)),
        )

        assert result is True
        assert messages == []
        assert props[material.name][cons.ShaderPropName.ROUGHNESSTEX][0] == "orm.png"
