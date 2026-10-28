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

"""Blendfile summary — one read-only health check: path status, datablock
counts, missing external files and linked libraries.
"""

from __future__ import annotations

from .. import call_blender, mcp
from ._hints import READ_ONLY

_SUMMARY_CODE = """
import os
import time

import bpy

filepath = bpy.data.filepath
path_exists = bool(filepath) and os.path.isfile(filepath)
path_info = {
    "filepath": filepath or None,
    "is_saved": bool(filepath),
    "exists": path_exists,
    "is_dirty": bpy.data.is_dirty,
}
if path_exists:
    stat = os.stat(filepath)
    path_info["age_seconds"] = round(time.time() - stat.st_mtime, 1)
    path_info["size_bytes"] = stat.st_size
if filepath:
    backups = []
    for i in range(1, 33):  # Blender numbers backups .blend1 .. .blend32, no gaps
        backup = filepath + str(i)
        if not os.path.exists(backup):
            break
        backups.append(os.path.basename(backup))
    path_info["backups"] = backups

datablocks = {}
for name in sorted(dir(bpy.data)):
    if name.startswith("_"):
        continue
    try:
        collection = getattr(bpy.data, name)
        if hasattr(collection, "__len__") and hasattr(collection, "keys") and len(collection) > 0:
            datablocks[name] = len(collection)
    except Exception:
        pass  # some collections raise during undo history

missing = []
checked = 0


def _visit(id_data, path, _placeholder):
    global checked
    checked += 1
    absolute = bpy.path.abspath(path)
    if not os.path.exists(absolute):
        missing.append({"id_type": type(id_data).__name__, "id_name": getattr(id_data, "name", ""), "path": absolute})


def _check_item(item):
    global checked
    path = getattr(item, "filepath", "")
    if not path or getattr(item, "packed_file", None) is not None:
        return
    checked += 1
    absolute = bpy.path.abspath(path)
    if not os.path.exists(absolute):
        missing.append({"id_type": type(item).__name__, "id_name": getattr(item, "name", ""), "path": absolute})


if hasattr(bpy.data, "file_path_foreach"):  # Blender 5.0+
    bpy.data.file_path_foreach(_visit, flags={"SKIP_PACKED", "SKIP_WEAK_REFERENCES", "RESOLVE_TOKEN"})
else:  # Blender 4.x fallback: walk the external-file-bearing collections
    for collection_name in ("images", "fonts", "volumes", "cache_files", "libraries"):
        for item in getattr(bpy.data, collection_name, []):
            _check_item(item)

linked_by_library = {}


def _tally(item):
    library = getattr(item, "library", None)
    if library is not None:
        key = library.name_full
        linked_by_library[key] = linked_by_library.get(key, 0) + 1


for name in dir(bpy.data):
    if name.startswith("_"):
        continue
    try:
        collection = getattr(bpy.data, name)
        if hasattr(collection, "__len__") and hasattr(collection, "keys"):
            for item in collection:
                _tally(item)
    except Exception:
        pass

libraries = {"total": len(bpy.data.libraries), "direct": [], "indirect": []}
for library in bpy.data.libraries:
    entry = {
        "name": library.name,
        "filepath": library.filepath,
        "linked_datablocks": linked_by_library.get(library.name_full, 0),
    }
    if library.parent is None:
        libraries["direct"].append(entry)
    else:
        entry["parent_library"] = library.parent.name
        libraries["indirect"].append(entry)

result = {
    "path_info": path_info,
    "datablocks": datablocks,
    "scene": bpy.context.scene.name,
    "render_engine": bpy.context.scene.render.engine,
    "workspaces": [workspace.name for workspace in bpy.data.workspaces],
    "active_workspace": bpy.context.window.workspace.name if bpy.context.window else None,
    "missing_files": {"count": len(missing), "total_checked": checked, "files": missing},
    "libraries": libraries,
}
"""


@mcp.tool(annotations=READ_ONLY, name="forge_blendfile_summary")
def blendfile_summary() -> dict:
    """Summarize the blend file: path/save status/age/backups, datablock counts, missing external files,
    linked libraries (direct vs indirect).
    """
    return call_blender(_SUMMARY_CODE)
