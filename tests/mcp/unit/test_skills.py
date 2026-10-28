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

"""Unit tests for skills/*.md loading and section parsing (forge_mcp/skills.py)."""

import pytest
from forge_mcp.skills import _normalize_heading, load_skills


def _create():
    return load_skills()["create"]


def test_load_skills_has_builtin_guides_and_custom_material():
    assert set(load_skills()) == {"create", "modify", "operators", "custom_material"}


def test_custom_material_documents_mix_and_conditional_alpha():
    content = load_skills()["custom_material"].content
    assert "ShaderNodeMix" in content
    assert 'data_type = "RGBA"' in content
    assert 'blend_type = "MULTIPLY"' in content
    assert "Alpha is linked only when the material's intended use requires transparency" in content
    assert 'material_usage in {"SEMITRANSPARENT", "MASK_CLIP"}' in content
    assert "not from Blender's `surface_render_method` or `blend_method` properties" in content
    assert 'outputs["Alpha"]' in content
    assert "`Scale: (1, 1, 1)`" in content
    assert "Mapping scale `(1, 1, 1)`" in content
    assert 'mapping.inputs["Scale"].default_value = (1.0, 1.0, 1.0)' in content
    assert "(2, 2, 1)" not in content
    assert 'image.colorspace_settings.name = "Non-Color" if non_color else "sRGB"' in content
    assert "exporter resolves this node by name" in content
    assert 'bsdf.name = "Principled BSDF"' in content
    assert "target.material_slots[0].material = mat" in content
    assert 'result = {"object": target.name, "material": mat.name}' in content


def test_normalize_heading_strips_markup_and_punctuation():
    assert _normalize_heading("#### `link`: ") == "link"
    assert _normalize_heading("## General rules") == "general rules"
    assert _normalize_heading("### Create tips:") == "create tips"
    assert _normalize_heading("#### `joint type`") == "joint type"


def test_sections_container_includes_children():
    sections = dict(_create().sections())
    body = sections["### Model create rules:"]
    assert "#### `link`:" in body
    assert "#### `joint`:" in body


def test_section_exact_match_returns_only_that_heading():
    out = _create().section("joint")
    assert out.splitlines()[0].strip() == "#### `joint`:"
    assert "bpy.ops.forge.create_joint" in out
    # must not include the following sibling section
    assert "create_light" not in out


def test_section_container_returns_all_children():
    out = _create().section("model create rules")
    assert "#### `link`:" in out
    assert "#### `joint`:" in out


def test_section_unique_substring_match():
    out = load_skills()["modify"].section("joint")  # only `#### joint type` contains it
    assert out.splitlines()[0].strip() == "#### `joint type`:"


def test_section_empty_returns_full_content():
    create = _create()
    assert create.section("") == create.content
    assert create.section("   ") == create.content


def test_section_unknown_lists_available():
    with pytest.raises(ValueError, match="available"):
        _create().section("bogus")


def test_section_does_not_mutate_content():
    create = _create()
    before = create.content
    create.section("joint")
    assert create.content == before
