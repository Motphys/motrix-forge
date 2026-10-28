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

"""
Base operator classes that eliminate boilerplate in creation / definition operators.

Usage:

    class Forge_OT_MyThing_Creation(BaseCreationOperator):
        bl_idname = "forge.create_my_thing"
        bl_label = "Create my thing(s)"
        collection_tag = cons.CollectionNames.MYTHING
        poll_model_types = [cons.ModelTypes.LINK]

        def create_single(self, context, report, collection, parent_obj):
            return funcs.add_my_thing(context, report, collection, parent_obj)

    class Forge_OT_MyThing_Define(BaseDefineOperator):
        bl_idname = "forge.define_my_thing"
        bl_label = "Define my thing(s)"
        poll_model_types = [cons.ModelTypes.MYTHING]
        type_prop_name = "my_type"
        type_items = MY_TYPES

    class Forge_OT_ExportModal(BaseProgressOperator):
        bl_idname = "forge.export_modal"
        bl_label = "Export MJCF"

        def task_setup(self, context): ...
        def build_steps(self, context): ...
"""

from __future__ import annotations

import time
from typing import ClassVar

import bpy
from bpy.props import BoolProperty
from bpy.types import Context, Operator

from ..core import function as funcs
from ..core import selection as sel

# ── Base creation operator ──────────────────────────────────────────


class BaseCreationOperator(Operator):
    """Iterate selected objects, create one per selection, or standalone.

    Subclasses override:
      * ``create_single(context, report, collection, parent_obj)``
      * Set class vars *collection_tag* and optionally *poll_model_types*.
    """

    bl_options = {"REGISTER", "UNDO"}

    collection_tag: ClassVar[str] = ""
    poll_model_types: ClassVar[list[str] | None] = None
    show_dialog: ClassVar[bool] = False  # Set True if the operator has a dialog

    def create_single(self, context: Context, report, collection, parent_obj):
        """Create and return one object (parent_obj may be None)."""
        raise NotImplementedError

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected object types.

        Returns True when no poll_model_types filter is set, when the selection
        matches the required model types, or when nothing is selected (standalone
        creation path).
        """
        if cls.poll_model_types is None:
            return True
        return sel.check_selected_model_types(context, cls.poll_model_types) or (
            context.selected_objects is not None and not context.selected_objects
        )

    def execute(self, context: Context):
        """Create objects for all selected targets, or a single standalone object.

        Iterates the selection (or uses a single None entry when nothing is
        selected), calling create_single for each target. New objects are
        selected after creation.
        """
        collection = funcs.get_collection(context, self.collection_tag)

        targets = [None]
        if len(context.selected_objects) > 1:
            targets = (
                sel.get_ordered_selection_objects(context)
                if "selected_order" in context.selected_objects[0] and len(context.selected_objects) > 1
                else list(context.selected_objects)
            )
        elif len(context.selected_objects) == 1:
            targets = [context.selected_objects[0]]

        new_objs = []
        for obj in targets:
            sel.clear_select()
            new = self.create_single(context, self.report, collection, obj)
            if new is not None:
                new_objs.append(new)

        for obj in new_objs:
            obj.select_set(True)
        funcs.update_ui(context)
        return {"FINISHED"}

    def invoke(self, context: Context, event):
        """Show a property dialog if show_dialog is set, otherwise execute directly."""
        if self.show_dialog:
            return context.window_manager.invoke_props_dialog(self)
        return self.execute(context)


# ── Base definition operator (apply_to_all + type) ─────────────────


class BaseDefineOperator(Operator):
    """Change a property (typically the type) of selected objects.

    Subclasses override *apply_type* and set *poll_model_types*.
    """

    bl_options = {"REGISTER", "UNDO"}

    poll_model_types: ClassVar[list[str] | None] = None

    apply_to_all: BoolProperty(
        name="Apply to all selected",
        default=False,
        description="Apply to all selected objects instead of only the active one",
    )  # type: ignore

    type: ClassVar[str] = ""

    def apply_type(self, context: Context, obj, new_type: str):
        """Apply the selected model type to the target object.

        Subclasses must override this method to perform the actual type
        change logic (e.g. updating object properties or modifiers).

        Args:
            context: The active Blender context.
            obj: The target Blender object.
            new_type: The model type string to apply.
        """
        raise NotImplementedError

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected model types.

        Returns True when no poll_model_types filter is set, or when the
        selection matches the required model types.
        """
        if cls.poll_model_types is None:
            return True
        return sel.check_selected_model_types(context, cls.poll_model_types)

    def execute(self, context: Context):
        """Apply the type change to selected objects.

        When apply_to_all is True, all selected objects are modified.
        Otherwise only the active object is changed.
        """
        targets = list(context.selected_objects) if self.apply_to_all else [context.active_object]
        if not targets or any(obj is None for obj in targets):
            self.report({"WARNING"}, "No active object selected")
            return {"CANCELLED"}
        for obj in targets:
            sel.clear_select()
            obj.select_set(True)
            context.view_layer.objects.active = obj
            self.apply_type(context, obj, self.type)
        for obj in targets:
            obj.select_set(True)

        funcs.update_ui(context)
        return {"FINISHED"}

    def invoke(self, context: Context, event):
        """Show a property dialog to let the user choose whether to apply to all selected objects."""
        return context.window_manager.invoke_props_dialog(self)


# ═══════════════════════════════════════════════════════════════════════
# Base progress operator — modal long-running task with UI feedback
# ═══════════════════════════════════════════════════════════════════════


class BaseProgressOperator(Operator):
    """Modal operator base for long-running tasks with progress bar and UI feedback."""

    bl_options = {"REGISTER"}

    total_stage_task_count: int = 1
    main_task_count: int = 1
    stage_task_count: int = 1
    action_task_count: int = 1

    sum_stage_index: int = 0

    main_task_index: int = 0
    stage_task_index: int = 0
    action_task_index: int = 0
    do_next_task: bool = False
    end_tasks: bool = False

    # ── Private state ────────────────────────────────────────────────
    _timer = None
    _timer_count = 0
    _modal_operation_token: str | None = None
    # ── Subclass API ─────────────────────────────────────────────────

    def go_next_action(self):
        """Advance to the next action within the current stage.

        Subclasses override this to define their action execution logic.
        """
        raise NotImplementedError

    def go_next_main_task(self, context: Context, init: bool = False):
        """Advance to the next main task in the pipeline.

        Args:
            context: The Blender context.
            init: True on first call during initialization.
        """
        raise NotImplementedError

    def go_next_stage_task(self):
        """Advance to the next stage within the current main task.

        Subclasses override this to define stage transition logic.
        """
        raise NotImplementedError

    def progress_task(self, context: Context):
        """Execute the current task and report progress.

        Args:
            context: The Blender context.

        Returns:
            True to continue, False to cancel.
        """
        raise NotImplementedError

    def reset_ui(self, context: Context):
        """Reset UI state after the modal task completes.

        Args:
            context: The Blender context.
        """
        raise NotImplementedError

    def update_progress(self, context: Context):
        """Update progress bar and UI during task execution.

        Args:
            context: The Blender context.
        """
        raise NotImplementedError

    # ── Entry point ──────────────────────────────────────────────────

    @classmethod
    def modal_operation_available(cls, context: Context) -> bool:
        """Return whether the main scene is free for a modal Forge operation."""
        try:
            scene = context.scene
            forge_props = context.blend_data.scenes[scene.Main_Scene].Forge_Props
        except (AttributeError, KeyError, TypeError):
            return False
        return not forge_props.modal_operation_active

    def begin_modal_operation(self) -> bool:
        """Claim the scene-level modal-operation slot for this operator instance."""
        forge_props = getattr(self, "forge_props", None)
        if forge_props is None:
            return True

        token = self._modal_operation_token
        if token and forge_props.modal_operation_active and forge_props.modal_operation_token == token:
            return True
        if forge_props.modal_operation_active:
            self.report({"ERROR"}, f"Forge modal operation already running: {forge_props.modal_operation_name}")
            return False

        token = f"{self.bl_idname}:{id(self)}:{time.monotonic_ns()}"
        self._modal_operation_token = token
        forge_props.modal_operation_active = True
        forge_props.modal_operation_name = self.bl_idname
        forge_props.modal_operation_token = token
        forge_props.modal_operation_status = "RUNNING"
        forge_props.modal_operation_message = ""
        forge_props.cancel_requested = False
        return True

    def set_modal_operation_result(self, status: str, message: str = "", *, release: bool = False) -> None:
        """Record this operator's terminal status without overwriting another owner's state."""
        forge_props = getattr(self, "forge_props", None)
        token = self._modal_operation_token
        if forge_props is None or token is None or forge_props.modal_operation_token != token:
            return
        forge_props.modal_operation_status = status
        forge_props.modal_operation_message = message
        if release:
            forge_props.modal_operation_active = False
            forge_props.modal_operation_token = ""

    def abort_modal_operation(self, message: str) -> None:
        """Record an initialization failure and release the modal-operation slot."""
        self.set_modal_operation_result("ERROR", message, release=True)

    def _advance_progress_task(self, context: Context) -> bool:
        """Run one task and advance the shared stage/action indices."""
        self.do_next_task = False
        if not self.progress_task(context):
            return False

        self.action_task_index += 1
        if self.action_task_index == self.action_task_count:
            self.action_task_index = 0
            self.stage_task_index += 1
            self.sum_stage_index += 1

            if self.stage_task_index == self.stage_task_count:
                self.stage_task_index = 0
                self.main_task_index += 1

                if self.main_task_index == self.main_task_count:
                    self.end_tasks = True
                self.go_next_main_task(context)
            else:
                self.go_next_stage_task()
        return True

    def _execute_blocking(self, context: Context):
        """Run the progress pipeline synchronously for ``blender --background``."""
        while not self.end_tasks:
            self.update_progress(context)
            if not self.do_next_task:
                message = "Operation task loop stalled"
                self.set_modal_operation_result("ERROR", message)
                self.finish(context)
                self.report({"ERROR"}, message)
                return {"CANCELLED"}
            try:
                if not self._advance_progress_task(context):
                    message = "Operation task failed"
                    self.set_modal_operation_result("ERROR", message)
                    self.finish(context)
                    self.report({"ERROR"}, message)
                    return {"CANCELLED"}
            except Exception as ex:  # pylint: disable=broad-exception-caught
                message = f"Task failed: {ex}"
                self.set_modal_operation_result("ERROR", message)
                self.finish(context)
                self.report({"ERROR"}, message)
                return {"CANCELLED"}

        self.set_modal_operation_result("FINISHED")
        self.finish(context)
        return {"FINISHED"}

    def execute(self, context: Context):
        """Start the modal task loop."""
        self._start_time = time.time()

        if not self.begin_modal_operation():
            return {"CANCELLED"}

        self.end_tasks = False
        self._timer_count = 0

        if bpy.app.background:
            return self._execute_blocking(context)

        wm = context.window_manager
        try:
            self._timer = wm.event_timer_add(0.005, window=context.window)
            wm.modal_handler_add(self)
        except Exception as ex:  # pylint: disable=broad-exception-caught
            message = f"Failed to start modal operation: {ex}"
            self.abort_modal_operation(message)
            self.reset_ui(context)
            self.report({"ERROR"}, message)
            return {"CANCELLED"}
        if context.area is not None:
            context.area.tag_redraw()
        return {"RUNNING_MODAL"}

    def modal(self, context: Context, event):
        """Handle modal timer events and drive the task loop.

        Args:
            context: The Blender context.
            event: The current window event.
        """
        forge_props = getattr(self, "forge_props", None)
        if forge_props is not None and forge_props.cancel_requested:
            forge_props.cancel_requested = False
            self.set_modal_operation_result("CANCELLED", "Operation cancelled")
            self.finish(context)
            self.report({"INFO"}, "Operation cancelled")
            return {"CANCELLED"}

        if not self.end_tasks:
            self.update_progress(context)

        if event.type == "ESC":
            self.set_modal_operation_result("CANCELLED", "Operation cancelled by user")
            self.finish(context)
            self.report({"INFO"}, "Operation cancelled")
            return {"CANCELLED"}

        if event.type == "TIMER":
            if self.end_tasks:
                self.set_modal_operation_result("FINISHED")
                self.finish(context)
                return {"FINISHED"}

            if self.do_next_task:
                try:
                    if not self._advance_progress_task(context):
                        self.set_modal_operation_result("ERROR", "Operation task failed")
                        self.finish(context)
                        self.report({"ERROR"}, "Operation task failed")
                        return {"CANCELLED"}
                except Exception as ex:  # pylint: disable=broad-exception-caught
                    self.set_modal_operation_result("ERROR", f"Task failed: {ex}")
                    self.finish(context)
                    self.report({"ERROR"}, f"Task fail: {str(ex):s}")
                    return {"CANCELLED"}

                return {"PASS_THROUGH"}

        return {"PASS_THROUGH"}

    # ── Internal helpers ─────────────────────────────────────────────

    def finish(self, context: Context):
        """Clean up timer, progress, and additional."""
        try:
            self.reset_ui(context)
            wm = context.window_manager
            if self._timer is not None:
                wm.event_timer_remove(self._timer)
                self._timer = None
            if context.area is not None:
                context.area.tag_redraw()
            execution_time = time.time() - self._start_time
            self.report({"INFO"}, f"Execution Time: {execution_time} seconds")
        finally:
            forge_props = getattr(self, "forge_props", None)
            self.set_modal_operation_result(
                getattr(forge_props, "modal_operation_status", "CANCELLED"),
                getattr(forge_props, "modal_operation_message", ""),
                release=not getattr(forge_props, "modal_operation_deferred", False),
            )
