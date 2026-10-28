# 第 10 章：常见问题与脚本调用

[上一章：CoACD](09_coacd.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/10_troubleshooting_and_scripting.md)

## 10.1 Definition 为什么只修改了一个对象？

**Geometry**、**Collider**、**Site**、**Joint** 和 **Actuator** 的 **Definition** 默认只修改活动对象。需要批量修改时，在弹窗中勾选 **Apply to all selected**；

## 10.2 Target 或 Reference 顺序反了

取消选择，再按正确顺序重新选择：

- **Equality**：第一个是 Target 1/父对象，第二个是 Target 2。
- **Sensor Reference**：第一个是 Target，第二个是 Reference。
- **Targetbody Light**：一个 Link 时该 Link 是目标；两个 Link 时第一个是 **Light** 位置/父对象，第二个是跟踪目标。
- **Targetbody Camera**：一个 Link 时该 Link 是目标；两个 Link 时第一个是 **Camera** 位置/父对象，第二个是跟踪目标。
- **Tendon**：Joint 按选择顺序加入目标列表。
- **Link Parent**：例外；活动对象始终是父对象，应最后激活。

## 10.3 Compute Inertial 找不到几何或计算失败

确认弹窗的 **Inertial Model Type** 与要使用的 **Visual / Collider** 一致，且几何是所选 **Link** 的直接子对象，或位于其 **Frame** 子层级中；不会搜索子 Link。Mesh 计算需要安装 **TetGen**；启用 **Check Geometry** 可先检查几何，失败时根据报告修复网格。Box、Sphere、Cylinder、Capsule 直接使用形状参数，不需要 TetGen。详细流程见[4.5](04_kinematics.md#45-compute-inertial)。

## 10.4 创建操作后原对象不再选中

多数 **Creation Operator** 会清除原选择，并选中新创建的对象。这是预期行为。要继续在原 **Link** 上创建其他子元素，需要重新选择 **Link**。

## 10.5 Shape Size 与 Object Scale

优先在 **Shape Properties** 中修改 **Size**、**Radius**、**Height**。Primitive 类型通常由 **Geometry Nodes Modifier** 参数控制并锁定 **Object Scale**；切换为 **Mesh** 后，几何会被烘焙到网格，Object Scale 可能重新可编辑。

## 10.6 Operator ID 速查

### Creation

| 功能 | Operator ID |
| --- | --- |
| Geometry / Collider / Site | `forge.create_geometry` / `forge.create_collider` / `forge.create_site` |
| Height Field / Plane | `forge.create_height_field` / `forge.create_plane` |
| Link / Joint / Inertial | `forge.create_link` / `forge.create_joint` / `forge.create_inertial` |
| Actuator / Tendon / Equality | `forge.create_actuator` / `forge.create_tendon` / `forge.create_equality` |
| Sensor / Contact | `forge.create_sensor` / `forge.create_contact` |
| Light / Camera | `forge.create_light` / `forge.create_camera` |
| Frame / Replicate | `forge.create_frame` / `forge.create_replicate` |
| Material | `forge.create_material` |

### Definition

| 功能 | Operator ID |
| --- | --- |
| Model | `forge.define_model_type` |
| Geometry / Collider / Site | `forge.define_geometry_type` / `forge.define_collider_type` / `forge.define_site_type` |
| Joint / Actuator | `forge.define_joint_type` / `forge.define_actuator_type` |
| Parent / Root | `forge.define_parent` / `forge.mark_root_link` |
| Instance Link | `forge.mark_instance_link` |
| Mesh / Gizmo | `forge.mesh_check` / `forge.scale_gizmo_size` |

### Utility、IO 与 CoACD

| 功能 | Operator ID |
| --- | --- |
| Batch Rename / Tag Select | `forge.batch_rename` / `forge.select_by_tag` |
| Model Type Select | `forge.select_by_model_type` |
| Select Hulls / Instance ID | `forge.select_hulls` / `forge.set_instance_idname` |
| Instance Link 标记 | `forge.mark_instance_link`（使用规则见 [4.7](04_kinematics.md#47-instance-使用规则)） |
| Import / Export | `forge.import_mjcf` / `forge.export_mjcf` |
| Attach / Include | `forge.create_attach` / `forge.create_include` |
| CoACD | `forge.coacds` |

### Properties

Properties Operator 使用统一的 `forge.properties_*` 命名，包括 `global`、`visual`、`hfield`、`plane`、`shape`、`shape_site`、`link`、`joint`、`actuator`、`tendon`、`equality`、`contact`、`sensor`、`light`、`camera`、`replicate`。

## 10.7 Blender Python 示例

```python
import bpy

# 先确保处于 Object Mode，并取消选择全部对象。
if bpy.context.mode != "OBJECT":
    raise RuntimeError("Forge operators require Object Mode")
bpy.ops.object.select_all(action="DESELECT")

bpy.ops.forge.create_geometry(
    geometry_type="BOX",
    size_box=(1.0, 2.0, 0.5),
)
```

**Operator** 调用受当前 **Blender Context** 和 `poll` 条件约束。批处理前应显式设置：

- **Object Mode**；
- 选择对象；
- 活动对象；
- 需要双目标时的 **Forge** 选择顺序。

---

[上一章：CoACD](09_coacd.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/10_troubleshooting_and_scripting.md)
