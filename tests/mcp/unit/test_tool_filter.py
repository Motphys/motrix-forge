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

"""Unit tests for FORGE_TOOLS filtering (forge_mcp/tools/__init__.py)."""

import os

import pytest
from forge_mcp.tools import apply_tool_filter
from mcp.server.mcpserver import MCPServer
from mcp.types import ToolAnnotations

READ_ONLY = ToolAnnotations(read_only_hint=True, destructive_hint=False)

# name -> is read-only, mirroring the real category split at small scale
_TOOLS: dict[str, bool] = {
    "forge_create_link": False,
    "forge_create_joint": False,
    "forge_define_model_type": False,
    "forge_define_parent": False,
    "forge_mark_instance_link": False,
    "forge_scene_info": True,
    "forge_measure": True,
    "forge_delete": False,
    "forge_search_docs": True,
    "forge_skill": True,
}


def _make_server() -> MCPServer:
    server = MCPServer("test-forge-filter")
    for name, read_only in _TOOLS.items():
        server.add_tool(lambda: "x", name=name, annotations=READ_ONLY if read_only else None)
    return server


def _names(server: MCPServer) -> list[str]:
    return sorted(server._tool_manager._tools)


def _apply(server: MCPServer, value: str) -> list[str]:
    os.environ["FORGE_TOOLS"] = value
    try:
        return apply_tool_filter(server)
    finally:
        os.environ.pop("FORGE_TOOLS", None)


def test_unset_keeps_all():
    server = _make_server()
    assert _apply(server, "") == []
    assert len(_names(server)) == len(_TOOLS)


def test_readonly_keeps_only_read_only():
    server = _make_server()
    _apply(server, "readonly")
    assert _names(server) == ["forge_measure", "forge_scene_info", "forge_search_docs", "forge_skill"]


def test_create_keeps_create_category():
    server = _make_server()
    _apply(server, "create")
    assert _names(server) == ["forge_create_joint", "forge_create_link"]


def test_modify_keeps_instance_link_marker():
    server = _make_server()
    _apply(server, "modify")
    assert _names(server) == ["forge_define_model_type", "forge_define_parent", "forge_mark_instance_link"]


def test_category_alias_search_keeps_docs():
    server = _make_server()
    _apply(server, "search")
    assert _names(server) == ["forge_search_docs"]


def test_substring_token():
    server = _make_server()
    _apply(server, "delete")
    assert _names(server) == ["forge_delete"]


def test_bogus_is_rejected_without_mutating_tools():
    server = _make_server()
    with pytest.raises(ValueError, match="matched no tools"):
        _apply(server, "bogus")
    assert len(_names(server)) == len(_TOOLS)


def test_contradictory_readonly_create_is_rejected_without_mutating_tools():
    server = _make_server()
    with pytest.raises(ValueError, match="matched no tools"):
        _apply(server, "readonly,create")
    assert len(_names(server)) == len(_TOOLS)
