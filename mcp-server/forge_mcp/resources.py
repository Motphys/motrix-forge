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

"""Expose the MJCF element reference as MCP resources (alongside ``forge_search_docs``).

Each ``forge_mcp/docs/mjcf/*.md`` file becomes a static resource ``mjcf://<element>`` so
agents that prefer reading resources (e.g. Claude Code) can pull a whole
document directly instead of calling the search tool. ``forge_mcp/docs/mjcf/index.md``
maps to ``mjcf://index`` — the element hierarchy / path registry overview.
``forge_search_docs`` stays for keyword search.

Importing this module registers the resources on ``mcp``.
"""

from __future__ import annotations

from . import mcp
from .docs import load_doc_files


def _make_reader(text: str):
    """Return a zero-arg reader bound to *text* (static resource functions take no params)."""

    def _read() -> str:
        return text

    return _read


def _register() -> None:
    for element, text in load_doc_files().items():
        mcp.resource(
            f"mjcf://{element}",
            name=f"MJCF {element}",
            title=f"MJCF element reference — {element}",
            description=f"MJCF element reference: forge_mcp/docs/mjcf/{element}.md",
            mime_type="text/markdown",
        )(_make_reader(text))


_register()
