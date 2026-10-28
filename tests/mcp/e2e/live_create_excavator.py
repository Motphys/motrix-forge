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
import math
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
            await session.call_tool("forge_skill", {"name": "create"})
            await session.call_tool("forge_skill", {"name": "modify"})

            async def call(tool: str, **kwargs):
                response = await session.call_tool(tool, kwargs)
                text = response.content[0].text if response.content else "{}"
                try:
                    data = json.loads(text)
                except json.JSONDecodeError:
                    data = {"raw": text}
                if getattr(response, "is_error", False):
                    raise RuntimeError(f"{tool}: {data}")
                if "error" in data:
                    raise RuntimeError(f"{tool}: {data}")
                return data

            async def rename(old: str, new: str):
                await call("forge_rename", name_map={old: new})
                return new

            async def create_link(name: str, parent: str | None = None):
                data = await call("forge_create_link", select=[] if parent is None else [parent])
                return await rename(data["created"][0], name)

            async def create_visual(name: str, parent: str, size: tuple[float, float, float], loc, rot=(0.0, 0.0, 0.0)):
                data = await call("forge_create_geometry", geometry_type="BOX", size_box=size, select=[parent])
                obj = await rename(data["created"][0], name)
                await call("forge_set_transform", name=obj, location=loc, rotation_euler=rot)
                await call("forge_set_property", name=obj, values={"density": 600.0})
                return obj

            async def create_capsule(name: str, parent: str, radius: float, height: float, loc, rot):
                data = await call(
                    "forge_create_geometry",
                    geometry_type="CAPSULE",
                    size_radius=radius,
                    size_height=height,
                    select=[parent],
                )
                obj = await rename(data["created"][0], name)
                await call("forge_set_transform", name=obj, location=loc, rotation_euler=rot)
                return obj

            async def collider(name: str, visual: str):
                data = await call(
                    "forge_create_collider", create_method="GEOMETRY_TYPE", auto_size=True, select=[visual]
                )
                return await rename(data["created"][0], name)

            async def inertial(link: str):
                data = await call("forge_create_inertial", select=[link])
                return await rename(data["created"][0], f"{link}_INERTIAL")

            async def joint(name: str, parent: str, location):
                data = await call("forge_create_joint", joint_type="HINGE", select=[parent])
                obj = await rename(data["created"][0], name)
                await call("forge_set_transform", name=obj, location=location)
                return obj

            async def actuator(name: str, joint_name: str, kind: str):
                data = await call("forge_create_actuator", actuator_type=kind, select=[joint_name])
                return await rename(data["created"][0], name)

            # Root carrier and undercarriage. Coordinates: X forward, Y left, Z up.
            base = await create_link("EXC_BASE")
            await call("forge_mark_root_link", select=[base])
            base_visual = await create_visual("EXC_BASE_FRAME", base, (3.4, 2.2, 0.55), (0.0, 0.0, 0.55))
            await inertial(base)
            await collider("EXC_BASE_COLLIDER", base_visual)
            await create_visual("EXC_TRACK_LEFT", base, (4.0, 0.70, 0.90), (0.0, -1.05, 0.50))
            await create_visual("EXC_TRACK_RIGHT", base, (4.0, 0.70, 0.90), (0.0, 1.05, 0.50))
            await create_visual("EXC_TRACK_FRAME", base, (2.9, 1.8, 0.35), (0.0, 0.0, 1.05))

            # Swing platform, counterweight, engine deck and operator cab.
            platform = await create_link("EXC_SLEW_PLATFORM", base)
            await call("forge_set_transform", name=platform, location=(0.0, 0.0, 1.25))
            platform_visual = await create_visual("EXC_PLATFORM", platform, (2.8, 1.9, 0.45), (0.0, 0.0, 0.0))
            await inertial(platform)
            await collider("EXC_PLATFORM_COLLIDER", platform_visual)
            await create_visual("EXC_COUNTERWEIGHT", platform, (1.55, 1.45, 1.00), (-0.95, 0.45, 0.72))
            await create_visual("EXC_ENGINE_DECK", platform, (1.45, 1.1, 0.55), (-0.35, 0.45, 0.50))
            await create_visual("EXC_CAB", platform, (1.55, 1.35, 1.65), (0.35, -0.48, 0.92))

            # Boom, stick and bucket form the working equipment.
            boom = await create_link("EXC_BOOM", platform)
            await call(
                "forge_set_transform",
                name=boom,
                location=(1.05, 0.0, 0.35),
                rotation_euler=(0.0, math.radians(-20.0), 0.0),
            )
            boom_visual = await create_visual("EXC_BOOM_MAIN", boom, (3.5, 0.55, 0.55), (1.70, 0.0, 0.12))
            await inertial(boom)
            await collider("EXC_BOOM_COLLIDER", boom_visual)
            await create_visual("EXC_BOOM_SIDE", boom, (2.9, 0.62, 0.20), (1.45, 0.0, -0.18))

            stick = await create_link("EXC_STICK", boom)
            await call(
                "forge_set_transform",
                name=stick,
                location=(3.35, 0.0, 0.0),
                rotation_euler=(0.0, math.radians(-38.0), 0.0),
            )
            stick_visual = await create_visual("EXC_STICK_MAIN", stick, (2.75, 0.45, 0.45), (1.30, 0.0, -0.02))
            await inertial(stick)
            await collider("EXC_STICK_COLLIDER", stick_visual)

            bucket = await create_link("EXC_BUCKET", stick)
            await call(
                "forge_set_transform",
                name=bucket,
                location=(2.45, 0.0, -0.03),
                rotation_euler=(0.0, math.radians(62.0), 0.0),
            )
            bucket_visual = await create_visual("EXC_BUCKET_BODY", bucket, (1.35, 1.35, 0.80), (0.55, 0.0, -0.25))
            await inertial(bucket)
            await collider("EXC_BUCKET_COLLIDER", bucket_visual)
            await create_visual("EXC_BUCKET_CUTTING_EDGE", bucket, (1.45, 1.45, 0.16), (1.05, 0.0, -0.55))

            # Hydraulic cylinders, represented as capsules with realistic radii.
            await create_capsule(
                "EXC_BOOM_CYLINDER", platform, 0.12, 2.20, (0.90, 0.0, 0.95), (0.0, math.radians(-55.0), 0.0)
            )
            await create_capsule(
                "EXC_STICK_CYLINDER", boom, 0.10, 1.90, (2.10, -0.32, 0.15), (0.0, math.radians(-65.0), 0.0)
            )
            await create_capsule(
                "EXC_BUCKET_CYLINDER", stick, 0.08, 1.20, (1.20, -0.28, -0.05), (0.0, math.radians(-35.0), 0.0)
            )

            # Four representative hinge axes and their hydraulic actuators.
            swing_joint = await joint("EXC_SWING_JOINT", base, (0.0, 0.0, 1.25))
            boom_joint = await joint("EXC_BOOM_JOINT", platform, (1.05, 0.0, 0.35))
            stick_joint = await joint("EXC_STICK_JOINT", boom, (3.35, 0.0, 0.0))
            bucket_joint = await joint("EXC_BUCKET_JOINT", stick, (2.45, 0.0, -0.03))
            await actuator("EXC_SWING_MOTOR", swing_joint, "MOTOR")
            await actuator("EXC_BOOM_ACTUATOR", boom_joint, "POSITION")
            await actuator("EXC_STICK_ACTUATOR", stick_joint, "POSITION")
            await actuator("EXC_BUCKET_ACTUATOR", bucket_joint, "POSITION")

            scene = await call("forge_scene_info")
            print(json.dumps(scene, ensure_ascii=False, indent=2))
            names = [item["name"] for item in scene.get("objects", [])]
            # Inspect major links and measure overall extents.
            major = [base, platform, boom, stick, bucket]
            details = []
            for name in major:
                details.append(await call("forge_object_info", name=name))
            measure = await call("forge_measure", names=["EXC_BASE_FRAME", "EXC_BUCKET_BODY", "EXC_CAB"])
            print(json.dumps({"major_details": details, "measure": measure}, ensure_ascii=False, indent=2))
            print(f"CREATED_OBJECTS={len(names)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
