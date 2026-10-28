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

"""Creation and definition operator tests.

Covers the ``forge.create_*`` operators from ``ops/creation.py`` and the
``forge.define_*_type`` operators from ``ops/definition.py`` that were
previously untested. Creation code calls
``bpy.ops.object.modifier_add_node_group`` for display-only shape modifiers,
which never works in background Blender — the ``headless_ops`` fixture shims
that call out (see ``mjcf_helpers.headless_shape_modifiers``).
"""

from types import SimpleNamespace

import bpy
import pytest
from Forge.core import constants as cons

from .mjcf_helpers import attach_shape_modifier, headless_shape_modifiers


@pytest.fixture
def headless_ops(registered_ops):
    """Registered operators with the asset-browser modifier call shimmed out."""
    with headless_shape_modifiers():
        yield bpy.context


def _select(ordered: list):
    """Select objects in order, tagging them with ``selected_order``."""
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
    for index, obj in enumerate(ordered):
        obj["selected_order"] = index
        obj.select_set(True)
    bpy.context.view_layer.objects.active = ordered[-1] if ordered else None
    return ordered


def _deselect_all():
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
    bpy.context.view_layer.objects.active = None


def _create_link(parent=None):
    _select([parent]) if parent else _deselect_all()
    bpy.ops.forge.create_link()
    return bpy.context.active_object


def _create_joint(link, joint_type=cons.JointTypes.HINGE):
    _select([link])
    bpy.ops.forge.create_joint(joint_type=joint_type)
    return bpy.context.active_object


def _objects_of_type(model_type):
    return [obj for obj in bpy.data.objects if obj.Forge_Model_Type == model_type]


class TestCreationOperators:
    def test_collider_size_ui_draws_only_the_selected_shape_size(self):
        from Forge.ops.creation import Forge_OT_Collider_Creation

        drawn_properties = []

        class Layout:
            def box(self):
                return self

            def column(self, **_kwargs):
                return self

            def prop(self, _owner, name, **_kwargs):
                drawn_properties.append(name)

            def separator(self):
                pass

        operator = SimpleNamespace(layout=Layout())

        Forge_OT_Collider_Creation._draw_size(operator, cons.GeometryTypes.BOX)

        assert drawn_properties == ["size_box"]
        assert "collider_type" not in drawn_properties
        assert "geometry_type" not in drawn_properties

    def test_sensor_type_change_clears_invalid_target(self, headless_ops):
        link = _create_link()
        joint = _create_joint(link)
        _select([joint])
        bpy.ops.forge.create_sensor(Sensor_Type="Jointpos")
        sensor = _objects_of_type(cons.ModelTypes.SENSOR)[0]

        sensor.Forge_Sensor.type = cons.SensorTypes.Contact

        assert sensor.Forge_Sensor.target is None

    def test_create_sensor_keeps_type_when_kwargs_restate_flag_defaults(self, headless_ops):
        """MCP-style calls always pass the three flags; RNA fires ``update`` on every
        assignment, so a flag that merely re-states its default must not clobber the
        requested ``Sensor_Type`` back to the first enum item (was: Gyro -> Touch)."""
        _create_link()
        _select([_create_link()])
        bpy.ops.forge.create_site(site_type="SPHERE")
        site = _objects_of_type(cons.ModelTypes.SITE)[0]

        _select([site])
        assert bpy.ops.forge.create_sensor(Sensor_Type="Gyro", set_ref=False, set_xbody=False, set_subtree=False) == {
            "FINISHED"
        }

        sensor = _objects_of_type(cons.ModelTypes.SENSOR)[0]
        assert sensor.Forge_Sensor.type == cons.SensorTypes.Gyro

    @staticmethod
    def _build_sensor_targets():
        """Return a root link plus a site, for sensor target selection."""
        link = _create_link()
        _select([link])
        bpy.ops.forge.create_site(site_type="SPHERE")
        return link, _objects_of_type(cons.ModelTypes.SITE)[0]

    @pytest.mark.parametrize(
        ("kwargs", "target", "expected"),
        [
            ({"set_xbody": True, "Sensor_Type": "Frameangvel"}, "link", cons.SensorTypes.Frameangvel),
            ({"set_xbody": True, "Sensor_Type": "Framelinvel"}, "link", cons.SensorTypes.Framelinvel),
            ({"set_subtree": True, "Sensor_Type": "Contact"}, "link", cons.SensorTypes.Contact),
            ({"set_ref": True, "Sensor_Type": "Framepos"}, "site_ref", cons.SensorTypes.Framepos),
            ({"Sensor_Type": "Framequat"}, "site", cons.SensorTypes.Framequat),
        ],
    )
    def test_create_sensor_type_survives_enabled_flags(self, headless_ops, kwargs, target, expected):
        """An *enabled* flag fires the reset callback too, so the requested type must be
        applied after it. Blender assigns operator arguments in RNA declaration order
        (not call order), which is why ``Forge_OT_Sensor_Creation`` declares the three
        flags before ``Sensor_Type``."""
        link, site = self._build_sensor_targets()
        _select([site, link] if target == "site_ref" else [link if target == "link" else site])

        assert bpy.ops.forge.create_sensor(**kwargs) == {"FINISHED"}

        sensor = _objects_of_type(cons.ModelTypes.SENSOR)[0]
        assert sensor.Forge_Sensor.type == expected

    def test_sensor_update_resets_type_on_flag_change(self):
        """The update callback clears Sensor_Type whenever a flag is assigned."""
        from Forge.ops.creation import Forge_OT_Sensor_Creation

        class FakeOp:
            def __init__(self):
                self.store = {}
                self.set_ref = False
                self.set_xbody = False
                self.set_subtree = False

            def get(self, key):
                return self.store.get(key)

            def __setitem__(self, key, value):
                self.store[key] = value

        op = FakeOp()
        op.store["Sensor_Type"] = 3  # Gyro within the SITE enum range

        # A flag assignment must clear stale dynamic-enum selections.
        Forge_OT_Sensor_Creation.update_type(op, None)
        assert op.store["Sensor_Type"] == 0

    def test_sensor_poll_explains_a_mixed_joint_selection(self, headless_ops):
        """A joint can only ever be a lone target (MJCF has no `joint` reftype), so a
        joint paired with another object must be refused with a reason rather than the
        bare "poll() failed, context is incorrect"."""
        link = _create_link()
        _select([link])
        bpy.ops.forge.create_joint(joint_type="HINGE")
        joint = _objects_of_type(cons.ModelTypes.JOINT)[-1]

        _select([link, joint])
        with pytest.raises(RuntimeError, match="joint cannot be combined"):
            bpy.ops.forge.create_sensor(Sensor_Type="Framepos", set_ref=True)

        # A lone joint is still a valid target.
        _select([joint])
        assert bpy.ops.forge.create_sensor(Sensor_Type="Jointpos") == {"FINISHED"}

    def test_create_geometry_standalone(self, headless_ops):
        """forge.create_geometry makes a standalone visual in the World collection."""
        _deselect_all()
        bpy.ops.forge.create_geometry(geometry_type="SPHERE")

        obj = bpy.context.active_object
        assert obj is not None
        assert obj.Forge_Model_Type == cons.ModelTypes.VISUAL
        assert obj.Forge_Geometry.type == cons.GeometryTypes.SPHERE
        assert obj.Forge_Geometry.group == cons.GeometryGroup.VISUAL
        assert any(coll.name == cons.CollectionNames.WORLD for coll in obj.users_collection)

    def test_create_geometry_default_is_box(self, headless_ops):
        """The Forge panel invokes this operator with no arguments, so the declared
        default is what a user gets from the dialog: a BOX."""
        _deselect_all()
        bpy.ops.forge.create_geometry()

        obj = bpy.context.active_object
        assert obj.Forge_Geometry.type == cons.GeometryTypes.BOX

    def test_create_collider_standalone(self, headless_ops):
        """forge.create_collider makes a standalone collider (COLLIDER_TYPE method, nothing selected)."""
        _deselect_all()
        bpy.ops.forge.create_collider(collider_type="BOX", create_method="COLLIDER_TYPE")

        obj = bpy.context.active_object
        assert obj is not None
        assert obj.Forge_Model_Type == cons.ModelTypes.COLLIDER
        assert obj.Forge_Geometry.type == cons.GeometryTypes.BOX
        assert obj.Forge_Geometry.group == cons.GeometryGroup.COLLIDER

    def test_create_site_on_link(self, headless_ops):
        """forge.create_site parents a site under the selected link."""
        link = _create_link()
        bpy.ops.forge.create_site(site_type="SPHERE")

        sites = _objects_of_type(cons.ModelTypes.SITE)
        assert len(sites) == 1
        assert sites[0].parent is link
        assert sites[0].Forge_Geometry.type == cons.GeometryTypes.SPHERE

    def test_create_joint_on_link(self, headless_ops):
        """forge.create_joint parents a joint under the selected link."""
        link = _create_link()
        bpy.ops.forge.create_joint(joint_type="HINGE")

        joints = _objects_of_type(cons.ModelTypes.JOINT)
        assert len(joints) == 1
        assert joints[0].parent is link
        assert joints[0].Forge_Joint.type == cons.JointTypes.HINGE

    def test_create_actuator_on_joint(self, headless_ops):
        """forge.create_actuator targets the selected joint."""
        link = _create_link()
        joint = _create_joint(link)

        bpy.ops.forge.create_actuator(actuator_type="POSITION")

        actuators = _objects_of_type(cons.ModelTypes.ACTUATOR)
        assert len(actuators) == 1
        assert actuators[0].Forge_Actuator.type == cons.ActuatorTypes.POSITION
        assert actuators[0].Forge_Actuator.target is joint

    def test_create_tendon_from_joints(self, headless_ops):
        """forge.create_tendon builds a fixed tendon over the ordered joint selection."""
        root = _create_link()
        child = _create_link(root)
        joint_a = _create_joint(child)
        joint_b = _create_joint(child, joint_type=cons.JointTypes.SLIDE)

        _select([joint_a, joint_b])
        assert bpy.ops.forge.create_tendon(tendon_type="FIXED") == {"FINISHED"}

        tendons = _objects_of_type(cons.ModelTypes.TENDON)
        assert len(tendons) == 1
        data = tendons[0].Forge_Tendon
        assert data.type == cons.TendonTypes.FIXED
        targets = [item.target for item in data.targets.items]
        assert targets == [joint_a, joint_b]

    def test_create_equality_weld_between_links(self, headless_ops):
        """forge.create_equality welds the two selected links."""
        root = _create_link()
        child = _create_link(root)

        _select([root, child])
        assert bpy.ops.forge.create_equality(equality_type="WELD") == {"FINISHED"}

        equalities = _objects_of_type(cons.ModelTypes.EQUALITY)
        assert len(equalities) == 1
        data = equalities[0].Forge_Equality
        assert data.type == cons.EqualityTypes.WELD
        assert data.target1 is root
        assert data.target2 is child

    def test_create_sensor_on_joint(self, headless_ops):
        """forge.create_sensor tracks the selected joint."""
        link = _create_link()
        joint = _create_joint(link)

        _select([joint])
        assert bpy.ops.forge.create_sensor(Sensor_Type="Jointpos") == {"FINISHED"}

        sensors = _objects_of_type(cons.ModelTypes.SENSOR)
        assert len(sensors) == 1
        data = sensors[0].Forge_Sensor
        assert data.type == cons.SensorTypes.Jointpos
        assert data.target is joint

    def test_create_contact_exclude_between_links(self, headless_ops):
        """forge.create_contact creates an exclude between the two selected links."""
        root = _create_link()
        child = _create_link(root)

        _select([root, child])
        assert bpy.ops.forge.create_contact(contact_type="EXCLUDE") == {"FINISHED"}

        contacts = _objects_of_type(cons.ModelTypes.CONTACT)
        assert len(contacts) == 1
        data = contacts[0].Forge_Contact
        assert data.type == cons.ContactTypes.EXCLUDE
        assert data.target1 is root
        assert data.target2 is child

    def test_create_light_standalone(self, headless_ops):
        """forge.create_light makes a directional light in the World collection."""
        _deselect_all()
        assert bpy.ops.forge.create_light(light_type="DIRECTIONAL", light_mode="FIXED") == {"FINISHED"}

        lights = _objects_of_type(cons.ModelTypes.LIGHT)
        assert len(lights) == 1
        assert lights[0].Forge_Light.type == cons.LightTypes.DIRECTIONAL
        assert lights[0].Forge_Light.mode == cons.TargetModes.FIXED
        assert lights[0].data.type == "SUN"
        assert any(coll.name == cons.CollectionNames.WORLD for coll in lights[0].users_collection)

    def test_create_camera_standalone(self, headless_ops):
        """forge.create_camera makes a perspective camera in the World collection."""
        _deselect_all()
        assert bpy.ops.forge.create_camera(camera_type="PERSPECTIVE", camera_mode="FIXED") == {"FINISHED"}

        cameras = _objects_of_type(cons.ModelTypes.CAMERA)
        assert len(cameras) == 1
        assert cameras[0].Forge_Camera.type == cons.CameraTypes.PERSPECTIVE
        assert cameras[0].Forge_Camera.mode == cons.TargetModes.FIXED
        assert cameras[0].data.type == "PERSP"
        assert any(coll.name == cons.CollectionNames.WORLD for coll in cameras[0].users_collection)

    def test_camera_targetbody_one_link_creates_world_camera(self, headless_ops):
        """One selected link + target-body mode makes a parentless camera targeting the link."""
        link = _create_link()
        _select([link])

        assert bpy.ops.forge.create_camera(camera_type="PERSPECTIVE", camera_mode="TARGETBODY") == {"FINISHED"}
        cameras = _objects_of_type(cons.ModelTypes.CAMERA)
        assert len(cameras) == 1
        assert cameras[0].parent is None
        assert cameras[0].Forge_Camera.mode == cons.TargetModes.TARGETBODY
        assert cameras[0].Forge_Camera.target == link

    def test_camera_targetbody_two_links_parents_first_targets_second(self, headless_ops):
        """Target-body mode with two ordered links parents the camera to the first, targets the second."""
        link = _create_link()
        second = _create_link()
        _select([link, second])

        assert bpy.ops.forge.create_camera(camera_type="PERSPECTIVE", camera_mode="TARGETBODY") == {"FINISHED"}
        cameras = _objects_of_type(cons.ModelTypes.CAMERA)
        assert len(cameras) == 1
        assert cameras[0].parent == link
        assert cameras[0].Forge_Camera.target == second

    def test_camera_enum_offers_targetbody_for_one_link(self, headless_ops):
        from Forge.ops.creation import Forge_OT_Camera_Creation

        link = _create_link()
        _select([link])
        identifiers = [item[0] for item in Forge_OT_Camera_Creation.mode_enum_items(None, bpy.context)]

        assert cons.TargetModes.TARGETBODY in identifiers
        assert cons.TargetModes.TARGETBODYCOM in identifiers

    def test_create_replicate_from_link(self, headless_ops):
        """forge.create_replicate wraps the selected link into a replicate array."""
        link = _create_link()

        _select([link])
        assert bpy.ops.forge.create_replicate(count=2, offset=(1.0, 0.0, 0.0)) == {"FINISHED"}

        replicates = _objects_of_type(cons.ModelTypes.REPLICATE)
        assert len(replicates) == 1
        assert replicates[0].Forge_Replicate.count == 2


class TestDefineOperators:
    def test_define_joint_type(self, headless_ops):
        """forge.define_joint_type switches a hinge joint to slide."""
        joint = _create_joint(_create_link())
        _select([joint])

        assert bpy.ops.forge.define_joint_type(joint_type="SLIDE", apply_to_all=True) == {"FINISHED"}
        assert joint.Forge_Joint.type == cons.JointTypes.SLIDE

    def test_define_actuator_type(self, headless_ops):
        """forge.define_actuator_type switches a position actuator to motor."""
        link = _create_link()
        _create_joint(link)
        bpy.ops.forge.create_actuator(actuator_type="POSITION")
        actuator = _objects_of_type(cons.ModelTypes.ACTUATOR)[0]

        _select([actuator])
        assert bpy.ops.forge.define_actuator_type(actuator_type="MOTOR", apply_to_all=True) == {"FINISHED"}
        assert actuator.Forge_Actuator.type == cons.ActuatorTypes.MOTOR

    def test_define_site_type(self, headless_ops):
        """forge.define_site_type switches a sphere site to box."""
        _create_link()
        bpy.ops.forge.create_site(site_type="SPHERE")
        site = _objects_of_type(cons.ModelTypes.SITE)[0]
        # change_site requires the current shape modifier to be present.
        attach_shape_modifier(site, cons.SiteShapeModifiers[cons.GeometryTypes.SPHERE])

        _select([site])
        assert bpy.ops.forge.define_site_type(site_type="BOX", apply_to_all=True) == {"FINISHED"}
        assert site.Forge_Geometry.type == cons.GeometryTypes.BOX

    def test_define_geometry_type(self, headless_ops):
        """forge.define_geometry_type switches a sphere visual to cylinder."""
        _deselect_all()
        bpy.ops.forge.create_geometry(geometry_type="SPHERE")
        visual = _objects_of_type(cons.ModelTypes.VISUAL)[0]
        # change_geometry requires the current shape modifier to be present.
        attach_shape_modifier(visual, cons.GeometryShapeModifiers[cons.GeometryTypes.SPHERE])

        _select([visual])
        assert bpy.ops.forge.define_geometry_type(geometry_type="CYLINDER", apply_to_all=True) == {"FINISHED"}
        assert visual.Forge_Geometry.type == cons.GeometryTypes.CYLINDER

    def test_define_collider_type(self, headless_ops):
        """forge.define_collider_type switches a box collider to sphere."""
        _deselect_all()
        bpy.ops.forge.create_collider(collider_type="BOX")
        collider = _objects_of_type(cons.ModelTypes.COLLIDER)[0]
        # change_collider requires the current shape modifier to be present.
        attach_shape_modifier(collider, cons.ColliderShapeModifiers[cons.GeometryTypes.BOX])

        _select([collider])
        assert bpy.ops.forge.define_collider_type(collider_type="SPHERE", apply_to_all=True) == {"FINISHED"}
        assert collider.Forge_Geometry.type == cons.GeometryTypes.SPHERE


class TestGizmoSizeOperator:
    @pytest.mark.parametrize("selected", [True, False])
    def test_scale_gizmo_size_does_not_scale_inertial(self, headless_ops, selected):
        from Forge.core.inertial import preview_matrix

        inertial = bpy.data.objects.new("InertialPreview", None)
        bpy.context.scene.collection.objects.link(inertial)
        inertial.Forge_Model_Type = cons.ModelTypes.INERTIAL
        inertial.empty_display_type = "CUBE"
        inertial.empty_display_size = 0.2
        inertial["_forge_gizmo_base_size"] = 0.2
        inertial.Forge_Inertial.mass = 3.0
        inertial.Forge_Inertial.diaginertia = (13, 10, 5)
        size_before = inertial.empty_display_size
        scale_before = tuple(inertial.scale)

        bpy.context.scene.Forge_Props.gizmo_scale = 4.0
        _select([inertial] if selected else [])
        assert bpy.ops.forge.scale_gizmo_size() == {"FINISHED"}
        assert bpy.ops.forge.scale_gizmo_size() == {"FINISHED"}

        assert inertial.empty_display_size == pytest.approx(size_before)
        assert tuple(inertial.scale) == pytest.approx(scale_before)
        assert tuple(column.length for column in preview_matrix(inertial).to_3x3().col) == pytest.approx((1, 2, 3))

    def test_scale_gizmo_size_scales_link_display(self, headless_ops):
        """forge.scale_gizmo_size scales the display size of selected links."""
        link = _create_link()
        base_size = link["_forge_gizmo_base_size"]

        forge_props = bpy.context.scene.Forge_Props
        forge_props.gizmo_scale = 2.0
        _select([link])
        assert bpy.ops.forge.scale_gizmo_size() == {"FINISHED"}
        assert bpy.ops.forge.scale_gizmo_size() == {"FINISHED"}

        assert link.empty_display_size == pytest.approx(base_size * 2.0)

    def test_gizmo_scale_edit_waits_for_the_operator(self, headless_ops):
        """``gizmo_scale`` is a stored setting, not an action: editing it leaves
        existing gizmos alone until ``forge.scale_gizmo_size`` runs, and the
        operator always re-derives from the captured base size."""
        link = _create_link()
        base_size = link["_forge_gizmo_base_size"]
        size_before_edit = link.empty_display_size

        bpy.context.scene.Forge_Props.gizmo_scale = 3.0

        assert link.empty_display_size == pytest.approx(size_before_edit)

        _select([link])
        assert bpy.ops.forge.scale_gizmo_size() == {"FINISHED"}
        assert link.empty_display_size == pytest.approx(base_size * 3.0)

        # Running it again re-derives from the base instead of compounding.
        assert bpy.ops.forge.scale_gizmo_size() == {"FINISHED"}
        assert link.empty_display_size == pytest.approx(base_size * 3.0)

    def test_camera_sensor_enum_excludes_contact(self, headless_ops):
        from Forge.ops.creation import Forge_OT_Sensor_Creation

        _deselect_all()
        bpy.ops.forge.create_camera(camera_type="PERSPECTIVE", camera_mode="FIXED")

        identifiers = [item[0] for item in Forge_OT_Sensor_Creation.sensor_enum_items(SimpleNamespace(), bpy.context)]

        assert cons.SensorTypes.Contact not in identifiers
