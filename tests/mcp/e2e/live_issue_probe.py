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

"""Probe known MCP/Forge issues against an already-running bridge.

Unlike the isolated E2E drivers, this script never starts or resets Blender.
It connects to FORGE_MCP_PORT (9876 by default) and runs the two issue
scenarios sequentially against the current session.
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


async def main(port: int) -> int:
    env = {**os.environ, "FORGE_MCP_PORT": str(port)}
    params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "forge_mcp"],
        cwd=str(Path(__file__).resolve().parents[3] / "mcp-server"),
        env=env,
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            async def call(tool: str, **kwargs):
                response = await session.call_tool(tool, kwargs)
                text = response.content[0].text if response.content else ""
                try:
                    payload = json.loads(text)
                except json.JSONDecodeError:
                    payload = {"raw": text}
                return getattr(response, "is_error", False), payload

            # The write tools are skill-gated; loading the guides is harmless
            # and does not change the current Blender scene.
            for skill in ("create", "modify"):
                failed, payload = await call("forge_skill", name=skill)
                if failed:
                    print(f"SKILL {skill}: FAIL {payload}")
                    return 2

            failed, before = await call("forge_scene_info")
            print("CURRENT SCENE:", json.dumps(before, ensure_ascii=False))
            if failed:
                print("scene_info failed")
                return 2

            links = [item["name"] for item in before.get("objects", []) if item.get("type") == "LINK"]
            if links:
                link = links[0]
            else:
                failed, created = await call("forge_create_link", select=[])
                if failed or not created.get("created"):
                    print("SETUP LINK: FAIL", json.dumps(created, ensure_ascii=False))
                    return 2
                link = created["created"][0]
            print("SETUP LINK:", link)

            print("\nISSUE 1 — subtree sensors (sequential calls)")
            issue1_failures = 0
            for sensor in ("Subtreecom", "Subtreelinvel", "Subtreeangmom"):
                failed, payload = await call("forge_create_sensor", sensor_type=sensor, set_subtree=True, select=[link])
                status = "FAIL (expected reproduction)" if failed else "PASS (unexpected)"
                if not failed:
                    issue1_failures += 1
                print(sensor, status, json.dumps(payload, ensure_ascii=False))

            failed, state = await call(
                "forge_execute",
                code="""import bpy
s = bpy.data.scenes[bpy.context.scene.Main_Scene]
p = s.Forge_Props
result = {
    'active': p.modal_operation_active,
    'status': p.modal_operation_status,
    'name': p.modal_operation_name,
    'token': p.modal_operation_token,
    'deferred': p.modal_operation_deferred,
}
""",
            )
            print("STATE AFTER SENSOR ISSUE:", json.dumps(state, ensure_ascii=False))

            print("\nISSUE 2 — include then attach (same bridge session)")
            external = Path(__file__).with_name("_live_probe_external.xml")
            try:
                external.write_text(
                    '<mujoco model="probe"><worldbody><body name="probe_base" /></worldbody></mujoco>',
                    encoding="utf-8",
                )
                failed, include = await call("forge_create_include", file=str(external), select=[])
                print("INCLUDE:", "FAIL" if failed else "PASS", json.dumps(include, ensure_ascii=False))
                failed, state = await call(
                    "forge_execute",
                    code="""import bpy
s = bpy.data.scenes[bpy.context.scene.Main_Scene]
p = s.Forge_Props
result = {
    'active': p.modal_operation_active,
    'status': p.modal_operation_status,
    'name': p.modal_operation_name,
    'token': p.modal_operation_token,
    'deferred': p.modal_operation_deferred,
}
""",
                )
                print("STATE AFTER INCLUDE:", json.dumps(state, ensure_ascii=False))
                failed, attach = await call("forge_create_attach", file=str(external), select=[])
                print(
                    "ATTACH AFTER INCLUDE:",
                    "FAIL (reproduced)" if failed else "PASS (not reproduced)",
                    json.dumps(attach, ensure_ascii=False),
                )
                failed, state = await call(
                    "forge_execute",
                    code="""import bpy
s = bpy.data.scenes[bpy.context.scene.Main_Scene]
p = s.Forge_Props
result = {
    'active': p.modal_operation_active,
    'status': p.modal_operation_status,
    'name': p.modal_operation_name,
    'token': p.modal_operation_token,
    'deferred': p.modal_operation_deferred,
}
""",
                )
                print("STATE AFTER ATTACH:", json.dumps(state, ensure_ascii=False))
            finally:
                external.unlink(missing_ok=True)

            print(f"\nprobe complete: subtree_unexpected_successes={issue1_failures}")
            return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=int(os.environ.get("FORGE_MCP_PORT", "9876")))
    args = parser.parse_args()
    raise SystemExit(asyncio.run(main(args.port)))
