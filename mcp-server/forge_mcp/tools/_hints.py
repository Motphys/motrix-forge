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

"""Shared ``ToolAnnotations`` presets for tool registration.

The MCP spec defaults ``destructive_hint`` to true, so read-only and plain
write tools must clear it explicitly.
"""

from __future__ import annotations

from mcp.types import ToolAnnotations

__all__ = ["DESTRUCTIVE", "READ_ONLY", "WRITE"]

READ_ONLY = ToolAnnotations(read_only_hint=True, destructive_hint=False)
WRITE = ToolAnnotations(destructive_hint=False)
DESTRUCTIVE = ToolAnnotations(destructive_hint=True)
