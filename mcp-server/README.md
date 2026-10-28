# Forge MCP Server Reference

[中文说明](README.zh-CN.md)

This page covers the agent-side MCP Server architecture, environment variables, Skills and document discovery, tool categories, and development. Initial installation, client configuration, startup, and connection troubleshooting live in [MCP setup and connection](../MCP_INSTALL.md).

## Runtime architecture

```text
AI agent ──stdio──> Forge MCP Server ──TCP──> Blender Forge MCP Bridge
```

The MCP Server runs beside the agent; the Bridge runs in the Blender process that owns the scene. Scene queries and modeling operations go through the Bridge. Skill reads and documentation searches use files local to the server and do not require Blender to be running. For Blender-side preferences and dependencies, see [Config Forge](../docs/content/en/preferences.md).

## Client startup and process management

After preparing the environment as described in [setup and connection](../MCP_INSTALL.md), use this workflow:

1. Enable Forge in Blender and start the **MCP Bridge**.
2. Start Claude Code or Codex from the workspace directory containing the client configuration.
3. The client reads the workspace configuration, starts and manages Forge MCP Server automatically, and communicates with it over stdio.
4. Check the MCP connection status in the client and confirm that `forge` is connected before running Forge operations.

After changing environment variables, Skills, or document files, reconnect or restart the MCP server through the client. Restarting only the Blender Bridge does not reload server-side documentation.

## Runtime configuration

| Env var              | Default     | Description                                                     |
| -------------------- | ----------- | --------------------------------------------------------------- |
| `FORGE_MCP_HOST`     | `localhost` | Blender bridge host                                             |
| `FORGE_MCP_PORT`     | `9876`      | Blender bridge port                                             |
| `FORGE_MCP_TOKEN`    | *(empty)*   | Shared bridge token; required when Blender binds outside localhost |
| `FORGE_MCP_TIMEOUT`  | `1800`      | Response timeout in seconds (matches the addon deferred timeout) |
| `FORGE_MCP_SKILL_GATE` | `soft`    | How the authoring-guide gate behaves: `soft` runs the operation and attaches a one-time `skill_hint` naming the guide, `strict` refuses until the guide is read, `off` never intervenes |
| `FORGE_SKILLS_DIR`   | *(search)*  | Directory holding the skill `.md` guides served by `forge_skill` |
| `FORGE_DOCS_DIR`     | *(search)*  | Directory holding the MJCF reference `.md` files searched by `forge_search_docs` |
| `FORGE_BLENDER_DOCS_DIR` | *(search)* | Blender docs root containing `api/` and `manual/` RST files (searched recursively) |
| `FORGE_TOOLS`        | *(all)*     | Serve only the listed tool categories / name substrings; `readonly` keeps just the read-only tools; an invalid non-empty filter fails startup |

## Skills and document discovery

At startup the server loads all `*.md` guides from the first populated Skills directory (search order: `FORGE_SKILLS_DIR`, the source-tree `forge_mcp/skills/`, any legacy `skills/` directory up the package path, then `./skills`). A one-line index of the loaded guides is injected as the server instructions, and each guide is served on demand by the `forge_skill` tool (`forge_skill(name="create")` / `forge_skill(name="modify")` / `forge_skill(name="operators")` / `forge_skill(name="custom_material")`), so agents discover the guides automatically but only pay the context cost when used. Pass `section` to fetch a single heading instead of the whole guide (e.g. `forge_skill(name="create", section="joint")` or `forge_skill(name="operators", section="create_sensor")`).

The `forge_mcp/docs/mjcf/*.md` element reference (same discovery scheme via `FORGE_DOCS_DIR` / `forge_mcp/docs/mjcf` on the package path) is loaded into a paragraph-level search index served by `forge_search_docs`. The same reference is also exposed as MCP **resources** (`mjcf://<element>` per doc file, `mjcf://index` for the element hierarchy / path registry) so agents that prefer native resource reads can pull a whole document directly; `forge_search_docs` remains for keyword search.

Read `forge_skill(name="create")` before authoring and `forge_skill(name="modify")` before editing. Enforcement is controlled by `FORGE_MCP_SKILL_GATE`: default `soft` allows the operation and attaches a one-time reading hint after a successful call; `strict` refuses operations until the required guide has been read. `forge_execute` uses the same policy for explicit `bpy.ops.forge.*` calls and `Forge_*` property writes; ordinary Blender modeling scripts are unaffected by this Forge gate. Tool filters retain `forge_skill` for operation access. Full authoring rules live in [MCP Skills](../docs/content/en/mcp_skills.md).

`forge_execute` injects `bpy` and `mathutils` into the script namespace. Scripts must assign a JSON-serializable dictionary to `result`, for example `result = {"scene": bpy.context.scene.name}`.

Blender RST documentation is loaded recursively from `forge_mcp/docs/blender/`, including `api/` and `manual/`. Discovery checks `FORGE_BLENDER_DOCS_DIR`, `forge_mcp/docs/blender/`, `docs/blender/` along the package's ancestor paths, then `./docs/blender/`; the first populated directory wins independently of MJCF. Missing Blender documentation is allowed. Restart the server after changing documentation files.

`forge_search_docs` searches both references by default. Use `source="mjcf"`, `"blender"`, `"blender_api"`, or `"blender_manual"` to narrow results:

```python
forge_search_docs(query="bpy.ops.mesh.bevel", source="blender_api")
forge_search_docs(query="bevel modifier", source="blender_manual", max_results=5)
forge_search_docs(query="condim", source="mjcf")
```

RST headings and API directives become section breadcrumbs, including fully qualified function/property names. Text, parameter fields and inline code are searchable; presentation metadata is omitted. This text parser does not build Sphinx, execute directives, or expand external includes. Results contain `source`, `path` (e.g. `blender/api/bpy.ops.mesh.rst`, relative to `docs/`), `breadcrumb`, `text`, `score`, and `index`; existing MJCF paths stay unchanged. Results are sorted by score and context stays within the matching section. Documentation search requires no running Blender instance.

## Tools

`forge_mcp.tools` registers tools by module:

- `create.py` — `forge_create_*`: link, inertial, joint, geometry, collider, height_field, plane, site, actuator, tendon, equality, contact, sensor, light, camera, frame, replicate, attach, include, material.
- `modify.py` — `forge_define_*`: model_type, geometry_type, collider_type, site_type, joint_type, actuator_type; plus define_parent, mark_root_link, mark_instance_link, mesh_check, scale_gizmo_size.
- `utilities.py` — scene_info, batch_rename, set_instance_idname, select_by_tag, select_hulls.
- `scene.py` — generic editing: object_info, measure, scene_config, set_transform, set_shape_size, set_property, set_scene_property, set_tendon_targets, rename, delete, execute.
- `geometry.py` — `forge_coacd`: decompose one Forge `VISUAL` mesh into new Collider hulls while preserving the source object.
- `io.py` — modal MJCF import/export plus explicit blend-file saving.
- `capture.py` — `forge_screenshot`: capture an area (default the 3D viewport) or the whole window as a PNG image, with imbuf downsampling to a size budget; `layout=True` returns the window layout as JSON instead.
- `blendfile.py` — `forge_blendfile_summary`: path/save status/backups, datablock counts, missing external files, linked libraries (direct vs indirect).
- `docs.py` — `forge_search_docs`: ranked full-text search over the bundled MJCF element reference and local Blender RST API/manual.
- `skill.py` — `forge_skill`: return the full text of an auto-loaded `skills/*.md` authoring guide, or a single section via `section` (`forge_skill(name="create", section="joint")`); unknown / ambiguous section names raise listing the available ones.

Tools are annotated with MCP `ToolAnnotations` (`tools/_hints.py`): read-only hints on query tools, destructive hints on recursive delete, arbitrary execute, MJCF import, CoACD and blend-file saving.

Every op tool (`create` / `modify` / op wrappers in `utilities`) accepts `select: list[str]` — object names that replace the Blender selection before the operator runs (order matters, first becomes active; `null` keeps the current selection). Results include `created`: names of new scene objects, so generated names never need guessing.

Conventions worth knowing (learned building a Newton's cradle end-to-end):

- A joint's exported rotation axis is its **local +Z in parent space** — rotate the joint object so its Z points along the desired world axis.
- Shape sizes are **local** to the parent (a child link's local frame differs from world) — check with `forge_measure` (world bboxes) after editing.
- `mesh_check` ignores boundary-only point-point, point-edge, point-face, edge-edge, and edge-face contact when incident geometry does not cross the other mesh. A coplanar shared face is also valid when its plane separates both complete objects, independent of winding; non-separating coplanar overlap and actual crossings remain intersections. Valid contact needs no epsilon gap.
- Blender silently suffixes name collisions (`.001`) — including with orphaned (out-of-scene) datablocks; `forge_rename` refuses instead.
- `Forge_Model_Type` is stored as an enum **index**; tools resolve it to names (`LINK`, `JOINT`, ...).

Note: `bpy.ops.forge.properties_*` popup dialogs are UI-only and ineffective for agents — parameters are changed via direct property access (`obj.Forge_<Type>.<property>`) and shape / gizmo sizes via `obj.modifiers[...]`.

## Development and tests

From the full repository root:

```bash
uv sync
uv run pytest tests/mcp/unit tests/mcp/integration
```

`uv sync` installs `forge-mcp` in editable mode into the root `.venv`, alongside add-on test dependencies. `uv sync --all-packages` is also supported. End-to-end tests require Blender; see [Development Forge](../docs/content/en/development.md).

For server-package development in an independent source directory:

```bash
cd mcp-server
uv venv --python 3.11
uv pip install --editable .
```

Keep `forge_mcp/skills/` and `forge_mcp/docs/` with the source. Installer and client startup instructions are maintained only in [setup and connection](../MCP_INSTALL.md).
