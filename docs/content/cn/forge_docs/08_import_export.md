# 第 8 章：导入与导出

[上一章：Properties](07_properties.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/08_import_export.md) · [下一章：CoACD](09_coacd.md)

## 8.1 Import

**Import** 面板用于从 **MJCF XML** 重建 **Blender** 场景。

网格资产可以引用 **OBJ**、**STL** 或 **GLB** 文件。GLB 资产只接受单个 Mesh 对象，相机、灯光、空节点等其他元素会被丢弃。Mesh 节点变换会烘焙到网格中，并保留文件坐标与 UV，支持 Forge 导出后再导入。MJCF 的 mesh `scale` 在此基础上应用；材质使用 MJCF 定义，不使用 GLB 内嵌材质。文件缺失、格式不支持或 GLB 包含零个或多个 Mesh 对象时，会在资产加载阶段明确报错。

**Operator ID：** `forge.import_mjcf`

GLB 导入和导出需要启用 Blender 的 **glTF 2.0** 插件（`io_scene_gltf2`）。未启用时会提示在 **Edit > Preferences > Add-ons** 中启用；导入会在清空场景前停止，导出会在写文件或修改网格前停止。OBJ/STL 导入、OBJ 导出以及仅更新 XML 不受此依赖限制。

弹窗：

<div align="center">
  <img src="../../assets/images/manual/00-forge-sidebar-overview-5.png" alt="导入面板" >
</div>

使用步骤：

1. 在 **File** 中选择 **MJCF XML** 文件；
2. 根据需要开启 **Import material**；
3. 点击 **Import**。

**Import** 是 **modal** 操作，会显示整体进度和当前阶段的子进度。导入前请保存当前工作：Import 会清理当前场景对象、集合、非主场景及无主数据，然后重新建立模型。

如果 **Forge Library** 不存在或路径失效，Forge 会尝试从插件的 `lib/assets` 目录重新配置；失败时操作会取消。

## 8.2 Export

**Export** 面板用于把当前 **Forge** 场景导出为 **MJCF XML**。

**Operator ID：** `forge.export_mjcf`

弹窗：

<div align="center">
  <img src="../../assets/images/manual/00-forge-sidebar-overview-6.png" alt="导出面板" >
</div>

参数：

- **Only Update File**：仅更新 **MJCF** 文件内容，跳过外部资产文件的重新写出；
- **Path**：导出目标路径。未输入 `.xml` 时，文件选择器会自动补齐；

通过 MCP 调用 `forge_export_mjcf` 时，如果目标文件已经存在，工具默认拒绝覆盖；确认需要覆盖时显式传入 `overwrite=True`。**UI Operator** `forge.export_mjcf` 则按当前文件选择器路径执行写出。

**Export** 会按“收集资产 → 写出图像、**Height Field**、**Visual/Collider** 网格 → 写入 **MJCF** 各 **section** → 写文件”的阶段执行，并显示主进度与子进度。

当导出的网格资产是空网格时将会忽略。

导出会从 `World`、`Link`、`Frame`、`Visual`、`Collider` 集合，以及 `Replicate` 及其子集合中收集模型对象：集合内无父对象的对象作为根，再沿父子层级收集其子对象。因此根 **Link** 即使位于 `Link` 或 `Frame` 集合中也会被导出。

如果 **World** 使用连接到环境纹理的 **Environment Texture**，Export 会将其写为 MJCF 的 `<texture type="envhdr">`；Import 会把该纹理恢复到主场景的 **World**。

棋盘格材质导出为 MJCF 原生二维内置 checker 贴图，不生成外部图像文件。开启 **Import material** 后，导入会恢复颜色、重复次数和 Blender 材质节点。创建参数与支持的节点连接方式见[创建棋盘格材质](03_geometry_and_material.md#创建棋盘格材质)。

**Instance**（实例复用）的标记与导出规则见[第 4.7 节](04_kinematics.md#47-instance-使用规则)：Instance Link 只提供资产，其子物体在导出时写入各占位 Link 之下。

导出路径可为绝对路径，也可使用相对于当前 `.blend` 文件的路径。导出前应确认目标目录存在且有写权限。

## 8.3 脚本与 MCP

**Import**、**Export**、**Attach**、**Include** 都是 **modal Operator**，调用后会先返回 `RUNNING_MODAL`。脚本或 MCP 客户端应等待对应状态结束：

- **Import**：`Forge_Props.is_importing`；
- **Export**：`Forge_Props.is_exporting`；
- **Attach**：`Forge_Props.is_attaching`；
- **Include**：`Forge_Props.is_including`。

通过 **MCP** 时优先使用 `forge_import_mjcf`、`forge_export_mjcf`、`forge_create_attach` 和 `forge_create_include`，这些工具会负责设置路径、等待 **modal** 操作完成并返回结果。

## 8.4 惯量导入与导出

导入 `<inertial fullinertia="...">` 时，Forge 将 Link 坐标轴下的完整张量分解为主轴姿态和对角惯量。导出在存在非零对角惯量时写入 `pos`、`mass`、`quat` 和 `diaginertia`，不会同时写出 `fullinertia`。因此导入的 fullinertia 可在再次导出时变为等效的 quat + diaginertia 表达。

惯量位姿使用相对于 Link 的物理变换，视口等效长方体的显示缩放不影响导出。Mesh Collider 导入后使用线框显示，并可通过 **Collider Preview** 查看半透明表面。

---

[上一章：Properties](07_properties.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/08_import_export.md) · [下一章：CoACD](09_coacd.md)
