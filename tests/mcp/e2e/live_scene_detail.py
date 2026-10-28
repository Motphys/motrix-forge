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
        command=sys.executable,
        args=["-m", "forge_mcp"],
        cwd=str(root / "mcp-server"),
        env=env,
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            await session.call_tool("forge_skill", {"name": "modify"})

            async def call(name: str, arguments: dict | None = None) -> dict:
                response = await session.call_tool(name, arguments or {})
                text = response.content[0].text if response.content else "{}"
                try:
                    data = json.loads(text)
                except json.JSONDecodeError:
                    data = {"raw": text}
                if getattr(response, "is_error", False):
                    data = {"error": data}
                return data

            scene = await call("forge_scene_info")
            config = await call("forge_scene_config")
            details = []
            for item in scene.get("objects", []):
                details.append(await call("forge_object_info", {"name": item["name"]}))
            print(
                json.dumps({"scene": scene, "config": config, "object_details": details}, ensure_ascii=False, indent=2)
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
