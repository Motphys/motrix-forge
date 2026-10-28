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
Safe Python code execution for MCP tool calls.

Isolates the ``exec()``-based code runner, JSON parsing, and result
validation from the socket I/O and server lifecycle logic.
"""

from __future__ import annotations

import hmac
import json
import traceback

from .capture import CaptureOutput
from .constants import ExecResult
from .guardian import Guardian


class CodeExecutor:
    """
    Execute Python code strings in a sandboxed environment.

    Each call runs inside a :class:`Guardian` context (which blocks
    dangerous operators) and a :class:`CaptureOutput` context (which
    captures stdout/stderr).
    """

    __slots__ = ()

    @staticmethod
    def execute(code: str, strict_json: bool) -> ExecResult:
        """
        Execute *code* and return an ``ExecResult``.

        Args:
            code: The Python code string to execute.
            strict_json: When true, the response *must* be serializable.

        Returns:
            An ExecResult containing the execution outcome.
        """
        # The bridge executes inside Blender, so expose the two Blender
        # modules promised by the ``forge_execute`` tool contract. Import
        # lazily to keep the executor unit-testable outside Blender.
        namespace: dict[str, object] = {"result": {}}
        try:
            import bpy  # type: ignore[import-not-found]

            namespace["bpy"] = bpy
        except ImportError:
            pass
        try:
            import mathutils  # type: ignore[import-not-found]

            namespace["mathutils"] = mathutils
        except ImportError:
            pass
        with CaptureOutput() as captured, Guardian():
            try:
                exec(code, namespace)
            except BaseException:  # Tool code must not escape into Blender's event loop.
                response: dict[str, object] = {"status": "error", "message": traceback.format_exc()}
                if captured.stdout:
                    response["stdout"] = captured.stdout
                if captured.stderr:
                    response["stderr"] = captured.stderr
                return ExecResult(response)

        # Check for a deferred response (background job in progress).
        check_fn_raw = namespace.get("check_is_finished")
        if check_fn_raw is not None and callable(check_fn_raw):
            cancel_fn_raw = namespace.get("cancel_operation")
            cancel_fn = cancel_fn_raw if callable(cancel_fn_raw) else None
            response = {}
            if captured.stdout:
                response["stdout"] = captured.stdout
            if captured.stderr:
                response["stderr"] = captured.stderr
            return ExecResult(response, check_fn_raw, cancel_fn)

        result = namespace["result"]
        if not isinstance(result, dict):
            response = {
                "status": "error",
                "message": (
                    f"""The `result` variable must be a dict, not {type(result).__name__}.
Wrap your return value: `result = {{{{"key": value}}}}`"""
                ),
            }
        else:
            if strict_json:
                try:
                    json.dumps(result)
                except (TypeError, ValueError) as ex:
                    response = {"status": "error", "message": f"The `result` value is not JSON-serializable: {str(ex)}"}
                else:
                    response = {"status": "ok", "result": result}
            else:
                # Fall back to ``repr`` so non-serializable objects appear as strings.
                result = json.loads(json.dumps(result, default=repr))
                response = {"status": "ok", "result": result}
        if captured.stdout:
            response["stdout"] = captured.stdout
        if captured.stderr:
            response["stderr"] = captured.stderr
        return ExecResult(response)

    @staticmethod
    def execute_from_request(request_data: bytes, expected_token: str = "") -> tuple[ExecResult, bool]:
        """
        Parse a raw request and execute the contained code.

        Args:
            request_data: Raw request bytes to parse and execute.

        Returns:
            A tuple of ``(exec_result, strict_json)``.
        """
        try:
            request = json.loads(request_data)
        except Exception:
            return ExecResult({"status": "error", "message": traceback.format_exc()}), False

        if not isinstance(request, dict):
            return ExecResult({"status": "error", "message": "Request must be a JSON object"}), False

        supplied_token = request.get("auth_token", "")
        if expected_token and (
            not isinstance(supplied_token, str) or not hmac.compare_digest(supplied_token, expected_token)
        ):
            return ExecResult({"status": "error", "message": "Authentication failed"}), False

        if request.get("type") != "execute":
            req_type = request.get("type")
            return (
                ExecResult(
                    {
                        "status": "error",
                        "message": f"Unknown request type: {req_type!r}",
                    }
                ),
                False,
            )

        code = request.get("code", "")
        strict_json = request.get("strict_json")
        if not isinstance(strict_json, bool):
            return (
                ExecResult(
                    {
                        "status": "error",
                        "message": (
                            """Internal error: a Forge mcp tool sent a request without the 'strict_json' boolean key.
                            This is a bug in the tool that generated this code"""
                        ),
                    }
                ),
                False,
            )

        exec_result = CodeExecutor.execute(code, strict_json=strict_json)
        return exec_result, strict_json
