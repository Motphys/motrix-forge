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
TCP socket bridge that receives MCP tool requests and dispatches them
to the Blender Python environment for execution.

Two operating modes:
  * **Interactive** (``poll``) — non-blocking timer-based loop for GUI sessions.
  * **Background** (``poll_blocking``) — blocking ``select``-based loop for
    ``blender --background`` CLI mode.
"""

from __future__ import annotations

import ipaddress
import json
import math
import select
import socket as _sock
import sys
import time

from .clients import Client, PendingResponse
from .constants import (
    CLIENT_TIMEOUT,
    DEFAULT_HOST,
    DEFAULT_PORT,
    DEFERRED_UNSUPPORTED_MESSAGE,
    LISTEN_BACKLOG,
    MAX_CLIENTS,
    MAX_REQUEST_BYTES,
    POLL_BLOCKING_TIMEOUT,
    RECV_BUFFER_SIZE,
    TIMER_ACTIVE_INTERVAL,
    TIMER_IDLE_DELAY_INTERVAL,
    TIMER_IDLE_INTERVAL,
    ExecResult,
    send_error,
    send_response,
)
from .deferred import DeferredManager
from .executor import CodeExecutor
from .guardian import Guardian


class TimerState:
    """Tracks the poll-interval state machine for the interactive timer.

    While there is work (pending clients, a response still draining, or a
    deferred operation that just finished) the timer fires at *active_interval*;
    after *idle_delay* seconds without work it drops to *idle_interval* to
    conserve CPU. A deferred operation that is still running is deliberately not
    work: its completion check keeps running on the idle interval so a long
    import or export does not hold the main thread at the active interval.
    """

    __slots__ = (
        "active_interval",
        "idle_interval",
        "idle_delay_interval",
        "idle_countdown_to_reset",
        "idle_countdown",
    )

    def __init__(self) -> None:
        """Initialize the timer state with default interval values."""
        self.active_interval: float = TIMER_ACTIVE_INTERVAL
        self.idle_interval: float = TIMER_IDLE_INTERVAL
        self.idle_delay_interval: float = TIMER_IDLE_DELAY_INTERVAL
        self.idle_countdown_to_reset: int = 0
        self.idle_countdown: int = 0

    def internal_timer_update(
        self,
        active: float | None = None,
        idle: float | None = None,
        idle_delay: float | None = None,
    ):
        """Update the timer intervals and recalculate the idle countdown."""
        if active is not None:
            self.active_interval = active
        if idle is not None:
            self.idle_interval = idle
        if idle_delay is not None:
            self.idle_delay_interval = idle_delay
        self.idle_countdown_to_reset = math.ceil(self.idle_delay_interval / self.active_interval)
        self.idle_countdown = self.idle_countdown_to_reset

    def timer_idle_reset(self):
        """Reset the idle countdown to its initial value."""
        self.idle_countdown = self.idle_countdown_to_reset

    def timer_idle_interval(self) -> float:
        """Return ``active_interval`` during the countdown, then ``idle_interval``.

        Returns:
            The active or idle interval value in seconds.
        """
        if self.idle_countdown > 0:
            self.idle_countdown -= 1
            return self.active_interval
        return self.idle_interval


class State:
    """Runtime state of the listening socket and active (non-deferred) clients."""

    __slots__ = (
        "socket",
        "clients",
        "responses",
    )

    def __init__(self) -> None:
        """Initialize the server state with no active socket."""
        self.socket: _sock.socket | None = None
        self.clients: list[Client] = []
        self.responses: list[PendingResponse] = []


class MCPServer:
    """
    Blender-side MCP bridge server.

    Owns the TCP listening socket, accepts client connections, reads
    null-byte-delimited JSON requests, executes the contained Python
    code via :class:`CodeExecutor`, and sends back JSON responses.
    """

    __slots__ = (
        "host",
        "port",
        "timer_state",
        "state",
        "executor",
        "deferred",
        "logging",
        "token",
    )

    def __init__(self, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT, token: str = "") -> None:
        """Initialize the MCP server with host and port."""
        self.host = host
        self.port = port
        self.timer_state = TimerState()
        self.state = State()
        self.executor = CodeExecutor()
        self.deferred = DeferredManager()
        self.logging: bool = False
        self.token = token

    # ── Lifecycle ──────────────────────────────────────────────────

    def is_running(self) -> bool:
        """Return whether the server is currently listening.

        Returns:
            True if the server socket is bound and listening.
        """
        return self.state.socket is not None

    @staticmethod
    def _is_loopback_host(host: str) -> bool:
        """Return whether *host* is an explicit loopback address/name."""
        if host.casefold() == "localhost":
            return True
        try:
            return ipaddress.ip_address(host).is_loopback
        except ValueError:
            return False

    def start(self, host: str | None = None, port: int | None = None, token: str | None = None) -> None:
        """Bind the listening socket and begin accepting connections."""
        if self.is_running():
            raise RuntimeError("Server is already running")

        self.host = host if host is not None else self.host
        self.port = port if port is not None else self.port
        self.token = token if token is not None else self.token

        if not self._is_loopback_host(self.host) and not self.token:
            raise ValueError("An authentication token is required when binding MCP to a non-loopback host")

        listener = _sock.socket(_sock.AF_INET, _sock.SOCK_STREAM)
        try:
            if sys.platform == "win32":
                # Windows SO_REUSEADDR lets multiple Blender instances bind
                # the same bridge port, making client routing unpredictable.
                listener.setsockopt(_sock.SOL_SOCKET, _sock.SO_EXCLUSIVEADDRUSE, 1)
            else:
                listener.setsockopt(_sock.SOL_SOCKET, _sock.SO_REUSEADDR, 1)
            listener.setblocking(False)
            listener.bind((self.host, self.port))
            listener.listen(LISTEN_BACKLOG)
            self.state.socket = listener
            print(f"BlenderMCP server started on {self.host}:{self.port}")
        except OSError:
            listener.close()
            self.state.socket = None
            raise

    def stop(self) -> None:
        """Close the listening socket, all client connections, and deferred responses."""
        if self.state.socket is not None:
            try:
                self.state.socket.close()
            except Exception:
                pass
            self.state.socket = None

        for client in self.state.clients:
            try:
                client.connection.close()
            except Exception:
                pass
        self.state.clients.clear()

        for response in self.state.responses:
            try:
                response.connection.close()
            except Exception:
                pass
        self.state.responses.clear()

        self.deferred.close_all()
        print("BlenderMCP server stopped")

    # ── Client I/O (interactive, non-blocking) ─────────────────────

    def _gather_clients(self):
        """Accept pending connections on the listening socket."""
        if self.state.socket is None:
            return
        while True:
            try:
                connection, _addr = self.state.socket.accept()
                connection.setblocking(False)
                connection_count = len(self.state.clients) + len(self.deferred.clients) + len(self.state.responses)
                if connection_count >= MAX_CLIENTS:
                    # Keep at most one best-effort rejection response beyond
                    # the normal client bound. Further arrivals are closed so
                    # stalled readers cannot grow this queue without limit.
                    if connection_count == MAX_CLIENTS:
                        self._queue_response(
                            connection,
                            {"status": "error", "message": f"Server client limit ({MAX_CLIENTS}) reached"},
                        )
                    else:
                        connection.close()
                    continue
                self.state.clients.append(Client(connection))
            except BlockingIOError:
                break
            except OSError:
                break

    def _close_client(self, client: Client) -> None:
        """Close a client connection and remove it from the active list."""
        try:
            client.connection.close()
        except Exception:
            pass
        try:
            self.state.clients.remove(client)
        except ValueError:
            pass

    def _queue_response(self, connection: _sock.socket, response: dict[str, object]) -> None:
        """Transfer a connection to the non-blocking response queue."""
        try:
            connection.setblocking(False)
            self.state.responses.append(PendingResponse(connection, response))
        except (OSError, TypeError, ValueError) as exc:
            print(f"Forge MCP response queue failed: {exc}", file=sys.stderr)
            try:
                connection.close()
            except OSError:
                pass

    def _queue_client_response(self, client: Client, response: dict[str, object]) -> None:
        """Remove an input client and queue its final response."""
        try:
            self.state.clients.remove(client)
        except ValueError:
            return
        self._queue_response(client.connection, response)

    def _flush_responses(self) -> bool:
        """Advance each non-blocking response by at most one send call."""
        work_state = False
        for pending in self.state.responses[:]:
            if time.monotonic() > pending.deadline:
                print("Forge MCP response send timed out", file=sys.stderr)
                self._close_response(pending)
                work_state = True
                continue
            try:
                sent = pending.connection.send(pending.data[pending.offset :])
            except BlockingIOError:
                continue
            except OSError as exc:
                print(f"Forge MCP response send failed: {exc}", file=sys.stderr)
                self._close_response(pending)
                work_state = True
                continue
            if sent <= 0:
                print("Forge MCP response send failed: connection closed", file=sys.stderr)
                self._close_response(pending)
                work_state = True
                continue
            pending.offset += sent
            work_state = True
            if pending.offset >= len(pending.data):
                self._close_response(pending)
        return work_state

    def _close_response(self, pending: PendingResponse) -> None:
        """Close and discard a queued response."""
        try:
            pending.connection.close()
        except OSError:
            pass
        try:
            self.state.responses.remove(pending)
        except ValueError:
            pass

    @staticmethod
    def _extract_request_data(buf: bytearray) -> bytes | None:
        """If *buf* contains a null byte, extract and return the data before it.

        The extracted bytes (including the delimiter) are removed from *buf*.
        The server enforces one request per connection and rejects trailing data.

        Returns:
            The extracted request bytes, or None if no complete request is available.
        """
        try:
            null_idx = buf.index(b"\0")
        except ValueError:
            return None
        request_data = bytes(buf[:null_idx])
        del buf[: null_idx + 1]
        return request_data

    @staticmethod
    def _request_for_log(request_data: bytes) -> str:
        """Format a request for logs without exposing its authentication token."""
        try:
            request = json.loads(request_data)
        except (UnicodeDecodeError, json.JSONDecodeError):
            return request_data.decode("utf-8", errors="replace")
        if isinstance(request, dict) and "auth_token" in request:
            request["auth_token"] = "***"
        return json.dumps(request, ensure_ascii=False)

    def _log_request(self, request_data: bytes) -> None:
        """Show incoming work before execution, outside captured script output."""
        if self.logging:
            sys.stderr.write(f"Forge request:\n{self._request_for_log(request_data)}\n")
            sys.stderr.flush()

    def _log_result(self, exec_result: ExecResult) -> None:
        """Flush the immediate response or deferred status to the system console."""
        if self.logging:
            if exec_result.check_fn is not None:
                sys.stderr.write("Forge response: deferred\n")
            else:
                sys.stderr.write(f"Forge response: {json.dumps(exec_result.response, indent=2)}\n")
            sys.stderr.flush()

    def _service_clients(self) -> bool:
        """Read from connected clients and execute complete requests.

        Returns:
            True if any work was performed.
        """
        work_state = False
        for client in self.state.clients[:]:
            if time.monotonic() > client.deadline:
                self._queue_client_response(client, {"status": "error", "message": "Client timed out"})
                continue

            try:
                chunk = client.connection.recv(RECV_BUFFER_SIZE)
            except BlockingIOError:
                continue
            except OSError:
                self._close_client(client)
                continue

            if not chunk:
                self._close_client(client)
                continue

            client.buffer.extend(chunk)

            if len(client.buffer) > MAX_REQUEST_BYTES:
                self._queue_client_response(
                    client,
                    {"status": "error", "message": f"Request exceeds {MAX_REQUEST_BYTES} byte limit"},
                )
                continue

            request_data = self._extract_request_data(client.buffer)
            if request_data is None:
                continue
            if client.buffer:
                self._queue_client_response(
                    client,
                    {"status": "error", "message": "Only one request is allowed per connection"},
                )
                work_state = True
                continue

            self._log_request(request_data)
            exec_result, strict_json = self.executor.execute_from_request(request_data, self.token)
            self._log_result(exec_result)

            if exec_result.check_fn is not None:
                self.deferred.gather(
                    client.connection,
                    exec_result.check_fn,
                    strict_json,
                    exec_result.response.get("stdout", ""),
                    exec_result.response.get("stderr", ""),
                    exec_result.cancel_fn,
                )
                try:
                    self.state.clients.remove(client)
                except ValueError:
                    pass
            else:
                self._queue_client_response(client, exec_result.response)
            work_state = True

        return work_state

    def poll(self) -> bool:
        """
        Non-blocking poll: accept new connections, service existing clients, and check deferred responses.

        Returns:
            True if work was done during this poll. Callers use the value to
            pick the next timer interval, so a deferred operation that is still
            running does *not* count as work: the timer backs off to its idle
            interval during a long operation and is reset as soon as it
            finishes. A response that is still draining does count, so the
            remaining bytes are flushed on the next active tick.
            Call from ``bpy.app.timers``.
        """
        self._gather_clients()
        work_state = self._service_clients()
        if self.deferred.poll(self._queue_response):
            work_state = True
        if self._flush_responses():
            work_state = True
        return work_state or bool(self.state.responses)

    # ── Client I/O (background, blocking) ──────────────────────────

    def _handle_blocking_client(self, connection: _sock.socket) -> bool:
        """Handle a single client connection synchronously (background mode).

        Returns:
            True if the client was handled successfully.
        """
        connection.settimeout(CLIENT_TIMEOUT)
        try:
            buf = bytearray()
            while True:
                chunk = connection.recv(RECV_BUFFER_SIZE)
                if not chunk:
                    return False
                buf.extend(chunk)
                if len(buf) > MAX_REQUEST_BYTES:
                    send_error(connection, f"Request exceeds {MAX_REQUEST_BYTES} byte limit")
                    return False
                request_data = self._extract_request_data(buf)
                if request_data is not None:
                    break

            if buf:
                send_error(connection, "Only one request is allowed per connection")
                return False

            self._log_request(request_data)
            exec_result, strict_json = self.executor.execute_from_request(request_data, self.token)
            self._log_result(exec_result)

            if exec_result.check_fn is not None:
                response = self.deferred.resolve_once(
                    exec_result.check_fn,
                    strict_json,
                    exec_result.response.get("stdout", ""),
                    exec_result.response.get("stderr", ""),
                )
                if response is None:
                    if exec_result.cancel_fn is not None:
                        try:
                            with Guardian():
                                exec_result.cancel_fn()
                        except BaseException:
                            pass
                    response = {**exec_result.response, "status": "error", "message": DEFERRED_UNSUPPORTED_MESSAGE}
                exec_result = ExecResult(response)
            send_response(connection, exec_result.response)
            return True
        except _sock.socket.timeout:
            send_error(connection, "Client timed out")
            return False
        except OSError:
            return False
        finally:
            connection.close()

    def poll_blocking(self, timeout: float = POLL_BLOCKING_TIMEOUT) -> bool:
        """
        Block until a connection arrives (up to *timeout* seconds), then handle it synchronously.

        For ``blender --background`` mode.

        Args:
            timeout: Maximum time in seconds to wait for a connection.

        Returns:
            True if a connection was handled.
        """
        if self.state.socket is None:
            return False

        try:
            readable, _writable, _errored = select.select([self.state.socket], [], [], timeout)
        except (OSError, ValueError):
            return False

        if not readable:
            return False

        try:
            connection, _addr = self.state.socket.accept()
        except (BlockingIOError, OSError):
            return False

        return self._handle_blocking_client(connection)
