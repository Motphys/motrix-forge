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

"""Live check of the skill gate modes against a running Bridge.

Proves the thing the unit tests cannot: through the real stdio MCP server, a
client that never calls ``forge_skill`` can still drive Blender in the default
``soft`` mode, and gets a one-time ``skill_hint`` pointing at the guide. Then
``strict`` still refuses until the guide is read.

    FORGE_MCP_PORT=9876 python tests/mcp/e2e/live_skill_gate_probe.py
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_CWD = str(Path(__file__).resolve().parents[3] / "mcp-server")
CREATE_CODE = "import bpy\nbpy.ops.forge.create_link()\nresult = {'n': len(bpy.context.scene.objects)}"


def _params(gate: str, port: str) -> StdioServerParameters:
    return StdioServerParameters(
        command=sys.executable,
        args=["-m", "forge_mcp"],
        cwd=SERVER_CWD,
        env={**os.environ, "FORGE_MCP_PORT": port, "FORGE_MCP_SKILL_GATE": gate},
    )


async def _call(session: ClientSession, tool: str, **kwargs):
    response = await session.call_tool(tool, kwargs)
    text = response.content[0].text if response.content else ""
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        data = {"raw": text}
    return data, getattr(response, "is_error", False)


async def _scene_objects(session: ClientSession) -> set[str]:
    data, _ = await _call(session, "forge_scene_info")
    return {o["name"] if isinstance(o, dict) else o for o in data.get("objects") or []}


async def _run_op(session: ClientSession, before: set[str]) -> tuple[bool, dict, set[str]]:
    """Run the create script and report the objects it actually added.

    ``forge_execute`` returns whatever the script assigned to ``result``, not a
    created-object list, so the scene is diffed for cleanup.
    """
    data, is_error = await _call(session, "forge_execute", code=CREATE_CODE)
    added = await _scene_objects(session) - before
    return is_error, data, added


async def check_soft(port: str, results: list[tuple[str, bool, str]]) -> None:
    """Default mode: no prewarm, first call hints, second call is silent."""
    async with stdio_client(_params("soft", port)) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()  # deliberately NO forge_skill call
            before = await _scene_objects(session)

            is_error, data, added = await _run_op(session, before)
            results.append(("soft/first op needs no prewarm", not is_error and bool(added), str(data)[:200]))
            hint = data.get("skill_hint") or {}
            results.append(("soft/first op carries a skill_hint", hint.get("skills") == ["create"], str(hint)[:200]))
            results.append(("soft/hint carries a section index", bool(hint.get("sections", {}).get("create")), ""))

            is_error2, data2, added2 = await _run_op(session, before | added)
            results.append(("soft/second op still works", not is_error2 and bool(added2), str(data2)[:200]))
            results.append(("soft/second op has no repeat hint", "skill_hint" not in data2, ""))

            leftover = added | added2
            if leftover:
                await session.call_tool("forge_delete", {"names": sorted(leftover)})


async def check_off(port: str, results: list[tuple[str, bool, str]]) -> None:
    """off: the operation runs and nothing is ever hinted."""
    async with stdio_client(_params("off", port)) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            before = await _scene_objects(session)

            is_error, data, added = await _run_op(session, before)
            results.append(("off/op runs without reading the guide", not is_error and bool(added), str(data)[:200]))
            results.append(("off/never attaches a skill_hint", "skill_hint" not in data, str(data)[:200]))
            if added:
                await session.call_tool("forge_delete", {"names": sorted(added)})


async def check_strict(port: str, results: list[tuple[str, bool, str]]) -> None:
    """strict: refused before the guide is read, allowed after."""
    async with stdio_client(_params("strict", port)) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            before = await _scene_objects(session)

            is_error, data, added = await _run_op(session, before)
            results.append(
                (
                    "strict/op refused before reading the guide",
                    is_error and "SKILL_REQUIRED" in json.dumps(data) and not added,
                    str(data)[:200],
                )
            )

            await session.call_tool("forge_skill", {"name": "create"})
            is_error2, data2, added2 = await _run_op(session, before | added)
            results.append(
                ("strict/op allowed after reading the guide", not is_error2 and bool(added2), str(data2)[:200])
            )
            results.append(("strict/no hint once the guide is read", "skill_hint" not in data2, ""))
            if added2:
                await session.call_tool("forge_delete", {"names": sorted(added2)})


async def main() -> int:
    port = os.environ.get("FORGE_MCP_PORT", "9876")
    results: list[tuple[str, bool, str]] = []
    await check_soft(port, results)
    await check_off(port, results)
    await check_strict(port, results)

    failures = [label for label, ok, _ in results if not ok]
    for label, ok, detail in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}" + ("" if ok else f" — {detail}"))
    print(f"SKILL GATE PROBE: {'FAIL' if failures else 'PASS'}; cases={len(results)} failures={len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
