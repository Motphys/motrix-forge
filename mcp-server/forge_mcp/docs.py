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

"""Load MJCF Markdown and Blender RST references for ``forge_search_docs``.

Files follow the MJCF reference layout: one ``#`` title per file, one ``##``
section per element path (``body/joint`` ...) holding prose paragraphs and
``Attributes`` markdown tables. Table rows are indexed as individual units so
attribute lookups (``condim``, ``kp`` ...) hit a single row, not a whole table.
"""

from __future__ import annotations

import math
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from .rst import parse_rst

DocSource = Literal["all", "mjcf", "blender", "blender_api", "blender_manual"]
_SOURCES = ("all", "mjcf", "blender", "blender_api", "blender_manual")

_STOPWORDS = frozenset(
    (
        "a an and are as at be but by for from has have how i in is it its of on or that the this to was what when "
        "where which who will with"
    ).split()
)

_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_TABLE_SEPARATOR = re.compile(r"^\|[\s:|-]+\|?\s*$")


@dataclass(frozen=True)
class Paragraph:
    """One indexable unit: a prose paragraph or a single table row."""

    file: str
    breadcrumb: tuple[str, ...]
    text: str
    source: str = "mjcf"


def _candidate_dirs(corpus: str = "mjcf") -> list[Path]:
    dirs: list[Path] = []
    env_var = "FORGE_DOCS_DIR" if corpus == "mjcf" else "FORGE_BLENDER_DOCS_DIR"
    if env_dir := os.environ.get(env_var):
        dirs.append(Path(env_dir))
    dirs.append(Path(__file__).parent / "docs" / corpus)  # package data alongside the module
    dirs += [
        parent / "docs" / corpus for parent in Path(__file__).resolve().parents
    ]  # backwards-compatible workspace fallback
    dirs.append(Path.cwd() / "docs" / corpus)
    return list(dict.fromkeys(dirs))


def load_docs(source: DocSource = "all") -> list[Paragraph]:
    """Load each corpus independently; recursively parse Blender API/manual RST.

    The first populated directory wins per corpus. Missing Blender docs are
    optional and never prevent loading the MJCF reference.
    """
    _validate_source(source)
    paragraphs: list[Paragraph] = []
    if source in ("all", "mjcf"):
        for directory in _candidate_dirs():
            loaded: list[Paragraph] = []
            for path in sorted(directory.glob("*.md")):
                loaded += _parse_markdown(path.name, path.read_text(encoding="utf-8"))
            if loaded:
                paragraphs.extend(loaded)
                break
    if source != "mjcf":
        for directory in _candidate_dirs("blender"):
            loaded = []
            for path in sorted(directory.rglob("*.rst")):
                relative = path.relative_to(directory)
                kind = {"api": "blender_api", "manual": "blender_manual"}.get(relative.parts[0], "blender")
                file = f"blender/{relative.as_posix()}"
                loaded.extend(
                    Paragraph(file, breadcrumb, text, kind)
                    for breadcrumb, text in parse_rst(path.read_text(encoding="utf-8-sig"), path.stem)
                )
            if loaded:
                paragraphs.extend(p for p in loaded if _matches_source(p, source))
                break
    return paragraphs


def _validate_source(source: str) -> None:
    if source not in _SOURCES:
        raise ValueError(f"unknown documentation source {source!r}; choose from {', '.join(_SOURCES)}")


def _matches_source(paragraph: Paragraph, source: str) -> bool:
    return (
        source == "all"
        or paragraph.source == source
        or (source == "blender" and paragraph.source.startswith("blender"))
    )


def load_doc_files() -> dict[str, str]:
    """Return ``{element: raw markdown}`` for the first ``forge_mcp/docs/mjcf`` directory found.

    Same discovery as :func:`load_docs`; the raw text backs the ``mjcf://*``
    MCP resources (``forge_mcp/resources.py``).
    """
    for directory in _candidate_dirs():
        if not directory.is_dir():
            continue
        files = {path.stem: path.read_text(encoding="utf-8") for path in sorted(directory.glob("*.md"))}
        if files:
            return files
    return {}


def search_docs(
    docs: list[Paragraph], query: str, max_results: int = 10, context: int = 0, source: DocSource = "all"
) -> dict:
    """Ranked paragraph search: every token must match the text, breadcrumb or path.

    When no paragraph matches all tokens, falls back to ranking paragraphs that
    match any token (``matched: "any"``) — row-granular units rarely contain
    every concept of a multi-attribute query.
    """
    _validate_source(source)
    if max_results < 1 or context < 0:
        raise ValueError("max_results must be positive and context must be non-negative")
    docs = [paragraph for paragraph in docs if _matches_source(paragraph, source)]
    tokens = list(dict.fromkeys(token for token in query.lower().split() if token not in _STOPWORDS))
    if not tokens or not docs:
        return {"hits": [], "truncated": False, "matched": "none"}

    file_parts: dict[str, list[str]] = {}
    for paragraph in docs:
        file_parts.setdefault(paragraph.file, []).extend((*paragraph.breadcrumb, paragraph.text))
    file_text = {file: "\n".join(parts).lower() for file, parts in file_parts.items()}
    file_count = len(file_text)

    idf = {
        token: math.log((file_count + 1) / (1 + sum(token in text for text in file_text.values()))) + 1
        for token in tokens
    }
    patterns = {token: _token_pattern(token) for token in tokens}

    matches: list[tuple[int, float]] = []  # (paragraph index, score)
    fallback: list[tuple[int, float]] = []
    for index, paragraph in enumerate(docs):
        text = paragraph.text.lower()
        breadcrumb = " ".join(paragraph.breadcrumb).lower()
        path = paragraph.file.rsplit(".", 1)[0].lower()
        score = 0.0
        matched_all = True
        for token in tokens:
            count = len(patterns[token].findall(text))
            in_breadcrumb = patterns[token].search(breadcrumb) is not None
            in_path = patterns[token].search(path) is not None
            if count or in_breadcrumb or in_path:
                score += (
                    count * idf[token] + (3 * idf[token] if in_breadcrumb else 0) + (3 * idf[token] if in_path else 0)
                )
            else:
                matched_all = False
        if score > 0:
            (matches if matched_all else fallback).append((index, score))

    matched = "all"
    if not matches:
        if fallback:
            matches = fallback
            matched = "any"
        else:
            matched = "none"

    hits = [_build_hit(docs, cluster, context) for cluster in _cluster(docs, matches, context)]
    hits.sort(key=lambda hit: hit["score"], reverse=True)
    truncated = len(hits) > max_results
    for index, hit in enumerate(hits[:max_results]):
        hit["index"] = index
    return {"hits": hits[:max_results], "truncated": truncated, "matched": matched}


def _token_pattern(token: str) -> re.Pattern:
    """``body/joint`` keeps matching inside ``body/joint`` — word boundaries only where the edge is a word char."""
    prefix = r"\b" if token[0].isalnum() else ""
    suffix = r"\b" if token[-1].isalnum() else ""
    return re.compile(f"{prefix}{re.escape(token)}{suffix}")


def _parse_markdown(file: str, content: str) -> list[Paragraph]:
    paragraphs: list[Paragraph] = []
    breadcrumb: list[str] = []
    buffer: list[str] = []
    table: list[str] = []

    def flush_buffer() -> None:
        text = "\n".join(buffer).strip()
        if text:
            paragraphs.append(Paragraph(file=file, breadcrumb=tuple(breadcrumb), text=text))
        buffer.clear()

    def flush_table() -> None:
        rows = table[2:] if len(table) >= 2 and _TABLE_SEPARATOR.match(table[1]) else table  # drop header + |---| rows
        for row in rows:
            if row.strip():
                paragraphs.append(Paragraph(file=file, breadcrumb=tuple(breadcrumb), text=row.strip()))
        table.clear()

    for line in content.splitlines():
        if heading := _HEADING.match(line):
            flush_buffer()
            flush_table()
            breadcrumb = breadcrumb[: heading[1].count("#") - 1]
            breadcrumb.append(heading[2])
        elif line.lstrip().startswith("|"):
            flush_buffer()
            table.append(line)
        elif line.strip():
            flush_table()
            buffer.append(line)
        else:
            flush_buffer()
            flush_table()
    flush_buffer()
    flush_table()
    return paragraphs


def _cluster(docs: list[Paragraph], matches: list[tuple[int, float]], context: int) -> list[list[tuple[int, float]]]:
    """Merge matches on adjacent paragraphs of the same file (gap <= 2*context+1) into one hit."""
    clusters: list[list[tuple[int, float]]] = []
    for index, score in matches:
        if (
            clusters
            and index - clusters[-1][-1][0] <= 2 * context + 1
            and docs[index].file == docs[clusters[-1][-1][0]].file
            and docs[index].breadcrumb == docs[clusters[-1][-1][0]].breadcrumb
        ):
            clusters[-1].append((index, score))
        else:
            clusters.append([(index, score)])
    return clusters


def _build_hit(docs: list[Paragraph], cluster: list[tuple[int, float]], context: int) -> dict:
    """Sum cluster scores; widen the text window within the same file and breadcrumb only."""
    start = _widen(docs, cluster[0][0], context, -1)
    end = _widen(docs, cluster[-1][0], context, +1)
    first = docs[cluster[0][0]]
    return {
        "path": first.file,
        "source": first.source,
        "breadcrumb": " > ".join(first.breadcrumb),
        "text": "\n".join(paragraph.text for paragraph in docs[start : end + 1]),
        "score": round(sum(score for _, score in cluster), 2),
    }


def _widen(docs: list[Paragraph], index: int, context: int, step: int) -> int:
    for _ in range(context):
        neighbor = index + step
        if (
            0 <= neighbor < len(docs)
            and docs[neighbor].file == docs[index].file
            and docs[neighbor].breadcrumb == docs[index].breadcrumb
        ):
            index = neighbor
    return index
