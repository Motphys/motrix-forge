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

"""Unit tests for the forge_skill tool function (forge_mcp/tools/skill.py)."""

import importlib

import pytest
from forge_mcp.tools.skill import skill
from mcp.server.mcpserver.exceptions import ToolError

skills_module = importlib.import_module("forge_mcp.skills")


def test_full_guide():
    out = skill("create")
    assert out.startswith("# Forge create")


def test_section():
    out = skill("create", section="joint")
    assert out.splitlines()[0].strip() == "#### `joint`:"


def test_section_none_returns_full():
    assert skill("create", section=None) == skill("create")


def test_unknown_skill_names_the_available_guides():
    # ToolError rather than ValueError: only ToolError text reaches the client,
    # so the "available: ..." hint must not be lost to a generic tool error.
    with pytest.raises(ToolError, match=r"unknown skill 'nope'"):
        skill("nope")


def test_unknown_section_lists_available():
    with pytest.raises(ToolError, match="available"):
        skill("create", section="bogus")


def test_invalid_section_does_not_mark_guide_loaded(monkeypatch):
    monkeypatch.setattr(skills_module, "_loaded_rules", set())

    with pytest.raises(ToolError, match="available"):
        skill("create", section="bogus")

    assert "create" not in skills_module.rules_loaded()
