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

"""Shared pytest configuration for Forge integration tests."""

import sys
from importlib import import_module
from pathlib import Path

import pytest

ADDON_ROOT = Path(__file__).resolve().parents[2] / "addon"
ADDON_PKG = ADDON_ROOT / "Forge"
if str(ADDON_ROOT) not in sys.path:
    sys.path.insert(0, str(ADDON_ROOT))

try:
    import bpy
except ImportError:
    pytest.skip("bpy not available — integration tests skipped", allow_module_level=True)

if not bpy.app.background:
    pytest.skip("Forge integration tests require Blender background mode", allow_module_level=True)


def pytest_report_header():
    import bpy

    return [f"bpy: {bpy.app.version_string}   addon: Forge"]


# ── Helpers for working with Blender in background mode ────────────


def select_objects(objects):
    """Set Blender selection to given objects."""
    import bpy

    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
    if objects:
        bpy.context.view_layer.objects.active = objects[0]


# ── Fixtures ───────────────────────────────────────────────────────


def _register_classes(classes):
    """Register classes and return only those newly registered here."""
    registered = []
    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except (RuntimeError, ValueError):
            continue
        registered.append(cls)
    return registered


def _unregister_classes(classes):
    """Unregister classes in reverse dependency order."""
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except (RuntimeError, ValueError):
            pass


@pytest.fixture(autouse=True)
def fresh_scene():
    """Yield scene, then destroy all new data blocks and reset Blender state."""
    import bpy

    snapshot = _data_snapshot()
    bpy.ops.object.select_all(action="DESELECT")
    if bpy.context.view_layer.objects.active:
        bpy.context.view_layer.objects.active = None
    yield bpy.context.scene
    bpy.ops.object.select_all(action="DESELECT")
    if bpy.context.view_layer.objects.active:
        bpy.context.view_layer.objects.active = None
    _data_restore(snapshot)


@pytest.fixture
def registered_props(fresh_scene):
    """Register Forge property groups on Blender types directly.

    Bypasses the full addon ``register()`` (which needs addon prefs and
    asset libraries) and only registers the PropertyGroup classes.
    """
    import bpy
    from Forge.core import props

    if hasattr(bpy.types.Object, "Forge_Model_Type"):
        yield
        return

    registered = _register_classes(props.classes)
    props.register_forge_model_props()
    try:
        yield
    finally:
        props.unregister_forge_model_props()
        _unregister_classes(registered)


@pytest.fixture
def registered_ops(registered_props):
    """Register testable operators on top of properties.

    Registers the subset of operators that don't need Shapes.blend assets
    or full addon preferences.  This lets tests call ``bpy.ops.forge.xxx()``.
    """

    # Operators testable without the asset browser — creation code paths that
    # call bpy.ops.object.modifier_add_node_group need the
    # mjcf_helpers.headless_shape_modifiers shim in background mode.
    # Each tuple: (module, class_name)
    _op_sources = [
        ("Forge.ops.definition", "Forge_OT_Type_Define"),
        ("Forge.ops.definition", "Forge_OT_Geometry_Define"),
        ("Forge.ops.definition", "Forge_OT_Collider_Define"),
        ("Forge.ops.definition", "Forge_OT_Site_Define"),
        ("Forge.ops.definition", "Forge_OT_Joint_Define"),
        ("Forge.ops.definition", "Forge_OT_Actuator_Define"),
        ("Forge.ops.definition", "Forge_OT_Parent_Define"),
        ("Forge.ops.utilities", "Forge_OT_Batch_Rename"),
        ("Forge.ops.creation", "Forge_OT_Link_Creation"),
        ("Forge.ops.creation", "Forge_OT_Link_MarkRoot"),
        ("Forge.ops.utilities", "Forge_OT_SelectByTAG"),
        ("Forge.ops.utilities", "Forge_OT_SelectByModelType"),
        ("Forge.ops.utilities", "Forge_OT_SelectHulls"),
        ("Forge.ops.creation", "Forge_OT_Change_Gizmo_Size"),
        ("Forge.ops.creation", "Forge_OT_Frame_Creation"),
        ("Forge.ops.creation", "Forge_OT_Mesh_Check"),
        ("Forge.ops.utilities", "Forge_OT_InstanceSet"),
        ("Forge.ops.utilities", "Forge_OT_Instance_Mark"),
        ("Forge.ops.creation", "Forge_OT_HeightField_Creation"),
        ("Forge.ops.creation", "Forge_OT_Plane_Creation"),
        ("Forge.ops.creation", "Forge_OT_Inertial_Creation"),
        ("Forge.ops.materials", "Forge_OT_Material_Creation"),
        ("Forge.ops.materials", "Forge_OT_Checker_Material_Creation"),
        ("Forge.ops.materials", "Forge_OT_Material_Assign"),
        ("Forge.ops.creation", "Forge_OT_Geometry_Creation"),
        ("Forge.ops.creation", "Forge_OT_Collider_Creation"),
        ("Forge.ops.creation", "Forge_OT_Site_Creation"),
        ("Forge.ops.creation", "Forge_OT_Joint_Creation"),
        ("Forge.ops.creation", "Forge_OT_Actuator_Creation"),
        ("Forge.ops.creation", "Forge_OT_Tendon_Creation"),
        ("Forge.ops.creation", "Forge_OT_Equality_Creation"),
        ("Forge.ops.creation", "Forge_OT_Sensor_Creation"),
        ("Forge.ops.creation", "Forge_OT_Contact_Creation"),
        ("Forge.ops.creation", "Forge_OT_Light_Creation"),
        ("Forge.ops.creation", "Forge_OT_Camera_Creation"),
        ("Forge.ops.creation", "Forge_OT_Replicate_Creation"),
    ]
    classes = [getattr(import_module(mod_path), cls_name) for mod_path, cls_name in _op_sources]
    registered = _register_classes(classes)
    try:
        yield
    finally:
        _unregister_classes(registered)


@pytest.fixture
def asset_lib_available():
    """Check whether the Shapes.blend library is available.

    Many tests don't need modifiers — they just need property access.
    """
    lib_path = ADDON_PKG / "lib" / "assets" / "Shapes.blend"
    return lib_path.exists()


@pytest.fixture
def forge_asset_library(asset_lib_available):
    """Register the Forge Library asset library in preferences (headless-safe).

    Mirrors what the addon ``register()`` does, so operators that add
    geometry-node modifiers from Shapes.blend work in tests.
    """
    import bpy

    if not asset_lib_available:
        pytest.fail("Forge Library Shapes.blend is required for this test suite")

    libraries = bpy.context.preferences.filepaths.asset_libraries
    asset_directory = str(ADDON_PKG / "lib" / "assets")
    if "Forge Library" in libraries:
        entry = libraries["Forge Library"]
        original_path = entry.path
        original_import_method = entry.import_method
        entry.path = asset_directory
        libraries.update()
        try:
            yield
        finally:
            entry.path = original_path
            entry.import_method = original_import_method
            libraries.update()
        return

    entry = libraries.new(name="Forge Library", directory=asset_directory)
    libraries.update()
    try:
        yield
    finally:
        libraries.remove(entry)
        libraries.update()


# ── Internal ───────────────────────────────────────────────────────


def _data_snapshot():
    import bpy

    return {
        "objects": set(bpy.data.objects),
        "meshes": set(bpy.data.meshes),
        "cameras": set(bpy.data.cameras),
        "lights": set(bpy.data.lights),
        "node_groups": set(bpy.data.node_groups),
        "collections": set(bpy.data.collections),
        "materials": set(bpy.data.materials),
        "images": set(bpy.data.images),
    }


def _data_restore(snapshot):
    import bpy

    for obj in set(bpy.data.objects) - snapshot["objects"]:
        bpy.data.objects.remove(obj, do_unlink=True)
    for mesh in set(bpy.data.meshes) - snapshot["meshes"]:
        bpy.data.meshes.remove(mesh)
    for camera in set(bpy.data.cameras) - snapshot["cameras"]:
        bpy.data.cameras.remove(camera)
    for light in set(bpy.data.lights) - snapshot["lights"]:
        bpy.data.lights.remove(light)
    for node_group in set(bpy.data.node_groups) - snapshot["node_groups"]:
        bpy.data.node_groups.remove(node_group)
    for coll in set(bpy.data.collections) - snapshot["collections"]:
        bpy.data.collections.remove(coll)
    for mat in set(bpy.data.materials) - snapshot["materials"]:
        bpy.data.materials.remove(mat)
    for img in set(bpy.data.images) - snapshot["images"]:
        bpy.data.images.remove(img)
