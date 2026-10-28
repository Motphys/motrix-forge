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

"""Smoke tests for the complete addon registration lifecycle."""

from types import SimpleNamespace

import bpy
import Forge
from Forge.ops import properties_operators
from Forge.ui import panel


class _FakeLayout:
    def __init__(self):
        self.labels = []
        self.prop_calls = []

    def box(self):
        return self

    def label(self, **kwargs):
        self.labels.append(kwargs)

    def prop(self, *args, **kwargs):
        self.prop_calls.append((args, kwargs))


def test_full_register_unregister_lifecycle():
    """The public addon entry points register and clean up every subsystem."""
    Forge.register()
    try:
        assert hasattr(bpy.types.Object, "Forge_Model_Type")
        assert hasattr(bpy.types.Object, "Forge_Matrix_Info")
        assert "Forge Library" in bpy.context.preferences.filepaths.asset_libraries
        assert any(cls.bl_idname == "forge.export_mjcf" for cls in Forge.operator.classes)
        assert any(cls.bl_idname == "forge.properties_visual" for cls in Forge.operator.classes)
        assert panel.Forge_Properties_Panel in panel.classes
    finally:
        Forge.unregister()

    assert not hasattr(bpy.types.Object, "Forge_Model_Type")
    assert not hasattr(bpy.types.Object, "Forge_Matrix_Info")


def test_property_operator_classes_are_registered(registered_props):
    """Popup editors expose every registered properties operator idname."""
    registered = []
    for cls in properties_operators.classes:
        try:
            bpy.utils.register_class(cls)
            registered.append(cls)
        except (RuntimeError, ValueError):
            pass
    try:
        for cls in properties_operators.classes:
            namespace, name = cls.bl_idname.split(".", 1)
            assert hasattr(getattr(bpy.ops, namespace), name)

        bpy.ops.object.select_all(action="DESELECT")
        assert properties_operators.Forge_OT_PROPERTIES_Global.poll(bpy.context) is True
        bpy.ops.mesh.primitive_cube_add()
        assert properties_operators.Forge_OT_PROPERTIES_Global.poll(bpy.context) is False
    finally:
        for cls in reversed(registered):
            try:
                bpy.utils.unregister_class(cls)
            except (RuntimeError, ValueError):
                pass


def test_mcp_panel_handles_unavailable_addon_preferences(monkeypatch):
    """Panel drawing remains safe while Blender has no preferences entry."""
    layout = _FakeLayout()
    panel_instance = SimpleNamespace(layout=layout)
    monkeypatch.setattr(panel, "get_addon_prefs", lambda: None)
    monkeypatch.setattr(panel, "get_server", lambda: None)

    panel.Forge_MCP_Panel.draw(panel_instance, bpy.context)

    assert layout.prop_calls == []
    assert layout.labels == [{"text": "Add-on preferences unavailable", "icon": "ERROR"}]
