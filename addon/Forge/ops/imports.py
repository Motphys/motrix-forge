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

import os
import struct
import xml.etree.ElementTree as ET
from collections.abc import Callable
from math import pi, radians
from pathlib import Path

import bpy
from bpy.types import Collection, Context, Node, NodeLinks, Nodes, Object, Scene
from bpy_extras import object_utils
from mathutils import Matrix, Vector

from ..core import constants as cons
from ..core import function as funcs
from ..core import props_data as def_props
from ..core import selection as sel
from ..core.common import ensure_shader_nodes, set_modifier_socket
from ..core.dependency import require_gltf_addon
from ..core.materials import build_checker_material
from ..core.props import (
    ActuatorItem,
    CameraItem,
    CompilerItem,
    ContactItem,
    EqualityItem,
    Forge_Props,
    GeomItem,
    GlobalConfig,
    GlobalItem,
    HeadlightItem,
    InertialItem,
    JointItem,
    LightItem,
    LinkItem,
    MapItem,
    OptionItem,
    QualityItem,
    RgbaItem,
    SensorItem,
    SsgiItem,
    StatisticItem,
    Temp_Props,
    TendonItem,
    TonemappingItem,
    VisualConfig,
)
from ..core.serialization import parse_attr_from_xml, set_props_from_xml
from ..core.utils import AssetsData, AttachData, Link, Sections, WmReportItems

section_order = [
    "include",
    "compiler",
    "option",
    "statistic",
    "visual",
    "default",
    "asset",
    "worldbody",
    "contact",
    "equality",
    "tendon",
    "actuator",
    "sensor",
]
section_order_map = {char: i for i, char in enumerate(section_order)}

assets_order = [
    "texture",
    "material",
    "mesh",
    "hfield",
    "model",
]
assets_order_map = {char: i for i, char in enumerate(assets_order)}


def get_link_name(context: Context, element: ET.Element, links: dict):
    """Recursively collect the names of XML body elements into the links dictionary.
    Iterate over all child nodes of the current element, extract the 'name' attribute
    from each <body> tag, store it in the links dictionary, and recursively process
    child elements.

    Args:
        context: The Blender context.
        element: The XML element to traverse.
        links: Link name dict (name -> name); body names are added here.
    """

    for child in element:
        tag_attrs = dict(child.attrib)
        match child.tag:
            case cons.MJCFTags.BODY:
                if "name" in tag_attrs and tag_attrs["name"] not in links:
                    links[tag_attrs["name"]] = tag_attrs["name"]
                get_link_name(context, child, links)


def parse_link_name(
    context: Context,
    rootElement: ET.Element,
) -> dict:
    """Parse all body link names from the <worldbody> in MJCF XML.
    Find the worldbody element, call get_link_name to recursively collect all body name
    attributes, and return a dictionary containing all link names (always includes "None" entry).

    Args:
        context: The Blender context.
        rootElement: MJCF XML root element.

    Returns:
        A link name dict where both keys and values are body name strings;
        always contains {"None": "None"}.
    """

    links: dict = {"None": "None"}

    element = rootElement.find("worldbody")
    if element is not None:
        get_link_name(context, element, links)

    return links


def get_link_names(context: Context, xml_path: Path) -> dict:
    """Get all available body link names from an MJCF XML file.
    Parse the specified XML file, call parse_link_name to collect all body name attributes
    from <worldbody>, and return a dictionary of all link names. Used by the UI to display
    selectable attach body options in a dropdown list.

    Args:
        context: The Blender context.
        xml_path: Path to the MJCF XML file.

    Returns:
        A link name dict (name -> name); always contains {"None": "None"}.
    """

    xml_path = xml_path.resolve()
    tree = ET.parse(xml_path)

    return parse_link_name(context, tree.getroot())


def set_coll_tag(coll_tag: str, parent_coll: Collection | None = None) -> str:
    """Set collection tag with optional parent prefix.

    Args:
        coll_tag: The collection tag string.
        parent_coll: Optional parent collection whose name is prepended as a prefix.

    Returns:
        The final collection tag, prefixed with the parent collection name if provided.
    """
    if parent_coll:
        return parent_coll.name + "_" + coll_tag
    else:
        return coll_tag


def set_name_by_attrs(obj: Object, tag_attrs: dict, prefix: str = ""):
    """Set object name from XML tag attributes.

    Args:
        obj: The Blender object to rename.
        tag_attrs: Dictionary of XML tag attributes containing an optional "name" key.
        prefix: Optional prefix to prepend to the object name.
    """
    if "name" in tag_attrs:
        if tag_attrs["name"] == obj.name and prefix == "":
            return
        obj.name = funcs.get_unique_object_name(obj, prefix + tag_attrs["name"])
    else:
        obj.name = funcs.get_unique_object_name(obj, prefix + obj.name)


def get_data_object(name: str, prefix: str | None = None):
    """Retrieve a Blender data object by name.

    Args:
        name: The name of the object to retrieve.
        prefix: Optional prefix to prepend to the object name when looking up.

    Returns:
        The Blender object if found, otherwise None.
    """
    prefix_name = prefix + name
    if prefix_name in bpy.data.objects:
        return bpy.data.objects[prefix_name]
    if name in bpy.data.objects:
        return bpy.data.objects[name]
    return None


def get_element(element: ET.Element, elements: list[tuple[int, ET.Element],], count: int = 0, has_parent: bool = False):
    """Recursively parse XML elements into a flat indexed list.

    Args:
        element: The XML element to parse.
        elements: List to append (index, element) tuples to.
        count: Current element index counter.
        has_parent: Whether the element has a parent in the hierarchy.
    """
    local_parent_id = count - 1
    if len(element.items()) > 0:
        elements.append((local_parent_id, element))
        count += 1

    return count


def get_element_iter(
    element: ET.Element, elements: list[tuple[int, ET.Element],], count: int = 0, has_parent: bool = False
):
    """Iteratively parse XML elements into a flat indexed list.

    Args:
        element: The XML element to parse.
        elements: List to append (index, element) tuples to.
        count: Current element index counter.
        has_parent: Whether the element has a parent in the hierarchy.
    """

    local_parent_id = count - 1
    for child in element:
        elements.append([local_parent_id, child])
        count += 1
        if child.tag in ["body", "frame", "replicate", "default"]:
            count = get_element_iter(child, elements, count, True)
    return count


def get_compiler(context: Context, element: ET.Element):
    """Parse compiler settings from a <compiler> XML element.

    Args:
        context: The Blender context.
        element: The XML element containing compiler attributes
                (autolimits, angle, eulerseq, assetdir, meshdir, texturedir).
    """
    data: CompilerItem = context.scene.Forge_GlobalConfig.g_compiler

    for key, value in dict(element.attrib).items():
        if key == "autolimits":
            data.autolimits = funcs.get_active(value)
        if key == "angle":
            data.angle = "DEGREE" if value == "degree" else "RADIAN"
        if key == "eulerseq":
            data.eulerseq = value.upper()
        if key in ["assetdir", "meshdir", "texturedir"]:
            setattr(data, key, value)


def get_option(context: Context, element: ET.Element):
    """Parse option settings from an <option> XML element.

    Args:
        context: The Blender context.
        element: The XML element containing option and flag attributes.
    """
    data: OptionItem = context.scene.Forge_GlobalConfig.g_option

    tag_attrs = dict(element.attrib)
    for prop in def_props.OPTION_PROPS:
        if prop in tag_attrs:
            set_props_from_xml(data, prop, tag_attrs)

    for child in element:
        if child.tag != "flag":
            continue
        tag_attrs = dict(child.attrib)
        for prop in def_props.FLAG_PROPS:
            if prop in tag_attrs:
                set_props_from_xml(data.flag, prop, tag_attrs)


def get_statistic(context: Context, element: ET.Element):
    """Parse statistic settings from a <statistic> XML element.

    Args:
        context: The Blender context.
        element: The XML element containing statistic attributes.
    """
    data: StatisticItem = context.scene.Forge_GlobalConfig.g_statistic

    tag_attrs = dict(element.attrib)
    for prop in def_props.STATISTIC_PROPS:
        if prop in tag_attrs:
            set_props_from_xml(data, prop, tag_attrs)


def get_global(context: Context, element: ET.Element):
    """Parse the global visual settings from a <global> XML element.

    Args:
        context: The Blender context.
        element: The XML element to parse.
    """

    data: GlobalItem = context.scene.Forge_VisualConfig.v_global
    for key, value in dict(element.attrib).items():
        if key == "orthographic":
            data.orthographic = funcs.get_active(value)
        if key in ["fovy", "azimuth", "elevation"]:
            value = radians(float(value))
            setattr(data, key, value)


def get_headlight(context: Context, element: ET.Element):
    """Parse the headlight visual settings from a <headlight> XML element.

    Args:
        context: The Blender context.
        element: The XML element to parse.
    """

    data: HeadlightItem = context.scene.Forge_VisualConfig.v_headlight
    for key, value in dict(element.attrib).items():
        if key == "active":
            data.active = funcs.get_active(value)
        if key in ["ambient", "diffuse", "specular"]:
            setattr(data, key, funcs.parse_float_list(value))


def get_map(context: Context, element: ET.Element):
    """Parse the map visual settings from a <map> XML element.

    Args:
        context: The Blender context.
        element: The XML element to parse.
    """

    data: MapItem = context.scene.Forge_VisualConfig.v_map
    for key, value in dict(element.attrib).items():
        if key in def_props.VISUAL_CONFIG_PROPS[cons.VisualConfigTypes.Map]:
            setattr(data, key, float(value))


def get_rgba(context: Context, element: ET.Element):
    """Parse the RGBA visual settings from a <rgba> XML element.

    Args:
        context: The Blender context.
        element: The XML element to parse.
    """

    data: RgbaItem = context.scene.Forge_VisualConfig.v_rgba
    for key, value in dict(element.attrib).items():
        if key in def_props.VISUAL_CONFIG_PROPS[cons.VisualConfigTypes.Rgba]:
            setattr(data, key, funcs.parse_float_list(value))


def get_quality(context: Context, element: ET.Element):
    """Parse the quality visual settings from a <quality> XML element.

    Args:
        context: The Blender context.
        element: The XML element to parse.
    """

    data: QualityItem = context.scene.Forge_VisualConfig.v_quality
    for key, value in dict(element.attrib).items():
        if key in ["shadowsize", "pointshadowsize"]:
            setattr(data, key, int(value))


def get_ssgi(context: Context, element: ET.Element):
    """Parse the SSGI visual settings from a <ssgi> XML element.

    Args:
        context: The Blender context.
        element: The XML element to parse.
    """

    data: SsgiItem = context.scene.Forge_VisualConfig.v_ssgi
    for key, value in dict(element.attrib).items():
        if key == "active":
            data.active = funcs.get_active(value)
        elif key in ["resolutionscale", "raycount", "stepcount", "gidenoiseoffset", "rraycount", "rdenoiseoffset"]:
            setattr(data, key, int(value))
        elif key in ["thickness", "intensity"]:
            setattr(data, key, float(value))


def get_tonemapping(context: Context, element: ET.Element):
    """Parse the tonemapping visual settings from a <tonemapping> XML element.

    Args:
        context: The Blender context.
        element: The XML element to parse.
    """

    data: TonemappingItem = context.scene.Forge_VisualConfig.v_tonemapping
    for key, value in dict(element.attrib).items():
        if key == "method":
            data.method = value


def get_visual(context: Context, element: ET.Element):
    """Parse visual settings from a <visual> XML element.

    Delegates to specific handlers for each child element type.

    Args:
        context: The Blender context.
        element: The XML element containing visual child elements.
    """

    match element.tag:
        case "global":
            get_global(context, element)
        case "headlight":
            get_headlight(context, element)
        case "map":
            get_map(context, element)
        case "rgba":
            get_rgba(context, element)
        case "quality":
            get_quality(context, element)
        case "ssgi":
            get_ssgi(context, element)
        case "tonemapping":
            get_tonemapping(context, element)


def load_textures(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    attrs: dict,
    images: dict,
    base_dir: Path,
    model: str = "",
):
    """Load textures from XML texture elements and create Blender images.

    Skips KTX2 format textures. Loaded images are stored in the images dictionary.

    Args:
        context: The Blender context.
        report: Report callback function for warnings and errors.
        attrs: Dictionary of texture attributes keyed by name.
        images: Dictionary cache to store loaded Blender images.
        base_dir: Base directory path for resolving texture file paths.
        model: Optional model prefix for image names.
    """
    tex_folder = base_dir
    data: CompilerItem = context.scene.Forge_GlobalConfig.g_compiler
    if data.assetdir:
        tex_folder = Path(base_dir / data.assetdir)
    else:
        tex_folder = Path(base_dir / data.texturedir)

    filepath = Path(tex_folder / attrs["file"])
    _, extension = os.path.splitext(filepath)
    if extension.lower() in ["ktx2"]:
        report({"WARNING"}, f"{extension.lower()} not support in blender")
        return
    if os.path.exists(filepath):
        image = bpy.data.images.load(str(filepath))
        name = attrs["name"]
        image.name = f"{model}{name}"
        if name not in images:
            images[name] = image
            return image
    return


def create_material(
    mat_data: dict,
    layers: list,
    images: dict,
    materials_map: dict,
    model: str = "",
    checker_textures: dict | None = None,
):
    """Create Blender materials from parsed XML material data.

    Builds node-based materials with shader properties including color,
    metallic, roughness, emission, and texture layers (rgb, rgba, normal,
    orm, emissive).

    Args:
        mat_data: Dictionary of material attributes keyed by name.
        layers: Dictionary of material texture layers keyed by material name.
        images: Dictionary of loaded Blender images accessible by name.
        materials_map: Dictionary mapping material names to created Blender materials.
        model: Optional model prefix for material names.
        checker_textures: Procedural checker texture attributes keyed by name.
    """
    checker_textures = checker_textures or {}
    mat = (
        bpy.data.materials[mat_data["name"]]
        if mat_data["name"] in bpy.data.materials
        else bpy.data.materials.new(mat_data["name"])
    )

    name = mat_data["name"]
    mat.name = f"{model}{name}"

    if name in materials_map:
        return

    if name not in materials_map:
        materials_map[name] = mat

    checker_attrs = checker_textures.get(mat_data.get("texture"))
    if checker_attrs is None and mat_data.get("texture") not in images:
        checker_attrs = next(
            (
                checker_textures[tex["texture"]]
                for tex in layers
                if tex["role"] in ["rgb", "rgba"] and tex["texture"] in checker_textures
            ),
            None,
        )
    if checker_attrs is not None:
        tint = funcs.srgb_to_linear(funcs.parse_float_list(mat_data.get("rgba", "1 1 1 1"))[:3])
        colors = []
        for attr, default in (("rgb1", "0.8 0.8 0.8"), ("rgb2", "0.5 0.5 0.5")):
            color = funcs.srgb_to_linear(funcs.parse_float_list(checker_attrs.get(attr, default)))
            colors.append([color[i] * tint[i] for i in range(3)] + [1.0])
        repeat = tuple(funcs.parse_float_list(mat_data.get("texrepeat", "1 1")))
        build_checker_material(*colors, repeat, material=mat)

    ensure_shader_nodes(mat)
    nodes: Nodes = mat.node_tree.nodes
    links: NodeLinks = mat.node_tree.links
    shader = nodes[cons.ShaderPropName.PRINCIPLED]

    linear_color = [1.0, 1.0, 1.0, 1.0]
    metallic = 0.0
    roughness = 0.5
    emission_color = [0.0, 0.0, 0.0, 1.0]

    if "rgba" in mat_data:
        value = funcs.parse_float_list(mat_data["rgba"])
        if len(value) == 3:
            value.append(1.0)
        else:
            if value[3] < 1.0:
                shader.inputs[cons.NodeInputName.ALPHA].default_value = value[3]
        srgb = list(value[:])
        srgb[0:3] = list(funcs.srgb_to_linear(srgb[0:3]))[:]
        linear_color[:4] = srgb[:4]
        shader.inputs[cons.NodeInputName.COLOR].default_value = srgb

    if "metallic" in mat_data:
        metallic = float(mat_data["metallic"])
        shader.inputs[cons.NodeInputName.METALLIC].default_value = metallic

    if "roughness" in mat_data:
        roughness = float(mat_data["roughness"])
        shader.inputs[cons.NodeInputName.ROUGHNESS].default_value = roughness

    if "emission" in mat_data:
        value = funcs.parse_float_list(mat_data["emission"])
        if len(value) == 3:
            value.append(1.0)
        emission_color[:4] = value[:4]
        shader.inputs[cons.NodeInputName.EMISSION].default_value = value

    if "emissionintensity" in mat_data:
        value = float(mat_data["emissionintensity"])
        shader.inputs[cons.NodeInputName.EMISSIONST].default_value = value

    mapping_node = None
    if checker_attrs is not None:
        checker = shader.inputs[cons.NodeInputName.COLOR].links[0].from_node
        mapping_node = checker.inputs["Vector"].links[0].from_node
    elif "texrepeat" in mat_data:
        mapping_node: Node = nodes.new("ShaderNodeMapping")
        value = mat_data["texrepeat"]
        tiling = funcs.parse_float_list(value)
        if len(tiling) == 2:
            tiling.append(1.0)
        mapping_node.inputs["Scale"].default_value = tiling
        uv_node: Node = nodes.new("ShaderNodeTexCoord")
        links.new(uv_node.outputs["UV"], mapping_node.inputs[cons.NodeInputName.VECTOR])

    if mat_data.get("texture") in checker_textures:
        return
    if "texture" in mat_data and mat_data["texture"] in images:
        mix_node: Node = nodes.new("ShaderNodeMix")
        mix_node.data_type = "RGBA"
        mix_node.blend_type = "MULTIPLY"
        mix_node.inputs[cons.NodeInputName.FACTOR].default_value = 1.0
        mix_node.inputs[cons.NodeInputName.COLORB].default_value = linear_color

        tex_node: Node = nodes.new("ShaderNodeTexImage")
        tex_node.image = images[mat_data["texture"]]
        tex_node.image.colorspace_settings.name = "sRGB"
        links.new(tex_node.outputs["Color"], mix_node.inputs[cons.NodeInputName.COLORA])
        links.new(mix_node.outputs["Result"], shader.inputs[cons.NodeInputName.COLOR])
        if mapping_node:
            links.new(mapping_node.outputs[cons.NodeInputName.VECTOR], tex_node.inputs[cons.NodeInputName.VECTOR])

    else:
        if not layers:
            return

        color_tex_name = ""
        color_tex_node = None
        for tex in layers:
            if tex["role"] in ["rgb", "rgba"]:
                if tex["texture"] in checker_textures:
                    continue
                mix_node: Node = nodes.new("ShaderNodeMix")
                mix_node.data_type = "RGBA"
                mix_node.blend_type = "MULTIPLY"
                mix_node.inputs[cons.NodeInputName.FACTOR].default_value = 1.0
                mix_node.inputs[cons.NodeInputName.COLORB].default_value = linear_color

                tex_node: Node = nodes.new("ShaderNodeTexImage")
                color_tex_node = tex_node
                tex_node.image = images[tex["texture"]]
                color_tex_name = tex["texture"]
                tex_node.image.colorspace_settings.name = "sRGB"
                links.new(tex_node.outputs["Color"], mix_node.inputs[cons.NodeInputName.COLORA])
                links.new(mix_node.outputs["Result"], shader.inputs[cons.NodeInputName.COLOR])
                if tex["role"] == "rgba":
                    mix_node: Node = nodes.new("ShaderNodeMath")
                    mix_node.operation = "MULTIPLY"
                    mix_node.use_clamp = True
                    mix_node.inputs[1].default_value = linear_color[3]
                    links.new(tex_node.outputs["Alpha"], mix_node.inputs[0])
                    links.new(mix_node.outputs[0], shader.inputs[cons.NodeInputName.ALPHA])
                if mapping_node:
                    links.new(
                        mapping_node.outputs[cons.NodeInputName.VECTOR], tex_node.inputs[cons.NodeInputName.VECTOR]
                    )
            if tex["role"] == "normal":
                nrm_node: Node = nodes.new("ShaderNodeNormalMap")
                links.new(nrm_node.outputs["Normal"], shader.inputs[cons.NodeInputName.NORMAL])
                tex_node: Node = nodes.new("ShaderNodeTexImage")
                tex_node.image = images[tex["texture"]]
                tex_node.image.colorspace_settings.name = "Non-Color"
                links.new(tex_node.outputs["Color"], nrm_node.inputs[cons.NodeInputName.NCOLOR])
                if mapping_node:
                    links.new(
                        mapping_node.outputs[cons.NodeInputName.VECTOR], tex_node.inputs[cons.NodeInputName.VECTOR]
                    )
            if tex["role"] == "orm":
                svec_node: Node = nodes.new("ShaderNodeSeparateXYZ")
                mix_node: Node = nodes.new("ShaderNodeMath")
                mix_node.operation = "MULTIPLY"
                mix_node.use_clamp = True
                mix_node.inputs[1].default_value = roughness
                links.new(svec_node.outputs["Y"], mix_node.inputs[0])
                links.new(mix_node.outputs[0], shader.inputs[cons.NodeInputName.ROUGHNESS])

                mix_node: Node = nodes.new("ShaderNodeMath")
                mix_node.operation = "MULTIPLY"
                mix_node.use_clamp = True
                mix_node.inputs[1].default_value = metallic
                links.new(svec_node.outputs["Z"], mix_node.inputs[0])
                links.new(mix_node.outputs[0], shader.inputs[cons.NodeInputName.METALLIC])
                tex_node: Node = nodes.new("ShaderNodeTexImage")
                tex_node.image = images[tex["texture"]]
                tex_node.image.colorspace_settings.name = "Non-Color"
                links.new(tex_node.outputs["Color"], svec_node.inputs[cons.NodeInputName.VECTOR])
                if mapping_node:
                    links.new(
                        mapping_node.outputs[cons.NodeInputName.VECTOR], tex_node.inputs[cons.NodeInputName.VECTOR]
                    )
            if tex["role"] == "emissive":
                if color_tex_name == tex["texture"]:
                    mix_node: Node = nodes.new("ShaderNodeMix")
                    mix_node.data_type = "RGBA"
                    mix_node.blend_type = "MULTIPLY"
                    mix_node.inputs[cons.NodeInputName.FACTOR].default_value = 1.0
                    mix_node.inputs[cons.NodeInputName.COLORB].default_value = emission_color

                    links.new(color_tex_node.outputs["Color"], mix_node.inputs[cons.NodeInputName.COLORA])
                    links.new(mix_node.outputs["Result"], shader.inputs[cons.NodeInputName.EMISSION])
                else:
                    mix_node: Node = nodes.new("ShaderNodeMix")
                    mix_node.data_type = "RGBA"
                    mix_node.blend_type = "MULTIPLY"
                    mix_node.inputs[cons.NodeInputName.FACTOR].default_value = 1.0
                    mix_node.inputs[cons.NodeInputName.COLORB].default_value = emission_color

                    tex_node: Node = nodes.new("ShaderNodeTexImage")
                    tex_node.image = images[tex["texture"]]
                    tex_node.image.colorspace_settings.name = "sRGB"
                    links.new(tex_node.outputs["Color"], mix_node.inputs[cons.NodeInputName.COLORA])
                    links.new(mix_node.outputs["Result"], shader.inputs[cons.NodeInputName.EMISSION])
                    if mapping_node:
                        links.new(
                            mapping_node.outputs[cons.NodeInputName.VECTOR],
                            tex_node.inputs[cons.NodeInputName.VECTOR],
                        )


def _import_glb_mesh(context: Context, filepath: str) -> Object:
    """Load the single Mesh object from a GLB asset, ignoring other elements.

    MJCF assets use file-space coordinates and UVs (as does Forge's GLB
    exporter), rather than Blender's glTF scene/UV conversion. The Mesh node's
    transform is baked, and MJCF remains responsible for materials.
    """
    require_gltf_addon("import")
    tracked = ("objects", "meshes", "cameras", "lights", "armatures", "materials", "images", "actions")
    before = {kind: set(getattr(bpy.data, kind)) for kind in tracked}
    temporary = bpy.data.collections.new("_ForgeGLBImport")
    context.scene.collection.children.link(temporary)
    result = None
    try:
        with context.temp_override(collection=temporary):
            status = bpy.ops.import_scene.gltf(
                filepath=filepath,
                import_scene_as_collection=False,
                import_select_created_objects=False,
                import_scene_extras=False,
                import_pack_images=False,
            )
        if "FINISHED" not in status:
            raise RuntimeError(f"GLB import did not finish: {filepath}")
        imported = set(bpy.data.objects) - before["objects"]
        meshes = [obj for obj in imported if obj.type == "MESH"]
        if not meshes:
            raise ValueError(f"GLB asset contains no mesh objects: {filepath}")
        if len(meshes) != 1:
            raise ValueError(f"GLB asset must contain exactly one mesh object (found {len(meshes)}): {filepath}")

        context.view_layer.update()
        depsgraph = context.evaluated_depsgraph_get()
        # Undo glTF Y-up -> Blender Z-up and scene-unit conversion so the
        # resulting mesh matches raw asset coordinates, like OBJ/STL assets.
        unit = context.scene.unit_settings.scale_length
        to_asset = Matrix(((unit, 0, 0, 0), (0, 0, unit, 0), (0, -unit, 0, 0), (0, 0, 0, 1)))
        source = meshes[0]
        mesh = bpy.data.meshes.new_from_object(
            source.evaluated_get(depsgraph), preserve_all_data_layers=True, depsgraph=depsgraph
        )
        mesh.transform(to_asset @ source.matrix_world)
        mesh.materials.clear()
        for polygon in mesh.polygons:
            polygon.material_index = 0
        for layer in mesh.uv_layers:
            for uv in layer.uv:
                uv.vector.y = 1.0 - uv.vector.y
        # Keep only static mesh data, not imported node extras or animation.
        result = bpy.data.objects.new("GLBMeshAsset", mesh)
        temporary.objects.link(result)
        return result
    finally:
        for obj in set(bpy.data.objects) - before["objects"]:
            if obj != result:
                bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(temporary)
        for kind in tracked[1:]:
            datablocks = getattr(bpy.data, kind)
            for datablock in set(datablocks) - before[kind]:
                if datablock.users == 0:
                    datablocks.remove(datablock)


def import_mesh(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    mesh_attrs: dict,
    objects: dict,
    mesh_folder: Path,
    collection: Collection,
    model: str = "",
):
    """Import meshes from files and create Blender mesh data.

     Supports OBJ, STL and GLB file formats. Also handles inline vertex/face data
     by constructing meshes from pydata and applying convex hull.

    Args:
         context: The Blender context.
         report: Report callback function for warnings and errors.
         mesh_attrs: Dictionary of mesh attributes keyed by name.
         objects: Dictionary cache mapping mesh names to created Blender objects.
         mesh_folder: Path to the directory containing mesh files.
         collection: The Blender collection to link created objects into.
         model: Optional model prefix for object names.
    """
    sel.clear_select()
    name = mesh_attrs["name"]
    if "file" in mesh_attrs:
        filepath = str(Path(mesh_folder / mesh_attrs["file"]))
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"Mesh asset {name!r} file not found: {filepath}")
        _, extension = os.path.splitext(filepath)
        if extension.lower() == ".obj":
            bpy.ops.wm.obj_import(
                filepath=filepath,
                filter_glob="*.obj",
                forward_axis="Y",
                up_axis="Z",
            )
            obj = context.active_object
        elif extension.lower() == ".stl":
            bpy.ops.wm.stl_import(filepath=filepath)
            obj = context.active_object
        elif extension.lower() == ".glb":
            obj = _import_glb_mesh(context, filepath)
        else:
            raise ValueError(f"Unsupported mesh format {extension!r} for asset {name!r}: {filepath}")
        funcs.link_collection(obj, collection)

        tag_name = f"{model}{name}"
        obj.data.name = tag_name
        obj.name = tag_name + extension
        obj["FORMAT"] = extension
        if "scale" in mesh_attrs:
            scale = funcs.parse_float_list(mesh_attrs["scale"])
            for ver in obj.data.vertices:
                ver.co *= Vector(scale)
            obj["SCALE"] = scale

        if name not in objects:
            objects[name] = obj
    elif "vertex" in mesh_attrs:
        collection.hide_viewport = False
        vertex_list = funcs.parse_float_list(mesh_attrs["vertex"])
        vertices = [[vertex_list[i], vertex_list[i + 1], vertex_list[i + 2]] for i in range(0, len(vertex_list), 3)]
        if "scale" in mesh_attrs:
            scale = funcs.parse_float_list(mesh_attrs["scale"])
            vertices = [[v[0] * scale[0], v[1] * scale[1], v[2] * scale[2]] for v in vertices]
        edges = []
        faces = []
        if "face" in mesh_attrs:
            face_list = funcs.parse_float_list(mesh_attrs["face"])
            faces = [
                [int(face_list[i]), int(face_list[i + 1]), int(face_list[i + 2])] for i in range(0, len(face_list), 3)
            ]

        tag_name = f"{model}{name}"
        mesh = bpy.data.meshes.new(tag_name)
        mesh.from_pydata(vertices, edges, faces)
        mesh.update()
        obj = bpy.data.objects.new(tag_name, mesh)
        funcs.link_collection(obj, collection)

        if name not in objects:
            objects[name] = obj
        collection.hide_viewport = True

    sel.clear_select()


def load_mesh(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    mesh_attrs: dict,
    objects: dict,
    base_dir: Path,
    parent_coll: Collection | None = None,
    model: str = "",
):
    """Load mesh assets from disk and create corresponding Blender objects.

    Args:
        context: The Blender context.
        report: Report callback function.
        mesh_attrs: Dictionary of mesh attributes.
        objects: Dictionary cache for created objects.
        base_dir: Base directory path for resolving mesh file paths.
        parent_coll: Optional parent collection.
        model: Optional model prefix for object names.
    """

    collection = funcs.get_collection(context, set_coll_tag(cons.CollectionNames.MESH_ASSETS, parent_coll))
    collection.hide_viewport = True
    mesh_folder = base_dir
    data: CompilerItem = context.scene.Forge_GlobalConfig.g_compiler
    if data.assetdir:
        mesh_folder = Path(base_dir / data.assetdir)
    else:
        mesh_folder = Path(base_dir / data.meshdir)

    import_mesh(context, report, mesh_attrs, objects, mesh_folder, collection, model)


def cleanup_mesh_asset_loaders() -> list[str]:
    """Remove the temporary file-mesh loader objects left by MJCF import.

    File-based ``<mesh>`` assets are imported as placeholder objects in the
    hidden mesh-assets collection; geom objects share their mesh data (see
    :func:`import_mesh`).  Once every geom is built the placeholders are
    dead weight in the outliner, so drop the ones whose mesh data found other
    users.  Loaders whose mesh is still unused are kept — they are the only
    carrier of that data.

    Returns:
        Names of the removed placeholder objects.
    """
    removed = []
    # Snapshot the collections: removing an object below must not invalidate
    # the iteration.
    for collection in list(bpy.data.collections):
        if not collection.name.startswith(cons.CollectionNames.MESH_ASSETS):
            continue
        for obj in list(collection.objects):
            model_type = getattr(obj, "Forge_Model_Type", None)
            if model_type not in (None, "", cons.ModelTypes.UNDEFINED):
                continue
            if obj.data is not None and obj.data.users <= 1:
                continue
            removed.append(obj.name)
            bpy.data.objects.remove(obj, do_unlink=True)
    return removed


def import_hfield(
    attrs: dict,
    images: dict,
    tex_folder: Path,
    model: str = "",
):
    """Import height field data from binary files or inline elevation data.

    Reads raw binary height data or inline nrow/ncol/elevation attributes
    and creates Blender images with float buffer pixel data.

    Args:
        attrs: Dictionary of height field attributes keyed by name.
        images: Dictionary cache to store created height field images.
        tex_folder: Path to the directory containing height field files.
        model: Optional model prefix for image names.
    """
    dim = [0] * 2
    tmpList = []
    if "file" in attrs:
        filepath = Path(tex_folder / attrs["file"])

        if os.path.exists(filepath):
            fp = str(filepath)

            size = os.stat(fp).st_size
            chunk = 4

            count = int(size / chunk)

            # Open File
            f = open(fp, "rb")

            for p in range(0, count):
                f.seek(p * chunk)
                bytes_data = f.read(chunk)
                if p < 2:
                    dim[p] = struct.unpack("<i", bytes_data)[0]
                else:
                    value = struct.unpack("<f", bytes_data)[0]
                    tmpList.extend((value, value, value, 1.0))
            f.close()
    else:
        dim[0] = int(attrs["nrow"])
        dim[1] = int(attrs["ncol"])
        for x in attrs["elevation"].strip().split():
            value = float(x)
            tmpList.extend((value, value, value, 1.0))
    fp_tmpList = []
    for p in range(dim[0]):
        fp_tmpList.extend(tmpList[p * dim[1] * 4 : (p + 1) * dim[1] * 4])

    image = bpy.data.images.new(attrs["name"], dim[1], dim[0], float_buffer=True, is_data=True)
    image.pixels = fp_tmpList

    name = attrs["name"]
    image.name = f"{model}{name}"
    if name not in images:
        images[name] = [image, attrs["size"], dim]


def load_hfield(
    context: Context,
    attrs: dict,
    images: dict,
    base_dir: Path,
    model: str = "",
):
    """Load height field assets from disk and create corresponding images.

    Args:
        context: The Blender context.
        attrs: Dictionary of height field attributes.
        images: Dictionary cache for loaded images.
        base_dir: Base directory path for resolving height field file paths.
        model: Optional model prefix for image names.
    """

    tex_folder = base_dir

    data: CompilerItem = context.scene.Forge_GlobalConfig.g_compiler
    if data.assetdir:
        tex_folder = Path(base_dir / data.assetdir)
    else:
        tex_folder = Path(base_dir / data.texturedir)
    import_hfield(attrs, images, tex_folder)


def get_asset(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    forge_props: Forge_Props,
    element: ET.Element,
    defaults: dict,
    assets_data: AssetsData,
    base_dir: Path,
    model: str = "",
    parent_coll: Collection | None = None,
):
    """Get asset data by parsing an <asset> XML element.

    Extracts textures, materials, meshes, hfields, and models from the element,
    then loads textures, creates materials, imports meshes, and loads height fields.

    Args:
        context: The Blender context.
        report: Report callback function.
        forge_props: Main props config.
        element: The XML element containing asset definitions.
        defaults: Default element configurations for attribute inheritance.
        assets_data: AssetsData object to accumulate all parsed resources.
        base_dir: Base directory path for resolving asset file paths.
        model: Optional model prefix for object and material names.
        parent_coll: Optional parent collection.
    """

    attrs = dict(element.attrib)
    env_imported = False
    match element.tag:
        case "texture" if forge_props.import_material:
            if attrs.get("builtin") == "checker" and attrs.get("type") == "2d":
                assets_data.checker_textures[attrs["name"]] = attrs
            elif "file" in attrs and "type" in attrs:
                if "name" not in attrs:
                    root, _ = os.path.splitext(attrs["file"])
                    name = os.path.basename(root)
                    attrs["name"] = name
                if attrs["type"] in ["2d", "envhdr"]:
                    image = load_textures(context, report, attrs, assets_data.images, base_dir, model)
                    if attrs["type"] == "envhdr" and not env_imported:
                        env_imported = True
                        for key in list(bpy.data.worlds):
                            bpy.data.worlds.remove(key)
                        world = bpy.data.worlds.new("World")
                        ensure_shader_nodes(world)
                        main_scene: Scene = context.blend_data.scenes.get(context.scene.Main_Scene)
                        main_scene.world = world
                        world_nodes = world.node_tree.nodes
                        world_links = world.node_tree.links
                        world_nodes.clear()
                        out_node = world_nodes.new("ShaderNodeOutputWorld")
                        shader_node = world_nodes.new("ShaderNodeBackground")
                        hdr_node = world_nodes.new("ShaderNodeTexEnvironment")
                        world_links.new(shader_node.outputs[0], out_node.inputs["Surface"])
                        world_links.new(hdr_node.outputs[0], shader_node.inputs["Color"])
                        hdr_node.image = image
                        # MCP timers/background imports have no active viewport.
                        # This display preference must not block HDR data import.
                        space = getattr(context, "space_data", None)
                        if isinstance(space, bpy.types.SpaceView3D):
                            space.shading.use_scene_world = True

        case "material" if forge_props.import_material:
            if "class" in attrs:
                parse_inherit_attrs(defaults, attrs, cons.MJCFTags.MATERIAL, attrs["class"])
            else:
                parse_inherit_attrs(defaults, attrs, cons.MJCFTags.MATERIAL)

            layers = []
            for layer in element:
                layer_attrs = dict(layer.attrib)
                layers.append(layer_attrs)

            create_material(
                attrs, layers, assets_data.images, assets_data.materials_map, model, assets_data.checker_textures
            )
        case "mesh":
            if "class" in attrs:
                parse_inherit_attrs(defaults, attrs, cons.MJCFTags.MESH, attrs["class"])
            else:
                parse_inherit_attrs(defaults, attrs, cons.MJCFTags.MESH)

            if "name" not in attrs:
                root, _ = os.path.splitext(attrs["file"])
                name = os.path.basename(root)
                attrs["name"] = name

            load_mesh(context, report, attrs, assets_data.objects, base_dir, parent_coll, model)
        case "hfield":
            if "name" not in attrs:
                root, _ = os.path.splitext(attrs["file"])
                name = os.path.basename(root)
                attrs["name"] = name

            load_hfield(context, attrs, assets_data.images, base_dir, model)


def get_sub_default(
    element: ET.Element,
    defaults: dict,
    parent: str,
):
    """Recursively parse nested <default> XML elements into the defaults dictionary.

    Args:
        element: The XML element to parse.
        defaults: The defaults dictionary to populate.
        parent: The parent class name for inheritance.
    """

    attrs = dict(element.attrib)
    class_childs = {}
    class_childs["parent"] = parent
    for child in element:
        if child.tag == "default":
            get_sub_default(child, defaults, attrs["class"])
        else:
            tag_attrs = dict(child.attrib)
            class_childs[child.tag] = tag_attrs
    defaults[attrs["class"]] = class_childs


def get_default(element: ET.Element, defaults: dict):
    """Parse the <default> XML element and build the defaults dictionary.

    Args:
        element: The XML element to parse.
        defaults: The defaults dictionary to populate.
    """

    for child in element:
        if child.tag == "default":
            get_sub_default(child, defaults, "root")
        else:
            tag_attrs = dict(child.attrib)
            defaults[child.tag] = tag_attrs


def parse_inherit_attrs(defaults: dict, tag_attrs: dict, tag: str, name: str = "root", recursive: bool = False):
    """Apply inherited default attributes from a class definition to the given tag attributes.

    Args:
        defaults: The defaults dictionary containing class definitions.
        tag_attrs: The tag attributes to populate with inherited values.
        tag: The XML tag name to inherit from.
        name: The class name to inherit from (defaults to "root").
        recursive: Whether to recursively inherit from parent classes.
    """

    if name != "root":
        if name not in defaults:
            return
        df_tag_attrs = defaults[name]
        if tag in df_tag_attrs:
            for key, attr in df_tag_attrs[tag].items():
                if key not in tag_attrs:
                    tag_attrs[key] = attr

        if "parent" in df_tag_attrs and recursive:
            parse_inherit_attrs(defaults, tag_attrs, tag, df_tag_attrs["parent"], recursive)
    else:
        if tag not in defaults:
            return
        for key, attr in defaults[tag].items():
            if key not in tag_attrs:
                tag_attrs[key] = attr


def parse_defaults(defaults: dict):
    """Resolve inherited parent attributes in default element definitions.


    Args:
        defaults: Dictionary of default element configurations.
    """
    for key, value in defaults.items():
        if "parent" not in value:
            continue
        parent = value["parent"]
        if parent == "root":
            for tag, tag_attrs in value.items():
                if tag == "parent":
                    continue
                if tag in defaults:
                    for key, attr in defaults[tag].items():
                        if key not in tag_attrs:
                            tag_attrs[key] = attr
        else:
            for tag, tag_attrs in value.items():
                if tag == "parent":
                    continue
                parse_inherit_attrs(defaults, tag_attrs, tag, parent, recursive=True)


def set_local_matrix(obj: Object, axis: Vector):
    """Set the local matrix of an object to align its Z axis with the given direction vector.

    Args:
        obj: The Blender object to modify.
        axis: The direction vector for the Z axis alignment.
    """

    z = axis.normalized()
    x = Vector.cross(axis, Vector((0, 1, 0))).normalized()
    if x.length_squared == 0:
        x = Vector((1, 0, 0))
    y = Vector.cross(z, x).normalized()
    obj.matrix_local = Matrix((x[:], y[:], z[:])).transposed().to_4x4()


def set_local_transform(obj: Object, tag_attrs: dict):
    """Set the local position and rotation of an object from XML tag attributes.

    Supports quaternion, axis-angle, euler, xyaxes, zaxis, dir, and axis rotation formats.

    Args:
        obj: The Blender object to modify.
        tag_attrs: Dictionary of XML tag attributes containing transform data.
    """

    data: CompilerItem = bpy.context.scene.Forge_GlobalConfig.g_compiler

    if "quat" in tag_attrs:
        obj.rotation_mode = "QUATERNION"
        obj.rotation_quaternion = funcs.parse_float_list(tag_attrs["quat"])
        obj.rotation_mode = "XYZ"
    elif "axisangle" in tag_attrs:
        axisangle = Vector(funcs.parse_float_list(tag_attrs["axisangle"]))
        angle = radians(axisangle[3]) if data.angle == "DEGREE" else axisangle[3]
        obj.matrix_local = Matrix.Rotation(angle, 4, axisangle[0:3])
    elif "euler" in tag_attrs:
        euler = funcs.parse_float_list(tag_attrs["euler"])
        euler = Vector([radians(e) for e in euler]) if data.angle == "DEGREE" else euler
        obj.rotation_mode = data.eulerseq.upper()
        obj.rotation_euler = euler
    elif "xyaxes" in tag_attrs:
        axis = funcs.parse_float_list(tag_attrs["xyaxes"])
        axis = [Vector(axis[0:3]), Vector(axis[3:])]

        x = axis[0].normalized()
        y = axis[1].normalized()
        z = Vector.cross(x, y).normalized()
        obj.matrix_local = Matrix((x[:], y[:], z[:])).transposed().to_4x4()
    elif "zaxis" in tag_attrs:
        axis = Vector(funcs.parse_float_list(tag_attrs["zaxis"]))
        set_local_matrix(obj, axis)
    elif "dir" in tag_attrs:
        axis = Vector(funcs.parse_float_list(tag_attrs["dir"])) * -1.0
        set_local_matrix(obj, axis)
    elif "axis" in tag_attrs:
        axis = Vector(funcs.parse_float_list(tag_attrs["axis"]))
        set_local_matrix(obj, axis)
    else:
        obj.rotation_euler = (0.0, 0.0, 0.0)
    obj.location = funcs.parse_float_list(tag_attrs["pos"]) if "pos" in tag_attrs else (0.0, 0.0, 0.0)


def add_camera(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    defaults: dict,
    tag_attrs: dict,
    parent_obj: Object | None = None,
    childClass: str | None = None,
    prefix: str = "",
):
    """Add a camera element from XML tag attributes.

    Parses class inheritance, camera type (perspective/orthographic), mode,
    transform, field of view, and target body reference.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the camera into.
        defaults: The defaults dictionary for attribute inheritance.
        tag_attrs: Dictionary of XML tag attributes for the camera.
        parent_obj: Optional parent object.
        childClass: Optional child class name for attribute inheritance.
        prefix: Optional prefix for the object name.
    """
    if "class" in tag_attrs:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.CAMERA, tag_attrs["class"])

    elif childClass:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.CAMERA, childClass)
    else:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.CAMERA)

    type = cons.CameraTypes.PERSPECTIVE
    if "orthographic" in tag_attrs:
        type = cons.CameraTypes.ORTHOGRAPHIC if tag_attrs["orthographic"] == "true" else type
    if "projection" in tag_attrs:
        type = tag_attrs["projection"].upper()

    mode = tag_attrs["mode"].upper() if "mode" in tag_attrs else cons.TargetModes.FIXED
    mode = mode if mode in cons.LC_Modes else mode

    obj = funcs.add_camera(context, report, collection, type, mode, parent_obj)
    set_name_by_attrs(obj, tag_attrs, prefix)

    set_local_transform(obj, tag_attrs)

    if "fovy" in tag_attrs:
        if type == cons.CameraTypes.ORTHOGRAPHIC:
            obj.data.ortho_scale = float(tag_attrs["fovy"])
        else:
            obj.data.angle_y = radians(float(tag_attrs["fovy"]))

    data: CameraItem = obj.Forge_Camera
    if "mode" in tag_attrs:
        data.mode = tag_attrs["mode"].upper()
    if data.mode in [cons.TargetModes.TARGETBODY, cons.TargetModes.TARGETBODYCOM]:
        if "target" in tag_attrs:
            target_name = tag_attrs["target"]
            if target_name in bpy.data.objects:
                data.target = bpy.data.objects[target_name]
            else:
                obj["target"] = target_name


def get_power(c: float, pf: float = 683, isSun: bool = False):
    """Convert light intensity to Blender power units (watts).

    Args:
        c: The intensity value to convert.
        pf: The luminous efficacy in lumens per watt (default 683).
        isSun: Whether the light is a sun type (uses division instead of multiplication).

    Returns:
        The converted power value in watts.
    """

    if isSun:
        return c / pf / pi

    return c * 12.57 / pf


def add_light(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    defaults: dict,
    tag_attrs: dict,
    parent_obj: Object | None = None,
    childClass: str | None = None,
    prefix: str = "",
):
    """Add a light element from XML tag attributes.

    Parses class inheritance, light type (spot/directional/point), mode,
    transform, color, intensity, range, spot angles, and shadow settings.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the light into.
        defaults: The defaults dictionary for attribute inheritance.
        tag_attrs: Dictionary of XML tag attributes for the light.
        parent_obj: Optional parent object.
        childClass: Optional child class name for attribute inheritance.
        prefix: Optional prefix for the object name.
    """
    if "class" in tag_attrs:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.LIGHT, tag_attrs["class"])

    elif childClass:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.LIGHT, childClass)

    else:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.LIGHT)

    type = tag_attrs["type"].upper() if "type" in tag_attrs else cons.LightTypes.SPOT
    if "directional" in tag_attrs and tag_attrs["directional"] == "true":
        type = cons.LightTypes.DIRECTIONAL

    mode = tag_attrs["mode"].upper() if "mode" in tag_attrs else cons.TargetModes.FIXED
    mode = mode if mode in cons.LC_Modes else mode

    obj = funcs.add_light(context, report, collection, type, mode, parent_obj)
    set_name_by_attrs(obj, tag_attrs, prefix)

    set_local_transform(obj, tag_attrs)

    if "diffuse" in tag_attrs:
        obj.data.color = funcs.parse_float_list(tag_attrs["diffuse"])
    if "intensity" in tag_attrs:
        power = get_power(float(tag_attrs["intensity"]), isSun=obj.data.type == "SUN")
        obj.data.energy = power

    if type != cons.LightTypes.DIRECTIONAL and "range" in tag_attrs:
        obj.data.cutoff_distance = float(tag_attrs["range"])

    if type == cons.LightTypes.SPOT:
        if "cutoff" in tag_attrs:
            cutoff = float(tag_attrs["cutoff"])
            angle = radians(cutoff * 2.0)
            obj.data.spot_size = angle
            if "innerangle" in tag_attrs and cutoff > 0.0:
                obj.data.spot_blend = 1.0 - (float(tag_attrs["innerangle"]) / cutoff)
    if type == cons.LightTypes.POINT:
        pass
    if "castshadow" in tag_attrs:
        obj.data.use_shadow = True if tag_attrs["castshadow"] == "true" else False

    data: LightItem = obj.Forge_Light
    data.mode = mode
    if data.mode in [cons.TargetModes.TARGETBODY, cons.TargetModes.TARGETBODYCOM]:
        if "target" in tag_attrs:
            target_name = tag_attrs["target"]
            if target_name in bpy.data.objects:
                data.target = bpy.data.objects[target_name]
            else:
                obj["target"] = target_name


def set_geom_props(obj: Object, tag_attrs: dict):
    """Set geometry properties on an object from XML tag attributes.

    Args:
        obj: The Blender object whose geometry properties to set.
        tag_attrs: Dictionary of XML tag attributes.
    """

    data: GeomItem = obj.Forge_Geometry
    for prop in def_props.GEOM_PROPS:
        if prop in tag_attrs:
            value = parse_attr_from_xml(data, prop, tag_attrs)
            if isinstance(value, list):
                attr = getattr(data, prop)
                for i in range(len(value)):
                    attr[i] = value[i]
            else:
                setattr(data, prop, value)


def add_mesh(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    assets_data: AssetsData,
    tag_attrs: dict,
    parent_obj: Object | None = None,
    prefix: str = "",
):
    """Add a mesh geometry element from XML tag attributes.

    Creates an object from an existing mesh asset, sets its model type,
    applies parent transform, assigns material, and sets geometry properties.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the mesh into.
        assets_data: AssetsData object containing loaded mesh objects.
        tag_attrs: Dictionary of XML tag attributes for the mesh.
        parent_obj: Optional parent object.
        prefix: Optional prefix for the object name.
    """

    object_utils.object_data_add(context, assets_data.objects[tag_attrs["mesh"]].data)
    obj = context.active_object
    obj.Forge_Model_Type = cons.ModelTypes.VISUAL
    obj.Forge_Geometry.type = tag_attrs.get("type", "mesh").upper()
    if cons.CollectionNames.COLLIDER in collection.name or "COL_" in collection.name or tag_attrs.get("group") == "3":
        obj.Forge_Model_Type = cons.ModelTypes.COLLIDER
        obj.display_type = "WIRE"
    set_name_by_attrs(obj, tag_attrs, prefix)

    funcs.link_collection(obj, collection)

    if parent_obj:
        obj.parent = parent_obj
        obj.matrix_local = obj.matrix_parent_inverse @ obj.matrix_local
        obj.matrix_parent_inverse = Matrix.Identity(4)
        obj.location = (0, 0, 0)

    scene = context.scene
    forge_props: Forge_Props = bpy.data.scenes[scene.Main_Scene].Forge_Props

    if "material" in tag_attrs and forge_props.import_material:
        if len(obj.material_slots) == 0:
            bpy.ops.object.material_slot_add()
            obj.material_slots[0].material = assets_data.materials_map[tag_attrs["material"]]
    set_local_transform(obj, tag_attrs)
    set_geom_props(obj, tag_attrs)


def add_geometry(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    assets_data: AssetsData,
    tag_attrs: dict,
    type: str,
    parent_obj: Object | None = None,
    prefix: str = "",
):
    """Add a geometry element from XML tag attributes.

    Creates primitive geometry (sphere, box, capsule, cylinder) with size,
    fromto positioning, material assignment, and geometry properties.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the geometry into.
        assets_data: AssetsData object containing material mappings.
        tag_attrs: Dictionary of XML tag attributes for the geometry.
        type: The geometry type string (e.g. SPHERE, BOX, CAPSULE, CYLINDER).
        parent_obj: Optional parent object.
        prefix: Optional prefix for the object name.
    """
    obj = funcs.add_geometry(context, report, collection, type, parent_obj)

    if "fromto" in tag_attrs and type != cons.GeometryTypes.SPHERE:
        fromto = funcs.parse_float_list(tag_attrs["fromto"])
        fromto = [Vector(fromto[0:3]), Vector(fromto[3:])]
        ray = fromto[1] - fromto[0]
        height = ray.length * 0.5
        radius = funcs.parse_float_list(tag_attrs["size"])[0]
        size = radius
        match type:
            case cons.GeometryTypes.CAPSULE:
                size = Vector((radius, height))
            case cons.GeometryTypes.CYLINDER:
                size = Vector((radius, height))
            case cons.GeometryTypes.BOX:
                size = Vector((radius, radius, height))

        funcs.set_geometry_size(obj, type, size, False)
        axis = ray.normalized()
        set_local_matrix(obj, axis)
        if "pos" not in tag_attrs:
            obj.location = (fromto[1] + fromto[0]) * 0.5
        else:
            obj.location = funcs.parse_float_list(tag_attrs["pos"])
    else:
        if "size" in tag_attrs:
            size = funcs.parse_float_list(tag_attrs["size"])
            size = size[0] if type == cons.GeometryTypes.SPHERE else Vector(size)
            funcs.set_geometry_size(obj, type, size, False)
            set_local_transform(obj, tag_attrs)

    set_name_by_attrs(obj, tag_attrs, prefix)

    scene = context.scene
    forge_props: Forge_Props = bpy.data.scenes[scene.Main_Scene].Forge_Props

    if "material" in tag_attrs and forge_props.import_material:
        modifier_name = cons.GeometryShapeModifiers[obj.Forge_Geometry.type]
        if len(obj.data.materials) == 0:
            obj.data.materials.append(None)
            obj.material_slots[0].link = "OBJECT"

        obj.material_slots[0].material = assets_data.materials_map[tag_attrs["material"]]
        if modifier_name in obj.modifiers:
            obj.modifiers[modifier_name].node_group.interface_update(context)
    set_geom_props(obj, tag_attrs)


def add_collider(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    assets_data: AssetsData,
    tag_attrs: dict,
    type: str,
    parent_obj: Object | None = None,
    prefix: str = "",
):
    """Add a collider element from XML tag attributes.

    Creates collider geometry with size, fromto positioning, and geometry properties.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the collider into.
        assets_data: AssetsData object containing material mappings.
        tag_attrs: Dictionary of XML tag attributes for the collider.
        type: The geometry type string (e.g. SPHERE, BOX, CAPSULE, CYLINDER).
        parent_obj: Optional parent object.
        prefix: Optional prefix for the object name.
    """
    obj = funcs.add_collider(context, report, collection, type, parent_obj)

    if "fromto" in tag_attrs and type != cons.GeometryTypes.SPHERE:
        fromto = funcs.parse_float_list(tag_attrs["fromto"])
        fromto = [Vector(fromto[0:3]), Vector(fromto[3:])]
        ray = fromto[1] - fromto[0]
        height = ray.length * 0.5
        radius = funcs.parse_float_list(tag_attrs["size"])[0]
        size = radius
        match type:
            case cons.GeometryTypes.CAPSULE:
                size = Vector((radius, height))
            case cons.GeometryTypes.CYLINDER:
                size = Vector((radius, height))
            case cons.GeometryTypes.BOX:
                size = Vector((radius, radius, height))

        funcs.set_collider_size(obj, type, size, False)
        axis = ray.normalized()
        set_local_matrix(obj, axis)
        if "pos" not in tag_attrs:
            obj.location = (fromto[1] + fromto[0]) * 0.5
        else:
            obj.location = funcs.parse_float_list(tag_attrs["pos"])
    else:
        if "size" in tag_attrs:
            size = funcs.parse_float_list(tag_attrs["size"])
            size = size[0] if type == cons.GeometryTypes.SPHERE else Vector(size)
            funcs.set_collider_size(obj, type, size, False)
            set_local_transform(obj, tag_attrs)

    set_name_by_attrs(obj, tag_attrs, prefix)
    set_geom_props(obj, tag_attrs)


def add_plane(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    assets_data: AssetsData,
    tag_attrs: dict,
    prefix: str = "",
):
    """Add a plane element from XML tag attributes.

    Creates a plane object with size and material settings applied through modifiers.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the plane into.
        assets_data: AssetsData object containing material mappings.
        tag_attrs: Dictionary of XML tag attributes for the plane.
        prefix: Optional prefix for the object name.
    """
    obj = funcs.add_plane(context, report, collection)
    modifier_name = cons.AdditionalShapeModifiers[obj.Forge_Model_Type]
    if modifier_name in obj.modifiers:
        PS = cons.ModifierSockets.Plane
        if "size" in tag_attrs:
            size = Vector(funcs.parse_float_list(tag_attrs["size"]))
            set_modifier_socket(obj.modifiers[modifier_name], PS.HALF_SIZE_X, size.x if size.x > 0.0 else 100.0)
            set_modifier_socket(obj.modifiers[modifier_name], PS.HALF_SIZE_Y, size.y if size.y > 0.0 else 100.0)
            set_modifier_socket(obj.modifiers[modifier_name], PS.INFINITE, True)

        scene = context.scene
        forge_props: Forge_Props = bpy.data.scenes[scene.Main_Scene].Forge_Props

        if "material" in tag_attrs and forge_props.import_material:
            if len(obj.data.materials) == 0:
                obj.data.materials.append(None)
                obj.material_slots[0].link = "OBJECT"

            obj.material_slots[0].material = assets_data.materials_map[tag_attrs["material"]]

        obj.modifiers[modifier_name].node_group.interface_update(context)

    set_name_by_attrs(obj, tag_attrs, prefix)

    set_local_transform(obj, tag_attrs)
    set_geom_props(obj, tag_attrs)


def add_hfield(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    assets_data: AssetsData,
    tag_attrs: dict,
    prefix: str = "",
):
    """Add a height field element from XML tag attributes.

    Sets up height field modifier parameters including grid dimensions,
    size radii, elevation, base height, and the height map image.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the height field into.
        assets_data: AssetsData object containing loaded height field images.
        tag_attrs: Dictionary of XML tag attributes for the height field.
        prefix: Optional prefix for the object name.
    """
    obj = funcs.add_height_field(context, report, collection)
    modifier_name = cons.AdditionalShapeModifiers[obj.Forge_Model_Type]

    if modifier_name in obj.modifiers:
        S = cons.ModifierSockets.HField
        if "hfield" in tag_attrs:
            image, size, dim = assets_data.images[tag_attrs["hfield"]]
            set_modifier_socket(obj.modifiers[modifier_name], S.NROW, dim[0])
            set_modifier_socket(obj.modifiers[modifier_name], S.NCOL, dim[1])

            size = funcs.parse_float_list(size)
            set_modifier_socket(obj.modifiers[modifier_name], S.RADIUS_X, size[0])
            set_modifier_socket(obj.modifiers[modifier_name], S.RADIUS_Y, size[1])
            set_modifier_socket(obj.modifiers[modifier_name], S.ELEVATION_Z, size[2])
            set_modifier_socket(obj.modifiers[modifier_name], S.BASE_Z, size[3])
            set_modifier_socket(obj.modifiers[modifier_name], S.USE_HEIGHT_MAP, True)
            set_modifier_socket(obj.modifiers[modifier_name], S.HEIGHT_MAP, image)

        scene = context.scene
        forge_props: Forge_Props = bpy.data.scenes[scene.Main_Scene].Forge_Props

        if "material" in tag_attrs and forge_props.import_material:
            if len(obj.data.materials) == 0:
                obj.data.materials.append(None)
                obj.material_slots[0].link = "OBJECT"

            obj.material_slots[0].material = assets_data.materials_map[tag_attrs["material"]]

        obj.modifiers[modifier_name].node_group.interface_update(context)
    set_name_by_attrs(obj, tag_attrs, prefix)

    set_local_transform(obj, tag_attrs)
    set_geom_props(obj, tag_attrs)


def add_geom(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    defaults: dict,
    assets_data: AssetsData,
    tag_attrs: dict,
    parent_obj: Object | None = None,
    childClass: str | None = None,
    parent_coll: Collection | None = None,
    prefix: str = "",
):
    """Add a geom element from XML tag attributes.

    Dispatches to add_mesh, add_hfield, add_plane, add_collider, or add_geometry
    based on the geometry type. Collider group (group=3) objects are placed in
    a separate collider collection.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the geom into.
        assets_data: AssetsData object containing assets and defaults.
        tag_attrs: Dictionary of XML tag attributes for the geom.
        parent_obj: Optional parent object.
        childClass: Optional child class name for attribute inheritance.
        parent_coll: Optional parent collection.
        prefix: Optional prefix for the object name.
    """
    if "class" in tag_attrs:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.GEOM, tag_attrs["class"])

    elif childClass:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.GEOM, childClass)

    else:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.GEOM)

    type = tag_attrs["type"].upper() if "type" in tag_attrs else cons.GeometryTypes.SPHERE
    match type:
        case cons.GeometryTypes.MESH | cons.GeometryTypes.SDF:
            if "group" in tag_attrs and int(tag_attrs["group"]) == 3 and parent_obj:
                collection = funcs.get_collection(
                    context, set_coll_tag(cons.CollectionNames.COLLIDER, parent_coll), parent_coll
                )
            add_mesh(context, report, collection, assets_data, tag_attrs, parent_obj, prefix)
        case cons.ModelTypes.HFIELD:
            add_hfield(context, report, collection, assets_data, tag_attrs, prefix)
        case cons.ModelTypes.PLANE:
            add_plane(context, report, collection, assets_data, tag_attrs, prefix)
        case _:
            if "group" in tag_attrs and int(tag_attrs["group"]) == 3:
                if parent_obj:
                    collection = funcs.get_collection(
                        context, set_coll_tag(cons.CollectionNames.COLLIDER, parent_coll), parent_coll
                    )
                add_collider(context, report, collection, assets_data, tag_attrs, type, parent_obj, prefix)
            else:
                add_geometry(context, report, collection, assets_data, tag_attrs, type, parent_obj, prefix)


def add_joint(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    defaults: dict,
    tag_attrs: dict,
    parent_obj: Object | None = None,
    childClass: str | None = None,
    prefix: str = "",
):
    """Add a joint element from XML tag attributes.

    Creates a joint object with type (hinge, ball, slide, free), transform,
    and joint-specific properties. Converts degree-range values to radians
    when the compiler is set to DEGREE mode.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the joint into.
        defaults: The defaults dictionary for attribute inheritance.
        tag_attrs: Dictionary of XML tag attributes for the joint.
        parent_obj: Optional parent object.
        childClass: Optional child class name for attribute inheritance.
        prefix: Optional prefix for the object name.
    """
    if "class" in tag_attrs:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.JOINT, tag_attrs["class"])

    elif childClass:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.JOINT, childClass)

    else:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.JOINT)

    if tag_attrs:
        type = tag_attrs["type"].upper() if "type" in tag_attrs else cons.JointTypes.HINGE
        obj = funcs.add_joint(context, report, collection, type, parent_obj)
        set_name_by_attrs(obj, tag_attrs, prefix)

        set_local_transform(obj, tag_attrs)

        compiler: CompilerItem = context.scene.Forge_GlobalConfig.g_compiler
        data: JointItem = obj.Forge_Joint
        for prop in def_props.JOINT_TYPE_PROPS[type]:
            if prop in tag_attrs:
                set_props_from_xml(data, prop, tag_attrs)
        if data.type in [cons.JointTypes.BALL, cons.JointTypes.HINGE]:
            if compiler.angle == "DEGREE":
                data.range = [radians(v) for v in data.range]


def add_site(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    defaults: dict,
    tag_attrs: dict,
    parent_obj: Object | None = None,
    childClass: str | None = None,
    prefix: str = "",
):
    """Add a site element from XML tag attributes.

    Creates a site object with type (sphere, box, capsule, cylinder), size,
    transform, and site-specific geometry properties.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the site into.
        defaults: The defaults dictionary for attribute inheritance.
        tag_attrs: Dictionary of XML tag attributes for the site.
        parent_obj: Optional parent object.
        childClass: Optional child class name for attribute inheritance.
        prefix: Optional prefix for the object name.
    """
    if "class" in tag_attrs:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.SITE, tag_attrs["class"])

    elif childClass:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.SITE, childClass)

    else:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.SITE)

    type = tag_attrs["type"].upper() if "type" in tag_attrs else cons.GeometryTypes.SPHERE
    obj = funcs.add_site(context, report, collection, type, parent_obj)
    if "size" in tag_attrs:
        size = (
            float(tag_attrs["size"])
            if type == cons.GeometryTypes.SPHERE
            else Vector(funcs.parse_float_list(tag_attrs["size"]))
        )
        funcs.set_site_size(obj, type, size, False)

    set_name_by_attrs(obj, tag_attrs, prefix)

    set_local_transform(obj, tag_attrs)

    data: GeomItem = obj.Forge_Geometry
    for prop in def_props.SITE_PROPS:
        if prop in tag_attrs:
            set_props_from_xml(data, prop, tag_attrs)


def add_link(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    tag_attrs: dict,
    parent_obj: Object | None = None,
    prefix: str = "",
):
    """Add a link (body) element from XML tag attributes.

    Creates a link object with transform and link-specific properties.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the body into.
        tag_attrs: Dictionary of XML tag attributes for the link.
        parent_obj: Optional parent object.
        prefix: Optional prefix for the object name.

    Returns:
        The created Blender object representing the link.
    """
    obj = funcs.add_link(context, report, collection, parent_obj)
    set_name_by_attrs(obj, tag_attrs, prefix)

    set_local_transform(obj, tag_attrs)
    data: LinkItem = obj.Forge_Link
    for prop in def_props.LINK_PROPS:
        if prop in tag_attrs:
            set_props_from_xml(data, prop, tag_attrs)

    return obj


def add_frame(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    tag_attrs: dict,
    parent_obj: Object | None = None,
    prefix: str = "",
):
    """Add a frame element from XML tag attributes.

    Creates a frame object with transform.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the frame into.
        tag_attrs: Dictionary of XML tag attributes for the frame.
        parent_obj: Optional parent object.
        prefix: Optional prefix for the object name.

    Returns:
        The created Blender object representing the frame.
    """
    obj = funcs.add_frame(context, report, collection, parent_obj)
    set_name_by_attrs(obj, tag_attrs, prefix)

    set_local_transform(obj, tag_attrs)

    return obj


def add_replicate(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    tag_attrs: dict,
    parent_obj: Object | None = None,
    prefix: str = "",
):
    """Add a replicate element from XML tag attributes.

    Creates a replicate object that duplicates its children a given number
    of times with specified separation, offset, and rotation.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the replicate into.
        tag_attrs: Dictionary of XML tag attributes for the replicate.
        parent_obj: Optional parent object.
        prefix: Optional prefix for the object name.

    Returns:
        The created Blender object representing the replicate.
    """
    count = int(tag_attrs["count"]) if "count" in tag_attrs else def_props.REPLICATE_PROPS_DEFAULT["count"]
    sep = tag_attrs["sep"] if "sep" in tag_attrs else def_props.REPLICATE_PROPS_DEFAULT["sep"]
    offset = (
        funcs.parse_float_list(tag_attrs["offset"])
        if "offset" in tag_attrs
        else def_props.REPLICATE_PROPS_DEFAULT["offset"]
    )
    euler = (
        funcs.parse_float_list(tag_attrs["euler"])
        if "euler" in tag_attrs
        else def_props.REPLICATE_PROPS_DEFAULT["euler"]
    )
    data: CompilerItem = context.scene.Forge_GlobalConfig.g_compiler
    if data.angle == "DEGREE":
        euler = [radians(v) for v in euler]

    obj = funcs.add_replicate(context, report, count, sep, offset, euler, collection, parent_obj=parent_obj)
    set_name_by_attrs(obj, tag_attrs, prefix)

    return obj


def get_attch_scene(scene_tag: str):
    """Get or create a Blender scene associated with the attachment.
    Return the existing scene if one with the given name already exists,
    otherwise create a new scene.

    Args:
        scene_tag: The scene name.

    Returns:
        The retrieved or created Blender scene.
    """

    if scene_tag in bpy.data.scenes:
        return bpy.data.scenes[scene_tag]
    else:
        return bpy.data.scenes.new(scene_tag)


def add_attach(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    attachs: dict[str, str],
    tag_attrs: dict,
    root_file_path: str,
    parent_obj: Object | None = None,
):
    """Process an <attach> sub-model reference in Blender.
    Look up the sub-model definition by the 'model' attribute, parse its XML file,
    decide whether to load the sub-model tree in link mode or world mode based on
    the presence of the 'body' attribute, then call funcs.add_attach to attach the
    sub-model to the current scene.

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the attach into.
        attachs: Dictionary mapping model names to (identifier, file) pairs.
        tag_attrs: Dictionary of XML tag attributes for the attach tag
                   (must contain "model", optionally "body" and "prefix").
        root_file_path: Root file path for resolving relative sub-model paths.
        parent_obj: Optional parent Blender object.
    """

    model = tag_attrs["model"]
    identifier, file = attachs[model]

    raw_attach = AttachData()
    raw_attach.file = file if os.path.exists(file) else Path(root_file_path, file).resolve()
    raw_attach.model = model
    raw_attach.link = tag_attrs["body"] if "body" in tag_attrs else ""
    raw_attach.prefix = tag_attrs["prefix"]

    current_scene = context.window.scene
    scene = get_attch_scene(identifier)
    context.window.scene = scene

    model_coll = funcs.get_collection(context, identifier)
    model_coll.hide_viewport = False

    model_prefix = identifier.replace(".", "_") + "_"

    sel.clear_select()
    link: Object = None
    if raw_attach.link != "":
        if raw_attach.prefix + raw_attach.link in bpy.data.objects:
            link = bpy.data.objects[raw_attach.prefix + raw_attach.link]
        elif model_prefix + raw_attach.link in bpy.data.objects:
            link = bpy.data.objects[model_prefix + raw_attach.link]
        if link is None:
            report({"WARNING"}, f"Attach body '{raw_attach.link}' was not found; attach skipped")
            model_coll.hide_viewport = True
            context.window.scene = current_scene
            return None
        link.select_set(True)
        for obj in link.children_recursive:
            obj.select_set(True)
        attach_name = f"{raw_attach.prefix}{raw_attach.link}"
    else:
        for obj in model_coll.all_objects:
            obj.select_set(True)
        attach_name = f"{raw_attach.prefix}{raw_attach.model}"

    att_collection = funcs.get_collection(context, attach_name)
    bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked": True, "mode": "TRANSLATION"})
    objs = list(context.selected_objects)

    count = len(model_prefix)
    for obj in objs:
        funcs.link_collection(obj, att_collection)
        if model_prefix == obj.name[:count]:
            obj.name = obj.name.replace(model_prefix, raw_attach.prefix)[:-4]
        else:
            obj.name = raw_attach.prefix + obj.name[:-4]

    model_coll.hide_viewport = True
    context.window.scene = current_scene

    att_obj = funcs.add_attach(context, report, raw_attach, collection, attach_name, parent_obj)
    att_obj.select_set(True)

    if link:
        if model_prefix == link.name[:count]:
            link = bpy.data.objects[link.name.replace(model_prefix, raw_attach.prefix)]
        else:
            link = bpy.data.objects[raw_attach.prefix + link.name]
        funcs.parent_under(link, att_obj, link.location)
    else:
        for obj in objs:
            if obj.parent is not None:
                continue
            funcs.parent_under(obj, att_obj, obj.location, obj.rotation_euler)

    for obj in objs:
        funcs.link_collection(obj, collection)


def add_inertial(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    collection: Collection,
    tag_attrs: dict,
    parent_obj: Object | None = None,
    prefix: str = "",
):
    """Add an inertial element from XML tag attributes.

    Creates an inertial object with transform and inertial properties
    (mass, inertia, etc.).

    Args:
        context: The Blender context.
        report: Report callback function.
        collection: The Blender collection to link the inertial into.
        tag_attrs: Dictionary of XML tag attributes for the inertial.
        parent_obj: Optional parent object.
        prefix: Optional prefix for the object name.
    """
    obj = funcs.add_inertial(context, report, collection, parent_obj)
    set_name_by_attrs(obj, tag_attrs, prefix)

    # XML poses are physical link-local transforms, before display compensation.
    obj.matrix_parent_inverse = Matrix.Identity(4)
    set_local_transform(obj, tag_attrs)
    data: InertialItem = obj.Forge_Inertial
    for prop in def_props.INERTIAL_PROPS:
        if prop in tag_attrs:
            # Decompose the complete tensor once; component-wise writes would
            # expose incomplete, potentially non-positive-definite matrices.
            if prop == "fullinertia":
                data.fullinertia = parse_attr_from_xml(data, prop, tag_attrs)
            else:
                set_props_from_xml(data, prop, tag_attrs)

    from ..core.inertial import update_empty_display

    update_empty_display(obj)


def build_world_tree(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    task: Sections,
    assets_data: AssetsData,
    sub_task_index: int,
    root_file_path: str,
    model: str = "",
    parent_coll: Collection | None = None,
):
    """Parse child elements within a link/body and create corresponding objects.

    Recursively processes body, frame, replicate, inertial, joint, light,
    camera, site, geom, and attach child elements.

    Args:
        context: The Blender context.
        report: Report callback function.
        task: Sections object containing worldbody elements and links.
        assets_data: AssetsData object containing assets and defaults.
        sub_task_index: Index into the worldbody elements list.
        root_file_path: Root file path for resolving relative sub-model paths.
        model: Optional model prefix for object names.
        parent_coll: Optional parent collection.
    """

    sel.clear_select()
    parent_id, element = task.worldbody.elements[sub_task_index]
    if parent_id >= 0:
        link = task.links[parent_id]
        parent_obj = link.object
        childClass = link.childclass
    else:
        parent_obj = None
        childClass = None

    tag_attrs = dict(element.attrib)
    match element.tag:
        case cons.MJCFTags.BODY:
            collection = funcs.get_collection(
                context,
                set_coll_tag(cons.CollectionNames.LINK if parent_obj else cons.CollectionNames.WORLD, parent_coll),
                parent_coll,
            )
            obj = add_link(context, report, collection, tag_attrs, parent_obj, model)
            childClass = tag_attrs["childclass"] if "childclass" in tag_attrs else childClass
            task.links[sub_task_index] = Link(obj, childClass)

        case cons.MJCFTags.FRAME:
            collection = funcs.get_collection(
                context,
                set_coll_tag(cons.CollectionNames.FRAME if parent_obj else cons.CollectionNames.WORLD, parent_coll),
                parent_coll,
            )
            obj = add_frame(context, report, collection, tag_attrs, parent_obj, model)
            childClass = tag_attrs["childclass"] if "childclass" in tag_attrs else childClass
            task.links[sub_task_index] = Link(obj, childClass)

        case cons.MJCFTags.REPLICATE:
            collection = funcs.get_collection(
                context,
                set_coll_tag(cons.CollectionNames.REPLICATE if parent_obj else cons.CollectionNames.WORLD, parent_coll),
                parent_coll,
            )
            obj = add_replicate(context, report, collection, tag_attrs, parent_obj, model)
            task.replicates.data.append(obj)
            task.replicates.count += 1
            task.links[sub_task_index] = Link(obj, childClass)
        case cons.MJCFTags.INERTIAL:
            collection = funcs.get_collection(
                context, set_coll_tag(cons.CollectionNames.INERTIAL, parent_coll), parent_coll
            )
            add_inertial(context, report, collection, tag_attrs, parent_obj, model)
        case cons.MJCFTags.JOINT | cons.MJCFTags.FJOINT:
            if element.tag == cons.MJCFTags.FJOINT:
                tag_attrs["type"] = "free"
            collection = funcs.get_collection(
                context, set_coll_tag(cons.CollectionNames.JOINT, parent_coll), parent_coll
            )
            add_joint(context, report, collection, task.defaults, tag_attrs, parent_obj, childClass, model)
        case cons.MJCFTags.LIGHT:
            collection = funcs.get_collection(
                context,
                set_coll_tag(cons.CollectionNames.LIGHT if parent_obj else cons.CollectionNames.WORLD, parent_coll),
                parent_coll,
            )
            add_light(context, report, collection, task.defaults, tag_attrs, parent_obj, childClass, model)
        case cons.MJCFTags.CAMERA:
            collection = funcs.get_collection(
                context,
                set_coll_tag(cons.CollectionNames.CAMERA if parent_obj else cons.CollectionNames.WORLD, parent_coll),
                parent_coll,
            )
            add_camera(context, report, collection, task.defaults, tag_attrs, parent_obj, childClass, model)
        case cons.MJCFTags.SITE:
            collection = funcs.get_collection(
                context, set_coll_tag(cons.CollectionNames.SITE, parent_coll), parent_coll
            )
            add_site(context, report, collection, task.defaults, tag_attrs, parent_obj, childClass, model)
        case cons.MJCFTags.GEOM:
            collection = funcs.get_collection(
                context,
                set_coll_tag(cons.CollectionNames.VISUAL if parent_obj else cons.CollectionNames.WORLD, parent_coll),
                parent_coll,
            )
            add_geom(
                context,
                report,
                collection,
                task.defaults,
                assets_data,
                tag_attrs,
                parent_obj,
                childClass,
                parent_coll,
                model,
            )
        case cons.MJCFTags.ATTACH:
            collection = funcs.get_collection(
                context,
                set_coll_tag(cons.CollectionNames.ATTACH if parent_obj else cons.CollectionNames.WORLD, parent_coll),
                parent_coll,
            )
            add_attach(context, report, collection, task.attachs, tag_attrs, root_file_path, parent_obj)


def add_contact(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    element: ET.Element,
    parent_coll: Collection | None = None,
    prefix: str = "",
):
    """Add contact constraint objects from <contact> XML element children.

    Args:
        context: The Blender context.
        report: Report callback function.
        element: The XML element containing contact pairs.
        parent_coll: Optional parent collection.
        prefix: Optional prefix for object name lookups.
    """

    collection = funcs.get_collection(context, set_coll_tag(cons.CollectionNames.CONTACT, parent_coll), parent_coll)

    sel.clear_select()
    tag_attrs = dict(element.attrib)

    if "body1" in tag_attrs and "body2" in tag_attrs:
        targets = [get_data_object(tag_attrs["body1"], prefix), get_data_object(tag_attrs["body2"], prefix)]
        obj = funcs.add_contact(context, report, collection, element.tag.upper(), targets)
        set_name_by_attrs(obj, tag_attrs, prefix)
    if "geom1" in tag_attrs and "geom2" in tag_attrs:
        targets = [get_data_object(tag_attrs["geom1"], prefix), get_data_object(tag_attrs["geom2"], prefix)]
        obj = funcs.add_contact(context, report, collection, element.tag.upper(), targets)
        set_name_by_attrs(obj, tag_attrs, prefix)
        data: ContactItem = obj.Forge_Contact
        for prop in def_props.CONTACT_TYPE_PROPS[element.tag.upper()]:
            if prop in tag_attrs:
                set_props_from_xml(data, prop, tag_attrs)


def add_equality(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    element: ET.Element,
    defaults: dict,
    parent_coll: Collection | None = None,
    prefix: str = "",
):
    """Add equality constraint objects from <equality> XML element children.

    Args:
        context: The Blender context.
        report: Report callback function.
        element: The XML element containing equality constraints.
        defaults: The defaults dictionary for attribute inheritance.
        parent_coll: Optional parent collection.
        prefix: Optional prefix for object name lookups.
    """

    collection = funcs.get_collection(context, set_coll_tag(cons.CollectionNames.EQUALITY, parent_coll), parent_coll)

    sel.clear_select()
    tag_attrs = dict(element.attrib)
    if "class" in tag_attrs:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.EQUALITY, tag_attrs["class"])
    else:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.EQUALITY)

    equality_type = element.tag.upper()
    if equality_type not in def_props.EQUALITY_TYPE_PROPS:
        report({"WARNING"}, f"Unsupported equality type '{element.tag}'; element skipped")
        return None

    tag = ""
    if "body1" in tag_attrs:
        tag = "body"
    elif "site1" in tag_attrs:
        tag = "site"
    elif "joint1" in tag_attrs:
        tag = "joint"

    if not tag or f"{tag}1" not in tag_attrs or (tag == "site" and f"{tag}2" not in tag_attrs):
        report({"WARNING"}, f"Equality '{element.tag}' is missing supported targets; element skipped")
        return None

    targets = [get_data_object(tag_attrs[f"{tag}1"], prefix)]
    if f"{tag}2" in tag_attrs:
        targets.append(get_data_object(tag_attrs[f"{tag}2"], prefix))
    obj = funcs.add_equality(context, report, collection, equality_type, targets)
    set_name_by_attrs(obj, tag_attrs, prefix)

    data: EqualityItem = obj.Forge_Equality
    if tag == "body" and "anchor" in tag_attrs:
        data.anchor = parse_attr_from_xml(data, "anchor", tag_attrs)

    for prop in def_props.EQUALITY_TYPE_PROPS[equality_type]:
        if prop == "anchor":
            continue
        if prop in tag_attrs:
            set_props_from_xml(data, prop, tag_attrs)


def add_tendon(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    element: ET.Element,
    defaults: dict,
    parent_coll: Collection | None = None,
    prefix: str = "",
):
    """Add tendon objects from <tendon> XML element children.

    Args:
        context: The Blender context.
        report: Report callback function.
        element: The XML element containing tendons.
        defaults: The defaults dictionary for attribute inheritance.
        parent_coll: Optional parent collection.
        prefix: Optional prefix for object name lookups.
    """

    collection = funcs.get_collection(context, set_coll_tag(cons.CollectionNames.TENDON, parent_coll), parent_coll)

    sel.clear_select()
    tag_attrs = dict(element.attrib)
    if "class" in tag_attrs:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.TENDON, tag_attrs["class"])
    else:
        parse_inherit_attrs(defaults, tag_attrs, cons.MJCFTags.TENDON)

    type = element.tag.upper()
    if type not in def_props.TENDON_TYPE_PROPS:
        report({"WARNING"}, f"{type} tendon not support yet!")
        return
    targets = []
    target_coefficients = []
    for target in element:
        target_attrs = dict(target.attrib)
        if "joint" in target_attrs:
            targets.append(get_data_object(target_attrs["joint"], prefix))
            target_coefficients.append(float(target_attrs.get("coef", 1.0)))

    obj = funcs.add_tendon(context, report, collection, type, targets)
    set_name_by_attrs(obj, tag_attrs, prefix)

    data: TendonItem = obj.Forge_Tendon
    for item, coefficient in zip(data.targets.items, target_coefficients):
        item.coef = coefficient
    for prop in def_props.TENDON_TYPE_PROPS[type]:
        if prop in tag_attrs:
            set_props_from_xml(data, prop, tag_attrs)


def add_actuator(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    element: ET.Element,
    defaults: dict,
    parent_coll: Collection | None = None,
    prefix: str = "",
):
    """Add actuator objects from <actuator> XML element children.

    Args:
        context: The Blender context.
        report: Report callback function.
        element: The XML element containing actuators.
        defaults: The defaults dictionary for attribute inheritance.
        parent_coll: Optional parent collection.
        prefix: Optional prefix for object name lookups.
    """

    collection = funcs.get_collection(context, set_coll_tag(cons.CollectionNames.ACTUATOR, parent_coll), parent_coll)

    sel.clear_select()
    tag_attrs = dict(element.attrib)
    if "class" in tag_attrs:
        parse_inherit_attrs(defaults, tag_attrs, element.tag, tag_attrs["class"])
    else:
        parse_inherit_attrs(defaults, tag_attrs, element.tag)

    tag = ""

    if "tendon" in tag_attrs:
        tag = "tendon"
    elif "site" in tag_attrs:
        tag = "site"
    elif "body" in tag_attrs:
        tag = "body"
    elif "joint" in tag_attrs:
        tag = "joint"

    target = get_data_object(tag_attrs[tag], prefix)
    type = element.tag.upper()

    obj = funcs.add_actuator(context, report, collection, type, target)
    set_name_by_attrs(obj, tag_attrs, prefix)

    data: ActuatorItem = obj.Forge_Actuator
    for prop in def_props.ACTUATOR_TYPE_PROPS[type]:
        if prop in tag_attrs:
            set_props_from_xml(data, prop, tag_attrs)


def add_sensor(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    element: ET.Element,
    parent_coll: Collection | None = None,
    prefix: str = "",
):
    """Add sensor objects from <sensor> XML element children.

    Args:
        context: The Blender context.
        report: Report callback function.
        element: The XML element containing sensors.
        parent_coll: Optional parent collection.
        prefix: Optional prefix for object name lookups.
    """

    collection = funcs.get_collection(context, set_coll_tag(cons.CollectionNames.SENSOR, parent_coll), parent_coll)

    sel.clear_select()
    tag_attrs = dict(element.attrib)

    type = element.tag.capitalize()
    targets = []
    ref_type = None
    target_type = cons.SensorTargetTypes.BODY
    if type not in def_props.SENSOR_TYPE_PROPS:
        report({"WARNING"}, f"{type} sensor not support yet!")
        return

    if type == "Contact":
        # Contact sensor — detect which filter group is present in the XML
        if "body1" in tag_attrs:
            target_type = cons.SensorTargetTypes.BODY
            targets.append(get_data_object(tag_attrs["body1"], prefix))
            if "body2" in tag_attrs:
                targets.append(get_data_object(tag_attrs["body2"], prefix))
        elif "geom1" in tag_attrs:
            target_type = cons.SensorTargetTypes.GEOM
            targets.append(get_data_object(tag_attrs["geom1"], prefix))
            if "geom2" in tag_attrs:
                targets.append(get_data_object(tag_attrs["geom2"], prefix))
        elif "subtree1" in tag_attrs:
            target_type = cons.SensorTargetTypes.SUBTREE
            targets.append(get_data_object(tag_attrs["subtree1"], prefix))
            if "subtree2" in tag_attrs:
                targets.append(get_data_object(tag_attrs["subtree2"], prefix))
        elif "site" in tag_attrs:
            target_type = cons.SensorTargetTypes.SITE
            targets.append(get_data_object(tag_attrs["site"], prefix))
    else:
        for key, item in def_props.SENSOR_TYPE_PROPS[type].items():
            if key in ["body", "site", "joint"]:
                if key in tag_attrs:
                    target_type = key.upper()
                    targets.append(get_data_object(tag_attrs[key], prefix))
            if key in ["objtype", "objname"]:
                if key == "objname":
                    if "objname" in tag_attrs:
                        target_type = tag_attrs["objtype"].upper()
                        targets.append(get_data_object(tag_attrs["objname"], prefix))
            if key in ["reftype", "refname"]:
                if key == "refname":
                    if "refname" in tag_attrs:
                        targets.append(get_data_object(tag_attrs["refname"], prefix))
                if key == "reftype" and "reftype" in tag_attrs:
                    ref_type = tag_attrs["reftype"].upper()
    if targets:
        obj = funcs.add_sensor(
            context,
            report,
            collection,
            type,
            target_type,
            targets[0] if len(targets) == 1 else targets,
            ref_type=ref_type,
        )
        set_name_by_attrs(obj, tag_attrs, prefix)
        data_obj: SensorItem = obj.Forge_Sensor
        # Enable xbody mode for xbody-based filters
        if target_type == cons.SensorTargetTypes.XBODY:
            data_obj.use_xbody = True
        # Enable subtree mode for subtree-based filters
        if target_type == cons.SensorTargetTypes.SUBTREE:
            data_obj.use_subtree = True
        if type == "Contact":
            # Set data first (triggers update_contact_num to auto-compute num)
            if "data" in tag_attrs:
                data_obj.data = set(tag_attrs["data"].lower().split())
            # Then set num and reduce (num overrides auto-computed value)
            for prop in ["num", "reduce"]:
                if prop in tag_attrs:
                    set_props_from_xml(data_obj, prop, tag_attrs)
        else:
            # Set type-specific properties for non-Contact sensors
            for key, item in def_props.SENSOR_TYPE_PROPS[type].items():
                if key not in ["body", "site", "joint", "objtype", "objname", "reftype", "refname"]:
                    if key in tag_attrs:
                        set_props_from_xml(data_obj, item, tag_attrs)

        # Set common sensor properties
        for prop in ["noise", "cutoff"]:
            if prop in tag_attrs:
                set_props_from_xml(data_obj, prop, tag_attrs)


def get_reference(
    element: ET.Element,
    base_dir: Path,
    task_list: list[tuple[str, str, str, Sections]],
    defaults: dict,
    ref_type: str,
    name: str,
    model: str = "",
):
    """Resolve and enqueue an MJCF reference (include, attach, or root file).

    Args:
        element: The XML element containing the reference.
        base_dir: Base directory for resolving file paths.
        task_list: List of import tasks to append to.
        defaults: Default element configurations.
        ref_type: The reference type (ROOT, ATTACH, INCLUDE).
        name: Reference name.
        model: Optional model identifier.
    """
    file = dict(element.attrib)["file"]
    filepath = Path(file) if os.path.exists(file) else Path(base_dir / file)
    get_task_recursive(filepath, task_list, defaults, file, ref_type, name, model)


def get_task_recursive(
    filepath: Path,
    task_list: list[tuple[str, str, str, Sections]],
    defaults: dict,
    file: str = "",
    ref_type: str = "ROOT",
    name: str = "",
    model: str = "",
):
    """Recursively parse an MJCF file and enqueue all referenced import tasks.

    Args:
        filepath: Path to the MJCF XML file.
        task_list: List of import tasks to append to.
        defaults: Default element configurations.
        file: Original file name for reference resolution.
        ref_type: The reference type (ROOT, ATTACH, INCLUDE).
        name: Reference name.
        model: Optional model identifier.
    """
    sections = Sections()

    xml_path = filepath.resolve()
    root_element = ET.parse(xml_path).getroot()
    sections.file = file
    sections.base_dir = xml_path.parent

    elements = [element for element in root_element]
    elements = sorted(elements, key=lambda obj: section_order_map.get(obj.tag, len(section_order)))

    for element in elements:
        match element.tag:
            case cons.MJCFTags.INCLUDE:
                file = dict(element.attrib)["file"]
                inc_name = Path(file).name
                sections.includes.append((inc_name, file, sections.base_dir))
                get_reference(
                    element,
                    sections.base_dir,
                    task_list,
                    defaults,
                    cons.ReferenceType.INCLUDE,
                    inc_name,
                )
            case cons.MJCFTags.COMPILER:
                get_element(element, sections.compiler.elements)
                sections.compiler.count = len(sections.compiler.elements)
            case cons.MJCFTags.OPTION:
                get_element(element, sections.option.elements)
                sections.option.count = len(sections.option.elements)
            case cons.MJCFTags.STATISTIC:
                get_element(element, sections.statistic.elements)
                sections.statistic.count = len(sections.statistic.elements)
            case cons.MJCFTags.VISUAL:
                get_element_iter(element, sections.visual.elements)
                sections.visual.count = len(sections.visual.elements)
            case cons.MJCFTags.DEFAULT:
                get_default(element, defaults)
            case cons.MJCFTags.ASSET:
                get_element_iter(element, sections.asset.elements)
                sections.asset.elements = sorted(
                    sections.asset.elements,
                    key=lambda obj: assets_order_map.get(obj[-1].tag, len(assets_order)),
                )
                count = 0
                for _pi, el in reversed(sections.asset.elements):
                    if el.tag == "model":
                        count += 1
                        attrs = dict(el.attrib)
                        file = attrs["file"]
                        att_identifier = Path(file).name
                        if "name" in attrs:
                            att_name = attrs["name"]
                        else:
                            root, _ = os.path.splitext(file)
                            att_name = os.path.basename(root)

                        sections.attachs[att_name] = [att_identifier, file]
                        att_defaults = {}
                        get_reference(
                            el,
                            sections.base_dir,
                            task_list,
                            att_defaults,
                            cons.ReferenceType.ATTACH,
                            att_identifier,
                            att_name,
                        )

                if count > 0:
                    sections.asset.elements = sections.asset.elements[:-count]
                sections.asset.count = len(sections.asset.elements)

            case cons.MJCFTags.WORLDBODY:
                get_element_iter(element, sections.worldbody.elements)
                sections.worldbody.count = len(sections.worldbody.elements)
            case cons.MJCFTags.CONTACT:
                get_element_iter(element, sections.contact.elements)
                sections.contact.count = len(sections.contact.elements)
            case cons.MJCFTags.EQUALITY:
                get_element_iter(element, sections.equality.elements)
                sections.equality.count = len(sections.equality.elements)
            case cons.MJCFTags.TENDON:
                get_element_iter(element, sections.tendon.elements)
                sections.tendon.count = len(sections.tendon.elements)
            case cons.MJCFTags.ACTUATOR:
                get_element_iter(element, sections.actuator.elements)
                sections.actuator.count = len(sections.actuator.elements)
            case cons.MJCFTags.SENSOR:
                get_element_iter(element, sections.sensor.elements)
                sections.sensor.count = len(sections.sensor.elements)

    sections.defaults = defaults.copy()
    parse_defaults(sections.defaults)
    task_list.append((ref_type, name if name else xml_path.name, model, sections))


def import_init(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
):
    """Main MJCF import entry point.

    Resets all visual/global/temp configuration, clears the current scene, purges orphan data.

    Args:
        context: The Blender context.
        report: Report callback function.
    """
    scene = context.scene
    visual_config: VisualConfig = bpy.data.scenes[scene.Main_Scene].Forge_VisualConfig
    visual_config.reset()

    global_config: GlobalConfig = bpy.data.scenes[scene.Main_Scene].Forge_GlobalConfig
    global_config.reset()

    temp_props: Temp_Props = bpy.data.scenes[scene.Main_Scene].Forge_Temp_Props
    temp_props.reset()

    for collection in bpy.data.collections:
        collection.hide_viewport = False

    bpy.context.window.scene = bpy.data.scenes["Scene"]
