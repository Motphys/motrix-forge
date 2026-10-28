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

"""MJCF import/export and blend-file persistence tools."""

from __future__ import annotations

from .. import call_blender, mcp
from ._hints import DESTRUCTIVE, WRITE

# Seconds a cancelled MJCF export waits for its modal task to stop before it
# gives up on cleaning the staged export and keeps the directory as recovery
# data. The task only has to notice ``cancel_requested``, so this is generous.
_CANCEL_CLEANUP_TIMEOUT = 60.0


@mcp.tool(annotations=DESTRUCTIVE, name="forge_import_mjcf")
def import_mjcf(filepath: str, import_material: bool = True) -> dict:
    """Import an MJCF file into Forge and wait for its modal job to finish.

    Import clears the current Forge scene objects, collections, non-main scenes
    and orphaned data before rebuilding the model. Save first if the current
    work must be retained.
    """
    code = """
import os
import bpy

path = os.path.abspath(bpy.path.abspath({filepath!r}))
if not os.path.isfile(path):
    raise RuntimeError(f"MJCF import file not found: {{path}}")
scene = bpy.data.scenes[bpy.context.scene.Main_Scene]
props = scene.Forge_Props
props.import_file_path = path
props.import_material = {import_material!r}
if props.modal_operation_active:
    raise RuntimeError(f"Forge modal operation already running: {{props.modal_operation_name}}")
props.modal_operation_deferred = True
try:
    # The MCP bridge has no file-browser UI context; execute directly.
    ret = bpy.ops.forge.import_mjcf('EXEC_DEFAULT')
except BaseException:
    props.modal_operation_deferred = False
    # The operator claimed the scene-level modal slot before failing; nothing
    # else releases it, so every later operation would be refused as
    # 'already running' for the rest of the session.
    if props.modal_operation_active and props.modal_operation_status != 'RUNNING':
        props.modal_operation_active = False
        props.modal_operation_token = ""
    raise
if 'CANCELLED' in ret:
    props.modal_operation_deferred = False
    if props.modal_operation_active and props.modal_operation_status != 'RUNNING':
        props.modal_operation_active = False
        props.modal_operation_token = ""
    raise RuntimeError("MJCF import failed to start")
operation_token = props.modal_operation_token

def release_operation():
    if props.modal_operation_token == operation_token:
        props.modal_operation_active = False
        props.modal_operation_deferred = False
        props.modal_operation_token = ""

def check_is_finished():
    if props.modal_operation_token != operation_token:
        raise RuntimeError("MJCF import operation state was replaced")
    if props.modal_operation_status == 'RUNNING':
        return None
    status = props.modal_operation_status
    message = props.modal_operation_message or f"MJCF import ended with {{status}}"
    release_operation()
    if status != 'FINISHED':
        raise RuntimeError(message)
    return {{
        "return_value": ["FINISHED"],
        "filepath": path,
        "scene": scene.name,
        "objects": len(scene.objects),
    }}

def cancel_operation():
    if props.modal_operation_token == operation_token:
        if props.modal_operation_status == 'RUNNING':
            if bpy.app.background:
                release_operation()
            else:
                props.modal_operation_deferred = False
                props.cancel_requested = True
        else:
            release_operation()

result = {{}}
""".format(filepath=filepath, import_material=import_material)
    return call_blender(code)


@mcp.tool(annotations=WRITE, name="forge_export_mjcf")
def export_mjcf(
    filepath: str,
    update_forge_only: bool = False,
    use_glb: bool = False,
    overwrite: bool = False,
) -> dict:
    """Export the Forge main scene to MJCF and wait for completion.

    The destination gets a `.xml` suffix when omitted. Existing XML and asset
    files are refused unless `overwrite=True`. `update_forge_only` and
    `use_glb` mirror `scene.Forge_Props` export settings. Compiler asset, mesh,
    and texture directories must stay inside the XML destination directory so
    every generated file can be staged and checked before commit.
    """
    if not filepath.lower().endswith(".xml"):
        filepath += ".xml"
    code = """
import os
import shutil
import tempfile
import time
import xml.etree.ElementTree as ET
from xml.dom import minidom

import bpy

requested_path = os.path.abspath(bpy.path.abspath({filepath!r}))
parent = os.path.dirname(requested_path)
if not os.path.isdir(parent):
    raise RuntimeError(f"MJCF export directory not found: {{parent}}")
if os.path.exists(requested_path) and not {overwrite!r}:
    raise RuntimeError(f"MJCF export destination exists; pass overwrite=True: {{requested_path}}")
scene = bpy.data.scenes[bpy.context.scene.Main_Scene]
props = scene.Forge_Props
if props.modal_operation_active:
    raise RuntimeError(f"Forge modal operation already running: {{props.modal_operation_name}}")
stage_dir = tempfile.mkdtemp(prefix=".forge-export-", dir=parent)
path = os.path.join(stage_dir, os.path.basename(requested_path))

def checked_export_dir(label, base, configured):
    candidate = os.path.abspath(os.path.join(base, configured)) if configured else base
    try:
        inside = os.path.commonpath((stage_dir, candidate)) == stage_dir
    except ValueError:
        inside = False
    if not inside:
        shutil.rmtree(stage_dir, ignore_errors=True)
        raise RuntimeError(f"Forge compiler {{label}} must stay inside the MJCF export directory: {{configured}}")
    return candidate

compiler = scene.Forge_GlobalConfig.g_compiler
asset_base = checked_export_dir("assetdir", stage_dir, compiler.assetdir)
compiler_base = asset_base if compiler.assetdir else stage_dir
checked_export_dir("meshdir", compiler_base, compiler.meshdir)
checked_export_dir("texturedir", compiler_base, compiler.texturedir)
props.export_path = path
props.rel_path = False
props.update_forge_only = {update_forge_only!r}
props.use_glb = {use_glb!r}

def cleanup_stage():
    shutil.rmtree(stage_dir, ignore_errors=True)

def restore_export_path():
    props.export_path = requested_path

def rewrite_include_paths():
    tree = ET.parse(path)
    root = tree.getroot()
    changed = False
    for include in root.iter("include"):
        value = include.get("file")
        if not value:
            continue
        source = os.path.abspath(os.path.join(stage_dir, value))
        try:
            final_value = os.path.relpath(source, parent)
        except ValueError:
            final_value = source
        if value != final_value:
            include.set("file", final_value)
            changed = True
    if changed:
        rough = ET.tostring(root, encoding="utf-8")
        pretty = minidom.parseString(rough).toprettyxml(indent="  ")
        if "\\n" in pretty:
            pretty = pretty.split("\\n", 1)[1]
        with open(path, "w", encoding="utf-8") as output:
            output.write(pretty)

def commit_export():
    restore_export_path()
    preserve_stage = False
    try:
        if not os.path.isfile(path):
            raise RuntimeError("MJCF export finished without producing the requested XML")
        rewrite_include_paths()
        staged = []
        for current_root, _dirs, filenames in os.walk(stage_dir):
            for filename in filenames:
                source = os.path.join(current_root, filename)
                relative = os.path.relpath(source, stage_dir)
                destination = os.path.join(parent, relative)
                staged.append((source, destination))
        conflicts = [destination for _source, destination in staged if os.path.exists(destination)]
        if conflicts and not {overwrite!r}:
            joined = ", ".join(conflicts)
            raise RuntimeError(f"MJCF export destinations exist; pass overwrite=True: {{joined}}")
        directories = [destination for _source, destination in staged if os.path.isdir(destination)]
        if directories:
            joined = ", ".join(directories)
            raise RuntimeError(f"MJCF export destination is a directory: {{joined}}")

        backup_dir = os.path.join(stage_dir, ".rollback")
        backups = []
        committed = []
        try:
            for index, (_source, destination) in enumerate(staged):
                if os.path.exists(destination):
                    os.makedirs(backup_dir, exist_ok=True)
                    backup = os.path.join(backup_dir, str(index))
                    os.replace(destination, backup)
                    backups.append((backup, destination))
            for source, destination in staged:
                os.makedirs(os.path.dirname(destination), exist_ok=True)
                os.replace(source, destination)
                committed.append(destination)
        except BaseException as commit_error:
            rollback_errors = []
            for destination in reversed(committed):
                try:
                    os.remove(destination)
                except OSError as error:
                    rollback_errors.append("remove %s: %s" % (destination, error))
            for backup, destination in reversed(backups):
                try:
                    os.makedirs(os.path.dirname(destination), exist_ok=True)
                    os.replace(backup, destination)
                except OSError as error:
                    rollback_errors.append("restore %s: %s" % (destination, error))
            if rollback_errors:
                preserve_stage = True
                details = "; ".join(rollback_errors)
                raise RuntimeError(
                    "MJCF export commit failed and rollback was incomplete; "
                    "recovery data preserved at %s: %s" % (stage_dir, details)
                ) from commit_error
            raise
        return [destination for _source, destination in staged]
    finally:
        if not preserve_stage:
            cleanup_stage()

props.modal_operation_deferred = True
try:
    ret = bpy.ops.forge.export_mjcf('INVOKE_DEFAULT')
except BaseException:
    props.modal_operation_deferred = False
    # The operator claimed the scene-level modal slot before failing; nothing
    # else releases it, so every later operation would be refused as
    # 'already running' for the rest of the session.
    if props.modal_operation_active and props.modal_operation_status != 'RUNNING':
        props.modal_operation_active = False
        props.modal_operation_token = ""
    restore_export_path()
    cleanup_stage()
    raise
if 'CANCELLED' in ret:
    props.modal_operation_deferred = False
    if props.modal_operation_active and props.modal_operation_status != 'RUNNING':
        props.modal_operation_active = False
        props.modal_operation_token = ""
    restore_export_path()
    cleanup_stage()
    raise RuntimeError("MJCF export failed to start")
operation_token = props.modal_operation_token

def release_operation():
    if props.modal_operation_token == operation_token:
        props.modal_operation_active = False
        props.modal_operation_deferred = False
        props.modal_operation_token = ""

def check_is_finished():
    if props.modal_operation_token != operation_token:
        raise RuntimeError("MJCF export operation state was replaced")
    if props.modal_operation_status == 'RUNNING':
        return None
    status = props.modal_operation_status
    message = props.modal_operation_message or f"MJCF export ended with {{status}}"
    release_operation()
    if status != 'FINISHED':
        restore_export_path()
        cleanup_stage()
        raise RuntimeError(message)
    files = commit_export()
    return {{
        "return_value": ["FINISHED"],
        "filepath": requested_path,
        "exists": os.path.isfile(requested_path),
        "size_bytes": os.path.getsize(requested_path) if os.path.isfile(requested_path) else 0,
        "files": files,
    }}

def cancel_operation():
    if props.modal_operation_token == operation_token:
        if props.modal_operation_status == 'RUNNING':
            if bpy.app.background:
                release_operation()
            else:
                props.modal_operation_deferred = False
            props.cancel_requested = True

            # The cancel request only takes effect once the modal task stops
            # writing into the stage directory, so wait for it — but bounded:
            # an operation that never leaves RUNNING keeps the staged export on
            # disk instead of having it deleted from under the exporter.
            cleanup_deadline = time.monotonic() + {cancel_cleanup_timeout!r}

            def cleanup_cancelled_export():
                current_token = props.modal_operation_token
                if current_token == operation_token and props.modal_operation_status == 'RUNNING':
                    if time.monotonic() < cleanup_deadline:
                        return 0.5
                    print(f"Forge export cancel cleanup gave up; staged export kept at {{stage_dir}}")
                    return None
                if current_token in ('', operation_token) and props.export_path == path:
                    restore_export_path()
                cleanup_stage()
                return None

            bpy.app.timers.register(cleanup_cancelled_export, first_interval=0.5)
        else:
            release_operation()
            restore_export_path()
            cleanup_stage()

result = {{}}
""".format(
        filepath=filepath,
        overwrite=overwrite,
        update_forge_only=update_forge_only,
        use_glb=use_glb,
        cancel_cleanup_timeout=_CANCEL_CLEANUP_TIMEOUT,
    )
    return call_blender(code)


@mcp.tool(annotations=DESTRUCTIVE, name="forge_save_blendfile")
def save_blendfile(filepath: str | None = None, overwrite: bool = False, save_copy: bool = False) -> dict:
    """Save the current `.blend` file.

    - With no `filepath`, saves to the current blend path (an unsaved file errors).
    - Existing destinations require `overwrite=True`, including the current path.
    - `save_copy=True` writes a copy without changing Blender's current file path.
    """
    code = """
import os
import bpy

requested = {filepath!r}
path = bpy.data.filepath if requested is None else os.path.abspath(bpy.path.abspath(requested))
if not path:
    raise RuntimeError("blend file has no path; provide filepath")
if not path.lower().endswith(".blend"):
    path += ".blend"
parent = os.path.dirname(path)
if not os.path.isdir(parent):
    raise RuntimeError(f"blend save directory not found: {{parent}}")
if os.path.exists(path) and not {overwrite!r}:
    raise RuntimeError(f"blend destination exists; pass overwrite=True: {{path}}")
before = bpy.data.filepath
ret = bpy.ops.wm.save_as_mainfile(filepath=path, copy={save_copy!r})
result = {{
    "return_value": list(ret),
    "filepath": path,
    "current_filepath": bpy.data.filepath,
    "previous_filepath": before,
    "save_copy": {save_copy!r},
}}
""".format(filepath=filepath, overwrite=overwrite, save_copy=save_copy)
    return call_blender(code)
