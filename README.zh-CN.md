<div align="center">

# Motrix Forge

**Make articulated multibody configuration easier.**

[![Download 0.1.0](https://img.shields.io/badge/Download-0.1.0-2ea44f?style=for-the-badge)](https://github.com/Motphys/motrix-forge/releases)
[![Blender 4.5 LTS](https://img.shields.io/badge/Blender-4.5-F5792A?style=for-the-badge&logo=blender&logoColor=white)](https://www.blender.org/releases/4-5/)
[![Blender 5.2 LTS](https://img.shields.io/badge/Blender-5.2-F5792A?style=for-the-badge&logo=blender&logoColor=white)](https://www.blender.org/releases/5-2/)
[![GitHub License](https://img.shields.io/github/license/motphys/motrix-forge?style=for-the-badge)](https://github.com/Motphys/motrix-forge/blob/main/LICENSE)

[English](README.md)  · [Releases](https://github.com/Motphys/motrix-forge/releases) · [Report an issue](https://github.com/Motphys/motrix-forge/issues/new?template=bug_report.yml)

</div>

<div align="center">
	<img src="media/images/forge_pipeline.png" alt="forge_pipeline">
</div>

## 概览

**Forge** 是一个高效用于创建、编辑和配置 —— 精确描述铰接多体系统运动学结构、惯性属性、几何视觉、几何碰撞、执行器与传感器等 XML 场景的拓展工具。主要解决了：MJCF 没有可视化编辑工具、简化 XML 场景描述的创建、编辑和配置。核心是 **Forge** 插件及其配套的 **MCP Server**。工具支持在 Blender 中创建、编辑、检查和导入/导出 MJCF 场景描述，也可以通过 MCP 将 Forge 能力提供给 Codex、Claude Code 等 AI Agent。

>**Forge** 基于 [**Blender 4.5 LTS**](https://www.blender.org/releases/4-5/) 与 [**Blender 5.2 LTS**](https://www.blender.org/releases/5-2/) 开发。使用 **Forge** 需要熟悉 **Blender** 的使用。

### 主要功能

- **创建 MJCF 模型结构**：创建和组织 Link、Joint、Geometry、Collider、Site、Inertial、Actuator、Tendon、Sensor、Equality、Contact、Light、Camera 等模型元素；
- **编辑模型定义与属性**：配置 Global/General 参数、模型类型、几何体和材质、运动学、硬件、Meta Elements，以及对象的父子关系、根 Link、实例 Link 和变换等属性；
- **在视口中交互编辑**：通过 Forge 面板、属性面板和 Gizmo 调整形状、Link、Joint、Actuator、Tendon、Sensor 等 MJCF 属性，实时检查场景结构；
- **导入与导出**：导入已有 MJCF 标准的 .XML 转换为 Forge 规则的场景结构，或将用 Forge 配置好的场景结构导出为 MJCF 标准的 .XML 文件，并保存 Blender 工程文件；
- **网格与碰撞处理**：执行网格检查，并使用 CoACD 将复杂网格分解为可用于碰撞检测的凸包；
- **MCP 自动化**：通过 MCP Bridge，让 Claude Code、Codex 等 Agent 查询场景、调用 Forge Operator、创建或修改模型、执行导入导出、检查多体关系等。

#### 组件分解

<div align="center">
    <img src="media/images/decomposition.png" alt="Decomposition"/>
</div>
*Blender 中构成 Forge 模型的各个元素的分解示意。这些元素可以在 Blender 中按 Forge 模型类型排列到不同图层或集合中，从而在编辑非常复杂的模型时避免混乱或遮挡视线。*

### 应用案例

![forge_pipeline](/media/videos/HD/forge_pipeline.mp4)
*使用 Forge 编辑配置装载机 → 编辑配置装载机作业环境 → 导出并在 MotrixSim 中进行仿真模拟和训练*

![arbitrary_robotic_arm](/media/videos/HD/arbitrary_robotic_arm.mp4)
*使用 Forge 编辑配置任意机械臂 → 导出并在 MotrixSim 中进行仿真模拟和训练*

![forge_with_agent](/media/videos/HD/forge_with_agent.mp4)
*使用 Agent 通过 Forge 创建编辑配置图片中的场景 → 导出并在 MotrixSim 中进行仿真模拟*

> MJCF 是一种用于精确描述铰接多体系统运动学结构、惯性属性、几何碰撞与执行传感配置的标准化 XML 场景格式，是 MotrixSim 物理引擎进行接触密集型仿真与具身智能策略训练的数据基础。

> Forge 插件与 `mcp-server` 是两个独立组件：插件运行在拥有 Blender 场景的进程中，`mcp-server` 运行在 Agent 侧。使用 MCP 工具前，必须先在 Blender 中安装、启用 Forge，并启动 MCP Bridge（默认 `localhost:9876`）。

## 工程结构

```shell
Motrix-Forge/
├── addon/
│   └── Forge/              # Blender 插件源码、资源与 MCP Bridge
├── docs/                   # 独立的中英文文档站点
├── mcp-server/
│   └── forge_mcp/          # Agent 侧 stdio MCP 服务、工具、Skills 与文档索引
├── tests/
│   ├── forge/              # Blender 插件测试
│   └── mcp/                # MCP 单元、协议集成及端到端测试
├── pyproject.toml          # 根开发环境与 uv workspace 配置
├── run_tests.py            # Forge Blender 测试入口
└── run_all_tests.py        # 全部测试套件入口
```

MCP 模式下的调用链如下：

```shell
AI Agent ──stdio──> Forge MCP Server ──TCP──> Blender 中的 Forge MCP Bridge
                                                   │
                                                   └──> 场景与 bpy.ops.forge.*
```

Forge 插件负责实际的场景操作，`mcp-server` 负责把这些操作封装成 Agent 可调用的 MCP 工具。两者默认通过 `localhost:9876` 通信。

## 环境要求

- Blender 4.5 LTS 或 Blender 5.2 LTS；
- Python 3.11（根开发环境限定为 `>=3.11,<3.14`）；
- [uv](https://docs.astral.sh/uv/)（用于安装依赖和运行 MCP 服务）；
- 可选：Codex CLI、Claude Code 或其他支持 stdio MCP 的客户端。

## 快速开始

### 1. 安装 Forge 插件

如果只需要在 Blender 中制作 MJCF 模型，仅安装插件即可：

1. 将 `addon/Forge` 打包为 ZIP，确保 ZIP 根目录直接包含 `blender_manifest.toml`；
2. 在 Blender 中打开 **Edit → Preferences → Add-ons → Install from Disk**；
3. 选择 ZIP 并启用 **Forge**；
4. 在插件设置的 **Dependencies** 中安装 `tetgen` 与 `CoACD`，然后重启 Blender；
5. 打开 3D View 侧栏（`N`），确认 Forge 面板可见。

详细操作：

- [Motphys Forge 中文 README](addon/README.zh-CN.md)
- [Motphys Forge 文档索引](https://motphys.github.io/motrix-forge/introduction.zh-CN.html)
- [Forge 中文操作手册](https://motphys.github.io/motrix-forge/cn/forge_docs.html)

### 2. 配置开发环境

在仓库根目录执行：

```bash
uv sync
```

根目录是一个 uv workspace；该命令会创建共享的 `.venv`，安装测试依赖，并以可编辑模式安装 `mcp-server` 中的 `forge-mcp`。

### 3. 接入 AI Agent（可选）

1. 在 Blender 中启用 Forge，并开启 **Auto-start server** 或点击 **Start MCP Bridge**；
2. 确认 Bridge 监听地址为 `localhost:9876`；
3. 从仓库根目录启动 MCP 客户端。Claude Code 等客户端会读取 `.mcp.json`；Codex 使用 `.codex/config.toml`。

Codex 的 PowerShell 启动示例：

```powershell
$env:CODEX_HOME = (Join-Path (Get-Location) '.codex')
codex
```

验证连接：

```bash
codex mcp list
```

对于 Claude Code，可运行 `claude mcp list`，或在 TUI 中输入 `/mcp` 查看 `forge` 连接状态。

详细操作：

- [Forge MCP 安装指南](https://motphys.github.io/motrix-forge/reference/MCP_INSTALL.zh-CN.html)
- [Forge MCP Server 中文 README](https://motphys.github.io/motrix-forge/reference/mcp-server/README.zh-CN.html)

跨机器连接时必须在两端设置相同的非空 Token，并通过防火墙或 VPN 限制 Bridge 端口。

## 开发与测试

运行不依赖 Blender 的 MCP 单元测试和协议集成测试：

```bash
uv run pytest tests/mcp/unit tests/mcp/integration
```

运行 Forge 插件测试（自动查找 Blender 4.5+，优先使用最新安装版本）：

```bash
uv run python run_tests.py
```

如果 Blender 未安装在标准目录或不在 `PATH` 中，可设置 `BLENDER_PATH`（或旧版 `BLENDER_45_PATH`）指向 Blender 可执行文件。

运行 MCP 与 Blender 的端到端测试：

```bash
uv run python tests/mcp/e2e/driver.py
```

运行全部测试套件：

```bash
uv run python run_all_tests.py
```

在仓库根目录运行 Ruff。`ruff.toml` 将文件发现范围限制为 `.py` 脚本（独立打开 `addon/` 时也有对应配置）；Markdown、Notebook 等其他文件不在处理范围内。

格式化 Python 脚本：

```bash
uv run ruff format .
```

检查代码规则和格式，不修改文件：

```bash
uv run ruff check .
uv run ruff format --check .
```

## 相关文档

先运行 `uv sync` 将文档依赖安装到根目录 `.venv`，再使用 `python docs/scripts/docs.py serve` 预览文档站点；使用 `python docs/scripts/docs.py build --strict` 构建到 `docs/site/`。目录结构和发布说明见[站点维护文档](docs/README.md)。

建议使用 [Obsidian](https://obsidian.md/) 将仓库根目录作为 Vault 打开，以便浏览文档层级、相对链接和内嵌图片。Obsidian 仅用于改善阅读体验，不是安装或运行本工程的必需依赖。

- [Motphys Forge 中文 README](addon/README.zh-CN.md)
- [Motphys Forge 文档索引](https://motphys.github.io/motrix-forge/introduction.zh-CN.html)
- [Forge 中文操作手册](https://motphys.github.io/motrix-forge/cn/forge_docs.html)
- [Forge MCP 安装指南](https://motphys.github.io/motrix-forge/reference/MCP_INSTALL.zh-CN.html)
- [Forge MCP Server 中文 README](https://motphys.github.io/motrix-forge/reference/mcp-server/README.zh-CN.html)

## 参与贡献

欢迎参与代码开发、问题反馈、文档与翻译、示例制作，以及 Blender 兼容性测试。

### 贡献者申请

1. 在 [Issue](https://github.com/Motphys/motrix-forge/issues) 中说明希望参与的方向、需要解决的问题或改进目标，以及计划采用的方案。较大改动请先与维护者讨论范围，再开始实现。
2. 修改代码或文档时，Fork 仓库并创建独立分支，通过 Pull Request 提交，并关联对应 Issue。小范围修正可以直接提交 Pull Request。
3. 希望长期参与维护时，请在 Issue 中补充个人简介、相关经验或已有贡献、希望负责的模块，以及预计可投入的时间。维护者会根据需要与你沟通职责和仓库权限；成为贡献者不代表自动获得写入权限。

### 贡献要求

- 阅读[开发指南](https://motphys.github.io/motrix-forge/cn/development.html)，遵循现有工程结构和代码风格；每个 Pull Request 聚焦一个问题。
- 在 Pull Request 中说明问题、修改后的行为和验证结果。修复缺陷时提供复现步骤；行为变化时更新或补充相关测试。
- 根据修改范围运行[开发与测试](#开发与测试)中的检查。Python 改动需通过 Ruff 代码及格式检查；文档改动需通过严格构建。
- 涉及 Blender API 或界面时，在 Blender 4.5 LTS 和 5.2 LTS 中验证受影响的行为。界面改动请附截图，并说明已测试版本及未完成的检查。
- 用户可见行为变化时，同步维护中英文文档。仅提交有权贡献的素材，不提交凭据、本地环境、生成的站点文件或无关改动。
- 尊重其他参与者，及时回应 Review 意见，并在合并前解决相关评论。维护者会从正确性、兼容性和可维护性等方面审核贡献。

## 许可证

Copyright (C) 2020-2026 Motphys Technology Co., Ltd. All Rights Reserved.

Motrix Forge 使用 GNU 通用公共许可证第 3 版或（由你选择）任何更新版本（`GPL-3.0-or-later`）授权。完整条款见 [LICENSE](LICENSE)。第三方组件保留各自的版权声明和许可证。

## 问题反馈

提交问题时，请附上 Blender 版本、插件或仓库 commit、操作步骤、预期结果、实际结果以及相关日志。MCP 连接问题还应注明客户端、Bridge 主机与端口，以及 `forge` 服务的连接状态；请勿提交访问 Token。

[English](README.md) | **中文**
