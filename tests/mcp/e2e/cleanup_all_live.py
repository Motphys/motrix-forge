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

"""Delete every object in the scene of a *running* Blender, over the live bridge.

Destructive helper for clearing a manual test session: it attaches to the bridge
port that is already listening (9876 by default, i.e. the developer's own Blender
with the Forge add-on loaded) and removes every object the scene reports.  It is
not part of any automated suite — ``driver.py`` spawns its own Blender on 9877
precisely so that tests never touch a live session.

Because running it by accident destroys unsaved work, it refuses to delete
anything unless ``--yes`` is passed explicitly:

    python tests/mcp/e2e/cleanup_all_live.py --yes [--port 9876]
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


def parse_args() -> argparse.Namespace:
    """Parse the port and the explicit confirmation flag."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--port", type=int, default=int(os.environ.get("FORGE_MCP_PORT", "9876")))
    parser.add_argument(
        "--yes",
        action="store_true",
        help="confirm deleting every object in the attached Blender's scene",
    )
    return parser.parse_args()


async def main(args: argparse.Namespace) -> int:
    """Delete all scene objects from the attached bridge, after confirmation."""
    if not args.yes:
        print(
            f"refusing to delete objects on port {args.port} without --yes: "
            "this wipes the scene of the Blender that owns that bridge"
        )
        return 2

    root = Path(__file__).resolve().parents[3]
    env = {**os.environ, "FORGE_MCP_PORT": str(args.port)}
    params = StdioServerParameters(
        command=sys.executable, args=["-m", "forge_mcp"], cwd=str(root / "mcp-server"), env=env
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            await session.call_tool("forge_skill", {"name": "modify"})
            response = await session.call_tool("forge_scene_info", {})
            data = json.loads(response.content[0].text)
            names = [item["name"] for item in data.get("objects", [])]
            print(f"deleting {len(names)} object(s) from port {args.port}")
            if names:
                response = await session.call_tool("forge_delete", {"names": names})
                print(response.content[0].text)
            response = await session.call_tool("forge_scene_info", {})
            print(response.content[0].text)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main(parse_args())))
