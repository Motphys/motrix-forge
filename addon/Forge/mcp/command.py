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

"""
CLI command handler for running the MCP server in background mode.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

import bpy

from ..settings import get_addon_prefs
from .constants import DEFAULT_HOST, DEFAULT_PORT
from .runner import check_online_state, exec_blocking
from .utils import get_server


def cli_exec(argv: list[str]) -> int:
    """Block and serve MCP requests until interrupted."""

    parser = argparse.ArgumentParser(
        prog="forge_mcp",
        description=(
            """Start the MCP server. Long-running Forge I/O runs synchronously in background mode;
            each request completes before returning."""
        ),
    )
    parser.add_argument(
        "--host",
        default=DEFAULT_HOST,
        help="Host to bind the TCP server (default: localhost).",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=DEFAULT_PORT,
        help="Port to bind the TCP server (default: 9876).",
    )
    parser.add_argument(
        "--blend-file",
        default=None,
        help="Path to .blend file to load before starting.",
    )
    parser.add_argument(
        "--token",
        default=os.environ.get("FORGE_MCP_TOKEN", ""),
        help="Shared authentication token (default: FORGE_MCP_TOKEN).",
    )

    args = parser.parse_args(argv)

    mcp_server = get_server()
    if mcp_server is None:
        print("Error: MCP server not registered")
        return 1

    if args.blend_file:
        blend_file = Path(args.blend_file).expanduser()
        if not blend_file.is_file():
            print(f"Error: blend file does not exist: {blend_file}")
            return 1
        try:
            bpy.ops.wm.open_mainfile(filepath=str(blend_file.resolve()))
        except Exception as ex:  # pylint: disable=broad-exception-caught
            print(f"Error: failed to load blend file: {str(ex):s}")
            return 1

    try:
        mcp_server.start(host=args.host, port=args.port, token=args.token)
    except Exception as ex:  # pylint: disable=broad-exception-caught
        print(f"Error: {str(ex):s}")
        return 1

    print(f"MCP server started on {args.host}:{args.port:d}, press Ctrl+C to exit.")

    try:
        exec_blocking()
    finally:
        mcp_server.stop()
    return 0


def cli_exec_handler(argv: list[str]) -> int:
    """Callback for the CLI: ``blender -c forge_mcp``."""

    prefs = get_addon_prefs()
    if not check_online_state(prefs):
        return 1

    return cli_exec(argv)
