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

"""glTF dependency failures must precede destructive I/O work."""

import addon_utils
import bpy
import pytest
from Forge.core import dependency
from Forge.core import function as funcs
from Forge.ops import imports as load
from Forge.ops import io_ops

from .test_io_ops import registered_io_ops  # noqa: F401


@pytest.fixture
def disabled_gltf():
    was_loaded = addon_utils.check("io_scene_gltf2")[1]
    if was_loaded:
        addon_utils.disable("io_scene_gltf2", default_set=False)
    try:
        assert not addon_utils.check("io_scene_gltf2")[1]
        yield
    finally:
        if was_loaded:
            addon_utils.enable("io_scene_gltf2", default_set=False)


@pytest.mark.parametrize("operation", ["import", "export"])
def test_disabled_addon_has_actionable_error(disabled_gltf, operation):
    with pytest.raises(RuntimeError, match="Enable it in Edit > Preferences > Add-ons"):
        dependency.require_gltf_addon(operation)


def test_glb_helper_fails_without_creating_datablocks(disabled_gltf, tmp_path):
    before = {kind: set(getattr(bpy.data, kind)) for kind in ("objects", "meshes", "collections")}
    with pytest.raises(RuntimeError, match="io_scene_gltf2"):
        load._import_glb_mesh(bpy.context, str(tmp_path / "unused.glb"))
    for kind, datablocks in before.items():
        assert set(getattr(bpy.data, kind)) == datablocks


def test_glb_export_preserves_selection_transform_uv(disabled_gltf, tmp_path):
    bpy.ops.mesh.primitive_plane_add(location=(3, 2, 1))
    obj = bpy.context.object
    bpy.context.view_layer.update()
    obj.select_set(False)
    matrix = obj.matrix_world.copy()
    uvs = [tuple(uv.vector) for uv in obj.data.uv_layers[0].uv]
    with pytest.raises(RuntimeError, match="io_scene_gltf2"):
        funcs.export_assets(obj, str(tmp_path), False, True)
    assert obj.matrix_world == matrix
    assert not obj.select_get()
    assert [tuple(uv.vector) for uv in obj.data.uv_layers[0].uv] == uvs
    assert list(tmp_path.iterdir()) == []
    assert funcs.export_assets(obj, str(tmp_path), True, True).endswith(".glb")
    assert funcs.export_assets(obj, str(tmp_path), False, False).endswith(".obj")
    assert list(tmp_path.glob("*.obj"))


@pytest.mark.parametrize("reference", ["direct", "default", "include"])
@pytest.mark.usefixtures("registered_io_ops")
def test_import_preflight_preserves_scene(disabled_gltf, tmp_path, monkeypatch, reference):
    asset = '<asset><mesh name="shape" file="mesh.GLB"/></asset>'
    if reference == "default":
        asset = '<default><mesh file="mesh.GLB"/></default><asset><mesh name="shape"/></asset>'
    elif reference == "include":
        (tmp_path / "child.xml").write_text(f"<mujoco>{asset}</mujoco>", encoding="utf-8")
        asset = '<include file="child.xml"/>'
    filepath = tmp_path / "input.xml"
    filepath.write_text(f'<mujoco model="dependency">{asset}<worldbody/></mujoco>', encoding="utf-8")
    bpy.ops.mesh.primitive_cube_add(location=(4, 5, 6))
    sentinel = bpy.context.object
    before = set(bpy.data.objects)
    props = bpy.context.scene.Forge_Props
    props.import_file_path = str(filepath)
    monkeypatch.setattr(io_ops, "_check_asset_library", lambda: None)
    with pytest.raises(RuntimeError, match="io_scene_gltf2"):
        bpy.ops.forge.import_mjcf("EXEC_DEFAULT")
    assert set(bpy.data.objects) == before
    assert tuple(sentinel.location) == (4, 5, 6)
    assert not props.modal_operation_active


@pytest.mark.usefixtures("registered_io_ops")
def test_export_preflight_before_output(disabled_gltf, tmp_path):
    props = bpy.context.scene.Forge_Props
    props.export_path = str(tmp_path / "out.xml")
    props.rel_path = False
    props.use_glb = True
    props.update_forge_only = False
    try:
        with pytest.raises(RuntimeError, match="io_scene_gltf2"):
            bpy.ops.forge.export_mjcf("EXEC_DEFAULT")
        assert list(tmp_path.iterdir()) == []
        assert not props.modal_operation_active
        props.update_forge_only = True
        assert bpy.ops.forge.export_mjcf("EXEC_DEFAULT") == {"FINISHED"}
        assert (tmp_path / "out.xml").is_file()
    finally:
        props.use_glb = False
        props.update_forge_only = False


@pytest.mark.parametrize("operation, namespace", [("import", "import_scene"), ("export", "export_scene")])
def test_enabled_addon_requires_registered_operator(monkeypatch, operation, namespace):
    from types import SimpleNamespace

    monkeypatch.setattr(addon_utils, "check", lambda _: (True, True))
    monkeypatch.setattr(bpy.ops, namespace, SimpleNamespace())
    with pytest.raises(RuntimeError, match="operator is unavailable"):
        dependency.require_gltf_addon(operation)
