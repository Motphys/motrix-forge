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
Deferred response management for long-running Blender background jobs.

A "deferred" request is one where the executed code sets
``check_is_finished`` in its namespace, allowing the server to
periodically poll for completion without blocking the event loop.
"""

from __future__ import annotations

import json
import socket as _sock
import time
import traceback
from collections.abc import Callable

from .clients import DeferredClient
from .constants import DEFERRED_TIMEOUT, send_response
from .guardian import Guardian


class DeferredManager:
    """
    Tracks and polls deferred client connections.

    Each deferred client has a ``check_fn`` that is called periodically
    until it returns a non-``None`` dict (success), the client
    disconnects, or the wall-clock deadline is exceeded.
    """

    __slots__ = ("clients",)

    def __init__(self) -> None:
        """Initialize the deferred manager with an empty client list."""
        self.clients: list[DeferredClient] = []

    # ── Public API ─────────────────────────────────────────────────

    def gather(
        self,
        connection: _sock.socket,
        check_fn: Callable[[], dict[str, object] | None],
        strict_json: bool,
        stdout: str,
        stderr: str,
        cancel_fn: Callable[[], object] | None = None,
    ) -> None:
        """Register a new deferred client."""
        self.clients.append(DeferredClient(connection, check_fn, strict_json, stdout, stderr, cancel_fn))

    @staticmethod
    def resolve_once(
        check_fn: Callable[[], dict[str, object] | None],
        strict_json: bool,
        stdout: str = "",
        stderr: str = "",
    ) -> dict[str, object] | None:
        """Evaluate one deferred callback and format a completed response."""
        try:
            with Guardian():
                result = check_fn()
        except BaseException:  # Deferred callbacks are supplied by tool code.
            return {"status": "error", "message": traceback.format_exc()}

        if result is None:
            return None
        if not isinstance(result, dict):
            return {
                "status": "error",
                "message": f"check_is_finished must return None or dict, not {type(result).__name__}",
            }

        if strict_json:
            try:
                json.dumps(result)
            except (TypeError, ValueError) as ex:
                return {"status": "error", "message": f"Deferred result is not JSON-serializable: {str(ex)}"}
        else:
            result = json.loads(json.dumps(result, default=repr))

        response: dict[str, object] = {"status": "ok", "result": result}
        if stdout:
            response["stdout"] = stdout
        if stderr:
            response["stderr"] = stderr
        return response

    def poll(
        self,
        response_sender: Callable[[_sock.socket, dict[str, object]], object] | None = None,
    ) -> bool:
        """
        Check all deferred clients for completion.

        ``response_sender`` can take ownership of completed connections, which
        lets the interactive server write responses over multiple timer ticks.
        Without it, responses are sent synchronously for backwards-compatible
        standalone use.

        Returns ``True`` if at least one client was resolved or removed.
        """
        work_state = False
        for dc in self.clients[:]:
            if self._is_disconnected(dc.connection):
                self._cancel(dc)
                self._remove(dc)
                work_state = True
                continue

            if time.monotonic() > dc.deadline:
                self._cancel(dc)
                self._finish(
                    dc,
                    {
                        "status": "error",
                        "message": f"Deferred operation timed out after {DEFERRED_TIMEOUT:.0f} seconds",
                    },
                    response_sender,
                )
                work_state = True
                continue

            response = self.resolve_once(dc.check_fn, dc.strict_json, dc.stdout, dc.stderr)
            if response is None:
                continue
            # A polling/check callback can fail before it gets a chance to
            # release the modal operation.  Cancel it before dropping the
            # client, otherwise Forge remains stuck in an active operation.
            if response.get("status") == "error":
                self._cancel(dc)
            self._finish(dc, response, response_sender)
            work_state = True

        return work_state

    def close_all(self) -> None:
        """Close all deferred connections without sending responses."""
        for dc in self.clients:
            self._cancel(dc)
            try:
                dc.connection.close()
            except OSError:
                pass
        self.clients.clear()

    def pending(self) -> bool:
        """Return ``True`` if there are deferred clients awaiting completion."""
        return bool(self.clients)

    # ── Internals ──────────────────────────────────────────────────

    @staticmethod
    def _is_disconnected(connection: _sock.socket) -> bool:
        """Return ``True`` if the remote end has closed the connection."""
        try:
            data = connection.recv(1, _sock.MSG_PEEK)
            return len(data) == 0
        except BlockingIOError:
            return False
        except OSError:
            return True

    def _remove(self, dc: DeferredClient) -> None:
        """Close a deferred connection and remove it from the list."""
        try:
            dc.connection.close()
        except OSError:
            pass
        try:
            self.clients.remove(dc)
        except ValueError:
            pass

    @staticmethod
    def _cancel(dc: DeferredClient) -> None:
        """Request cancellation of the underlying operation, when supported."""
        if dc.cancel_fn is None:
            return
        try:
            with Guardian():
                dc.cancel_fn()
        except BaseException:
            pass

    def _send_and_close(self, dc: DeferredClient, response: dict[str, object]) -> None:
        """Send the final response and remove the deferred client."""
        try:
            send_response(dc.connection, response)
        finally:
            self._remove(dc)

    def _finish(
        self,
        dc: DeferredClient,
        response: dict[str, object],
        response_sender: Callable[[_sock.socket, dict[str, object]], object] | None,
    ) -> None:
        """Send synchronously or transfer the connection to a response writer."""
        if response_sender is None:
            self._send_and_close(dc, response)
            return

        try:
            self.clients.remove(dc)
        except ValueError:
            return
        try:
            response_sender(dc.connection, response)
        except BaseException:
            try:
                dc.connection.close()
            except OSError:
                pass
            raise
