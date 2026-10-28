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

"""MCP protocol integration tests — spawn the real forge-mcp server over stdio.

No Blender required: exercises initialize / tools / resources / forge_skill /
forge_search_docs / FORGE_TOOLS filtering over the wire.
"""

import asyncio
import json
import os
import sys
from pathlib import Path

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_DIR = Path(__file__).resolve().parents[3] / "mcp-server"


def _params(env_extra: dict | None = None) -> StdioServerParameters:
    # Run the checked-out server directly so protocol tests do not depend on
    # uv's cache or on a network connection while spawning each test server.
    env = {**os.environ, **(env_extra or {})}
    return StdioServerParameters(
        command=sys.executable,
        args=["-m", "forge_mcp"],
        cwd=str(SERVER_DIR),
        env=env,
    )


async def _with_session(fn, env_extra: dict | None = None):
    async with stdio_client(_params(env_extra)) as (read, write):
        async with ClientSession(read, write) as session:
            init = await session.initialize()
            return await fn(session, init)


def _run(coro):
    return asyncio.run(coro)


def _text(result) -> str:
    return result.content[0].text


def test_initialize_announces_forge_mcp():
    async def check(session, init):
        assert init.server_info.name == "forge-mcp"
        assert "forge_skill" in (init.instructions or "")
        return True

    assert _run(_with_session(check))


def test_tools_and_resources_listed():
    async def check(session, _init):
        tools = (await session.list_tools()).tools
        resources = (await session.list_resources()).resources
        assert len(tools) == 55
        assert all(t.name.startswith("forge_") for t in tools)
        assert len(resources) == 16
        assert all(str(r.uri).startswith("mjcf://") for r in resources)
        return True

    assert _run(_with_session(check))


def test_read_resource_body_and_index():
    async def check(session, _init):
        body = await session.read_resource("mjcf://body")
        assert body.contents[0].text.startswith("# body")
        assert body.contents[0].mime_type == "text/markdown"
        index = await session.read_resource("mjcf://index")
        assert index.contents[0].text.startswith("# MJCF XML Reference")
        return True

    assert _run(_with_session(check))


def test_read_resource_unknown_errors():
    async def check(session, _init):
        with pytest.raises(Exception):
            await session.read_resource("mjcf://nope")
        return True

    assert _run(_with_session(check))


def test_forge_skill_full_section_and_errors():
    async def check(session, _init):
        full = await session.call_tool("forge_skill", {"name": "create"})
        assert not full.is_error and _text(full).startswith("# Forge create")

        sec = await session.call_tool("forge_skill", {"name": "create", "section": "joint"})
        assert not sec.is_error
        assert _text(sec).splitlines()[0].strip() == "#### `joint`:"
        assert "create_light" not in _text(sec)

        # The tool's own message must survive the trip: a generic
        # "Error executing tool ..." would leave the caller nothing to act on.
        bad = await session.call_tool("forge_skill", {"name": "create", "section": "bogus"})
        assert bad.is_error
        assert "no section" in _text(bad) and "available" in _text(bad)

        no_skill = await session.call_tool("forge_skill", {"name": "nope"})
        assert no_skill.is_error
        assert "unknown skill 'nope'" in _text(no_skill)

        bad_args = await session.call_tool("forge_search_docs", {"query": "condim", "max_results": 0})
        assert bad_args.is_error
        assert "max_results must be positive" in _text(bad_args)

        missing = await session.call_tool("forge_skill", {})
        assert missing.is_error

        return True

    assert _run(_with_session(check))


def test_search_docs_returns_json_hits():
    async def check(session, _init):
        res = await session.call_tool("forge_search_docs", {"query": "condim", "max_results": 3})
        assert not res.is_error
        data = json.loads(_text(res))
        assert data["matched"] == "all" and data["hits"]

        empty = await session.call_tool("forge_search_docs", {"query": ""})
        assert not empty.is_error
        assert json.loads(_text(empty))["matched"] == "none"
        return True

    assert _run(_with_session(check))


def test_search_blender_rst_over_protocol(tmp_path):
    api = tmp_path / "api"
    manual = tmp_path / "manual" / "modeling"
    api.mkdir()
    manual.mkdir(parents=True)
    (api / "mesh.rst").write_text(
        "Mesh\n====\n\n.. module:: bpy.ops.mesh\n\n.. function:: bevel(offset=0.0)\n\n   Bevel selected edges.",
        encoding="utf-8",
    )
    (manual / "bevel.rst").write_text("Bevel Modifier\n==============\n\nBevel the mesh edges.", encoding="utf-8")

    async def check(session, init):
        assert "blender_api" in init.instructions
        tools = (await session.list_tools()).tools
        search_tool = next(tool for tool in tools if tool.name == "forge_search_docs")
        assert "blender_manual" in search_tool.input_schema["properties"]["source"]["enum"]
        for source, query, path in (
            ("all", "bpy.ops.mesh.bevel", "blender/api/mesh.rst"),
            ("blender_api", "bpy.ops.mesh.bevel", "blender/api/mesh.rst"),
            ("blender_manual", "bevel modifier", "blender/manual/modeling/bevel.rst"),
            ("mjcf", "condim", "body.md"),
        ):
            result = await session.call_tool("forge_search_docs", {"query": query, "source": source})
            assert not result.is_error
            hits = json.loads(_text(result))["hits"]
            assert any(hit["path"] == path for hit in hits)
            if source != "all":
                assert all(hit["source"] == source for hit in hits)
        bad = await session.call_tool("forge_search_docs", {"query": "bevel", "source": "invalid"})
        assert bad.is_error
        return True

    assert _run(_with_session(check, {"FORGE_BLENDER_DOCS_DIR": str(tmp_path)}))


def test_filter_readonly_keeps_read_only_tools():
    async def check(session, _init):
        tools = (await session.list_tools()).tools
        assert len(tools) == 8
        names = {tool.name for tool in tools}
        assert {"forge_mesh_check", "forge_select_by_tag", "forge_select_hulls"}.isdisjoint(names)
        return True

    assert _run(_with_session(check, {"FORGE_TOOLS": "readonly"}))


def test_filter_create_keeps_create_tools():
    async def check(session, _init):
        tools = (await session.list_tools()).tools
        # The 20 create tools are accompanied by forge_skill so the contract
        # remains discoverable whenever an operation category is enabled.
        assert len(tools) == 21
        assert sum(t.name.startswith("forge_create_") for t in tools) == 20
        assert "forge_skill" in {t.name for t in tools}
        return True

    assert _run(_with_session(check, {"FORGE_TOOLS": "create"}))


def test_filter_bogus_rejects_server_startup():
    async def check(session, _init):
        await session.list_tools()

    with pytest.raises(Exception):
        _run(_with_session(check, {"FORGE_TOOLS": "bogus"}))
