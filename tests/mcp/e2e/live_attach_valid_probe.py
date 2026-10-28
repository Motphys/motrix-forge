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
import shutil
import sys
import tempfile
import uuid
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> int:
    root = Path(__file__).resolve().parents[3]
    # Scratch directory: an interrupted run must not leave a file in the source
    # tree, and the attach reads the model from here either way.
    work_dir = Path(tempfile.mkdtemp(prefix="forge_attach_valid_"))
    external = work_dir / f"_attach_valid_{uuid.uuid4().hex}.xml"
    # One write: ``write_text`` truncates, so three calls left only the last chunk.
    external.write_text(
        '<mujoco model="attach_model">'
        '<worldbody><body name="base"><geom name="base_geom" type="box" size="0.1 0.1 0.1"/></body></worldbody>'
        "</mujoco>",
        encoding="utf-8",
    )
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
                    data = json.loads(text)
                except json.JSONDecodeError:
                    data = {"raw": text}
                return getattr(response, "is_error", False), data

            created: list[str] = []
            try:
                failed, parent = await call("forge_create_link", select=[])
                parent_name = parent.get("created", [None])[0]
                if parent_name:
                    created.append(parent_name)
                print("PARENT:", json.dumps(parent, ensure_ascii=False))
                failed, attach = await call(
                    "forge_create_attach",
                    file=str(external),
                    model="attach_model",
                    prefix="ATT_VALID_",
                    link="None",
                    select=[parent_name],
                )
                print("ATTACH:", "FAIL" if failed else "PASS", json.dumps(attach, ensure_ascii=False))
                if not failed:
                    created.extend(attach.get("created", []))
                return 1 if failed else 0
            finally:
                shutil.rmtree(work_dir, ignore_errors=True)
                if created:
                    response = await session.call_tool("forge_delete", {"names": list(dict.fromkeys(created))})
                    print("CLEANUP:", response.content[0].text if response.content else "")


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
