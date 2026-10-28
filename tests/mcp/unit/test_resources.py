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

"""Unit tests for the mjcf:// resource registration (forge_mcp/resources.py)."""

import asyncio

import forge_mcp.resources  # noqa: F401 — importing registers the resources
from forge_mcp import mcp


def _read_text(uri: str) -> tuple[str, str]:
    async def _go():
        items = list(await mcp.read_resource(uri))
        return items[0]

    item = asyncio.run(_go())
    content = item.content.decode("utf-8") if isinstance(item.content, bytes) else item.content
    return content, item.mime_type


def test_all_docs_registered():
    uris = set(mcp._resource_manager._resources)
    assert len(uris) == 16
    assert "mjcf://index" in uris
    assert "mjcf://body" in uris


def test_read_body_returns_markdown():
    text, mime = _read_text("mjcf://body")
    assert text.startswith("# body")
    assert mime == "text/markdown"


def test_read_index_returns_overview():
    text, _ = _read_text("mjcf://index")
    assert text.startswith("# MJCF XML Reference")
