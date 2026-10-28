# 第 7 章：属性编辑

[上一章：Meta Elements](06_meta_elements.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/07_properties.md) · [下一章：Import 与 Export](08_import_export.md)

## 7.1 三个属性入口

### Model Define → Global

用于 Scene 级的 Global Properties 与 Visual Properties，详见第 2 章。必须先取消所有对象选择。

### 3D 视图属性 Gizmo

在 **Object Mode** 中选择 **Forge** 对象后，点击随对象显示的彩色 **Gizmo**，可打开对应的 **Properties** 弹窗。

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <strong>蓝色 Gizmo</strong>
  </div>
  <div style="flex: 1.8; text-align: center; ">
    <strong>点击 Gizmo 后</strong>
  </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/07-gizmo-properties-0.png"
      width="300"
      alt="对象属性 Gizmo">
  </div>
  <div style="flex: 1.8; text-align: center; ">
    <img
      src="../../assets/images/manual/07-gizmo-properties-1.png"
      width="580"
      alt="Gizmo 打开的属性弹窗">
  </div>
</div>

### Object Properties → Forge Properties

显示活动对象的：

- **Local/World Location** 与 **Rotation**；
- **Dimensions**；
- **Parent**；
- **Forge Model Type**；
- 当前类型对应的模型属性数据。

面板查看步骤：

1. 打开 `Properties` 窗口 ![Properties 窗口位置](../../assets/images/manual/07-forge-properties-area.png)；
2. 切换到 `Object Properties` 页签 ![Object Properties 页签](../../assets/images/manual/07-forge-properties-tab.png)；
3. 展开 `Forge Properties`，查看当前 Model Type 对应的属性。

<div align="center">
  <img src="../../assets/images/manual/07-forge-properties.png" alt="Forge properties">
</div>

## 7.2 看不到属性 Gizmo

请依次确认：

1. 当前在 **3D** 视图 且处于 **Object Mode** ![](../../assets/images/manual/07-object-model.png)。
2. **3D** 视图的 **Gizmos** 显示已开启 ![](../../assets/images/manual/07-3d-gizmo.png)。
3. 活动对象的 **Blender** 类型和 **Forge** 类型正确。
4. 形状类对象仍具有 **Forge** 创建时添加的 **Geometry Nodes Modifier**。

## 7.3 对象属性弹窗一览

以下属性弹窗均为 UI-only Operator，供 Blender 界面交互使用。

### Height Field

**Operator ID：** `forge.properties_hfield`

| 主要可编辑内容                                                                                             |
| --------------------------------------------------------------------------------------------------- |
| Nrow/Ncol、Elevation、X/Y Radius、Elevation Z、Base Z、Offset、Use Height Map、Height Map、接触/求解属性 |

弹窗：

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <strong>Hfield Properties</strong>
  </div>
  <div style="flex: 1; text-align: center; ">
    <strong>Model Properties</strong>
  </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/07-hfield-properties.png"
      width="412"
      alt="Hfield Properties弹窗">
  </div>
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/07-hfield-model-properties.png"
      width="412"
      alt="Hfield Model Properties弹窗">
  </div>
</div>

### Plane

**Operator ID：** `forge.properties_plane`

| 主要可编辑内容                                 |
| --------------------------------------- |
| X/Y Half Size、Infinite、接触/求解属性 |

弹窗：

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <strong>Plane Properties</strong>
  </div>
  <div style="flex: 1; text-align: center; ">
    <strong>Model Properties</strong>
  </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/07-plane-properties.png"
      width="412"
      alt="Hfield Properties弹窗">
  </div>
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/07-hfield-model-properties.png"
      width="412"
      alt="Hfield Model Properties弹窗">
  </div>
</div>

### Visual / Collider

**Operator ID：** `forge.properties_shape`

| 主要可编辑内容                                                                                                  |
| -------------------------------------------------------------------------------------------------------- |
| 基本形状尺寸；Group、Condim、Contype、Conaffinity、Priority、Friction、Mass、Density、Margin、Gap、Solver |

- **Box**：编辑 **X/Y/Z Size**。
- **Sphere**：编辑 **Radius**。
- **Capsule/Cylinder**：编辑 **Radius** 与 **Height**。
- **Mesh** 类型：没有 **Primitive Size** 输入，应修改 **Mesh** 本身或对象尺寸。

材质不在此弹窗中编辑。请使用 **Create Material**，或在 Blender 的对象材质槽中直接指定材质。

**Model Properties** 区域保存 **MJCF Geometry** 的碰撞、质量和 **Solver** 参数。弹窗：

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <strong>Visual Properties</strong>
  </div>
  <div style="flex: 1; text-align: center; ">
    <strong>Collider Properties</strong>
  </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/07-shape-properties-0.png"
      width="412"
      alt="Geom Properties弹窗">
  </div>
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/07-shape-properties-1.png"
      width="412"
      alt="Geom Properties弹窗">
  </div>
</div>

### Link

**Operator ID：** `forge.properties_link`

| 主要可编辑内容                                        |
| ---------------------------------------------- |
| Empty Display Type、Display Size、Mocap、Gravcomp |

弹窗：

<div align="center">
  <img src="../../assets/images/manual/07-link-properties.png" alt="Link properties">
</div>

### Site

**Operator ID：** `forge.properties_shape_site`

| 主要可编辑内容                                |
| -------------------------------------- |
| Box/Sphere/Capsule/Cylinder 的尺寸与 Group |

弹窗：

<div align="center">
  <img src="../../assets/images/manual/07-site-properties.png" alt="Site properties">
</div>

### Inertial

选中 **Inertial**，在 **Object Properties → Forge Properties → Inertial Info** 查看 `mass`、`diaginertia` 和 `fullinertia`。当前面板只读，也没有单独的惯量属性弹窗；需要修改数值时可通过 Python 操作对象的 `Forge_Inertial`：

```python
import bpy

inertial = bpy.context.active_object.Forge_Inertial
inertial.mass = 2.0
inertial.fullinertia = (0.2, 0.3, 0.4, 0.0, 0.0, 0.0)
```

- `diaginertia` 为惯性主轴坐标系下的三个对角分量；对象相对于父 Link 的旋转决定主轴方向，位置为质心。
- `fullinertia` 为质心处、以 **Link 坐标轴** 表达的完整对称惯量张量，顺序为 `Ixx, Iyy, Izz, Ixy, Ixz, Iyz`。它根据当前旋转和对角惯量实时派生。
- 写入非零 `fullinertia` 时需为正定张量；Forge 会分解它并同步更新主轴旋转与 `diaginertia`。脚本应一次赋值完整的六分量数组，避免逐分量写入不完整张量。
- 质量或惯量变更会更新等效长方体。质量须为有限正数、三个对角惯量须为有限正数且满足惯量三角关系，才会显示预览；不满足时不绘制。

### Joint

**Operator ID：** `forge.properties_joint`

| 主要可编辑内容                                                                                             |
| --------------------------------------------------------------------------------------------------- |
| Type、Display Size、Springdamper、Solver、Range、Force Range、Stiffness、Ref、Armature、Damping、Frictionloss |

弹窗：

<div align="center">
  <img
    src="../../assets/images/manual/07-joint-properties.png"
    width="412"
    alt="Joint Properties弹窗">

</div>

### Actuator

**Operator ID：** `forge.properties_actuator`

| 主要可编辑内容                                                           |
| ----------------------------------------------------------------- |
| Type、Target、控制/力范围、Gain/Bias 类型、类型专用参数、Gear/Dynamics/Gain/Bias 数组 |

弹窗：

<div align="center">
  <img
    src="../../assets/images/manual/07-actuator-properties.png"
    width="492"
    alt="Actuator Properties弹窗">

</div>

### Tendon

**Operator ID：** `forge.properties_tendon`

**Tendon** 可通过 `+` / `-` 增删 Target 列表项，对应 Operator 分别为 `forge.add_tendon_target_item` 和 `forge.remove_tendon_target_item`。这两个 Operator 也是 UI 辅助入口；脚本/MCP 应直接维护 Tendon 的 Target 集合。

| 主要可编辑内容                                                       |
| ------------------------------------------------------------- |
| Type、Target 列表增删、Range、Solver、Spring Length、Stiffness、Damping |

弹窗：

<div align="center">
  <img
    src="../../assets/images/manual/07-tendon-properties.png"
    width="412"
    alt="Tendon Properties弹窗">

</div>

### Equality

**Operator ID：** `forge.properties_equality`

**Equality** 的 **Active** 关闭后，主体参数不可编辑。

| 主要可编辑内容                       |
| ----------------------------- |
| Active、Type、Target 1/2、类型专用参数 |

弹窗：

<div align="center">
  <img
    src="../../assets/images/manual/07-equality-properties.png"
    width="412"
    alt="Equality Properties弹窗">

</div>

### Contact

**Operator ID：** `forge.properties_contact`

**Contact** 只有 **Pair** 类型显示碰撞和 **Solver** 参数。

| 主要可编辑内容                                                  |
| -------------------------------------------------------- |
| Type、Target 1/2；Pair 的 Condim、Friction、Solver、Margin、Gap |

弹窗：

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <strong>Exclude Properties</strong>
  </div>
  <div style="flex: 1; text-align: center; ">
    <strong>Pair Properties</strong>
  </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/07-contact-properties-0.png"
      width="412"
      alt="Contact Properties弹窗">
  </div>
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/07-contact-properties-1.png"
      width="412"
      alt="Contact Properties弹窗">
  </div>
</div>

### Sensor

**Operator ID：** `forge.properties_sensor`

**Frame Sensor** 可设置 **Reference**；**Contact Sensor** 会根据 **Target Type** 显示 **Link**、**Geom**、**Subtree** 或 **Site** 名称。

| 主要可编辑内容                                                                                     |
| ------------------------------------------------------------------------------------------- |
| Sensor/Target Type、Target、Reference、Xbody/Subtree、Noise、Cutoff；Contact Sensor 的 Data/Reduce |

弹窗：

<div align="center">
  <img
    src="../../assets/images/manual/07-sensor-properties.png"
    width="412"
    alt="Sensor Properties弹窗">

</div>

### Light

**Operator ID：** `forge.properties_light`

**Light** 只有 **Targetbody/Targetbodycom** 模式显示 **Target**。

| 主要可编辑内容                                                          |
| ---------------------------------------------------------------- |
| Type、Mode、Target、Shadow、Color、Energy、Size/Distance/Angle/Spot 参数 |

弹窗：

<div align="center">
  <img
    src="../../assets/images/manual/07-light-properties.png"
    width="412"
    alt="Light Properties弹窗">

</div>

### Camera

**Operator ID：** `forge.properties_camera`

**Camera** 只有 **Targetbody/Targetbodycom** 模式显示 **Target**。

| 主要可编辑内容                                           |
| ------------------------------------------------- |
| Type、Mode、Target、FOV 或 Ortho Scale、Clip Start/End |

弹窗：

<div align="center">
  <img
    src="../../assets/images/manual/07-camera-properties.png"
    width="412"
    alt="Camera Properties弹窗">

</div>

### Replicate

**Operator ID：** `forge.properties_replicate`

| 主要可编辑内容                      |
| ---------------------------- |
| Count、Offset、Euler、Separator |

弹窗：

<div align="center">
  <img
    src="../../assets/images/manual/07-replicate-properties.png"
    width="412"
    alt="Replicate Properties弹窗">

</div>

动态字段：

- **Global / Visual**：**Headlight** 和 **SSGI** 的详细参数分别受 **Active** 开关控制；关闭时对应字段会被禁用。
- **Height Field**：只有启用 **Use Height Map** 后才显示 **Height Map** 字段。
- **Plane**：**Infinite** 是独立开关，不会隐藏 **Half Size** 字段。
- **Visual / Collider**：几何类型决定尺寸字段；**Box** 显示三轴 **Size**，**Sphere** 显示 **Radius**，**Capsule/Cylinder** 显示 **Radius + Height**。**Mesh** 不显示 Primitive 尺寸。材质通过对象的第一个 **Material Slot** 管理。
- **Site**：几何类型决定显示 **Size**、**Radius** 或 **Radius + Height**。
- **Link**：**Display Type / Display Size / Mocap / Gravcomp** 始终显示，没有按类型隐藏的字段。
- **Joint**：**Free** 只显示基础的 **Stiffness / Armature / Damping / Frictionloss**；其他类型才显示 **Springdamper**、Solver、Range、Limited 等字段；**Ball** 不显示 **Actuator Force Range/Limited**。
- **Actuator**：**Position** 显示 **Kp / Kv / Inheritrange**，**Velocity** 显示 **Kv**，**Adhesion** 显示 **Gain**；其他类型显示 **Gear / Dynamics / Gain / Bias** 数组。
- **Tendon**：**Target** 字段来自可变长度的 Target 列表，列表项数量由 `+ / -` 控制。
- **Equality**：关闭 **Active** 时其余字段不可编辑；只有设置 **Target 1** 后才显示 **Target 2**，其余参数按 Equality 类型变化。
- **Contact**：只有 **Pair** 类型显示 **Condim、Friction、Solver、Margin、Gap**；**Exclude** 不显示这些字段。
- **Sensor**：**Contact** Sensor 会根据 **Target Type** 将目标字段标记为 **Link1/2、Geom1/2、Subtree1/2** 或 **Site**；Frame 类 Sensor 在设置 Target 后显示 **Reference** 与 **Use Xbody**，Contact 类 Sensor 在需要第二目标时显示 **Reference** 与 **Use Subtree**。
- **Light**：只有 **Targetbody/Targetbodycom** 模式显示 **Target**；**Spot/Point** 显示 **Shadow Soft Size / Cutoff Distance**，其他类型显示 **Angle**；**Spot** 额外显示 **Spot Size / Spot Blend**。
- **Camera**：只有 **Targetbody/Targetbodycom** 模式显示 **Target**；**Perspective** 显示 **FOV/Angle**，**Orthographic** 显示 **Ortho Scale**。
- **Replicate**：仅在对象仍具有 Replicate Modifier 时显示 **Count / Offset / Euler**；**Separator** 始终属于 Replicate 属性。

## 7.4 修改如何生效

属性弹窗直接修改 **Object**、**Modifier** 或 **Scene** 数据，不需要 **Apply/Save** 按钮。关闭弹窗后修改仍然保留，并可使用 **Blender Undo** 撤销。

优先在 **Properties** 中修改 **Size**、**Radius**、**Height**。**Forge** 的多个对象会锁定 **Object Scale**，形状尺寸由 **Geometry Nodes Modifier** 参数驱动。

---

[上一章：Meta Elements](06_meta_elements.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/07_properties.md) · [下一章：Import 与 Export](08_import_export.md)
