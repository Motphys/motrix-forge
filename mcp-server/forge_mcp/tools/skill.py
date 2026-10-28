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

"""Skill docs — serve the ``skills/*.md`` authoring guides on demand (see ``forge_mcp/skills.py``)."""

from __future__ import annotations

from mcp.server.mcpserver.exceptions import ToolError

from .. import mcp, skill_guides
from ..skills import mark_loaded
from ._hints import READ_ONLY

_GUIDE_INDEX = (
    ", ".join(f"`{name}`: {guide.summary or guide.title}" for name, guide in sorted(skill_guides.items()))
    or "none found"
)

_DESCRIPTION = (
    "Return a Forge MJCF authoring guide in full, or one section of it. "
    f"Available guides: {_GUIDE_INDEX}."
    ' Set `section` (e.g. `"joint"`) to return only that heading + body for a targeted lookup; '
    "omit it for the full guide."
)


@mcp.tool(name="forge_skill", description=_DESCRIPTION, annotations=READ_ONLY)
def skill(name: str, section: str | None = None) -> str:
    """Return a Forge MJCF authoring guide, optionally restricted to one section.

    With `section` set (e.g. ``"joint"``, ``"link"``, ``"sensor"``) only that
    section's heading + body is returned instead of the whole guide. Unknown or
    ambiguous skill / section names raise a ``ToolError`` listing the available
    names, and that text reaches the caller.
    """
    try:
        guide = skill_guides[name]
    except KeyError:
        available = ", ".join(f"`{n}`" for n in sorted(skill_guides))
        raise ToolError(f"unknown skill {name!r}; available: {available}") from None
    if section is None or not section.strip():
        content = guide.content
    else:
        # ``Skill.section`` reports unknown / ambiguous headings as ValueError,
        # which is the right contract for a text utility but is invisible over
        # MCP: the framework forwards ToolError verbatim and treats any other
        # exception as a crash detail, replacing it with a generic message.
        try:
            content = guide.section(section.strip())
        except ValueError as exc:
            raise ToolError(str(exc)) from None
    # A section read marks the whole guide as delivered, so a later soft hint
    # will not repeat it: serving one part is taken as awareness that the guide
    # exists, not as having read every rule in it.
    mark_loaded(name)
    return content
