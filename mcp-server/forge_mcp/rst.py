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

"""Extract searchable sections from Blender's Sphinx RST without building Sphinx.

This is a text indexer, not a renderer: headings and Python directive scopes
become breadcrumbs, prose/fields/code remain searchable, and presentation
metadata is omitted. Includes are never opened and directives are never run.
"""

from __future__ import annotations

import re
import textwrap

_ADORNMENT = re.compile(r"^([=\-~^\"'`:+*#<>_%])\1{2,}$")
_DIRECTIVE = re.compile(r"^(\s*)\.\.\s+(?:py:)?([\w-]+)::\s*(.*)$")
_ROLE = re.compile(r":(?:[\w-]+:)?[\w-]+:`([^`]+)`")
_LINK = re.compile(r"`([^`]+)`_{1,2}")
_OPTION = re.compile(
    r":(?:align|width|height|scale|alt|target|class|name|caption|linenos|lineno-start|"
    r"emphasize-lines|dedent|force|noindex|no-index|noindexentry|no-index-entry|"
    r"annotation|canonical|value|abstractmethod|async|classmethod|staticmethod):"
)
_SYMBOLS = {"class", "function", "method", "classmethod", "staticmethod", "attribute", "data", "property", "exception"}
_SKIP = {"toctree", "index", "include", "literalinclude", "default-role", "highlight", "tabularcolumns", "meta"}


def _inline(text: str) -> str:
    def label(match: re.Match) -> str:
        value = match[1]
        # Keep both the human label and the target searchable.
        return value.lstrip("~!")

    text = _ROLE.sub(label, text)
    text = _LINK.sub(label, text)
    return text.replace("``", "`")


def parse_rst(content: str, fallback_title: str = "Document") -> list[tuple[tuple[str, ...], str]]:
    """Return (breadcrumb, text) units, including fully qualified API symbols.

    Supports overline/underline headings, nested Python API directives, field
    lists, admonitions, literal blocks and code-block directives. Unknown
    directive bodies are retained as text rather than discarded.
    """
    lines = content.expandtabs(8).splitlines()
    result: list[tuple[tuple[str, ...], str]] = []
    headings: list[str] = []
    styles: list[tuple[str, bool]] = []
    symbols: list[tuple[int, str]] = []
    module = ""
    buffer: list[str] = []
    skip_indent: int | None = None
    option_indent: int | None = None
    code_indent: int | None = None

    def breadcrumb() -> tuple[str, ...]:
        return tuple(headings or [fallback_title]) + tuple(name for _, name in symbols)

    def flush() -> None:
        text = textwrap.dedent("\n".join(buffer)).strip()
        if text:
            result.append((breadcrumb(), text))
        buffer.clear()

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        indent = len(line) - len(line.lstrip())
        if not stripped:
            if code_indent is not None:
                buffer.append("")
            else:
                flush()
            i += 1
            continue
        if skip_indent is not None:
            if indent > skip_indent:
                i += 1
                continue
            skip_indent = None
        if option_indent is not None:
            if indent > option_indent and _OPTION.match(stripped):
                i += 1
                continue
            option_indent = None
        if code_indent is not None:
            if indent > code_indent:
                buffer.append(line)
                i += 1
                continue
            flush()
            code_indent = None

        # API scopes end on dedent; flush under the previous breadcrumb first.
        if symbols and indent <= symbols[-1][0]:
            flush()
            while symbols and indent <= symbols[-1][0]:
                symbols.pop()

        heading = None
        if (
            _ADORNMENT.fullmatch(stripped)
            and i + 2 < len(lines)
            and lines[i + 1].strip()
            and lines[i + 2].strip() == stripped
        ):
            heading = (lines[i + 1].strip(), (stripped[0], True), 3)
        elif (
            i + 1 < len(lines)
            and _ADORNMENT.fullmatch(lines[i + 1].strip())
            and not _ADORNMENT.fullmatch(stripped)
            and len(lines[i + 1].strip()) >= len(stripped)
            and len(lines[i + 1]) - len(lines[i + 1].lstrip()) == indent
        ):
            heading = (stripped, (lines[i + 1].strip()[0], False), 2)
        if heading:
            flush()
            title, style, consumed = heading
            if style not in styles:
                styles.append(style)
            level = styles.index(style)
            headings = headings[:level] + [_inline(title)]
            symbols.clear()
            # Titles must be searchable even in a section with no body.
            result.append((breadcrumb(), _inline(title)))
            i += consumed
            continue

        if directive := _DIRECTIVE.match(line):
            flush()
            kind, value = directive[2], directive[3]
            if kind in ("module", "currentmodule"):
                module = value
                symbols.clear()
                option_indent = indent
            elif kind in _SYMBOLS:
                name = value.split("(", 1)[0].strip()
                parent = symbols[-1][1] if symbols else module
                qualified = f"{parent}.{name}" if parent and not name.startswith(parent + ".") else name
                symbols.append((indent, qualified))
                result.append((breadcrumb(), f"{kind} {qualified}{value[len(name) :]}"))
                option_indent = indent
            elif kind in _SKIP:
                skip_indent = indent
            elif kind in ("code-block", "code", "sourcecode"):
                code_indent = indent
                option_indent = indent
            else:
                option_indent = indent
                if kind not in ("image", "figure", "container", "only", "rubric"):
                    buffer.append(_inline(f"{kind}: {value}"))
                elif kind == "rubric":
                    buffer.append(_inline(value))
            i += 1
            continue
        if stripped.startswith(".. ") or stripped == "..":
            # Explicit targets, substitutions and comments are metadata.
            flush()
            skip_indent = indent
            i += 1
            continue
        if _ADORNMENT.fullmatch(stripped):
            flush()
            i += 1
            continue
        buffer.append(_inline(line))
        if stripped.endswith("::"):
            flush()
            code_indent = indent
        i += 1
    flush()
    return result
