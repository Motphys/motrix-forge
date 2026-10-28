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

"""Blender RST parsing, document discovery and search regressions."""

import importlib

import pytest
from forge_mcp.docs import Paragraph, load_docs, search_docs
from forge_mcp.rst import parse_rst

docs_module = importlib.import_module("forge_mcp.docs")


def test_heading_hierarchy_roles_and_empty_sections():
    sections = parse_rst("""
********
Modeling
********

Modifiers
=========

See :doc:`Bevel </modeling/bevel>` and :kbd:`Ctrl-B`.

Options
-------

Use ``segments``.

Siblings
========
""")
    assert (("Modeling", "Modifiers"), "See Bevel </modeling/bevel> and Ctrl-B.") in sections
    assert (("Modeling", "Modifiers", "Options"), "Use `segments`.") in sections
    assert sections[-1] == (("Modeling", "Siblings"), "Siblings")


def test_api_symbols_and_parameter_fields_keep_scope():
    sections = parse_rst("""
Objects
=======

.. currentmodule:: bpy.types

.. py:class:: Object(ID)

   Object description.

   .. attribute:: location

      Position in local space.

      :type: :class:`Vector`

   .. method:: select_set(state)

      Select this object.

      :arg state: Selection state.
      :type state: bool

.. class:: Mesh(ID)

   Mesh description.
""")
    location = [(b, t) for b, t in sections if "bpy.types.Object.location" in b]
    assert location and all(b[-2:] == ("bpy.types.Object", "bpy.types.Object.location") for b, _ in location)
    assert any(":type: Vector" in t for _, t in location)
    method = [(b, t) for b, t in sections if "bpy.types.Object.select_set" in b]
    assert any("select_set(state)" in t for _, t in method)
    assert any(":arg state:" in t and ":type state: bool" in t for _, t in method)
    assert sections[-1] == (("Objects", "bpy.types.Mesh"), "Mesh description.")


def test_code_admonitions_and_metadata():
    sections = parse_rst("""
Example
=======

.. _example-anchor:

.. index:: hidden-index

.. toctree::
   :maxdepth: 2

   hidden-navigation

.. include:: missing-file.rst

.. literalinclude:: missing-code.py
   :lines: 1-10

.. comment hidden-comment
   hidden-comment-body

.. figure:: /images/hidden-image.png
   :width: 200px

   Visible caption.

.. warning:: Keep this warning.

   Keep this explanation.

.. code-block:: python
   :linenos:

   if True:
       print(":class:`Keep code literal`")

   # Still code.

After the example.
""")
    text = "\n".join(t for _, t in sections)
    assert "hidden" not in text and "missing-" not in text
    assert "width" not in text and "linenos" not in text
    assert "Visible caption." in text
    assert "warning: Keep this warning." in text and "Keep this explanation." in text
    assert 'if True:\n    print(":class:`Keep code literal`")\n\n# Still code.' in text
    assert sections[-1] == (("Example",), "After the example.")


def test_api_field_without_description_and_literal_block():
    sections = parse_rst("""
.. module:: example

.. data:: value
   :noindex:

   :type: int

Example::

   if value:
       print(value)
""")
    assert (("Document", "example.value"), ":type: int") in sections
    assert any(t == "if value:\n    print(value)" for _, t in sections)
    assert not any("noindex" in t for _, t in sections)


@pytest.fixture
def local_docs(tmp_path, monkeypatch):
    mjcf = tmp_path / "mjcf"
    blender = tmp_path / "blender"
    mjcf.mkdir()
    (blender / "api").mkdir(parents=True)
    (blender / "manual" / "modeling").mkdir(parents=True)
    (mjcf / "body.md").write_text("# body\n\nMJCF body joint.", encoding="utf-8")
    (blender / "api" / "mesh.rst").write_text(
        "Mesh\n====\n\n.. module:: bpy.ops.mesh\n\n.. function:: bevel(offset=0.0)\n\n   Bevel the selected edges.",
        encoding="utf-8",
    )
    (blender / "manual" / "modeling" / "bevel.rst").write_text(
        "Bevel Modifier\n==============\n\nBevel edges with a modifier.", encoding="utf-8-sig"
    )
    # Exercise actual environment precedence while excluding machine/repo fallbacks.
    candidates = docs_module._candidate_dirs
    monkeypatch.setenv("FORGE_DOCS_DIR", str(mjcf))
    monkeypatch.setenv("FORGE_BLENDER_DOCS_DIR", str(blender))
    monkeypatch.setattr(docs_module, "_candidate_dirs", lambda corpus="mjcf": candidates(corpus)[:1])
    return load_docs()


def test_loads_both_corpora_recursively(local_docs):
    assert {p.source for p in local_docs} == {"mjcf", "blender_api", "blender_manual"}
    assert {p.file for p in local_docs} == {"body.md", "blender/api/mesh.rst", "blender/manual/modeling/bevel.rst"}
    assert {p.source for p in load_docs("blender_api")} == {"blender_api"}
    assert {p.source for p in load_docs("mjcf")} == {"mjcf"}


def test_source_filters_and_fully_qualified_search(local_docs):
    hit = search_docs(local_docs, "bpy.ops.mesh.bevel")["hits"][0]
    assert hit["source"] == "blender_api" and "Bevel the selected edges." in hit["text"]
    assert "offset=0.0" in hit["text"]
    assert search_docs(local_docs, "bevel", source="mjcf")["matched"] == "none"
    hits = search_docs(local_docs, "bevel", source="blender_manual")["hits"]
    assert hits and all(h["source"] == "blender_manual" for h in hits)
    assert {h["source"] for h in search_docs(local_docs, "bevel", source="blender")["hits"]} == {
        "blender_api",
        "blender_manual",
    }


def test_missing_blender_keeps_mjcf(local_docs, monkeypatch, tmp_path):
    monkeypatch.setenv("FORGE_BLENDER_DOCS_DIR", str(tmp_path / "missing"))
    assert {p.source for p in load_docs()} == {"mjcf"}


def test_discovery_falls_back_and_does_not_duplicate(tmp_path, monkeypatch):
    empty, first, second = (tmp_path / name for name in ("empty", "first", "second"))
    for path in (empty, first, second):
        path.mkdir()
    (first / "guide.rst").write_text("First\n=====\n\nChosen document.", encoding="utf-8")
    (second / "guide.rst").write_text("Second\n======\n\nIgnored document.", encoding="utf-8")
    monkeypatch.setattr(docs_module, "_candidate_dirs", lambda corpus="mjcf": [empty, first, second])
    loaded = load_docs("blender")
    assert len(loaded) == 2 and all("Second" not in p.breadcrumb for p in loaded)


def test_ranking_and_context_do_not_merge_api_members():
    docs = [
        Paragraph("blender/api/a.rst", ("API", "first"), "bevel", "blender_api"),
        Paragraph("blender/api/a.rst", ("API", "second"), "bevel bevel bevel", "blender_api"),
        Paragraph("blender/api/a.rst", ("API", "third"), "unrelated", "blender_api"),
    ]
    result = search_docs(docs, "bevel", max_results=1, context=3)
    assert result["truncated"]
    assert result["hits"][0]["breadcrumb"] == "API > second"
    assert result["hits"][0]["text"] == "bevel bevel bevel"
    assert result["hits"][0]["index"] == 0


@pytest.mark.parametrize("kwargs", [{"source": "invalid"}, {"max_results": 0}, {"context": -1}])
def test_invalid_search_arguments(kwargs):
    with pytest.raises(ValueError):
        search_docs([], "bevel", **kwargs)
