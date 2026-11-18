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

"""Comprehensive Forge API integration tests — runs against real bpy."""

from unittest.mock import MagicMock

import bpy
import pytest
from Forge.core import constants as cons
from Forge.core import function as funcs
from Forge.core import selection as sel
from Forge.core import serialization as ser
from Forge.core.common import prop_modifier_socket
from Forge.core.geometry_handler import SHAPE_ASSET_IDS, GeometryHandler, add_shape_modifier
from Forge.ops.exports import add_compiler, add_visual, prettify
from Forge.ops.imports import get_data_object, parse_inherit_attrs, set_coll_tag

from .mjcf_helpers import attach_shape_modifier, headless_shape_modifiers

# ═══════════════════════════════════════════════════════════════════
#  1. Core data model
# ═══════════════════════════════════════════════════════════════════


class TestDefines:
    def test_model_type_strings(self):
        assert cons.ModelTypes.LINK == "LINK"
        assert cons.ModelTypes.VISUAL == "VISUAL"
        assert cons.ModelTypes.COLLIDER == "COLLIDER"
        assert cons.ModelTypes.JOINT == "JOINT"

    def test_collection_names_consistency(self):
        # Collection names are written to disk, so pin the literals: the map must
        # carry exactly these, and each CollectionNames member must hold its value.
        expected = {
            cons.ModelTypes.LINK: "Link",
            cons.ModelTypes.INERTIAL: "Inertial",
            cons.ModelTypes.VISUAL: "Visual",
            cons.ModelTypes.COLLIDER: "Collider",
            cons.ModelTypes.JOINT: "Joint",
            cons.ModelTypes.SITE: "Site",
            cons.ModelTypes.ACTUATOR: "Actuator",
            cons.ModelTypes.TENDON: "Tendon",
            cons.ModelTypes.EQUALITY: "Equality",
            cons.ModelTypes.CONTACT: "Contact",
            cons.ModelTypes.SENSOR: "Sensor",
            cons.ModelTypes.LIGHT: "Light",
            cons.ModelTypes.CAMERA: "Camera",
            cons.ModelTypes.FRAME: "Frame",
            cons.ModelTypes.REPLICATE: "Replicate",
            cons.ModelTypes.ATTACH: "Attach",
            cons.ModelTypes.INCLUDE: "Include",
        }
        assert dict(cons.Model_Collection_Names) == expected
        for mt, cn in expected.items():
            assert getattr(cons.CollectionNames, mt.name) == cn

    def test_geometry_group_constants(self):
        assert cons.GeometryGroup.VISUAL == 2
        assert cons.GeometryGroup.COLLIDER == 3

    def test_shape_asset_ids(self):
        for ctx in ("Visual", "Collider", "Site"):
            for shape in ("BOX", "CAPSULE", "CYLINDER", "SPHERE"):
                assert (ctx, shape) in SHAPE_ASSET_IDS
        assert ("Collider", "MESH") in SHAPE_ASSET_IDS


# ═══════════════════════════════════════════════════════════════════
#  2. Property registration
# ═══════════════════════════════════════════════════════════════════


class TestProperties:
    def test_model_type_property(self, registered_props):
        obj = bpy.data.objects.new("T", None)
        assert hasattr(obj, "Forge_Model_Type")
        assert obj.Forge_Model_Type == "UNDEFINED"

    def test_scene_props(self, registered_props):
        assert hasattr(bpy.context.scene, "Forge_Props")
        assert hasattr(bpy.context.scene, "Forge_GlobalConfig")

    def test_object_props(self, registered_props):
        obj = bpy.data.objects.new("T", None)
        for prop in (
            "Forge_Link",
            "Forge_Geometry",
            "Forge_Joint",
            "Forge_Actuator",
            "Forge_Inertial",
            "Forge_Light",
            "Forge_Camera",
            "Forge_Attach",
            "Forge_Replicate",
            "Forge_Include",
            "Forge_Sensor",
            "Forge_Contact",
            "Forge_Tendon",
            "Forge_Equality",
        ):
            assert hasattr(obj, prop), f"Missing {prop}"

    def test_geom_prop_defaults(self, registered_props):
        obj = bpy.data.objects.new("G", None)
        obj.Forge_Model_Type = "VISUAL"
        assert obj.Forge_Geometry.type == "SPHERE"

    def test_export_path_prop(self, registered_props):
        forge = bpy.data.scenes[bpy.context.scene.Main_Scene].Forge_Props
        assert hasattr(forge, "export_path")
        assert hasattr(forge, "import_file_path")
        assert hasattr(forge, "scale_factor")


# ═══════════════════════════════════════════════════════════════════
#  3. Object creation (property-level, no asset modifiers)
# ═══════════════════════════════════════════════════════════════════


class TestObjectCreation:
    """Verify object creation with model-type properties.
    Some tests skip modifier-heavy paths where Shapes.blend isn't loaded.
    """

    def test_create_empty_set_type(self, registered_props):
        bpy.ops.object.empty_add(type="PLAIN_AXES")
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "LINK"
        assert obj.Forge_Model_Type == "LINK"

    def test_create_mesh_set_visual(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "VISUAL"
        obj.Forge_Geometry.type = "BOX"
        assert obj.Forge_Geometry.type == "BOX"

    def test_set_joint_type_property(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "JOINT"
        obj.Forge_Joint.type = "HINGE"
        assert obj.Forge_Joint.type == "HINGE"

    def test_set_actuator_type_property(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "ACTUATOR"
        obj.Forge_Actuator.type = "POSITION"
        assert obj.Forge_Actuator.type == "POSITION"

    def test_joint_props_have_defaults(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "JOINT"
        assert obj.Forge_Joint.stiffness == 0.0
        assert obj.Forge_Joint.damping == 0.0
        assert obj.Forge_Joint.limited == "AUTO"

    def test_geom_props_defaults(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "VISUAL"
        assert obj.Forge_Geometry.condim == 3
        assert obj.Forge_Geometry.contype == 1
        assert obj.Forge_Geometry.density == 1000

    def test_light_props(self, registered_props):
        bpy.ops.object.light_add(type="POINT")
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "LIGHT"
        obj.Forge_Light.type = "POINT"
        obj.Forge_Light.mode = "FIXED"
        assert obj.Forge_Light.type == "POINT"

    def test_camera_props(self, registered_props):
        bpy.ops.object.camera_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "CAMERA"
        obj.Forge_Camera.type = "PERSPECTIVE"
        obj.Forge_Camera.mode = "FIXED"
        assert obj.Forge_Camera.type == "PERSPECTIVE"

    def test_hfield(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "HFIELD"
        assert obj.Forge_Model_Type == "HFIELD"

    def test_plane(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "PLANE"
        assert obj.Forge_Model_Type == "PLANE"

    def test_equality_props(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "EQUALITY"
        obj.Forge_Equality.type = "WELD"
        assert obj.Forge_Equality.type == "WELD"
        assert obj.Forge_Equality.active is True

    def test_sensor_props(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "SENSOR"
        # Sensor type enum expects specific names
        assert hasattr(obj, "Forge_Sensor")
        assert obj.Forge_Sensor.noise == 0.0

    def test_tendon_props(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "TENDON"
        assert obj.Forge_Tendon.stiffness == 0.0

    def test_contact_props(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "CONTACT"
        assert hasattr(obj, "Forge_Contact")

    def test_replicate_props(self, registered_props):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "REPLICATE"
        assert hasattr(obj, "Forge_Replicate")
        assert obj.Forge_Replicate.count == 0

    def test_attach_props(self, registered_props):
        bpy.ops.object.empty_add(type="PLAIN_AXES")
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "ATTACH"
        assert hasattr(obj, "Forge_Attach")
        assert obj.Forge_Attach.prefix == "ATT_"

    def test_include_props(self, registered_props):
        bpy.ops.object.empty_add(type="PLAIN_AXES")
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "INCLUDE"
        assert hasattr(obj, "Forge_Include")
        assert obj.Forge_Include.file == ""

    def test_set_model_type_via_direct_assignment(self, registered_props):
        """Verify all model types can be set."""
        for mt_name in (
            "LINK",
            "VISUAL",
            "COLLIDER",
            "JOINT",
            "SITE",
            "ACTUATOR",
            "INERTIAL",
            "LIGHT",
            "CAMERA",
            "HFIELD",
            "PLANE",
            "FRAME",
            "REPLICATE",
            "ATTACH",
            "INCLUDE",
            "SENSOR",
            "CONTACT",
            "TENDON",
            "EQUALITY",
        ):
            bpy.ops.mesh.primitive_cube_add()
            obj = bpy.context.active_object
            obj.Forge_Model_Type = mt_name
            assert obj.Forge_Model_Type == mt_name, f"Failed for {mt_name}"
            bpy.data.objects.remove(obj, do_unlink=True)


# ═══════════════════════════════════════════════════════════════════
#  4. Selection and poll helpers
# ═══════════════════════════════════════════════════════════════════


class TestSelection:
    def _link_and_select(self, objs):
        """Link objects to scene collection and select them."""
        coll = bpy.context.scene.collection
        for o in objs:
            coll.objects.link(o)
        bpy.ops.object.select_all(action="DESELECT")
        for o in objs:
            o.select_set(True)
        if objs:
            bpy.context.view_layer.objects.active = objs[0]

    def test_check_selected_all_match(self, registered_props):
        obj1 = bpy.data.objects.new("A", None)
        obj2 = bpy.data.objects.new("B", None)
        obj1.Forge_Model_Type = "LINK"
        obj2.Forge_Model_Type = "LINK"
        self._link_and_select([obj1, obj2])
        assert sel.check_selected_model_types(bpy.context, ["LINK"]) is True

    def test_check_selected_mismatch(self, registered_props):
        obj1 = bpy.data.objects.new("A", None)
        obj2 = bpy.data.objects.new("B", None)
        obj1.Forge_Model_Type = "LINK"
        obj2.Forge_Model_Type = "VISUAL"
        self._link_and_select([obj1, obj2])
        assert sel.check_selected_model_types(bpy.context, ["LINK"]) is False

    def test_check_selected_empty(self, registered_props):
        assert sel.check_selected_model_types(bpy.context, ["LINK"]) is False

    def test_get_ordered_selection(self, registered_props):
        """get_ordered_selection matches sorted scene objects by selection_order."""
        # Create objects in scene with deliberate order
        names = ["Third", "First", "Second"]
        for n in names:
            obj = bpy.data.objects.new(n, None)
            bpy.context.scene.collection.objects.link(obj)

        # Select all of them
        bpy.ops.object.select_all(action="DESELECT")
        for i, name in enumerate(["Third", "First", "Second"]):
            if name in bpy.data.objects:
                bpy.data.objects[name].select_set(True)
                bpy.data.objects[name]["selected_order"] = i  # 0=Third, 1=First, 2=Second

        # The addon function should sort by selection_order
        result = sel.get_ordered_selection_objects(bpy.context)
        result_names = [o.name for o in result]

        # Manual sort of same objects by selection_order
        manual = sorted(
            [o for o in bpy.data.objects if o.name in names],
            key=lambda x: x.get("selected_order", -1),
        )
        manual_names = [o.name for o in manual]

        assert result_names == manual_names, f"{result_names} != {manual_names}"
        # Specifically: Third (idx 0) → First (idx 1) → Second (idx 2)
        assert result_names == ["Third", "First", "Second"]

    def test_get_ordered_selection_keeps_untagged_objects(self, registered_props):
        tagged = bpy.data.objects.new("Tagged", None)
        untagged = bpy.data.objects.new("Untagged", None)
        bpy.context.collection.objects.link(tagged)
        bpy.context.collection.objects.link(untagged)
        tagged["selected_order"] = 0
        tagged.select_set(True)
        untagged.select_set(True)

        assert sel.get_ordered_selection_objects(bpy.context) == [tagged, untagged]

    def test_poll_functions(self, registered_props):
        obj = bpy.data.objects.new("T", None)
        obj.Forge_Model_Type = "LINK"
        assert sel.link_only_poll(None, obj) is True
        obj.Forge_Model_Type = "JOINT"
        assert sel.link_only_poll(None, obj) is False
        assert sel.joint_only_poll(None, obj) is True


# ═══════════════════════════════════════════════════════════════════
#  5. Operators  (via bpy.ops.forge.*)
# ═══════════════════════════════════════════════════════════════════


class TestOperators:
    """Call addon operators and verify scene state changes."""

    @pytest.mark.parametrize(
        ("object_type", "expected"),
        [
            ("EMPTY", ["LINK"]),
            ("MESH", ["VISUAL", "COLLIDER"]),
            ("LIGHT", ["LIGHT"]),
            ("CAMERA", ["CAMERA"]),
            ("CURVE", []),
        ],
    )
    def test_undefined_model_type_options(self, registered_ops, object_type, expected):
        from Forge.ops.definition import Forge_OT_Type_Define

        data = {
            "EMPTY": lambda: None,
            "MESH": lambda: bpy.data.meshes.new("Mesh"),
            "LIGHT": lambda: bpy.data.lights.new("Light", "POINT"),
            "CAMERA": lambda: bpy.data.cameras.new("Camera"),
            "CURVE": lambda: bpy.data.curves.new("Curve", "CURVE"),
        }[object_type]()
        obj = bpy.data.objects.new("Untyped", data)
        bpy.context.collection.objects.link(obj)
        obj.select_set(True)
        items = Forge_OT_Type_Define.model_enum_items(None, bpy.context)
        assert [item[0] for item in items] == expected

    @pytest.mark.parametrize("model_type", ["VISUAL", "COLLIDER", "LIGHT", "CAMERA"])
    def test_defined_model_type_only_offers_reset(self, registered_ops, model_type):
        from Forge.ops.definition import Forge_OT_Type_Define

        bpy.ops.mesh.primitive_cube_add()
        bpy.context.active_object.Forge_Model_Type = model_type
        items = Forge_OT_Type_Define.model_enum_items(None, bpy.context)
        assert [item[0] for item in items] == ["UNDEFINED"]

    @pytest.mark.parametrize(("source", "target"), [("COLLIDER", "VISUAL"), ("VISUAL", "COLLIDER")])
    @pytest.mark.parametrize("shape", ["MESH", "BOX"])
    def test_model_type_conversion_requires_reset(self, registered_ops, source, target, shape):
        bpy.ops.object.empty_add()
        parent = bpy.context.active_object
        parent.location = (3, -2, 5)
        parent.rotation_euler = (0.2, 0.4, -0.6)
        parent.scale = (2, 2, 2)
        parent.Forge_Model_Type = "LINK"
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.parent = parent
        obj.location = (1, 2, 3)
        obj.rotation_euler = (0.3, -0.2, 0.1)
        obj.Forge_Model_Type = source
        obj.Forge_Geometry.type = shape
        if shape == "BOX":
            modifiers = cons.GeometryShapeModifiers if source == "VISUAL" else cons.ColliderShapeModifiers
            attach_shape_modifier(obj, modifiers[shape])
        bpy.context.view_layer.update()
        world = obj.matrix_world.copy()
        old_mesh = obj.data

        with pytest.raises(TypeError):
            bpy.ops.forge.define_model_type(Model_Type=target)
        assert obj.Forge_Model_Type == source
        assert obj.parent == parent

        assert bpy.ops.forge.define_model_type(Model_Type="UNDEFINED") == {"FINISHED"}
        bpy.context.view_layer.update()
        assert obj.parent is None
        for actual, expected in zip(obj.matrix_world, world, strict=True):
            assert tuple(actual) == pytest.approx(tuple(expected), abs=1e-5)
        assert obj.data != old_mesh
        assert obj.data.name == obj.name.lower()
        assert obj.data.polygons
        assert not obj.modifiers

        assert bpy.ops.forge.define_model_type(Model_Type=target) == {"FINISHED"}
        assert obj.Forge_Model_Type == target
        assert obj.Forge_Geometry.type == "MESH"
        assert obj.Forge_Geometry.group == (2 if target == "VISUAL" else 3)
        assert obj.Forge_Geometry.contype == (0 if target == "VISUAL" else 1)
        assert obj.Forge_Geometry.conaffinity == (0 if target == "VISUAL" else 1)

    def test_untyped_mixed_blender_types_cannot_be_defined(self, registered_ops):
        bpy.ops.object.empty_add()
        empty = bpy.context.active_object
        bpy.ops.mesh.primitive_cube_add()
        mesh = bpy.context.active_object
        empty.select_set(True)
        assert bpy.ops.forge.define_model_type("INVOKE_DEFAULT") == {"CANCELLED"}
        with pytest.raises(TypeError):
            bpy.ops.forge.define_model_type(Model_Type="VISUAL")
        assert empty.Forge_Model_Type == mesh.Forge_Model_Type == "UNDEFINED"

    def test_define_multiple_untyped_meshes(self, registered_ops):
        bpy.ops.mesh.primitive_cube_add()
        first = bpy.context.active_object
        bpy.ops.mesh.primitive_cube_add()
        second = bpy.context.active_object
        first.select_set(True)
        assert bpy.ops.forge.define_model_type(Model_Type="VISUAL") == {"FINISHED"}
        assert first.Forge_Model_Type == second.Forge_Model_Type == "VISUAL"
        assert first.Forge_Geometry.contype == second.Forge_Geometry.contype == 0

    def test_reset_mesh_collider_bakes_convex_surface(self, registered_ops):
        bpy.ops.mesh.primitive_cube_add()
        source = bpy.context.active_object
        source.Forge_Model_Type = "VISUAL"
        source.Forge_Geometry.type = "BOX"
        collider = bpy.data.objects.new("Convex", bpy.data.meshes.new("Empty base"))
        bpy.context.collection.objects.link(collider)
        collider.Forge_Model_Type = "COLLIDER"
        collider.Forge_Geometry.type = "MESH"
        attach_shape_modifier(collider, cons.ColliderShapeModifiers["MESH"])
        funcs.set_collider_size_by_ref(collider, cons.GeometryTypes.MESH, source)
        source.select_set(False)
        collider.select_set(True)
        bpy.context.view_layer.objects.active = collider

        assert bpy.ops.forge.define_model_type(Model_Type="UNDEFINED") == {"FINISHED"}

        assert collider.Forge_Model_Type == "UNDEFINED"
        assert collider.data.polygons
        assert not collider.modifiers
        assert source.Forge_Model_Type == "VISUAL"
        assert len(source.data.vertices) == 8

    @pytest.mark.parametrize(("first", "second"), [("UNDEFINED", "VISUAL"), ("LINK", "COLLIDER")])
    def test_model_type_poll_rejects_ineligible_selections(self, registered_ops, first, second):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = first
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.active_object.Forge_Model_Type = second
        obj.select_set(True)
        assert not bpy.ops.forge.define_model_type.poll()

    def test_define_model_type_undefined(self, registered_ops):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        bpy.ops.forge.define_model_type(Model_Type="COLLIDER")
        obj.Forge_Geometry.friction = (0.8, 0.2, 0.1)
        obj.lock_scale = (True, True, True)
        obj.show_in_front = True
        name = obj.name
        collections = tuple(obj.users_collection)
        obj.modifiers.new("User modifier", "BEVEL")
        material = bpy.data.materials.new("Reset material")
        obj.data.materials.append(material)
        override = bpy.data.materials.new("Object override")
        obj.material_slots[0].link = "OBJECT"
        obj.material_slots[0].material = override
        source_mesh = obj.data
        shared = bpy.data.objects.new("Shared mesh", source_mesh)
        obj["custom"] = "keep"

        assert bpy.ops.forge.define_model_type(Model_Type="UNDEFINED") == {"FINISHED"}
        assert obj.Forge_Model_Type == "UNDEFINED"
        defaults = bpy.data.objects.new("Defaults", None)
        assert obj.Forge_Geometry.group == defaults.Forge_Geometry.group
        assert tuple(obj.Forge_Geometry.friction) == tuple(defaults.Forge_Geometry.friction)
        assert obj.display_type == defaults.display_type
        assert tuple(obj.lock_scale) == (False, False, False)
        assert obj.show_in_front is False
        assert obj.name == name
        assert tuple(obj.users_collection) == collections
        assert not obj.modifiers
        assert obj.data != source_mesh
        assert shared.data == source_mesh
        assert len(obj.data.vertices) > len(source_mesh.vertices)
        assert obj.material_slots[0].material == override
        assert source_mesh.materials[0] == material
        assert obj["custom"] == "keep"

        bpy.ops.forge.define_model_type(Model_Type="VISUAL")
        assert obj.Forge_Model_Type == "VISUAL"

    def test_define_model_type_undefined_mixed_selection(self, registered_ops):
        bpy.ops.object.light_add(type="POINT")
        link = bpy.context.active_object
        link.Forge_Model_Type = "LIGHT"
        link["Root Link"] = True
        link["INSTANCE_LINK"] = True
        link.Forge_Link.mass = 7
        bpy.ops.mesh.primitive_cube_add()
        mesh = bpy.context.active_object
        mesh.Forge_Model_Type = "COLLIDER"
        link.select_set(True)

        assert bpy.ops.forge.define_model_type(Model_Type="UNDEFINED") == {"FINISHED"}
        assert link.Forge_Model_Type == mesh.Forge_Model_Type == "UNDEFINED"
        assert "Root Link" not in link
        assert "INSTANCE_LINK" not in link
        assert not link.is_property_set("Forge_Link")

    @pytest.mark.parametrize("model_type", ["VISUAL", "COLLIDER"])
    @pytest.mark.parametrize("shape", ["BOX", "SPHERE", "CAPSULE", "CYLINDER"])
    def test_reset_shape_bakes_solid_mesh(self, registered_ops, model_type, shape, capfd):
        obj = bpy.data.objects.new("Shape", bpy.data.meshes.new("Shape base"))
        bpy.context.collection.objects.link(obj)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        obj.Forge_Model_Type = model_type
        obj.Forge_Geometry.type = shape
        modifiers = cons.GeometryShapeModifiers if model_type == "VISUAL" else cons.ColliderShapeModifiers
        attach_shape_modifier(obj, modifiers[shape])
        original_mesh = obj.data

        assert bpy.ops.forge.define_model_type(Model_Type="UNDEFINED") == {"FINISHED"}

        assert "independent mesh" in capfd.readouterr().out
        assert obj.Forge_Model_Type == "UNDEFINED"
        assert obj.data != original_mesh
        assert obj.data.polygons
        assert not obj.modifiers

    def test_define_model_type_link(self, registered_ops):
        """forge.define_model_type assigns LINK to an EMPTY object."""
        bpy.ops.object.empty_add(type="PLAIN_AXES")
        obj = bpy.context.active_object
        assert obj.Forge_Model_Type == "UNDEFINED"

        bpy.ops.forge.define_model_type(Model_Type="LINK")
        assert obj.Forge_Model_Type == "LINK"

    def test_define_model_type_visual(self, registered_ops):
        """forge.define_model_type with a mesh type assigns VISUAL."""
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        bpy.ops.forge.define_model_type(Model_Type="VISUAL")
        assert obj.Forge_Model_Type == "VISUAL"
        assert obj.Forge_Geometry.type == "MESH"
        assert obj.Forge_Geometry.group == cons.GeometryGroup.VISUAL

    def test_define_model_type_collider(self, registered_ops):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        bpy.ops.forge.define_model_type(Model_Type="COLLIDER")
        assert obj.Forge_Model_Type == "COLLIDER"
        assert obj.Forge_Geometry.group == cons.GeometryGroup.COLLIDER

    def test_define_model_type_directional_light_lands_in_world(self, registered_ops):
        """A directional light is detached from its parent, so it belongs in World, not Light."""
        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.forge.create_link()
        link = bpy.context.active_object

        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.object.light_add(type="SUN")
        light = bpy.context.active_object
        light.parent = link
        bpy.context.view_layer.update()

        bpy.ops.forge.define_model_type(Model_Type="LIGHT")
        assert light.parent is None
        assert [c.name for c in light.users_collection] == [cons.CollectionNames.WORLD]

    def test_create_link_standalone(self, registered_ops):
        """forge.create_link creates an empty LINK with no parent."""
        bpy.ops.forge.create_link()
        obj = bpy.context.active_object
        assert obj is not None
        assert obj.Forge_Model_Type == "LINK"
        assert obj.type == "EMPTY"
        assert obj.get("Root Link") is True

    def test_create_link_child(self, registered_ops):
        """Create a parent link, then child with parent selected."""
        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.forge.create_link()
        parent = bpy.context.active_object
        bpy.context.view_layer.objects.active = parent
        print(parent)
        print(bpy.context.selected_objects)

        bpy.ops.forge.create_link()
        child = bpy.context.active_object
        print(bpy.context.selected_objects)
        print(child)
        print(child.parent)
        bpy.context.view_layer.update()
        print(bpy.context.selected_objects)

        print(bpy.data.objects[:])
        assert child is not None
        assert child.parent == parent

    def test_create_frame_standalone(self, registered_ops):
        bpy.ops.forge.create_frame()
        obj = bpy.context.active_object
        assert obj is not None
        assert obj.Forge_Model_Type == "FRAME"

    def test_create_frame_under_link(self, registered_ops):
        bpy.ops.forge.create_link()
        link = bpy.context.active_object
        bpy.ops.forge.create_frame()
        frame = bpy.context.active_object
        assert frame.parent == link

    def test_batch_rename(self, registered_ops):
        """forge.batch_rename renames selected objects."""
        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.mesh.primitive_cube_add()
        cube1 = bpy.context.active_object
        bpy.ops.mesh.primitive_cube_add()
        cube2 = bpy.context.active_object

        bpy.ops.object.select_all(action="DESELECT")
        cube1.select_set(True)
        cube2.select_set(True)
        bpy.context.view_layer.objects.active = cube1
        bpy.context.view_layer.update()

        bpy.ops.forge.batch_rename(new_name="Part", numerate="###")
        assert cube1.name.startswith("Part_")
        assert cube2.name.startswith("Part_")

    def test_mark_root_link(self, registered_ops):
        """forge.mark_root_link sets Root Link on top-level links."""
        bpy.ops.forge.create_link()
        link = bpy.context.active_object
        # Unmark first, then re-mark
        link["Root Link"] = False
        bpy.ops.forge.mark_root_link()
        assert link.get("Root Link") is True

    def test_mark_root_link_unparents_and_preserves_world_transform(self, registered_ops):
        """A nested link is detached before it is marked as a root."""
        bpy.ops.forge.create_link()
        parent = bpy.context.active_object
        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.forge.create_link()
        child = bpy.context.active_object
        child.parent = parent
        child.location = (1.0, 2.0, 3.0)
        bpy.context.view_layer.update()
        world_before = child.matrix_world.copy()

        bpy.ops.forge.mark_root_link()

        assert child.parent is None
        assert child.get("Root Link") is True
        assert tuple(child.matrix_world.translation) == pytest.approx(tuple(world_before.translation))

    def test_select_by_tag(self, registered_ops):
        """forge.select_by_tag selects objects whose name contains the tag."""
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.active_object.name = "GEO_Wheel"
        bpy.ops.object.duplicate()
        bpy.context.active_object.name = "COL_Wheel"

        scene = bpy.context.scene
        bpy.data.scenes[scene.Main_Scene].Forge_Props.select_tag = "Wheel"
        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.forge.select_by_tag()

        selected = [o for o in bpy.data.objects if o.select_get()]
        assert len(selected) == 2

    def test_define_parent(self, registered_ops):
        """forge.define_parent parents selected child to active parent."""
        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.forge.create_link()
        parent = bpy.context.active_object
        bpy.ops.object.select_all(action="DESELECT")

        bpy.ops.forge.create_link()
        child = bpy.context.active_object
        child.parent = None  # un-parent
        bpy.context.view_layer.update()

        bpy.ops.object.select_all(action="DESELECT")
        child.select_set(True)
        parent.select_set(True)
        bpy.context.view_layer.objects.active = parent
        bpy.context.view_layer.update()

        bpy.ops.forge.define_parent()
        assert child.parent == parent

    def test_define_parent_refuses_collider_under_visual(self, registered_ops):
        """Parenting a collider to a visual is refused: that collider would not be exported."""
        from Forge.ops.definition import Forge_OT_Parent_Define

        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.mesh.primitive_cube_add()
        visual = bpy.context.active_object
        visual.Forge_Model_Type = cons.ModelTypes.VISUAL
        bpy.ops.object.select_all(action="DESELECT")

        bpy.ops.mesh.primitive_cube_add()
        collider = bpy.context.active_object
        collider.Forge_Model_Type = cons.ModelTypes.COLLIDER

        bpy.ops.object.select_all(action="DESELECT")
        collider.select_set(True)
        visual.select_set(True)
        bpy.context.view_layer.objects.active = visual
        bpy.context.view_layer.update()

        assert Forge_OT_Parent_Define.poll(bpy.context) is False
        # poll_message_set supplies this text and it survives into the RuntimeError,
        # which is what the MCP bridge surfaces to the caller.
        with pytest.raises(RuntimeError, match="not exported"):
            bpy.ops.forge.define_parent()
        assert collider.parent is None

    def test_define_parent_lifts_nested_visual_children_to_link(self, registered_ops):
        """Reparenting a visual moves its collider children to the link, repairing the legacy nesting."""
        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.forge.create_link()
        link = bpy.context.active_object
        bpy.ops.object.select_all(action="DESELECT")

        bpy.ops.mesh.primitive_cube_add()
        visual = bpy.context.active_object
        visual.parent = link
        visual.Forge_Model_Type = cons.ModelTypes.VISUAL

        # Two colliders so the lift is asserted for more than one child.
        colliders = []
        for index in range(2):
            bpy.ops.mesh.primitive_cube_add()
            collider = bpy.context.active_object
            collider.name = f"COL_Box_{index}"
            collider.parent = visual
            collider.Forge_Model_Type = cons.ModelTypes.COLLIDER
            colliders.append(collider)

        bpy.ops.object.select_all(action="DESELECT")
        visual.select_set(True)
        bpy.context.view_layer.objects.active = link
        bpy.context.view_layer.update()

        assert bpy.ops.forge.define_parent() == {"FINISHED"}
        assert visual.parent == link
        assert [c.parent for c in colliders] == [link, link]

    def test_define_parent_moves_children_into_their_type_collection(self, registered_ops):
        """Reparented objects land in the collection of their model type, lifted children included."""
        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.forge.create_link()
        link = bpy.context.active_object

        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.mesh.primitive_cube_add()
        visual = bpy.context.active_object
        visual.Forge_Model_Type = cons.ModelTypes.VISUAL

        bpy.ops.mesh.primitive_cube_add()
        collider = bpy.context.active_object
        collider.name = "COL_Box"
        collider.parent = visual
        collider.Forge_Model_Type = cons.ModelTypes.COLLIDER

        bpy.ops.object.select_all(action="DESELECT")
        visual.select_set(True)
        link.select_set(True)
        bpy.context.view_layer.objects.active = link
        bpy.context.view_layer.update()

        assert bpy.ops.forge.define_parent() == {"FINISHED"}
        assert visual.parent == link
        assert collider.parent == link
        assert [c.name for c in visual.users_collection] == [cons.CollectionNames.VISUAL]
        assert [c.name for c in collider.users_collection] == [cons.CollectionNames.COLLIDER]

    def test_update_model_collection_follows_parent_state(self, registered_ops):
        """The routing helper sends a parentless object to World, a parented one to its type collection."""
        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.forge.create_link()
        link = bpy.context.active_object

        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.mesh.primitive_cube_add()
        visual = bpy.context.active_object
        visual.Forge_Model_Type = cons.ModelTypes.VISUAL

        funcs.update_model_collection(bpy.context, visual)
        assert [c.name for c in visual.users_collection] == [cons.CollectionNames.WORLD]

        visual.parent = link
        funcs.update_model_collection(bpy.context, visual)
        assert [c.name for c in visual.users_collection] == [cons.CollectionNames.VISUAL]

    def test_create_inertial_computes_on_link(self, registered_ops):
        """forge.create_inertial creates INERTIAL child on a LINK."""
        bpy.ops.forge.create_link()
        link = bpy.context.active_object

        # Ensure link has a visual child with mesh
        bpy.ops.mesh.primitive_cube_add()
        cube = bpy.context.active_object
        cube.parent = link
        cube.Forge_Model_Type = "VISUAL"
        cube.Forge_Geometry.type = "MESH"
        cube.Forge_Geometry.density = 1.0

        # Select the link
        bpy.ops.object.select_all(action="DESELECT")
        link.select_set(True)
        bpy.context.view_layer.objects.active = link

        assert bpy.ops.forge.create_inertial() == {"FINISHED"}
        # Should have created an INERTIAL node under the link
        inertials = [c for c in link.children if c.Forge_Model_Type == "INERTIAL"]
        assert len(inertials) == 1
        inertial = inertials[0]
        assert inertial.Forge_Inertial.mass == pytest.approx(8.0)
        assert tuple(inertial.location) == pytest.approx((0, 0, 0), abs=1e-6)
        assert tuple(inertial.Forge_Inertial.diaginertia) == pytest.approx((16 / 3,) * 3)

    def test_create_plane(self, registered_ops):
        """forge.create_plane creates a PLANE mesh."""
        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.forge.create_plane()
        obj = bpy.context.active_object
        assert obj is not None
        assert obj.Forge_Model_Type == "PLANE"

    def test_create_height_field(self, registered_ops, forge_asset_library):
        """forge.create_height_field creates an HFIELD mesh."""
        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.forge.create_height_field()
        obj = bpy.context.active_object
        assert obj is not None
        assert obj.Forge_Model_Type == "HFIELD"

    def test_instance_idname(self, registered_ops):
        """forge.set_instance_idname sets INSTANCE_IDNAME on BODY objects."""
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "LINK"
        scene = bpy.context.scene
        bpy.data.scenes[scene.Main_Scene].Forge_Props.instance_body = obj

        bpy.ops.forge.set_instance_idname()
        assert obj.get("INSTANCE_IDNAME") == obj

    def test_instance_idname_clear(self, registered_ops):
        """forge.set_instance_idname removes INSTANCE_IDNAME when no instance body is set."""
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.Forge_Model_Type = "LINK"
        scene = bpy.context.scene
        props = bpy.data.scenes[scene.Main_Scene].Forge_Props
        props.instance_body = obj
        bpy.ops.forge.set_instance_idname()
        assert obj.get("INSTANCE_IDNAME") == obj

        props.instance_body = None
        bpy.ops.forge.set_instance_idname()
        assert obj.get("INSTANCE_IDNAME") is None

    def test_instance_idname_skips_marked_instance_link(self, registered_ops):
        """forge.set_instance_idname refuses links already marked INSTANCE_LINK."""
        links = []
        for name in ("template", "placeholder"):
            bpy.ops.mesh.primitive_cube_add()
            obj = bpy.context.active_object
            obj.name = name
            obj.Forge_Model_Type = "LINK"
            links.append(obj)
        template, marked = links

        bpy.context.view_layer.objects.active = template
        template.select_set(True)
        assert bpy.ops.forge.mark_instance_link() == {"FINISHED"}

        scene = bpy.context.scene
        props = bpy.data.scenes[scene.Main_Scene].Forge_Props
        props.instance_body = template
        marked.select_set(True)
        bpy.context.view_layer.objects.active = marked
        bpy.ops.forge.set_instance_idname()

        assert marked.get("INSTANCE_IDNAME") is None

    def test_mark_instance_link_toggles(self, registered_ops):
        """forge.mark_instance_link toggles INSTANCE_LINK on selected links."""
        from Forge.core import selection as sel

        objects = []
        for name in ("first", "second"):
            bpy.ops.mesh.primitive_cube_add()
            obj = bpy.context.active_object
            obj.name = name
            obj.Forge_Model_Type = "LINK"
            objects.append(obj)

        first, second = objects
        for obj in objects:
            obj.select_set(True)
        bpy.context.view_layer.objects.active = first

        assert bpy.ops.forge.mark_instance_link() == {"FINISHED"}
        assert first.get("INSTANCE_LINK") is True
        assert second.get("INSTANCE_LINK") is True
        # The instance_body picker only accepts marked links.
        assert sel.instance_link_only_poll(None, first) is True

        second.select_set(False)
        assert bpy.ops.forge.mark_instance_link() == {"FINISHED"}
        assert first.get("INSTANCE_LINK") is None
        assert second.get("INSTANCE_LINK") is True
        assert sel.instance_link_only_poll(None, first) is False
        assert sel.instance_link_only_poll(None, second) is True


# ═══════════════════════════════════════════════════════════════════
#  6. Geometry handler
# ═══════════════════════════════════════════════════════════════════


class TestGeometryHandler:
    def _fake_mod(self, vals=None):
        vals = vals or {}
        sv = vals.get("SIZE", (1.0, 1.0, 1.0))
        hv = vals.get("HEIGHT", 0.5)
        m = MagicMock()
        m.__getitem__ = MagicMock(
            side_effect=lambda k: {
                "Socket_0": sv,
                "Socket_2": hv,
                "Socket_3": sv,
                "Socket_4": hv,
            }.get(k, 0.0)
        )
        m.__setitem__ = MagicMock()
        return m

    def test_box_half_extent(self):
        h = GeometryHandler("BOX", cons.ModifierSockets.Visual)
        s = h.get_size(self._fake_mod({"SIZE": (2.0, 2.0, 2.0)}))
        assert list(s) == [1.0, 1.0, 1.0]

    def test_sphere_retains_radius(self):
        h = GeometryHandler("SPHERE", cons.ModifierSockets.Visual)
        s = h.get_size(self._fake_mod({"SIZE": 0.5}))
        assert s == 0.5

    def test_gizmo_offset_box(self):
        h = GeometryHandler("BOX", cons.ModifierSockets.Visual)
        off = h.get_gizmo_offset(self._fake_mod({"SIZE": (1.0, 1.0, 1.0)}))
        assert off == [0.5, 0.5, 0.5]

    def test_gizmo_offset_sphere(self):
        h = GeometryHandler("SPHERE", cons.ModifierSockets.Visual)
        off = h.get_gizmo_offset(self._fake_mod({"SIZE": 0.4}))
        assert off == [0.4, 0.4, 0.4]

    def test_set_box_size(self):
        h = GeometryHandler("BOX", cons.ModifierSockets.Visual)
        m = self._fake_mod()
        h.set_size(m, (2.0, 2.0, 2.0), based_on_dimensions=True)
        m.__setitem__.assert_called()
        assert m.__setitem__.call_args[0][1] == (2.0, 2.0, 2.0)

    def test_dimensions_roundtrip_box(self):
        h = GeometryHandler("BOX", cons.ModifierSockets.Visual)
        d = h.get_dimensions(self._fake_mod({"SIZE": (1.0, 1.0, 1.0)}))
        assert list(d) == [1.0, 1.0, 1.0]

    def test_dimensions_capsule(self):
        h = GeometryHandler("CAPSULE", cons.ModifierSockets.Visual)
        d = h.get_dimensions(self._fake_mod({"SIZE": 0.3, "HEIGHT": 1.0}))
        assert d[0] == pytest.approx(0.6)
        assert d[2] == pytest.approx(1.6)

    def test_dimensions_cylinder(self):
        h = GeometryHandler("CYLINDER", cons.ModifierSockets.Visual)
        d = h.get_dimensions(self._fake_mod({"SIZE": 0.3, "HEIGHT": 1.0}))
        assert d[0] == pytest.approx(0.6)
        assert d[2] == 1.0


class _PropRecorder:
    """Minimal ``UILayout`` double recording ``prop()`` calls."""

    def __init__(self):
        self.calls = []

    def prop(self, data, prop, *args, **kwargs):
        self.calls.append((data, prop, args, kwargs))


class TestModifierSocketUI:
    def test_prop_modifier_socket_targets_the_socket_value(self):
        """UI editors must target the socket struct on 5.2+, not a nested path."""
        mesh = bpy.data.meshes.new("ui-socket")
        obj = bpy.data.objects.new("ui-socket", mesh)
        bpy.context.scene.collection.objects.link(obj)
        with headless_shape_modifiers():
            add_shape_modifier(obj, "Visual", "BOX")

        modifier = obj.modifiers["Geometry_Box"]
        layout = _PropRecorder()
        prop_modifier_socket(layout, modifier, cons.ModifierSockets.Visual.SIZE, text="", slider=1)

        data, prop, _, kwargs = layout.calls[0]
        assert kwargs == {"text": "", "slider": 1}
        if bpy.app.version >= (5, 2, 0):
            # ``UILayout.prop`` cannot resolve ``properties.inputs.Socket_N.value``,
            # so the socket struct and its direct ``value`` property are passed.
            assert prop == "value"
            assert data is not modifier
            assert tuple(data.value) == pytest.approx((1.0, 1.0, 1.0))
        else:
            assert data is modifier
            assert prop == '["Socket_0"]'


# ═══════════════════════════════════════════════════════════════════
#  7. Serialization
# ═══════════════════════════════════════════════════════════════════


class TestSerialization:
    def test_get_active(self):
        assert ser.get_active("true") is True
        assert ser.get_active("false") is False

    def test_get_bool_str(self):
        assert ser.get_bool_str(True) == "true"
        assert ser.get_bool_str(False) == "false"

    def test_round_float(self):
        assert ser.round_float(3.14159, 3) == 3.142

    def test_parse_vector(self):
        r = ser.parse_vector_array_to_xml([1.0, 2.0, 3.0])
        assert len(r.split(" ")) == 3

    def test_parse_value_bool(self):
        assert ser.parse_value_by_attr(True) == "true"

    def test_parse_value_number(self):
        assert ser.parse_value_by_attr(42) == "42"

    def test_parse_float_list(self):
        assert ser.parse_float_list("1.0 2.5") == [1.0, 2.5]

    def test_fix_image_name(self):
        assert ser.fix_image_name("tex.jpg") == "tex.png"
        assert ser.fix_image_name("Texture.JPEG") == "Texture.png"
        assert ser.fix_image_name("bare") == "bare.png"


# ═══════════════════════════════════════════════════════════════════
#  8. Export
# ═══════════════════════════════════════════════════════════════════


class TestExport:
    def test_compiler_section(self, registered_props):
        c = bpy.context.scene.Forge_GlobalConfig.g_compiler
        c.autolimits = False
        c.angle = "RADIAN"
        c.eulerseq = "ZYX"
        import xml.etree.ElementTree as ET

        mujoco = ET.Element("mujoco")
        add_compiler(bpy.context, mujoco)
        assert mujoco.find("compiler").get("autolimits") == "false"
        assert mujoco.find("compiler").get("angle") == "radian"
        assert mujoco.find("compiler").get("eulerseq") == "zyx"
        c.reset()

    def test_visual_section(self, registered_props):
        v = bpy.context.scene.Forge_VisualConfig
        v.v_global.fovy = 0.8
        v.v_global.azimuth = 1.57
        v.v_headlight.active = 1
        import xml.etree.ElementTree as ET

        mujoco = ET.Element("mujoco")
        add_visual(bpy.context, mujoco)
        assert "fovy" in mujoco.find(".//global").attrib

    def test_prettify(self):
        import xml.etree.ElementTree as ET

        e = ET.Element("mujoco")
        wb = ET.SubElement(e, "worldbody")
        ET.SubElement(wb, "geom", name="floor")
        r = prettify(e)
        assert "  <worldbody>" in r
        assert "    <geom" in r


# ═══════════════════════════════════════════════════════════════════
#  9. Import helpers
# ═══════════════════════════════════════════════════════════════════


class TestImportHelpers:
    def test_parse_inherit_attrs_root(self):
        defaults = {"geom": {"rgba": "0.5 0.5 0.5 1", "priority": "2"}}
        ta = {"type": "box"}
        parse_inherit_attrs(defaults, ta, "geom", "root")
        assert ta["rgba"] == "0.5 0.5 0.5 1"
        assert ta["type"] == "box"

    def test_parse_inherit_attrs_subclass(self):
        defaults = {
            "root": {"geom": {"rgba": "0.5 0.5 0.5 1"}},
            "metal": {"parent": "root", "geom": {"rgba": "0.8 0.2 0.2 1"}},
        }
        ta = {"type": "box"}
        parse_inherit_attrs(defaults, ta, "geom", "metal")
        assert ta["rgba"] == "0.8 0.2 0.2 1"

    def test_set_coll_tag(self):
        assert set_coll_tag("Visual") == "Visual"
        parent = bpy.data.collections.new("Robot")
        assert set_coll_tag("Visual", parent) == "Robot_Visual"

    def test_get_data_object(self):
        assert get_data_object("nope", "") is None
