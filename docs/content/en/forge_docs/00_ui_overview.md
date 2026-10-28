# Chapter 0: UI overview and common operations

[Contents](../forge_docs.md) · [中文](../../cn/forge_docs/00_ui_overview.md) · [Next: MCP service](01_mcp_server.md)

## 0.1 Open the Forge panel

After installing and enabling Forge, press `N` in the 3D View to open the sidebar, then switch to the **Forge** tab.

This documentation set covers the following UI panels:

<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img src="../../assets/images/manual/00-forge-sidebar-overview-0.png" width="292" alt="Forge information panel">
    </div>
    <div style="flex: 2;">
        <dt style="font-weight: bold !important; ">Forge info</dt>
        <ul><li>General information about Forge tools.</li></ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img src="../../assets/images/manual/00-forge-sidebar-overview-1.png" width="292" alt="MCP panel">
    </div>
    <div style="flex: 2;">
        <strong style="font-weight: bold !important; ">MCP Server</strong>
        <ul><li>MCP service configuration; see Chapter 1.</li></ul>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img src="../../assets/images/manual/00-forge-sidebar-overview-2.png" width="292" alt="Model Define panel">
    </div>
    <div style="flex: 2;">
        <strong style="font-weight: bold !important; ">Model Define</strong>
        <ul><li>Global settings, type definitions, model-element creation, and helper tools; see Chapters 0 and 2–5.</li></ul>
        <strong style="font-weight: bold !important; ">Layout</strong>
        <ol>
            <li><dt style="font-weight: bold !important; ">Global:</dt> Global Properties and Visual Properties.</li>
            <li><dt style="font-weight: bold !important; ">General:</dt> Define model and Batch Rename.</li>
            <li><dt style="font-weight: bold !important; ">Geometry:</dt> Create and define Visual/Collider shapes, Height Field, Plane, and Check Meshs (manifold and intersection checks).</li>
            <li><dt style="font-weight: bold !important; ">Material:</dt> Create common materials from the Forge PBR library, create checker materials, and assign existing materials.</li>
            <li><dt style="font-weight: bold !important; ">Kinematics:</dt> Link, Joint, Parent, Inertial, and Root.</li>
            <li><dt style="font-weight: bold !important; ">Instance:</dt> Mark, Choose, and Set.</li>
            <li><dt style="font-weight: bold !important; ">Hardware:</dt> Actuator, Site, Tendon, Equality, Sensor, Contact, Light, and Camera.</li>
            <li><dt style="font-weight: bold !important; ">Tag / Select:</dt> Select scene objects by name tag.</li>
            <li><dt style="font-weight: bold !important; ">Type / Select:</dt> Select scene objects by type.</li>
            <li><dt style="font-weight: bold !important; ">Gizmo display size:</dt> Adjust the display size of Forge gizmos in bulk.</li>
        </ol>
    </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; ">
        <img src="../../assets/images/manual/00-forge-sidebar-overview-3.png" width="292" alt="Meta Elements panel">
    </div>
    <div style="flex: 2;"><strong style="font-weight: bold !important; ">Meta Elements</strong><ul><li>Frame, Replicate, Attach, and Include; see Chapter 6.</li></ul></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/00-forge-sidebar-overview-4.png" width="292" alt="CoACD panel"></div>
    <div style="flex: 2;"><strong style="font-weight: bold !important; ">CoACD</strong><ul><li>Use CoACD to decompose a mesh into convex pieces; see Chapter 9.</li></ul></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/00-forge-sidebar-overview-5.png" width="292" alt="Import panel"></div>
    <div style="flex: 2;"><strong style="font-weight: bold !important; ">Import</strong><ul><li>Import an MJCF XML file; see Chapter 8.</li></ul></div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
    <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/00-forge-sidebar-overview-6.png" width="292" alt="Export panel"></div>
    <div style="flex: 2;"><strong style="font-weight: bold !important; ">Export</strong><ul><li>Export an MJCF XML file; see Chapter 8.</li></ul></div>
</div>

> Hover over a button or parameter to see its available tooltip.
> Blender's **Object Properties → Forge Properties** also exposes the active object's transform, parent, Forge type, and model properties; see Chapter 7.

## 0.2 Selection, active object, and selection order

- **Selected objects:** all objects currently selected.
- **Active object:** the last object activated, normally shown with a brighter outline.
- **Forge type:** the object's `Forge_Model_Type`, such as `LINK`, `VISUAL`, or `JOINT`.
- **Selection order:** Forge records the order in which objects were selected and uses it to assign roles such as Target, Reference, and parent.

<div align="center"><img src="../../assets/images/manual/00-selection-and-active-object.png" alt="Multiple selection and active-object outline"></div>

> A Creation Operator usually creates one object for every selected target; a Definition Operator modifies only the active object by default. Pay particular attention to selection order for `Equality`, `Sensor`, `Light`, `Camera`, and `Tendon`, which use two or more targets.

## 0.3 What a disabled button means

A grey button means that the operator's preconditions are not satisfied. Common causes include:

- the wrong number of objects is selected;
- a selected object has an unsupported Forge type;
- an object should be deselected but is still selected;
- there is no valid active object; or
- Blender is not in Object Mode.

<div align="center"><img src="../../assets/images/manual/00-operator-active.png" alt="Disabled operator button"></div>

> The exact conditions for each feature are listed in the tables in the later chapters.

## 0.4 Tags, model type selection, and viewport display

### Select by tag

1. Enter the text to match in **Tag**.
2. Click **Select** to call `forge.select_by_tag`.
3. Forge selects objects in the current scene whose names contain the text; the existing selection is not cleared automatically.

<div align="center"><img src="../../assets/images/manual/00-tag-and-selection.png" alt="Select by tag"></div>

### Select by model type

1. Choose a Forge model type such as **Link** or **Collider** in **Type**.
2. Click **Select** below it to call `forge.select_by_model_type`.
3. Available only in **Object Mode**. Matching objects from the current context's selectable objects are added to the existing selection.

<div align="center">
  <img src="../../assets/images/manual/00-type-and-selection.png" alt="Select by model type">
</div>

### Adjust gizmo size

1. Choose **Scale factor** or **Ratio**.
2. Click the execute button on the right to call `forge.scale_gizmo_size`.
3. If objects are selected, only those objects are changed. With no selection, all objects in the `.blend` file, including objects in other scenes, are changed.

<div align="center"><img src="../../assets/images/manual/00-gizmo-scale.png" alt="Scale gizmo"></div>

**Inertial** display dimensions are determined by mass and inertia and are excluded from this scaling operation.

### Viewport preview toggles

Open **Blender Preferences → Add-ons → Forge → General → Viewport Previews**. **Collider Preview** and **Inertial Preview** are enabled by default and control translucent collider surfaces and equivalent inertia boxes in all 3D viewports.

Both previews require **Overlays** and **Extras** in the current viewport. Selected previews are orange; unselected Colliders are pale blue and Inertials are red. Collider objects use wireframe display, which remains available when surface previews are disabled. Disabling Inertial Preview retains its selectable native Empty box.

## 0.5 Recommended modeling workflow

1. Create or import **Mesh** into **Blender**.
2. Use **Define model** to define meshes as **Visuals** or **Colliders**. Create **Links** with **Create link(s)**, or define an **Empty** as a **Link**. Primitive shapes can also be created directly with the creation buttons.
3. Build the **Link** hierarchy and use **Link Parent** to adjust parent-child relationships.
4. Create **Visual**, **Collider**, **Joint**, and **Site** objects.
5. Create **Actuator**, **Tendon**, **Equality**, **Sensor**, **Contact**, **Light**, and **Camera** objects.
6. Edit parameters with the viewport **Gizmo**.
7. Run **Compute Inertial** on the **Link**, choose **Visual / Collider**, and enable **Check Geometry** as needed.
8. Select the top-level **Link/Frame** and run **Mark root**.

---

[Contents](../forge_docs.md) · [中文](../../cn/forge_docs/00_ui_overview.md) · [Next: MCP service](01_mcp_server.md)
