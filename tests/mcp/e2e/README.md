# MCP / Forge end-to-end tests

These scripts drive the `forge-mcp` server over stdio against a Blender that has
the Forge add-on loaded. There are two kinds, and the distinction matters
because one kind owns the Blender it talks to and the other borrows yours.

## Automated (run by `run_all_tests.py`)

| Script | Blender | Port | What it does |
| --- | --- | --- | --- |
| `driver.py` | launches its own headless Blender | 9877 | Smoke suite over the public MCP tools, asserting on real `bpy.ops.forge.*` results. |
| `full_model_matrix.py` | launches its own headless Blender | 9878 | Creates every Forge model type and declared subtype, edits each one through the MCP editing tools, and prints a pass/fail matrix. |

Each spawns its own Blender on `FORGE_E2E_PORT` (`--port` also selects it), and
both ports are deliberately distinct from the live session port 9876, so these
can never touch a Blender you have open. `_bridge_setup.py` and
`_bridge_full_setup.py` are their Blender-side bootstraps — one per driver, each
with a matching default port — and are not meant to be run directly.

## Manual probes (`live_*.py`, `cleanup_*.py`)

These attach to an **already running** Blender bridge — `FORGE_MCP_PORT`,
default **9876** — and work on whatever scene that Blender has open; most of
them create, edit and delete objects there. Nothing wires them into a runner,
and they do not save the file, so treat them as debugging aids:

- `live_multibody_matrix.py` — multi-body build/edit/export round-trip.
- `live_hardware_target_matrix.py` — every Hardware type and subtype created as
  both a single-target and a multi-target relationship, checked against the
  exported MJCF. Needs an **empty file** (it compares whole-export relationship
  counts against what it created, and the exporter reads the file-global Forge
  collections rather than the current scene) and exits with code 2 rather than
  touching a file that already holds anything. Cleanup diffs against a pre-run
  snapshot, so it also removes the collections Forge created for the rig and
  puts back the scene-level Forge properties the run wrote.
- `live_create_excavator.py` / `live_validate_excavator.py` — build a small
  excavator, then re-read and mesh-check it.
- `live_sensor_probe.py`, `live_contact_probe.py`, `live_gear_probe.py`,
  `live_attach_valid_probe.py`, `live_issue_probe.py` — focused probes for the
  sensor, contact, actuator/gear, attach and reported-issue paths.
- `live_tool_coverage_matrix.py` — exercises **every** registered MCP tool once
  (create, edit, query, validate, CoACD, export/save/import) and fails if any
  tool in the server's registry was never called. Needs a file with a single
  empty scene **named `Scene`** and exits with code 2 otherwise: it ends with an
  MJCF import, which clears every scene except `Scene`. Cleanup restores the
  pre-run snapshot, so the file is left as it was found.
- `live_skill_gate_probe.py` — checks the three `FORGE_MCP_SKILL_GATE` modes
  over the real stdio server: default `soft` needs no prewarm and returns a
  one-time `skill_hint`, `strict` still refuses until the guide is read.
- `live_scene_detail.py` — read-only dump of scene info and one object's detail.
- `cleanup_all_live.py` — deletes **every** object in the attached scene.
  Requires `--yes`.
- `cleanup_live_probe.py` — deletes only the leftovers those probes create
  (`LNK_Link` and the `INC__live_*_external_xml` includes). Requires `--yes`.

Each probe selects its port with `FORGE_MCP_PORT`; `live_issue_probe.py` and the
two cleanup scripts also accept `--port`. Point them at a scratch Blender unless
you mean to work in your own session:

```bash
# against a scratch Blender you started yourself, on any free port:
FORGE_MCP_PORT=9880 python tests/mcp/e2e/live_sensor_probe.py
python tests/mcp/e2e/live_issue_probe.py --port 9880
# against your own live session on 9876:
python tests/mcp/e2e/cleanup_all_live.py --yes --port 9876
```

Temporary MJCF files and exports go to a scratch directory (or a uniquely named
file that the probe removes); no generated output belongs in this folder.
