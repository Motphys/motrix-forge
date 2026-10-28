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
PBR material library loader and builder.

Loads the JSON material library from ``lib/materials`` (lazily, cached)
and builds node-based Blender materials from it. The library entries are
generated from a physically based material database; ``color`` values are
already in linear working space (extracted from ``srgb-linear``), so they
are set on shader inputs directly without conversion.

Non-shader fields (density, viscosity, category, tags, ...) are stored as
custom ID properties on the material for later use.
"""

from __future__ import annotations

import json
import os
from functools import lru_cache
from typing import Any

import bpy
from bpy.types import Context, Material, Object

from . import constants as cons
from .common import ensure_shader_nodes

_MATERIALS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "lib", "materials")

_CATEGORIES = ("Crystal", "Human", "Liquid", "Manmade", "Metal", "Organic", "Plastic")

#: Fields stored as custom ID properties (everything not mapped to a shader input).
_CUSTOM_PROP_KEYS = (
    "density",
    "viscosity",
    "surfaceTension",
    "category",
    "tags",
    "group",
    "acousticAbsorption",
    "volumeCoefficients",
    "transmissionDispersion",
)


# ═══════════════════════════════════════════════════════════════════════
# Library loader
# ═══════════════════════════════════════════════════════════════════════


@lru_cache(maxsize=1)
def _load_all() -> dict[str, dict[str, dict[str, Any]]]:
    """Lazily load all category JSON files once, keyed by category then name.

    Returns:
        A dict mapping category names to dicts of material name to params.
    """
    library: dict[str, dict[str, dict[str, Any]]] = {}
    for category in _CATEGORIES:
        with open(os.path.join(_MATERIALS_DIR, f"{category}.json"), encoding="utf-8") as file:
            library[category] = json.load(file)
    return library


def get_categories() -> list[str]:
    """Return the ordered list of material library categories.

    Returns:
        A list of category names in library file order.
    """
    return list(_load_all().keys())


def get_material_names(category: str) -> list[str]:
    """Return the material names in a category, in library order.

    Args:
        category: The category name.

    Returns:
        A list of material names (empty for an unknown category).
    """
    return list(_load_all().get(category, {}).keys())


def load_material(category: str, name: str) -> dict[str, Any] | None:
    """Return the raw params dict for (category, name), or None when missing.

    Args:
        category: The category name.
        name: The material name.

    Returns:
        The material params dict, or None if not found.
    """
    return _load_all().get(category, {}).get(name)


# ═══════════════════════════════════════════════════════════════════════
# Material builder
# ═══════════════════════════════════════════════════════════════════════


def _scalar(value: Any) -> Any:
    """Reduce a library list value to a scalar by taking its last element.

    Args:
        value: A scalar or list value from the library.

    Returns:
        The value itself, or the last element when it is a non-empty list.
    """
    return value[-1] if isinstance(value, list) and value else value


def _set_input(inputs, name: str, value: Any):
    """Set a shader input only when it exists and the value is not None.

    Args:
        inputs: The node input sockets collection.
        name: The socket name.
        value: The value to assign.
    """
    if value is None or name not in inputs:
        return
    inputs[name].default_value = value


def build_material(params: dict[str, Any], use_existing: bool = True) -> Material:
    """Create or update a Blender material from library params.

    With ``use_existing`` an existing material with the same name is reused
    (updating it in place); otherwise a new material is always created
    (Blender suffixes the name when it is taken). Sets the renderable PBR
    fields on the Principled BSDF shader, and stores all other library
    fields as custom ID properties.

    Args:
        params: The material params dict from the JSON library.
        use_existing: Reuse an existing material with the same name.

    Returns:
        The created or updated Material.
    """
    name = params["name"]
    mat = bpy.data.materials.get(name) if use_existing else None
    if mat is None:
        mat = bpy.data.materials.new(name)
    ensure_shader_nodes(mat)

    nodes = mat.node_tree.nodes
    shader = nodes.get(cons.ShaderPropName.PRINCIPLED)
    if shader is None:
        shader = nodes.new("ShaderNodeBsdfPrincipled")
        output = nodes.get("Material Output")
        if output:
            mat.node_tree.links.new(shader.outputs["BSDF"], output.inputs["Surface"])

    inputs = shader.inputs

    # The library color is already linear (srgb-linear source) — set directly.
    color = list(params["color"])
    if len(color) == 3:
        color.append(1.0)
    _set_input(inputs, cons.NodeInputName.COLOR, color)

    _set_input(inputs, cons.NodeInputName.METALLIC, params.get("metalness", 0.0))
    _set_input(inputs, cons.NodeInputName.ROUGHNESS, params.get("roughness", 0.5))
    _set_input(inputs, "IOR", params.get("ior"))
    _set_input(inputs, "Transmission Weight", params.get("transmission"))
    _set_input(inputs, "Transmission Depth", params.get("transmissionDepth"))

    if "subsurfaceRadius" in params:
        _set_input(inputs, "Subsurface Weight", 1.0)
        _set_input(inputs, "Subsurface Method", "Christensen-Burley")
        _set_input(inputs, "Subsurface Radius", list(params["subsurfaceRadius"]))

    _set_input(inputs, "Thin Film Thickness", _scalar(params.get("thinFilmThickness")))
    _set_input(inputs, "Thin Film IOR", params.get("thinFilmIor"))

    for key in _CUSTOM_PROP_KEYS:
        if key in params:
            mat[key] = params[key]

    return mat


def build_checker_material(
    color1, color2, repeat: float | tuple[float, float], *, material: Material | None = None
) -> Material:
    """Build a UV checker material, optionally using an existing material.

    Repeat may be a scalar or separate U/V repeat counts for imported materials.
    """
    mat = material if material is not None else bpy.data.materials.new("Checker")
    ensure_shader_nodes(mat)
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    shader = nodes[cons.ShaderPropName.PRINCIPLED]
    shader.location = (300, 0)
    nodes["Material Output"].location = (600, 0)

    checker = nodes.new("ShaderNodeTexChecker")
    checker.location = (0, 0)
    checker.inputs["Color1"].default_value = color1
    checker.inputs["Color2"].default_value = color2
    checker.inputs["Scale"].default_value = 2.0

    mapping = nodes.new("ShaderNodeMapping")
    mapping.location = (-300, 0)
    repeat_uv = (repeat, repeat) if isinstance(repeat, (int, float)) else repeat
    mapping.inputs["Scale"].default_value = (*repeat_uv, 1.0)
    coordinates = nodes.new("ShaderNodeTexCoord")
    coordinates.location = (-550, 0)

    links.new(coordinates.outputs["UV"], mapping.inputs["Vector"])
    links.new(mapping.outputs["Vector"], checker.inputs["Vector"])
    links.new(checker.outputs["Color"], shader.inputs[cons.NodeInputName.COLOR])
    return mat


# ═══════════════════════════════════════════════════════════════════════
# Assignment
# ═══════════════════════════════════════════════════════════════════════


def _assign_material_slot(obj: Object, mat: Material) -> bool:
    """Assign *mat* to the first material slot of a mesh object.

    Args:
        obj: The mesh object.
        mat: The material to assign.

    Returns:
        True on success.
    """
    if len(obj.material_slots) == 0:
        obj.data.materials.append(None)

    obj.material_slots[0].link = "OBJECT"
    obj.material_slots[0].material = mat
    return True


def assign_material(context: Context, obj: Object, mat: Material) -> bool:
    """Assign *mat* to a Forge object based on its model and geometry type.

    Assigns the material to the first object-level material slot for visual,
    plane, and height-field geometry. Objects without a material target
    (colliders, empties, links, ...) are skipped.

    Args:
        context: The Blender context.
        obj: The object to assign to.
        mat: The material to assign.

    Returns:
        True when the material was assigned, False when skipped.
    """
    model_type = obj.Forge_Model_Type
    if model_type == cons.ModelTypes.VISUAL:
        return _assign_material_slot(obj, mat)

    if model_type in (cons.ModelTypes.PLANE, cons.ModelTypes.HFIELD):
        return _assign_material_slot(obj, mat)

    if model_type == cons.ModelTypes.UNDEFINED and obj.type == "MESH":
        return _assign_material_slot(obj, mat)

    return False
