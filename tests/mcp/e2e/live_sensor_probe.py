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
    env = {**os.environ, "FORGE_MCP_PORT": os.environ.get("FORGE_MCP_PORT", "9876")}
    params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "forge_mcp"],
        cwd=str(Path(__file__).resolve().parents[3] / "mcp-server"),
        env=env,
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            for skill in ("create", "modify"):
                await session.call_tool("forge_skill", {"name": skill})

            async def call(tool: str, **kwargs):
                response = await session.call_tool(tool, kwargs)
                text = response.content[0].text if response.content else ""
                try:
                    data = json.loads(text)
                except json.JSONDecodeError:
                    data = {"raw": text}
                if getattr(response, "is_error", False):
                    raise RuntimeError(data)
                return data

            created: list[str] = []
            failures = []
            try:
                link = (await call("forge_create_link", select=[]))["created"][0]
                created.append(link)
                joint = (await call("forge_create_joint", joint_type="HINGE", select=[link]))["created"][0]
                site = (await call("forge_create_site", site_type="SPHERE", select=[link]))["created"][0]
                visual = (await call("forge_create_geometry", geometry_type="BOX", select=[link]))["created"][0]
                created += [joint, site, visual]

                cases = [
                    ("Jointpos", joint, {}, "JOINT"),
                    ("Jointvel", joint, {}, "JOINT"),
                    ("Touch", site, {}, "SITE"),
                    ("Accelerometer", site, {}, "SITE"),
                    ("Velocimeter", site, {}, "SITE"),
                    ("Gyro", site, {}, "SITE"),
                    ("Framepos", link, {}, "BODY"),
                    ("Framequat", link, {}, "BODY"),
                    ("Framexaxis", link, {}, "BODY"),
                    ("Frameyaxis", link, {}, "BODY"),
                    ("Framezaxis", link, {}, "BODY"),
                    ("Framelinvel", link, {}, "BODY"),
                    ("Frameangvel", link, {}, "BODY"),
                    # Subtree sensors use a LINK target with the default BODY
                    # selection context; set_subtree=True is only for Contact.
                    ("Subtreecom", link, {}, "BODY"),
                    ("Subtreelinvel", link, {}, "BODY"),
                    ("Subtreeangmom", link, {}, "BODY"),
                ]
                for sensor_type, target, flags, target_type in cases:
                    made = await call("forge_create_sensor", sensor_type=sensor_type, select=[target], **flags)
                    name = made["created"][0]
                    created.append(name)
                    info = await call("forge_object_info", name=name)
                    props = info.get("props") or {}
                    valid = (
                        info.get("type") == "SENSOR"
                        and props.get("type") == sensor_type
                        and props.get("target") == target
                        and props.get("target_type") == target_type
                    )
                    if not valid:
                        failures.append(sensor_type)
                    print(
                        f"{sensor_type}: {'PASS' if valid else 'FAIL'} type={props.get('type')} "
                        f"target={props.get('target')} target_type={props.get('target_type')}"
                    )

                # Contact sensors have three valid target contexts.
                for label, target, flags, expected in (
                    ("Contact/body", link, {}, "BODY"),
                    ("Contact/subtree", link, {"set_subtree": True}, "SUBTREE"),
                    ("Contact/site", site, {}, "SITE"),
                    ("Contact/geom", visual, {}, "GEOM"),
                ):
                    made = await call("forge_create_sensor", sensor_type="Contact", select=[target], **flags)
                    name = made["created"][0]
                    created.append(name)
                    info = await call("forge_object_info", name=name)
                    props = info.get("props") or {}
                    valid = (
                        props.get("type") == "Contact"
                        and props.get("target") == target
                        and props.get("target_type") == expected
                    )
                    if not valid:
                        failures.append(label)
                    print(
                        f"{label}: {'PASS' if valid else 'FAIL'} target={props.get('target')} "
                        f"target_type={props.get('target_type')} use_subtree={props.get('use_subtree')}"
                    )
                return 0 if not failures else 1
            finally:
                if created:
                    response = await session.call_tool("forge_delete", {"names": [created[0]]})
                    print("CLEANUP:", response.content[0].text if response.content else "")


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
