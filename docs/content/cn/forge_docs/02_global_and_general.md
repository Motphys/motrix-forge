# 第 2 章：Model Define — 全局与通用设置

[上一章：MCP 服务](01_mcp_server.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/02_global_and_general.md) · [下一章：Geometry 与 Material](03_geometry_and_material.md)

## 2.1 Global 分组

Global 分组用于编辑 Scene 级设置。两个按钮都要求当前没有选中对象。

<div align="center">
  <img src="../../assets/images/manual/02-global-properties-region.png" alt="Global 分组">
</div>

### Global Properties

**Operator ID：** `forge.properties_global`

弹窗包括：

<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/02-compiler-properties.png"
          width="412"
          alt="Global Properties 弹窗"
        >
    </div>
    <div style="flex: 1;">
        <dt style="font-weight: bold !important; ">Compiler Properties</dt>
        <ul>
            <li>编译设置，Autolimits 开关控制自动范围推断。<a href="https://motrixsim.readthedocs.io/zh-cn/latest/user_guide/getting_started/mjcf_reference.html#compiler">MJCF 描述</a> </li>
        </ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/02-option-properties.png"
          width="412"
          alt="Global Properties 弹窗"
        >
    </div>
    <div style="flex: 1;">
        <dt style="font-weight: bold !important; ">Option Properties</dt>
        <ul>
            <li>仿真 Option 设置。<a href="https://motrixsim.readthedocs.io/zh-cn/latest/user_guide/getting_started/mjcf_reference.html#option">MJCF 描述</a> </li>
        </ul>
        <dt style="font-weight: bold !important; ">Flag Option</dt>
        <ul>
            <li>Option Properties 内的嵌套子面板，包含 Override 和各项 Flag 开关。<a href="https://motrixsim.readthedocs.io/zh-cn/latest/user_guide/getting_started/mjcf_reference.html#flag">MJCF 描述</a> </li>
        </ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/02-statistic-properties.png"
          width="412"
          alt="Global Properties 弹窗"
        >
    </div>
    <div style="flex: 1;">
        <dt style="font-weight: bold !important; ">Statistic Properties</dt>
        <ul>
            <li>模型统计数据。<a href="https://motrixsim.readthedocs.io/zh-cn/latest/user_guide/getting_started/mjcf_reference.html#statistic">MJCF 描述</a> </li>
        </ul>
    </div>
</div>

> 修改会直接写入 Scene 的 Forge_GlobalConfig。

### Visual Properties

**Operator ID：** `forge.properties_visual`

弹窗包括 **Global、Headlight、Map、RGBA、Quality、SSGI、Tonemapping**：

<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/02-global-properties.png"
          width="412"
          alt="Visual Global Properties 弹窗"
        >
    </div>
    <div style="flex: 1;">
        <dt style="font-weight: bold !important; ">Global Properties</dt>
        <ul>
            <li>全局杂项参数配置。<a href="https://motrixsim.readthedocs.io/zh-cn/latest/user_guide/getting_started/mjcf_reference.html#global">MJCF 描述</a> </li>
        </ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/02-headlight-properties.png"
          width="412"
          alt="Headlight Properties 弹窗"
        >
    </div>
    <div style="flex: 1;">
        <dt style="font-weight: bold !important; ">Headlight Properties</dt>
        <ul>
            <li>Headlight 参数设置， Active 关闭时 Headlight 子参数不可编辑。导出时 Active 状态写入 headlight 的 active 属性（1/0）；导入时 1/0 与 true/false 均可识别。<a href="https://motrixsim.readthedocs.io/zh-cn/latest/user_guide/getting_started/mjcf_reference.html#headlight">MJCF 描述</a> </li>
        </ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/02-map-properties.png"
          width="412"
          alt="Map Properties 弹窗"
        >
    </div>
    <div style="flex: 1;">
        <dt style="font-weight: bold !important; ">Map Properties</dt>
        <ul>
            <li>视距和雾效设置。<a href="https://motrixsim.readthedocs.io/zh-cn/latest/user_guide/getting_started/mjcf_reference.html#map">MJCF 描述</a> </li>
        </ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/02-rgba-properties.png"
          width="412"
          alt="RGBA Properties 弹窗"
        >
    </div>
    <div style="flex: 1;">
        <dt style="font-weight: bold !important; ">Rgba Properties</dt>
        <ul>
            <li>不同装饰对象的颜色和透明度设置。<a href="https://motrixsim.readthedocs.io/zh-cn/latest/user_guide/getting_started/mjcf_reference.html#rgba">MJCF 描述</a> </li>
        </ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/02-quality-properties.png"
          width="412"
          alt="Quality Properties 弹窗"
        >
    </div>
    <div style="flex: 1;">
        <dt style="font-weight: bold !important; ">Quality Properties</dt>
        <ul>
            <li>Shadow map的质量设置。<a href="https://motrixsim.readthedocs.io/zh-cn/latest/user_guide/getting_started/mjcf_reference.html#quality">MJCF 描述</a> </li>
        </ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/02-ssgi-properties.png"
          width="412"
          alt="SSGI Properties 弹窗"
        >
    </div>
    <div style="flex: 1;">
        <dt style="font-weight: bold !important; ">SSGI Properties</dt>
        <ul>
            <li>SSGI 设置，Active 关闭时，SSGI 子参数不可编辑。<a href="https://motrixsim.readthedocs.io/zh-cn/latest/user_guide/getting_started/mjcf_reference.html#ssgi-mpex">MJCF 描述</a> </li>
        </ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/02-tonemapping-properties.png"
          width="412"
          alt="Tonemapping Properties 弹窗"
        >
    </div>
    <div style="flex: 1;">
        <dt style="font-weight: bold !important; ">Tonemapping Properties</dt>
        <ul>
            <li>Tonemapping 设置。<a href="https://motrixsim.readthedocs.io/zh-cn/latest/user_guide/getting_started/mjcf_reference.html#tonemapping-mpex">MJCF 描述</a> </li>
        </ul>
    </div>
</div>

> 修改会直接写入 Scene 的 Forge_VisualConfig。

## 2.2 General 分组

<div align="center">
  <img src="../../assets/images/manual/02-general-properties-region.png" alt="General 分组">
</div>

### Define model

**Operator ID：** `forge.define_model_type`

弹窗：
<div align="center">
  <img src="../../assets/images/manual/02-general-define.png" alt="General 分组">
</div>

只对 `Forge_Model_Type == UNDEFINED` 的对象可用。可选 Forge 类型取决于 Blender 对象类型：

| Blender 对象类型 | 可定义的 Forge 类型   | 额外行为                                                                          |
| ------------ | --------------- | ----------------------------------------------------------------------------- |
| Empty        | Link            | 移入 Link 或 World Collection，使用 `LNK_` 前缀。                                      |
| Mesh         | Visual、Collider | 初始化为 Mesh；Visual 使用 Group 2 并关闭接触位，Collider 使用 Group 3；使用 `GEO_` 或 `COL_` 前缀。 |
| Light        | Light           | 不支持 Area Light；初始化 Forge Light，使用 `LIT_` 前缀。                                  |
| Camera       | Camera          | 只支持 Perspective 和 Orthographic，使用 `CAM_` 前缀。                                  |

操作步骤：

1. 选择尚未定义的同类 Blender 对象。
2. 点击 **Define model**。
3. 选择 Model Type 并确认。

### Batch Rename

**Operator ID：** `forge.batch_rename`

弹窗：
<div align="center">
  <img src="../../assets/images/manual/02-general-rename.png" alt="General 分组">
</div>

至少选择一个对象后可用：

1. 在 **New Name** 输入统一名称前缀。
2. 在 **Numerate** 输入编号占位文本；字符数量决定补零位数。
3. 确认后名称按 `前缀_编号` 生成。

例如 New Name 为 `arm`、Numerate 为 `###` 时，结果为 `arm_000`、`arm_001`……

---

[上一章：MCP 服务](01_mcp_server.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/02_global_and_general.md) · [下一章：Geometry 与 Material](03_geometry_and_material.md)
