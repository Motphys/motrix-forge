# Chapter 1: MCP service

[Previous: UI overview](00_ui_overview.md) · [Contents](../forge_docs.md) · [中文](../../cn/forge_docs/01_mcp_server.md) · [Next: Global and General](02_global_and_general.md)

## Add-on-side MCP service port

<div style="flex: 1; text-align: center; ">
    <img src="../../assets/images/manual/00-forge-sidebar-overview-1.png" width="292" alt="MCP panel">
</div>

Service configuration:

See [Config Forge](../preferences.md) for the complete connection, Polling, Startup, and Debug settings.

- **Address:** `localhost` by default.
- **Port:** `9876` by default.
- **Auto-start server:** the automatic startup option in the add-on preferences; enabled by default.
- **Authentication Token:** configure a shared token when the listening address is not localhost.
- **Log requests to console:** toggle request/response logging immediately, without restarting the Bridge. Logs go to Blender's system console, rather than the Python Console editor; on Windows, use **Window → Toggle System Console**.

**Start/Stop MCP Bridge** in the sidebar controls the TCP bridge on the Blender add-on side. It is not the MCP server on the agent side.

## Agent-side MCP service

Use it as follows:

- Prepare the workspace and install dependencies using [MCP setup and connection](../../reference/MCP_INSTALL.md). The full repository's development environment uses the root `.venv`; a minimal MCP workspace uses `mcp-server/.venv`.
- Make sure Forge is enabled in Blender and start the add-on-side MCP bridge.
- Start Claude Code or Codex from the workspace directory. The client reads its configuration and automatically starts and manages Forge MCP Server. For the full installation, startup, and connection checks, see [MCP setup and connection](../../reference/MCP_INSTALL.md).
- Claude Code reads `.mcp.json` at the workspace root. Codex uses the workspace's `.codex/config.toml`; see the installation guide for startup instructions.
- **Portable workspace:** copy the complete workspace, including `.mcp.json`, `.codex/config.toml`, and `mcp-server/`, to any location. In a console run `mcp-server/install.ps1` on Windows or `bash mcp-server/install.sh` on Unix-like systems to install dependencies, then start the agent (`claude` or `codex`) from that directory. Codex should use `CODEX_HOME="$PWD/.codex"`. The host machine must have [uv](https://docs.astral.sh/uv/) installed.
- The default connection is `localhost:9876`. For a non-default address, set `FORGE_MCP_HOST` and `FORGE_MCP_PORT`; set `FORGE_MCP_TOKEN` when authentication is enabled.
- Check the connection before running Forge operations: Codex users can run `codex mcp list`, while Claude Code users can run `claude mcp list`; `/mcp` is also available in either client's TUI. Scene queries and edits require the Blender-side Bridge. Reading Skills and searching local documentation do not.
- `mcp-server` and `addon/Forge` are independent components. The former provides agent-side stdio MCP; the latter runs in the Blender instance that owns the scene. See [Installation Forge](../installation.md) for Blender version requirements. Operating scenes through an agent requires both components.
- When distributing only `mcp-server`, keep the source directories `forge_mcp/skills` and `forge_mcp/docs` and create the environment with the installation scripts above. Use `FORGE_BLENDER_DOCS_DIR` to override the default Blender documentation directory.
- For cross-machine connections, configure the bridge in the add-on preferences or with the background command's `--host`, `--port`, and `--token` options; set `FORGE_MCP_HOST`, `FORGE_MCP_PORT`, and `FORGE_MCP_TOKEN` in the client process. Both sides must use the same token. Non-localhost listeners must use a token and should be protected by a firewall or VPN.
- **The Bridge requires Blender's online-access permission.** Without it, the port does not listen. Use `--online-mode` for background launches, or allow online access in Preferences for GUI sessions. If startup fails, check the **Debug** error message in Forge preferences.

For the complete configuration and environment-variable reference, see [`mcp-server/README.md`](../../reference/mcp-server/README.md).

---

[Previous: UI overview](00_ui_overview.md) · [Contents](../forge_docs.md) · [中文](../../cn/forge_docs/01_mcp_server.md) · [Next: Global and General](02_global_and_general.md)
