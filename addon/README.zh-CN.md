# Forge

**[详细介绍](../README.zh-CN)**

## 系统要求

- Blender 4.5 LTS 或 Blender 5.2 LTS；
- Windows、macOS 或 Linux；
- 使用 MCP 功能时，Agent 侧还需要安装 [uv](https://docs.astral.sh/uv/)、Claude Code 或 Codex CLI。

## 安装插件

1. 下载[Forge 插件 ZIP](http://gitlab.mp/motphys/blender-tools/-/archive/master/blender-tools-master.zip?path=addon/Forge)。
2. 打开 Blender，进入 **Edit → Preferences → Add-ons → Install from Disk**。
3. 选择 ZIP 文件并点击 **Install from Disk**。
4. 在 Add-ons 列表中搜索并勾选 **Forge**。
5. 打开 3D View 侧栏（`N`），确认 Forge 面板可见。

MCP 功能需要在 Forge 面板或设置中启动 **MCP Bridge**。默认监听 `localhost:9876`；远程连接时请同步配置主机、端口和访问令牌。

<div align="center">
  <img src="images/Addons.png" alt="Install the Blender add-on">
</div>


**安装依赖**：
- 用管理员权限启动 **Blender**；
- 在 **Preferences → Add-ons → Forge → Dependencies**；
- **Install** **tetgen** 和 **CoACD**；
- 重启 **Blender**。

<div align="center">
  <img src="images/forge-dep.png" alt="Forge Dependencies">
</div>

## 文档

- [Forge 中文操作文档](../docs/content/cn/forge_docs)
- [Forge English operator guide](../docs/content/en/forge_docs)
- [Forge 与 MCP 集成说明](../docs/content/cn/forge_docs/01_mcp_server)
- [Forge MCP 安装文档](../MCP_INSTALL.zh-CN)
- [mcp-server 中文说明](../mcp-server/README.zh-CN) · [English](../mcp-server/README)

## 反馈

反馈问题时请提供 Blender 版本、插件和 commit、操作步骤、预期与实际结果，以及日志。
