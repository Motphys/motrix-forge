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

from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> int:
    root = Path(__file__).resolve().parents[3]
    env = {**os.environ, "FORGE_MCP_PORT": os.environ.get("FORGE_MCP_PORT", "9876")}
    params = StdioServerParameters(
        command=sys.executable, args=["-m", "forge_mcp"], cwd=str(root / "mcp-server"), env=env
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            await session.call_tool("forge_skill", {"name": "modify"})

            async def call(tool: str, arguments: dict | None = None):
                response = await session.call_tool(tool, arguments or {})
                text = response.content[0].text if response.content else "{}"
                try:
                    data = json.loads(text)
                except json.JSONDecodeError:
                    data = {"raw": text}
                return getattr(response, "is_error", False), data

            # Hinge axes: local +Z rotated onto +Y in the parent frame.
            for name in ("EXC_BOOM_JOINT", "EXC_STICK_JOINT", "EXC_BUCKET_JOINT"):
                failed, data = await call(
                    "forge_set_transform", {"name": name, "rotation_euler": (-1.57079632679, 0.0, 0.0)}
                )
                if failed:
                    raise RuntimeError(data)

            visuals = [
                "EXC_BASE_FRAME",
                "EXC_TRACK_LEFT",
                "EXC_TRACK_RIGHT",
                "EXC_TRACK_FRAME",
                "EXC_PLATFORM",
                "EXC_COUNTERWEIGHT",
                "EXC_ENGINE_DECK",
                "EXC_CAB",
                "EXC_BOOM_MAIN",
                "EXC_BOOM_SIDE",
                "EXC_STICK_MAIN",
                "EXC_BUCKET_BODY",
                "EXC_BUCKET_CUTTING_EDGE",
                "EXC_BOOM_CYLINDER",
                "EXC_STICK_CYLINDER",
                "EXC_BUCKET_CYLINDER",
            ]
            mesh = {}
            for name in visuals:
                failed, data = await call("forge_mesh_check", {"select": [name]})
                mesh[name] = {"error": data} if failed else data

            failed, bounds = await call(
                "forge_execute",
                {
                    "code": """
import bpy
from mathutils import Vector

names = [o.name for o in bpy.context.scene.objects if o.Forge_Model_Type == 'VISUAL']
corners = []
for name in names:
    obj = bpy.data.objects[name]
    corners.extend([obj.matrix_world @ Vector(c) for c in obj.bound_box])
mins = [min(v[i] for v in corners) for i in range(3)] if corners else [0.0, 0.0, 0.0]
maxs = [max(v[i] for v in corners) for i in range(3)] if corners else [0.0, 0.0, 0.0]
result = {'visual_count': len(names), 'min': mins, 'max': maxs,
          'dimensions': [b - a for a, b in zip(mins, maxs)]}
"""
                },
            )
            if failed:
                raise RuntimeError(bounds)

            joints = {}
            for name in ("EXC_SWING_JOINT", "EXC_BOOM_JOINT", "EXC_STICK_JOINT", "EXC_BUCKET_JOINT"):
                _, joints[name] = await call("forge_object_info", {"name": name})
            inertials = {}
            for name in (
                "EXC_BASE_INERTIAL",
                "EXC_SLEW_PLATFORM_INERTIAL",
                "EXC_BOOM_INERTIAL",
                "EXC_STICK_INERTIAL",
                "EXC_BUCKET_INERTIAL",
            ):
                _, inertials[name] = await call("forge_object_info", {"name": name})
            _, scene = await call("forge_scene_info")
            print(
                json.dumps(
                    {
                        "scene": scene,
                        "joints": joints,
                        "inertials": inertials,
                        "mesh_checks": mesh,
                        "overall_bounds": bounds,
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
