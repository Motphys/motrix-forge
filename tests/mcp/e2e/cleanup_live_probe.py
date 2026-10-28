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

"""Delete live-probe leftovers from the scene of a *running* Blender.

Targeted companion to the ``live_*.py`` probes, which are run by hand against a
bridge that is already listening (9876 by default, i.e. the developer's own
Blender with the Forge add-on loaded).  It removes only the objects those probes
leave behind — the shared ``LNK_Link`` and the ``INC__live_*_external_xml``
includes — and is not part of any automated suite (``driver.py`` spawns its own
Blender on 9877 precisely so that tests never touch a live session).

The names it matches are generic Forge output names, so it still deletes from a
scene it did not create; pass ``--yes`` to confirm:

    python tests/mcp/e2e/cleanup_live_probe.py --yes [--port 9876]
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

PROBE_OBJECT_PREFIXES = ("INC__live_probe_external_xml", "INC__live_multibody_external_xml")


def parse_args() -> argparse.Namespace:
    """Parse the port and the explicit confirmation flag."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--port", type=int, default=int(os.environ.get("FORGE_MCP_PORT", "9876")))
    parser.add_argument(
        "--yes",
        action="store_true",
        help="confirm deleting the matched objects in the attached Blender's scene",
    )
    return parser.parse_args()


async def main(args: argparse.Namespace) -> int:
    """Delete the probe leftovers from the attached bridge, after confirmation."""
    if not args.yes:
        print(f"refusing to delete objects on port {args.port} without --yes")
        return 2

    env = {**os.environ, "FORGE_MCP_PORT": str(args.port)}
    params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "forge_mcp"],
        cwd=str(Path(__file__).resolve().parents[3] / "mcp-server"),
        env=env,
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            await session.call_tool("forge_skill", {"name": "modify"})
            response = await session.call_tool("forge_scene_info", {})
            data = json.loads(response.content[0].text)
            print("SCENE:", json.dumps(data, ensure_ascii=False))
            names = [
                item["name"]
                for item in data.get("objects", [])
                if item.get("name") == "LNK_Link" or item.get("name", "").startswith(PROBE_OBJECT_PREFIXES)
            ]
            if names:
                response = await session.call_tool("forge_delete", {"names": names})
                print(response.content[0].text)
            else:
                print("no live probe objects found")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main(parse_args())))
