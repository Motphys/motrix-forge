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

"""Unit tests for the MJCF reference loading and search (forge_mcp/docs.py)."""

from forge_mcp.docs import load_doc_files, load_docs, search_docs


def test_load_docs_nonempty():
    docs = load_docs()
    assert len(docs) > 100
    assert all(d.file and d.breadcrumb and d.text for d in docs)


def test_load_doc_files_includes_index_and_body():
    files = load_doc_files()
    assert "index" in files
    assert "body" in files
    assert files["body"].startswith("# body")


def test_search_docs_single_token_all():
    res = search_docs(load_docs(), "condim", max_results=5)
    assert res["matched"] == "all"
    assert res["hits"]
    assert all({"path", "breadcrumb", "text", "score", "index"} <= h.keys() for h in res["hits"])
    assert all(h["score"] > 0 for h in res["hits"])


def test_search_docs_fallback_any():
    # "joint" matches many paragraphs, "zzzzqqxx" matches none -> fallback
    res = search_docs(load_docs(), "zzzzqqxx joint", max_results=3)
    assert res["matched"] == "any"
    assert res["hits"]


def test_search_docs_no_match():
    res = search_docs(load_docs(), "zzzzqqxx", max_results=3)
    assert res["hits"] == []
    assert res["matched"] == "none"


def test_search_docs_empty_query():
    res = search_docs(load_docs(), "", max_results=3)
    assert res["hits"] == []
    assert res["matched"] == "none"


def test_search_docs_max_results_truncates():
    res = search_docs(load_docs(), "condim", max_results=2)
    assert len(res["hits"]) <= 2
    assert res["truncated"] is True or len(res["hits"]) == 2


def test_search_docs_context_does_not_crash():
    res = search_docs(load_docs(), "condim", max_results=1, context=2)
    assert res["hits"]
