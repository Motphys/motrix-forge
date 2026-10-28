# Forge MCP Setup and Connection

[中文](MCP_INSTALL.zh-CN) | **English**

This page covers the path from preparing a workspace to a working client connection. Full environment-variable definitions, server operation, Skills and document discovery, and development are maintained in the [server reference](mcp-server/README.md).

The agent-side stdio MCP server lives in `mcp-server/`. Client configuration is provided in `.mcp.json` (Claude Code and similar clients) and `.codex/config.toml` (Codex). You can clone or copy the following four items into an empty workspace and start the agent from there:

```text
.claude/
.codex/
.mcp.json
mcp-server/
```

A minimal MCP workspace needs only the items above; no Blender test project is required. Scene queries and edits require Blender with `addon/Forge` installed and enabled and the add-on's MCP Bridge running (default `localhost:9876`). Reading Skills and searching local documentation do not require Blender to be running.

## Check Blender before connecting

Complete the [Forge add-on installation](docs/content/en/installation.md), enable Forge in the Blender instance that owns the scene, and allow Blender online access. Click **Start MCP Bridge** in the Forge sidebar and confirm it is running. Listener, token, startup, and polling controls are documented in [Config Forge](docs/content/en/preferences.md).

## 1. Prepare a workspace

Clone the repository to obtain the complete layout:

```bash
git clone <repository-url> forge-mcp-workspace
cd forge-mcp-workspace
```

If you copy an existing checkout, include the hidden directories and `.mcp.json` listed above; do not copy only `mcp-server/`. Check that the configuration items beginning with `.` are included in the copy.

## 2. Install MCP dependencies

Install [uv](https://docs.astral.sh/uv/) first. In a full checkout containing the root `pyproject.toml`, run `uv sync` from the repository root to prepare the root `.venv` used by the client. See the [development environment instructions](docs/content/en/development.md#set-up-the-development-environment) for details.

For a minimal MCP workspace containing only the items listed above, run the installer below from that workspace. It creates a Python 3.11 environment in `mcp-server/.venv` and installs `mcp` and `forge-mcp` without modifying the system Python.

Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\mcp-server\install.ps1
```

macOS / Linux / WSL:

```bash
bash mcp-server/install.sh
```

The installer can launch a client after installation:

```powershell
.\mcp-server\install.ps1 -Launch claude
.\mcp-server\install.ps1 -Launch codex
```

```bash
bash mcp-server/install.sh claude
bash mcp-server/install.sh codex
```

These installers prepare a workspace for using the server. To modify source and run tests, use the [development environment in the server reference](mcp-server/README.md#development-and-tests).

## 3. Start an agent in the workspace

Open a new terminal and change to the workspace:

```powershell
cd C:\path\to\forge-mcp-workspace
claude       # Claude Code
```

```powershell
cd C:\path\to\forge-mcp-workspace
$env:CODEX_HOME = (Join-Path (Get-Location) '.codex')
codex        # Codex CLI
```

On macOS / Linux, use `export CODEX_HOME="$PWD/.codex"`. With `CODEX_HOME` set, Codex reads the copied `.codex/config.toml`; Claude Code reads `.mcp.json` from the workspace root. The client automatically starts the MCP server over stdio using its configuration. A minimal MCP workspace uses the installer's `mcp-server/.venv`; the full repository's uv workspace uses the root `.venv`, which must first be prepared using the [development environment instructions](docs/content/en/development.md#set-up-the-development-environment). The `--no-sync` option only skips dependency synchronization; it does not create or repair the environment.

## 4. Verify the connection

- Codex: run `codex mcp list`, or enter `/mcp` in the TUI;
- Claude Code: run `claude mcp list`, or enter `/mcp` and confirm that `forge` is connected;

The default port is `9876`. For a non-default or remote endpoint, set `FORGE_MCP_HOST` and `FORGE_MCP_PORT` consistently in the `env` sections of `.mcp.json` and `.codex/config.toml`. Cross-machine connections must also use the same non-empty `FORGE_MCP_TOKEN` on both sides; restrict the bridge port with a firewall or VPN.

## Connection troubleshooting

| Symptom | Check first |
| --- | --- |
| No `forge` entry in the client | Workspace location, client configuration, and whether the client was restarted |
| Server process fails to start | Installer results, availability of `uv`, and tool filters or directory overrides in [runtime configuration](mcp-server/README.md#runtime-configuration) |
| MCP connects, but scene operations fail or time out | Blender is running, Forge is enabled, the Bridge is started, and host, port, and token match |
| Bridge fails to start | Blender online access and port availability; see [Config Forge](docs/content/en/preferences.md) |

The configuration uses `uv --no-cache run --no-sync` so server startup does not access the user-level uv cache. If Codex reports a handshake timeout, first run `uv --no-cache run --no-sync --directory mcp-server python -c "import forge_mcp.__main__; print('OK')"` from the workspace to check the environment. Neither this check nor MCP initialization requires a running Blender Bridge. Reconnect MCP or restart the client after changing its configuration; reload the Blender add-on after changing its code.

Once connected, use the [server reference](mcp-server/README.md) for runtime configuration and [MCP Skills](docs/content/en/mcp_skills.md) for authoring rules.

## Configuration files

- `.mcp.json`: MCP configuration read by Claude Code, Cursor, and similar clients;
- `.claude/settings.local.json`: enables the project's `forge` MCP entry;
- `.codex/config.toml`: project-level MCP configuration for Codex; the project must be trusted by Codex;

OpenAI's documentation explains that Codex CLI, IDE extensions, and the desktop app share MCP configuration. Project-level configuration is stored in `.codex/config.toml` for trusted projects; use `codex mcp list` or the TUI `/mcp` command to inspect the connection: <https://developers.openai.com/codex/mcp/>.

[中文](MCP_INSTALL.zh-CN) | **English**
