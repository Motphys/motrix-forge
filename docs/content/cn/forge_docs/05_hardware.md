# 第 5 章：Model Define — 硬件

[上一章：Kinematics](04_kinematics.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/05_hardware.md) · [下一章：Meta Elements](06_meta_elements.md)

## 5.1 Hardware 分组布局

**Hardware** 从上到下包括 **Create Actuator/Site**、**Define Actuator/Site**、**Create Tendon/Equality**、**Create Sensor/Contact**、**Create Light/Camera**。

<div align="center">
  <img src="../../assets/images/manual/05-hardware-region.png" alt="Hardware 分组">
</div>

## 5.2 Actuator

### Create actuator(s)

**Operator ID：** `forge.create_actuator`

弹窗：
<div align="center">
  <img src="../../assets/images/manual/05-actuator-creation.png" alt="Create actuator(s)">
</div>

所选对象必须全部为 **Link**、**Joint** 或 **Tendon**。**Forge** 为每个目标创建一个 **Actuator**，类型为 **General**、**Motor**、**Position**、**Velocity** 或 **Adhesion**，默认为 **Position**。

### Define actuator(s)

**Operator ID：** `forge.define_actuator_type`

弹窗：
<div align="center">
  <img src="../../assets/images/manual/05-actuator-define.png" alt="Define actuator(s)">
</div>

所选对象必须全部为 **Actuator**。默认只修改活动对象；勾选 **Apply to all selected** 后批量修改。

## 5.3 Site

### Create site(s)

**Operator ID：** `forge.create_site`

弹窗：
<div align="center">
  <img src="../../assets/images/manual/05-site-creation.png" alt="Create site(s)">
</div>

所选对象必须全部为 **Link**。**Forge** 为每个 **Link** 创建一个 **Site**；类型可选 **Box**、**Capsule**、**Cylinder**、**Sphere**，并可设置 **Size**、**Radius** 或 **Height**。

### Define site(s)

**Operator ID：** `forge.define_site_type`

弹窗：
<div align="center">
  <img src="../../assets/images/manual/05-site-define.png" alt="Define site(s)">
</div>

所选对象必须全部为 **Site**。可修改为 **Box**、**Capsule**、**Cylinder** 或 **Sphere**；默认只修改活动 **Site**，可用 **Apply to all selected** 批量修改。

## 5.4 Create Tendon

**Operator ID：** `forge.create_tendon`

弹窗：
<div align="center">
  <img src="../../assets/images/manual/05-tendon-creation.png" alt="Create tendon">
</div>

至少选择两个 **Joint**，且全部必须为 **Slide** 或 **Hinge**。**Forge** 按选择顺序把这些 **Joint** 组成一个 **Fixed Tendon**。

## 5.5 Create Equality

**Operator ID：** `forge.create_equality`

弹窗：
<div align="center">
  <img src="../../assets/images/manual/05-equality-creation.png" alt="Create equality">
</div>

必须恰好选择两个同类对象：

- 两个 **Link** 或两个 **Site**：可选 **Connect**、**Weld**；
- 两个 **Joint**：只可选 **Joint Equality**。

第一个选择对象是 **Target 1**，同时也是新 **Equality** 对象的父对象；第二个是 **Target 2**。

## 5.6 Create Sensor(s)

**Operator ID：** `forge.create_sensor`

弹窗：
<div align="center">
  <img src="../../assets/images/manual/05-sensor-creation.png" alt="Create sensor(s)">
</div>

**Sensor Type** 会根据选择动态变化：

- **Link**：**Body Sensor**（**Frame** 系列、**Contact**、**Subtreecom/Subtreelinvel/Subtreeangmom**）；勾选 **Use Xbody** 后仅 Frame 系列，勾选 **Use Subtree** 后仅 **Contact**。
- **Joint**：只提供 **Joint** 支持的 **Sensor**；**Joint** 不能作为 **Frame Sensor** 的 **Target/Reference**。
- **Site**、**Visual/Collider**、**Camera**：提供对应目标类型支持的 **Sensor**。
- 恰好选择两个兼容对象时可启用 **Use Reference**；第一个是 **Target**，第二个是 **Reference**。

注意：

- **Use Xbody** 与 **Use Subtree** 互斥；
- 切换 **Reference/Xbody/Subtree** 会重置 **Sensor Type**；
- 下拉框显示 `None` 表示当前组合没有合法 **Sensor**。

## 5.7 Create Contact

**Operator ID：** `forge.create_contact`

弹窗：
<div align="center">
  <img src="../../assets/images/manual/05-contact-creation.png" alt="Create contact">
</div>

- 至少选择两个 **Link**：创建 **Exclude**。
- 至少选择两个 **Visual/Collider/Plane/Height Field**：创建 **Pair**。
- 选择超过两个对象：为所有对象两两组合创建 **Contact**。

每个 **Contact** 的第一个目标也是其父对象。

## 5.8 Light

**Operator ID：** `forge.create_light`

弹窗：
<div align="center">
  <img src="../../assets/images/manual/05-light-creation.png" alt="Create light">
</div>

未选择对象或所选对象全部为 **Link** 时可用。类型：无选择时为 **Directional**、**Spot**、**Point**（默认 **Directional**），选择 **Link** 时仅 **Spot**、**Point**（默认 **Spot**）；模式：选择 1～2 个 **Link** 时为全部五种（默认 **Targetbody**），无选择或选择 ≥3 个 **Link** 时仅 **Fixed**、**Track**、**Trackcom**（默认 **Fixed**）。

- 无选择：在 **3D Cursor** 位置创建 **World Light**。
- 普通跟踪模式：为每个所选 **Link** 创建子 **Light**。
- 选择一个 **Link** 并使用 **Targetbody/Targetbodycom** 模式：在 **3D Cursor** 位置创建 **World Light**，并以该 **Link** 为目标。
- 选择两个 **Link** 并使用 **Targetbody/Targetbodycom** 模式：第一个是 **Light** 的位置（父对象），第二个是目标，创建单个 **Light**。

## 5.9 Camera

弹窗：
<div align="center">
  <img src="../../assets/images/manual/05-camera-creation.png" alt="Create camera">
</div>

**Operator ID：** `forge.create_camera`

未选择对象或所选对象全部为 **Link** 时可用。类型为 **Perspective** 或 **Orthographic**；模式：选择 1～2 个 **Link** 时为全部五种（默认 **Targetbody**），无选择或选择 ≥3 个 **Link** 时仅 **Fixed**、**Track**、**Trackcom**（默认 **Fixed**）。

- 无选择：在 **3D Cursor** 位置创建 **World Camera**。
- 普通跟踪模式：为每个所选 **Link** 创建子 **Camera**。
- 选择一个 **Link** 并使用 **Targetbody/Targetbodycom** 模式：在 **3D Cursor** 位置创建 **World Camera**，并以该 **Link** 为目标；其他模式为该 **Link** 创建子 **Camera**。
- 选择两个 **Link** 并使用 **Targetbody/Targetbodycom** 模式：第一个是 **Camera** 的位置（父对象），第二个是目标，创建单个 **Camera**。

---

[上一章：Kinematics](04_kinematics.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/05_hardware.md) · [下一章：Meta Elements](06_meta_elements.md)
