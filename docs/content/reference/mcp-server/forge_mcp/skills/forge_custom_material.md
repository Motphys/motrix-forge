# Forge custom material

Create, inspect, or repair a Blender material that follows the custom textured-material node contract documented by the Forge material workflow.

## When this skill applies

Use this guide when a Forge `VISUAL`, `HEIGHT FIELD`, or `PLANE` needs a custom Blender material with texture maps, or when an existing material must be checked before MJCF export. The graph is an authoring contract: keep the four framed branches separate so each branch can be disconnected and replaced by a Principled BSDF parameter when a texture is not needed.

The material is assigned through the object's first material slot. Do not confuse that slot with Forge geometry properties such as `group`, `friction`, or `density`.

## Required graph

Build one `ShaderNodeOutputMaterial` and one `ShaderNodeBsdfPrincipled`. Keep the Principled node's `name` set to exactly `Principled BSDF`, because the Forge exporter resolves this node by name. Connect the BSDF to the Output `Surface`. Use one `ShaderNodeTexCoord` and one `ShaderNodeMapping` as the shared coordinate source:

```text
Texture Coordinate (UV) -> Mapping (Vector)
                             ├-> albedo Image Texture (Vector)
                             ├-> ARM Image Texture (Vector)
                             ├-> normal Image Texture (Vector)
                             └-> emission Image Texture (Vector)
```

The reference Mapping node is `Type: Point`, `Location: (0, 0, 0)`, `Rotation: (0°, 0°, 0°)`, and `Scale: (1, 1, 1)`. Use the UV output for ordinary mesh assets. If the asset intentionally uses generated/object coordinates, keep that choice consistent for every image branch.

### Base Color branch (orange frame)

- Image Texture for the albedo/base-color map. Use the image's native color data as `sRGB`.
- Feed its `Color` to a `ShaderNodeMix` configured with `data_type = "RGBA"`, `blend_type = "MULTIPLY"`, and `Factor = 1.0`; keep the other color input (`B`) white (`(1, 1, 1, 1)`).
- Connect the multiply result to Principled BSDF `Base Color`.
- If no albedo map is required, disconnect this branch and set the BSDF `Base Color` directly; do not leave a dead texture link that claims a texture dependency.

### Alpha branch (conditional)

Alpha is linked only when the material's intended use requires transparency. Decide this from the material usage, not from Blender's `surface_render_method` or `blend_method` properties. Use an explicit usage decision such as:

- `OPAQUE`: no Alpha link;
- `SEMITRANSPARENT`: create the Alpha link;
- `MASK_CLIP`: create the Alpha link.

For `SEMITRANSPARENT` or `MASK_CLIP`, the source color layer must be `rgba`; an `rgb` layer must not create an Alpha link. Opaque materials, hashed/dithered-only materials, and the importer's direct `material.texture` path do not get a synthesized Alpha link. The material-usage decision is the gate; the `rgba` role only confirms that an alpha source exists.

- Keep the material's base alpha value as the second input of a `ShaderNodeMath` set to `MULTIPLY` with clamping enabled (the importer uses the linear material alpha; the default is `1.0`).
- Connect the RGBA color Image Texture `Alpha` output to the Math node's first input, then connect the Math result to Principled BSDF `Alpha`.
- When there is no RGBA layer, leave Principled `Alpha` unlinked and use its direct scalar value. If an explicit material `rgba` parameter has an alpha below `1.0`, set that direct value even when no texture is present.
- Do not infer alpha from an RGB image, ARM, normal, or emission map. The branch is opt-in and must be disconnected when the material is opaque or its source is absent.

### ARM branch (green frame)

ARM is a packed, non-color texture. Set its Image Texture color space to `Non-Color` and connect its `Color` to `ShaderNodeSeparateXYZ` `Vector`.

- `Separate XYZ Y` (the packed roughness channel) -> a `ShaderNodeMath` set to `MULTIPLY`, with the other value at `1.0` and clamping enabled -> Principled `Roughness`.
- `Separate XYZ Z` (the packed metallic channel) -> a second clamped `MULTIPLY` with the other value at `1.0` -> Principled `Metallic`.
- `Separate XYZ X` is the packed ambient-occlusion channel. The reference graph does not connect it to Principled; leave it unconnected unless the intended material workflow explicitly adds AO handling outside the Forge export contract.
- If ARM is absent, disconnect the roughness/metallic links and use the BSDF's direct scalar parameters.

The multiply nodes are identity controls in the reference (`Value = 1.0`, `Clamp` enabled). Preserve them when repairing the reference graph; changing them changes the exported channel values.

### Normal branch (blue frame)

- Image Texture for the normal map, color space `Non-Color`.
- Image `Color` -> `ShaderNodeNormalMap` `Color`.
- Normal Map `Strength = 1.0`, `Space = Tangent`.
- Normal Map `Normal` -> Principled BSDF `Normal`.
- Without a normal map, disconnect the branch and leave the BSDF `Normal` input unlinked.

### Emission branch (teal frame)

- Image Texture for the emission map. The reference uses `sRGB`.
- Image `Color` -> `ShaderNodeMix` with `data_type = "RGBA"`, `blend_type = "MULTIPLY"`, `Factor = 1.0`, and the other color input (`B`) white.
- Connect the result to Principled BSDF `Emission Color`.
- Set Principled `Emission Strength` to the desired value; the reference image uses `10.0`.
- Without an emission map, disconnect this branch and use the BSDF's direct emission color/strength.

## Reference defaults

The screenshot shows these useful defaults: Principled `IOR = 1.5`, `Alpha = 1.0`; image textures use `Interpolation: Linear`, `Projection: Flat`, `Extension: Repeat`, and `Single Image`; Normal Map `Strength = 1.0`; Mapping scale `(1, 1, 1)`. Treat these as reference values, not reasons to overwrite intentional material settings.

## Construction and repair rules

1. Inspect the existing material and its first node tree before editing. Reuse image datablocks where possible; do not duplicate images merely to rename nodes.
2. Keep one shared Mapping node and fan its Vector output out to every active image branch. A branch may omit the Mapping connection only when it deliberately uses another documented coordinate source.
3. Use explicit node types and socket links, not screen coordinates or node labels alone. Labels such as `Tex_*_alb`, `Tex_*_arm`, `Tex_*_nrm`, and `*_Emissive` are helpful conventions but are not substitutes for links.
4. Set texture color space by data meaning: albedo/emission are `sRGB`; ARM/normal are `Non-Color`.
5. Preserve the four branch boundaries (Base Color, ARM, Normal, Emission). Each branch can be replaced by a direct Principled input when its map is unavailable.
6. Validate every link after construction: Output Surface, Base Color, Roughness, Metallic, Normal, and Emission Color must resolve to the intended sockets; verify image paths exist and the material is in the object's first slot.
7. A pure-parameter material is valid: no texture needs to be connected to Principled when direct BSDF values are intended. If no tiling is needed, the Mapping node may be omitted from the image vectors.
8. Before export, ensure the graph still matches this contract. The Forge documentation warns that an incompatible custom graph can cause export failure; report unsupported node conversions instead of silently approximating them.

## Minimal Blender Python skeleton

Use this as a construction pattern, adapting image loading and material values to the asset. It deliberately leaves the ARM X/AO output unconnected, matching the reference image, and only adds the Alpha link when the material usage is `SEMITRANSPARENT` or `MASK_CLIP` and the color layer role is `rgba`.

```python
import bpy

mat = bpy.data.materials.new("Custom_Material")
mat.use_nodes = True
nt = mat.node_tree
nt.nodes.clear()

out = nt.nodes.new("ShaderNodeOutputMaterial")
bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
bsdf.name = "Principled BSDF"
texcoord = nt.nodes.new("ShaderNodeTexCoord")
mapping = nt.nodes.new("ShaderNodeMapping")
mapping.vector_type = "POINT"
mapping.inputs["Scale"].default_value = (1.0, 1.0, 1.0)
nt.links.new(texcoord.outputs["UV"], mapping.inputs["Vector"])


def image_node(image, label, non_color=False):
    node = nt.nodes.new("ShaderNodeTexImage")
    node.image = image
    node.label = label
    node.interpolation = "Linear"
    node.projection = "FLAT"
    node.extension = "REPEAT"
    image.colorspace_settings.name = "Non-Color" if non_color else "sRGB"
    nt.links.new(mapping.outputs["Vector"], node.inputs["Vector"])
    return node


def color_multiply(label):
    node = nt.nodes.new("ShaderNodeMix")
    node.data_type = "RGBA"
    node.blend_type = "MULTIPLY"
    node.inputs["Factor"].default_value = 1.0
    node.inputs["B"].default_value = (1.0, 1.0, 1.0, 1.0)
    node.label = label
    return node


def value_multiply(label):
    node = nt.nodes.new("ShaderNodeMath")
    node.operation = "MULTIPLY"
    node.use_clamp = True
    node.inputs[1].default_value = 1.0
    node.label = label
    return node


# Supply Image datablocks (or None for a direct BSDF parameter) before running
# this block, for example: albedo_image = bpy.data.images.get("wood_alb.png").
# A None value leaves that branch unlinked and uses the BSDF parameter instead.
# Replace these placeholders with the appropriate Image datablocks.
albedo_image = None
arm_image = None
normal_image = None
emission_image = None
color_layer_role = "rgb"    # use "rgba" only when the source layer explicitly carries alpha
material_usage = "OPAQUE"   # or "SEMITRANSPARENT" / "MASK_CLIP"
base_alpha = 1.0
bsdf.inputs["Alpha"].default_value = base_alpha
alb = image_node(albedo_image, "Tex_material_alb") if albedo_image else None
arm = image_node(arm_image, "Tex_material_arm", non_color=True) if arm_image else None
nrm = image_node(normal_image, "Tex_material_nrm", non_color=True) if normal_image else None
emi = image_node(emission_image, "Tex_material_emission") if emission_image else None

if alb:
    alb_mix = color_multiply("Base Color Multiply")
    nt.links.new(alb.outputs["Color"], alb_mix.inputs["A"])
    nt.links.new(alb_mix.outputs["Result"], bsdf.inputs["Base Color"])
    alpha_required = color_layer_role == "rgba" and material_usage in {"SEMITRANSPARENT", "MASK_CLIP"}
    if alpha_required:
        alpha_mul = value_multiply("Alpha Multiply")
        alpha_mul.inputs[1].default_value = base_alpha
        nt.links.new(alb.outputs["Alpha"], alpha_mul.inputs[0])
        nt.links.new(alpha_mul.outputs["Value"], bsdf.inputs["Alpha"])

if arm:
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    rough_mul = value_multiply("ARM Roughness Multiply")
    metal_mul = value_multiply("ARM Metallic Multiply")
    nt.links.new(arm.outputs["Color"], sep.inputs["Vector"])
    nt.links.new(sep.outputs["Y"], rough_mul.inputs[0])
    nt.links.new(sep.outputs["Z"], metal_mul.inputs[0])
    nt.links.new(rough_mul.outputs["Value"], bsdf.inputs["Roughness"])
    nt.links.new(metal_mul.outputs["Value"], bsdf.inputs["Metallic"])

if nrm:
    normal = nt.nodes.new("ShaderNodeNormalMap")
    normal.space = "TANGENT"
    normal.inputs["Strength"].default_value = 1.0
    nt.links.new(nrm.outputs["Color"], normal.inputs["Color"])
    nt.links.new(normal.outputs["Normal"], bsdf.inputs["Normal"])

if emi:
    emi_mix = color_multiply("Emission Multiply")
    nt.links.new(emi.outputs["Color"], emi_mix.inputs["A"])
    emission_input = bsdf.inputs.get("Emission Color") or bsdf.inputs.get("Emission")
    if emission_input:
        nt.links.new(emi_mix.outputs["Result"], emission_input)
    if bsdf.inputs.get("Emission Strength"):
        bsdf.inputs["Emission Strength"].default_value = 10.0

nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])

# Replace this placeholder with the requested Forge VISUAL, HFIELD, or PLANE.
target = bpy.data.objects["Visual"]
if not target.material_slots:
    target.data.materials.append(None)
target.material_slots[0].link = "OBJECT"
target.material_slots[0].material = mat

result = {"object": target.name, "material": mat.name}
```

When modifying an existing material, prefer preserving its material name and image assignments. After editing, inspect the node links and save/export only to the user-specified destination.
