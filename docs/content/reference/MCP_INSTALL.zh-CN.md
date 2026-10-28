# Forge MCP 安装与连接

**中文** | [English](MCP_INSTALL.md)

本页负责从准备工作区到首次连接成功的流程。环境变量的完整定义、服务运行方式、Skills 与文档加载机制以及开发说明统一放在[服务端参考](mcp-server/README.zh-CN.md)。

本项目把 Agent 侧的 stdio MCP 服务放在 `mcp-server/`，把客户端配置放在 `.mcp.json`（Claude Code 等客户端）和 `.codex/config.toml`（Codex）。因此可以把下面四项复制或 clone 到一个空工作目录，再从该目录启动 Agent：

```text
.claude/
.codex/
.mcp.json
mcp-server/
```

精简 MCP 工作区只需上述项目，不需要复制 Blender 测试工程。运行场景查询或编辑工具时，Blender 中必须安装并启用 `addon/Forge`，并启动插件的 MCP Bridge（默认 `localhost:9876`）；读取 Skills 和搜索本地文档不需要运行 Blender。

## 连接前检查 Blender

先完成 [Forge 插件安装](../cn/installation.md)，在拥有场景的 Blender 实例中启用 Forge，并允许 Blender 在线访问。在 Forge 侧栏点击 **Start MCP Bridge**，确认 Bridge 已启动。监听地址、Token、自动启动与轮询设置见[配置 Forge](../cn/preferences.md)，本页不重复插件参数说明。

## 1. 准备工作目录

推荐 clone（会自动得到完整目录结构）：

```bash
git clone <仓库地址> forge-mcp-workspace
cd forge-mcp-workspace
```

如果是从已有目录复制，请确保复制了上面列出的隐藏目录和 `.mcp.json`，不要只复制 `mcp-server/`。复制时请检查这些以 `.` 开头的配置项是否完整。

## 2. 安装 MCP 依赖

先安装 [uv](https://docs.astral.sh/uv/)。若使用包含根目录 `pyproject.toml` 的完整仓库，在仓库根目录执行 `uv sync`，准备客户端实际使用的根目录 `.venv`；详细说明见[开发环境](../cn/development.md#准备开发环境)。

若使用仅复制上述项目的精简 MCP 工作区，在工作目录执行下面的安装脚本。脚本会在 `mcp-server/.venv` 创建 Python 3.11 环境，并安装 `mcp` 与 `forge-mcp`，不会改动系统 Python。

Windows PowerShell：

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\mcp-server\install.ps1
```

macOS / Linux / WSL：

```bash
bash mcp-server/install.sh
```

也可以让脚本安装后直接启动客户端：

```powershell
.\mcp-server\install.ps1 -Launch claude
.\mcp-server\install.ps1 -Launch codex
```

```bash
bash mcp-server/install.sh claude
bash mcp-server/install.sh codex
```

以上脚本面向使用服务的工作区。需要修改源码并运行测试时，改用[服务端参考中的开发环境](mcp-server/README.zh-CN.md#开发与测试)。

## 3. 在该目录启动 Agent

安装完成后，打开新的控制台并进入工作目录：

```powershell
cd C:\path\to\forge-mcp-workspace
claude       # Claude Code
```

```powershell
cd C:\path\to\forge-mcp-workspace
$env:CODEX_HOME = (Join-Path (Get-Location) '.codex')
codex        # Codex CLI
```

macOS / Linux 使用 `export CODEX_HOME="$PWD/.codex"`。设置 `CODEX_HOME` 后，Codex 会读取复制来的 `.codex/config.toml`；Claude Code 会读取工作目录根部的 `.mcp.json`。客户端会按配置自动通过 stdio 启动 MCP 服务。精简 MCP 工作区使用安装脚本创建的 `mcp-server/.venv`；完整仓库中的 uv workspace 使用根目录 `.venv`，需先按[开发环境说明](../cn/development.md#准备开发环境)准备依赖。配置中的 `--no-sync` 只跳过依赖同步，不会自动创建或修复环境。

## 4. 验证连接

- Codex：运行 `codex mcp list`，或在 TUI 输入 `/mcp`；
- Claude Code：运行 `claude mcp list`，或输入 `/mcp` 查看 `forge` 是否为 connected；

默认端口为 `9876`。远程或非默认端口时，在 `.mcp.json` 与 `.codex/config.toml` 的 `env` 中同步设置 `FORGE_MCP_HOST`、`FORGE_MCP_PORT`；跨机器连接还必须设置两端相同的非空 `FORGE_MCP_TOKEN`，并用防火墙或 VPN 限制 Bridge 端口。

## 连接问题排查

| 现象 | 先检查 |
| --- | --- |
| 客户端没有 `forge` 条目 | 工作目录、客户端配置文件及客户端是否已重新启动 |
| 服务进程启动失败 | 安装脚本是否成功、`uv` 是否可用，以及[运行时配置](mcp-server/README.zh-CN.md#运行时配置)中的过滤条件和目录设置 |
| MCP 已连接，但场景操作失败或超时 | Blender 是否运行、Forge 是否启用、Bridge 是否启动，以及主机、端口、Token 是否匹配 |
| Bridge 无法启动 | Blender 在线访问许可、端口是否占用；详细设置见[配置 Forge](../cn/preferences.md) |

连接成功后，查阅[服务端参考](mcp-server/README.zh-CN.md)了解运行时配置；模型创作规则见[英文 MCP Skills](../en/mcp_skills.md)。

## 配置文件说明

- `.mcp.json`：Claude Code、Cursor 等读取的 MCP 配置；
- `.claude/settings.local.json`：启用项目中的 `forge` MCP 条目；
- `.codex/config.toml`：Codex 的项目级 MCP 配置；项目必须被 Codex 信任；

OpenAI 官方文档说明，Codex CLI、IDE 扩展和桌面端共享 MCP 配置；项目级配置位于受信任项目的 `.codex/config.toml`，可用 `codex mcp list` 和 TUI 的 `/mcp` 检查连接：<https://developers.openai.com/codex/mcp/>。

[English](MCP_INSTALL.md) | **中文**
