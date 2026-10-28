# 第 4 章：Model Define — 运动学与实例

[上一章：Geometry 与 Material](03_geometry_and_material.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/04_kinematics.md) · [下一章：Hardware](05_hardware.md)

## 4.1 Kinematics 分组布局

<div align="center">
  <img src="../../assets/images/manual/04-kinematics-region.png" alt="Kinematics 分组">
</div>

| 按钮               | Operator ID               | 可用条件                                                  |
| ---------------- | ------------------------- | ----------------------------------------------------- |
| Create link(s)   | `forge.create_link`       | 未选择；所选对象均属于 Link/Frame/Replicate；或均属于 Visual/Collider |
| Create joint(s)  | `forge.create_joint`      | 所选对象均为 Link                                           |
| Mark root        | `forge.mark_root_link`    | 所选对象均为 Link、Frame 或 Replicate                       |
| Define joint(s)  | `forge.define_joint_type` | 所选对象均为 Joint                                          |
| Link Parent      | `forge.define_parent`     | 活动对象和其他所选对象满足合法父子类型                                   |
| Compute Inertial | `forge.create_inertial`   | 所选对象均为 Link                                           |
| Mark Instance Link | `forge.mark_instance_link` | 所选对象均为 Link（使用规则见 [4.7](#47-instance-使用规则)）        |
| Set instance idname | `forge.set_instance_idname` | 所选对象均为 Link、Frame 或 Visual（只修改其中未标记 `INSTANCE_LINK` 的 Link） |

## 4.2 创建 Link

### Create link(s)

- 未选择对象：创建顶层 Link。
- 选择 Link/Frame/Replicate：为每个对象创建子 Link。
- 选择 Visual/Collider：根据所选几何对象创建 Link。
- `Shift + 点击`：反向父子关系——在所选 **Link/Frame/Replicate** 的位置和朝向创建新的父 **Link**，并把所选对象改为该 **Link** 的子对象。与 **Create frame(s)** 的 `Shift + 点击` 行为一致。

创建完成后，新 Link 会成为当前选择。无弹窗。

## 4.3 创建与定义 Joint

### Create joint(s)

为每个所选 **Link** 创建 **Joint**。类型为 **Free**、**Ball**、**Slide**、**Hinge**，默认为 **Hinge**。

弹窗：
<div align="center">
  <img src="../../assets/images/manual/04-joint-creation.png" alt="Create joint(s)">
</div>

### Define joint(s)

- 弹窗以活动 **Joint** 的类型为初始值，默认只修改活动对象；
- 勾选 **Apply to all selected** 后修改全部所选 Joint。
- 类型变更时会同步更新 **Joint** 的显示形状。

弹窗：
<div align="center">
  <img src="../../assets/images/manual/04-joint-define.png" alt="Define joint(s)">
</div>

## 4.4 Link Parent

**Link Parent** 始终把活动对象作为父对象，无弹窗：

- 活动对象为 **Link**、**Frame** 或 **Replicate**，其他所选对象必须都是允许的 **Link** 子元素：
- **Link**、**Frame**、**Replicate**、**Visual**、**Collider**、**Joint**、**Site**、**Light**、**Camera**、**Attach**
- 活动对象为 **Visual** 时该操作不可用：**Collider** 应与 **Visual** 同级挂在 **Link** 之下，**Collider** 套在 **Visual** 里不会导出。
- 被移动的 **Visual** 原有子对象（例如仍绑定到它的 **Collider**）会先重新挂到新的活动父对象下，从而修复旧的 **Collider** 套 **Visual** 层级。
- 被重新挂接的对象会同时移入其模型类型对应的集合 —— **Visual** 进 `Visual`，**Collider** 进 `Collider`，以此类推。在世界根下创建的对象位于 `World`，挂接后才移出。

操作步骤：

1. 先选择需要移动的子对象。
2. 最后选择目标父对象，使其成为活动对象。
3. 点击 **Link Parent**。

## 4.5 Compute Inertial

选中一个或多个 **Link**，点击 **Compute Inertial**。弹窗包含：

| 参数 | 默认值 | 作用 |
| --- | --- | --- |
| Inertial Model Type | Visual | 选择以 **Visual** 或 **Collider** 作为计算来源 |
| Check Geometry | 关闭 | 计算前检查所收集几何的有效性；检查失败则跳过该 Link |

- 收集所选类型的直接子对象，并递归进入 **Frame** 子层级；不会进入子 **Link** 的层级，也不会混用 Visual 和 Collider。
- **Box / Sphere / Cylinder / Capsule** 根据形状参数直接计算实体质量和惯量，无需 TetGen；会计入世界变换中的缩放（包括非均匀缩放）、镜像及父级引入的剪切。
- **Mesh** 使用应用修改器后的网格，经 **TetGen** 四面体化计算；需要安装 TetGen，并提供可用于体积计算的有效网格。
- 密度默认取每个对象的 `Forge_Geometry.density`；若第一个材质槽的材质含 `density` 自定义属性，则优先使用材质密度。
- 多个几何对象的质量、质心和惯量会合并。计算成功后，在 Link 下新建 **Inertial** 并选中；不会替换已有 Inertial，重复计算前应先清理旧对象。
- 找不到匹配几何、启用检查后检查失败或惯量计算失败时，该 Link 不会生成新的 Inertial；错误详情见报告区域。

推荐流程：确认几何类型、尺寸和密度，选择 **Link**，在弹窗选择 **Visual / Collider**；需要计算前检查时启用 **Check Geometry**。独立的 **Check Mesh(s)** 按钮仍只接受 Visual。

### 惯量预览

**Inertial** 使用与质量和对角惯量等效的长方体显示，位置为质心、方向为惯性主轴。修改质量或惯量会更新显示；其显示尺寸不受 **Gizmo display size** 控制。物理位置和旋转相对于父 Link 保存，显示用缩放不写入 MJCF 惯量位姿。

惯量属性编辑见[第 7 章](07_properties.md)，预览开关见[第 0 章](00_ui_overview.md)。

## 4.6 Mark root

给没有父对象的所选 **Link/Frame/Replicate** 写入 `Root Link` 标记。有父对象的将断开父子链接并标记，并会显示警告。无弹窗。

## 4.7 Instance 使用规则

**Instance** 用于把同一个 **Link** 子树（如夹爪、车轮）复用到多个位置：被标记的 **Instance Link** 只作为"模板"提供内容，导出时它的子物体会自动写入各个引用它的 **Link** 之下。

对应 **Kinematics** 下方独立的 **Instance** 分组，包含三行：**Mark Instance Link** 按钮、**Instance** 字段、**Set instance idname** 按钮。

<div align="center">
  <img src="../../assets/images/manual/04-instance-region.png" alt="Instance 分组">
</div>
### 概念

| 名称                 | 标记                          | 说明                                                                                          |
| ------------------ | --------------------------- | ------------------------------------------------------------------------------------------- |
| Instance Link（实例源） | `INSTANCE_LINK` 自定义属性       | 由 **Mark Instance Link** 写入 / 再次点击取消；导出时不作为 `<body>` 出现；未被引用时**完全不导出**（含资产）                  |
| 占位 Link            | `INSTANCE_IDNAME` 自定义属性     | 由 **Instance 字段 + Set instance idname** 写入；保留自己的 Link（名字、位姿、属性），子物体被替换为 Instance Link 的子树副本 |
| Instance 字段        | `Forge_Props.instance_body` | 选择列表**只列出已标记的 Instance Link**                                                               |

### 使用步骤

1. 在场景中搭建一个模板 **Link**（含 Joint、Visual、子 Link 等），放在世界根层级并保持可见。
2. 选中模板 **Link**，点击 **Mark Instance Link**（打上 `INSTANCE_LINK` 标记；再点一次则取消）。
3. **Instance** 字段中选择该模板。
4. 选中一个或多个占位 **Link** 并且未被标记为 `INSTANCE_LINK`（通常是在目标父级下新建的空 **Link**），点击 **Set instance idname** 写入 `INSTANCE_IDNAME`；**Instance** 字段为空时点击会清除所选 Link 的引用。
5. 正常导出（见[第 8 章](08_import_export.md)）。

### 导出规则

- **Instance Link 本体不导出**为 `<body>`；被占位 **Link** 引用时，其子树的 mesh、材质资产会随副本导出；
- **未被任何占位 Link 引用的 Instance Link 完全不导出**——不写 `<body>`，也不导出其子树的任何资产（显示警告）。
- 每个占位 **Link** 导出自己的 `<body>`（名字、pos、quat、属性），子物体替换为模板子树的完整副本：
- 副本内所有元素名自动加前缀 `<占位 Link 名>_`（如 `grip_l_finger`），多份副本之间不会重名；名称仍冲突时自动追加 `_inst` 后缀；
- 副本内 **Camera / Light** 的 `target` 引用会同步改名；
- 模板子树的 **mesh**、材质资产只导出一份，被所有副本共享。
- 占位 **Link** 自己的子物体**不会导出**，也不参与资产收集。
- 全局段（`actuator`、`sensor`、`tendon`、`equality`、`contact`）不会按副本复制，也不要引用 **Instance Link** 内部的元素名。

### 注意事项

- `INSTANCE_IDNAME` 保存的是对 Instance Link 对象的引用而非名称，因此重命名模板后引用依然有效；旧文件中保存为名称的标记在导出时也能被识别。
- `INSTANCE_IDNAME` 指向的对象被删除或不再是 **Link** 时，该占位 **Link** 回退为普通导出并显示警告。
- 已标记为 **Instance Link** 的 **Link** 不能再被设置 `INSTANCE_IDNAME`（会跳过并显示警告）；模板子树内部的 `INSTANCE_IDNAME` 标记在复制时会被忽略（副本是纯内容拷贝）。
- 嵌套在模板子树内部的 **Instance Link** 不会作为 `<body>` 复制进副本，其内容仍只经由引用它的占位 **Link** 导出（未被引用则不导出）。
- **Instance** 标记是 **Blender** 侧的创作概念，重新 **Import MJCF** 不会还原。

### MCP 调用

```python
forge_mark_instance_link(select=["gripper"])                  # 标记 / 取消标记模板
forge_set_scene_property(group="forge_props", values={"instance_body": "gripper"})
forge_set_instance_idname(select=["arm_l", "arm_r"])          # 占位 Link 写入引用
```

---

[上一章：Geometry 与 Material](03_geometry_and_material.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/04_kinematics.md) · [下一章：Hardware](05_hardware.md)
