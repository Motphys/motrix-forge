# 第 1 章：MCP 服务

[上一章：界面总览](00_ui_overview.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/01_mcp_server.md) · [下一章：Global 与 General](02_global_and_general.md)

## 插件侧 MCP 服务端口

<div style="flex: 1; text-align: center; ">
    <img
        src="../../assets/images/manual/00-forge-sidebar-overview-1.png"
        width="292"
        alt="MCP 面板"
    >
</div>

服务配置：

“配置 Forge”页面中的连接参数、Polling、Startup 和 Debug 完整说明见[配置 Forge](../preferences.md)。

- 地址：默认 `localhost`；
- 端口：默认 `9876`；
- **Auto-start server**：插件偏好设置中的自动启动选项，默认开启；
- **Authentication Token**：当监听地址不是 localhost 时，应配置共享 Token；
- **Log requests to console**：即时开启或关闭请求/响应日志，无需重启 Bridge。日志写入 Blender 系统控制台，不是 Python Console；Windows 可通过 **Window → Toggle System Console** 查看。

侧栏里的 **Start/Stop MCP Bridge** 控制 Blender 插件侧 TCP bridge；它不是 Agent 侧的 MCP server。

## Agent 侧 MCP 服务

使用方法：

- 按 [MCP 安装与连接](../../reference/MCP_INSTALL.zh-CN.md)准备工作区并安装依赖；完整仓库的开发环境使用根目录 `.venv`，精简 MCP 工作区使用 `mcp-server/.venv`；
- 确保 Blender 已启用 Forge，并启动插件侧 MCP bridge；
- 在工作区目录启动 Claude Code 或 Codex，由客户端读取配置并自动启动、管理 Forge MCP Server；安装、启动与连接检查的完整流程见 [MCP 安装与连接](../../reference/MCP_INSTALL.zh-CN.md)；
- Claude Code 读取工作区根目录的 `.mcp.json`；Codex 使用工作区的 `.codex/config.toml`，启动方式见安装指南；
- **workspace 随拷随用**：把整个 workspace（含 `.mcp.json`、`.codex/config.toml`、`mcp-server/`）拷到任意位置后，在 console 中执行 `mcp-server/install.ps1`（Windows）或 `bash mcp-server/install.sh` 安装依赖，再进入该目录启动 agent（`claude` / `codex`，Codex 需 `CODEX_HOME="$PWD/.codex"`）即可自动加载 forge MCP（前提：本机装有 [uv](https://docs.astral.sh/uv/)）；
- 默认连接地址为 `localhost:9876`，非默认地址时同步设置 `FORGE_MCP_HOST`、`FORGE_MCP_PORT`，需要鉴权时设置 `FORGE_MCP_TOKEN`；
- 执行 Forge 操作前检查连接：Codex 用户可运行 `codex mcp list`，Claude Code 用户可运行 `claude mcp list`；两种客户端也都可在 TUI 中输入 `/mcp`。场景查询和编辑需要 Blender 插件侧 Bridge 运行；读取 Skills 和搜索本地文档不依赖 Bridge。
- `mcp-server` 与 `addon/Forge` 是两个独立组件：前者负责 Agent 侧 stdio MCP，后者安装在实际拥有场景的 Blender 中。Blender 版本要求见[安装 Forge](../installation.md)。通过 Agent 操作场景需要同时配置这两个组件。
- 若仅分发 `mcp-server`，直接保留 `forge_mcp/skills` 和 `forge_mcp/docs` 源码目录，并按上述安装脚本创建环境；`FORGE_BLENDER_DOCS_DIR` 可用于覆盖默认的 Blender 文档目录。
- 跨机器连接时，在插件偏好设置（或后台命令的 `--host` / `--port` / `--token`）配置 bridge，再在客户端进程设置 `FORGE_MCP_HOST` / `FORGE_MCP_PORT` / `FORGE_MCP_TOKEN`；两端 Token 必须一致，非 localhost 必须使用 Token，并用防火墙或 VPN 限制端口访问。
- **Bridge 需要 Blender 允许在线访问**：未开启时不会监听端口。后台启动 Blender 时使用 `--online-mode`；GUI 中在偏好设置的网络选项中允许在线访问。启动失败时，查看 Forge 偏好设置中的 **Debug** 错误信息。

完整配置和环境变量见 [`mcp-server/README.zh-CN.md`](../../reference/mcp-server/README.zh-CN.md)。

---

[上一章：界面总览](00_ui_overview.md) · [返回目录](../forge_docs.md) · [English](../../en/forge_docs/01_mcp_server.md) · [下一章：Global 与 General](02_global_and_general.md)
