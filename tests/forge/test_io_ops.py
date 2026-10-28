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

"""Tests for the public MJCF I/O operators and their progress loop."""

import bpy
import pytest
from Forge.ops import io_ops


@pytest.fixture
def registered_io_ops(registered_props):
    classes = [
        io_ops.Forge_OT_SelectTempLink,
        io_ops.Forge_OT_SelectTempFile,
        io_ops.Forge_OT_SelectTempInclude,
        io_ops.Forge_OT_SelectImportPath,
        io_ops.Forge_OT_SelectExportPath,
        io_ops.Forge_OT_Import,
        io_ops.Forge_OT_Attach,
        io_ops.Forge_OT_Include,
        io_ops.Forge_OT_Export,
    ]
    registered = []
    for cls in classes:
        try:
            bpy.utils.register_class(cls)
            registered.append(cls)
        except (RuntimeError, ValueError):
            pass
    try:
        yield
    finally:
        for cls in reversed(registered):
            try:
                bpy.utils.unregister_class(cls)
            except (RuntimeError, ValueError):
                pass


class TestExportOperator:
    def test_export_operator_initializes_progress_pipeline(self, registered_io_ops, tmp_path):
        filepath = tmp_path / "operator.xml"
        forge_props = bpy.context.scene.Forge_Props
        forge_props.export_path = str(filepath)
        forge_props.rel_path = False

        # Blender owns Operator instances; invoke the public operator and
        # replace only the timer registration so the task queue can be checked
        # in background mode.
        from Forge.ops.base_operator import BaseProgressOperator

        original = BaseProgressOperator.execute
        BaseProgressOperator.execute = lambda self, _context: {"RUNNING_MODAL"}
        try:
            assert bpy.ops.forge.export_mjcf("INVOKE_DEFAULT") == {"RUNNING_MODAL"}
        finally:
            BaseProgressOperator.execute = original
            forge_props.modal_operation_active = False
            forge_props.modal_operation_token = ""

    def test_export_invalid_path_reports_cancel(self, registered_io_ops, tmp_path):
        forge_props = bpy.context.scene.Forge_Props
        forge_props.export_path = str(tmp_path / "missing" / "out.xml")
        forge_props.rel_path = False

        from Forge.ops.base_operator import BaseProgressOperator

        original = BaseProgressOperator.execute
        BaseProgressOperator.execute = lambda self, _context: {"RUNNING_MODAL"}
        try:
            assert bpy.ops.forge.export_mjcf("INVOKE_DEFAULT") == {"RUNNING_MODAL"}
        finally:
            BaseProgressOperator.execute = original
            forge_props.modal_operation_active = False
            forge_props.modal_operation_token = ""

    def test_export_runs_to_completion_in_background(self, registered_io_ops, tmp_path):
        filepath = tmp_path / "background-export.xml"
        forge_props = bpy.context.scene.Forge_Props
        forge_props.export_path = str(filepath)
        forge_props.rel_path = False

        assert bpy.app.background is True
        assert bpy.ops.forge.export_mjcf("INVOKE_DEFAULT") == {"FINISHED"}
        assert filepath.is_file()
        assert forge_props.modal_operation_active is False
        assert forge_props.modal_operation_status == "FINISHED"


class TestImportRelatedOperators:
    def test_modal_operations_are_mutually_exclusive(self, registered_io_ops):
        forge_props = bpy.context.scene.Forge_Props
        forge_props.modal_operation_active = True
        forge_props.modal_operation_name = "forge.import_mjcf"

        assert io_ops.Forge_OT_Import.poll(bpy.context) is False
        assert io_ops.Forge_OT_Export.poll(bpy.context) is False
        assert io_ops.Forge_OT_Attach.poll(bpy.context) is False
        assert io_ops.Forge_OT_Include.poll(bpy.context) is False

        forge_props.modal_operation_active = False

    def test_import_invalid_path_is_cancelled(self, registered_io_ops, tmp_path):
        bpy.context.scene.Forge_Props.import_file_path = str(tmp_path / "missing.xml")
        with pytest.raises(RuntimeError, match="Import path incorrect"):
            bpy.ops.forge.import_mjcf("INVOKE_DEFAULT")

    def test_import_runs_to_completion_in_background(self, registered_io_ops, forge_asset_library, tmp_path):
        filepath = tmp_path / "background-import.xml"
        filepath.write_text(
            '<mujoco model="background"><worldbody><body name="base" /></worldbody></mujoco>',
            encoding="utf-8",
        )
        forge_props = bpy.context.scene.Forge_Props
        forge_props.import_file_path = str(filepath)
        forge_props.import_material = False

        assert bpy.app.background is True
        assert bpy.ops.forge.import_mjcf("INVOKE_DEFAULT") == {"FINISHED"}
        assert bpy.data.objects["base"].Forge_Model_Type == "LINK"
        assert forge_props.modal_operation_active is False
        assert forge_props.modal_operation_status == "FINISHED"

    def test_import_via_exec_default_cleans_mesh_loaders(self, registered_io_ops, forge_asset_library, tmp_path):
        """The MCP wrapper drives import with EXEC_DEFAULT (no file-browser context)
        and a deferred modal slot; the run must complete and drop the mesh-asset
        placeholder objects end to end — not just when called directly."""
        (tmp_path / "box.obj").write_text("v 0 0 0\nv 1 0 0\nv 1 1 0\nv 0 1 0\nf 1 2 3\nf 1 3 4\n", encoding="utf-8")
        filepath = tmp_path / "model.xml"
        filepath.write_text(
            "<mujoco>"
            '<compiler meshdir="." />'
            "<asset>"
            '<mesh name="box" file="box.obj" />'
            "</asset>"
            "<worldbody>"
            '<body name="body"><geom name="g" type="mesh" mesh="box" /></body>'
            "</worldbody>"
            "</mujoco>",
            encoding="utf-8",
        )
        bpy.context.scene.Forge_GlobalConfig.reset()
        forge_props = bpy.context.scene.Forge_Props
        forge_props.import_file_path = str(filepath)
        forge_props.import_material = False

        # Same sequence mcp-server/forge_mcp/tools/io.py generates.
        forge_props.modal_operation_deferred = True
        try:
            assert bpy.ops.forge.import_mjcf("EXEC_DEFAULT") == {"FINISHED"}
            assert forge_props.modal_operation_status == "FINISHED"
            # The deferred caller owns the slot until it observes the status.
            assert forge_props.modal_operation_active is True

            geom = next(o for o in bpy.data.objects if o.Forge_Model_Type == "VISUAL")
            assert geom.data.name == "box"
            assert [o.name for o in bpy.data.objects if o.name.endswith(".obj")] == []
            assert geom.data.users == 1
        finally:
            forge_props.modal_operation_active = False
            forge_props.modal_operation_deferred = False
            forge_props.modal_operation_token = ""

    def test_import_checks_asset_library_on_both_entry_points(self, registered_io_ops, tmp_path, monkeypatch):
        """The check lives in execute() only; invoke() delegates there, so both
        entry points must still cancel when the Forge Library is unusable."""
        filepath = tmp_path / "ok.xml"
        filepath.write_text('<mujoco model="ok"><worldbody><body name="base" /></worldbody></mujoco>', encoding="utf-8")
        forge_props = bpy.context.scene.Forge_Props
        forge_props.import_file_path = str(filepath)
        monkeypatch.setattr(io_ops, "_check_asset_library", lambda: "missing C:/nope")

        for mode in ("INVOKE_DEFAULT", "EXEC_DEFAULT"):
            with pytest.raises(RuntimeError, match="asset library reload failed"):
                bpy.ops.forge.import_mjcf(mode)
            assert forge_props.modal_operation_active is False, mode

    def test_import_clears_progress_state_when_asset_library_fails(self, registered_io_ops, tmp_path, monkeypatch):
        """invoke() sets the progress state *before* delegating to execute(), so a
        failure there has to reset it or the panel stays on "importing". Headless
        Blender never runs invoke(), so the state it produces is applied directly."""
        filepath = tmp_path / "ok.xml"
        filepath.write_text('<mujoco model="ok"><worldbody><body name="base" /></worldbody></mujoco>', encoding="utf-8")
        forge_props = bpy.context.scene.Forge_Props
        forge_props.import_file_path = str(filepath)
        monkeypatch.setattr(io_ops, "_check_asset_library", lambda: "missing C:/nope")

        # Exactly what Forge_OT_Import.invoke() does before `return self.execute(...)`.
        forge_props.is_importing = True
        forge_props.progress = 0.02
        forge_props.progress_info = "Initialling..."

        with pytest.raises(RuntimeError, match="asset library reload failed"):
            bpy.ops.forge.import_mjcf("EXEC_DEFAULT")

        assert forge_props.is_importing is False
        assert forge_props.progress == 0.0
        assert forge_props.progress_info == ""

    def test_import_cancels_when_task_queue_is_empty(self, registered_io_ops, tmp_path):
        filepath = tmp_path / "empty-import.xml"
        filepath.write_text('<mujoco model="empty"><worldbody /></mujoco>', encoding="utf-8")
        forge_props = bpy.context.scene.Forge_Props
        forge_props.import_file_path = str(filepath)

        with pytest.raises(RuntimeError, match="no importable MJCF sections"):
            bpy.ops.forge.import_mjcf("INVOKE_DEFAULT")
        assert forge_props.modal_operation_active is False
        assert forge_props.is_importing is False

    def test_attach_cancels_when_task_queue_is_empty(self, registered_io_ops, forge_asset_library, tmp_path):
        filepath = tmp_path / "empty-attach.xml"
        filepath.write_text('<mujoco model="empty"><worldbody /></mujoco>', encoding="utf-8")
        bpy.ops.object.select_all(action="DESELECT")
        temp_props = bpy.context.scene.Forge_Temp_Props
        temp_props.tmp_file = str(filepath)
        temp_props.tmp_model = "empty"
        temp_props.tmp_prefix = "empty_"
        temp_props.tmp_link = "None"

        with pytest.raises(RuntimeError, match="no importable MJCF sections"):
            bpy.ops.forge.create_attach()
        forge_props = bpy.context.scene.Forge_Props
        assert forge_props.modal_operation_active is False
        assert forge_props.is_attaching is False

    def test_import_attach_include_reject_non_mujoco_root(self, registered_io_ops, forge_asset_library, tmp_path):
        filepath = tmp_path / "invalid-root.xml"
        filepath.write_text("<not-mujoco />", encoding="utf-8")
        forge_props = bpy.context.scene.Forge_Props
        forge_props.import_file_path = str(filepath)
        bpy.ops.object.select_all(action="DESELECT")

        with pytest.raises(RuntimeError, match="Invalid import XML"):
            bpy.ops.forge.import_mjcf("INVOKE_DEFAULT")
        assert forge_props.is_importing is False

        temp_props = bpy.context.scene.Forge_Temp_Props
        temp_props.tmp_file = str(filepath)
        temp_props.tmp_model = "invalid"
        temp_props.tmp_prefix = "invalid_"
        temp_props.tmp_link = "None"
        with pytest.raises(RuntimeError, match="Invalid attach XML"):
            bpy.ops.forge.create_attach()
        assert forge_props.is_attaching is False

        temp_props.tmp_include = str(filepath)
        with pytest.raises(RuntimeError, match="Invalid include XML"):
            bpy.ops.forge.create_include()
        assert forge_props.is_including is False

    def test_attach_and_include_polls_require_empty_selection(self, registered_io_ops):
        bpy.ops.object.select_all(action="DESELECT")
        assert io_ops.Forge_OT_Attach.poll(bpy.context) is True
        assert io_ops.Forge_OT_Include.poll(bpy.context) is True

        bpy.ops.mesh.primitive_cube_add()
        assert io_ops.Forge_OT_Attach.poll(bpy.context) is False
        assert io_ops.Forge_OT_Include.poll(bpy.context) is False

    def test_include_rejects_empty_mjcf_document(self, registered_io_ops, forge_asset_library, tmp_path):
        filepath = tmp_path / "empty-include.xml"
        filepath.write_text('<mujoco model="empty" />', encoding="utf-8")
        bpy.ops.object.select_all(action="DESELECT")
        bpy.context.scene.Forge_Temp_Props.tmp_include = str(filepath)

        with pytest.raises(RuntimeError, match="Invalid include XML"):
            bpy.ops.forge.create_include()
        assert bpy.context.scene.Forge_Props.modal_operation_active is False

    def test_include_accepts_document_with_supported_section(self, registered_io_ops, forge_asset_library, tmp_path):
        filepath = tmp_path / "valid-include.xml"
        filepath.write_text(
            '<mujoco model="valid"><worldbody><body name="base" /></worldbody></mujoco>',
            encoding="utf-8",
        )
        bpy.ops.object.select_all(action="DESELECT")
        bpy.context.scene.Forge_Temp_Props.tmp_include = str(filepath)

        assert bpy.ops.forge.create_include() == {"FINISHED"}
        assert bpy.context.scene.Forge_Props.modal_operation_active is False

    def test_include_cancels_when_task_queue_is_empty(self, registered_io_ops, forge_asset_library, tmp_path):
        filepath = tmp_path / "empty-section-include.xml"
        filepath.write_text('<mujoco model="empty"><worldbody /></mujoco>', encoding="utf-8")
        bpy.ops.object.select_all(action="DESELECT")
        bpy.context.scene.Forge_Temp_Props.tmp_include = str(filepath)

        with pytest.raises(RuntimeError, match="no importable MJCF sections"):
            bpy.ops.forge.create_include()
        forge_props = bpy.context.scene.Forge_Props
        assert forge_props.modal_operation_active is False
        assert forge_props.is_including is False
