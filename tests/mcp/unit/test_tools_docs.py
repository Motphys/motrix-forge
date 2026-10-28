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

"""Unit tests for the forge_search_docs tool wrapper (forge_mcp/tools/docs.py)."""

import pytest
from forge_mcp.tools.docs import search
from mcp.server.mcpserver.exceptions import ToolError


def test_search_returns_hits():
    out = search("condim", max_results=3)
    assert out["hits"]


def test_bad_max_results_surfaces_a_message():
    # ToolError rather than ValueError: only ToolError text reaches the client,
    # so "max_results must be positive" must not degrade to a generic error.
    with pytest.raises(ToolError, match="max_results must be positive"):
        search("condim", max_results=0)


def test_negative_context_surfaces_a_message():
    with pytest.raises(ToolError, match="context must be non-negative"):
        search("condim", context=-1)
