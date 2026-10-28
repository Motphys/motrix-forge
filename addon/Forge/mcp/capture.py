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

__all__ = ("CaptureOutput",)

import io
import sys
from typing import IO, Self

from .constants import MAX_CAPTURED_OUTPUT_BYTES

_TRUNCATION_MARKER = "\n[output truncated]\n"


class _Mirror(io.TextIOBase):
    """Write to both a :class:`io.StringIO` buffer and the original stream."""

    __slots__ = (
        "_buffer",
        "_original",
        "_truncated",
    )

    def __init__(self, original: IO[str]) -> None:
        """Initialize the mirror with the original stream."""
        self._buffer = io.StringIO()
        self._original = original
        self._truncated = False

    def write(self, s: str) -> int:
        """Write to both the original stream and the buffer."""
        self._original.write(s)
        remaining = MAX_CAPTURED_OUTPUT_BYTES - self._buffer.tell()
        if remaining > 0 and not self._truncated:
            if len(s) <= remaining:
                self._buffer.write(s)
            else:
                payload = max(0, remaining - len(_TRUNCATION_MARKER))
                self._buffer.write(s[:payload])
                self._buffer.write(_TRUNCATION_MARKER[: remaining - payload])
                self._truncated = True
        return len(s)

    def flush(self) -> None:
        """Flush both the original stream and the buffer."""
        self._original.flush()
        self._buffer.flush()

    def getvalue(self) -> str:
        """Return the captured output from the buffer."""
        return self._buffer.getvalue()


class CaptureOutput:
    """Context manager that captures STDOUT & STDERR.

    Output is forwarded to the original streams in real time
    and also stored for retrieval via `stdout` and `stderr`.
    """

    __slots__ = (
        "_mirror_out",
        "_mirror_err",
        "_original_out",
        "_original_err",
    )

    def __enter__(self) -> Self:
        """Enter the capture context, redirecting stdout/stderr."""
        self._original_out = sys.stdout
        self._original_err = sys.stderr
        self._mirror_out = _Mirror(self._original_out)
        self._mirror_err = _Mirror(self._original_err)
        sys.stdout = self._mirror_out
        sys.stderr = self._mirror_err
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        """Exit the capture context, restoring original streams."""
        del exc_type, exc_val, exc_tb
        sys.stdout = self._original_out
        sys.stderr = self._original_err

    @property
    def stdout(self) -> str:
        """Return the captured stdout string."""
        return self._mirror_out.getvalue()

    @property
    def stderr(self) -> str:
        """Return the captured stderr string."""
        return self._mirror_err.getvalue()
