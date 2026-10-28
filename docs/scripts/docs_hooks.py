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

"""Build the portable documentation site using only files within docs/."""

import os
import posixpath
import re
from email.utils import formatdate
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit

from mkdocs.structure.files import File, Files
from mkdocs.utils import get_relative_url

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "content"
REFERENCES = (
    DOCS / "reference/MCP_INSTALL.md",
    DOCS / "reference/MCP_INSTALL.zh-CN.md",
    DOCS / "reference/mcp-server/README.md",
    DOCS / "reference/mcp-server/README.zh-CN.md",
)
LINK = re.compile(r"\[([^\]\n]*(?:`[^`\n]*`[^\]\n]*)*)\]\(([^\s)]+)\)")
HTML_ASSET = re.compile(r"""(\b(?:src|poster)\s*=\s*)(["'])([^"']+)\2""")


def _references():
    return REFERENCES


def _skills():
    order = {
        name: index
        for index, name in enumerate(("forge_create", "forge_modify", "forge_custom_material", "forge_operators"))
    }
    return sorted(
        (DOCS / "reference/mcp-server/forge_mcp/skills").glob("*.md"),
        key=lambda path: (order.get(path.stem, len(order)), path.name),
    )


def _skill_original(uri):
    if uri == "cn/mcp_skills.md":
        return "en/mcp_skills.md"
    if uri.startswith(("cn/mcp_skills/", "en/mcp_skills/")):
        return "reference/mcp-server/forge_mcp/skills/" + posixpath.basename(uri)
    if uri == "en/mcp_skills.md" or uri.startswith("reference/mcp-server/forge_mcp/skills/"):
        return uri
    return None


def _skill_ui_uri(uri, language):
    original = _skill_original(uri)
    if original is None:
        return uri
    return (
        f"{language}/mcp_skills.md"
        if original == "en/mcp_skills.md"
        else f"{language}/mcp_skills/" + posixpath.basename(original)
    )


def _english_only(uri):
    return _skill_original(uri) is not None


def _title(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def on_config(config):
    """Discover all Markdown pages, including newly added chapters."""
    config.theme.static_templates.add("cn/search.html")
    config.extra_javascript.remove("assets/javascripts/manual.js")
    config.extra_javascript.append("assets/javascripts/manual.js")
    config.nav = [{_title(DOCS / "introduction.md"): "introduction.md"}]
    for language, label in (("cn", "中文文档"), ("en", "English guide")):
        pages = [{"章节目录" if language == "cn" else "Contents": f"{language}/forge_docs.md"}]
        if language == "cn":
            pages.insert(0, {_title(DOCS / "introduction.zh-CN.md"): "introduction.zh-CN.md"})
        pages[0:0] = [
            {_title(DOCS / language / name): f"{language}/{name}"}
            for name in ("installation.md", "preferences.md", "development.md", "examples.md")
        ]
        for path in sorted((DOCS / language / "forge_docs").rglob("*.md")):
            pages.append({_title(path): path.relative_to(DOCS).as_posix()})
        config.nav.append({label: pages})
    config.nav.append({"Local preview": "en/preview.md"})
    config.nav.append({"本地预览": "cn/preview.md"})
    config.nav.append({"MCP reference": [{_title(path): path.relative_to(DOCS).as_posix()} for path in _references()]})
    config.nav.append(
        {
            "MCP Skills (English only)": [
                {"Overview": "en/mcp_skills.md"},
                *[{_title(path): _skill_ui_uri(path.relative_to(DOCS).as_posix(), "en")} for path in _skills()],
                {
                    "中文界面": [
                        {"Overview": "cn/mcp_skills.md"},
                        *[{_title(path): _skill_ui_uri(path.relative_to(DOCS).as_posix(), "cn")} for path in _skills()],
                    ]
                },
            ]
        }
    )
    return config


def on_files(files, config):
    """Render shared English sources under symmetric cn/ and en/ UI routes."""
    # Keep the site root as its landing page after renaming the Markdown source.
    files.get_file_from_path("introduction.md").dest_uri = "index.html"
    sources = [DOCS / "en/mcp_skills.md", *_skills()]
    for path in sources:
        original = path.relative_to(DOCS).as_posix()
        for language in ("en", "cn"):
            uri = _skill_ui_uri(original, language)
            if uri != original:
                files.append(File.generated(config, uri, abs_src_path=str(path)))
        if original.startswith("reference/"):
            files.remove(files.get_file_from_path(original))
    return files


def on_page_markdown(markdown, page, config, files):
    """Resolve extensionless links within the portable content directory.

    MkDocs then handles .md-to-.html conversion, including fragment links.
    Workspace config references remain text: runtime config is not a site asset.
    """
    source = Path(page.file.abs_src_path)
    language = _language(page.file.src_uri)
    # Resolve the shared source to its canonical URI first, then choose UI language.
    published = {
        Path(f.abs_src_path).resolve(): _skill_original(f.src_uri) or f.src_uri for f in files if f.abs_src_path
    }

    def rewrite(match):
        label, href = match.groups()
        url = urlsplit(href)
        if url.scheme or url.netloc or not url.path or url.path.startswith("/"):
            return match[0]
        target = (source.parent / unquote(url.path)).resolve()
        # Names such as README.zh-CN have a suffix, but still need .md appended.
        if not target.is_file() and Path(str(target) + ".md").is_file():
            target = Path(str(target) + ".md")
        destination = published.get(target)
        if destination:
            destination = _skill_ui_uri(destination, language)
            if (
                _english_only(page.file.src_uri)
                and _language(destination) != language
                and not _english_only(destination)
            ):
                translated = _counterpart(destination, files)
                if translated:
                    destination = translated.src_uri
            path = posixpath.relpath(destination, posixpath.dirname(page.file.src_uri) or ".")
            return f"[{label}]({urlunsplit(('', '', path, url.query, url.fragment))})"
        if target.is_file() and not target.is_relative_to(DOCS):
            return label
        return match[0]

    def rewrite_html_asset(match):
        prefix, quote, href = match.groups()
        url = urlsplit(href)
        if url.scheme or url.netloc or not url.path or url.path.startswith("/"):
            return match[0]
        target = (source.parent / unquote(url.path)).resolve()
        destination = published.get(target)
        if destination is None:
            return match[0]
        path = posixpath.relpath(destination, posixpath.dirname(page.file.src_uri) or ".")
        return prefix + quote + urlunsplit(("", "", path, url.query, url.fragment)) + quote

    # The HTML shell provides translated navigation and language switching.
    # Keep the original Markdown navigation intact for Obsidian readers.
    markdown = re.sub(r"^\[[^\n]+ · [^\n]+\n?", "", markdown, flags=re.M)
    markdown = re.sub(r"^## 章节跳转\s*$", "", markdown, flags=re.M)
    # Chapter indexes use the language switcher instead of parallel translations.
    markdown = re.sub(r"\s*·\s*\[(?:English|中文)\]\([^\n)]+\)", "", markdown)
    # Do not reinterpret Markdown examples inside fenced code blocks.
    chunks = re.split(r"(^```[^\n]*\n.*?^```[^\n]*$|^~~~[^\n]*\n.*?^~~~[^\n]*$)", markdown, flags=re.M | re.S)
    return "".join(
        chunk if i % 2 else HTML_ASSET.sub(rewrite_html_asset, LINK.sub(rewrite, chunk))
        for i, chunk in enumerate(chunks)
    )


def on_page_content(html, page, config, files):
    """Make the manual index's chapter list collapsible in both languages."""
    if page.file.src_uri not in {"cn/forge_docs.md", "en/forge_docs.md"}:
        return html

    def chapter_list(match):
        heading, chapters = match.groups()
        count = chapters.count("<li>")
        title = (
            f"章节列表（{count} 章）" if _language(page.file.src_uri) == "cn" else f"Chapter list ({count} chapters)"
        )
        return (
            heading
            + '<details class="chapter-index" data-nav-group="manual-page-contents" open>'
            + f'<summary class="chapter-index-toggle">{title}</summary>'
            + chapters
            + "</details>"
        )

    return re.sub(r"(<h2\b[^>]*>.*?</h2>\s*)(<ol\b[^>]*>.*?</ol>)", chapter_list, html, count=1, flags=re.S)


def _language(uri):
    return "cn" if uri.startswith("cn/") or ".zh-CN." in uri else "en"


def _counterpart(uri, files):
    if _english_only(uri):
        candidate = _skill_ui_uri(uri, "en" if _language(uri) == "cn" else "cn")
    elif uri.startswith(("cn/", "en/")):
        candidate = ("en/" if uri.startswith("cn/") else "cn/") + uri[3:]
    elif ".zh-CN.md" in uri:
        candidate = uri.replace(".zh-CN.md", ".md")
    else:
        candidate = uri.removesuffix(".md") + ".zh-CN.md"
    return files.get_file_from_path(candidate)


def _manual_context(context, uri, current_url):
    """Render only the current language's navigation, with paired page URLs."""
    files = Files(context["pages"])
    language = _language(uri)
    chinese = language == "cn"
    english_only = _english_only(uri)
    home = files.get_file_from_path("introduction.zh-CN.md" if chinese else "introduction.md")

    def entry(source, title=None):
        file = files.get_file_from_path(source)
        return {
            "title": title or file.page.title,
            "url": get_relative_url(file.url, current_url),
            "active": source == uri,
            "source": source,
        }

    chapters = [entry(f"{language}/forge_docs.md", "章节目录" if chinese else "Contents")]
    for path in sorted((DOCS / language / "forge_docs").rglob("*.md")):
        title = _title(path)
        title = re.sub(r"^(?:第 \d+ 章：|Chapter \d+: )", "", title)
        title = title.replace("Model Define — ", "")
        number = path.stem.split("_", 1)[0].lstrip("0") or "0"
        chapters.append(entry(path.relative_to(DOCS).as_posix(), f"{number}. {title}"))
    references = []
    for path in _references():
        source = path.relative_to(DOCS).as_posix()
        if _language(source) == language:
            references.append(entry(source, _title(path)))
    getting_started = [
        entry("introduction.zh-CN.md" if chinese else "introduction.md", "关于 Forge" if chinese else "About Forge"),
        entry(f"{language}/installation.md", "安装 Forge" if chinese else "Installation Forge"),
        entry(f"{language}/preferences.md", "配置 Forge" if chinese else "Config Forge"),
        entry(f"{language}/development.md", "开发 Forge" if chinese else "Development Forge"),
    ]
    skills = [entry(_skill_ui_uri("en/mcp_skills.md", language), "Overview")]
    skills.extend(entry(_skill_ui_uri(path.relative_to(DOCS).as_posix(), language), _title(path)) for path in _skills())
    examples = [entry(f"{language}/examples.md", "应用案例" if chinese else "Case studies")]
    groups = [
        {"id": "getting-started", "title": "开始使用" if chinese else "Getting started", "items": getting_started},
        {"id": "examples", "title": "案例" if chinese else "Examples", "items": examples},
        {"id": "manual", "title": "使用手册" if chinese else "User manual", "items": chapters},
        {"id": "mcp-reference", "title": "MCP 参考" if chinese else "MCP reference", "items": references},
        {"id": "mcp-skills", "title": "MCP Skills (English only)" if chinese else "MCP Skills", "items": skills},
        {
            "id": "documentation",
            "title": "文档" if chinese else "Documentation",
            "items": [entry(f"{language}/preview.md", "本地预览" if chinese else "Local preview")],
        },
    ]
    other = _counterpart(uri, files)
    if other is None and not english_only:
        other = files.get_file_from_path("cn/forge_docs.md" if not chinese else "en/forge_docs.md")
    previous_page = next_page = None
    for sequence in (getting_started + examples + chapters, references, skills, groups[-1]["items"]):
        for i, item in enumerate(sequence):
            if item["active"]:
                previous_page = sequence[i - 1] if i else None
                next_page = sequence[i + 1] if i + 1 < len(sequence) else None
    context.update(
        {
            "manual_language": language,
            "manual_english_only": english_only,
            "manual_current_url": get_relative_url(current_url, current_url),
            "manual_home": get_relative_url(home.url, current_url),
            "manual_groups": groups,
            "manual_previous": previous_page,
            "manual_next": next_page,
            "manual_other_url": get_relative_url(other.url, current_url) if other else None,
            "manual_search": get_relative_url("cn/search.html" if chinese else "search.html", current_url),
        }
    )
    if uri in {"search.html", "cn/search.html"}:
        context["manual_other_url"] = get_relative_url("search.html" if chinese else "cn/search.html", current_url)
    return context


def on_page_context(context, page, config, nav):
    return _manual_context(context, page.file.src_uri, page.url)


def on_template_context(context, template_name, config):
    return _manual_context(context, template_name, template_name)


def on_serve(server, config, builder):
    """Add byte-range video delivery to MkDocs 1.6's preview server."""
    application = server.get_app()

    def media_application(environ, start_response):
        path = environ.get("PATH_INFO", "").encode("latin-1").decode("utf-8", "ignore")
        method = environ.get("REQUEST_METHOD", "GET")
        if method not in {"GET", "HEAD"} or not path.startswith(server.mount_path) or not path.endswith(".mp4"):
            return application(environ, start_response)
        relative = path[len(server.mount_path) :]
        root = Path(server.root).resolve()
        video = (root / relative).resolve()
        if not video.is_relative_to(root) or not video.is_file():
            return application(environ, start_response)
        # Match MkDocs' rebuild coordination so requests see completed output.
        with server._epoch_cond:
            server._epoch_cond.wait_for(lambda: server._visible_epoch == server._wanted_epoch)
            try:
                stream = video.open("rb")
            except OSError:
                return application(environ, start_response)
        stat = os.fstat(stream.fileno())
        size = stat.st_size
        start, end, partial = 0, size - 1, False
        header = environ.get("HTTP_RANGE", "")
        # Ignore unsupported/malformed ranges and conditional ranges (full response).
        match = re.fullmatch(r"bytes=(\d*)-(\d*)", header)
        if method == "GET" and match and any(match.groups()) and not environ.get("HTTP_IF_RANGE"):
            first, last = match.groups()
            try:
                start = int(first) if first else max(0, size - int(last))
                end = min(int(last), size - 1) if first and last else size - 1
            except ValueError:
                start, end = 0, size - 1
            else:
                if start >= size or end < start or (not first and int(last) == 0):
                    stream.close()
                    start_response(
                        "416 Range Not Satisfiable",
                        [("Content-Range", f"bytes */{size}"), ("Accept-Ranges", "bytes"), ("Content-Length", "0")],
                    )
                    return []
                partial = True
        length = end - start + 1
        headers = [
            ("Content-Type", "video/mp4"),
            ("Content-Length", str(length)),
            ("Accept-Ranges", "bytes"),
            ("Last-Modified", formatdate(stat.st_mtime, usegmt=True)),
        ]
        if partial:
            headers.append(("Content-Range", f"bytes {start}-{end}/{size}"))
        start_response("206 Partial Content" if partial else "200 OK", headers)
        if method == "HEAD":
            stream.close()
            return []

        def chunks():
            with stream:
                stream.seek(start)
                remaining = length
                while remaining:
                    chunk = stream.read(min(64 * 1024, remaining))
                    if not chunk:
                        break
                    remaining -= len(chunk)
                    yield chunk

        return chunks()

    server.set_app(media_application)
    return server
