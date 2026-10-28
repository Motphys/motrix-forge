# Development Forge

The Blender add-on, agent-side MCP server, and documentation site share one repository and the root `.venv`. Choose validation steps based on your changes.

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

The add-on performs scene operations in Blender. The MCP Server exposes tool interfaces and calls the add-on's MCP Bridge over TCP. Documentation tools also use the root `.venv`, with dependencies declared in the root `pyproject.toml`.

## Set up the development environment

The root project declares **Python 3.11 ≤ version < 3.14** (`>=3.11,<3.14`). Install uv, then run from the repository root:

```bash
git lfs pull
uv sync
```

`uv sync` creates the shared `.venv`, installs root development dependencies, and installs `forge-mcp` from the `mcp-server` workspace member in editable mode. Server source changes do not require reinstalling the package each time.

Add-on tests also need a supported Blender installation. See [Config Forge: Dependencies](preferences.md#dependencies) for installing feature dependencies inside Blender.

## Python linting and formatting

Run these commands from the repository root. Ruff discovers only `.py` scripts, as configured in `ruff.toml` and `addon/ruff.toml`; Markdown, notebooks, and other files are outside this scope.

```bash
uv run ruff format .
uv run ruff check .
uv run ruff format --check .
```

`format` applies formatting; `check` checks lint rules, and `format --check` verifies formatting without modifying files.

## Run tests

Choose an entry point from the repository root based on the change:

| Scope | Validation entry point |
| --- | --- |
| MCP tools and protocol without starting Blender | `uv run pytest tests/mcp/unit tests/mcp/integration` |
| Forge add-on | `uv run python run_tests.py` |
| Actual MCP-to-Blender calls | `uv run python tests/mcp/e2e/driver.py` |
| All test suites | `uv run python run_all_tests.py` |

`run_tests.py` discovers Blender 4.5+, prefers the newest installation found, and runs add-on tests in a separate background Blender process. To specify an executable in PowerShell:

```powershell
$env:BLENDER_PATH = 'C:\Program Files\Blender Foundation\Blender 4.5\blender.exe'
uv run python run_tests.py
```

Replace the example path with the actual installation location. Forward pytest arguments to select relevant add-on tests:

```bash
uv run python run_tests.py -k inertia
```

`run_all_tests.py` also runs the full model matrix end-to-end suite. Its suites run sequentially.

## Verify UI changes

1. Package the current `addon/Forge`, install it in the test Blender, and confirm that the enabled add-on matches your checkout.
2. Restart Blender and open a model that reproduces the case.
3. Check the affected Operators, property panels, Gizmos, or import/export behavior.
4. Update the relevant English and Chinese operator documentation.

Background tests validate data and operation logic. Layout, interaction, and viewport preview changes also need inspection in Blender's UI.

## Change the documentation site

Run `uv sync` from the repository root to install dependencies, then preview the site using the shared root `.venv`:

```powershell
python docs/scripts/docs.py serve
```

Open <http://127.0.0.1:8000>. Markdown, image, style, and template changes rebuild automatically. Restart the preview server after changing `docs/scripts/docs_hooks.py`.

Build the static HTML intended for later hosting:

```powershell
python docs/scripts/docs.py build --strict
```

Output goes to the Git-ignored `docs/site/`; generated HTML does not need manual maintenance. Pair Chinese and English pages using matching filenames. Add operator chapters under each language's `forge_docs/` directory to include them automatically in navigation. See [Local preview](preview.md).

## Before submitting changes

- Run relevant tests and record the environment and results.
- Maintain both language versions and check language switching, images, and fragment links.
- Keep `.venv` and the generated `docs/site/` out of commits.
- For issue reports, include the Blender version, source commit, reproduction steps, expected and actual results, and relevant logs.

Continue to the [user manual contents](forge_docs.md) to learn add-on workflows.
