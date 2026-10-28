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
            await session.call_tool("forge_skill", {"name": "create"})
            await session.call_tool("forge_skill", {"name": "modify"})

            async def call(tool: str, **kwargs):
                response = await session.call_tool(tool, kwargs)
                text = response.content[0].text if response.content else ""
                try:
                    payload = json.loads(text)
                except json.JSONDecodeError:
                    payload = {"raw": text}
                return getattr(response, "is_error", False), payload

            created: list[str] = []
            try:
                _, link = await call("forge_create_link", select=[])
                link_name = link["created"][0]
                created.append(link_name)
                _, joint = await call("forge_create_joint", joint_type="HINGE", select=[link_name])
                joint_name = joint["created"][0]
                created.append(joint_name)
                _, actuator = await call("forge_create_actuator", actuator_type="MOTOR", select=[joint_name])
                actuator_name = actuator["created"][0]
                created.append(actuator_name)

                _, before = await call("forge_object_info", name=actuator_name)
                print("BEFORE:", json.dumps(before.get("props"), ensure_ascii=False))

                gear = [2.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                failed, via_mcp = await call("forge_set_property", name=actuator_name, values={"gear": gear})
                _, after_mcp = await call("forge_object_info", name=actuator_name)
                print("MCP SET:", "ERROR" if failed else "OK", json.dumps(via_mcp, ensure_ascii=False))
                print("AFTER MCP:", json.dumps(after_mcp.get("props"), ensure_ascii=False))

                direct_code = f"""import bpy
obj = bpy.data.objects[{actuator_name!r}]
before = list(obj.Forge_Actuator.gear)
obj.Forge_Actuator.gear = {gear!r}
after = list(obj.Forge_Actuator.gear)
result = {{'before': before, 'after': after, 'equal': after == {gear!r}}}
"""
                failed, direct = await call("forge_execute", code=direct_code)
                _, after_direct = await call("forge_object_info", name=actuator_name)
                print("DIRECT SET:", "ERROR" if failed else "OK", json.dumps(direct, ensure_ascii=False))
                print("AFTER DIRECT:", json.dumps(after_direct.get("props"), ensure_ascii=False))
                return (
                    0 if not failed and direct.get("equal") and after_direct.get("props", {}).get("gear") == gear else 1
                )
            finally:
                if created:
                    response = await session.call_tool("forge_delete", {"names": created})
                    print("CLEANUP:", response.content[0].text if response.content else "")


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
