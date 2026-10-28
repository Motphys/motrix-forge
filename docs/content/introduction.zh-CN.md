# 关于 Forge

Forge 是面向铰接多体系统的可视化场景创作工具，用于高效创建、编辑、检查和配置 MJCF XML 场景，描述系统的运动学结构、惯性属性、视觉几何、碰撞几何、执行器与传感器。它为 MJCF 场景提供可视化编辑能力，通过 Blender 中的模型层级、属性面板和 Gizmo，简化机器人、机构及其作业环境的创建与配置，并支持场景导入和导出，衔接后续仿真流程。

Forge 的核心是运行在 Blender 中的 Forge 插件及其配套的 MCP Server。插件负责场景建模与实际操作；可选的 MCP Server 通过 MCP 将这些能力提供给 Codex、Claude Code 等 AI Agent，支持自动化创建、修改、检查和导入导出场景。

![从 Blender 建模到场景配置和仿真的工作流程](assets/images/forge_pipeline.png)

## 从这里开始

| 你想做什么 | 阅读页面 |
| --- | --- |
| 在 Blender 中安装并启用 Forge | [安装 Forge](cn/installation.md) |
| 配置预览、MCP Bridge、依赖与自动启动 | [配置 Forge](cn/preferences.md) |
| 查找界面按钮、模型属性和操作流程 | [使用手册](cn/forge_docs.md) |
| 修改插件、MCP 服务或文档，运行测试 | [开发 Forge](cn/development.md) |
| 通过 AI Agent 操作 Blender 场景 | [MCP 安装指南](reference/MCP_INSTALL.zh-CN.md) |
| 观看建模、仿真衔接和 Agent 自动化演示 | [应用案例与视频](cn/examples.md) |

## 可以做什么

- **搭建模型层级**：创建 Link、Joint、Visual、Collider、Site 和 Inertial，配置父子关系与根节点。
- **编辑模型参数**：通过侧栏、属性面板和视口 Gizmo 调整几何形状、材质、关节及硬件属性。
- **配置仿真元素**：创建执行器、传感器、肌腱、约束、接触、灯光和相机。
- **检查几何与惯量**：检查网格，使用 CoACD 分解凸包，从 Visual 或 Collider 计算质量、质心和惯量。
- **往返编辑场景**：导入已有 MJCF，编辑后导出 XML 和关联资源，同时保存 `.blend` 工程。
- **接入自动化**：通过可选的 MCP 服务让 Agent 查询场景、调用 Forge Operator 并执行导入导出。

下图以机械臂为例，展示 Link、Joint、Hardware、Inertial、Visual 和 Collider 如何共同组成完整模型，并在导出后进入 MotrixSim 仿真。

<div style="text-align: center;">
  <img
    src="assets/images/decomposition.png"
    alt="机械臂模型的组成：Link、Joint、Hardware、Inertial、Visual 和 Collider，以及导出到 MotrixSim 的流程"
  >
</div>

## 工作方式

1. 在 Blender 中创建或导入几何对象。
2. 将对象定义为 Forge 模型类型，建立 Link 层级。
3. 配置碰撞体、关节、执行器和传感器等元素。
4. 检查几何，计算惯量，并确认模型属性。
5. 导出 MJCF XML 和资源，交给仿真环境使用。

详细操作从[界面总览](cn/forge_docs/00_ui_overview.md)开始。Forge 提供建模与场景配置能力，仿真在导出后的目标环境中进行。

## 插件与 MCP 服务

| 组件 | 运行位置 | 作用 |
| --- | --- | --- |
| Forge 插件 | Blender 进程 | 提供 UI、模型数据、Operator、导入导出和 MCP Bridge |
| Forge MCP Server（可选） | Agent 侧 Python 进程 | 通过 stdio 向 Agent 暴露工具，再通过 TCP 调用 Blender Bridge |

只使用 Blender 界面建模时，安装插件即可。需要 Agent 自动化时，再配置 MCP 服务；实际操作场景的 Blender 实例必须已启用 Forge。

## 使用这份文档

左侧依次提供关于 Forge、安装 Forge、配置 Forge、开发 Forge，以及案例和完整的使用手册，右侧显示本页目录。使用左下角的语言选择切换到同一页面的英文版本，主题按钮可切换浅色和黑色外观。

需要离线修改或预览文档时，参阅[本地预览](cn/preview.md)。
