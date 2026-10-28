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

"""Shared helpers for the MJCF export/import roundtrip tests.

Provides a reference scene builder (two-link robot with most MJCF element
types) and pipeline drivers that replicate the ``Forge_OT_Export`` /
``Forge_OT_Import`` operator task sequences without the modal timer loop
(which has no event loop in background Blender).
"""

import contextlib
import xml.etree.ElementTree as ET
from pathlib import Path

import bpy
from Forge.core import constants as cons
from Forge.core import function as funcs
from Forge.ops import exports as out

SHAPES_BLEND = Path(__file__).resolve().parents[2] / "addon" / "Forge" / "lib" / "assets" / "Shapes.blend"


# ═══════════════════════════════════════════════════════════════════════
# Headless shims
# ═══════════════════════════════════════════════════════════════════════


class _ObjectOpsProxy:
    """``bpy.ops.object`` proxy that no-ops ``modifier_add_node_group``."""

    def __init__(self, real):
        self._real = real

    def __getattr__(self, name):
        return getattr(self._real, name)

    def modifier_add_node_group(self, **_kwargs):
        return {"FINISHED"}


class _OpsProxy:
    """``bpy.ops`` proxy delegating everything except ``object``."""

    def __init__(self, real):
        self._real = real

    def __getattr__(self, name):
        if name == "object":
            return _ObjectOpsProxy(getattr(self._real, "object"))
        return getattr(self._real, name)


class _BpyProxy:
    """``bpy`` module proxy delegating everything except ``ops``."""

    def __init__(self, real):
        self._real = real

    def __getattr__(self, name):
        if name == "ops":
            return _OpsProxy(self._real.ops)
        return getattr(self._real, name)


@contextlib.contextmanager
def headless_shape_modifiers():
    """Make creation code skip ``bpy.ops.object.modifier_add_node_group``.

    The operator relies on the asset browser, whose libraries never finish
    loading in background Blender (it either warns "Asset loading is
    unfinished" or raises "No asset found at path"). Creation functions call
    it for display-only shape modifiers; tests attach the real node groups
    via :func:`attach_shape_modifier` where a modifier is actually needed.
    """
    from Forge.core import function as function_module
    from Forge.core import geometry_handler as geometry_handler_module

    patched = [(module, module.bpy, _BpyProxy(bpy)) for module in (function_module, geometry_handler_module)]
    for module, _original, proxy in patched:
        module.bpy = proxy
    try:
        yield
    finally:
        for module, original, _proxy in patched:
            module.bpy = original


def attach_shape_modifier(obj, modifier_name):
    """Attach a Forge shape node-group modifier to *obj* directly.

    ``bpy.ops.object.modifier_add_node_group`` relies on the asset browser,
    whose libraries never finish loading in background mode ("Asset loading
    is unfinished"), so the node group is linked from Shapes.blend instead.
    """
    with bpy.data.libraries.load(str(SHAPES_BLEND), link=False) as (data_from, data_to):
        data_to.node_groups = [name for name in data_from.node_groups if name == modifier_name]
    modifier = obj.modifiers.new(modifier_name, "NODES")
    modifier.node_group = bpy.data.node_groups[modifier_name]


def collector(messages):
    """Return an operator ``report`` callback that records every message."""

    def report(kind, message):
        messages.append((tuple(kind), message))

    return report


def _select(ordered):
    """Select objects in order, tagging them with ``selected_order``."""
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
    for index, obj in enumerate(ordered):
        obj["selected_order"] = index
        obj.select_set(True)
    bpy.context.view_layer.objects.active = ordered[-1] if ordered else None


def _deselect_all():
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
    bpy.context.view_layer.objects.active = None


def build_scene(context):
    """Build a two-link robot covering most MJCF element types.

    Follows the forge_create skill rules: every element is created through
    ``bpy.ops.forge.create_<type>`` (never the internal ``funcs.add_*`` API),
    the root link is marked with ``forge.mark_root_link()``, and transforms
    are changed after creation.

    Requires the creation operators to be registered (``registered_ops``).
    Returns the created objects as a dict keyed by element role.
    """
    with headless_shape_modifiers():
        return _build_scene(context)


def _build_scene(context):
    objects = {}

    # Root link (nothing selected → created in the World collection).
    _deselect_all()
    bpy.ops.forge.create_link()
    objects["root"] = context.active_object
    bpy.ops.forge.mark_root_link()

    # Child link under the root, offset along Z per the modify-order rule.
    _select([objects["root"]])
    bpy.ops.forge.create_link()
    objects["child"] = context.active_object
    objects["child"].location = (0.0, 0.0, 1.0)

    # A primitive visual on the child link (template-material path).
    _select([objects["child"]])
    bpy.ops.forge.create_geometry(geometry_type="SPHERE")
    objects["visual"] = context.active_object
    attach_shape_modifier(objects["visual"], cons.GeometryShapeModifiers[cons.GeometryTypes.SPHERE])

    # Hinge joint on the child link.
    _select([objects["child"]])
    bpy.ops.forge.create_joint(joint_type="HINGE")
    objects["joint"] = context.active_object

    # Position actuator + jointpos sensor on the joint.
    _select([objects["joint"]])
    bpy.ops.forge.create_actuator(actuator_type="POSITION")
    objects["actuator"] = context.active_object

    _select([objects["joint"]])
    bpy.ops.forge.create_sensor(Sensor_Type="Jointpos")
    objects["sensor"] = context.active_object

    # Weld equality and contact exclude between the two links (ordered selection).
    _select([objects["root"], objects["child"]])
    bpy.ops.forge.create_equality(equality_type="WELD")
    objects["equality"] = context.active_object

    _select([objects["root"], objects["child"]])
    bpy.ops.forge.create_contact(contact_type="EXCLUDE")
    objects["contact"] = context.active_object

    # World light and camera (nothing selected).
    _deselect_all()
    bpy.ops.forge.create_light(light_type="DIRECTIONAL", light_mode="FIXED")
    objects["light"] = context.active_object

    # create_light leaves the new light selected — deselect again for the camera poll.
    _deselect_all()
    bpy.ops.forge.create_camera(camera_type="PERSPECTIVE", camera_mode="FIXED")
    objects["camera"] = context.active_object

    return objects


def run_export(context, filepath):
    """Run the full export pipeline (the operator's task sequence) on the current scene.

    Returns (messages, xml root element).
    """
    forge_props = context.scene.Forge_Props
    forge_props.export_path = str(filepath)
    forge_props.rel_path = False

    messages = []
    report = collector(messages)

    geometry_map = {}
    attach_model_map = {}
    hfield_map = {}
    collider_map = {}
    geo_materials_map = {}
    materials_map = {}
    materials_props_map = {}

    instance_templates = funcs.collect_instance_templates(report)
    funcs.find_assets(
        context,
        geometry_map,
        attach_model_map,
        hfield_map,
        collider_map,
        geo_materials_map,
        materials_map,
        materials_props_map,
        report,
        instance_templates,
    )

    root = ET.Element("mujoco")
    out.add_include(context, root, str(filepath).rsplit("/", 1)[0])
    out.add_compiler(context, root)
    out.add_option(context, root)
    out.add_statistic(context, root)
    out.add_visual(context, root)
    out.add_asset(root, geometry_map, attach_model_map, hfield_map, collider_map, materials_props_map, report)
    out.set_world(context, root, geometry_map, hfield_map, collider_map, geo_materials_map, report, instance_templates)
    out.add_contact(context, root, report)
    out.add_equality(context, root, report)
    out.add_tendon(context, root, report)
    out.add_actuator(context, root, report)
    out.add_sensor(context, root, report)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(out.prettify(root))

    return messages, ET.parse(filepath).getroot()
