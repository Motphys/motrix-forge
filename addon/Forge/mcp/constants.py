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
Shared constants and utilities for the MCP bridge sub-system.
"""

import json
import socket as _sock
import sys
from collections.abc import Callable
from typing import NamedTuple

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 9876

# Interval of main-thread timer ticks while actively processing requests.
TIMER_ACTIVE_INTERVAL = 0.05
# Interval of main-thread timer ticks while idle (no pending work).
TIMER_IDLE_INTERVAL = 1.0
# Delay interval of inactivity before switching to the idle interval.
TIMER_IDLE_DELAY_INTERVAL = 5.0

MAX_REQUEST_BYTES = 10 * 1024 * 1024  # 10 MiB.
# Keep the interactive bridge bounded when a local client misbehaves.
MAX_CLIENTS = 32
# Captured tool output is mirrored to Blender's console but capped in memory.
MAX_CAPTURED_OUTPUT_BYTES = 1024 * 1024
LISTEN_BACKLOG = 5
RECV_BUFFER_SIZE = 8192
# Time before a client that has not sent a complete request is evicted.
CLIENT_TIMEOUT = 10.0
# How often ``poll_blocking`` checks for shutdown.
POLL_BLOCKING_TIMEOUT = 1.0

# Time budget for a single blocking ``sendall`` (background mode). Screenshots
# and tool output can approach the one-MiB capture limit, so a short budget
# would truncate healthy responses; this only guards against a peer that stops
# reading, which stalls the caller for the whole budget.
SEND_TIMEOUT = 30.0

# Time budget for one queued incremental response (interactive mode): how long a
# non-blocking connection may sit in the response queue before it is dropped.
# Kept separate from SEND_TIMEOUT because the two bound different things — a
# stalled blocking send stalls the caller, a stalled queued send only holds one
# of the MAX_CLIENTS connection slots.
QUEUE_SEND_TIMEOUT = 30.0

# Total wall-time in seconds before a deferred operation is considered timed out.
# Half hour is long for interactive use, but renders can take a while.
DEFERRED_TIMEOUT = 60.0 * 30.0

DEFERRED_UNSUPPORTED_MESSAGE = """The deferred operation did not complete synchronously in background mode.
Use the interactive add-on server for work that requires event-loop polling."""

# ── Shared data types ──────────────────────────────────────────────


class ExecResult(NamedTuple):
    """Result of executing tool-code."""

    response: dict[str, object]
    check_fn: Callable[[], dict[str, object] | None] | None = None
    cancel_fn: Callable[[], object] | None = None


# ── Shared helpers ─────────────────────────────────────────────────


def encode_response(response: dict[str, object]) -> bytes:
    """Serialize a response dict as null-byte-delimited JSON bytes."""
    return (json.dumps(response) + "\0").encode("utf-8")


def send_response(connection: _sock.socket, response: dict[str, object]) -> bool:
    """Send a response synchronously for the background-mode bridge."""
    try:
        connection.setblocking(True)
        connection.settimeout(SEND_TIMEOUT)
        connection.sendall(encode_response(response))
        return True
    except (OSError, TypeError, ValueError) as exc:
        print(f"Forge MCP response send failed: {exc}", file=sys.stderr)
        return False


def send_error(connection: _sock.socket, message: str) -> bool:
    """Send an error response and report whether delivery succeeded."""
    return send_response(connection, {"status": "error", "message": message})
