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
            try:
                link1 = (await call("forge_create_link", select=[]))["created"][0]
                link2 = (await call("forge_create_link", select=[link1]))["created"][0]
                created += [link1, link2]

                exclude = await call("forge_create_contact", contact_type="EXCLUDE", select=[link1, link2])
                exclude_names = exclude["created"]
                created += exclude_names
                exclude_info = await call("forge_object_info", name=exclude_names[0])
                exclude_props = exclude_info.get("props") or {}
                exclude_ok = (
                    exclude_info.get("type") == "CONTACT"
                    and exclude_props.get("type") == "EXCLUDE"
                    and {exclude_props.get("target1"), exclude_props.get("target2")} == {link1, link2}
                )
                print(
                    "EXCLUDE:",
                    json.dumps({"create": exclude, "info": exclude_info, "valid": exclude_ok}, ensure_ascii=False),
                )

                visual1 = (await call("forge_create_geometry", geometry_type="BOX", select=[link1]))["created"]
                visual2 = (await call("forge_create_geometry", geometry_type="BOX", select=[link2]))["created"]
                created += visual1 + visual2
                pair = await call("forge_create_contact", contact_type="PAIR", select=[visual1[0], visual2[0]])
                pair_names = pair["created"]
                created += pair_names
                pair_info = await call("forge_object_info", name=pair_names[0])
                pair_props = pair_info.get("props") or {}
                pair_ok = (
                    pair_info.get("type") == "CONTACT"
                    and pair_props.get("type") == "PAIR"
                    and {pair_props.get("target1"), pair_props.get("target2")} == {visual1[0], visual2[0]}
                )
                print("PAIR:", json.dumps({"create": pair, "info": pair_info, "valid": pair_ok}, ensure_ascii=False))
                return 0 if exclude_ok and pair_ok else 1
            finally:
                if created:
                    response = await session.call_tool("forge_delete", {"names": created})
                    print("CLEANUP:", response.content[0].text if response.content else "")


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
