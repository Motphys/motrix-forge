# Chapter 10: Troubleshooting and scripting

[Previous: CoACD](09_coacd.md) · [Contents](../forge_docs.md) · [中文](../../cn/forge_docs/10_troubleshooting_and_scripting.md)

## 10.1 Why did Definition change only one object?

**Definition** for **Geometry**, **Collider**, **Site**, **Joint**, and **Actuator** changes only the active object by default. To batch-edit, enable **Apply to all selected** in the dialog.

## 10.2 Target or Reference order is reversed

Deselect everything, then select again in the correct order:

- **Equality:** the first is Target 1/parent; the second is Target 2.
- **Sensor Reference:** the first is Target; the second is Reference.
- **Targetbody Light:** with one Link, that Link is the target; with two Links, the first is the Light position/parent and the second is the tracking target.
- **Targetbody Camera:** with one Link, that Link is the target; with two Links, the first is the Camera position/parent and the second is the tracking target.
- **Tendon:** Joints are added to the target list in selection order.
- **Link Parent:** the exception; the active object is always the parent and must be activated last.

## 10.3 Compute Inertial finds no geometry or fails

Ensure **Inertial Model Type** matches the intended **Visual / Collider** source and that geometry is a direct child of the selected **Link**, or inside its **Frame** descendants. Child Links are not searched. Mesh calculation requires **TetGen**; enable **Check Geometry** for validation and repair failures reported for the mesh. Box, Sphere, Cylinder, and Capsule use shape parameters directly and do not require TetGen. See [4.5](04_kinematics.md#45-compute-inertial).

## 10.4 The original object is no longer selected after creation

Most **Creation Operators** clear the original selection and select the newly created objects. This is expected. To continue creating child elements on the original **Link**, select the Link again.

## 10.5 Shape Size and Object Scale

Prefer editing **Size**, **Radius**, and **Height** in **Shape Properties**. Primitive shapes are normally controlled by **Geometry Nodes Modifier** parameters and lock **Object Scale**. After changing to **Mesh**, the geometry is baked into the mesh and Object Scale may become editable again.

## 10.6 Operator ID quick reference

### Creation

| Function | Operator ID |
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

| Function | Operator ID |
| --- | --- |
| Model | `forge.define_model_type` |
| Geometry / Collider / Site | `forge.define_geometry_type` / `forge.define_collider_type` / `forge.define_site_type` |
| Joint / Actuator | `forge.define_joint_type` / `forge.define_actuator_type` |
| Parent / Root | `forge.define_parent` / `forge.mark_root_link` |
| Instance Link | `forge.mark_instance_link` |
| Mesh / Gizmo | `forge.mesh_check` / `forge.scale_gizmo_size` |

### Utility, IO, and CoACD

| Function | Operator ID |
| --- | --- |
| Batch Rename / Tag Select | `forge.batch_rename` / `forge.select_by_tag` |
| Model Type Select | `forge.select_by_model_type` |
| Select Hulls / Instance ID | `forge.select_hulls` / `forge.set_instance_idname` |
| Instance Link marker | `forge.mark_instance_link` (see [4.7](04_kinematics.md#47-instance-rules)) |
| Import / Export | `forge.import_mjcf` / `forge.export_mjcf` |
| Attach / Include | `forge.create_attach` / `forge.create_include` |
| CoACD | `forge.coacds` |

### Properties

Properties operators use the common `forge.properties_*` naming scheme, including `global`, `visual`, `hfield`, `plane`, `shape`, `shape_site`, `link`, `joint`, `actuator`, `tendon`, `equality`, `contact`, `sensor`, `light`, `camera`, and `replicate`.

## 10.7 Blender Python example

```python
import bpy

# Ensure Object Mode and deselect every object first.
if bpy.context.mode != "OBJECT":
    raise RuntimeError("Forge operators require Object Mode")
bpy.ops.object.select_all(action="DESELECT")

bpy.ops.forge.create_geometry(
    geometry_type="BOX",
    size_box=(1.0, 2.0, 0.5),
)
```

**Operator** calls are constrained by the current **Blender Context** and `poll` conditions. Before batch operations, set explicitly:

- **Object Mode**;
- the selected objects;
- the active object; and
- the **Forge** selection order when two targets are required.

---

[Previous: CoACD](09_coacd.md) · [Contents](../forge_docs.md) · [中文](../../cn/forge_docs/10_troubleshooting_and_scripting.md)
