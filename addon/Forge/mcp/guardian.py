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
Guardian for LLM-generated code execution.

Notes:

- The reason *not* to use the prompt is that it tends not to be reliable,
  sometimes initial requests leave the context window (or are ignored for whatever reason),
  so we are better off with a simple way to prevent some things from happening.

- If the LLM (or its user) is motivated these can be worked around.
  This is more of a slap on the wrist not to try some things.
"""

__all__ = ("Guardian",)

import sys
from typing import Any, Self


def _block_exit(*args: object, **kwargs: object) -> None:  # noqa: ARG001
    """Block sys.exit calls by raising RuntimeError."""
    raise RuntimeError("sys.exit() is not allowed in LLM-generated code")


# Each entry is `(object, attr_name, replacement)`.
_OVERRIDES: tuple[tuple[object, str, object], ...] = ((sys, "exit", _block_exit),)

# Operators that LLM-generated code must not access.
# Each entry is `("module.func", "reason")`.
_BLOCKED_OPS: tuple[tuple[str, str], ...] = (
    (
        "wm.quit_blender",
        "Terminates the Blender process, use bpy.app.quit() if you must",
    ),
    (
        "wm.read_factory_settings",
        """Resets all user preferences and startup file, use bpy.ops.wm.read_homefile()
        or bpy.ops.wm.read_homefile(use_empty=True, use_factory_startup=True) instead""",
    ),
    (
        "wm.read_factory_userpref",
        """Resets all user preferences, use bpy.ops.wm.read_homefile()
        or bpy.ops.wm.read_homefile(use_empty=True, use_factory_startup=True) instead""",
    ),
    (
        "wm.read_userpref",
        "May reset user preferences or disabling this add-on, avoid calling",
    ),
    (
        "wm.write_homefile",
        "Overwrites the default startup file. This should not be done by the LLM.",
    ),
)


def _make_blocked(key: str, reason: str):
    """Create a replacement operator that raises RuntimeError."""

    def _blocked(
        *args: tuple[object, ...],
        **kwargs: dict[str, object],
    ):
        """Blocked operator that raises RuntimeError with details."""
        args_str = ", ".join([repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()])
        raise RuntimeError(f"Operator 'bpy.ops.{key}({args_str})' is not allowed in LLM-generated code: {reason}")

    return _blocked


class Guardian:
    """Context manager wrapping ``exec()`` of LLM-generated code."""

    __slots__ = (
        "_store_attrs",
        "_store_ops",
    )

    @staticmethod
    def override_store() -> list[tuple[object, str, object]]:
        """Save current values listed in ``_OVERRIDES`` and apply replacements."""
        saved: list[tuple[object, str, object]] = []
        for obj, attr, replacement in _OVERRIDES:
            saved.append((obj, attr, getattr(obj, attr)))
            setattr(obj, attr, replacement)
        return saved

    @staticmethod
    def override_restore(saved: list[tuple[object, str, object]]) -> None:
        """Restore values previously captured by `override_store`."""
        for obj, attr, original in saved:
            setattr(obj, attr, original)

    @staticmethod
    def ops_blocked_store() -> dict[str, tuple]:
        """Replace ``bpy.ops._op_create_function`` with a filtered wrapper."""
        import bpy.ops as _bpy_ops  # noqa: WPS433

        _store_ops: dict[str, Any] = {}

        for op_key, reason in _BLOCKED_OPS:
            module_name, func_name = op_key.split(".")

            try:
                submod = getattr(_bpy_ops, module_name)  # bpy.ops.wm
            except AttributeError:
                continue  # Module doesn't exist in this Blender build

            # Pre-warm: trigger lazy creation by accessing the operator
            try:
                original = getattr(submod, func_name)
            except AttributeError:
                continue  # Operator doesn't exist in this Blender build

            # Save original for restore
            _store_ops[op_key] = (submod, func_name, original)

            # Replace with blocked version
            setattr(submod, func_name, _make_blocked(op_key, reason))

        return _store_ops

    @staticmethod
    def ops_blocked_restore(saved: dict[str, tuple]) -> None:
        """Restore the original operators."""
        for submod, func_name, original in saved.values():
            try:
                setattr(submod, func_name, original)
            except Exception:
                pass

    def __enter__(self) -> Self:
        """Enter the guardian context, saving and overriding dangerous operations."""
        self._store_attrs = self.override_store()
        self._store_ops = self.ops_blocked_store()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        """Exit the guardian context, restoring overridden operations."""
        del exc_type, exc_val, exc_tb
        self.ops_blocked_restore(self._store_ops)
        self.override_restore(self._store_attrs)
