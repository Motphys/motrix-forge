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

"""Which authoring guide each dedicated tool asks for, pinned as a table.

`required_skills_for_code` reads the *generated* code, so a tool is gated
because its template happens to contain a Forge operator call or a `Forge_`
access — not because of what the tool is for, and not because of its name. For
the tools built by `op_call` that is structural: the helper emits
`bpy.ops.forge.<op>`, so `forge_create_*` gates as `create` and every other
operator as `modify`.

The rest gate (or don't) as a side effect of their template's shape, which is
how `forge_set_property` came to be gated through an unrelated `obj.data` branch
of the same loop rather than through the `Forge_` group it writes.
`EXPECTED_SKILLS` is the contract for those tools, and
`test_every_tool_is_accounted_for` fails when a tool is neither structurally
gated nor listed here — a new tool has to say which guide it needs.
"""

from __future__ import annotations

import ast
import asyncio
import importlib
import sys
from pathlib import Path

import forge_mcp.tools  # noqa: F401 — importing registers every tool on `mcp`
import pytest
from forge_mcp import mcp
from forge_mcp.blender import required_skills_for_code

# Tools that never reach the Blender bridge, so the gate cannot apply to them.
SERVER_SIDE = frozenset({"forge_search_docs", "forge_skill"})

# tool -> (args that build its code, the skills it must ask for).
# `forge_execute` is content-dependent: what is pinned here is the half this
# change is about — ordinary code with no Forge operation passes through.
EXPECTED_SKILLS: dict[str, tuple[tuple, tuple[str, ...]]] = {
    "forge_blendfile_summary": ((), ()),
    "forge_create_attach": (("C:/nonexistent/probe.xml",), ("create", "modify")),
    "forge_create_include": (("C:/nonexistent/probe.xml",), ("create", "modify")),
    "forge_delete": ((["LNK_X"],), ()),
    "forge_execute": (("result = {}",), ()),
    "forge_measure": ((["LNK_X"],), ()),
    "forge_object_info": (("LNK_X",), ()),
    "forge_rename": (({"LNK_X": "LNK_Y"},), ()),
    "forge_save_blendfile": (("C:/nonexistent/probe.blend",), ()),
    "forge_scene_config": (("g_option",), ()),
    "forge_scene_info": ((), ()),
    "forge_screenshot": ((), ()),
    "forge_set_property": (("LNK_X", {"damping": 0.1}), ("modify",)),
    "forge_set_scene_property": (("g_option", {"timestep": 0.002}), ("modify",)),
    "forge_set_shape_size": (("GEO_X", 0.5), ("modify",)),
    "forge_set_tendon_targets": (("TENDON_X", [{"target": "JOINT_X"}]), ("modify",)),
    "forge_set_transform": (("LNK_X", (1.0, 0.0, 0.0)), ()),
}


def _scan_tools() -> dict[str, tuple[str, str, bool]]:
    """Map every `@mcp.tool` name to (module, function, whether the gate is structural)."""
    tools_dir = Path(sys.modules["forge_mcp.tools"].__file__).parent
    scanned: dict[str, tuple[str, str, bool]] = {}
    for path in sorted(tools_dir.glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            names = [
                keyword.value.value
                for decorator in node.decorator_list
                if isinstance(decorator, ast.Call)
                for keyword in decorator.keywords
                if keyword.arg == "name" and isinstance(keyword.value, ast.Constant)
            ]
            if not names:
                continue
            # `op_call` emits `bpy.ops.forge.<op>` for its caller; a literal in
            # the template's own string is the same guarantee written out.
            structural = any(
                getattr(call.func, "id", None) == "op_call" for call in ast.walk(node) if isinstance(call, ast.Call)
            ) or any(
                isinstance(constant, ast.Constant)
                and isinstance(constant.value, str)
                and "bpy.ops.forge." in constant.value
                for constant in ast.walk(node)
            )
            for name in names:
                scanned[name] = (path.stem, node.name, structural)
    return scanned


def _generated_code(tool: str, args: tuple) -> str:
    """Run a tool with the bridge stubbed out; return the code it built."""
    module_name, func_name, _ = _scan_tools()[tool]
    module = importlib.import_module(f"forge_mcp.tools.{module_name}")
    seen: dict[str, str] = {}

    def _stub(code, **_kwargs):
        seen.setdefault("code", code)
        # `forge_screenshot` decodes this out of the response; every other tool
        # just hands the dict back.
        return {"image_base64": ""}

    original = module.call_blender
    module.call_blender = _stub
    try:
        getattr(module, func_name)(*args)
    finally:
        module.call_blender = original
    return seen["code"]


def test_the_scan_sees_every_registered_tool():
    """A tool registered some other way would slip past the table unnoticed."""
    registered = {tool.name for tool in asyncio.run(mcp.list_tools())}
    assert registered == set(_scan_tools()), (
        f"registry and source scan disagree; registered only={sorted(registered - set(_scan_tools()))}, "
        f"scanned only={sorted(set(_scan_tools()) - registered)}"
    )


def test_every_tool_is_accounted_for():
    """Each tool is either structurally gated, server-side, or named in the table."""
    unaccounted = sorted(
        name
        for name, (_, _, structural) in _scan_tools().items()
        if not structural and name not in EXPECTED_SKILLS and name not in SERVER_SIDE
    )
    assert not unaccounted, (
        f"{unaccounted} drive Blender without a structural gate, so which guide they ask for is an accident of "
        f"their template. Add each to EXPECTED_SKILLS (or SERVER_SIDE if it never reaches the bridge)."
    )

    stale = sorted(set(EXPECTED_SKILLS) - set(_scan_tools()))
    assert not stale, f"EXPECTED_SKILLS names tools that no longer exist: {stale}"


@pytest.mark.parametrize("tool", sorted(EXPECTED_SKILLS))
def test_tool_asks_for_the_expected_guides(tool):
    args, expected = EXPECTED_SKILLS[tool]
    assert required_skills_for_code(_generated_code(tool, args)) == expected
