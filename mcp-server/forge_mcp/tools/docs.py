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

"""Docs search over the local MJCF reference and Blender API/manual."""

from __future__ import annotations

from mcp.server.mcpserver.exceptions import ToolError

from .. import doc_paragraphs, mcp
from ..docs import DocSource, search_docs
from ._hints import READ_ONLY


@mcp.tool(annotations=READ_ONLY, name="forge_search_docs")
def search(query: str, max_results: int = 10, context: int = 0, source: DocSource = "all") -> dict:
    """Search local MJCF Markdown and Blender RST documentation without connecting to Blender.

    Set source to all (default), mjcf, blender, blender_api, or blender_manual.
    Blender queries can use API names (bpy.ops.mesh.bevel, bpy.types.Object.location)
    or manual keywords (bevel modifier).

    Returns ranked hits with `path` (relative file), `source`, `breadcrumb` (section path like
    `body > body/joint > Attributes`), `text` (matching paragraph or
    attribute-table row) and `score`. All query tokens must match; when none do,
    best single-token matches are returned with `matched: "any"`. Use `context`
    to widen each hit by N neighboring rows/paragraphs.
    """
    # ``search_docs`` reports bad arguments as ValueError, which is the right
    # contract for the search utility but is invisible over MCP: the framework
    # forwards ToolError verbatim and treats any other exception as a crash
    # detail, replacing it with a generic message.
    try:
        return search_docs(doc_paragraphs, query, max_results=max_results, context=context, source=source)
    except ValueError as exc:
        raise ToolError(str(exc)) from None
