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

"""Client-side MCP server exposing Forge (Blender MJCF addon) tools.

Tools run in Blender through the TCP bridge implemented in
:mod:`forge_mcp.blender`; tool definitions live in :mod:`forge_mcp.tools`.
The ``forge_mcp/skills/*.md`` authoring guides, ``forge_mcp/docs/mjcf/*.md``
element reference and ``forge_mcp/docs/blender/**/*.rst`` API/manual
are loaded at startup: guides are indexed in the server instructions and
served in full by the ``forge_skill`` tool, the reference is searchable via
``forge_search_docs``.
"""

from __future__ import annotations

from mcp.server.mcpserver import MCPServer

from .blender import call_blender
from .docs import Paragraph, load_docs
from .skills import Skill, build_instructions, guides_loaded

__all__ = ["Paragraph", "Skill", "call_blender", "doc_paragraphs", "mcp", "skill_guides"]

# Loaded once at import. These deliberately do not reuse the submodule names
# ``skills`` and ``docs``: binding those here would shadow ``forge_mcp.skills``
# and ``forge_mcp.docs``, so ``from forge_mcp import skills`` would hand back a
# dict where any reader expects the module.
doc_paragraphs = load_docs()
skill_guides = guides_loaded()
mcp = MCPServer("forge-mcp", instructions=build_instructions(skill_guides, has_docs=bool(doc_paragraphs)))
