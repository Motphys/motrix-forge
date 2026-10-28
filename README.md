<div align="center">

# Motrix Forge

**Make articulated multibody configuration easier.**

[![Download 0.1.0](https://img.shields.io/badge/Download-0.1.0-2ea44f?style=for-the-badge)](https://github.com/Motphys/motrix-forge/releases)
[![Blender 4.5 LTS](https://img.shields.io/badge/Blender-4.5-F5792A?style=for-the-badge&logo=blender&logoColor=white)](https://www.blender.org/releases/4-5/)
[![Blender 5.2 LTS](https://img.shields.io/badge/Blender-5.2-F5792A?style=for-the-badge&logo=blender&logoColor=white)](https://www.blender.org/releases/5-2/)
[![GitHub License](https://img.shields.io/github/license/motphys/motrix-forge?style=for-the-badge)](https://github.com/Motphys/motrix-forge/blob/main/LICENSE)

[简体中文](README.zh-CN.md)  · [Releases](https://github.com/Motphys/motrix-forge/releases) · [Report an issue](https://github.com/Motphys/motrix-forge/issues/new?template=bug_report.yml)

</div>

<div align="center">
	<img src="media/images/forge_pipeline.png" alt="forge_pipeline">
</div>

## Overview

**Forge** is an extension tool for efficiently creating, editing, and configuring XML scenes that precisely describe the kinematic structure, inertial properties, visual geometry, collision geometry, actuators, and sensors of articulated multibody systems. It primarily solves the lack of visual editing tools for MJCF and simplifies the creation, editing, and configuration of XML scene descriptions. At its core are the **Forge** add-on and its companion **MCP Server**. The tool supports creating, editing, validating, importing, and exporting MJCF scene descriptions in Blender, and can also expose Forge capabilities to AI agents such as Codex and Claude Code through MCP.

> **Forge** is developed on [**Blender 4.5 LTS**](https://www.blender.org/releases/4-5/) and [**Blender 5.2 LTS**](https://www.blender.org/releases/5-2/). Using **Forge** requires familiarity with **Blender**.

### Main capabilities

- **Create MJCF model structures**: create and organize Links, Joints, Geometry, Colliders, Sites, Inertials, Actuators, Tendons, Sensors, Equalities, Contacts, Lights, Cameras, and other model elements;
- **Edit model definitions and properties**: configure Global/General parameters, model types, geometry and materials, kinematics, hardware, Meta Elements, and object properties such as parent-child relationships, root Links, instance Links, and transforms;
- **Edit interactively in the viewport**: adjust Shape, Link, Joint, Actuator, Tendon, Sensor, and other MJCF properties through the Forge panel, property panels, and Gizmos while inspecting the scene structure in real time;
- **Import and export**: import existing MJCF-standard .XML files and convert them into Forge-convention scene structures, or export a scene configured with Forge as a standard MJCF .XML file, and save the Blender project file;
- **Mesh and collision processing**: run mesh checks and use CoACD to decompose complex meshes into convex hulls suitable for collision detection;
- **MCP automation**: through the MCP Bridge, let agents such as Claude Code and Codex query scenes, call Forge Operators, create or modify models, run import/export, inspect multibody relationships, and more.

#### Component decomposition

<div align="center">
    <img src="media/images/decomposition.png" alt="Decomposition"/>
</div>
*An exploded view of the elements that make up a Forge model in Blender. These elements can be arranged by Forge model type into different layers or collections in Blender, which avoids clutter or obstructed views when editing very complex models.*

### Use cases

![forge_pipeline](/media/videos/HD/forge_pipeline.mp4)
*Edit and configure a wheel loader with Forge → edit and configure the loader's working environment → export and simulate and train in MotrixSim*

![arbitrary_robotic_arm](/media/videos/HD/arbitrary_robotic_arm.mp4)
*Edit and configure an arbitrary robotic arm with Forge → export and simulate and train in MotrixSim*

![forge_with_agent](/media/videos/HD/forge_with_agent.mp4)
*Use an agent to create, edit, and configure the scene in the image through Forge → export and simulate in MotrixSim*

> MJCF is a standardized XML scene format for precisely describing the kinematic structure, inertial properties, geometric collision, and actuator/sensor configuration of articulated multibody systems. It is the data foundation for MotrixSim's contact-intensive simulation and embodied-intelligence policy training.

> The Forge add-on and `mcp-server` are two independent components: the add-on runs in the process that owns the Blender scene, while `mcp-server` runs on the agent side. Before using MCP tools, you must install and enable Forge in Blender and start the MCP Bridge (default `localhost:9876`).

## Repository layout

```shell
Motrix-Forge/
├── addon/
│   └── Forge/              # Blender add-on source, assets, and MCP Bridge
├── docs/                   # Self-contained documentation site
├── mcp-server/
│   └── forge_mcp/          # Agent-side stdio MCP server, tools, skills, and documentation indexes
├── tests/
│   ├── forge/              # Blender add-on tests
│   └── mcp/                # MCP unit, protocol integration, and end-to-end tests
├── pyproject.toml          # Root development environment and uv workspace configuration
├── run_tests.py            # Forge Blender test entry point
└── run_all_tests.py        # All-suite test entry point
```

The MCP data path is:

```shell
AI agent ──stdio──> Forge MCP Server ──TCP──> Forge MCP Bridge in Blender
                                                        │
                                                        └──> scene and bpy.ops.forge.*
```

The Forge add-on performs operations in the Blender process; `mcp-server` wraps those operations as MCP tools for an agent. The default bridge endpoint is `localhost:9876`.

## Requirements

- Blender 4.5 LTS (4.5.6 or later in the 4.5 series) or Blender 5.2 LTS;
- Python 3.11 (the root development environment requires `>=3.11,<3.14`);
- [uv](https://docs.astral.sh/uv/) for dependency management and running the MCP server;
- Optional: Codex CLI, Claude Code, or another stdio MCP client.

## Quick start

### 1. Install the Forge add-on

If you only need to author MJCF models in Blender, install the add-on by itself:

1. Package `addon/Forge` as a ZIP whose root contains `blender_manifest.toml`;
2. In Blender, open **Edit → Preferences → Add-ons → Install from Disk**;
3. Select the ZIP and enable **Forge**;
4. In the add-on **Dependencies** settings, install `tetgen` and **CoACD**, then restart Blender;
5. Open the 3D View sidebar (`N`) and verify that the Forge panel is visible.

Detailed operation guides:

- [Motphys Forge README](addon/README.md)
- [Motphys Forge documentation index](https://motphys.github.io/motrix-forge/)
- [Forge operator guide](https://motphys.github.io/motrix-forge/en/forge_docs.html)

### 2. Set up the development environment

From the repository root:

```bash
uv sync
```

The root is a uv workspace. This creates the shared `.venv`, installs test dependencies, and installs the editable `forge-mcp` package from `mcp-server`.

### 3. Connect an AI agent (optional)

1. Enable Forge in Blender and turn on **Auto-start server**, or click **Start MCP Bridge**;
2. Confirm that the bridge listens on `localhost:9876`;
3. Start the MCP client from the repository root. Claude Code and similar clients read `.mcp.json`; Codex uses `.codex/config.toml`.

PowerShell example for Codex:

```powershell
$env:CODEX_HOME = (Join-Path (Get-Location) '.codex')
codex
```

Check the connection with:

```bash
codex mcp list
```

For Claude Code, run `claude mcp list` or enter `/mcp` in the TUI to inspect the `forge` connection.

Detailed operation guides:

- [Forge MCP installation guide](https://motphys.github.io/motrix-forge/reference/MCP_INSTALL.html)
- [Forge MCP Server README](https://motphys.github.io/motrix-forge/reference/mcp-server/README.html)

For connections across machines, set the same non-empty token on both sides and restrict the bridge port with a firewall or VPN.

## Development and testing

Run MCP unit and protocol integration tests without Blender:

```bash
uv run pytest tests/mcp/unit tests/mcp/integration
```

Run the Forge add-on tests (the runner discovers Blender 4.5+ automatically, preferring the newest installation):

```bash
uv run python run_tests.py
```

If Blender is not in a standard installation directory or on `PATH`, set `BLENDER_PATH` (or the legacy `BLENDER_45_PATH`) to the Blender executable.

Run the MCP/Blender end-to-end tests:

```bash
uv run python tests/mcp/e2e/driver.py
```

Run every test suite:

```bash
uv run python run_all_tests.py
```

Run Ruff from the repository root. File discovery is limited to `.py` scripts by `ruff.toml` (also configured for standalone work in `addon/`); Markdown, notebooks, and other files are outside this scope.

Format Python scripts:

```bash
uv run ruff format .
```

Check lint rules and formatting without modifying files:

```bash
uv run ruff check .
uv run ruff format --check .
```

## Documentation

Run `uv sync` to install documentation dependencies into the root `.venv`, then preview the site with `python docs/scripts/docs.py serve`. Build static HTML with `python docs/scripts/docs.py build --strict`; output goes to `docs/site/`. See [Site maintenance](docs/README.md).

For a better reading experience, we recommend opening the repository root as an [Obsidian](https://obsidian.md/) vault. Obsidian makes it easier to navigate the documentation hierarchy, relative links, and embedded images. It is optional and is not required to install or run the project.

- [Motphys Forge README](addon/README.md)
- [Motphys Forge documentation index](https://motphys.github.io/motrix-forge/)
- [Forge operator guide](https://motphys.github.io/motrix-forge/en/forge_docs.html)
- [Forge MCP installation guide](https://motphys.github.io/motrix-forge/reference/MCP_INSTALL.html)
- [Forge MCP Server README](https://motphys.github.io/motrix-forge/reference/mcp-server/index.html)

## Contributing

Contributions are welcome in code, bug reports, documentation, translations, examples, and Blender compatibility testing.

### Apply to contribute

1. Open an [Issue](https://github.com/Motphys/motrix-forge/issues) describing the area you want to contribute to, the problem or proposed improvement, and your planned approach. For larger changes, discuss the scope with maintainers before implementation.
2. For code or documentation changes, fork the repository, create a focused branch, and submit a Pull Request referencing the Issue. Small fixes can be submitted directly as a Pull Request.
3. To participate in ongoing maintenance, include a brief introduction, relevant experience or previous contributions, the area you would like to maintain, and your expected availability in the Issue. Maintainers will discuss responsibilities and repository access with you as needed; contributor status does not automatically grant write access.

### Contribution requirements

- Read the [development guide](https://motphys.github.io/motrix-forge/en/development.html) and follow the existing project structure and coding style. Keep each Pull Request focused on one problem.
- Explain the problem, resulting behavior, and verification in the Pull Request. Add reproduction steps for bug fixes and update or add relevant tests when behavior changes.
- Run the applicable tests from [Development and testing](#development-and-testing). Python changes must pass Ruff lint and formatting checks; documentation changes must pass the strict documentation build.
- For Blender API or UI changes, verify the affected behavior in Blender 4.5 LTS and 5.2 LTS. Include screenshots for UI changes, and state the versions tested and any checks you could not complete.
- Keep English and Chinese documentation consistent when user-facing behavior changes. Use assets you have permission to contribute, and do not commit credentials, local environments, generated site output, or unrelated files.
- Communicate respectfully, respond to review feedback, and resolve review comments before merging. Maintainers review contributions for correctness, compatibility, and maintainability.

## License

Copyright (C) 2020-2026 Motphys Technology Co., Ltd. All Rights Reserved.

Motrix Forge is licensed under the GNU General Public License, version 3 or (at your option) any later version (`GPL-3.0-or-later`). See [LICENSE](LICENSE) for the full terms. Third-party components retain their respective copyright notices and licenses.

## Feedback

When reporting an issue, include the Blender version, the add-on or repository commit, reproduction steps, expected and actual results, and relevant logs. For MCP connection issues, also include the client, bridge host and port, and the `forge` service connection status. Do not include access tokens.

[中文](README.zh-CN.md) | **English**
