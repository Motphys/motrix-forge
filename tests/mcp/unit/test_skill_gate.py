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

"""Unit tests for the skill gate: modes, one-time hints, and the call_blender wiring."""

import json

import forge_mcp.blender as blender
import pytest
from forge_mcp import skills as skill_mod
from forge_mcp.blender import required_skills_for_code
from forge_mcp.skills import (
    DEFAULT_GATE_MODE,
    _normalize_heading,
    claim_hints,
    gate_mode,
    hint_message,
    load_skills,
    mark_loaded,
    require_rule,
)
from mcp.server.mcpserver.exceptions import ToolError


def test_package_attribute_skills_is_the_module_not_the_loaded_dict():
    """Guard the shadowing footgun: ``forge_mcp.__init__`` must not bind a ``skills`` dict.

    Binding one there makes ``from forge_mcp import skills`` hand back loaded
    guides where every reader expects the module, which silently breaks
    monkeypatching of the module's gate state.
    """
    import forge_mcp

    assert skill_mod is not forge_mcp.skill_guides
    assert isinstance(forge_mcp.skill_guides, dict)
    assert hasattr(skill_mod, "require_rule")


@pytest.fixture(autouse=True)
def clean_gate(monkeypatch):
    """Isolate the process-wide gate state and the mode from every other test."""
    monkeypatch.delenv("FORGE_MCP_SKILL_GATE", raising=False)
    monkeypatch.setattr(skill_mod, "_loaded_rules", set())
    monkeypatch.setattr(skill_mod, "_hinted_rules", set())
    yield


class FakeSocket:
    def __init__(self, chunks):
        self.chunks = iter(chunks)
        self.sent = b""

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return None

    def sendall(self, data):
        self.sent += data

    def recv(self, _size):
        return next(self.chunks, b"")


def _patch_connection(monkeypatch, *chunks):
    connection = FakeSocket(chunks)
    monkeypatch.setattr(blender.socket, "create_connection", lambda *_a, **_k: connection)
    return connection


def _ok(result: dict) -> bytes:
    return json.dumps({"status": "ok", "result": result}).encode() + b"\0"


# ── Mode resolution ───────────────────────────────────────────────────


def test_gate_defaults_to_soft():
    assert DEFAULT_GATE_MODE == "soft"
    assert gate_mode() == "soft"


@pytest.mark.parametrize("mode", ["off", "soft", "strict"])
def test_gate_mode_reads_env(monkeypatch, mode):
    monkeypatch.setenv("FORGE_MCP_SKILL_GATE", mode)
    assert gate_mode() == mode


@pytest.mark.parametrize("value", ["", "   ", "STRICT!", "yes", "1"])
def test_gate_mode_falls_back_when_unset_or_unknown(monkeypatch, value):
    monkeypatch.setenv("FORGE_MCP_SKILL_GATE", value)
    assert gate_mode() == DEFAULT_GATE_MODE


def test_gate_mode_is_case_and_space_insensitive(monkeypatch):
    monkeypatch.setenv("FORGE_MCP_SKILL_GATE", "  Strict ")
    assert gate_mode() == "strict"


# ── Per-mode behaviour ────────────────────────────────────────────────


def test_soft_mode_does_not_block():
    require_rule("create")  # must not raise


def test_claim_hints_reports_each_guide_once():
    assert claim_hints(("create",)) == ("create",)
    # An agent that ignores the pointer must not be nagged on every call.
    assert claim_hints(("create",)) == ()
    assert claim_hints(("modify",)) == ("modify",)


def test_claim_hints_skips_a_guide_already_read():
    mark_loaded("create")
    assert claim_hints(("create",)) == ()


def test_claim_hints_is_sorted_and_deduplicated():
    assert claim_hints(("modify", "create", "create")) == ("create", "modify")


def test_claim_hints_reports_nothing_in_off_mode(monkeypatch):
    monkeypatch.setenv("FORGE_MCP_SKILL_GATE", "off")
    assert claim_hints(("create",)) == ()


def test_off_mode_does_not_block(monkeypatch):
    monkeypatch.setenv("FORGE_MCP_SKILL_GATE", "off")
    require_rule("create")


def test_strict_mode_refuses_until_the_guide_is_read(monkeypatch):
    monkeypatch.setenv("FORGE_MCP_SKILL_GATE", "strict")
    with pytest.raises(ToolError, match="SKILL_REQUIRED"):
        require_rule("create")
    mark_loaded("create")
    require_rule("create")  # now permitted
    # strict never attaches a hint; require_rule did the refusing already.
    assert claim_hints(("create",)) == ()


def test_a_guide_read_before_any_hint_is_never_claimed():
    require_rule("create")
    mark_loaded("create")
    assert claim_hints(("create",)) == ()


# ── Hint payload ──────────────────────────────────────────────────────


def test_hint_names_the_guide_and_carries_a_section_index():
    hint = hint_message(("create",))
    assert hint["skills"] == ["create"]
    assert "forge_skill(name='create')" in hint["message"]
    assert hint["sections"]["create"] == [
        "general rules",
        "forge mjcf model types",
        "hierarchy rules",
        "create rules",
    ]


def test_hint_message_agrees_with_the_number_of_guides():
    # One call can owe both guides; the sentence has to read as a sentence.
    one = hint_message(("create",))["message"]
    assert one.startswith("forge_skill(name='create') is the authoritative guide")
    assert "read it before authoring" in one

    both = hint_message(("create", "modify"))["message"]
    assert "forge_skill(name='create') and forge_skill(name='modify') are the authoritative guides" in both
    assert "read them before authoring" in both


def test_hint_index_keeps_only_level_two_headings():
    guide = load_skills()["create"]
    sub_headings = [_normalize_heading(h) for h, _ in guide.sections() if h.startswith("### ")]
    assert sub_headings, "the create guide is expected to nest sub-sections"
    assert not set(sub_headings) & set(guide.section_index())


def test_hint_stays_small_next_to_the_guide_it_points_at():
    guide = load_skills()["create"]
    payload = json.dumps(hint_message(("create",)))
    assert len(payload) < len(guide.content) / 10


# ── call_blender wiring ───────────────────────────────────────────────


def test_call_blender_lets_a_forge_op_through_with_a_one_time_hint(monkeypatch):
    _patch_connection(monkeypatch, _ok({"created": ["LNK_Link"]}))
    result = blender.call_blender("import bpy\nbpy.ops.forge.create_link()")
    assert result["created"] == ["LNK_Link"]
    assert result["skill_hint"]["skills"] == ["create"]

    _patch_connection(monkeypatch, _ok({"created": ["LNK_Link_001"]}))
    assert "skill_hint" not in blender.call_blender("import bpy\nbpy.ops.forge.create_link()")


def test_call_blender_attaches_no_hint_for_ordinary_blender_edits(monkeypatch):
    # op_call emits obj.select_set(True) for every selection-based call; the
    # marker scan that used to gate on it is gone.
    code = "obj.select_set(True)\nobj.location = (1.0, 0.0, 0.0)"
    assert required_skills_for_code(code) == ()

    _patch_connection(monkeypatch, _ok({"ok": True}))
    assert "skill_hint" not in blender.call_blender(code)


def test_call_blender_strict_mode_refuses_a_forge_op(monkeypatch):
    monkeypatch.setenv("FORGE_MCP_SKILL_GATE", "strict")
    _patch_connection(monkeypatch, _ok({"created": ["LNK_Link"]}))
    with pytest.raises(ToolError, match="SKILL_REQUIRED"):
        blender.call_blender("import bpy\nbpy.ops.forge.create_link()")


def test_call_blender_off_mode_never_hints(monkeypatch):
    monkeypatch.setenv("FORGE_MCP_SKILL_GATE", "off")
    _patch_connection(monkeypatch, _ok({"created": ["LNK_Link"]}))
    assert "skill_hint" not in blender.call_blender("import bpy\nbpy.ops.forge.create_link()")


def test_failed_operation_does_not_leak_its_hint_onto_the_next_call(monkeypatch):
    # A call that never returns must not leave a hint queued for whatever runs
    # next, and must not mark the guide as already pointed at either.
    _patch_connection(monkeypatch, json.dumps({"status": "error", "message": "boom"}).encode() + b"\0")
    with pytest.raises(ToolError, match="boom"):
        blender.call_blender("import bpy\nbpy.ops.forge.create_link()")

    _patch_connection(monkeypatch, _ok({"ok": True}))
    assert "skill_hint" not in blender.call_blender("result = {}")

    _patch_connection(monkeypatch, _ok({"created": ["LNK_Link"]}))
    retry = blender.call_blender("import bpy\nbpy.ops.forge.create_link()")
    assert retry["skill_hint"]["skills"] == ["create"]


def test_enforce_skill_false_skips_the_check_entirely(monkeypatch):
    monkeypatch.setenv("FORGE_MCP_SKILL_GATE", "strict")
    _patch_connection(monkeypatch, _ok({}))
    assert blender.call_blender("import bpy\nbpy.ops.forge.create_link()", enforce_skill=False) == {}


# ── dedicated tools that write through direct property access ─────────


def _generated_code(monkeypatch, tool: str, *args) -> str:
    """Run a dedicated tool with the bridge stubbed out; return the code it built."""
    import forge_mcp.tools.scene as scene

    seen: dict[str, str] = {}
    monkeypatch.setattr(scene, "call_blender", lambda code, **_: seen.setdefault("code", code))
    getattr(scene, tool)(*args)
    return seen["code"]


def test_set_property_is_gated_by_its_direct_forge_access(monkeypatch):
    """`forge_set_property` writes a `Forge_` group, so it asks for modify by rule.

    See "Direct property access" in `skills/forge_modify.md`. The gate used to
    ride an unrelated branch of the same template — the `obj.data, key[5:]`
    binding — so rewriting that binding silently dropped the tool to ungated.
    Binding the group through a literal-bearing expression is what makes the
    direct access visible to the visitor.
    """
    code = _generated_code(monkeypatch, "set_property", "LNK_X", {"damping": 0.1})

    assert required_skills_for_code(code) == ("modify",)
    # Independent of that binding — clearing it must not change the answer.
    without_data_binding = code.replace("obj.data, key[5:]", "None, key[5:]")
    assert without_data_binding != code, "the data: binding moved; this test is stale"
    assert required_skills_for_code(without_data_binding) == ("modify",)


def test_set_shape_size_is_gated(monkeypatch):
    """Shape / gizmo sizes are direct property access too (`obj.modifiers[...]` sockets).

    The signal comes from the template's `obj.Forge_Geometry.type` read rather
    than from the socket write, which the visitor cannot follow through
    `next(...)`. Pinned here so the tool cannot silently lose the gate.
    """
    assert required_skills_for_code(_generated_code(monkeypatch, "set_shape_size", "GEO_X", 0.5)) == ("modify",)


def test_read_only_inspection_is_not_gated(monkeypatch):
    """`forge_object_info` reads the same group; reading is not a Forge edit."""
    assert required_skills_for_code(_generated_code(monkeypatch, "object_info", "GEO_X")) == ()
