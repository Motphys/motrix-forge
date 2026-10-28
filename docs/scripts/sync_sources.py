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

"""Refresh portable documentation snapshots from a full Forge checkout.

This is an explicit authoring step. Preview and builds never read outside docs/.
"""

import posixpath
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
LINK = re.compile(r"\[([^\]\n]*(?:`[^`\n]*`[^\]\n]*)*)\]\(([^\s)]+)\)")
HTML_ASSET = re.compile(r"""(\b(?:src|poster)\s*=\s*)(["'])([^"']+)\2""")
FENCES = re.compile(r"(^```[^\n]*\n.*?^```[^\n]*$|^~~~[^\n]*\n.*?^~~~[^\n]*$)", re.M | re.S)


def source_pairs(repository):
    references = [
        repository / name
        for name in (
            "MCP_INSTALL.md",
            "MCP_INSTALL.zh-CN.md",
            "mcp-server/README.md",
            "mcp-server/README.zh-CN.md",
        )
    ]
    references.extend(sorted((repository / "mcp-server/forge_mcp/skills").glob("*.md")))
    assets = [
        repository / "media/images" / name
        for name in (
            "forge_pipeline.png",
            "decomposition.png",
            "Addons.png",
            "forge-dep.png",
        )
    ]
    assets.extend(sorted((repository / "media/videos/HD").glob("*.mp4")))
    return [(path, CONTENT / "reference" / path.relative_to(repository)) for path in references] + [
        (path, CONTENT / "assets" / ("images" if path.suffix == ".png" else "videos") / path.name) for path in assets
    ]


def relocate_links(text, origin, destination, mapping):
    """Rewrite repository links to their portable copies, preserving code examples."""

    def resolve(href):
        url = urlsplit(href)
        if url.scheme or url.netloc or not url.path or url.path.startswith("/"):
            return None
        target = (origin.parent / unquote(url.path)).resolve()
        published = mapping.get(target) or mapping.get(Path(str(target) + ".md"))
        if published is not None:
            path = posixpath.relpath(published.as_posix(), destination.parent.as_posix())
            return urlunsplit(("", "", path, url.query, url.fragment))
        return None

    def link(match):
        label, href = match.groups()
        resolved = resolve(href)
        if resolved is not None:
            return f"[{label}]({resolved})"
        target = (origin.parent / unquote(urlsplit(href).path)).resolve()
        # Runtime configuration and source files are named, never bundled as site assets.
        if not urlsplit(href).scheme and target.is_file() and target not in mapping:
            return label
        return match[0]

    def asset(match):
        prefix, quote, href = match.groups()
        resolved = resolve(href)
        return prefix + quote + resolved + quote if resolved is not None else match[0]

    return "".join(
        chunk if i % 2 else HTML_ASSET.sub(asset, LINK.sub(link, chunk)) for i, chunk in enumerate(FENCES.split(text))
    )


def main():
    repository = ROOT.parent
    if not (repository / "addon/Forge").is_dir() or not (repository / "mcp-server").is_dir():
        raise SystemExit(
            "Run this optional sync step in the full Forge checkout. Standalone docs can build without it."
        )
    pairs = source_pairs(repository)
    mapping = {source.resolve(): target.resolve() for source, target in pairs}
    # Original guides can link to authored site pages such as Forge configuration.
    mapping.update({path.resolve(): path.resolve() for path in CONTENT.rglob("*") if path.is_file()})
    for source, _ in pairs:
        if not source.is_file():
            raise SystemExit(f"Missing source: {source}")
        if source.suffix != ".md":
            with source.open("rb") as stream:
                if stream.read(128).startswith(b"version https://git-lfs.github.com/spec/"):
                    raise SystemExit(f"Git LFS pointer found: {source}. Run git lfs pull before syncing.")
    for source, target in pairs:
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix == ".md":
            text = relocate_links(source.read_text(encoding="utf-8"), source, target, mapping)
            target.write_text(text, encoding="utf-8")
        else:
            shutil.copy2(source, target)
    print(f"Synced {len(pairs)} reference documents and media files into docs/content.")


if __name__ == "__main__":
    main()
