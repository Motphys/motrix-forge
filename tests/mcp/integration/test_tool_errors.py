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

"""Every tool's error must reach the client carrying its own message.

The MCP framework forwards ``ToolError`` text verbatim but replaces every other
exception with a generic ``Error executing tool <name>`` — so a tool that lets a
``ValueError`` escape silently loses the reason it failed. Blender-backed tools
are safe by construction (``call_blender`` converts bridge and transport
failures into ``ToolError``), so only tools that finish *without* a Blender
round-trip need an error case of their own.

``test_every_registered_tool_is_classified`` scans the tool sources and fails
when an in-process tool appears that has no case in ``SERVER_SIDE_CASES``, so a
new tool cannot quietly reintroduce the gap.
``test_server_side_tool_errors_reach_the_client`` then proves each case really
delivers its message over the wire.

Note the boundary: the source scan covers tool function bodies. A helper that a
Blender-backed tool calls *before* reaching the bridge is out of its reach — the
dynamic cases are the guarantee for behavior, the scan is the tripwire for new
tools.
"""

from __future__ import annotations

import ast
import asyncio
import os
import sys
from dataclasses import dataclass
from pathlib import Path

import forge_mcp.tools  # noqa: F401 — importing registers every tool on `mcp`
from forge_mcp import mcp
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_DIR = Path(__file__).resolve().parents[3] / "mcp-server"

# Tools that complete without a Blender round-trip: {tool: (invalid args, fragment
# of the message the caller must receive)}. Anything here must fail with its own
# wording rather than the framework's generic wrapper.
SERVER_SIDE_CASES: dict[str, tuple[dict, str]] = {
    "forge_skill": ({"name": "nope"}, "unknown skill 'nope'"),
    "forge_search_docs": ({"query": "condim", "max_results": 0}, "max_results must be positive"),
}


@dataclass(frozen=True)
class _ToolSource:
    """Where a tool is defined, and how it can fail in this process."""

    file: str
    calls_blender: bool
    bare_raises: tuple[str, ...]


def _decorated_tool_name(decorator: ast.AST, default: str) -> str | None:
    """Return the tool name an ``@mcp.tool(...)`` decorator declares, else None.

    ``name`` is optional in the SDK and defaults to the decorated function's
    name, so *default* keeps that form from being skipped by the scan.
    """
    if not isinstance(decorator, ast.Call):
        return None
    func = decorator.func
    if not (isinstance(func, ast.Attribute) and func.attr == "tool"):
        return None
    for keyword in decorator.keywords:
        if keyword.arg == "name" and isinstance(keyword.value, ast.Constant):
            return str(keyword.value.value)
    return default


def _raise_target(node: ast.Raise) -> str | None:
    """Dotted name of the exception a ``raise`` builds, when it is statically known."""
    exc = node.exc
    if exc is None:  # bare ``raise`` re-raises whatever is in flight
        return None
    target = exc.func if isinstance(exc, ast.Call) else exc
    try:
        return ast.unparse(target)
    except Exception:  # noqa: BLE001 — unparse is best-effort, not a hard requirement
        return None


def _scan_tool_sources() -> dict[str, _ToolSource]:
    """Map every ``@mcp.tool`` function in the source to its failure surface."""
    tools_dir = Path(sys.modules["forge_mcp.tools"].__file__).parent
    scanned: dict[str, _ToolSource] = {}
    for path in sorted(tools_dir.glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            names = [n for n in (_decorated_tool_name(d, node.name) for d in node.decorator_list) if n]
            if not names:
                continue
            # Only a call counts; ``call_blender`` inside a code-string template
            # is emitted into Blender, where the bridge forwards the exception.
            calls_blender = any(
                isinstance(child, ast.Call) and isinstance(child.func, ast.Name) and child.func.id == "call_blender"
                for child in ast.walk(node)
            )
            bare = tuple(
                target
                for target in (_raise_target(child) for child in ast.walk(node) if isinstance(child, ast.Raise))
                if target and target.rsplit(".", 1)[-1] != "ToolError"
            )
            for name in names:
                scanned[name] = _ToolSource(path.name, calls_blender, bare)
    return scanned


def _registered_tool_names() -> set[str]:
    return {tool.name for tool in asyncio.run(mcp.list_tools())}


def test_every_registered_tool_is_classified():
    """A tool must either route through the bridge, or declare an error case."""
    registered = _registered_tool_names()
    scanned = _scan_tool_sources()

    assert registered == set(scanned), (
        f"tool registry and source scan disagree; "
        f"registered only={sorted(registered - set(scanned))}, scanned only={sorted(set(scanned) - registered)}"
    )

    unclassified = sorted(
        name for name, source in scanned.items() if not source.calls_blender and name not in SERVER_SIDE_CASES
    )
    assert not unclassified, (
        f"{unclassified} do not call call_blender, so their exceptions stay in the server and reach the "
        f"client as a generic 'Error executing tool <name>'. Add a case to SERVER_SIDE_CASES."
    )

    stale = sorted(set(SERVER_SIDE_CASES) - registered)
    assert not stale, f"SERVER_SIDE_CASES names tools that no longer exist: {stale}"


def test_no_tool_raises_a_bare_exception():
    """In a tool body, only ToolError survives the trip to the client."""
    offenders = {name: list(source.bare_raises) for name, source in _scan_tool_sources().items() if source.bare_raises}
    assert not offenders, (
        f"these tools raise a non-ToolError exception, whose text the framework replaces with a generic "
        f"message; raise ToolError(str(exc)) instead: {offenders}"
    )


def test_server_side_tool_errors_reach_the_client():
    """Each in-process tool delivers its own message, not the framework's wrapper."""
    params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "forge_mcp"],
        cwd=str(SERVER_DIR),
        env={**os.environ},
    )

    async def check() -> list[str]:
        problems: list[str] = []
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                for tool, (args, fragment) in sorted(SERVER_SIDE_CASES.items()):
                    result = await session.call_tool(tool, args)
                    text = result.content[0].text if result.content else ""
                    if not result.is_error:
                        problems.append(f"{tool}: expected the call to fail, got {text!r}")
                    elif fragment not in text:
                        problems.append(f"{tool}: {text!r} does not contain {fragment!r}")
        return problems

    problems = asyncio.run(check())
    assert not problems, "\n".join(problems)
