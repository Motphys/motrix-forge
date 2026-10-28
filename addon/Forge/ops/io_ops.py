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
Import / Export / Attach / Include operators.

Registered via ``operator.classes``.
"""

from __future__ import annotations

import os
import time
import xml.etree.ElementTree as ET
from collections.abc import Callable
from os.path import basename
from pathlib import Path
from typing import Any

import bpy
from bpy.props import EnumProperty, StringProperty
from bpy.types import Collection, Context, Image, Object, Operator, Scene
from bpy_extras.io_utils import ImportHelper

from ..core import constants as cons
from ..core import function as funcs
from ..core import selection as sel
from ..core.dependency import require_gltf_addon
from ..core.props import Forge_Props, ReplicateItem, Temp_Props
from ..core.utils import AssetsData, Scene_Data, Section, Sections
from . import exports as out
from . import imports as load
from .base_operator import BaseProgressOperator


def _check_asset_library() -> str | None:
    """Ensure the Forge Library asset library is loaded, reloading it if needed.

    If the "Forge Library" entry is missing from the asset library preferences,
    or its configured directory no longer contains the ``Shapes.blend`` asset
    bundle, the entry is (re)created pointing to the addon's ``lib`` directory
    and the asset library list is updated to reload it.

    Returns:
        None when the library is valid, otherwise an error reason naming the
        directory that failed the check.
    """
    asset_libraries = bpy.context.preferences.filepaths.asset_libraries
    lib_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "lib", "assets"))

    needs_update = False
    if "Forge Library" not in asset_libraries:
        asset_libraries.new(name="Forge Library", directory=lib_dir)
        needs_update = True
    else:
        library = asset_libraries["Forge Library"]
        current_dir = os.path.abspath(bpy.path.abspath(library.path))
        # normcase/normpath so a merely differently-written path (case, trailing
        # separator) is not treated as broken — re-pointing it would force an
        # asset-library reload on every call, which is what this check avoids.
        expected = os.path.normcase(os.path.normpath(os.path.abspath(lib_dir)))
        if (
            os.path.normcase(os.path.normpath(current_dir)) != expected
            or not os.path.isdir(current_dir)
            or not os.path.exists(os.path.join(current_dir, "Shapes.blend"))
        ):
            library.path = lib_dir
            needs_update = True

    # Updating Blender's asset-library registry can fail in an INVOKE/deferred
    # bridge call when no file-browser/window context exists.  A valid existing
    # entry needs no reload; only update after creating or repairing it.
    if needs_update:
        asset_libraries.update()
    if os.path.isdir(lib_dir) and os.path.exists(os.path.join(lib_dir, "Shapes.blend")):
        return None
    return f"missing {lib_dir}"


def _validate_mjcf_file(path: Path, operation: str) -> str | None:
    """Return an error message when *path* is not an importable MJCF file.

    Import, Attach, and Include all consume the same top-level MJCF document
    format.  Keep this validation shared so malformed roots and empty
    documents are rejected consistently before any modal operation starts.
    """
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as ex:
        return f"Invalid {operation} XML: {ex}"
    if root.tag != "mujoco":
        return f"Invalid {operation} XML: root element must be <mujoco>"
    supported_sections = set(load.section_order)
    if not any(child.tag in supported_sections for child in root):
        return f"Invalid {operation} XML: file must contain at least one supported MJCF section"
    return None


# ═══════════════════════════════════════════════════════════════════════
# Attach — link from external MJCF file
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_SelectTempLink(Operator):
    """Select an attach link from a temporary MJCF file."""

    bl_idname = "forge.temp_link"
    bl_label = "Select"
    bl_description = "Select attach link"
    bl_options = {"REGISTER", "UNDO"}

    def tmp_link_items(self, context: Context):
        """Generate enum items for temporary link selection from the configured file."""
        scene = context.scene
        temp_props: Temp_Props = bpy.data.scenes[scene.Main_Scene].Forge_Temp_Props
        if temp_props.tmp_file == "" or temp_props.tmp_file == "*.xml" or not os.path.exists(Path(temp_props.tmp_file)):
            return [("NONE", "None", "")]
        items = load.get_link_names(context, Path(temp_props.tmp_file))
        return [(k, v, "") for k, v in items.items()] or [("NONE", "None", "")]

    tmp_link: EnumProperty(
        name="Temp Link",
        items=tmp_link_items,
        default=0,
        description="Link from tmp file",
    )  # type: ignore

    def execute(self, context: Context):
        """Execute the operator, storing the selected temporary link name."""
        scene = context.scene
        temp_props: Temp_Props = bpy.data.scenes[scene.Main_Scene].Forge_Temp_Props
        temp_props.tmp_link = self.tmp_link
        return {"FINISHED"}

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the temporary link selection dialog."""
        return context.window_manager.invoke_props_dialog(self)


class Forge_OT_SelectTempFile(Operator):
    """Select an MJCF file path for import/attach."""

    bl_idname = "forge.temp_file"
    bl_label = "Select"
    bl_description = "Select mjcf file path"
    bl_options = {"REGISTER", "UNDO"}

    filepath: StringProperty(
        name="Path",
        subtype="FILE_PATH",
    )  # type: ignore

    filter_glob: StringProperty(default="*.xml", options={"HIDDEN"})  # type: ignore

    def execute(self, context: Context):
        """Execute the operator, storing the selected temporary file path."""
        scene = context.scene
        temp_props: Temp_Props = bpy.data.scenes[scene.Main_Scene].Forge_Temp_Props
        temp_props.tmp_file = self.filepath
        filepath, _ = os.path.splitext(self.filepath)
        model = basename(filepath)
        temp_props.tmp_model = model
        temp_props.tmp_link = "None"
        temp_props.tmp_prefix = model + "_"
        temp_props.tmp_links_class.clear()
        if context.area is not None:
            context.area.tag_redraw()
        return {"FINISHED"}

    def invoke(self, context: Context, event):
        """Invoke the operator, opening the file selection dialog."""
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


class Forge_OT_SelectTempInclude(Operator):
    """Select an MJCF file path for include reference."""

    bl_idname = "forge.temp_include"
    bl_label = "Select"
    bl_description = "Select mjcf file path"
    bl_options = {"REGISTER", "UNDO"}

    filepath: StringProperty(
        name="Path",
        subtype="FILE_PATH",
    )  # type: ignore

    filter_glob: StringProperty(default="*.xml", options={"HIDDEN"})  # type: ignore

    def execute(self, context: Context):
        """Execute the operator, storing the selected include file path."""
        scene = context.scene
        temp_props: Temp_Props = bpy.data.scenes[scene.Main_Scene].Forge_Temp_Props
        temp_props.tmp_include = self.filepath
        if context.area is not None:
            context.area.tag_redraw()
        return {"FINISHED"}

    def invoke(self, context: Context, event):
        """Invoke the operator, opening the file selection dialog."""
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


class Forge_OT_SelectImportPath(Operator):
    """Select an MJCF file path for import."""

    bl_idname = "forge.file_path"
    bl_label = "Select"
    bl_description = "Select mjcf file path"
    bl_options = {"REGISTER", "UNDO"}

    filepath: StringProperty(
        name="Export Path",
        subtype="FILE_PATH",
    )  # type: ignore

    filter_glob: StringProperty(default="*.xml", options={"HIDDEN"})  # type: ignore

    def execute(self, context: Context):
        """Execute the operator, storing the selected import file path."""
        scene = context.scene
        forge_props: Forge_Props = bpy.data.scenes[scene.Main_Scene].Forge_Props
        forge_props.import_file_path = self.filepath
        return {"FINISHED"}

    def invoke(self, context: Context, event):
        """Invoke the operator, opening the file selection dialog."""
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


class Forge_OT_SelectExportPath(Operator):
    """Select an MJCF export path."""

    bl_idname = "forge.export_path"
    bl_label = "Select"
    bl_description = "Select mjcf export path"
    bl_options = {"REGISTER", "UNDO"}

    filepath: StringProperty(
        name="Export Path",
        subtype="FILE_PATH",
    )  # type: ignore

    filter_glob: StringProperty(default="*.xml", options={"HIDDEN"})  # type: ignore

    def execute(self, context: Context):
        """Execute the operator, storing the selected export file path."""
        scene = context.scene
        forge_props: Forge_Props = bpy.data.scenes[scene.Main_Scene].Forge_Props
        path = self.filepath
        if not path.lower().endswith(".xml"):
            path += ".xml"
        blend_dir = os.path.dirname(bpy.data.filepath)
        if bpy.data.filepath and blend_dir in path:
            forge_props.export_path = bpy.path.relpath(path)
            forge_props.rel_path = True
        else:
            forge_props.export_path = path
            forge_props.rel_path = False
        return {"FINISHED"}

    def invoke(self, context: Context, event):
        """Invoke the operator, opening the file selection dialog."""
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


# ═══════════════════════════════════════════════════════════════════════
# Import
# ═══════════════════════════════════════════════════════════════════════


class BaseImportOperator(BaseProgressOperator):
    """Base class for progressive MJCF import with task-based progress tracking."""

    filepath: str
    filedir: str

    task_list: list[tuple[str, str, str, Sections]]
    assets_data: AssetsData
    file: str
    model: str
    model_prefix: str

    stage_names: list
    task_quene: list[list[str], list[str], list[tuple[Callable, tuple[Any, ...], dict[str, Any]]]] = []
    stage_quene: list[tuple[Callable, tuple[Any, ...], dict[str, Any]]] = []
    stage_infos: list = []
    forge_props: Forge_Props = None

    stage_name: str
    ref_type: str
    identifier: str
    task: Sections
    stage: Section | Scene_Data
    main_scene: Scene

    parent_coll: Collection | None

    def go_next_action(self):
        """Advance to the next action task, updating the sub-progress label."""
        if self.stage_name == "replicates":
            if self.stage.count > 0:
                element: Object = self.stage.data[self.action_task_index]
                remain = self.action_task_count - self.action_task_index
                self.forge_props.sub_progress_info = (
                    f"Add {self.stage_name.capitalize()} ({element.name}) Remain: {remain}"
                )
        else:
            element: ET.Element
            _pi, element = self.stage.elements[self.action_task_index]
            remain = self.action_task_count - self.action_task_index
            self.forge_props.sub_progress_info = f"Add {self.stage_name.capitalize()} ({element.tag}) Remain: {remain}"

        self.do_next_task = True

    def update_by_type(self, context: Context, init: bool = False):
        """Update the scene and parent collection based on the reference type.

        Args:
            context: The Blender context.
            init: Whether this is the initial setup call.
        """
        self.model_prefix = self.identifier.replace(".", "_") + "_" if self.model else ""
        if not init and self.ref_type in [cons.ReferenceType.ROOT, cons.ReferenceType.ATTACH]:
            self.assets_data = self.task.assets_data

        if self.ref_type == cons.ReferenceType.ROOT:
            context.window.scene = self.main_scene
            self.parent_coll = None
        else:
            if self.identifier not in bpy.data.collections:
                scene = load.get_attch_scene(self.identifier)
                # Progress state is stored on the main scene.  Keep the
                # generated attachment/include scene linked back to it so UI
                # panels can continue to resolve the active operation state
                # after this method switches the window scene below.
                scene.Main_Scene = self.main_scene.name
                scene["att_model"] = self.model
                context.window.scene = scene
                self.parent_coll = bpy.data.collections.new(self.identifier)
                context.scene.collection.children.link(self.parent_coll)
                assets_collection = funcs.get_collection(context, cons.CollectionNames.MESH_ASSETS)
                if assets_collection not in list(context.scene.collection.children):
                    context.scene.collection.children.link(assets_collection)
            else:
                self.parent_coll = bpy.data.collections[self.identifier]

    def update_task(self, context: Context, init: bool = False):
        """Reset stage task index and update current task from the task list.

        Args:
            context: The Blender context.
            init: Whether this is the initial setup call.
        """
        self.stage_task_index = 0
        self.ref_type, self.identifier, self.model, self.task = self.task_list[self.main_task_index]

        self.task.replicates.count = 0
        self.task.replicates.data = []

        self.update_by_type(context, init)

        if not init:
            self._add_include(context)

    def go_next_main_task(self, context: Context, init: bool = False):
        """Advance to the next main task, setting up stage queue and starting sub-tasks.

        Args:
            context: The Blender context.
            init: Whether this is the initial setup call.
        """
        if self.end_tasks:
            return

        self.stage_names, self.stage_infos, self.stage_quene = self.task_quene[self.main_task_index]
        self.stage_task_count = len(self.stage_names)
        self.update_task(context, init)

        self.go_next_stage_task()

    def go_next_stage_task(self):
        """Advance to the next stage within the current main task."""
        self.action_task_index = 0
        if self.stage_name == "worldbody":
            if self.task.replicates.data:
                self.task.replicates.data.reverse()

        self.stage_name = self.stage_names[self.stage_task_index]
        self.stage = getattr(self.task, self.stage_name)

        self.action_task_count = max(1, self.stage.count)
        self.do_next_task = True

    def progress_task(self, context: Context):
        """Execute the current progress task function.

        Args:
            context: The Blender context.

        Returns:
            True if the task completed, False otherwise.
        """
        fn, args, kwargs = self.stage_quene[self.stage_task_index]

        if fn(*args, **kwargs):
            return True
        else:
            return False

    def update_progress(self, context: Context):
        """Update the progress bar and info labels for the UI.

        Args:
            context: The Blender context.
        """
        # Keep progress rendering safe if an unexpected zero-stage queue gets
        # this far.  Import, Attach, and Include cancel empty queues during
        # initialization, but this guard protects the shared loop as well.
        total_stage_tasks = max(1, self.total_stage_task_count)
        self.forge_props.progress = (self.sum_stage_index + 1) / float(total_stage_tasks)
        self.forge_props.progress_info = self.stage_infos[self.stage_task_index]
        self.forge_props.sub_progress = (
            0.5 if self.action_task_count == 0 else (self.action_task_index + 1) / float(self.action_task_count)
        )
        if context.area is not None:
            context.area.tag_redraw()

    def _timed(self, label: str, fn, *args, **kwargs):
        """Decorator timing wrapper that measures and reports function execution time.

        Args:
            label: A descriptive label for the timed operation.
            fn: The function to execute.
            *args: Positional arguments passed to the function.
            **kwargs: Keyword arguments passed to the function.
        """
        start = time.time()
        fn(*args, **kwargs)
        self.report({"INFO"}, f"Parse {label} Time: {time.time() - start} seconds")

    def _add_include(self, context: Context):
        """Link include collections from referenced MJCF files.

        Args:
            context: The Blender context.
        """
        for inc, file, base_dir in self.task.includes:
            include_coll = bpy.data.collections[inc]

            collection = funcs.get_collection(
                context,
                load.set_coll_tag(cons.CollectionNames.INCLUDE, self.parent_coll),
                self.parent_coll,
            )
            funcs.add_include(
                context,
                self.report,
                file,
                base_dir,
                collection,
                include_coll,
                inc,
            )

    def _load_compiler(self, context: Context):
        """Load the compiler settings from the MJCF element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        _pi, element = self.stage.elements[self.action_task_index]
        load.get_compiler(context, element)
        self.go_next_action()
        return True

    def _load_option(self, context: Context):
        """Load the option settings from the MJCF element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        _pi, element = self.stage.elements[self.action_task_index]
        load.get_option(context, element)
        self.go_next_action()
        return True

    def _load_statistic(self, context: Context):
        """Load the statistic settings from the MJCF element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        _pi, element = self.stage.elements[self.action_task_index]
        load.get_statistic(context, element)
        self.go_next_action()
        return True

    def _load_visual(self, context: Context):
        """Load the visual settings from the MJCF element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        _pi, element = self.stage.elements[self.action_task_index]
        load.get_visual(context, element)
        self.go_next_action()
        return True

    def _load_asset(self, context: Context):
        """Load assets from the MJCF element in batches.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        end = False
        for _i in range(8):
            _pi, element = self.stage.elements[self.action_task_index]
            load.get_asset(
                context,
                self.report,
                self.forge_props,
                element,
                self.task.defaults,
                self.assets_data,
                self.task.base_dir,
                self.model_prefix,
            )
            self.action_task_index += 1
            if self.action_task_index == self.action_task_count:
                self.action_task_index -= 1
                end = True
                break

        if not end:
            self.action_task_index -= 1

        self.go_next_action()
        return True

    def _load_worldbody(self, context: Context):
        """Build the world body tree from MJCF elements in batches.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        end = False
        for _i in range(8):
            load.build_world_tree(
                context,
                self.report,
                self.task,
                self.assets_data,
                self.action_task_index,
                self.filedir,
                self.model_prefix,
                self.parent_coll,
            )
            self.action_task_index += 1
            if self.action_task_index == self.action_task_count:
                self.action_task_index -= 1
                end = True
                break

        if not end:
            self.action_task_index -= 1

        self.go_next_action()
        return True

    def _load_contact(self, context: Context):
        """Load contact pairs from MJCF elements in batches.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        end = False
        for _i in range(8):
            _pi, element = self.stage.elements[self.action_task_index]
            load.add_contact(
                context,
                self.report,
                element,
                self.parent_coll,
                self.model_prefix,
            )
            self.action_task_index += 1
            if self.action_task_index == self.action_task_count:
                self.action_task_index -= 1
                end = True
                break

        if not end:
            self.action_task_index -= 1
        self.go_next_action()
        return True

    def _load_equality(self, context: Context):
        """Load equality constraints from MJCF elements in batches.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        end = False
        for _i in range(8):
            _pi, element = self.stage.elements[self.action_task_index]
            load.add_equality(
                context,
                self.report,
                element,
                self.task.defaults,
                self.parent_coll,
                self.model_prefix,
            )
            self.action_task_index += 1
            if self.action_task_index == self.action_task_count:
                self.action_task_index -= 1
                end = True
                break

        if not end:
            self.action_task_index -= 1

        self.go_next_action()
        return True

    def _load_tendon(self, context: Context):
        """Load tendon definitions from MJCF elements in batches.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        end = False
        for _i in range(8):
            _pi, element = self.stage.elements[self.action_task_index]
            load.add_tendon(
                context,
                self.report,
                element,
                self.task.defaults,
                self.parent_coll,
                self.model_prefix,
            )
            self.action_task_index += 1
            if self.action_task_index == self.action_task_count:
                self.action_task_index -= 1
                end = True
                break

        if not end:
            self.action_task_index -= 1

        self.go_next_action()
        return True

    def _load_actuator(self, context: Context):
        """Load actuator definitions from MJCF elements in batches.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        end = False
        for _i in range(8):
            _pi, element = self.stage.elements[self.action_task_index]
            load.add_actuator(
                context,
                self.report,
                element,
                self.task.defaults,
                self.parent_coll,
                self.model_prefix,
            )
            self.action_task_index += 1
            if self.action_task_index == self.action_task_count:
                self.action_task_index -= 1
                end = True
                break

        if not end:
            self.action_task_index -= 1
        self.go_next_action()
        return True

    def _load_sensor(self, context: Context):
        """Load sensor definitions from MJCF elements in batches.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        end = False
        for _i in range(8):
            _pi, element = self.stage.elements[self.action_task_index]
            load.add_sensor(
                context,
                self.report,
                element,
                self.parent_coll,
                self.model_prefix,
            )
            self.action_task_index += 1
            if self.action_task_index == self.action_task_count:
                self.action_task_index -= 1
                end = True
                break

        if not end:
            self.action_task_index -= 1
        self.go_next_action()
        return True

    def _load_replicate(self, context: Context):
        """Create replicated objects from replicate task data.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        if self.task.replicates.count == 0:
            self.go_next_action()
            return True

        replicate: Object = self.task.replicates.data[self.action_task_index]
        data: ReplicateItem = replicate.Forge_Replicate
        source_objs = [obj for obj in replicate.children]
        funcs.set_replicate(
            context,
            self.report,
            data.count,
            data.sep,
            data.offset,
            data.euler,
            replicate,
            source_objs,
        )
        self.go_next_action()
        return True

    def const_stask_data(self, context: Context):
        """Build the static stage task lists (names, infos, and functions).

        Args:
            context: The Blender context.

        Returns:
            A tuple of (stage_task_names, stage_task_infos, stage_task_funcs).
        """
        stage_task_names = [
            "compiler",
            "option",
            "statistic",
            "visual",
            "asset",
            "worldbody",
            "contact",
            "equality",
            "tendon",
            "actuator",
            "sensor",
            "replicates",
        ]

        stage_task_infos = [
            "Parsing Compiler...",
            "Parsing Option...",
            "Parsing Statistic...",
            "Parsing Visual...",
            "Loading Assets...",
            "Creating World...",
            "Creating Contact...",
            "Creating Equality...",
            "Creating Tendon...",
            "Creating Actuator...",
            "Creating Sensor...",
            "Creating Replicates...",
        ]

        stage_task_funcs = [
            (self._load_compiler, (context,), {}),
            (self._load_option, (context,), {}),
            (self._load_statistic, (context,), {}),
            (self._load_visual, (context,), {}),
            (self._load_asset, (context,), {}),
            (self._load_worldbody, (context,), {}),
            (self._load_contact, (context,), {}),
            (self._load_equality, (context,), {}),
            (self._load_tendon, (context,), {}),
            (self._load_actuator, (context,), {}),
            (self._load_sensor, (context,), {}),
            (self._load_replicate, (context,), {}),
        ]

        return stage_task_names, stage_task_infos, stage_task_funcs

    def prepare_task(self, context: Context):
        """Build the task queue from parsed task data for progressive execution.

        Args:
            context: The Blender context.
        """
        stage_task_names, stage_task_infos, stage_task_funcs = self.const_stask_data(context)

        self.task_quene = []
        count = 0
        for i in range(len(self.task_list)):
            _ref_type, _identifier, _model, task = self.task_list[i]
            task_names = []
            task_infos = []
            task_funcs = []
            for j in range(len(stage_task_names)):
                stage_name = stage_task_names[j]
                stage: Section = getattr(task, stage_name)
                if stage.count > 0:
                    count += 1
                    task_names.append(stage_task_names[j])
                    task_infos.append(stage_task_infos[j])
                    task_funcs.append(stage_task_funcs[j])
            task_names.append(stage_task_names[-1])
            task_infos.append(stage_task_infos[-1])
            task_funcs.append(stage_task_funcs[-1])
            self.task_quene.append([task_names, task_infos, task_funcs])
        self.total_stage_task_count = count

    def cancel_if_no_tasks(self, context: Context, operation: str) -> bool:
        """Cancel an import-style operation when its queue has no work.

        Empty or otherwise unsupported MJCF documents must not enter the
        progressive loop.  Besides avoiding invalid progress arithmetic, this
        prevents Attach/Include from creating empty generated scenes and keeps
        Import from clearing the current scene for a no-op file.
        """
        if self.total_stage_task_count > 0:
            return False

        message = f"{operation} cancelled: no importable MJCF sections"
        self.abort_modal_operation(message)
        if self.forge_props is not None:
            self.reset_ui(context)
        self.report({"ERROR"}, message)
        return True

    def pre_task_init(self, context: Context):
        """Run the initial setup before the main task loop starts.

        Args:
            context: The Blender context.
        """
        self.go_next_main_task(context, True)
        self.go_next_action()

    def parse_xml(self):
        """Parse the MJCF XML file and populate the task list recursively."""
        defaults = {}
        load.get_task_recursive(
            Path(self.filepath),
            self.task_list,
            defaults,
            self.file,
            self.ref_type,
            model=self.model,
        )
        # Includes and attached models are already resolved. Check before any
        # import initialization or removal of the existing scene.
        for _, _, _, task in self.task_list:
            if task is None:
                continue
            for _, element in task.asset.elements:
                if element.tag != "mesh":
                    continue
                attrs = dict(element.attrib)
                load.parse_inherit_attrs(task.defaults, attrs, cons.MJCFTags.MESH, attrs.get("class", "root"))
                if Path(attrs.get("file", "")).suffix.lower() in {".gltf", ".glb"}:
                    require_gltf_addon("import")
                    return

    def reset_progress(self):
        """Reset all progress bar and info label values to zero/empty."""
        self.forge_props.progress = 0.0
        self.forge_props.progress_info = ""
        self.forge_props.sub_progress = 0.0
        self.forge_props.sub_progress_info = ""


# ═══════════════════════════════════════════════════════════════════════
# Import
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Import(BaseImportOperator):
    bl_idname = "forge.import_mjcf"
    bl_label = "Import"
    bl_description = "Import a mjcf file"
    bl_options = {"REGISTER", "UNDO"}

    clear_task_funcs: list[tuple[Callable, tuple[Any, ...], dict[str, Any]]] = []
    clear_tasks_info: list = []
    clear_stage_task_name: list = []

    init: Scene_Data
    objects: Scene_Data
    meshes: Scene_Data
    images: Scene_Data
    materials: Scene_Data
    collections: Scene_Data
    scenes: Scene_Data
    purge: Scene_Data

    clear_task_funcs_count: int

    @classmethod
    def poll(cls, context: Context):
        """Allow import only while no other Forge modal operation is active."""
        return cls.modal_operation_available(context)

    def go_next_action(self):
        """Advance to the next action task, updating sub-progress for import or clear phase."""
        if self.main_task_index != 0:
            if self.stage_name == "replicates":
                if self.stage.count > 0:
                    element: Object = self.stage.data[self.action_task_index]
                    remain = self.action_task_count - self.action_task_index
                    self.forge_props.sub_progress_info = (
                        f"Add {self.stage_name.capitalize()} ({element.name}) Remain: {remain}"
                    )
            else:
                element: ET.Element
                _pi, element = self.stage.elements[self.action_task_index]
                remain = self.action_task_count - self.action_task_index
                self.forge_props.sub_progress_info = (
                    f"Add {self.stage_name.capitalize()} ({element.tag}) Remain: {remain}"
                )
        else:
            self.forge_props.sub_progress_info = (
                f"Remain {self.stage_name.capitalize()}: {self.action_task_index}/{self.action_task_count}"
            )
        self.do_next_task = True

    def update_task(self, context: Context, init: bool = False):
        """Reset stage task index and update current import task (skipping index 0, the clear phase).

        Args:
            context: The Blender context.
            init: Whether this is the initial setup call.
        """
        self.stage_task_index = 0
        self.ref_type, self.identifier, self.model, self.task = self.task_list[max(1, self.main_task_index)]
        self.task.replicates.count = 0
        self.task.replicates.data = []

        self.update_by_type(context, init)

        self._add_include(context)

    def go_next_main_task(self, context: Context, init: bool = False):
        """Advance to the next main task, handling both clear (index 0) and import phases.

        Args:
            context: The Blender context.
            init: Whether this is the initial setup call.
        """
        if self.end_tasks:
            return

        if self.main_task_index != 0:
            self.main_task_index %= self.main_task_count
            self.stage_names, self.stage_infos, self.stage_quene = self.task_quene[self.main_task_index - 1]
            self.stage_task_count = len(self.stage_names)
            self.update_task(context, init)
        else:
            self.stage_task_count = self.clear_task_funcs_count

        self.go_next_stage_task()

    def go_next_stage_task(self):
        """Advance to the next stage, selecting the task or clear stage based on phase."""
        self.action_task_index = 0
        if self.main_task_index != 0:
            if self.stage_name == "worldbody":
                self.task.replicates.data.reverse()

            self.stage_name = self.stage_names[self.stage_task_index]
            self.stage = getattr(self.task, self.stage_name)
        else:
            self.stage_name = self.clear_stage_task_name[self.stage_task_index]
            self.stage = getattr(self, self.stage_name)

        self.action_task_count = max(1, self.stage.count)
        self.do_next_task = True

    def progress_task(self, context: Context):
        """Execute the current progress task, routing to clear or import functions.

        Args:
            context: The Blender context.

        Returns:
            True if the task completed, False otherwise.
        """
        if self.main_task_index == 0:
            fn, args, kwargs = self.clear_task_funcs[self.stage_task_index]
        else:
            fn, args, kwargs = self.stage_quene[self.stage_task_index]

        if fn(*args, **kwargs):
            return True
        else:
            return False

    def update_progress(self, context: Context):
        """Update the progress bar and info labels for import or clear phase.

        Args:
            context: The Blender context.
        """
        total_stage_tasks = max(1, self.total_stage_task_count)
        if self.main_task_index == 0:
            self.forge_props.progress = (self.stage_task_index + 1) / float(total_stage_tasks)
            self.forge_props.progress_info = self.clear_tasks_info[self.stage_task_index]
        else:
            self.forge_props.progress = (self.clear_task_funcs_count + self.sum_stage_index + 1) / float(
                total_stage_tasks
            )
            self.forge_props.progress_info = self.stage_infos[self.stage_task_index]
        self.forge_props.sub_progress = (
            1.0 if self.action_task_count == 0 else (self.action_task_index + 1) / float(self.action_task_count)
        )
        if context.area is not None:
            context.area.tag_redraw()

    def _import_init(self, context: Context):
        """Run import initialization to prepare the scene.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        load.import_init(context, self.report)
        self.go_next_action()
        return True

    def _clear_objects(self):
        """Delete all objects in the current scene and purge orphans.

        Returns:
            True when complete.
        """
        if self.scenes.count == 0:
            self.go_next_action()
            return True

        scene = self.scenes.data[self.action_task_index]
        bpy.context.window.scene = scene
        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete(use_global=True, confirm=False)

        bpy.ops.outliner.orphans_purge()

        self.go_next_action()
        return True

    def _clear_meshes(self):
        """Remove the current mesh data block.

        Returns:
            True when complete.
        """
        if self.meshes.count == 0:
            self.go_next_action()
            return True

        bpy.data.meshes.remove(self.meshes.data[self.action_task_index])
        self.go_next_action()
        return True

    def _clear_images(self):
        """Remove the current image data block, skipping Render Result.

        Returns:
            True when complete.
        """
        if self.images.count == 0:
            self.go_next_action()
            return True

        image = self.images.data[self.action_task_index]
        if image.name == "Render Result":
            self.go_next_action()
            return True

        bpy.data.images.remove(image)
        self.go_next_action()
        return True

    def _clear_materials(self):
        """Remove the current material data block.

        Returns:
            True when complete.
        """
        if self.materials.count == 0:
            self.go_next_action()
            return True

        bpy.data.materials.remove(self.materials.data[self.action_task_index])
        self.go_next_action()
        return True

    def _clear_collections(self):
        """Remove all collections from Blender data.

        Returns:
            True when complete.
        """
        if self.collections.count == 0:
            self.go_next_action()
            return True

        for collection in list(bpy.data.collections):
            bpy.data.collections.remove(collection)
        self.go_next_action()
        return True

    def _clear_scenes(self):
        """Remove the current scene, keeping the default "Scene".

        Returns:
            True when complete.
        """
        if self.scenes.count == 0:
            self.go_next_action()
            return True

        scene = self.scenes.data[self.action_task_index]
        if scene.name == "Scene":
            self.go_next_action()
            return True
        bpy.data.scenes.remove(scene)
        self.go_next_action()
        return True

    def _orphans_purge(self):
        """Purge orphaned data blocks from Blender.

        Returns:
            True when complete.
        """
        bpy.ops.outliner.orphans_purge()
        self.go_next_action()
        return True

    def _prepare_clear_task(self, context: Context):
        """Build the clear-phase task list (import init, then delete scene data).

        Args:
            context: The Blender context.
        """
        self.clear_task_funcs = [
            (self._import_init, (context,), {}),
            (self._clear_objects, (), {}),
            # (self._clear_meshes, (), {}),
            # (self._clear_images, (), {}),
            # (self._clear_materials, (), {}),
            (self._clear_collections, (), {}),
            (self._clear_scenes, (), {}),
            (self._orphans_purge, (), {}),
        ]

        self.clear_stage_task_name = [
            "init",
            "scenes",
            # "objects",
            # "meshes",
            # "images",
            # "materials",
            "collections",
            "scenes",
            "purge",
        ]

        self.clear_tasks_info = [
            "Import Init...",
            "Clear Data...",
            # "Clear Meshes...",
            # "Clear Images...",
            # "Clear Materials...",
            "Clear Collections...",
            "Clear Scenes...",
            "Orphans Purge...",
        ]

    def prepare_task(self, context: Context):
        """Build the task queue from parsed data, skipping the clear-phase placeholder entry.

        Args:
            context: The Blender context.
        """
        stage_task_names, stage_task_infos, stage_task_funcs = self.const_stask_data(context)

        self.task_quene = []
        count = 0
        for i in range(1, len(self.task_list)):
            _ref_type, _identifier, _model, task = self.task_list[i]
            task_names = []
            task_infos = []
            task_funcs = []
            for j in range(len(stage_task_names)):
                stage_name = stage_task_names[j]
                stage: Section = getattr(task, stage_name)
                if stage.count > 0:
                    count += 1
                    task_names.append(stage_task_names[j])
                    task_infos.append(stage_task_infos[j])
                    task_funcs.append(stage_task_funcs[j])
            task_names.append(stage_task_names[-1])
            task_infos.append(stage_task_infos[-1])
            task_funcs.append(stage_task_funcs[-1])
            self.task_quene.append([task_names, task_infos, task_funcs])
        self.total_stage_task_count = count

    def execute(self, context):
        """Execute the import operator, parsing XML and running the progressive task loop.

        Args:
            context: The Blender context.

        Returns:
            A Blender operator result set.
        """
        try:
            self.main_scene = bpy.data.scenes[context.scene.Main_Scene]
            if self.forge_props is None:
                self.forge_props = self.main_scene.Forge_Props
            library_error = _check_asset_library()
            if library_error is not None:
                # invoke() sets the progress state before delegating here, so it
                # has to be cleared or the panel stays on "importing".
                self.reset_ui(context)
                self.report(
                    {"ERROR"},
                    f"'Forge Library' asset library reload failed ({library_error}),"
                    " check Preferences -> File Paths -> Asset Libraries",
                )
                return {"CANCELLED"}
            if not getattr(self, "filepath", ""):
                self.filepath = self.forge_props.import_file_path
            if not getattr(self, "file", ""):
                self.file = ""
            if not getattr(self, "model", ""):
                self.model = ""
            if not getattr(self, "ref_type", ""):
                self.ref_type = cons.ReferenceType.ROOT
            if not os.path.exists(self.filepath):
                self.report({"ERROR"}, f"Import path incorrect, not find: {self.filepath}")
                return {"CANCELLED"}
            validation_error = _validate_mjcf_file(Path(self.filepath).resolve(), "import")
            if validation_error:
                if self.forge_props is not None:
                    self.reset_ui(context)
                self.report({"ERROR"}, validation_error)
                return {"CANCELLED"}
            if not self.begin_modal_operation():
                return {"CANCELLED"}
            self.stage_name = ""
            funcs.get_collection(context, cons.CollectionNames.MESH_ASSETS).hide_viewport = True

            self.task_list = []
            self.task_list.append(("", "", "", None))

            self.init = Scene_Data()
            self.objects = Scene_Data(list(bpy.data.objects))
            self.meshes = Scene_Data(list(bpy.data.meshes))
            self.images = Scene_Data(list(bpy.data.images))
            self.materials = Scene_Data(list(bpy.data.materials))
            self.collections = Scene_Data()
            self.scenes = Scene_Data(list(bpy.data.scenes))
            self.purge = Scene_Data()
            self.parse_xml()

            _ref_type, _identifier, _model, task = self.task_list[-1]
            self.assets_data = task.assets_data
            if context.area is not None:
                context.area.tag_redraw()

            self.prepare_task(context)
            if self.cancel_if_no_tasks(context, "Import"):
                return {"CANCELLED"}
            self._prepare_clear_task(context)

            self.main_task_count = len(self.task_list)
            self.clear_task_funcs_count = len(self.clear_task_funcs)
            self.total_stage_task_count += self.clear_task_funcs_count

            self.main_task_index = 0
            self.stage_task_index = 0
            self.action_task_index = 0

            self.filedir = Path(self.filepath).parent
            self.pre_task_init(context)

            return super().execute(context)
        except Exception as ex:  # pylint: disable=broad-exception-caught
            message = f"Import fail: {str(ex):s}"
            self.abort_modal_operation(message)
            self.report({"ERROR"}, message)
            if self.forge_props is not None:
                self.reset_ui(context)
            return {"CANCELLED"}

    def invoke(self, context, event):
        """Invoke the import operator, validating the file path and starting execution.

        The asset library is checked in :meth:`execute` only.  This invoke always
        ends with ``return self.execute(context)`` on the paths that get that far,
        so checking here too would only run the same check twice.

        Args:
            context: The Blender context.
            event: The triggering event.

        Returns:
            A Blender operator result set.
        """
        scene = context.scene
        self.forge_props = bpy.data.scenes[scene.Main_Scene].Forge_Props

        self.forge_props.is_importing = True
        self.forge_props.progress = 0.02
        self.forge_props.progress_info = "Initialling..."
        if context.area is not None:
            context.area.tag_redraw()

        self.main_scene = bpy.data.scenes[scene.Main_Scene]
        self.filepath = self.forge_props.import_file_path
        self.file = ""
        self.model = ""
        self.ref_type = cons.ReferenceType.ROOT

        if not os.path.exists(self.filepath):
            self.report({"ERROR"}, f"Import path incorrect, not find: {self.filepath}")
            self.reset_ui(context)
            return {"CANCELLED"}

        self.report({"INFO"}, f"Import: {self.filepath}")

        return self.execute(context)

    def reset_ui(self, context: Context):
        """Reset UI after import completes, hiding the assets collection and clearing progress.

        Args:
            context: The Blender context.
        """
        assets_collection = funcs.get_collection(context, cons.CollectionNames.MESH_ASSETS)
        assets_collection.hide_viewport = True

        if self.end_tasks:
            # Only on full success — a cancelled import keeps its loaders for retry.
            load.cleanup_mesh_asset_loaders()

        self.forge_props.is_importing = False
        self.reset_progress()


# ═══════════════════════════════════════════════════════════════════════
# Attach
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Attach(BaseImportOperator, ImportHelper):
    """Attach link from other file, optionally based on selected existing frame(s) | link(s) | replicate(s)"""

    bl_idname = "forge.create_attach"
    bl_label = "Attach link(s)"
    bl_options = {"REGISTER", "UNDO"}

    link: str
    prefix: str
    attach_model: str
    parent_obj: Object

    def draw(self, context: Context):
        """Draw operator UI elements for attach file, model, prefix, and link selection."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        scene = context.scene
        temp_props: Temp_Props = bpy.data.scenes[scene.Main_Scene].Forge_Temp_Props

        col = layout.column(align=True)
        row = col.row(align=True)
        row.prop(temp_props, "tmp_file", text="File")
        row.operator(
            Forge_OT_SelectTempFile.bl_idname,
            text="",
            icon="FILE_FOLDER",
        )
        col.prop(temp_props, "tmp_model", text="Model")
        col.prop(temp_props, "tmp_prefix", text="Prefix")
        name = temp_props.tmp_link
        row = col.row(align=True).split(factor=0.4)
        row.alignment = "RIGHT"
        row.label(text="Link")
        row.operator(
            Forge_OT_SelectTempLink.bl_idname,
            text=name,
        )

    def go_next_main_task(self, context: Context, init: bool = False):
        """Advance to the next main task, adding attach references when all tasks complete.

        Args:
            context: The Blender context.
            init: Whether this is the initial setup call.
        """
        if self.end_tasks:
            self._add_attach(context)
            return

        super().go_next_main_task(context, init)

    def _add_attach(self, context: Context):
        """Create the attach reference in the scene after importing the external model.

        Args:
            context: The Blender context.
        """
        context.window.scene = self.main_scene
        collection = funcs.get_collection(
            context,
            cons.CollectionNames.ATTACH,
        )
        _ref_type, _identifier, _model, task = self.task_list[-1]
        tag_attrs = {"model": self.attach_model, "file": self.file, "body": self.link, "prefix": self.prefix}
        load.add_attach(
            context,
            self.report,
            collection,
            task.attachs,
            tag_attrs,
            self.filepath,
            parent_obj=self.parent_obj,
        )

    def execute(self, context: Context):
        """Execute the operator, attaching links from an external mjcf file."""
        try:
            self.stage_name = ""
            funcs.get_collection(context, cons.CollectionNames.MESH_ASSETS).hide_viewport = True

            scene = context.scene
            self.forge_props = bpy.data.scenes[scene.Main_Scene].Forge_Props

            library_error = _check_asset_library()
            if library_error is not None:
                self.report(
                    {"ERROR"},
                    f"'Forge Library' asset library reload failed ({library_error}),"
                    " check Preferences -> File Paths -> Asset Libraries",
                )
                return {"CANCELLED"}

            temp_props: Temp_Props = bpy.data.scenes[scene.Main_Scene].Forge_Temp_Props
            self.file = temp_props.tmp_file
            self.attach_model = self.model = temp_props.tmp_model
            self.prefix = temp_props.tmp_prefix
            self.link = temp_props.tmp_link if temp_props.tmp_link != "None" else ""

            if self.model == "":
                self.report({"ERROR"}, "Model is empty\nAttach cancelled")
                return {"CANCELLED"}
            if self.file == "":
                self.report({"ERROR"}, "File is empty\nAttach cancelled")
                return {"CANCELLED"}
            if not os.path.exists(Path(self.file)):
                self.report({"ERROR"}, "File not exist\nAttach cancelled")
                return {"CANCELLED"}
            if self.prefix == "":
                self.report({"ERROR"}, "Prefix is empty\nAttach cancelled")
                return {"CANCELLED"}
            self.parent_obj = context.selected_objects[0] if len(context.selected_objects) == 1 else None
            self.filepath = self.file
            self.main_scene = bpy.data.scenes[scene.Main_Scene]

            path = Path(self.filepath).resolve()

            self.task_list = []

            validation_error = _validate_mjcf_file(path, "attach")
            if validation_error:
                self.report({"ERROR"}, validation_error)
                return {"CANCELLED"}

            if path.name in bpy.data.collections:
                self._add_attach(context)
                self.reset_ui(context)
                return {"FINISHED"}

            if not self.begin_modal_operation():
                return {"CANCELLED"}

            self.forge_props.is_attaching = True
            self.forge_props.progress = 0.02
            self.forge_props.progress_info = "Initialling..."
            if context.area is not None:
                context.area.tag_redraw()

            defaults = {}
            load.get_task_recursive(
                path,
                self.task_list,
                defaults,
                self.file,
                cons.ReferenceType.ATTACH,
                path.name,
                self.model,
            )

            sections = Sections()
            sections.attachs[self.model] = [path.name, self.file]

            self.task_list.append((cons.ReferenceType.ROOT, "", "", sections))
            _ref_type, _identifier, _model, task = self.task_list[-2]
            self.assets_data = task.assets_data
            if context.area is not None:
                context.area.tag_redraw()

            self.prepare_task(context)
            if self.cancel_if_no_tasks(context, "Attach"):
                return {"CANCELLED"}

            self.main_task_count = len(self.task_list)

            self.main_task_index = 0
            self.stage_task_index = 0
            self.action_task_index = 0

            self.filedir = Path(self.filepath).parent
            self.pre_task_init(context)

            return super().execute(context)
        except Exception as ex:  # pylint: disable=broad-exception-caught
            message = f"Attach fail: {str(ex):s}"
            self.abort_modal_operation(message)
            self.report({"ERROR"}, message)
            if self.forge_props is not None:
                self.reset_ui(context)
            return {"CANCELLED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run based on selected link, replicate, frame, or no selection."""
        valid_selection = (
            len(context.selected_objects) == 1
            and sel.check_selected_model_types(
                context,
                [cons.ModelTypes.LINK, cons.ModelTypes.REPLICATE, cons.ModelTypes.FRAME],
            )
        ) or not context.selected_objects
        return valid_selection and cls.modal_operation_available(context)

    def invoke(self, context, event):
        """Invoke the operator, showing the attach dialog."""
        return context.window_manager.invoke_props_dialog(self)

    def reset_ui(self, context: Context):
        """Reset UI after attach completes, hiding assets collection and clearing progress.

        Args:
            context: The Blender context.
        """
        assets_collection = funcs.get_collection(context, cons.CollectionNames.MESH_ASSETS)
        assets_collection.hide_viewport = True

        if self.end_tasks:
            # Only on full success — a cancelled attach keeps its loaders for retry.
            load.cleanup_mesh_asset_loaders()

        self.forge_props.is_attaching = False
        self.reset_progress()


# ═══════════════════════════════════════════════════════════════════════
# Include
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Include(BaseImportOperator, ImportHelper):
    """Add include from mjcf file, only add include tags when export"""

    bl_idname = "forge.create_include"
    bl_label = "Add include"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context: Context):
        """Draw operator UI elements for include file selection."""
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        scene = context.scene
        temp_props: Temp_Props = bpy.data.scenes[scene.Main_Scene].Forge_Temp_Props

        col = layout.column(align=True)
        row = col.row(align=True)
        row.prop(temp_props, "tmp_include", text="File")
        row.operator(
            Forge_OT_SelectTempInclude.bl_idname,
            text="",
            icon="FILE_FOLDER",
        )

    def update_task(self, context: Context, init: bool = False):
        """Reset stage task index and update current include task, adding includes for non-final tasks.

        Args:
            context: The Blender context.
            init: Whether this is the initial setup call.
        """
        self.stage_task_index = 0
        self.ref_type, self.identifier, self.model, self.task = self.task_list[
            self.main_task_index % self.main_task_count
        ]

        self.task.replicates.count = 0
        self.task.replicates.data = []

        self.update_by_type(context, init)

        if self.main_task_index < self.main_task_count - 1:
            self._add_include(context)

    def go_next_main_task(self, context: Context, init: bool = False):
        """Advance to the next main task, adding the include reference when all tasks complete.

        Args:
            context: The Blender context.
            init: Whether this is the initial setup call.
        """
        if self.end_tasks:
            context.window.scene = self.main_scene
            self._add_include_ref(context)
            return

        self.stage_names, self.stage_infos, self.stage_quene = self.task_quene[self.main_task_index]
        self.stage_task_count = len(self.stage_names)

        self.update_task(context, init)

        self.go_next_stage_task()

    def _add_include_ref(self, context: Context):
        """Add the final include reference to the scene collection.

        Args:
            context: The Blender context.
        """
        context.window.scene = self.main_scene
        collection = funcs.get_collection(context, cons.CollectionNames.INCLUDE)
        _ref_type, _identifier, _model, self.task = self.task_list[-1]

        for inc, file, base_dir in self.task.includes:
            include_coll = bpy.data.collections[inc]

            funcs.add_include(
                context,
                self.report,
                file,
                base_dir,
                collection,
                include_coll,
                inc,
            )

    def execute(self, context: Context):
        """Execute the operator, adding an include reference from an MJCF file."""
        try:
            self.stage_name = ""
            funcs.get_collection(context, cons.CollectionNames.MESH_ASSETS).hide_viewport = True

            scene = context.scene
            self.forge_props = bpy.data.scenes[scene.Main_Scene].Forge_Props
            temp_props: Temp_Props = bpy.data.scenes[scene.Main_Scene].Forge_Temp_Props

            library_error = _check_asset_library()
            if library_error is not None:
                self.report(
                    {"ERROR"},
                    f"'Forge Library' asset library reload failed ({library_error}),"
                    " check Preferences -> File Paths -> Asset Libraries",
                )
                return {"CANCELLED"}

            self.file = temp_props.tmp_include

            self.filepath = self.file

            if not os.path.exists(self.filepath):
                self.report({"ERROR"}, f"Include path incorrect, not find: {self.filepath}")
                return {"CANCELLED"}

            self.parent_obj = None
            self.main_scene = bpy.data.scenes[scene.Main_Scene]

            path = Path(self.filepath).resolve()

            validation_error = _validate_mjcf_file(path, "include")
            if validation_error:
                self.report({"ERROR"}, validation_error)
                return {"CANCELLED"}

            if path.name in bpy.data.collections:
                self.report({"WARNING"}, f"Include {path.name} is in Scene")
                self.reset_ui(context)
                return {"FINISHED"}

            if not self.begin_modal_operation():
                return {"CANCELLED"}

            self.forge_props.is_including = True
            self.forge_props.progress = 0.02
            self.forge_props.progress_info = "Initialling..."
            if context.area is not None:
                context.area.tag_redraw()

            self.task_list = []
            self.task = None

            defaults = {}
            load.get_task_recursive(
                path,
                self.task_list,
                defaults,
                self.file,
                cons.ReferenceType.INCLUDE,
                path.name,
            )

            sections = Sections()
            sections.includes.append((path.name, self.file, path.parent))

            self.task_list.append((cons.ReferenceType.ROOT, path.name, "", sections))

            _ref_type, _identifier, _model, task = self.task_list[-2]
            self.assets_data = task.assets_data
            if context.area is not None:
                context.area.tag_redraw()

            self.prepare_task(context)
            if self.cancel_if_no_tasks(context, "Include"):
                return {"CANCELLED"}

            self.main_task_count = len(self.task_list)

            self.main_task_index = 0
            self.stage_task_index = 0
            self.action_task_index = 0

            self.filedir = Path(self.filepath).parent
            self.pre_task_init(context)

            return super().execute(context)
        except Exception as ex:  # pylint: disable=broad-exception-caught
            message = f"Include fail: {str(ex):s}"
            self.abort_modal_operation(message)
            self.report({"ERROR"}, message)
            if self.forge_props is not None:
                self.reset_ui(context)
            return {"CANCELLED"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run (no objects selected).

        Args:
            context: The Blender context.

        Returns:
            True if no objects are selected.
        """
        return not context.selected_objects and cls.modal_operation_available(context)

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the include file dialog.

        Args:
            context: The Blender context.
            event: The triggering event.

        Returns:
            A Blender operator result set.
        """
        return context.window_manager.invoke_props_dialog(self)

    def reset_ui(self, context: Context):
        """Reset UI after include completes, hiding assets collection and clearing progress.

        Args:
            context: The Blender context.
        """
        assets_collection = funcs.get_collection(context, cons.CollectionNames.MESH_ASSETS)
        assets_collection.hide_viewport = True

        if self.end_tasks:
            # Only on full success — a cancelled include keeps its loaders for retry.
            # Include builds its assets through the same BaseImportOperator pipeline
            # as Import/Attach, so it leaves the same placeholder objects behind.
            load.cleanup_mesh_asset_loaders()

        self.forge_props.is_including = False
        self.reset_progress()


# ═══════════════════════════════════════════════════════════════════════
# Export
# ═══════════════════════════════════════════════════════════════════════


class Forge_OT_Export(BaseProgressOperator):
    """Exports a complete MuJoCo MJCF model XML from the Blender scene.
    This is the main entry function that coordinates asset collection, scene tree
    construction, and file writing.
    """

    bl_idname = "forge.export_mjcf"
    bl_label = "Export"

    forge_props: Forge_Props = None

    task_quene: list[tuple[Callable, tuple[Any, ...], dict[str, Any]]] = []
    stage_infos: list

    stage_action_task_count: list
    geometry_map: dict
    attach_model_map: dict
    instance_templates: dict
    hfield_map: dict
    collider_map: dict
    geo_materials_map: dict
    materials_map: dict
    materials_props_map: dict
    filepath: str
    root_element: ET.Element

    export_images_tasks: list
    export_hfield_tasks: list
    export_v_meshes_tasks: list
    export_c_meshes_tasks: list

    @classmethod
    def poll(cls, context: Context):
        """Allow export only while no other Forge modal operation is active."""
        return cls.modal_operation_available(context)

    def go_next_action(self):
        """Advance to the next export action task, updating the sub-progress info."""
        remain = self.action_task_count - self.action_task_index
        self.forge_props.sub_progress_info = f"Remain: {remain}"

        self.do_next_task = True

    def go_next_main_task(self, context: Context, init: bool = False):
        """Advance to the next main export task.

        Args:
            context: The Blender context.
            init: Whether this is the initial setup call.
        """
        if self.end_tasks:
            return

        self.stage_task_index = 0
        self.go_next_stage_task()

    def go_next_stage_task(self):
        """Advance to the next export stage, skipping stages with zero action count."""
        self.action_task_index = 0
        if self.stage_action_task_count[self.stage_task_index] == 0:
            find_next = False
            while not find_next:
                self.stage_task_index += 1
                if self.stage_task_index == self.stage_task_count:
                    self.stage_task_index -= 1
                    break
                if self.stage_action_task_count[self.stage_task_index] > 0:
                    find_next = True

        self.action_task_count = self.stage_action_task_count[self.stage_task_index]
        self.do_next_task = True

    def progress_task(self, context: Context):
        """Execute the current export progress task function.

        Args:
            context: The Blender context.

        Returns:
            True if the task completed, False otherwise.
        """
        fn, args, kwargs = self.task_quene[self.stage_task_index]

        if fn(*args, **kwargs):
            return True
        else:
            return False

    def update_progress(self, context: Context):
        """Update the export progress bar and info labels.

        Args:
            context: The Blender context.
        """
        self.forge_props.progress = (self.sum_stage_index + 1) / float(self.total_stage_task_count)
        self.forge_props.progress_info = self.stage_infos[self.stage_task_index]
        self.forge_props.sub_progress = (self.action_task_index + 1) / float(self.action_task_count)
        if context.area is not None:
            context.area.tag_redraw()

    def _gather_assets(self, context: Context):
        """Scan the scene for all assets and populate the export maps.

        Args:
            context: The Blender context.

        Returns:
            False on error, True after processing.
        """
        if not os.path.exists(os.path.dirname(self.filepath)):
            self.report({"ERROR"}, "Export path incorrect")
            return False
        if os.path.basename(self.filepath) == "*.xml":
            self.report({"ERROR"}, "Export path incorrect")
            return False

        self.instance_templates = funcs.collect_instance_templates(self.report)

        if not funcs.find_assets(
            context,
            self.geometry_map,
            self.attach_model_map,
            self.hfield_map,
            self.collider_map,
            self.geo_materials_map,
            self.materials_map,
            self.materials_props_map,
            self.report,
            self.instance_templates,
        ):
            self.report({"WARNING"}, "Export empty assets see previous info")

        self.export_images_tasks = list(self.materials_props_map.values())
        self.export_hfield_tasks = list(self.hfield_map.values())
        self.export_v_meshes_tasks = list(self.geometry_map.values())
        self.export_c_meshes_tasks = list(self.collider_map.values())
        self.stage_action_task_count[1:5] = [
            len(self.export_images_tasks),
            len(self.export_hfield_tasks),
            len(self.export_v_meshes_tasks),
            len(self.export_c_meshes_tasks),
        ]

        self.go_next_action()
        return True

    def _export_images(self):
        """Export the current image asset to disk.

        Returns:
            True when complete.
        """
        if self.action_task_index > 0:
            out.export_images(
                self.export_images_tasks[self.action_task_index],
                self.forge_props.update_forge_only,
            )
        else:
            if not self.forge_props.update_forge_only:
                _textureFile, img, path = self.export_images_tasks[0][cons.ShaderPropName.BACKGROUND]
                if img:
                    img: Image
                    img.save(filepath=path, save_copy=True)

        self.go_next_action()
        return True

    def _export_hfields(self):
        """Export the current height field asset to disk.

        Returns:
            True when complete.
        """
        out.export_hfields(
            self.export_hfield_tasks[self.action_task_index],
            self.forge_props.update_forge_only,
        )
        self.go_next_action()
        return True

    def _export_visuals(self):
        """Export the current visual mesh asset to disk.

        Returns:
            True when complete.
        """
        out.export_meshs(
            self.export_v_meshes_tasks[self.action_task_index],
            self.forge_props.update_forge_only,
            self.forge_props.use_glb,
        )
        self.go_next_action()
        return True

    def _export_colliders(self):
        """Export the current collider mesh asset to disk.

        Returns:
            True when complete.
        """
        out.export_collider(
            self.export_c_meshes_tasks[self.action_task_index],
            self.forge_props.update_forge_only,
        )
        self.go_next_action()
        return True

    def _set_includes(self, context: Context):
        """Write include tags into the root XML element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        out.add_include(context, self.root_element, os.path.dirname(self.filepath))
        self.go_next_action()
        return True

    def _set_compiler(self, context: Context):
        """Write the compiler section into the root XML element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        out.add_compiler(context, self.root_element)
        self.go_next_action()
        return True

    def _set_option(self, context: Context):
        """Write the option section into the root XML element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        out.add_option(context, self.root_element)
        self.go_next_action()
        return True

    def _set_statistic(self, context: Context):
        """Write the statistic section into the root XML element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        out.add_statistic(context, self.root_element)
        self.go_next_action()
        return True

    def _set_visual(self, context: Context):
        """Write the visual section into the root XML element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        out.add_visual(context, self.root_element)
        self.go_next_action()
        return True

    def _set_assets(self, context: Context):
        """Write the asset section (meshes, materials, textures) into the root XML element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        out.add_asset(
            self.root_element,
            self.geometry_map,
            self.attach_model_map,
            self.hfield_map,
            self.collider_map,
            self.materials_props_map,
            self.report,
        )
        self.go_next_action()
        return True

    def _set_world(self, context: Context):
        """Write the world body section into the root XML element.

        Args:
            context: The Blender context.

        Returns:
            False on error, True after processing.
        """
        if not out.set_world(
            context,
            self.root_element,
            self.geometry_map,
            self.hfield_map,
            self.collider_map,
            self.geo_materials_map,
            self.report,
            self.instance_templates,
        ):
            self.report({"WARNING"}, "Export empty multibody see previous info")
        self.go_next_action()
        return True

    def _set_contact(self, context: Context):
        """Write the contact section into the root XML element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        out.add_contact(context, self.root_element, self.report)
        self.go_next_action()
        return True

    def _set_equality(self, context: Context):
        """Write the equality constraint section into the root XML element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        out.add_equality(context, self.root_element, self.report)
        self.go_next_action()
        return True

    def _set_tendon(self, context: Context):
        """Write the tendon section into the root XML element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        out.add_tendon(context, self.root_element, self.report)
        self.go_next_action()
        return True

    def _set_actuator(self, context: Context):
        """Write the actuator section into the root XML element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        out.add_actuator(context, self.root_element, self.report)
        self.go_next_action()
        return True

    def _set_sensor(self, context: Context):
        """Write the sensor section into the root XML element.

        Args:
            context: The Blender context.

        Returns:
            True when complete.
        """
        out.add_sensor(context, self.root_element, self.report)
        self.go_next_action()
        return True

    def _write_to_file(self, context: Context):
        """Write the final XML tree to the export file on disk.

        Args:
            context: The Blender context.

        Returns:
            False on error, True after successful write.
        """
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                f.write(out.prettify(self.root_element))

            self.report({"INFO"}, f"Export {self.filepath} Done")
        except Exception as ex:  # pylint: disable=broad-exception-caught
            self.report({"ERROR"}, f"Export fail: {str(ex):s}")
            return False
        self.go_next_action()
        return True

    def execute(self, context: Context):
        """Execute the export operator, gathering assets and writing the MJCF XML file.

        Args:
            context: The Blender context.

        Returns:
            A Blender operator result set.
        """
        try:
            if self.forge_props is None:
                self.forge_props = bpy.data.scenes[context.scene.Main_Scene].Forge_Props
            if self.forge_props.use_glb and not self.forge_props.update_forge_only:
                require_gltf_addon("export")
            if not self.begin_modal_operation():
                return {"CANCELLED"}
            self.geometry_map = {}
            self.attach_model_map = {}
            self.instance_templates = {}
            self.hfield_map = {}
            self.collider_map = {}
            self.geo_materials_map = {}
            self.materials_map = {}
            self.materials_props_map = {}
            self.filepath = (
                bpy.path.abspath(self.forge_props.export_path)
                if self.forge_props.rel_path
                else self.forge_props.export_path
            )
            self.root_element = ET.Element("mujoco")
            self.task_quene = [
                (self._gather_assets, (context,), {}),
                (self._export_images, (), {}),
                (self._export_hfields, (), {}),
                (self._export_visuals, (), {}),
                (self._export_colliders, (), {}),
                (self._set_includes, (context,), {}),
                (self._set_compiler, (context,), {}),
                (self._set_option, (context,), {}),
                (self._set_statistic, (context,), {}),
                (self._set_visual, (context,), {}),
                (self._set_assets, (context,), {}),
                (self._set_world, (context,), {}),
                (self._set_contact, (context,), {}),
                (self._set_equality, (context,), {}),
                (self._set_tendon, (context,), {}),
                (self._set_actuator, (context,), {}),
                (self._set_sensor, (context,), {}),
                (self._write_to_file, (context,), {}),
            ]

            self.stage_infos = [
                "Gathering assets...",
                "Exporting images...",
                "Exporting hfields...",
                "Exporting visuals...",
                "Exporting colliders...",
                "Exporting includes...",
                "Exporting compiler...",
                "Exporting option...",
                "Exporting statistic...",
                "Exporting visual...",
                "Exporting assets...",
                "Exporting world...",
                "Exporting contact...",
                "Exporting equality...",
                "Exporting tendon...",
                "Exporting actuator...",
                "Exporting sensor...",
                "Writing to file...",
            ]

            self.stage_task_count = len(self.task_quene)
            self.total_stage_task_count = self.stage_task_count
            self.stage_action_task_count = [1] * self.stage_task_count

            self.main_task_index = 0

            self.go_next_main_task(context)
            self.go_next_action()

            return super().execute(context)
        except Exception as ex:  # pylint: disable=broad-exception-caught
            message = f"Export fail: {str(ex):s}"
            self.abort_modal_operation(message)
            self.report({"ERROR"}, message)
            if self.forge_props is not None:
                self.reset_ui(context)
            return {"CANCELLED"}

    def invoke(self, context, event):
        """Invoke the export operator, initializing progress and starting execution.

        Args:
            context: The Blender context.
            event: The triggering event.

        Returns:
            A Blender operator result set.
        """
        scene = context.scene
        context.window.scene = bpy.data.scenes[scene.Main_Scene]
        self.forge_props = bpy.data.scenes[scene.Main_Scene].Forge_Props
        self.forge_props.is_exporting = True
        self.forge_props.progress = 0.02
        self.forge_props.progress_info = "Initialling..."
        if context.area is not None:
            context.area.tag_redraw()
        return self.execute(context)

    def reset_ui(self, context: Context):
        """Reset UI after export completes, clearing all progress values.

        Args:
            context: The Blender context.
        """
        self.forge_props.is_exporting = False
        self.forge_props.progress = 0.0
        self.forge_props.progress_info = ""
        self.forge_props.sub_progress = 0.0
        self.forge_props.sub_progress_info = ""
