# Chapter 2: Model Define — Global and General

[Previous: MCP service](01_mcp_server.md) · [Contents](../forge_docs.md) · [中文](../../cn/forge_docs/02_global_and_general.md) · [Next: Geometry and Material](03_geometry_and_material.md)

## 2.1 Global group

The Global group edits scene-level settings. Both buttons require that no object is selected.

<div align="center"><img src="../../assets/images/manual/02-global-properties-region.png" alt="Global group"></div>

### Global Properties

**Operator ID:** `forge.properties_global`

The dialog contains:

<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/02-compiler-properties.png" width="412" alt="Global Properties dialog"></div>
    <div style="flex: 1;"><dt style="font-weight: bold !important; ">Compiler Properties</dt><ul><li>Compiler settings. The Autolimits switch controls automatic range inference. <a href="https://motrixsim.readthedocs.io/en/latest/user_guide/getting_started/mjcf_reference.html#compiler">MJCF reference</a></li></ul></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/02-option-properties.png" width="412" alt="Global Properties dialog"></div>
    <div style="flex: 1;"><dt style="font-weight: bold !important; ">Option Properties</dt><ul><li>Simulation option settings. <a href="https://motrixsim.readthedocs.io/en/latest/user_guide/getting_started/mjcf_reference.html#option">MJCF reference</a></li></ul><dt style="font-weight: bold !important; ">Flag Option</dt><ul><li>A nested subpanel inside Option Properties containing Override and the individual flag switches. <a href="https://motrixsim.readthedocs.io/en/latest/user_guide/getting_started/mjcf_reference.html#flag">MJCF reference</a></li></ul></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/02-statistic-properties.png" width="412" alt="Global Properties dialog"></div>
    <div style="flex: 1;"><dt style="font-weight: bold !important; ">Statistic Properties</dt><ul><li>Model statistics. <a href="https://motrixsim.readthedocs.io/en/latest/user_guide/getting_started/mjcf_reference.html#statistic">MJCF reference</a></li></ul></div>
</div>

> Changes are written directly to the scene's `Forge_GlobalConfig`.

### Visual Properties

**Operator ID:** `forge.properties_visual`

The dialog contains **Global, Headlight, Map, RGBA, Quality, SSGI,** and **Tonemapping**:

<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/02-global-properties.png" width="412" alt="Visual Global Properties dialog"></div>
    <div style="flex: 1;"><dt style="font-weight: bold !important; ">Global Properties</dt><ul><li>Global miscellaneous parameters. <a href="https://motrixsim.readthedocs.io/en/latest/user_guide/getting_started/mjcf_reference.html#global">MJCF reference</a></li></ul></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/02-headlight-properties.png" width="412" alt="Headlight Properties dialog"></div>
    <div style="flex: 1;"><dt style="font-weight: bold !important; ">Headlight Properties</dt><ul><li>Headlight parameters. When Active is disabled, the Headlight sub-parameters cannot be edited. Export writes the Active state to the headlight active attribute as 1/0; import accepts both 1/0 and true/false. <a href="https://motrixsim.readthedocs.io/en/latest/user_guide/getting_started/mjcf_reference.html#headlight">MJCF reference</a></li></ul></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/02-map-properties.png" width="412" alt="Map Properties dialog"></div>
    <div style="flex: 1;"><dt style="font-weight: bold !important; ">Map Properties</dt><ul><li>View-distance and fog settings. <a href="https://motrixsim.readthedocs.io/en/latest/user_guide/getting_started/mjcf_reference.html#map">MJCF reference</a></li></ul></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/02-rgba-properties.png" width="412" alt="RGBA Properties dialog"></div>
    <div style="flex: 1;"><dt style="font-weight: bold !important; ">RGBA Properties</dt><ul><li>Color and transparency settings for different decorative objects. <a href="https://motrixsim.readthedocs.io/en/latest/user_guide/getting_started/mjcf_reference.html#rgba">MJCF reference</a></li></ul></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/02-quality-properties.png" width="412" alt="Quality Properties dialog"></div>
    <div style="flex: 1;"><dt style="font-weight: bold !important; ">Quality Properties</dt><ul><li>Shadow-map quality settings. <a href="https://motrixsim.readthedocs.io/en/latest/user_guide/getting_started/mjcf_reference.html#quality">MJCF reference</a></li></ul></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/02-ssgi-properties.png" width="412" alt="SSGI Properties dialog"></div>
    <div style="flex: 1;"><dt style="font-weight: bold !important; ">SSGI Properties</dt><ul><li>SSGI settings. When Active is disabled, SSGI sub-parameters cannot be edited. <a href="https://motrixsim.readthedocs.io/en/latest/user_guide/getting_started/mjcf_reference.html#ssgi-mpex">MJCF reference</a></li></ul></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/02-tonemapping-properties.png" width="412" alt="Tonemapping Properties dialog"></div>
    <div style="flex: 1;"><dt style="font-weight: bold !important; ">Tonemapping Properties</dt><ul><li>Tonemapping settings. <a href="https://motrixsim.readthedocs.io/en/latest/user_guide/getting_started/mjcf_reference.html#tonemapping-mpex">MJCF reference</a></li></ul></div>
</div>

> Changes are written directly to the scene's `Forge_VisualConfig`.

## 2.2 General group

<div align="center"><img src="../../assets/images/manual/02-general-properties-region.png" alt="General group"></div>

### Define model

**Operator ID:** `forge.define_model_type`

Dialog:

<div align="center"><img src="../../assets/images/manual/02-general-define.png" alt="Define model dialog"></div>

This operator is available only for objects whose `Forge_Model_Type == UNDEFINED`. The available Forge types depend on the Blender object type:

| Blender object type | Forge types available | Additional behavior |
| --- | --- | --- |
| Empty | Link | Move to the Link or World Collection and use the `LNK_` prefix. |
| Mesh | Visual, Collider | Initialize as Mesh; Visual uses Group 2 with contact disabled, Collider uses Group 3; use the `GEO_` or `COL_` prefix. |
| Light | Light | Area Light is unsupported; initialize a Forge Light and use the `LIT_` prefix. |
| Camera | Camera | Perspective and Orthographic only; use the `CAM_` prefix. |

Procedure:

1. Select Blender objects of the same type that have not been defined.
2. Click **Define model**.
3. Choose a Model Type and confirm.

### Batch Rename

**Operator ID:** `forge.batch_rename`

Dialog:

<div align="center"><img src="../../assets/images/manual/02-general-rename.png" alt="Batch Rename dialog"></div>

The operator becomes available when at least one object is selected:

1. Enter a common name prefix in **New Name**.
2. Enter a numbering placeholder in **Numerate**; the number of characters determines the zero padding.
3. Confirm. Names are generated as `prefix_number`.

For example, with New Name `arm` and Numerate `###`, the results are `arm_000`, `arm_001`, and so on.

---

[Previous: MCP service](01_mcp_server.md) · [Contents](../forge_docs.md) · [中文](../../cn/forge_docs/02_global_and_general.md) · [Next: Geometry and Material](03_geometry_and_material.md)
