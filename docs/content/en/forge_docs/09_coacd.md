# Chapter 9: CoACD convex decomposition

[Previous: Import and Export](08_import_export.md) · [Contents](../forge_docs.md) · [中文](../../cn/forge_docs/09_coacd.md) · [Next: Troubleshooting and scripting](10_troubleshooting_and_scripting.md)

## 9.1 Function and prerequisites

**CoACD** decomposes a mesh into several approximately convex collision meshes, which is useful for generating **Collider** shapes from a complex **Visual**.

**Operator ID:** `forge.coacds`

<div align="center"><img src="../../assets/images/manual/09-coacd.png" alt="CoACD panel"></div>

Available in **Object Mode** when at least one **Visual** is selected. The operator selection check requires every selected object to be a **Visual**, and each Visual must contain Mesh data. When calling the MCP tool by name, pass one Visual object.

## 9.2 Before running

- The `coacd` package must be installed in the Blender Python environment. It can be installed from the **Dependencies** page in the Forge add-on preferences.
- Processing can take several minutes, depending on mesh complexity and sampling/MCTS parameters. Logs appear in the system console, not Blender's Python Console editor.
- On Windows, use **Window → Toggle System Console**. The current CoACD dialog also calls `bpy.ops.wm.console_toggle()`, so opening the dialog hides an already visible console; toggle it again if needed. On macOS / Linux, start Blender from a terminal and read logs there. See [Blender's command-line launch guide](https://docs.blender.org/manual/en/latest/advanced/command_line/launch/index.html).

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; "><img src="../../assets/images/manual/09-sys-console.png" width="238" alt="System Console"></div>
  <div style="flex: 1.5; text-align: center; "><img src="../../assets/images/manual/09-console-log.png" width="448" alt="Console log"></div>
</div>

- The operation decomposes evaluated triangle faces. It creates new convex-hull objects, so save the file or create a backup first.
- Each output hull is a new Mesh object in the source object's first **Collection** and is initialized as a Forge **Collider** (`Forge_Model_Type=COLLIDER`, Geometry type `MESH`).

## 9.3 Main parameters

- **Threshold:** concavity threshold; a smaller value usually produces a finer decomposition;
- **Max Convex Hull:** maximum number of hulls when merging is enabled;
- **Preprocess Mode / Resolution:** manifold preprocessing method and resolution;
- **Sample Resolution:** Hausdorff-distance sampling resolution;
- **MCTS nodes / Iteration / Max Depth:** search size;
- **PCA**, **Merge**, **Decimate**, **Max Convex Hull vertex**;
- **Extrude**, **Extrude Margin**;
- **Seed:** random-sampling seed.

After completion, use **Select Hulls** to select hull objects generated from `coacd_name_template`. The hulls are already Forge **Collider** objects and do not need to be defined again; continue by adjusting hierarchy or properties.

---

[Previous: Import and Export](08_import_export.md) · [Contents](../forge_docs.md) · [中文](../../cn/forge_docs/09_coacd.md) · [Next: Troubleshooting and scripting](10_troubleshooting_and_scripting.md)
