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

"""
Material library operators.

Registered via ``operator.classes``.
"""

from __future__ import annotations

import bpy
from bpy.props import BoolProperty, EnumProperty, FloatVectorProperty, IntProperty, StringProperty
from bpy.types import Context, Operator

from ..core import constants as cons
from ..core import materials as matlib
from ..core import selection as sel


class Forge_OT_Material_Creation(Operator):
    """Create a PBR material from the Forge material library and assign it to the selected objects."""

    bl_idname = "forge.create_material"
    bl_label = "Common Material"
    bl_description = "Create a material from the Forge PBR library and assign it to the selection"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context: Context):
        """Require a non-empty selection of renderable Forge geometry objects.

        Materials created by this operator are assigned immediately, so every
        selected object must be a VISUAL, HFIELD, or PLANE model type and at
        least one object must be selected.

        Args:
            context: The Blender context.

        Returns:
            True when there is a selection and every selected object is VISUAL,
            HFIELD, or PLANE.
        """

        return sel.check_selected_model_types(
            context, [cons.ModelTypes.VISUAL, cons.ModelTypes.HFIELD, cons.ModelTypes.PLANE]
        )

    def category_items(self, context: Context):
        """Generate enum items for the library categories.

        Args:
            context: The Blender context.

        Returns:
            A list of (identifier, name, description) enum items.
        """
        return [(c, c, "") for c in matlib.get_categories()] or [("NONE", "None", "")]

    def material_items(self, context: Context):
        """Generate enum items for the materials in the selected category.

        Args:
            context: The Blender context.

        Returns:
            A list of (identifier, name, description) enum items.
        """
        if not self.category:
            return [("NONE", "None", "")]
        return [(n, n, "") for n in matlib.get_material_names(self.category)] or [("NONE", "None", "")]

    def category_update(self, context: Context):
        """Reset the material selection when the category changes.

        Args:
            context: The Blender context.
        """
        names = matlib.get_material_names(self.category)
        self.material = names[0] if names else "NONE"

    # Enum identifiers are the raw material names — they are unique across the
    # library and legal for Python-defined EnumProperty items.
    category: EnumProperty(  # type: ignore
        name="Category",
        items=category_items,
        update=category_update,
        default=0,
    )
    material: EnumProperty(  # type: ignore
        name="Material",
        items=material_items,
        default=0,
    )
    use_existing: BoolProperty(  # type: ignore
        name="Use Existing",
        description=(
            "Reuse an existing material with the same name instead of creating a new one "
            "(the existing material is assigned as-is, without rebuilding it from the library)"
        ),
        default=True,
    )

    def execute(self, context: Context):
        """Create the selected material and assign it to the selected objects.

        With ``use_existing`` an already present material with the same name
        is assigned as-is; otherwise a new material is built from the library.

        Args:
            context: The Blender context.

        Returns:
            A Blender operator result set.
        """
        params = matlib.load_material(self.category, self.material)
        if params is None:
            self.report({"ERROR"}, f"Material not found: {self.category}/{self.material}")
            return {"CANCELLED"}

        mat = bpy.data.materials.get(self.material) if self.use_existing else None
        reused = mat is not None
        if mat is None:
            mat = matlib.build_material(params, use_existing=False)

        assigned = 0
        for obj in context.selected_objects:
            if matlib.assign_material(context, obj, mat):
                assigned += 1

        message = f"Using existing material '{mat.name}'" if reused else f"Material '{mat.name}' created"
        if assigned:
            message += f", assigned to {assigned} object(s)"
        self.report({"INFO"}, message)
        return {"FINISHED"}

    def invoke(self, context: Context, event):
        """Invoke the operator, showing the category/material selection dialog.

        Args:
            context: The Blender context.
            event: The triggering event.

        Returns:
            A Blender operator result set.
        """
        return context.window_manager.invoke_props_dialog(self)


class Forge_OT_Material_Assign(Operator):
    """Assign an existing Blender material to the selected Forge geometry."""

    bl_idname = "forge.assign_material"
    bl_label = "Assign Material"
    bl_description = "Choose an existing material and assign it to the selection"
    bl_options = {"REGISTER", "UNDO"}

    material: StringProperty(  # type: ignore
        name="Material",
        description="Existing Blender material to assign",
    )

    @classmethod
    def poll(cls, context: Context):
        """Use the same geometry selection requirements as material creation."""
        return Forge_OT_Material_Creation.poll(context)

    def draw(self, context: Context):
        """Offer a searchable dropdown of existing material datablocks."""
        self.layout.prop_search(self, "material", bpy.data, "materials", icon="MATERIAL")

    def invoke(self, context: Context, event):
        """Start with the active object's material, when available."""
        if not self.material and context.object and context.object.active_material:
            self.material = context.object.active_material.name
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context: Context):
        """Reuse the selected material without rebuilding or copying it."""
        mat = bpy.data.materials.get(self.material)
        if mat is None:
            self.report({"ERROR"}, "Choose an existing material")
            return {"CANCELLED"}

        assigned = sum(matlib.assign_material(context, obj, mat) for obj in context.selected_objects)
        self.report({"INFO"}, f"Material '{mat.name}' assigned to {assigned} object(s)")
        return {"FINISHED"}


class Forge_OT_Checker_Material_Creation(Operator):
    """Create a PBR checker material and assign it to the selected geometry."""

    bl_idname = "forge.create_checker_material"
    bl_label = "Checker Material"
    bl_description = "Create a PBR checker material and assign it to the selection"
    bl_options = {"REGISTER", "UNDO"}

    color1: FloatVectorProperty(  # type: ignore
        name="Color 1",
        subtype="COLOR",
        size=4,
        min=0.0,
        max=1.0,
        default=(0.0, 0.0, 0.0, 1.0),
    )
    color2: FloatVectorProperty(  # type: ignore
        name="Color 2",
        subtype="COLOR",
        size=4,
        min=0.0,
        max=1.0,
        default=(1.0, 1.0, 1.0, 1.0),
    )
    repeat: IntProperty(  # type: ignore
        name="Repeat",
        description="Mapping scale along X and Y",
        default=4,
        min=1,
        max=128,
    )

    @classmethod
    def poll(cls, context: Context):
        """Use the same selection requirements as Create Material."""
        return Forge_OT_Material_Creation.poll(context)

    def execute(self, context: Context):
        """Build one checker material and assign it to every selected object."""
        mat = matlib.build_checker_material(self.color1, self.color2, self.repeat)
        assigned = 0
        for obj in context.selected_objects:
            if matlib.assign_material(context, obj, mat):
                assigned += 1
        self.report({"INFO"}, f"Material '{mat.name}' created, assigned to {assigned} object(s)")
        return {"FINISHED"}

    def invoke(self, context: Context, event):
        """Show the checker colors and repeat parameters."""
        return context.window_manager.invoke_props_dialog(self)
