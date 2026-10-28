# 第 0 章：界面总览与通用操作

[返回目录](../forge_docs.md) · [English](../../en/forge_docs/00_ui_overview.md) · [下一章：MCP 服务](01_mcp_server.md)

## 0.1 打开 Forge 面板

安装并启用 Forge 后，在 3D 视图中按 `N` 打开侧栏，再切换到 **Forge** 页签。

本系列文档涉及以下 UI 面板：

<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/00-forge-sidebar-overview-0.png"
          width="292"
          alt="Forge 信息面板"
        >
    </div>
    <div style="flex: 2;">
        <dt style="font-weight: bold !important; ">Forge info</dt>
        <ul>
            <li>Forge 工具主要信息 </li>
        </ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/00-forge-sidebar-overview-1.png"
          width="292"
          alt="MCP 面板"
        >
    </div>
    <div style="flex: 2;">
        <strong style="font-weight: bold !important; ">MCP Server</strong>
        <ul>
            <li>MCP 服务相关参数配置 | 第 1 章 </li>
        </ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/00-forge-sidebar-overview-2.png"
          width="292"
          alt="Model Define 面板"
        >
    </div>
    <div style="flex: 2;">
        <strong style="font-weight: bold !important; ">Model Define</strong>
        <ul>
            <li>全局设置、类型定义、模型元素创建与辅助工具 | 第 0，2～5 章 </li>
        </ul>
        <strong style="font-weight: bold !important; ">布局</strong>
        <ol>
            <li>
                <dt style="font-weight: bold !important; ">Global：</dt>Global Properties、Visual Properties。
            </li>
            <li>
                <dt style="font-weight: bold !important; ">General：</dt>Define model、Batch Rename。
            </li>
            <li>
                <dt style="font-weight: bold !important; ">Geometry：</dt>Visual/Collider shape 的创建与定义、Height Field（高度场）、Plane（平面）、Check Meshs（流形与穿插检查）。
            </li>
            <li>
                <dt style="font-weight: bold !important; ">Material：</dt>从 Forge PBR 库创建常见材质、 创建checker材质、 赋予已有材质。
            </li>
            <li>
                <dt style="font-weight: bold !important; ">Kinematics：</dt>Link、Joint、Parent、Inertial、Root。
            </li>
            <li>
                <dt style="font-weight: bold !important; ">Instance：</dt>Mark、 Choose、 Set。
            </li>
            <li>
                <dt style="font-weight: bold !important; ">Hardware：</dt>Actuator、Site、Tendon、Equality、Sensor、Contact、Light、Camera。
            </li>
            <li>
                <dt style="font-weight: bold !important; ">Tag / Select：</dt>按名称标签选中场景对象。
            </li>
            <li>
                <dt style="font-weight: bold !important; ">Type / Select：</dt>按类型选中场景对象。
            </li>
            <li>
                <dt style="font-weight: bold !important; ">Gizmo display size：</dt>批量调整 Forge Gizmo 显示尺寸。
            </li>
        </ol>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/00-forge-sidebar-overview-3.png"
          width="292"
          alt="Meta 元素面板"
        >
    </div>
    <div style="flex: 2;">
        <strong style="font-weight: bold !important; ">Meta Elements</strong>
        <ul>
            <li>Frame、Replicate、Attach、Include | 第 6 章 </li>
        </ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/00-forge-sidebar-overview-4.png"
          width="292"
          alt="CoACD 面板"
        >
    </div>
    <div style="flex: 2;">
        <strong style="font-weight: bold !important; ">CoACD</strong>
        <ul>
            <li>使用 CoACD 将网格分解为凸形部件 | 第 9 章 </li>
        </ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/00-forge-sidebar-overview-5.png"
          width="292"
          alt="导入面板"
        >
    </div>
    <div style="flex: 2;">
        <strong style="font-weight: bold !important; ">Import</strong>
        <ul>
            <li>导入 MJCF XML 文件 | 第 8 章 </li>
        </ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img
          src="../../assets/images/manual/00-forge-sidebar-overview-6.png"
          width="292"
          alt="导出面板"
        >
    </div>
    <div style="flex: 2;">
        <strong style="font-weight: bold !important; ">Export</strong>
        <ul>
            <li>导出为 MJCF XML 文件 | 第 8 章 </li>
        </ul>
    </div>
</div>

> 将鼠标悬停在按钮或参数上，可查看其可用的提示说明。
> Blender 的 **Object Properties（对象属性）→ Forge Properties** 还提供活动对象的变换、父对象、Forge 类型及模型属性，详见第 7 章。

## 0.2 选择、活动对象与选择顺序

- **选中对象**：当前所有被选中的对象。
- **活动对象**：最后激活的对象，通常显示更亮的轮廓。
- **Forge 类型**：对象的 `Forge_Model_Type`，例如 `LINK`、`VISUAL`、`JOINT`等。
- **选择顺序**：Forge 会记录对象被选择的先后，用于 Target、Reference、父对象等角色分配。

<div align="center">
  <img src="../../assets/images/manual/00-selection-and-active-object.png" alt="多选与活动对象轮廓">
</div>

> Creation Operator 通常为每个所选目标创建一个对象；
> Definition Operator 默认只修改活动对象。
> 需要两个或多个目标的 `Equality`、`Sensor`、`Light`、`Camera`和`Tendon`应特别注意选择顺序。

## 0.3 按钮灰色的含义

按钮灰色表示 Operator 的前置条件不满足，常见原因包括：

- 选择数量错误；
- 选中对象中混入了不支持的 Forge 类型；
- 应该取消选择但仍有对象被选中；
- 没有正确的活动对象；
- 当前不在 Object Mode。

<div align="center">
  <img src="../../assets/images/manual/00-operator-active.png" alt="按钮灰色">
</div>

> 每个功能的具体条件会在后续章节的表格中列出。

## 0.4 Tag、类型选择与视口显示

### 按标签选择

1. 在 **Tag** 输入需要匹配的文本。
2. 点击 **Select**，调用 `forge.select_by_tag`。
3. Forge 会选中当前场景中名称包含该文本的对象；原有选择不会自动清空。

<div align="center">
  <img src="../../assets/images/manual/00-tag-and-selection.png" alt="按标签选择">
</div>

### 按模型类型选择

1. 在 **Type** 下拉框选择 Forge 模型类型，例如 **Link** 或 **Collider**。
2. 点击下方 **Select**，调用 `forge.select_by_model_type`。
3. 仅在 **Object Mode** 可用；遍历当前上下文中可选择的对象，将匹配类型的对象加入选择，保留原有选择。

<div align="center">
  <img src="../../assets/images/manual/00-type-and-selection.png" alt="按模型类型选择">
</div>
### 调整 Gizmo 大小

1. 选择 Scale factor 或 Ratio。
2. 点击右侧执行按钮，调用 `forge.scale_gizmo_size`。
3. 有选中对象时只调整所选对象，没有选择时调整整个 `.blend` 文件中的全部对象（含其他场景中的对象）。

<div align="center">
  <img src="../../assets/images/manual/00-gizmo-scale.png" alt="缩放 Gizmo">
</div>

**Inertial** 的显示尺寸由质量和惯量决定，不参与此缩放操作。

### 视口预览开关

在 **Blender Preferences → Add-ons → Forge → General → Viewport Previews** 中，**Collider Preview** 和 **Inertial Preview** 默认开启，分别控制所有 3D 视图中的碰撞体半透明表面和惯量等效长方体预览。

两种预览都要求当前视图开启 **Overlays** 和其中的 **Extras**。选中的预览显示橙色；未选中的 Collider 显示淡蓝色，Inertial 显示红色。Collider 对象使用线框显示，关闭表面预览后仍可查看原生线框；关闭 Inertial 预览后仍保留可选择的原生 Empty 长方体。

## 0.5 推荐建模流程

1. 创建或导入 **Mesh** 到 **Blender**。
2. 使用 **Define model** 将网格定义为 **Visual** 或 **Collider**；使用 **Create link(s)** 创建 **Link**，或将 **Empty** 定义为 **Link**。也可直接通过创建按钮生成基本形状。
3. 建立 **Link** 层级，并用 **Link Parent** 调整父子关系。
4. 创建 **Visual、Collider、Joint** 和 **Site**。
5. 创建 **Actuator、Tendon、Equality、Sensor、Contact、Light** 和 **Camera**。
6. 通过视图 **Gizmo** 编辑参数。
7. 对 **Link** 执行 **Compute Inertial**，选择 **Visual / Collider** 来源，并按需启用 **Check Geometry**。
8. 选择顶层 **Link/Frame** 并执行 **Mark root**。

---

[返回目录](../forge_docs.md) · [English](../../en/forge_docs/00_ui_overview.md) · [下一章：MCP 服务](01_mcp_server.md)
