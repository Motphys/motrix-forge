# 第 3 章：Model Define — 几何与材质

[上一章：Global 与 General](02_global_and_general.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/03_geometry_and_material.md) · [下一章：Kinematics](04_kinematics.md)

## 3.1 Geometry 分组布局

**Geometry** 分组从上到下依次是：

1. Create geometry(s) / Create collider(s)
2. Define geometry(s) / Define collider(s)
3. Create height field / Create plane
4. Check Mesh(s)

<div align="center">
  <img src="../../assets/images/manual/03-geom-define.png" alt="Geometry 分组">
</div>

## 3.2 创建 Visual Geometry

**按钮：** **Create geometry(s)**

**Operator ID：** `forge.create_geometry`

弹窗：

<div align="center">
  <img src="../../assets/images/manual/03-visual-creation.png" alt="Create geometry(s)">
</div>

可用条件：未选择对象，或所选对象均为 **Link**、**Frame**、**Replicate**。

- 未选择：在 **World** 创建一个 **Visual**。
- 有选择：为每个所选父对象创建一个 **Visual**。
- 类型：**Box**、**Capsule**、**Cylinder**、**Sphere**。
- 尺寸：
- **Box** 使用三轴 **Size**；
- **Sphere** 使用 **Radius**；
- **Capsule/Cylinder** 使用 **Radius** 与 **Height**。

创建完成后，新 **Visual** 会成为当前选择。

## 3.3 创建 Collider

**按钮：** **Create collider(s)**

**Operator ID：** `forge.create_collider`

弹窗面板：

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <strong>无选中的 Object 手动选择 Collider type</strong>
  </div>
  <div style="flex: 1; text-align: center; ">
    <strong>基于选中 Object 的 Geometry type</strong>
  </div>
  <div style="flex: 1; text-align: center; ">
    <strong>手动选择 Collider type</strong>
  </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/03-collider-creation-0.png"
      width="314"
      alt="Create collider(s)弹窗"
    >
  </div>
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/03-collider-creation-1.png"
      width="314"
      alt="Create collider(s)弹窗"
    >
  </div>
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/03-collider-creation-2.png"
      width="314"
      alt="Create collider(s)弹窗"
    >
  </div>
</div>

可用条件：

- 未选择对象；
- 所选对象均为 **Link/Frame**；
- 所选对象均为 **Visual**。

选择 **Visual** 时有两种 **Method**：

- **Geometry type**：每个 **Collider** 跟随对应 **Visual** 的类型。
- **Collider type**：所有 **Collider** 使用统一指定类型。非 **Mesh** 类型可启用 **Auto size** 自动计算尺寸。**Capsule** / **Cylinder** 可勾选 **Use Min As Height**，以 Visual 包围盒的**最小**轴作为高度（形状也沿该轴朝向），而非最大轴；未启用 **Auto size** 时该选项无效。

未选择或选择为 **Link/Frame** 时，按指定 **Collider Type** 和 **Size** 创建。

## 3.4 修改 Geometry / Collider 类型

弹窗：

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <strong>Visual Define</strong>
  </div>
  <div style="flex: 1; text-align: center; ">
    <strong>Collider Define</strong>
  </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/03-visual-define.png"
      width="314"
      alt="Visual Define弹窗"
    >
  </div>
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/03-collider-define.png"
      width="314"
      alt="Collider Define弹窗"
    >
  </div>
</div>

| 按钮               | Operator ID                  | 适用对象 | 类型                                 |
| ------------------ | ---------------------------- | -------- | ------------------------------------ |
| Define geometry(s) | `forge.define_geometry_type` | Visual   | Box、Capsule、Cylinder、Sphere、Mesh、Sdf |
| Define collider(s) | `forge.define_collider_type` | Collider | Box、Capsule、Cylinder、Sphere、Mesh、Sdf |

弹窗以活动对象的当前类型为初始值，默认只修改活动对象。勾选 **Apply to all selected** 可批量修改。改型时会同步切换或重建对应形状。

SDF 使用现有网格：将 Visual 定义为 **Sdf**，导出为 `type="sdf"` 并引用 mesh 资源。Mesh 与 SDF 之间切换保留网格；从基本形状切换会先应用形状修改器。基本形状转换为 **Mesh** 或 **Sdf** 时保留材质槽、材质分配和活动材质槽，不影响共享原网格的其他对象。

Collider 同样支持 **Sdf**。选中 Visual 后，可在 **Create collider(s)** 中选择 Sdf，以 linked duplicate 方式共享 Visual 的 Mesh Data，并保留父级和变换。修改网格顶点会同步影响两者；也可通过 **Define collider(s)** 切换类型。SDF Collider 按网格计算惯量，导出为 `type="sdf"`；与 Visual 共享网格时复用同一 mesh 资源，单独导出时使用 STL 资源。

## 3.5 Height Field 与 Plane

这两个按钮只在没有选中对象时可用，创建结果位于 World。当前无弹窗。

| 按钮                | Operator ID                 | 结果                                              |
| ------------------- | --------------------------- | ------------------------------------------------- |
| Create height field | `forge.create_height_field` | 创建 Height Field；详细参数在 Properties 中编辑。 |
| Create plane        | `forge.create_plane`        | 创建 Plane；详细参数在 Properties 中编辑。        |

## 3.6 Mesh Check

**按钮：** **Check Mesh(s)**

**Operator ID：** `forge.mesh_check`

只对全部为 **Visual** 的选择可用。它检查网格是否满足惯量计算等后续操作的要求，并在状态/报告区域显示错误和耗时。

- 检查 **Visual** 模型是不是流形；
- 检查 **Visual** 模型是不是存在穿插。

**Compute Inertial** 仅在勾选 **Check Geometry** 时执行计算前检查（默认关闭），检查对象由其 **Visual / Collider** 来源决定。若检查失败，应先修复非封闭、退化或其他无效网格。

## 3.7 Material 分组

<div align="center">
  <img src="../../assets/images/manual/03-mat-define.png" alt="Material 分组">
</div>

**按钮：** **Common Material**

**Operator ID：** `forge.create_material`

弹窗：

<div align="center">
  <img src="../../assets/images/manual/03-mat-creation.png" alt="Create Material">
</div>

所选对象全部为 **Visual**、**Height Field** 或 **Plane** 时可用，可创建纯参数材质：

1. 选择 **Forge PBR Library** 的 **Category**；
2. 选择 **Material**；
3. **Use Existing** 开启时，优先复用 **Blender** 中的同名材质；
4. 确认后，将复用或新建的材质分配给全部所选对象的第一个 **Material Slot**。复用时保留已有材质的设置；新建时使用材质库参数。**Visual**、**Height Field** 和 **Plane** 都使用对象级材质槽。

材质名称的结尾后缀决定导出时的 MJCF `alpha_mode`：

| 名称后缀    | 导出的 `alpha_mode` |
| ----------- | ------------------- |
| `_blend`    | `blend`             |
| `_mask`     | `mask`              |
| `_multiply` | `multiply`          |

后缀是材质名称的一部分，导出的 `<material name>` 同样保留该后缀；没有上述后缀时使用 MJCF 默认的不透明模式。

### • 赋予现有材质

**按钮：** **Assign Material**

**Operator ID：** `forge.assign_material`

弹窗：

<div align="center">
  <img src="../../assets/images/manual/03-mat-assign.png" alt="Assign Material">
</div>

1. 选中一个或多个 **Visual**、**Height Field** 或 **Plane** 对象。
2. 在 **Material** 分组点击 **Assign Material**。
3. 从可搜索的 **Material** 下拉菜单中选择 Blender 中已有的材质并确认。活动对象已有材质时，弹窗默认选中该材质。

所选材质会赋给全部选中对象的第一个对象级 **Material Slot**；没有材质槽时自动创建，其他槽位保留。操作直接复用现有材质及其节点和设置，不创建副本。未选中的对象保留原有材质分配，包括共享同一网格的对象。没有可选材质时，请先创建或导入材质。

### • 创建棋盘格材质

**按钮：** **Checker Material**

**Operator ID：** `forge.create_checker_material`

弹窗：

<div align="center">
  <img src="../../assets/images/manual/03-mat-checker.png" alt="Checker Material">
</div>

选中一个或多个 **Visual**、**Height Field** 或 **Plane** 对象，在 **Material** 分组点击 **Checker Material**。所有选中对象都必须属于这三种类型。

| 参数 | 含义 | 默认值 |
| --- | --- | --- |
| **Color 1** | 第一种棋盘格颜色 | 黑色 |
| **Color 2** | 第二种棋盘格颜色 | 白色 |
| **Repeat** | UV 两个方向的整数重复次数，范围为 1～128 | 4 |

确认后创建新材质，并分配给全部所选对象的第一个对象级 **Material Slot**。每次执行都会创建新材质，本次所选对象共用该材质。

生成的节点连接为 **Texture Coordinate（UV）→ Mapping → Checker Texture → Principled BSDF（Base Color）**。**Repeat** 设置 Mapping 的 Scale X、Y，Z 保持为 1；Checker Texture 节点的 **Scale** 为 2。编辑需要导出到 MJCF 的棋盘格时，请保留这套节点连接和 Scale，通过 Mapping 调整平铺次数。

导出时生成 MJCF 原生的 `<texture type="2d" builtin="checker">`，并在材质中通过 RGB 纹理层引用，无需烘焙或写出图像文件。**Color 1 / Color 2** 对应 `rgb1` / `rgb2`，Blender 的线性颜色会转换为 sRGB。Mapping 的 Scale X、Y 对应材质的 `texrepeat`；两值相同时写入 `texuniform="true"`，否则为 `false`。纹理定义会放在引用它的材质之前。

开启 **Import material** 后，导入 MJCF 的二维内置 checker 贴图会恢复 UV、Mapping、Checker Texture 节点、颜色和 `texrepeat`。支持材质的 `texture` 属性引用，以及 RGB/RGBA `<layer>` 引用。导入的 U、V 重复次数可以不同；创建弹窗中的 **Repeat** 则同时设置两个方向。

### • 创建自定义材质

下图中是带纹理贴图的完整自定义材质样板，其中4个框的内容可以单独断开链接到 BSDF 节点，用 BSDF 的纯参数。场景会根据是否链接到 BSDF 节点导出依赖参数和贴图。

<div align="center">
  <img src="../../assets/images/manual/03-material-node.png" alt="Custom Material">
</div>

> 图像贴图材质应遵循上图的节点连接方式；程序化棋盘格使用上一节说明的节点连接方式。
> 纯参数材质不需要链接任何节点到 BSDF 节点。
> 如果不需要 **Tiling**（平铺），可以不将 **Mapping** 节点连接到贴图节点。

---

[上一章：Global 与 General](02_global_and_general.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/03_geometry_and_material.md) · [下一章：Kinematics](04_kinematics.md)
