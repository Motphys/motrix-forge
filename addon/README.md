# Forge

**[Detailed introduction](../README)**

## Requirements

- Blender 4.5 LTS (4.5.6 or later in the 4.5 series) or Blender 5.2 LTS;
- Windows, macOS, or Linux;
- To use MCP features, the agent side also needs [uv](https://docs.astral.sh/uv/), Claude Code, or the Codex CLI.

## Install the add-on

1. Download the [Forge add-on ZIP](http://gitlab.mp/motphys/blender-tools/-/archive/master/blender-tools-master.zip?path=addon/Forge).
2. In Blender, open **Edit → Preferences → Add-ons → Install from Disk**.
3. Select the ZIP file and click **Install from Disk**.
4. Search for **Forge** in the Add-ons list and enable it.
5. Open the 3D View sidebar (`N`) and confirm that the Forge panel is visible.

MCP features require starting **MCP Bridge** from the Forge panel or settings. It listens on `localhost:9876` by default. For remote connections, configure the same host, port, and access token on both sides.

<div align="center">
  <img src="../media/images/Addons.png" alt="Install the Blender add-on">
</div>

**Install dependencies**:
- Start **Blender** with administrator privileges;
- In **Preferences → Add-ons → Forge → Dependencies**;
- **Install** **tetgen** and **CoACD**;
- Restart **Blender**.

<div align="center">
  <img src="../media/images/forge-dep.png" alt="Forge Dependencies">
</div>

## Documentation

- [Forge English operator guide](../docs/content/en/forge_docs)
- [Forge 中文操作文档](../docs/content/cn/forge_docs)
- [Forge and MCP integration guide](../docs/content/en/forge_docs/01_mcp_server)
- [Forge MCP installation guide](../MCP_INSTALL)
- [mcp-server README](../mcp-server/README) · [中文说明](../mcp-server/README.zh-CN)

## Feedback

When reporting an issue, include the Blender version, add-on and commit, reproduction steps, expected and actual results, and logs.
