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

"""Load the ``skills/*.md`` authoring guides served by the ``forge_skill`` tool.

Each ``forge_<name>.md`` becomes a skill named ``<name>``; the first ``#``
heading is the title and the paragraph below it the summary used in the
server instructions index. Served on demand so the full guides never sit in
context unless an agent actually asks for them.
"""

from __future__ import annotations

import os
import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

from mcp.server.mcpserver.exceptions import ToolError

_HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$", re.MULTILINE)

# Tool execution is nudged at the Blender bridge boundary: reading a guide
# once marks this server process as authorized, so the full guides never sit
# in context unless an agent actually asks for them. The set lives for the
# whole process lifetime on purpose — it is shared across requests and clients
# and resets when the server process restarts.
_loaded_rules: set[str] = set()

# Skills already pointed at, so an agent that ignores the hint is not nagged on
# every call. Guides actually read live in ``_loaded_rules`` and are never
# pointed at again. Nothing is queued here: a hint is derived from the call that
# earns it (see :func:`claim_hints`), so a call that fails cannot leave one
# behind for an unrelated operation to inherit.
_hinted_rules: set[str] = set()

# How the guard behaves, from ``FORGE_MCP_SKILL_GATE``:
#   off    — never intervene;
#   soft   — let the operation through and attach one pointer to the guide
#            (the default: guidance belongs in the prompt, not in a wall);
#   strict — refuse the operation until the guide has been read.
GATE_MODES = ("off", "soft", "strict")
DEFAULT_GATE_MODE = "soft"


def gate_mode() -> str:
    """Resolve the configured gate mode, falling back to the default when unset or unknown."""
    mode = os.environ.get("FORGE_MCP_SKILL_GATE", DEFAULT_GATE_MODE).strip().lower()
    return mode if mode in GATE_MODES else DEFAULT_GATE_MODE


def mark_loaded(name: str) -> None:
    """Record that a guide has been delivered."""
    _loaded_rules.add(name)


def rules_loaded() -> frozenset[str]:
    return frozenset(_loaded_rules)


_guides: dict[str, Skill] | None = None


def guides_loaded() -> dict[str, Skill]:
    """The parsed guides, loaded once per process.

    The package loads them at import for the server instructions; hints are
    built from the same parse rather than re-reading every ``.md`` mid-request,
    which would also let the section index drift from what ``forge_skill`` serves.
    """
    global _guides
    if _guides is None:
        _guides = load_skills()
    return _guides


def require_rule(name: str) -> None:
    """Apply the gate for *name*: refuse (strict) or allow (soft, off).

    Only strict intervenes here; soft defers to :func:`claim_hints` once the
    operation has actually succeeded, so a refused or failed call never counts
    as having delivered — or consumed — a pointer to the guide.
    """
    if name in _loaded_rules:
        return
    if gate_mode() != "strict":
        return
    # ToolError (not RuntimeError): the MCP framework forwards ToolError
    # messages to the client verbatim, while a generic exception's text is
    # treated as a crash detail and stays server-side.
    raise ToolError(
        f"SKILL_REQUIRED: read forge_skill(name='{name}') before Blender operations; "
        f"the {name} guide is authoritative for supported workflows"
    )


def claim_hints(names: Iterable[str]) -> tuple[str, ...]:
    """Return the guides among *names* still owed a pointer, and mark them pointed at.

    Call this only once the operation has succeeded: a call that fails must not
    consume a hint, nor mark the guide as delivered. Each guide is claimed at
    most once per process, so an agent that ignores the pointer is not nagged.
    """
    if gate_mode() != "soft":
        return ()
    fresh = tuple(sorted({name for name in names if name not in _loaded_rules and name not in _hinted_rules}))
    _hinted_rules.update(fresh)
    return fresh


def hint_message(names: tuple[str, ...]) -> dict[str, object]:
    """Compact pointer to the owed guides: names, how to read them, and a section index.

    Deliberately not the guide bodies — the point is to let an agent fetch one
    section on demand instead of pulling a 20 KB guide into context.
    """
    guides = guides_loaded()
    # A call can owe one guide or both, so the sentence has to agree with the
    # count. At most two exist — ``required_skills_for_code`` returns only
    # "create" and "modify" — so " and " is enough to join them.
    plural = len(names) > 1
    calls = " and ".join(f"forge_skill(name='{name}')" for name in names)
    return {
        "skills": list(names),
        "message": (
            f"{calls} {'are' if plural else 'is'} the authoritative "
            f"guide{'s' if plural else ''} for supported workflows — read "
            f"{'them' if plural else 'it'} before authoring (pass `section` to fetch just one part)."
        ),
        "sections": {name: guides[name].section_index() for name in names if name in guides},
    }


def _normalize_heading(text: str) -> str:
    """Normalize a heading for loose matching: strip heading marks, inline code/emphasis, trailing punctuation."""
    t = re.sub(r"^#+\s*", "", text)
    t = re.sub(r"[`*_]", "", t)
    t = re.sub(r"[:.\s]+$", "", t)
    return re.sub(r"\s+", " ", t).strip().lower()


@dataclass(frozen=True)
class Skill:
    """One ``skills/*.md`` guide."""

    name: str
    title: str
    summary: str
    content: str

    def sections(self) -> list[tuple[str, str]]:
        """Split content into ``(heading, body)`` pairs at every level-2+ heading.

        Each body runs from its heading up to (not including) the next heading of
        the same or higher level, so container headings include their sub-sections.
        """
        lines = self.content.splitlines()
        marks: list[tuple[int, int, str]] = [
            (i, len(m.group(1)), line) for i, line in enumerate(lines) if (m := _HEADING_RE.match(line))
        ]
        out: list[tuple[str, str]] = []
        for idx, (start, level, heading) in enumerate(marks):
            end = len(lines)
            for nxt in range(idx + 1, len(marks)):
                if marks[nxt][1] <= level:
                    end = marks[nxt][0]
                    break
            out.append((heading, "\n".join(lines[start:end])))
        return out

    def section_index(self) -> list[str]:
        """Top-level section names, as the compact index a soft-mode hint carries.

        Only level-2 headings: the sub-headings would balloon the pointer toward
        the size of the guide it exists to avoid pulling into context.
        """
        return [_normalize_heading(heading) for heading, _ in self.sections() if heading.startswith("## ")]

    def section(self, name: str) -> str:
        """Return the body of the section whose heading best matches *name*.

        Prefers an exact normalized match, then a unique substring match. Raises
        ``ValueError`` (listing candidates / available sections) when the match is
        ambiguous or nothing matches.
        """
        target = _normalize_heading(name)
        if not target:
            return self.content
        sections = self.sections()
        exact = [(h, b) for h, b in sections if _normalize_heading(h) == target]
        if len(exact) == 1:
            general = next((b for h, b in sections if _normalize_heading(h) == "general rules"), "")
            return f"{exact[0][1]}\n\n{general}" if general and target != "general rules" else exact[0][1]
        if len(exact) > 1:
            raise ValueError(f"ambiguous section {name!r} in skill {self.name!r}: {[h for h, _ in exact]}")
        subs = [(h, b) for h, b in sections if target in _normalize_heading(h)]
        if len(subs) == 1:
            return subs[0][1]
        if len(subs) > 1:
            raise ValueError(f"ambiguous section {name!r} in skill {self.name!r}: {[h for h, _ in subs]}")
        available = ", ".join(f"`{_normalize_heading(h)}`" for h, _ in sections)
        raise ValueError(f"no section {name!r} in skill {self.name!r}; available: {available}")


def _candidate_dirs() -> list[Path]:
    dirs: list[Path] = []
    if env_dir := os.environ.get("FORGE_SKILLS_DIR"):
        dirs.append(Path(env_dir))
    dirs.append(Path(__file__).parent / "skills")  # package data alongside the module
    dirs += [
        parent / "skills" for parent in Path(__file__).resolve().parents
    ]  # backwards-compatible workspace fallback
    dirs.append(Path.cwd() / "skills")
    return dirs


def load_skills() -> dict[str, Skill]:
    """Load every ``*.md`` from the first ``skills`` directory that contains any."""
    for directory in _candidate_dirs():
        if not directory.is_dir():
            continue
        skills = {
            name: _parse_skill(name, path)
            for path in sorted(directory.glob("*.md"))
            if (name := _skill_name(path.name))
        }
        if skills:
            return skills
    return {}


def build_instructions(skills: dict[str, Skill], has_docs: bool = False) -> str | None:
    """Short index injected as server instructions so agents discover the guides and docs search."""
    if not skills and not has_docs:
        return None
    lines = []
    if skills:
        lines.append("Forge MJCF authoring guides are available via the `forge_skill` tool:")
        lines += [
            f'- forge_skill(name="{name}") — {skills[name].summary or skills[name].title}' for name in sorted(skills)
        ]
    if has_docs:
        lines.append(
            "Local MJCF and Blender API/manual documentation is searchable with `forge_search_docs(query, source)`; "
            "source can be all, mjcf, blender, blender_api, or blender_manual."
        )
    lines.append("Read the relevant guide with `forge_skill` before creating or modifying Forge models.")
    lines.append(
        "Follow the guides strictly: they are the authoritative spec — never read the addon source code for "
        "behavior, and report a missing capability as feedback instead of improvising."
    )
    if gate_mode() == "soft":
        lines.append(
            "The tools do not block on this: an operation that needs a guide runs normally and returns a "
            "`skill_hint` naming it, so treat that hint as a required follow-up read, not a warning."
        )
    return "\n".join(lines)


def _skill_name(filename: str) -> str:
    """``forge_create.md`` -> ``create``."""
    return re.sub(r"\.md$", "", filename, flags=re.IGNORECASE).removeprefix("forge_")


def _parse_skill(name: str, path: Path) -> Skill:
    content = path.read_text(encoding="utf-8")
    title: str | None = None
    summary = ""
    for line in content.splitlines():
        text = line.strip()
        if not text:
            continue
        if title is None:
            if text.startswith("# "):
                title = text[2:].strip()
            continue
        if not text.startswith("#"):
            summary = text
            break
    return Skill(name=name, title=title or name, summary=summary, content=content)
