# Chapter 7: Properties editing

[Previous: Meta Elements](06_meta_elements.md) · [Contents](../forge_docs.md) · [中文](../../cn/forge_docs/07_properties.md) · [Next: Import and Export](08_import_export.md)

## 7.1 Three property entry points

### Model Define → Global

This entry edits scene-level Global Properties and Visual Properties; see Chapter 2. All objects must be deselected first.

### 3D View property gizmo

In **Object Mode**, select a **Forge** object and click the colored **Gizmo** shown next to the object to open its **Properties** dialog.

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; "><strong>Blue Gizmo</strong></div>
  <div style="flex: 1.8; text-align: center; "><strong>After clicking the Gizmo</strong></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/07-gizmo-properties-0.png" width="300" alt="Object property Gizmo"></div>
  <div style="flex: 1.8; text-align: center; "><img src="../../assets/images/manual/07-gizmo-properties-1.png" width="580" alt="Property dialog opened from the Gizmo"></div>
</div>

### Object Properties → Forge Properties

This panel displays the active object's:

- **Local/World Location** and **Rotation**;
- **Dimensions**;
- **Parent**;
- **Forge Model Type**; and
- model-property data for the current type.

To open the panel:

1. Open the `Properties` editor ![Properties editor location](../../assets/images/manual/07-forge-properties-area.png).
2. Switch to the `Object Properties` tab ![Object Properties tab](../../assets/images/manual/07-forge-properties-tab.png).
3. Expand `Forge Properties` to show properties for the current Model Type.

<div align="center"><img src="../../assets/images/manual/07-forge-properties.png" alt="Forge properties"></div>

## 7.2 The property gizmo is not visible

Check the following in order:

1. The current area is a **3D** View and Blender is in **Object Mode** ![](../../assets/images/manual/07-object-model.png).
2. **Gizmos** are enabled in the **3D** View ![](../../assets/images/manual/07-3d-gizmo.png).
3. The active object's **Blender** type and **Forge** type are correct.
4. A shape object still has the **Geometry Nodes Modifier** that Forge added during creation.

## 7.3 Object property dialogs

All dialogs below are UI-only Operators intended for interaction through the Blender interface.

### Height Field

**Operator ID:** `forge.properties_hfield`

| Main editable values |
| --- |
| Nrow/Ncol, Elevation, X/Y Radius, Elevation Z, Base Z, Offset, Use Height Map, Height Map, contact/solver properties |

Dialog:

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; "><strong>Hfield Properties</strong></div>
  <div style="flex: 1; text-align: center; "><strong>Model Properties</strong></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/07-hfield-properties.png" width="412" alt="Hfield Properties dialog"></div>
  <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/07-hfield-model-properties.png" width="412" alt="Hfield Model Properties dialog"></div>
</div>

### Plane

**Operator ID:** `forge.properties_plane`

| Main editable values |
| --- |
| X/Y Half Size, Infinite, contact/solver properties |

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; "><strong>Plane Properties</strong></div>
  <div style="flex: 1; text-align: center; "><strong>Model Properties</strong></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/07-plane-properties.png" width="412" alt="Plane Properties dialog"></div>
  <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/07-hfield-model-properties.png" width="412" alt="Hfield Model Properties dialog"></div>
</div>

### Visual / Collider

**Operator ID:** `forge.properties_shape`

| Main editable values |
| --- |
| Basic shape dimensions; Group, Condim, Contype, Conaffinity, Priority, Friction, Mass, Density, Margin, Gap, Solver |

- **Box:** edit **X/Y/Z Size**.
- **Sphere:** edit **Radius**.
- **Capsule/Cylinder:** edit **Radius** and **Height**.
- **Mesh:** there is no **Primitive Size** input; edit the **Mesh** itself or the object dimensions.

Materials are not edited in this dialog. Use **Create Material**, or assign a material directly in the Blender object material slots.

The **Model Properties** area stores collision, mass, and **Solver** parameters for the **MJCF Geometry**.

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; "><strong>Visual Properties</strong></div>
  <div style="flex: 1; text-align: center; "><strong>Collider Properties</strong></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/07-shape-properties-0.png" width="412" alt="Visual Properties dialog"></div>
  <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/07-shape-properties-1.png" width="412" alt="Collider Properties dialog"></div>
</div>

### Link

**Operator ID:** `forge.properties_link`

| Main editable values |
| --- |
| Empty Display Type, Display Size, Mocap, Gravcomp |

<div align="center"><img src="../../assets/images/manual/07-link-properties.png" alt="Link properties"></div>

### Site

**Operator ID:** `forge.properties_shape_site`

| Main editable values |
| --- |
| Box/Sphere/Capsule/Cylinder dimensions and Group |

<div align="center"><img src="../../assets/images/manual/07-site-properties.png" alt="Site properties"></div>

### Inertial

Select an **Inertial** to view `mass`, `diaginertia`, and `fullinertia` under **Object Properties → Forge Properties → Inertial Info**. This panel is read-only and there is no separate inertia properties dialog. To change values, use the object's `Forge_Inertial` through Python:

```python
import bpy

inertial = bpy.context.active_object.Forge_Inertial
inertial.mass = 2.0
inertial.fullinertia = (0.2, 0.3, 0.4, 0.0, 0.0, 0.0)
```

- `diaginertia` contains the three diagonal components in the principal inertia frame. The object's rotation relative to its parent Link defines the principal axes; its position is the center of mass.
- `fullinertia` is the symmetric tensor about the center of mass, expressed in **Link axes**, ordered `Ixx, Iyy, Izz, Ixy, Ixz, Iyz`. It is derived from the current rotation and diagonal inertia.
- A nonzero `fullinertia` assignment must be positive definite. Forge decomposes it and updates the principal rotation and `diaginertia`. Scripts should assign all six components together to avoid incomplete intermediate tensors.
- Changing mass or inertia updates the equivalent box. Preview requires finite positive mass, finite positive diagonal moments, and the inertia triangle inequalities; otherwise it is not drawn.

### Joint

**Operator ID:** `forge.properties_joint`

| Main editable values |
| --- |
| Type, Display Size, Springdamper, Solver, Range, Force Range, Stiffness, Ref, Armature, Damping, Frictionloss |

<div align="center"><img src="../../assets/images/manual/07-joint-properties.png" width="412" alt="Joint Properties dialog"></div>

### Actuator

**Operator ID:** `forge.properties_actuator`

| Main editable values |
| --- |
| Type, Target, control/force ranges, Gain/Bias types, type-specific parameters, Gear/Dynamics/Gain/Bias arrays |

<div align="center"><img src="../../assets/images/manual/07-actuator-properties.png" width="492" alt="Actuator Properties dialog"></div>

### Tendon

**Operator ID:** `forge.properties_tendon`

**Tendon** uses `+` and `-` to add or remove Target list entries. The Operators are `forge.add_tendon_target_item` and `forge.remove_tendon_target_item`. They are UI helper entry points; scripts and MCP should maintain the Tendon Target collection directly.

| Main editable values |
| --- |
| Type, add/remove Target entries, Range, Solver, Spring Length, Stiffness, Damping |

<div align="center"><img src="../../assets/images/manual/07-tendon-properties.png" width="412" alt="Tendon Properties dialog"></div>

### Equality

**Operator ID:** `forge.properties_equality`

When **Active** is disabled, the main **Equality** parameters cannot be edited.

| Main editable values |
| --- |
| Active, Type, Target 1/2, type-specific parameters |

<div align="center"><img src="../../assets/images/manual/07-equality-properties.png" width="412" alt="Equality Properties dialog"></div>

### Contact

**Operator ID:** `forge.properties_contact`

Only **Pair** contacts display collision and **Solver** parameters.

| Main editable values |
| --- |
| Type, Target 1/2; for Pair: Condim, Friction, Solver, Margin, Gap |

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; "><strong>Exclude Properties</strong></div>
  <div style="flex: 1; text-align: center; "><strong>Pair Properties</strong></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/07-contact-properties-0.png" width="412" alt="Exclude Properties dialog"></div>
  <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/07-contact-properties-1.png" width="412" alt="Pair Properties dialog"></div>
</div>

### Sensor

**Operator ID:** `forge.properties_sensor`

**Frame Sensor** can set **Reference**. **Contact Sensor** shows a **Link**, **Geom**, **Subtree**, or **Site** name according to **Target Type**.

| Main editable values |
| --- |
| Sensor/Target Type, Target, Reference, Xbody/Subtree, Noise, Cutoff; Contact Sensor Data/Reduce |

<div align="center"><img src="../../assets/images/manual/07-sensor-properties.png" width="412" alt="Sensor Properties dialog"></div>

### Light

**Operator ID:** `forge.properties_light`

**Target** is shown only for **Targetbody/Targetbodycom** modes.

| Main editable values |
| --- |
| Type, Mode, Target, Shadow, Color, Energy, Size/Distance/Angle/Spot parameters |

<div align="center"><img src="../../assets/images/manual/07-light-properties.png" width="412" alt="Light Properties dialog"></div>

### Camera

**Operator ID:** `forge.properties_camera`

**Target** is shown only for **Targetbody/Targetbodycom** modes.

| Main editable values |
| --- |
| Type, Mode, Target, FOV or Ortho Scale, Clip Start/End |

<div align="center"><img src="../../assets/images/manual/07-camera-properties.png" width="412" alt="Camera Properties dialog"></div>

### Replicate

**Operator ID:** `forge.properties_replicate`

| Main editable values |
| --- |
| Count, Offset, Euler, Separator |

<div align="center"><img src="../../assets/images/manual/07-replicate-properties.png" width="412" alt="Replicate Properties dialog"></div>

Dynamic fields:

- **Global / Visual:** detailed **Headlight** and **SSGI** parameters are controlled by their **Active** switches; disabling them disables the corresponding fields.
- **Height Field:** **Height Map** appears only after **Use Height Map** is enabled.
- **Plane:** **Infinite** is independent and does not hide **Half Size**.
- **Visual / Collider:** the geometry type determines dimension fields; **Box** shows three-axis **Size**, **Sphere** shows **Radius**, **Capsule/Cylinder** show **Radius + Height**, and **Mesh** shows no primitive size. Materials are managed through the object's first **Material Slot**.
- **Site:** the geometry type determines whether **Size**, **Radius**, or **Radius + Height** is shown.
- **Link:** **Display Type / Display Size / Mocap / Gravcomp** are always shown; no fields are hidden by type.
- **Joint:** **Free** shows only basic **Stiffness / Armature / Damping / Frictionloss**. Other types also show **Springdamper**, Solver, Range, Limited, and related fields. **Ball** does not show **Actuator Force Range/Limited**.
- **Actuator:** **Position** shows **Kp / Kv / Inheritrange**, **Velocity** shows **Kv**, and **Adhesion** shows **Gain**; other types show **Gear / Dynamics / Gain / Bias** arrays.
- **Tendon:** the **Target** field comes from a variable-length Target list controlled by `+ / -`.
- **Equality:** disabling **Active** disables all remaining fields. **Target 2** appears only after **Target 1** is set; the remaining parameters depend on Equality type.
- **Contact:** only **Pair** shows **Condim, Friction, Solver, Margin, Gap**; **Exclude** does not show them.
- **Sensor:** a **Contact** Sensor labels target fields as **Link1/2, Geom1/2, Subtree1/2**, or **Site** according to **Target Type**. Frame sensors show **Reference** and **Use Xbody** after Target is set; Contact sensors show **Reference** and **Use Subtree** when a second target is required.
- **Light:** only **Targetbody/Targetbodycom** shows **Target**; **Spot/Point** show **Shadow Soft Size / Cutoff Distance**, other types show **Angle**, and **Spot** additionally shows **Spot Size / Spot Blend**.
- **Camera:** only **Targetbody/Targetbodycom** shows **Target**; **Perspective** shows **FOV/Angle**, while **Orthographic** shows **Ortho Scale**.
- **Replicate:** **Count / Offset / Euler** appear only while the object still has a Replicate Modifier; **Separator** always belongs to Replicate properties.

## 7.4 How changes take effect

Property dialogs modify **Object**, **Modifier**, or **Scene** data directly and do not have an **Apply/Save** button. Changes remain after closing the dialog and can be undone with **Blender Undo**.

Prefer changing **Size**, **Radius**, and **Height** in **Properties**. Several **Forge** objects lock **Object Scale**; shape dimensions are driven by the **Geometry Nodes Modifier** parameters.

---

[Previous: Meta Elements](06_meta_elements.md) · [Contents](../forge_docs.md) · [中文](../../cn/forge_docs/07_properties.md) · [Next: Import and Export](08_import_export.md)
