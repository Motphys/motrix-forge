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

"""End-to-end MJCF export tests.

Builds a scene through the ``funcs.add_*`` creation API and runs it through
the export pipeline — the same ``out.*`` / ``funcs.find_assets`` sequence the
``Forge_OT_Export`` operator drives via its modal task queue (the modal timer
loop itself has no event loop in background mode and is not covered here).
The exported MJCF XML structure is then asserted element by element.
"""

import xml.etree.ElementTree as ET

import bmesh
import bpy
import pytest
from Forge.core import constants as cons
from Forge.core import function as funcs
from Forge.core.common import set_modifier_socket
from Forge.ops import exports as out

from .mjcf_helpers import SHAPES_BLEND, attach_shape_modifier, build_scene, headless_shape_modifiers, run_export


@pytest.fixture(autouse=True)
def require_shapes_asset():
    """Fail loudly when the checked-in shape library is missing."""
    if not SHAPES_BLEND.exists():
        pytest.fail("Shapes.blend asset library is required for export tests")


class TestExportMjcf:
    @pytest.mark.parametrize(
        ("rgba", "expected"),
        [
            ((-0.2, 0.4, 1.2, -0.1), (0.0, 0.4, 1.0, 0.0)),
            ((0.0, 1.0, 0.5, 1.0), (0.0, 1.0, 0.5, 1.0)),
            ((2.0, 3.0, 4.0, 1.5), (1.0, 1.0, 1.0, 1.0)),
        ],
    )
    def test_material_rgba_is_clamped_without_changing_emission_or_source(self, rgba, expected):
        material = {
            cons.NodeInputName.COLOR: rgba,
            cons.NodeInputName.ROUGHNESS: 0.5,
            cons.NodeInputName.METALLIC: 0.0,
            cons.NodeInputName.EMISSION: (2.0, 3.0, 4.0),
            cons.NodeInputName.EMISSIONST: 10.0,
        }
        for tag in [
            cons.ShaderPropName.COLORTEX,
            cons.ShaderPropName.ALPHATEX,
            cons.ShaderPropName.NORMALTEX,
            cons.ShaderPropName.ROUGHNESSTEX,
            cons.ShaderPropName.METALLICTEX,
            cons.ShaderPropName.EMISSIONTEX,
        ]:
            material[tag] = [None, None, None]
        root = ET.Element("asset")

        out.set_material_tags(root, "test_material", material)

        element = root.find("material")
        assert [float(value) for value in element.get("rgba").split()] == pytest.approx(expected)
        assert [float(value) for value in element.get("emission").split()] == [2.0, 3.0, 4.0]
        assert float(element.get("emissionintensity")) == 10.0
        assert material[cons.NodeInputName.COLOR] == rgba

    @pytest.mark.parametrize(
        ("equality_type", "target_type", "target_attribute"),
        [
            (cons.EqualityTypes.CONNECT, cons.EqualityTargetTypes.LINK, "body1"),
            (cons.EqualityTypes.WELD, cons.EqualityTargetTypes.LINK, "body1"),
            (cons.EqualityTypes.JOINT, cons.EqualityTargetTypes.JOINT, "joint1"),
        ],
    )
    def test_export_equality_omits_optional_second_target(
        self, registered_props, equality_type, target_type, target_attribute
    ):
        target = bpy.data.objects.new("target", None)
        target.Forge_Model_Type = target_type
        bpy.context.collection.objects.link(target)
        equality_obj = bpy.data.objects.new("equality", None)
        equality_obj.Forge_Model_Type = cons.ModelTypes.EQUALITY
        equality_obj.Forge_Equality.type = equality_type
        equality_obj.Forge_Equality.target_type = target_type
        equality_obj.Forge_Equality.target1 = target
        equality_obj.Forge_Equality.target2 = None
        collection = bpy.data.collections.new(cons.CollectionNames.EQUALITY)
        bpy.context.scene.collection.children.link(collection)
        collection.objects.link(equality_obj)
        root = ET.Element("mujoco")

        out.add_equality(bpy.context, root, lambda *_: None)

        element = root.find(f"equality/{equality_type.lower()}")
        assert element is not None
        assert element.get(target_attribute) == target.name
        assert element.get(target_attribute[:-1] + "2") is None

    def test_hfield_geom_position_is_object_origin(self, registered_props):
        mesh = bpy.data.meshes.new("terrain")
        obj = bpy.data.objects.new("terrain", mesh)
        bpy.context.collection.objects.link(obj)
        obj.Forge_Model_Type = cons.ModelTypes.HFIELD
        obj.location = (1.0, 2.0, 5.0)
        # Object matrices are evaluated lazily after direct transform writes in
        # background Blender.  Update the view layer before testing the value
        # serialized by the exporter.
        bpy.context.view_layer.update()
        root = ET.Element("worldbody")

        out.set_hfield_tags(root, obj, {obj.name: ("terrain.hfield", obj, "")})

        assert [float(value) for value in root.find("geom").get("pos").split()] == pytest.approx((1.0, 2.0, 5.0))

    def test_hfield_asset_uses_mujoco_image_content_type(self, registered_ops, forge_asset_library):
        bpy.ops.object.select_all(action="DESELECT")
        assert bpy.ops.forge.create_height_field() == {"FINISHED"}
        hfield_obj = bpy.context.active_object
        attach_shape_modifier(hfield_obj, cons.AdditionalShapeModifiers[cons.ModelTypes.HFIELD])
        root = ET.Element("mujoco")

        out.add_asset(
            root,
            {},
            {},
            {hfield_obj.name: ("height.png", None, None)},
            {},
            {},
            lambda *_: None,
        )

        assert root.find("asset/hfield").get("content_type") == "image/vnd.mujoco.hfield"

    def test_export_full_scene(self, registered_ops, tmp_path):
        """A scene built through the creation API exports to well-formed MJCF."""
        context = bpy.context
        objects = build_scene(context)
        filepath = tmp_path / "robot.xml"

        export_messages, root = run_export(context, str(filepath))

        assert filepath.exists()
        assert root.tag == "mujoco"
        # No export errors reported (warnings about template materials are fine).
        errors = [m for kind, m in export_messages if "ERROR" in kind]
        assert errors == []

        # ── worldbody tree ──
        worldbody = root.find("worldbody")
        assert worldbody is not None
        bodies = worldbody.findall("body")
        assert [b.get("name") for b in bodies] == [objects["root"].name]

        root_body = bodies[0]
        # Parentless lights and cameras export at worldbody level.
        light = worldbody.find("light")
        assert light is not None
        # The light shape must be expressed only through `type`; the
        # deprecated `directional` attribute conflicts with it in the MuJoCo
        # schema ("at most one of 'directional', 'type' can be specified").
        assert light.get("type") == "directional"
        assert "directional" not in light.attrib
        assert worldbody.find("camera") is not None

        child_bodies = root_body.findall("body")
        assert [b.get("name") for b in child_bodies] == [objects["child"].name]
        child_body = child_bodies[0]
        assert [float(v) for v in child_body.get("pos").split()] == pytest.approx([0.0, 0.0, 1.0])

        # Joint parented under the child link.
        joint = child_body.find("joint")
        assert joint is not None
        assert joint.get("name") == objects["joint"].name
        assert joint.get("type") == "hinge"
        assert joint.get("axis") == "0.0 0.0 1.0"

        # Visual geom inside the child link, resolved to the template material.
        geom = child_body.find("geom")
        assert geom is not None
        assert geom.get("type") == "sphere"
        assert geom.get("material") == "template"

        # ── actuator ──
        actuator = root.find("actuator/position")
        assert actuator is not None
        assert actuator.get("name") == objects["actuator"].name
        assert actuator.get("joint") == objects["joint"].name

        # ── sensor ──
        sensor = root.find("sensor/jointpos")
        assert sensor is not None
        assert sensor.get("name") == objects["sensor"].name
        assert sensor.get("joint") == objects["joint"].name

        # ── equality (weld between the two links) ──
        equality = root.find("equality/weld")
        assert equality is not None
        assert equality.get("name") == objects["equality"].name
        assert equality.get("body1") == objects["root"].name
        assert equality.get("body2") == objects["child"].name

        # ── contact (exclude between the two links) ──
        exclude = root.find("contact/exclude")
        assert exclude is not None
        assert exclude.get("body1") == objects["root"].name
        assert exclude.get("body2") == objects["child"].name

        # ── assets (template material registered) ──
        material = root.find("asset/material")
        assert material is not None
        assert material.get("name") == "template"

    def test_export_reports_for_empty_scene(self, registered_props, tmp_path):
        """Exporting a scene with no exportable objects still writes XML and reports."""
        context = bpy.context
        filepath = tmp_path / "empty.xml"

        messages, root = run_export(context, str(filepath))

        assert filepath.exists()
        assert root.tag == "mujoco"
        # Without a World collection set_world refuses to export anything.
        assert any("Not find World collection" in m for _, m in messages)

    def test_export_skips_empty_mesh_visual_with_warning(self, registered_props, tmp_path):
        """An empty mesh is omitted from assets and worldbody without failing export."""
        world = bpy.data.collections.new(cons.CollectionNames.WORLD)
        bpy.context.scene.collection.children.link(world)

        empty_mesh = bpy.data.meshes.new("empty_mesh")
        visual = bpy.data.objects.new("empty_visual", empty_mesh)
        world.objects.link(visual)
        visual.Forge_Model_Type = cons.ModelTypes.VISUAL
        visual.Forge_Geometry.type = cons.GeometryTypes.MESH

        link = bpy.data.objects.new("empty_link", None)
        world.objects.link(link)
        link.Forge_Model_Type = cons.ModelTypes.LINK
        nested_mesh = bpy.data.meshes.new("nested_empty_mesh")
        nested_visual = bpy.data.objects.new("nested_empty_visual", nested_mesh)
        world.objects.link(nested_visual)
        nested_visual.parent = link
        nested_visual.Forge_Model_Type = cons.ModelTypes.VISUAL
        nested_visual.Forge_Geometry.type = cons.GeometryTypes.MESH

        filepath = tmp_path / "empty-mesh.xml"
        messages, root = run_export(bpy.context, str(filepath))

        assert filepath.exists()
        assert any("empty_visual" in message and "exclude for export" in message for _, message in messages)
        assert any("nested_empty_visual" in message and "exclude for export" in message for _, message in messages)
        assert not root.findall(".//geom")
        assert not root.findall("asset/mesh")

    def test_export_keeps_mesh_collider_with_modifier_hull(self, registered_props, tmp_path):
        """A mesh collider whose hull lives in Collider_Convex is exported, not skipped as empty.

        ``create_collider`` stores the hull in the node group and leaves the collider's
        datablock empty, so its base mesh always looks like zero triangles.
        """
        world = bpy.data.collections.new(cons.CollectionNames.WORLD)
        bpy.context.scene.collection.children.link(world)

        link = bpy.data.objects.new("hull_link", None)
        world.objects.link(link)
        link.Forge_Model_Type = cons.ModelTypes.LINK

        source_mesh = bpy.data.meshes.new("hull_source")
        bm = bmesh.new()
        bmesh.ops.create_cube(bm, size=0.4)
        bm.to_mesh(source_mesh)
        bm.free()
        source = bpy.data.objects.new("hull_source", source_mesh)
        world.objects.link(source)
        source.parent = link
        source.Forge_Model_Type = cons.ModelTypes.VISUAL
        source.Forge_Geometry.type = cons.GeometryTypes.BOX

        collider = bpy.data.objects.new("hull_collider", bpy.data.meshes.new("hull_collider"))
        world.objects.link(collider)
        collider.parent = link
        collider.Forge_Model_Type = cons.ModelTypes.COLLIDER
        collider.Forge_Geometry.type = cons.GeometryTypes.MESH
        modifier_name = cons.ColliderShapeModifiers[cons.GeometryTypes.MESH]
        attach_shape_modifier(collider, modifier_name)
        # Same wiring ``create_collider`` performs: point the hull at the source visual.
        funcs.set_collider_size_by_ref(collider, cons.GeometryTypes.MESH, source)

        assert not collider.data.vertices, "the hull must live in the modifier, not the datablock"
        assert funcs.has_exportable_mesh(collider) is True

        filepath = tmp_path / "mesh-collider.xml"
        messages, root = run_export(bpy.context, str(filepath))

        geom = root.find(".//geom[@name='hull_collider']")
        assert geom is not None, [message for _, message in messages]
        assert geom.get("type") == "mesh"
        assert geom.get("mesh") == "hull_collider"
        assert root.find("asset/mesh[@name='hull_collider']") is not None

        # Close the loop: the STL the export operator writes must have the hull in it.
        funcs.export_collider(collider, str(tmp_path), False)
        stl = tmp_path / "hull_collider.stl"
        assert stl.exists() and stl.stat().st_size > 0

    def test_export_site_and_collider_geometry(self, registered_ops, tmp_path):
        """Site and collider elements are emitted in addition to visual geoms."""
        with headless_shape_modifiers():
            bpy.ops.forge.create_link()
            link = bpy.context.active_object
            bpy.ops.forge.create_geometry(geometry_type="SPHERE")
            visual = bpy.context.active_object
            attach_shape_modifier(visual, cons.GeometryShapeModifiers[cons.GeometryTypes.SPHERE])

            bpy.ops.object.select_all(action="DESELECT")
            link.select_set(True)
            bpy.context.view_layer.objects.active = link
            bpy.ops.forge.create_site(site_type="SPHERE")
            site = bpy.context.active_object
            attach_shape_modifier(site, cons.SiteShapeModifiers[cons.GeometryTypes.SPHERE])

            bpy.ops.object.select_all(action="DESELECT")
            link.select_set(True)
            bpy.context.view_layer.objects.active = link
            bpy.ops.forge.create_collider(collider_type="BOX", create_method="COLLIDER_TYPE")
            collider = bpy.context.active_object
            attach_shape_modifier(collider, cons.ColliderShapeModifiers[cons.GeometryTypes.BOX])

        filepath = tmp_path / "site-collider.xml"
        _messages, root = run_export(bpy.context, str(filepath))

        assert root.find(".//site") is not None
        geoms = root.findall(".//geom")
        assert any(g.get("type") == "sphere" for g in geoms)
        assert any(g.get("type") == "box" for g in geoms)

    def test_replicate_export_reads_modifier_socket_values(self, registered_ops):
        with headless_shape_modifiers():
            bpy.ops.forge.create_link()
            link = bpy.context.active_object
            assert bpy.ops.forge.create_replicate(count=2, offset=(1.0, 0.0, 0.0)) == {"FINISHED"}
            replicate = bpy.context.active_object
            attach_shape_modifier(replicate, cons.AdditionalShapeModifiers[cons.ModelTypes.REPLICATE])

        modifier = replicate.modifiers[cons.AdditionalShapeModifiers[cons.ModelTypes.REPLICATE]]
        set_modifier_socket(modifier, "Socket_0", 3)
        set_modifier_socket(modifier, "Socket_2", (1.0, 2.0, 3.0))
        set_modifier_socket(modifier, "Socket_3", (0.0, 0.0, 0.0))
        root = ET.Element("worldbody")

        out.set_multi_body(bpy.context, root, replicate, {}, {}, {})

        element = root.find("replicate")
        assert element is not None
        assert element.get("count") == "3"
        assert element.get("offset") == "1.0 2.0 3.0"
        assert element.find("body").get("name") == link.name

    def test_export_tendon_element(self, registered_ops, tmp_path):
        """A fixed tendon with multiple joints is serialized under <tendon>."""
        with headless_shape_modifiers():
            bpy.ops.forge.create_link()
            link = bpy.context.active_object
            bpy.ops.forge.create_joint(joint_type="HINGE")
            first = bpy.context.active_object
            bpy.ops.object.select_all(action="DESELECT")
            link.select_set(True)
            bpy.context.view_layer.objects.active = link
            bpy.ops.forge.create_joint(joint_type="SLIDE")
            second = bpy.context.active_object

            bpy.ops.object.select_all(action="DESELECT")
            first.select_set(True)
            first["selected_order"] = 0
            second.select_set(True)
            second["selected_order"] = 1
            bpy.context.view_layer.objects.active = second
            bpy.ops.forge.create_tendon(tendon_type="FIXED")
            tendon = bpy.context.active_object
            tendon.Forge_Tendon.targets.items[0].coef = 0.25
            tendon.Forge_Tendon.targets.items[1].coef = 0.75

        filepath = tmp_path / "tendon.xml"
        _messages, root = run_export(bpy.context, str(filepath))

        fixed = root.find("tendon/fixed")
        assert fixed is not None
        assert [j.get("joint") for j in fixed.findall("joint")] == [first.name, second.name]
        assert [float(j.get("coef")) for j in fixed.findall("joint")] == pytest.approx([0.25, 0.75])

    def test_export_frame_sensor_uses_independent_reference_type(self, registered_ops, tmp_path):
        """Frame sensors export reftype from the reference object, not the target type."""
        with headless_shape_modifiers():
            bpy.ops.forge.create_link()
            link = bpy.context.active_object

            bpy.ops.object.select_all(action="DESELECT")
            link.select_set(True)
            bpy.context.view_layer.objects.active = link
            bpy.ops.forge.create_site(site_type="SPHERE")
            site = bpy.context.active_object
            attach_shape_modifier(site, cons.SiteShapeModifiers[cons.GeometryTypes.SPHERE])

            bpy.ops.object.select_all(action="DESELECT")
            link.select_set(True)
            link["selected_order"] = 0
            site.select_set(True)
            site["selected_order"] = 1
            bpy.context.view_layer.objects.active = link
            assert bpy.ops.forge.create_sensor(Sensor_Type="Framepos", set_ref=True) == {"FINISHED"}
            sensor = bpy.context.active_object

        assert sensor.Forge_Sensor.target_type == cons.SensorTargetTypes.BODY
        assert sensor.Forge_Sensor.ref_type == cons.SensorTargetTypes.SITE

        filepath = tmp_path / "frame-sensor.xml"
        _messages, root = run_export(bpy.context, str(filepath))
        element = root.find("sensor/framepos")
        assert element is not None
        assert element.get("objtype") == "body"
        assert element.get("reftype") == "site"
        assert element.get("objname") == link.name
        assert element.get("refname") == site.name


class TestInstanceExport:
    """Links marked with INSTANCE_IDNAME export a copy of the template subtree."""

    def _select_only(self, context, ordered):
        bpy.ops.object.select_all(action="DESELECT")
        for index, obj in enumerate(ordered):
            obj["selected_order"] = index
            obj.select_set(True)
        context.view_layer.objects.active = ordered[0]

    def _build_scene(self, context):
        """Robot root + gripper template (joint, visual, child link with site) + two arm links."""
        objects = {}
        with headless_shape_modifiers():
            bpy.ops.forge.create_link()
            objects["robot"] = context.active_object
            bpy.ops.forge.mark_root_link()

            # Deselect so the template becomes a true root link, parked at
            # world level (the recommended instance-link placement).
            bpy.ops.object.select_all(action="DESELECT")
            bpy.ops.forge.create_link()
            objects["template"] = context.active_object

            self._select_only(context, [objects["template"]])
            bpy.ops.forge.create_joint(joint_type="HINGE")
            objects["template_joint"] = context.active_object

            self._select_only(context, [objects["template"]])
            bpy.ops.forge.create_geometry(geometry_type="SPHERE")
            objects["template_visual"] = context.active_object
            attach_shape_modifier(objects["template_visual"], cons.GeometryShapeModifiers[cons.GeometryTypes.SPHERE])

            self._select_only(context, [objects["template"]])
            bpy.ops.forge.create_link()
            objects["template_tip"] = context.active_object

            self._select_only(context, [objects["template_tip"]])
            bpy.ops.forge.create_site(site_type="SPHERE")
            objects["template_site"] = context.active_object
            attach_shape_modifier(objects["template_site"], cons.SiteShapeModifiers[cons.GeometryTypes.SPHERE])

            self._select_only(context, [objects["robot"]])
            bpy.ops.forge.create_link()
            objects["arm_l"] = context.active_object

            self._select_only(context, [objects["robot"]])
            bpy.ops.forge.create_link()
            objects["arm_r"] = context.active_object

        return objects

    def _mark_instances(self, context, template, links):
        """Mark *template* as instance link, then mark links as its instances."""
        self._select_only(context, [template])
        assert bpy.ops.forge.mark_instance_link() == {"FINISHED"}
        props = bpy.data.scenes[context.scene.Main_Scene].Forge_Props
        props.instance_body = template
        for link in links:
            self._select_only(context, [link])
            assert bpy.ops.forge.set_instance_idname() == {"FINISHED"}
        props.instance_body = None

    def _warning_messages(self, messages):
        return [message for kinds, message in messages if any("WARNING" in kind for kind in kinds)]

    def test_instance_subtree_copied_under_each_instance(self, registered_ops, tmp_path):
        """Each instance link exports the template subtree with its own name prefix."""
        context = bpy.context
        objects = self._build_scene(context)
        self._mark_instances(context, objects["template"], [objects["arm_l"], objects["arm_r"]])

        _messages, root = run_export(context, str(tmp_path / "instance.xml"))

        worldbody = root.find("worldbody")
        # The template link itself is not exported anywhere, even unprefixed.
        assert worldbody.find(f".//body[@name='{objects['template'].name}']") is None
        assert root.find(f".//joint[@name='{objects['template_joint'].name}']") is None

        for arm in (objects["arm_l"], objects["arm_r"]):
            body = worldbody.find(f".//body[@name='{arm.name}']")
            assert body is not None
            joint = body.find(f"joint[@name='{arm.name}_{objects['template_joint'].name}']")
            assert joint is not None
            assert joint.get("type") == "hinge"
            geom = body.find(f"geom[@name='{arm.name}_{objects['template_visual'].name}']")
            assert geom is not None
            assert geom.get("type") == "sphere"
            tip = body.find(f"body[@name='{arm.name}_{objects['template_tip'].name}']")
            assert tip is not None
            assert tip.find(f"site[@name='{arm.name}_{objects['template_site'].name}']") is not None

        # Shape primitives serialize by type + size — no mesh asset is exported.
        assert root.findall("asset/mesh") == []
        # The referenced marked template still feeds the asset section
        # (its visual's material is resolved for the copies).
        material = root.find("asset/material")
        assert material is not None
        assert material.get("name") == "template"

    def test_instance_own_children_replaced_by_template(self, registered_ops, tmp_path):
        """An instance link's own children are ignored and gather no assets."""
        context = bpy.context
        objects = self._build_scene(context)
        with headless_shape_modifiers():
            self._select_only(context, [objects["arm_l"]])
            bpy.ops.forge.create_geometry(geometry_type="SPHERE")
            own_visual = context.active_object
            attach_shape_modifier(own_visual, cons.GeometryShapeModifiers[cons.GeometryTypes.SPHERE])
        self._mark_instances(context, objects["template"], [objects["arm_l"]])

        _messages, root = run_export(context, str(tmp_path / "instance-own.xml"))

        arm_l = root.find(f".//body[@name='{objects['arm_l'].name}']")
        assert arm_l is not None
        assert arm_l.find(f"geom[@name='{own_visual.name}']") is None
        assert arm_l.find(f"geom[@name='{objects['arm_l'].name}_{own_visual.name}']") is None
        # The template copy is there instead.
        assert arm_l.find(f"geom[@name='{objects['arm_l'].name}_{objects['template_visual'].name}']") is not None
        mesh_names = [mesh.get("name") for mesh in root.findall("asset/mesh")]
        # Shape primitives ship no mesh file, so the ignored own visual adds
        # no asset either.
        assert mesh_names == []

    def test_invalid_instance_marker_exports_link_normally(self, registered_ops, tmp_path):
        """A missing template name warns and falls back to exporting own children."""
        context = bpy.context
        objects = self._build_scene(context)
        with headless_shape_modifiers():
            self._select_only(context, [objects["arm_r"]])
            bpy.ops.forge.create_site(site_type="SPHERE")
            own_site = context.active_object
            attach_shape_modifier(own_site, cons.SiteShapeModifiers[cons.GeometryTypes.SPHERE])
        objects["arm_r"]["INSTANCE_IDNAME"] = "missing"

        messages, root = run_export(context, str(tmp_path / "instance-invalid.xml"))

        assert any("missing" in message and "invalid" in message for message in self._warning_messages(messages))
        arm_r = root.find(f".//body[@name='{objects['arm_r'].name}']")
        assert arm_r is not None
        assert arm_r.find(f"site[@name='{own_site.name}']") is not None
        # No template copy was applied either.
        assert arm_r.find(f"joint[@name='{objects['arm_r'].name}_{objects['template_joint'].name}']") is None

    def test_self_instance_marker_exports_link_normally(self, registered_ops, tmp_path):
        """A self-referencing instance marker warns and exports the link as-is."""
        context = bpy.context
        objects = self._build_scene(context)
        with headless_shape_modifiers():
            self._select_only(context, [objects["arm_l"]])
            bpy.ops.forge.create_site(site_type="SPHERE")
            own_site = context.active_object
            attach_shape_modifier(own_site, cons.SiteShapeModifiers[cons.GeometryTypes.SPHERE])
        objects["arm_l"]["INSTANCE_IDNAME"] = objects["arm_l"].name

        messages, root = run_export(context, str(tmp_path / "instance-self.xml"))

        assert any("invalid" in message for message in self._warning_messages(messages))
        arm_l = root.find(f".//body[@name='{objects['arm_l'].name}']")
        assert arm_l is not None
        assert arm_l.find(f"site[@name='{own_site.name}']") is not None

    def test_marked_instance_link_without_references_exports_nothing(self, registered_ops, tmp_path):
        """An unreferenced INSTANCE_LINK exports neither body nor assets, and warns."""
        context = bpy.context
        objects = self._build_scene(context)
        self._select_only(context, [objects["template"]])
        assert bpy.ops.forge.mark_instance_link() == {"FINISHED"}

        messages, root = run_export(context, str(tmp_path / "instance-unreferenced.xml"))

        assert root.find(f".//body[@name='{objects['template'].name}']") is None
        # Nothing of the subtree is exported — no mesh, no material.
        assert root.findall("asset/mesh") == []
        assert root.find("asset/material") is None
        warnings = self._warning_messages(messages)
        assert any("not referenced" in message for message in warnings)

        # Unmarking restores the link to a normal exported body.
        self._select_only(context, [objects["template"]])
        assert bpy.ops.forge.mark_instance_link() == {"FINISHED"}
        _messages, root = run_export(context, str(tmp_path / "instance-restored.xml"))
        assert root.find(f".//body[@name='{objects['template'].name}']") is not None

    def test_nested_marked_link_inside_template_is_not_copied(self, registered_ops, tmp_path):
        """A marked link nested in the template subtree is never exported as a body."""
        context = bpy.context
        objects = self._build_scene(context)
        # Nest a second marked link inside the template's tip link.
        with headless_shape_modifiers():
            self._select_only(context, [objects["template_tip"]])
            bpy.ops.forge.create_link()
            nested = context.active_object
            bpy.ops.forge.create_site(site_type="SPHERE")
            nested_site = context.active_object
            attach_shape_modifier(nested_site, cons.SiteShapeModifiers[cons.GeometryTypes.SPHERE])
        self._select_only(context, [nested])
        assert bpy.ops.forge.mark_instance_link() == {"FINISHED"}

        self._mark_instances(context, objects["template"], [objects["arm_l"]])
        _messages, root = run_export(context, str(tmp_path / "instance-nested.xml"))

        arm_l = root.find(f".//body[@name='{objects['arm_l'].name}']")
        assert arm_l is not None
        # The copied subtree contains the tip body, but the nested marked
        # link is never exported as a body — its own or a prefixed copy.
        tip = arm_l.find(f"body[@name='{objects['arm_l'].name}_{objects['template_tip'].name}']")
        assert tip is not None
        assert tip.find("body") is None
        assert root.find(f".//body[@name='{nested.name}']") is None
