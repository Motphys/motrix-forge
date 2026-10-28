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

"""Viewport capture — screenshot an area or the whole window for visual verification.

The Blender-side code runs in the addon's timer callback on the main thread,
where ``bpy.context`` has no validated window/area, so area lookups walk
``window.screen.areas`` explicitly and the screenshot operator runs under
``temp_override``.
"""

from __future__ import annotations

import base64
from typing import Literal

from mcp.server.mcpserver import Image

from .. import call_blender, mcp
from ._hints import READ_ONLY

AreaUIType = Literal[
    "VIEW_3D",
    "IMAGE_EDITOR",
    "UV",
    "ShaderNodeTree",
    "CompositorNodeTree",
    "GeometryNodeTree",
    "TextureNodeTree",
    "SEQUENCE_EDITOR",
    "CLIP_EDITOR",
    "DOPESHEET_EDITOR",
    "GRAPH_EDITOR",
    "NLA_EDITOR",
    "TEXT_EDITOR",
    "CONSOLE",
    "INFO",
    "TOPBAR",
    "STATUSBAR",
    "OUTLINER",
    "PROPERTIES",
    "FILE_BROWSER",
    "SPREADSHEET",
    "PREFERENCES",
]

_SCREENSHOT_CODE = """
import base64
import math
import os
import tempfile

import bpy

if bpy.app.background:
    raise RuntimeError("screenshot requires Blender in GUI mode (no window or areas in background mode)")
window = bpy.context.window
if window is None:
    raise RuntimeError("no active window - screenshot requires Blender in GUI mode")


def _space_info(area):
    space = area.spaces.active
    info = {"type": area.type, "ui_type": area.ui_type}
    if area.type == "VIEW_3D":
        r3d = space.region_3d
        if r3d is not None:
            info["view_perspective"] = r3d.view_perspective
            info["view_location"] = [round(v, 4) for v in r3d.view_location]
        info["shading"] = space.shading.type
        info["show_overlays"] = space.overlay.show_overlays
    elif area.type == "PROPERTIES":
        info["tab"] = space.context
    elif area.type == "OUTLINER":
        info["display_mode"] = space.display_mode
    elif area.type == "NODE_EDITOR":
        info["tree_type"] = space.tree_type
        info["node_tree"] = space.node_tree.name if space.node_tree else None
    elif area.type == "TEXT_EDITOR":
        info["text"] = space.text.name if space.text else None
    return info


if params["layout"]:
    areas = [
        {
            "type": area.type,
            "ui_type": area.ui_type,
            "x": area.x,
            "y": area.y,
            "width": area.width,
            "height": area.height,
            "space": _space_info(area),
            "regions": [
                {"type": region.type, "width": region.width, "height": region.height}
                for region in area.regions
                if region.width > 0 and region.height > 0
            ],
        }
        for area in window.screen.areas
    ]
    view_layer = bpy.context.view_layer
    result = {
        "window": [window.width, window.height],
        "workspace": window.workspace.name,
        "scene": bpy.context.scene.name,
        "areas": areas,
        "active_object": bpy.context.active_object.name if bpy.context.active_object else None,
        "selected_objects": [obj.name for obj in bpy.context.selected_objects],
    }
else:
    with tempfile.TemporaryDirectory(prefix="forge_shot_") as tmp:
        path = os.path.join(tmp, "shot.png")
        if params["whole_window"]:
            with bpy.context.temp_override(window=window):
                ret = bpy.ops.screen.screenshot(filepath=path)
        else:
            matching = [area for area in window.screen.areas if area.ui_type == params["area_ui_type"]]
            if not matching:
                available = sorted({area.ui_type for area in window.screen.areas})
                raise RuntimeError(f"no area with ui_type {params['area_ui_type']!r}; available: {available}")
            area = next((a for a in matching if a == bpy.context.area), max(matching, key=lambda a: a.width * a.height))
            override = {"window": window, "area": area}
            region = next((r for r in area.regions if r.type == "WINDOW"), None)
            if region is not None:
                override["region"] = region
            with bpy.context.temp_override(**override):
                ret = bpy.ops.screen.screenshot_area(filepath=path)
        if "CANCELLED" in ret or not os.path.exists(path):
            raise RuntimeError(f"screenshot operator failed (result: {ret})")
        with open(path, "rb") as fh:
            data = fh.read()

        width = height = None
        limit = params["size_limit_bytes"] or (1048576 * 3) // 4  # MCP budget with base64 4/3 expansion
        downscale_skipped = False
        try:
            import imbuf

            image_buf = imbuf.load(path)
            width, height = image_buf.size
            if len(data) > limit:
                divisor = max(1.0, float(bpy.context.preferences.system.pixel_size))  # HiDPI first
                for _ in range(12):  # guided search: PNG size tracks pixel count
                    scale = 1.0 / divisor
                    new_size = (max(64, int(width * scale)), max(64, int(height * scale)))
                    image_buf.resize(new_size, method="BILINEAR")
                    resized_path = path + ".resized.png"
                    image_buf.filepath = resized_path  # single-arg write: 4.5 rejects the filepath argument
                    imbuf.write(image_buf)
                    with open(resized_path, "rb") as fh:
                        data = fh.read()
                    width, height = new_size
                    if len(data) <= limit or min(new_size) <= 64:
                        break
                    divisor = max(divisor + 1.0, divisor * math.sqrt(len(data) / limit))
        except ImportError:
            downscale_skipped = True

        result = {
            "image_base64": base64.b64encode(data).decode("ascii"),
            "width": width,
            "height": height,
            "bytes": len(data),
        }
        if downscale_skipped:
            result["downscale_skipped"] = True  # imbuf unavailable - original size returned
"""


@mcp.tool(annotations=READ_ONLY, name="forge_screenshot")
def screenshot(
    area_ui_type: AreaUIType = "VIEW_3D",
    whole_window: bool = False,
    layout: bool = False,
    size_limit_bytes: int = 0,
) -> object:
    """Screenshot a Blender area (default the 3D viewport) or the whole window as a PNG image.

    - `area_ui_type` picks the largest matching area; `whole_window=True` captures everything instead.
    - `layout=True` skips the image and returns the window layout as JSON (areas, regions, view state, selection).
    - `size_limit_bytes` (0 = default ~768KB) downsamples the PNG via imbuf when larger.
    """
    res = call_blender(
        "params = "
        + repr(
            {
                "area_ui_type": area_ui_type,
                "whole_window": whole_window,
                "layout": layout,
                "size_limit_bytes": size_limit_bytes,
            }
        )
        + "\n"
        + _SCREENSHOT_CODE
    )
    if layout:
        return res
    return Image(data=base64.b64decode(res["image_base64"]), format="png")
