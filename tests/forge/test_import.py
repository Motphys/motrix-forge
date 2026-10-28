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

"""Roundtrip MJCF import tests.

Exports a scene via the export pipeline (see ``test_export``), feeds the XML
through the import pipeline — the same ``load.*`` sequence the
``Forge_OT_Import`` operator drives via its modal task queue — and asserts
the reconstructed scene. A re-export of the imported scene closes the loop.

``bpy.ops.object.modifier_add_node_group`` never works in background mode
(asset libraries never finish loading), so imported shape visuals get their
node-group modifier linked directly from Shapes.blend.
"""

import xml.etree.ElementTree as ET
from math import degrees
from pathlib import Path
from types import SimpleNamespace

import bpy
import pytest
from Forge.core import constants as cons
from Forge.ops import exports as out
from Forge.ops import imports as load

from .mjcf_helpers import (
    SHAPES_BLEND,
    attach_shape_modifier,
    build_scene,
    collector,
    headless_shape_modifiers,
    run_export,
)


@pytest.fixture(autouse=True)
def require_shapes_asset():
    """Fail loudly when the checked-in shape library is missing."""
    if not SHAPES_BLEND.exists():
        pytest.fail("Shapes.blend asset library is required for import tests")


@pytest.mark.parametrize("space_kind", ["none", "other", "view3d"])
def test_envhdr_import_does_not_require_viewport_context(registered_props, monkeypatch, tmp_path, space_kind):
    image = bpy.data.images.new("test_environment", width=2, height=1, float_buffer=True)
    monkeypatch.setattr(load, "load_textures", lambda *_args: image)
    created_worlds = []

    class TestWorlds:
        def __iter__(self):
            # Keep unrelated fixture worlds out of the importer's replacement.
            return iter(())

        def new(self, name):
            world = bpy.data.worlds.new(name)
            created_worlds.append(world)
            return world

    monkeypatch.setattr(load, "bpy", SimpleNamespace(data=SimpleNamespace(worlds=TestWorlds()), types=bpy.types))
    if space_kind == "view3d":
        space = next(
            area.spaces.active for screen in bpy.data.screens for area in screen.areas if area.type == "VIEW_3D"
        )
    elif space_kind == "other":
        space = SimpleNamespace(shading=SimpleNamespace(use_scene_world=False))
    else:
        space = None
    previous_setting = space.shading.use_scene_world if space else None
    if space_kind == "view3d":
        space.shading.use_scene_world = False
    previous_world = bpy.context.scene.world
    context = SimpleNamespace(scene=bpy.context.scene, blend_data=bpy.data, space_data=space)
    try:
        load.get_asset(
            context,
            lambda *_args: None,
            SimpleNamespace(import_material=True),
            ET.fromstring('<texture name="environment" type="envhdr" file="environment.hdr" />'),
            {},
            SimpleNamespace(images={}),
            tmp_path,
        )
        world = bpy.context.scene.world
        assert world == created_worlds[0]
        environment = next(node for node in world.node_tree.nodes if node.type == "TEX_ENVIRONMENT")
        assert environment.image == image
        assert environment.outputs["Color"].is_linked
        background = next(node for node in world.node_tree.nodes if node.type == "BACKGROUND")
        assert background.outputs[0].is_linked
        if space_kind == "view3d":
            assert space.shading.use_scene_world is True
        elif space_kind == "other":
            assert space.shading.use_scene_world is False
    finally:
        bpy.context.scene.world = previous_world
        if space:
            space.shading.use_scene_world = previous_setting
        for world in created_worlds:
            bpy.data.worlds.remove(world)


def run_import(context, filepath):
    """Run the import pipeline (the operator's task sequence) on an MJCF file.

    Returns the collected report messages.
    """
    messages = []
    report = collector(messages)
    forge_props = context.scene.Forge_Props

    task_list = [("", "", "", None)]
    load.get_task_recursive(Path(filepath), task_list, {})

    with headless_shape_modifiers():
        for ref_type, identifier, model, task in task_list[1:]:
            model_prefix = identifier.replace(".", "_") + "_" if model else ""
            base_dir = task.base_dir

            for _pi, element in task.compiler.elements:
                load.get_compiler(context, element)
            for _pi, element in task.option.elements:
                load.get_option(context, element)
            for _pi, element in task.statistic.elements:
                load.get_statistic(context, element)
            for _pi, element in task.visual.elements:
                load.get_visual(context, element)
            for _pi, element in task.asset.elements:
                load.get_asset(
                    context, report, forge_props, element, task.defaults, task.assets_data, base_dir, model_prefix
                )
            for index in range(len(task.worldbody.elements)):
                load.build_world_tree(
                    context, report, task, task.assets_data, index, str(Path(filepath).parent), model_prefix, None
                )
            for _pi, element in task.contact.elements:
                load.add_contact(context, report, element, None, model_prefix)
            for _pi, element in task.equality.elements:
                load.add_equality(context, report, element, task.defaults, None, model_prefix)
            for _pi, element in task.tendon.elements:
                load.add_tendon(context, report, element, task.defaults, None, model_prefix)
            for _pi, element in task.actuator.elements:
                load.add_actuator(context, report, element, task.defaults, None, model_prefix)
            for _pi, element in task.sensor.elements:
                load.add_sensor(context, report, element, None, model_prefix)

    return messages


def _objects_of_type(model_type):
    return [obj for obj in bpy.data.objects if obj.Forge_Model_Type == model_type]


class TestImportMjcf:
    @pytest.mark.parametrize("reference", ["attribute", "layer"])
    @pytest.mark.parametrize("explicit", [False, True])
    @pytest.mark.parametrize("tinted", [False, True])
    def test_import_checker_material(self, registered_ops, tmp_path, reference, explicit, tinted):
        from Forge.core import function as funcs

        colors = 'rgb1="0.1 0.3 0.5" rgb2="0.7 0.4 0.2"' if explicit else ""
        repeat = 'texrepeat="3 5"' if explicit else ""
        texture_ref = 'texture="checks"' if reference == "attribute" else ""
        layer = '<layer role="rgb" texture="checks" />' if reference == "layer" else ""
        rgba = 'rgba="0.5 0.7 0.9 0.4"' if tinted else ""
        filepath = tmp_path / "checker.xml"
        filepath.write_text(
            "<mujoco><asset>"
            f'<texture name="checks" type="2d" builtin="checker" {colors} width="512" height="512" />'
            f'<material name="CheckerImport" {texture_ref} {repeat} {rgba} metallic="0.3" roughness="0.6">'
            f"{layer}</material></asset>"
            '<worldbody><geom name="floor" type="sphere" size="1" material="CheckerImport" /></worldbody>'
            "</mujoco>",
            encoding="utf-8",
        )

        messages = run_import(bpy.context, str(filepath))
        assert [message for kind, message in messages if "ERROR" in kind] == []
        material = bpy.data.materials["CheckerImport"]
        floor = next(obj for obj in bpy.data.objects if obj.name == "floor")
        assert floor.material_slots[0].material is material
        shader = material.node_tree.nodes[cons.ShaderPropName.PRINCIPLED]
        checker = shader.inputs[cons.NodeInputName.COLOR].links[0].from_node
        assert checker.bl_idname == "ShaderNodeTexChecker"
        assert sum(node.bl_idname == "ShaderNodeTexChecker" for node in material.node_tree.nodes) == 1
        assert sum(node.bl_idname == "ShaderNodeMapping" for node in material.node_tree.nodes) == 1
        expected_colors = [(0.1, 0.3, 0.5), (0.7, 0.4, 0.2)] if explicit else [(0.8,) * 3, (0.5,) * 3]
        tint = funcs.srgb_to_linear((0.5, 0.7, 0.9)) if tinted else (1, 1, 1)
        linear_colors = [
            [channel * factor for channel, factor in zip(funcs.srgb_to_linear(color), tint)]
            for color in expected_colors
        ]
        for socket, color in zip(("Color1", "Color2"), linear_colors):
            assert tuple(checker.inputs[socket].default_value) == pytest.approx(color + [1.0])
        assert checker.inputs["Scale"].default_value == 2.0
        mapping = checker.inputs["Vector"].links[0].from_node
        assert tuple(mapping.inputs["Scale"].default_value) == pytest.approx((3, 5, 1) if explicit else (1, 1, 1))
        assert mapping.inputs["Vector"].links[0].from_socket.name == "UV"
        assert shader.inputs[cons.NodeInputName.METALLIC].default_value == pytest.approx(0.3)
        assert shader.inputs[cons.NodeInputName.ROUGHNESS].default_value == pytest.approx(0.6)
        assert shader.inputs[cons.NodeInputName.ALPHA].default_value == pytest.approx(0.4 if tinted else 1.0)

        exported = {}
        assert funcs.parse_material(
            {cons.GSubPaths.TEXTURE: str(tmp_path)}, {material.name: material}, exported, collector(messages)
        )
        props = exported[material.name]
        for actual, expected in zip(props[cons.ShaderPropName.CHECKER], linear_colors):
            assert actual == pytest.approx(funcs.linear_to_srgb(expected))
        assert props[cons.ShaderPropName.TILING] == pytest.approx((3, 5) if explicit else (1, 1))
        asset = ET.Element("asset")
        out.set_material_tags(asset, material.name, props)
        texture = asset.find("texture")
        assert texture.get("builtin") == "checker"
        for attr, color in zip(("rgb1", "rgb2"), linear_colors):
            assert funcs.parse_float_list(texture.get(attr)) == pytest.approx(funcs.linear_to_srgb(color), abs=1e-5)
        assert asset.find("material/layer").get("texture") == texture.get("name")

    def test_anonymous_body_does_not_hide_named_descendants(self):
        root = ET.fromstring('<mujoco><worldbody><body><body name="visible" /></body></worldbody></mujoco>')

        assert load.parse_link_name(bpy.context, root)["visible"] == "visible"

    def test_inline_mesh_preserves_concave_vertices(self):
        collection = bpy.data.collections.new("InlineMeshes")
        bpy.context.scene.collection.children.link(collection)
        objects = {}
        attrs = {
            "name": "concave",
            "vertex": "0 0 0 2 0 0 2 2 0 1 1 0 0 2 0",
            "face": "0 1 3 1 2 3 0 3 4",
        }

        load.import_mesh(bpy.context, lambda *_: None, attrs, objects, Path(), collection)

        mesh = objects["concave"].data
        assert len(mesh.vertices) == 5
        assert tuple(mesh.vertices[3].co) == pytest.approx((1.0, 1.0, 0.0))

    def test_xyaxes_keeps_independent_y_axis(self, registered_props):
        obj = bpy.data.objects.new("xyaxes", None)
        bpy.context.collection.objects.link(obj)

        load.set_local_transform(obj, {"xyaxes": "1 0 0 0 1 0"})

        assert tuple(obj.matrix_local.col[0][:3]) == pytest.approx((1, 0, 0))
        assert tuple(obj.matrix_local.col[1][:3]) == pytest.approx((0, 1, 0))
        assert tuple(obj.matrix_local.col[2][:3]) == pytest.approx((0, 0, 1))

    @pytest.mark.parametrize(
        ("attrs", "expected_type", "expected_fovy"),
        [
            ({"name": "perspective", "fovy": "45"}, cons.CameraTypes.PERSPECTIVE, 45.0),
            (
                {"name": "orthographic", "orthographic": "true", "fovy": "10"},
                cons.CameraTypes.ORTHOGRAPHIC,
                10.0,
            ),
        ],
    )
    def test_camera_fovy_roundtrip(self, registered_ops, attrs, expected_type, expected_fovy):
        load.add_camera(bpy.context, lambda *_: None, bpy.context.collection, {}, attrs.copy())
        camera = bpy.context.active_object

        assert camera.Forge_Camera.type == expected_type
        if expected_type == cons.CameraTypes.PERSPECTIVE:
            assert degrees(camera.data.angle_y) == pytest.approx(expected_fovy)
        else:
            assert camera.data.ortho_scale == pytest.approx(expected_fovy)

        parent = ET.Element("worldbody")
        out.set_camera_tags(parent, camera)
        exported = parent.find("camera")
        assert exported is not None
        assert float(exported.get("fovy")) == pytest.approx(expected_fovy)

    def test_unsupported_equality_is_skipped_with_warning(self, registered_props):
        messages = []

        result = load.add_equality(
            bpy.context,
            lambda level, message: messages.append((level, message)),
            ET.fromstring('<tendon name="unsupported" tendon1="a" tendon2="b" />'),
            {},
        )

        assert result is None
        assert messages == [({"WARNING"}, "Unsupported equality type 'tendon'; element skipped")]

    @pytest.mark.parametrize(
        "xml",
        [
            '<connect name="world-connect" body1="body" anchor="0 0 0" />',
            '<weld name="world-weld" body1="body" />',
            '<joint name="fixed-joint" joint1="joint" />',
        ],
    )
    def test_equality_allows_optional_second_target(self, registered_props, monkeypatch, xml):
        body = bpy.data.objects.new("body", None)
        body.Forge_Model_Type = cons.ModelTypes.LINK
        bpy.context.collection.objects.link(body)
        joint = bpy.data.objects.new("joint", None)
        joint.Forge_Model_Type = cons.ModelTypes.JOINT
        bpy.context.collection.objects.link(joint)
        equality = bpy.data.objects.new("equality", None)
        equality.Forge_Model_Type = cons.ModelTypes.EQUALITY
        bpy.context.collection.objects.link(equality)
        captured = {}

        def fake_add_equality(_context, _report, _collection, equality_type, targets):
            captured["type"] = equality_type
            captured["targets"] = targets
            equality.Forge_Equality.type = equality_type
            equality.Forge_Equality.target1 = targets[0]
            equality.Forge_Equality.target2 = targets[1] if len(targets) > 1 else None
            equality.Forge_Equality.target_type = targets[0].Forge_Model_Type
            return equality

        monkeypatch.setattr(load.funcs, "add_equality", fake_add_equality)

        result = load.add_equality(bpy.context, lambda *_: None, ET.fromstring(xml), {})

        assert result is None
        assert len(captured["targets"]) == 1
        assert equality.Forge_Equality.target2 is None

    def test_frame_sensor_rejects_joint_reference(self, registered_props):
        sensor = bpy.data.objects.new("sensor", None)
        sensor.Forge_Model_Type = cons.ModelTypes.SENSOR
        bpy.context.collection.objects.link(sensor)
        joint = bpy.data.objects.new("joint", None)
        joint.Forge_Model_Type = cons.ModelTypes.JOINT
        bpy.context.collection.objects.link(joint)

        sensor.Forge_Sensor.type = cons.SensorTypes.Framepos

        assert sensor.Forge_Sensor.ref_poll(joint) is False

    def test_spot_light_zero_cutoff_does_not_divide_by_zero(self, registered_props):
        collection = bpy.data.collections.new("Lights")
        bpy.context.scene.collection.children.link(collection)

        load.add_light(
            bpy.context,
            lambda *_: None,
            collection,
            {},
            {"name": "zero", "type": "spot", "cutoff": "0", "innerangle": "0"},
        )

        assert bpy.context.active_object.name == "zero"

    def test_tendon_joint_coefficients_are_imported(self, registered_props, monkeypatch):
        targets = []
        for name in ("joint_a", "joint_b"):
            obj = bpy.data.objects.new(name, None)
            bpy.context.collection.objects.link(obj)
            obj.Forge_Model_Type = cons.ModelTypes.JOINT
            targets.append(obj)

        tendon = bpy.data.objects.new("tendon", None)
        bpy.context.collection.objects.link(tendon)
        tendon.Forge_Model_Type = cons.ModelTypes.TENDON
        for target in targets:
            item = tendon.Forge_Tendon.targets.items.add()
            item.target = target
        monkeypatch.setattr(load.funcs, "add_tendon", lambda *_args: tendon)
        element = ET.fromstring(
            '<fixed name="path"><joint joint="joint_a" coef="0.25" /><joint joint="joint_b" coef="0.75" /></fixed>'
        )

        load.add_tendon(bpy.context, lambda *_: None, element, {}, prefix="")

        assert [item.coef for item in tendon.Forge_Tendon.targets.items] == pytest.approx([0.25, 0.75])

    def test_collider_fromto_keeps_start_to_end_direction(self, registered_props, monkeypatch):
        obj = bpy.data.objects.new("capsule", None)
        bpy.context.collection.objects.link(obj)
        axes = []
        monkeypatch.setattr(load.funcs, "add_collider", lambda *_args: obj)
        monkeypatch.setattr(load.funcs, "set_collider_size", lambda *_args: None)
        monkeypatch.setattr(load, "set_local_matrix", lambda _obj, axis: axes.append(axis.copy()))

        load.add_collider(
            bpy.context,
            lambda *_: None,
            bpy.context.collection,
            None,
            {"name": "capsule", "fromto": "0 0 0 2 0 0", "size": "0.2"},
            cons.GeometryTypes.CAPSULE,
        )

        assert tuple(axes[0]) == pytest.approx((1.0, 0.0, 0.0))
        assert tuple(obj.location) == pytest.approx((1.0, 0.0, 0.0))

    def test_default_class_inheritance_is_resolved(self):
        """Nested MJCF defaults inherit root and parent-class attributes."""
        defaults = {}
        root = ET.fromstring(
            """<default>
                <geom rgba=\"1 0 0 1\" contype=\"1\" />
                <default class=\"parent\">
                    <geom size=\"0.25\" contype=\"2\" />
                    <default class=\"child\"><geom friction=\"0.5 0.1 0.01\" /></default>
                </default>
            </default>"""
        )
        load.get_default(root, defaults)
        load.parse_defaults(defaults)

        attrs = {"class": "child"}
        load.parse_inherit_attrs(defaults, attrs, "geom", "child", recursive=True)
        assert attrs["friction"] == "0.5 0.1 0.01"
        assert attrs["size"] == "0.25"
        assert attrs["contype"] == "2"
        assert attrs["rgba"] == "1 0 0 1"

    def test_global_option_and_visual_sections_parse(self, registered_ops):
        """Section parsers populate typed Blender property groups from XML."""
        context = bpy.context
        load.get_compiler(
            context, ET.fromstring('<compiler angle="radian" eulerseq="zyx" autolimits="false" assetdir="assets" />')
        )
        compiler = context.scene.Forge_GlobalConfig.g_compiler
        assert compiler.angle == "RADIAN"
        assert compiler.eulerseq == "ZYX"
        assert compiler.autolimits is False
        assert compiler.assetdir == "assets"

        load.get_option(
            context,
            ET.fromstring('<option timestep="0.01" gravity="0 0 -3" iterations="12"><flag contact="false" /></option>'),
        )
        option = context.scene.Forge_GlobalConfig.g_option
        assert option.timestep == pytest.approx(0.01)
        assert tuple(option.gravity) == pytest.approx((0.0, 0.0, -3.0))
        assert option.iterations == 12
        assert option.flag.contact is False

        load.get_statistic(context, ET.fromstring('<statistic extent="4.5" center="1 2 3" />'))
        statistic = context.scene.Forge_GlobalConfig.g_statistic
        assert statistic.extent == pytest.approx(4.5)
        assert tuple(statistic.center) == pytest.approx((1.0, 2.0, 3.0))

        load.get_visual(context, ET.fromstring('<global orthographic="true" fovy="45" azimuth="90" elevation="-30" />'))
        visual = context.scene.Forge_VisualConfig.v_global
        assert visual.orthographic is True
        assert visual.fovy == pytest.approx(0.785398, rel=1e-5)

    def test_headlight_active_round_trips_as_a_boolean(self, registered_props):
        """An enabled headlight survives export → import.

        The exporter writes ``active="1"`` but the importer parsed the attribute
        with ``get_active``, which only recognised ``"true"`` — so re-importing a
        model silently switched the headlight back off."""
        context = bpy.context
        visual_config = context.scene.Forge_VisualConfig
        visual_config.reset()
        visual_config.v_headlight.active = True

        mujoco = ET.Element("mujoco")
        out.add_visual(context, mujoco)
        element = mujoco.find(".//headlight")
        assert element.get("active") == "1"

        visual_config.reset()
        load.get_visual(context, element)
        assert visual_config.v_headlight.active is True

        # A file from elsewhere may spell the same flag the long way.
        visual_config.reset()
        load.get_visual(context, ET.fromstring('<headlight active="true" />'))
        assert visual_config.v_headlight.active is True

    def test_frame_sensor_import_preserves_reference_type(self, registered_ops):
        """MJCF reftype is imported independently from objtype."""
        context = bpy.context
        with headless_shape_modifiers():
            bpy.ops.forge.create_link()
            link = context.active_object
            bpy.ops.object.select_all(action="DESELECT")
            link.select_set(True)
            context.view_layer.objects.active = link
            bpy.ops.forge.create_site(site_type="SPHERE")
            site = context.active_object

            messages = []
            element = ET.fromstring(
                f'<framepos name="mixed_ref" objtype="body" objname="{link.name}" '
                f'reftype="site" refname="{site.name}" />'
            )
            load.add_sensor(context, collector(messages), element, None, "")

        sensor = next(obj for obj in _objects_of_type(cons.ModelTypes.SENSOR) if obj.name == "mixed_ref")
        assert sensor.Forge_Sensor.target is link
        assert sensor.Forge_Sensor.target_type == cons.SensorTargetTypes.BODY
        assert sensor.Forge_Sensor.ref is site
        assert sensor.Forge_Sensor.ref_type == cons.SensorTargetTypes.SITE

    def test_file_mesh_loaders_are_cleaned_after_import(self, registered_ops, tmp_path):
        """File-based ``<mesh>`` assets import as placeholder objects.  After the import
        completes, the loaders whose mesh was shared with a geom are removed, while an
        unreferenced asset keeps its carrier (its only data holder)."""
        # run_import bypasses import_init, so reset the shared compiler config
        # (e.g. an assetdir left over from another test would redirect the mesh
        # folder and silently skip the asset).
        bpy.context.scene.Forge_GlobalConfig.reset()
        (tmp_path / "box.obj").write_text("v 0 0 0\nv 1 0 0\nv 1 1 0\nv 0 1 0\nf 1 2 3\nf 1 3 4\n", encoding="utf-8")
        (tmp_path / "spare.obj").write_text("v 0 0 0\nv 1 0 0\nv 0 1 0\nf 1 2 3\n", encoding="utf-8")
        filepath = tmp_path / "model.xml"
        filepath.write_text(
            "<mujoco>"
            '<compiler meshdir="." />'
            "<asset>"
            '<mesh name="box" file="box.obj" />'
            '<mesh name="spare" file="spare.obj" />'
            "</asset>"
            "<worldbody>"
            '<body name="body"><geom name="g" type="mesh" mesh="box" /></body>'
            "</worldbody>"
            "</mujoco>",
            encoding="utf-8",
        )

        import_messages = run_import(bpy.context, str(filepath))
        errors = [m for kind, m in import_messages if "ERROR" in kind]
        assert errors == []

        geoms = _objects_of_type(cons.ModelTypes.VISUAL)
        assert len(geoms) == 1
        assert geoms[0].data.users == 2  # geom + its loader share the mesh
        assert {obj.name for obj in bpy.data.objects if obj.name.endswith(".obj")} == {"box.obj", "spare.obj"}

        removed = load.cleanup_mesh_asset_loaders()

        assert removed == ["box.obj"]
        assert [obj.name for obj in bpy.data.objects if obj.name.endswith(".obj")] == ["spare.obj"]
        assert geoms[0].data.users == 1
        assert len(geoms[0].data.vertices) == 4

    def test_roundtrip_export_import(self, registered_ops, tmp_path):
        """Export → import reconstructs the scene; a re-export matches the original XML."""
        context = bpy.context
        # The Forge config lives on the shared Scene, so a value another test set
        # earlier (e.g. an enabled headlight) would otherwise decide how much of
        # the <visual> section this roundtrip actually exercises. Pin it, and turn
        # the headlight on so the section is never emitted empty.
        context.scene.Forge_VisualConfig.reset()
        context.scene.Forge_VisualConfig.v_headlight.active = True
        build_scene(context)
        filepath = tmp_path / "robot.xml"
        run_export(context, str(filepath))
        original_root = ET.parse(filepath).getroot()

        # ── import the exported file (the operator clears the scene first) ──
        for obj in list(bpy.data.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
        for coll in list(bpy.data.collections):
            bpy.data.collections.remove(coll)
        import_messages = run_import(context, str(filepath))
        errors = [m for kind, m in import_messages if "ERROR" in kind]
        assert errors == []

        links = _objects_of_type(cons.ModelTypes.LINK)
        assert len(links) == 2
        root_link = next(obj for obj in links if obj.parent is None)
        child_link = next(obj for obj in links if obj.parent is root_link)
        assert child_link.location.z == pytest.approx(1.0)
        # The importer places parentless elements in the World collection.
        assert cons.CollectionNames.WORLD in root_link.users_collection[0].name or any(
            coll.name == cons.CollectionNames.WORLD for coll in root_link.users_collection
        )

        joints = _objects_of_type(cons.ModelTypes.JOINT)
        assert len(joints) == 1
        joint = joints[0]
        assert joint.parent is child_link
        assert joint.Forge_Joint.type == cons.JointTypes.HINGE

        actuators = _objects_of_type(cons.ModelTypes.ACTUATOR)
        assert len(actuators) == 1
        assert actuators[0].Forge_Actuator.type == cons.ActuatorTypes.POSITION
        assert actuators[0].Forge_Actuator.target is joint

        sensors = _objects_of_type(cons.ModelTypes.SENSOR)
        assert len(sensors) == 1
        assert sensors[0].Forge_Sensor.type == cons.SensorTypes.Jointpos
        assert sensors[0].Forge_Sensor.target is joint

        equalities = _objects_of_type(cons.ModelTypes.EQUALITY)
        assert len(equalities) == 1
        assert equalities[0].Forge_Equality.type == cons.EqualityTypes.WELD
        assert equalities[0].Forge_Equality.target1 is root_link
        assert equalities[0].Forge_Equality.target2 is child_link

        contacts = _objects_of_type(cons.ModelTypes.CONTACT)
        assert len(contacts) == 1
        assert contacts[0].Forge_Contact.type == cons.ContactTypes.EXCLUDE

        assert len(_objects_of_type(cons.ModelTypes.LIGHT)) == 1
        assert len(_objects_of_type(cons.ModelTypes.CAMERA)) == 1

        visuals = _objects_of_type(cons.ModelTypes.VISUAL)
        assert len(visuals) == 1
        assert visuals[0].Forge_Geometry.type == cons.GeometryTypes.SPHERE

        # The asset material was imported.
        assert "template" in bpy.data.materials

        # ── re-export the imported scene and compare structure ──
        attach_shape_modifier(visuals[0], cons.GeometryShapeModifiers[cons.GeometryTypes.SPHERE])
        filepath2 = tmp_path / "robot2.xml"
        run_export(context, str(filepath2))
        reexported_root = ET.parse(filepath2).getroot()

        def structure(root):
            """Structural summary: (tag, name, sorted attribute keys) per element, depth-first."""
            return [
                (elem.tag, elem.get("name"), tuple(sorted(elem.attrib))) for elem in root.iter() if elem.tag != "mujoco"
            ]

        # Same element tree with the same attribute sets (values may round floats).
        assert structure(reexported_root) == structure(original_root)
