# Forge operators

Complete inventory of every `bpy.ops.forge.*` operator implemented by the Forge addon (`addon/Forge`): signature with defaults, selection requirement (`poll`), behavior and the MCP tool that wraps it. Workflow rules live in the `create` / `modify` skills — this guide is the exhaustive lookup; fetch a single entry with `forge_skill(name="operators", section="<operator name>")`.

## Agent usage rules

- **Contract**: this inventory is the complete supported operator surface. Strictly follow it — never read, search or infer behavior from the addon source code (`addon/Forge/**`); source internals are not part of the interface. When an operator, parameter or enum value you need is not documented here or in the `create` / `modify` skills, it has no supported implementation: report the missing capability as feedback instead of improvising a workaround.
- Operators are grouped below as creation, definition, utility, file/IO, CoACD, UI-only popups, and add-on infrastructure. Sources: `ops/creation.py`, `ops/materials.py`, `ops/definition.py`, `ops/utilities.py`, `ops/io_ops.py`, `ops/coacd.py`, `ops/properties_operators.py`, `core/props.py`, `settings.py`, `mcp/operator.py`.
- Selection semantics: every `poll` below means *each selected object* must match the listed `Forge_Model_Type` set (`check_selected_model_types`, all-of). Operators additionally allowing an empty selection say "or nothing selected". Creation/definition operators read the **ordered** selection (`selected_order` custom property) — MCP `select=[...]` lists set that order.
- Creation / definition operators open a parameter dialog only via `INVOKE_DEFAULT`; calling with `EXEC_DEFAULT` plus keyword arguments runs headless — this is what the MCP wrappers do. Prefer the wrapper (`forge_create_*`, `forge_define_*`, ...) whenever one exists: it manages selection, waits for modal jobs and returns `created` names.
- **Modal** operators (`import_mjcf`, `export_mjcf`, `create_attach`, `create_include`) return `RUNNING_MODAL` and keep working on a UI timer; poll `Forge_Props.is_importing` / `is_exporting` / `is_attaching` / `is_including` for completion, or use the MCP wrappers that wait. Every modal operation also claims the scene-level slot `Forge_Props.modal_operation_active` (with `modal_operation_name` / `token` / `status` / `message`); a second modal operator fails while the slot is held — read, never write, these state properties.
- **UI-only** operators (section below) cannot be driven by agents — the agent path is direct property assignment (`obj.Forge_<Type>.<property>`, `scene.Forge_Props`, `scene.Forge_Temp_Props`) documented in the `modify` skill.
- File-browser helpers (`forge.temp_file` etc.) are drivable via `EXEC_DEFAULT` with an explicit `filepath`, but setting the target property directly is simpler and is what the MCP wrappers do.

## Creation operators

#### `forge.create_geometry(geometry_type='BOX', size_box=(1, 1, 1), size_radius=0.5, size_height=1)`

> - Requires: selection all in `[LINK, FRAME, REPLICATE]`, or nothing selected.
> - One `visual` per selected object as its child at local `[0, 0, 0]`; nothing selected → standalone visual in the `World` collection at the 3D cursor.
> - `geometry_type` in `[BOX, CAPSULE, CYLINDER, SPHERE]` (MESH excluded); size param per type: `BOX` → `size_box` (full dimensions), `SPHERE` → `size_radius`, `CAPSULE` / `CYLINDER` → `size_radius` + `size_height` (full straight-section height; the socket stores the same full height).
> - MCP: `forge_create_geometry`.

#### `forge.create_collider(collider_type='BOX', create_method='GEOMETRY_TYPE', auto_size=False, use_min_as_height=False, size_box=(1, 1, 1), size_radius=0.5, size_height=1)`

> - Requires: selection all in `[LINK, FRAME]`, or all `VISUAL`, or nothing selected.
> - `create_method='GEOMETRY_TYPE'` (default): only with `visual` selection — auto-detects shape from each visual (`MESH` included); size params unused and `collider_type` is **ignored** (the collider takes the visual's own geometry type).
> - `create_method='COLLIDER_TYPE'`: explicit `collider_type` in `[BOX, CAPSULE, CYLINDER, SPHERE, MESH]` with size params or `auto_size=True` (measure from selected visual); `MESH` bakes the visual geometry into a convex mesh collider and needs a `visual` selection.
> - `auto_size=True` is ignored with a `link`/`frame` selection or no selection: with no selected visual to measure, explicit size parameters (or their defaults) are used. A `replicate` selection is not accepted by this operator.
> - `use_min_as_height=True`: CAPSULE/CYLINDER only — the height is taken from the selected `visual`'s **smallest** bounding-box axis rather than its largest, and the shape is oriented along that axis. Only effective together with `auto_size=True`; with explicit `size_radius`/`size_height` the values are used as given and the flag is ignored.
> - MCP: `forge_create_collider` (exposes this parameter as `min_is_height`).

#### `forge.create_height_field()`

> - Requires: nothing selected. Creates a root `hfield` node (no parent) in the `World` collection at the 3D cursor.
> - MCP: `forge_create_height_field`.

#### `forge.create_plane()`

> - Requires: nothing selected. Creates a root `plane` node (no parent) in the `World` collection at the 3D cursor.
> - MCP: `forge_create_plane`.

#### `forge.create_site(site_type='SPHERE', size_box=(0.2, 0.2, 0.2), size_radius=0.1, size_height=0.2)`

> - Requires: selection all `LINK`. One `site` per selected link as its child.
> - `site_type` in `[BOX, CAPSULE, CYLINDER, SPHERE]`; size param mapping as `create_geometry`.
> - MCP: `forge_create_site`.

#### `forge.create_link()`

> - Requires: selection all in `[LINK, FRAME, REPLICATE]`, or all in `[VISUAL, COLLIDER]`, or nothing selected.
> - No parameters. Based on `[LINK, FRAME, REPLICATE]` → child at local `[0, 0, 0]`; based on `VISUAL` / `COLLIDER` with forge parent → sibling under that parent at the object's local position; based on parentless `VISUAL` / `COLLIDER` → link at the object's location marked `Root Link`; nothing selected → `World` collection root candidate (mark with `forge.mark_root_link`).
> - MCP: `forge_create_link`.

#### `forge.create_joint(joint_type='HINGE')`

> - Requires: selection all `LINK`. One `joint` per selected link as its child.
> - `joint_type` in `[FREE, BALL, SLIDE, HINGE]`.
> - MCP: `forge_create_joint`.

#### `forge.create_actuator(actuator_type='POSITION')`

> - Requires: selection all in `[LINK, JOINT, TENDON]`. One `actuator` per selected target.
> - `actuator_type` in `[GENERAL, MOTOR, POSITION, VELOCITY, ADHESION]`.
> - MCP: `forge_create_actuator`.

#### `forge.create_tendon(tendon_type='FIXED')`

> - Requires: at least 2 selected, all `JOINT`, every joint subtype in `[SLIDE, HINGE]`.
> - Creates a **single** `tendon` from the ordered selection; each target item exports `coef` (default `0.5`).
> - `tendon_type` currently only `FIXED`.
> - MCP: `forge_create_tendon`.

#### `forge.create_equality(equality_type='CONNECT')`

> - Requires: exactly 2 selected, all `LINK`, all `JOINT` or all `SITE`.
> - Dynamic type items: `JOINT` selection → `JOINT` only (joint-coupling equality); `LINK` / `SITE` selection → `CONNECT` / `WELD`.
> - Ordered selection: first object is `target1`, second is `target2`.
> - MCP: `forge_create_equality`.

#### `forge.create_sensor(Sensor_Type, set_ref=False, set_xbody=False, set_subtree=False)`

> - Requires: selection all `LINK`, all `JOINT`, all `SITE`, all in `[VISUAL, COLLIDER]`, or all in `[LINK, SITE, VISUAL, COLLIDER, CAMERA]` (mixed — also covers camera-only selections).
> - Available `Sensor_Type` items are computed from the selection / flags — full ranges in the `create` skill (joint → `Jointpos`/`Jointvel`; site → `Touch`…`Contact`; link → frame + subtree types; visual/collider → frame types + `Contact`; camera → frame types only).
> - `set_ref=True`: needs exactly 2 selected — first is target, second is reference.
> - `set_xbody` / `set_subtree`: only for `LINK` targets, mutually exclusive (`xbody` → xbody frame sensors, `subtree` → `Contact` only).
> - Contact subtree workflow: require exactly two `LINK` roots and use both `set_ref=True` and `set_subtree=True`. Ordered selection maps the first root to `subtree1` (`target`), the second to `subtree2` (`ref`); both must be explicitly set and verified in the exported sensor.
> - MCP: `forge_create_sensor`.

#### `forge.create_contact(contact_type)`

> - Requires: at least 2 selected, all `LINK`, or all in `[VISUAL, COLLIDER, PLANE, HFIELD]`.
> - Dynamic type items: `LINK` selection → `EXCLUDE` (default); geom selection → `PAIR` (default).
> - Creates one `contact` per **pair combination** of the ordered selection (n·(n−1)/2 objects).
> - MCP: `forge_create_contact`.

#### `forge.create_light(light_type, light_mode)`

> - Requires: selection all `LINK`, or nothing selected.
> - Dynamic items: nothing selected → `light_type` `[DIRECTIONAL, SPOT, POINT]`, `light_mode` `[FIXED, TRACK, TRACKCOM]` (defaults `DIRECTIONAL` / `FIXED`); links selected → `light_type` `[SPOT, POINT]` (default `SPOT`); 1–2 links → `light_mode` full `[TARGETBODY, TARGETBODYCOM, FIXED, TRACK, TRACKCOM]` (default `TARGETBODY`), 3+ links or nothing selected → `[FIXED, TRACK, TRACKCOM]` (default `FIXED`).
> - 1 link + `TARGETBODY`/`TARGETBODYCOM` → single world light at the 3D cursor targeting that link; 2 links + targeting mode → single light, first selected is position, second is target; otherwise one light per link as its child. Nothing selected → world light at the 3D cursor.
> - MCP: `forge_create_light`.

#### `forge.create_camera(camera_type='PERSPECTIVE', camera_mode)`

> - Requires: selection all `LINK`, or nothing selected.
> - `camera_type` in `[PERSPECTIVE, ORTHOGRAPHIC]`. Dynamic `camera_mode`: 1–2 links selected → full `[TARGETBODY, TARGETBODYCOM, FIXED, TRACK, TRACKCOM]` (default `TARGETBODY`); nothing or 3+ links selected → `[FIXED, TRACK, TRACKCOM]` (default `FIXED`).
> - 1 link + targeting mode → single world camera at the 3D cursor targeting that link; 2 links + targeting mode → single camera, first selected is position, second is target; otherwise one camera per link as its child. Nothing selected → world camera at the 3D cursor.
> - MCP: `forge_create_camera`.

#### `forge.create_frame()`

> - Requires: selection all in `[LINK, REPLICATE, FRAME]`, or nothing selected.
> - One `frame` per selected object as its child; nothing selected → `World` root at the 3D cursor.
> - Shift+Click in the UI reverses parenting (selected objects become children of the new frame) — `reverse_parent` is a plain class attribute, not an operator parameter; scripts use `forge_define_parent` instead.
> - MCP: `forge_create_frame`.

#### `forge.create_replicate(count=0, sep='', offset=(0, 0, 0), euler=(0, 0, 0))`

> - Requires: selection non-empty and all in `[CAMERA, LIGHT, VISUAL, COLLIDER, SITE, LINK, FRAME, ATTACH, REPLICATE]`.
> - Creates a **single** `replicate` object with the selection as its sources; copies differ by `offset` / `euler` and are named with `sep`.
> - Moves the sources (with their subtrees) into the replicate's own collection, created viewport-hidden. Blender cannot select objects there, so a later operator over them selects nothing and fails its `poll` (`context is incorrect`).
> - MCP: `forge_create_replicate`.

#### `forge.create_inertial(inertial_model_type='VISUAL', check_mesh_valid=False)`

> - Requires: selection all `LINK` (links without children are skipped).
> - Collects children of the selected type (`VISUAL` or `COLLIDER`), recursively through `FRAME` descendants, without entering child `LINK` hierarchies; needs at least one matching geometry object.
> - Mesh validation runs only when `check_mesh_valid=True`. A failed check skips the Link. Primitive shapes use analytic mass and inertia; `MESH` geometry requires TetGen. A successful calculation creates a new `INERTIAL` child without replacing existing inertials.
> - MCP: `forge_create_inertial` uses the defaults above and accepts only `select`. For the other calculation options, use the documented operator parameters through `forge_execute`.

#### `forge.create_material(category, material, use_existing=True)`

> - Requires: selection non-empty and all in `[VISUAL, HFIELD, PLANE]` (materials can be assigned to visual, height-field and plane geometry).
> - `category` / `material` are exact bundled Forge PBR library names; `use_existing=True` assigns an existing same-named datablock as-is, `False` always rebuilds (Blender suffixes the taken name).
> - Assignment uses the first object-level material slot, creating it when empty; the operator does not write primitive geometry-node material sockets.
> - MCP: `forge_create_material`.

#### `forge.assign_material(material)`

> - Requires: selection non-empty and all in `[VISUAL, HFIELD, PLANE]`.
> - `material` is the exact name of an existing Blender material, including any Blender suffix.
> - Reuses its nodes and settings as-is, assigning the first object-level material slot on each selected object. Does not create or copy a material; other slots and unselected object assignments are preserved.
> - MCP: call through `forge_execute` after reading the modify skill.

## Definition operators

#### `forge.define_model_type(Model_Type)`

> - Requires: selection all `UNDEFINED` (plain Blender objects). Available `Model_Type` from the Blender object type: `EMPTY` → `LINK`; `MESH` → `VISUAL` or `COLLIDER`; `LIGHT` → `LIGHT`; `CAMERA` → `CAMERA`.
> - Side effects: `VISUAL` sets geometry type `MESH`, group `2`, `contype`/`conaffinity` `0`, prefix `GEO_`; `COLLIDER` sets type `MESH`, group `3`, prefix `COL_`; `LINK` prefix `LNK_`; `LIGHT` maps Blender type (`SUN` → `DIRECTIONAL`, else `SPOT`/`POINT`, `AREA` cancels), mode `FIXED`, prefix `LIT_`; `CAMERA` maps `ORTHO`/`PERSP` (others cancel), mode `FIXED`, prefix `CAM_`. Objects move to the matching type collection (`WORLD` when parentless).
> - MCP: `forge_define_model_type`.

#### `forge.define_geometry_type(geometry_type='MESH', apply_to_all=False)`

> - Requires: selection all `VISUAL`.
> - `geometry_type` in `[BOX, CAPSULE, CYLINDER, SPHERE, MESH]`; size preserved when switching shapes; to `MESH` bakes current geometry and unlocks scale; from `MESH` uses object dimensions as size.
> - `apply_to_all=False` applies to the active object only.
> - MCP: `forge_define_geometry_type`.

#### `forge.define_collider_type(collider_type='SPHERE', apply_to_all=False)`

> - Requires: selection all `COLLIDER`. Behavior as `define_geometry_type` (size preserved, `MESH` bakes).
> - MCP: `forge_define_collider_type`.

#### `forge.define_site_type(site_type='SPHERE', apply_to_all=False)`

> - Requires: selection all `SITE`. `site_type` in `[BOX, CAPSULE, CYLINDER, SPHERE]`; size preserved.
> - MCP: `forge_define_site_type`.

#### `forge.define_joint_type(joint_type='HINGE', apply_to_all=False)`

> - Requires: selection all `JOINT`. `joint_type` in `[FREE, BALL, SLIDE, HINGE]`; updates the joint shape gizmo.
> - MCP: `forge_define_joint_type`.

#### `forge.define_actuator_type(actuator_type='POSITION', apply_to_all=False)`

> - Requires: selection all `ACTUATOR`. `actuator_type` in `[GENERAL, MOTOR, POSITION, VELOCITY, ADHESION]`.
> - MCP: `forge_define_actuator_type`.

#### `forge.define_parent()`

> - Requires: an active object plus selection. Active `VISUAL` is refused — a `collider` under a `visual` is not exported. Active in `[LINK, FRAME, REPLICATE]` → parents selected objects of type `[LINK, VISUAL, COLLIDER, JOINT, SITE, LIGHT, CAMERA, FRAME, REPLICATE, ATTACH]` to it; children of a selected `VISUAL` are lifted to the same parent first. Active object itself is skipped.
> - World position of children is preserved.
> - Every reparented object moves into the collection of its model type (`visual` → `Visual`, `collider` → `Collider`, …), so a root object in `World` leaves it.
> - Ordered selection matters: parent first, children after (MCP `forge_define_parent`).
> - MCP: `forge_define_parent`.

## Utility operators

#### `forge.batch_rename(new_name='', numerate='###')`

> - Requires: any selection. Renames each selected object to `{new_name}_{index}` with zero padding of `numerate` length, index from 0 in Blender's selected-object iteration order; this is not the recorded click order.
> - MCP: `forge_batch_rename`.

#### `forge.set_instance_idname()`

> - Requires: selection all in `[LINK, FRAME, VISUAL]`. Applies only to selected `LINK` objects (Frame and Visual objects are skipped): writes `obj["INSTANCE_IDNAME"] = Forge_Props.instance_body` (an object reference that survives renames), or removes the property when no instance body is chosen. Reports how many links were marked / cleared. Links already marked `INSTANCE_LINK` are refused (warning).
> - The instance source is a link marked with `INSTANCE_LINK` (via `forge.mark_instance_link`); `Forge_Props.instance_body` (panel *Instance* field) only accepts marked links. A marked instance link never appears as a `<body>` in the multibody tree; a **referenced** one feeds the `<asset>` section with its subtree's meshes / materials, while an **unreferenced** one exports nothing at all (warned).
> - Export semantics: the instance link's children are written into every link marked with `INSTANCE_IDNAME = <instance link name>`. Each such link keeps its own body element (name / pos / quat / link props) but its children are replaced by the copy, with every element name prefixed `"<instance>_<name>"` (camera / light `target` refs inside the subtree renamed too). Instance subtrees gather no assets of their own, and global sections (`actuator` / `sensor` / `tendon` / `equality` / `contact`) are not duplicated per instance — don't reference instance-link-internal elements from them. A marked link nested inside a template subtree is never copied as a `<body>` either — its content still only exports through the placeholders referencing it.
> - MCP: `forge_set_instance_idname`.

#### `forge.select_by_tag()`

> - Requires: object mode. **Adds** every scene object whose name contains the main scene's `Forge_Props.select_tag` to the current selection — it does not clear first, so pre-selected objects stay selected.
> - An empty `select_tag` matches every object name (`""` is contained in any string) and therefore selects the whole scene.
> - MCP: `forge_select_by_tag`.

#### `forge.select_by_model_type()`

> - Requires: Object Mode. Adds selectable objects whose Forge type matches the main scene's `Forge_Props.select_model_type` to the current selection; existing selection is preserved.
> - No dedicated MCP wrapper. Set `Forge_Props.select_model_type` and invoke the documented operator through `forge_execute` when needed.

#### `forge.select_hulls()`

> - Requires: object mode. Selects every scene object whose **full name matches** the addon preference `coacd_name_template` interpreted as a pattern (`?` → any name segment, `#` → digits) — the same template CoACD uses to name hulls.
> - MCP: `forge_select_hulls`.

#### `forge.scale_gizmo_size()`

> - No poll. Sets gizmo display of selected objects — or all objects in the blend file when nothing is selected — using the main scene's `Forge_Props.gizmo_scale` relative to each object's stored base size: modifier `Socket_0` for `JOINT` / `CONTACT` / `EQUALITY` / `TENDON` / `ACTUATOR` / `SENSOR`, `empty_display_size` for `LINK` / `FRAME` / `ATTACH`. `INERTIAL` display is determined by mass and inertia and is excluded.
> - MCP: `forge_scale_gizmo_size`.

#### `forge.mark_root_link()`

> - Requires: selection all in `[LINK, FRAME, REPLICATE]`. Parentless objects are marked with `obj["Root Link"] = True`; objects that have a parent are first unparented while preserving world transform, then marked.
> - MCP: `forge_mark_root_link`.

#### `forge.mark_instance_link()`

> - Requires: selection all `LINK`. Toggles `obj["INSTANCE_LINK"] = True` per selected link (run again to unmark); reports how many links were marked / unmarked.
> - A marked instance link never exports as a `<body>`; its children are written under every `INSTANCE_IDNAME` link. A **referenced** marked link feeds the `<asset>` section with its subtree's meshes / materials; an **unreferenced** one exports nothing at all (warned). `Forge_Props.instance_body`'s picker only lists marked links.
> - MCP: `forge_mark_instance_link`.

#### `forge.mesh_check()`

> - Requires: selection all `VISUAL`. Reports self- and pairwise intersections (boundary-only contact and separating coplanar faces are valid — details in the `modify` skill). Run before `create_inertial` / export.
> - MCP: `forge_mesh_check`.

#### `forge.add_tendon_target_item()`

> - Requires: the active object is `TENDON`. Appends an item to `obj.Forge_Tendon.targets.items` and sets `active_index` to the new last entry (fill `target` / `coef` afterwards via property access).
> - No MCP wrapper — prefer `forge_set_tendon_targets(name, [...])` which replaces the whole ordered path.

#### `forge.remove_tendon_target_item()`

> - Requires: the active object is `TENDON`. Removes the item at `Forge_Tendon.targets.active_index` and clamps the index.
> - No MCP wrapper — prefer `forge_set_tendon_targets`.

## File and IO operators

#### `forge.import_mjcf(filepath)`

> - **Modal** (`BaseProgressOperator`). `filepath` argument wins, else the main scene's `Forge_Props.import_file_path`; missing file cancels.
> - **Destructive**: clears scene objects, collections, non-main scenes and orphaned data before rebuilding the model (stage order: compiler → option → statistic → visual → asset → worldbody → contact → equality → tendon → actuator → sensor → replicates).
> - Requires the `Forge Library` asset library (auto-recreated from the addon's `lib/assets` when missing).
> - MCP: `forge_import_mjcf` (sets `import_file_path` / `import_material`, invokes, waits for `is_importing` to clear).

#### `forge.export_mjcf()`

> - **Modal**. No filepath parameter — always writes the main scene's `Forge_Props.export_path` (resolved against the blend file when `rel_path` is set).
> - Stage order: gather assets → export images / hfields / visual meshes / collider meshes → XML sections (include, compiler, option, statistic, visual, asset, world, contact, equality, tendon, actuator, sensor) → write file. `update_forge_only` skips asset file writes; `use_glb` switches visual mesh format.
> - Empty mesh visuals/colliders (zero vertices or triangles) are skipped, so no mesh asset or `<geom mesh="...">` reference is emitted.
> - A World environment image connected through an Environment Texture is exported as `<texture type="envhdr">` and restored to the main scene World on import.
> - MCP: `forge_export_mjcf` (sets `export_path` + `rel_path=False` and the two flags, refuses existing destinations without `overwrite=True`, waits for `is_exporting` to clear).

#### `forge.create_attach()`

> - **Modal**. Requires: exactly 1 selected `[LINK, REPLICATE, FRAME]` object (becomes the attach parent), or nothing selected.
> - Reads the main scene's `Forge_Temp_Props`: `tmp_file`, `tmp_model`, `tmp_prefix`, `tmp_link` — all must be non-empty (file must exist). Imports the external model into its own scene / collection, then creates the `attach` reference.
> - A file already `include`d in the scene yields an empty attach task list and reports `Attach fail: list index out of range`; attach and include take separate files.
> - MCP: `forge_create_attach` (sets `Forge_Temp_Props` directly from the `file` / `model` / `prefix` / `link` arguments and waits).

#### `forge.create_include()`

> - **Modal**. Requires: nothing selected. Reads `Forge_Temp_Props.tmp_include`; imports the file's collections into the scene but only an `<include>` tag is written on export (file content never exported).
> - MCP: `forge_create_include` (sets `tmp_include` directly).

#### `forge.temp_file(filepath)`

> - UI file browser (`*.xml`) feeding `create_attach`. On execute stores `Forge_Temp_Props.tmp_file`, derives `tmp_model` (basename) and `tmp_prefix` (`model + "_"`), resets `tmp_link` to `"None"`.
> - Agent path: assign `Forge_Temp_Props` directly (what `forge_create_attach` does); drivable via `EXEC_DEFAULT` with `filepath=...`.

#### `forge.temp_link(tmp_link)`

> - UI enum dialog listing the `<body>` links parsed from `Forge_Temp_Props.tmp_file` (`get_link_names` identifiers); stores the choice in `tmp_link`.
> - Agent path: assign `Forge_Temp_Props.tmp_link` directly with the link identifier.

#### `forge.temp_include(filepath)`

> - UI file browser (`*.xml`) feeding `create_include`; stores `Forge_Temp_Props.tmp_include`.
> - Agent path: assign `Forge_Temp_Props.tmp_include` directly.

#### `forge.file_path(filepath)`

> - UI file browser; stores the chosen path in `Forge_Props.import_file_path` (used by `import_mjcf` invoke).
> - Agent path: assign `Forge_Props.import_file_path` directly.

#### `forge.export_path(filepath)`

> - UI file browser; appends `.xml` when missing and stores `Forge_Props.export_path`; sets `rel_path=True` when the path lies under the blend file's directory (stores a blend-relative path), else `rel_path=False`.
> - Agent path: assign `Forge_Props.export_path` (+ `rel_path`) directly.

## CoACD

#### `forge.coacds(threshold=0.05, max_convex_hull=-1, preprocess_mode='Auto', preprocess_resolution=50, resolution=2000, mcts_nodes=20, mcts_iterations=100, mcts_max_depth=3, pca=False, merge=True, decimate=False, max_ch_vertex=128, extrude=False, extrude_margin=0.01, apx_mode='CH', seed=0)`

> - Requires: object mode with one or more selected `VISUAL` objects; needs the `coacd` python package (install via addon preferences pip).
> - Decomposes triangle faces from the evaluated mesh without applying a Triangulate modifier to or deleting the source object; processing can take minutes.
> - Creates one mesh object per convex hull in the source object's first collection, named from the add-on preference `coacd_name_template` (`?` → source object name, `#` → 1-based zero-padded hull index). Each hull has `Forge_Model_Type='COLLIDER'`, geometry type `MESH`, the source's world transform, and the same parent as the source.
> - Key parameters: `threshold` (concavity termination), `max_convex_hull` (only with `merge`), `preprocess_mode` in `[Auto, On, Off]`, sampling / MCTS controls, `decimate` + `max_ch_vertex`, `extrude` + `extrude_margin`, `seed`.
> - MCP: `forge_coacd` (single object by name).

## UI-only popup operators

All 16 open `invoke_props_dialog` windows whose edits happen through the live UI; their `execute` is a no-op for agents. Every value they expose is reachable by direct property assignment — see the parameter reference in the `modify` skill. Never call them from scripts.

- `forge.properties_global` — scene `Forge_GlobalConfig` (`compiler` / `option` / `statistic`).
- `forge.properties_visual` — scene `Forge_VisualConfig` (`<visual>` section groups).
- `forge.properties_link`, `forge.properties_shape`, `forge.properties_shape_site`, `forge.properties_hfield`, `forge.properties_plane`, `forge.properties_joint`, `forge.properties_actuator`, `forge.properties_tendon`, `forge.properties_equality`, `forge.properties_contact`, `forge.properties_sensor`, `forge.properties_light`, `forge.properties_camera`, `forge.properties_replicate` — per-object `Forge_<Type>` property groups.

## Addon infrastructure operators

Not model-authoring; manage the environment and the MCP bridge itself. No MCP wrappers.

- `forge.pip_install(package)` — install / upgrade a python package into Blender's environment (addon preferences dependency rows).
- `forge.ensure_pip()` — bootstrap pip / setuptools / wheel when missing.
- `forge.mcp_server_start` — start the in-Blender TCP bridge the MCP server connects to; refuses in `--background` mode (use `blender --background --command forge_mcp` instead).
- `forge.mcp_server_stop` — stop the bridge and unregister its polling timer.
