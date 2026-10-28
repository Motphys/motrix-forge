# 第 6 章：Model Define — 元元素

[上一章：Hardware](05_hardware.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/06_meta_elements.md) · [下一章：Properties](07_properties.md)

**Meta Elements** 面板位于 **Forge** 页签中，用于创建模型组织与引用元素。

<div align="center">
  <img src="../../assets/images/manual/00-forge-sidebar-overview-3.png" alt="Meta Elements">
</div>

## 6.1 Create frame(s)

**Operator ID：** `forge.create_frame`

未选择对象，或所选对象全部为 **Link**、**Frame**、**Replicate** 时可用，无弹窗：

- 普通点击：为每个所选对象创建子 **Frame**；无选择时创建 **World Frame**。
- `Shift + 点击`：创建 **Frame**，并把原所选对象改为该 **Frame** 的子对象。

## 6.2 Create replicate

**Operator ID：** `forge.create_replicate`

所选对象必须均属于 **Camera**、**Light**、**Visual**、**Collider**、**Site**、**Link**、**Frame**、**Attach** 或 **Replicate**。

弹窗：

<div align="center">
  <img src="../../assets/images/manual/06-replicate-creation.png" alt="Meta Elements">
</div>

参数：

- **Count**：副本数量。
- **Separator**：生成副本名称时使用的分隔符。
- **Offset**：相邻副本的平移增量。
- **Euler**：相邻副本的旋转增量。

**Replicate** 创建后可以修改 **Count**、**Offset**、**Euler** 和 **Separator** 详见第 7 章 **Replicate**。

## 6.3 Attach 与 Include

**Meta Elements** 同时提供 **Attach** 与 **Include**。它们不属于 **Creation**、**Definition**、**Properties** **Operator** 的主体范围，但都用于引用其他场景、模型或 **MJCF** 文件。

执行期间，面板会显示主进度和子进度。文件的选择、前缀等需结合 **MJCF** 标签参数。

### Attach

**Operator ID：** `forge.create_attach`

可用条件：没有选择对象，或恰好选择一个 **Link**、**Frame** 或 **Replicate**，该对象会作为 Attach 的父对象。

弹窗字段：

- **File**：外部 MJCF XML 文件，必须存在；
- **Model**：外部模型名称，不能为空；
- **Prefix**：导入对象名称前缀，不能为空；
- **Link**：可选的外部 Body/Link。选择 `None` 时表示不指定 Body。

确认后 Forge 会以 modal 任务导入外部模型，再创建 Attach 引用。执行期间不要重复启动其他 Import、Export、Attach 或 Include 操作；面板中的第一条进度条表示整体阶段，第二条表示当前阶段内的元素数量。

### Include

**Operator ID：** `forge.create_include`

Include 要求当前没有选择对象。Forge 会导入外部文件中的集合以便在场景中使用，但导出 MJCF 时只写入 `<include file="...">` 引用，外部文件内容不会合并进当前 XML。

Include 同样以 modal 任务执行，并在 Meta Elements 面板显示主进度和子进度。

弹窗：

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <strong>Attach</strong>
  </div>
  <div style="flex: 1; text-align: center; ">
    <strong>Include</strong>
  </div>
</div>
<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/06-add-attach.png"
      width="314"
      alt="Attach 弹窗"
    >
  </div>
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/06-add-include.png"
      width="314"
      alt="Include 弹窗"
    >
  </div>
</div>

进度条：

<div align="center">
  <img src="../../assets/images/manual/06-attach-progress.png" alt="Meta Elements">
</div>

---

[上一章：Hardware](05_hardware.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/06_meta_elements.md) · [下一章：Properties](07_properties.md)
