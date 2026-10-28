# 第 9 章：CoACD 凸分解

[上一章：Import 与 Export](08_import_export.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/09_coacd.md) · [下一章：常见问题与脚本](10_troubleshooting_and_scripting.md)

## 9.1 功能与适用条件

**CoACD** 将网格分解为多个近似凸的碰撞网格，适合为复杂 **Visual** 生成 **Collider** 形状。

**Operator ID：** `forge.coacds`

弹窗：

<div align="center">
  <img src="../../assets/images/manual/09-coacd.png" alt="CoACD 面板" >
</div>

可用条件：处于 **Object Mode** 且至少选择一个 **Visual**。Operator 的选择检查要求所有所选对象都是 **Visual**；每个 Visual 必须带有 Mesh 数据。MCP 工具按名称调用时应传入一个 Visual 对象。

## 9.2 执行前注意事项

- 需要在 **Blender Python** 环境中安装 `coacd` 包，可从 **Forge** 插件偏好设置的 **Dependencies** 页面安装；
- 处理可能需要几分钟，具体取决于网格复杂度和采样/MCTS 参数。进度日志输出到系统控制台，而非 Blender 的 Python Console 编辑器。
- Windows 上可通过 **Window → Toggle System Console** 切换系统控制台；当前 CoACD 弹窗也会调用 `bpy.ops.wm.console_toggle()`，若控制台已打开，该调用会将其隐藏，需要时可再次切换。macOS / Linux 从终端启动 Blender 后在该终端查看日志。参阅 [Blender 命令行启动说明](https://docs.blender.org/manual/en/latest/advanced/command_line/launch/index.html)。

<div style="display: flex; gap: 24px; align-items: flex-start;">
  <div style="flex: 1; text-align: center; ">
    <img
      src="../../assets/images/manual/09-sys-console.png"
      width="238"
      alt="Windows 系统控制台菜单"
    >
  </div>
  <div style="flex: 1.5; text-align: center; ">
    <img
      src="../../assets/images/manual/09-console-log.png"
      width="448"
      alt="CoACD 系统控制台日志"
    >
  </div>
</div>

- 操作会读取评估后的三角面执行分解；它会生成新的凸包对象，执行前仍建议保存或创建备份；
- 输出的每个凸包都是新的 Mesh 对象，放在源对象的第一个 **Collection** 中，并设置为 Forge **Collider**（`Forge_Model_Type=COLLIDER`、Geometry 类型为 `MESH`）。

## 9.3 主要参数

- **Threshold**：凹度阈值，越小通常产生更精细的分解；
- **Max Convex Hull**：启用合并时的凸包数量上限；
- **Preprocess Mode / Resolution**：流形预处理方式和分辨率；
- **Sample Resolution**：Hausdorff 距离采样分辨率；
- **MCTS nodes / Iteration / Max Depth**：搜索规模；
- **PCA**、**Merge**、**Decimate**、**Max Convex Hull vertex**；
- **Extrude**、**Extrude Margin**；
- **Seed**：随机采样种子。

完成后可以使用 **Select Hulls** 选择按 `coacd_name_template` 生成的凸包对象；凸包在生成时已经是 Forge **Collider**（无需再定义），可直接继续调整层级或参数。

---

[上一章：Import 与 Export](08_import_export.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/09_coacd.md) · [下一章：常见问题与脚本](10_troubleshooting_and_scripting.md)
