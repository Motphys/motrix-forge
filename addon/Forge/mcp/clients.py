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
Deferred response handling for long-running Blender background jobs.
"""

import socket as sock
import time
from collections.abc import Callable

from .constants import CLIENT_TIMEOUT, DEFERRED_TIMEOUT, QUEUE_SEND_TIMEOUT, encode_response

__all__ = (
    "Client",
    "DeferredClient",
    "PendingResponse",
)


class Client:
    """Per-connection state for a client (the MCP server process) that has not yet sent a complete request."""

    __slots__ = (
        "connection",
        "buffer",
        "deadline",
    )

    def __init__(self, connection: sock.socket) -> None:
        """Initialize the client with the given connection."""
        self.connection = connection
        # Accumulates data until the null-byte delimiter is received.
        self.buffer = bytearray()
        # Wall-clock deadline after which this client is evicted.
        self.deadline = time.monotonic() + CLIENT_TIMEOUT


class DeferredClient:
    """A client connection waiting for a background job to complete."""

    __slots__ = (
        "connection",
        "check_fn",
        "strict_json",
        "stdout",
        "stderr",
        "deadline",
        "cancel_fn",
    )

    def __init__(
        self,
        connection: sock.socket,
        check_fn: Callable[[], dict[str, object] | None],
        strict_json: bool,
        stdout: str,
        stderr: str,
        cancel_fn: Callable[[], object] | None = None,
    ) -> None:
        """Initialize the deferred client with connection and polling callback."""
        self.connection = connection
        self.check_fn = check_fn
        self.strict_json = strict_json
        self.stdout = stdout
        self.stderr = stderr
        self.cancel_fn = cancel_fn
        self.deadline = time.monotonic() + DEFERRED_TIMEOUT


class PendingResponse:
    """A response being written incrementally to a non-blocking client."""

    __slots__ = (
        "connection",
        "data",
        "offset",
        "deadline",
    )

    def __init__(self, connection: sock.socket, response: dict[str, object]) -> None:
        """Encode *response* and initialize its bounded send state."""
        self.connection = connection
        self.data = encode_response(response)
        self.offset = 0
        self.deadline = time.monotonic() + QUEUE_SEND_TIMEOUT
