# Forge modify

Modify MJCF model elements with Forge tools.

## General rules

- **Specification compliance**: these guides are the authoritative specification of the Forge tool surface — strictly follow the rules, signatures, parameter ranges and workflows documented here. Never read, search or infer behavior from the addon source code (`addon/Forge/**`); source internals are not part of the interface. Runtime inspection through the MCP tools (`forge_object_info`, `forge_scene_config`, ...) is allowed.
- **No undocumented operations**: work only through what these guides document. When a needed operation, parameter or enum value has no documented implementation, do not improvise with raw `bpy` or undocumented APIs — stop and report the gap (what was attempted, what is missing) as feedback.
- **Main scene**: the main scene must be named `Scene`. Forge resolves the active scene through `scene.Main_Scene` (defaults to `"Scene"`), e.g. `bpy.data.scenes[scene.Main_Scene].Forge_Props`. Modify the model in the scene named `Scene` only — do not rename or delete it, and do not modify objects in another scene.

- **Collider selection**: prefer shape colliders (`BOX`, `CAPSULE`, `CYLINDER`, `SPHERE`). Consider a `MESH` collider only when shape colliders cannot meet the required collision geometry or accuracy. A mesh visual alone is not a reason to choose a mesh collider.

### MCP tool workflow

- Prefer dedicated MCP tools: inspect with `forge_blendfile_summary`, `forge_scene_info`, `forge_object_info` and `forge_measure`; change model/type/parent with `forge_define_*`; edit values with `forge_set_transform`, `forge_set_shape_size`, `forge_set_property` and `forge_rename`; validate with `forge_mesh_check`. Use `forge_execute` only for a Forge property or collection edit that no dedicated tool can express. Its skill check applies to explicit `bpy.ops.forge.*` calls and direct `Forge_*` property writes; ordinary Blender modelling edits are allowed even when the target object has a Forge model type.
- **Skill gate scope**: generic Blender deletion/removal operations remain available without a Forge guide. Use the dedicated Forge operations for Forge hierarchy changes, especially `forge_define_parent`; direct `obj.parent` assignment is only the documented detach escape hatch below.
- Every `bpy.ops.forge.*` operator (signature, defaults, `poll`, MCP wrapper) is inventoried in the `operators` skill — `forge_skill(name="operators", section="<operator name>")` for a single entry.
- Follow **inspect → edit → verify → validate → save/export**. Read object types, parents, locks and current property values before mutation. Re-read every changed object, remeasure world-space bounds, mesh-check the relevant visuals, and use `forge_screenshot` when visual confirmation adds value.
- Every MCP `select=[...]` argument is ordered. The first name becomes the active object and list indices become Forge `selected_order` values. For `forge_define_parent`, put the intended parent first and the children after it; for target/reference operations preserve the order documented in the create rules.
- `forge_object_info` returns the whole `Forge_<Type>` group, modifier sockets and transforms — but **not** Blender-native `obj.data`. Read light / camera data (`energy`, `angle`, `clip_start`, ...) with `forge_execute`; write it with `forge_set_property` `data:`-prefixed keys.
- `forge_delete` recursively removes all descendants of every named root. Inspect `children` first and name only the intended roots. Inspect output destinations before save/export and do not overwrite files unless requested.

## Modify tips

- **Joint axis**: the exported mjcf `axis` is the joint object's local +Z expressed in parent space (`obj.matrix_local.to_3x3().transposed()[2]`). Default creation gives +Z along parent +Z; rotate the joint object's euler so its Z aligns with the desired world axis (e.g. `rotation_euler = (-90°, 0, 0)` makes the axis point along parent +Y).
- **Local vs world coordinates**: `location` and shape sizes are in the parent's local space. When a link sits below / away from the world origin, convert: `local = world - parent_world` (for unrotated parents). Verify placements with evaluated world bounding boxes, not socket values.
- **Shape size sockets** are arrays for BOX (`Socket_0` = full xyz dimensions, written as a 3-tuple) and scalars for SPHERE (visual `Socket_0` / collider `Socket_3` = radius); assigning a scalar to an array socket raises `TypeError`. On Blender 5.2+ read/write a socket as `mod.properties.inputs.Socket_N.value`; on Blender 4.x–5.1 use `mod["Socket_N"]`. Prefer `forge_set_shape_size`, which handles both. Modifier names capitalize the shape (`Geometry_Box`, `Collider_Sphere`). `forge_set_shape_size` covers all four shapes: BOX takes the full (x, y, z) tuple, SPHERE a radius, CAPSULE / CYLINDER a `(radius, height)` pair — height is the full length of the straight section (capsule overall length = height + 2·radius); height socket is visual `Socket_2`, collider / site `Socket_4`.
- **mesh_check scope**: the check reports pairwise intersections between *all* selected objects. Boundary-only point-point, point-edge, point-face, edge-edge, and edge-face contact is allowed when incident geometry does not cross the other mesh. A coplanar shared face is also allowed when its plane separates the two complete objects (for example aligned boxes placed flush), independent of face winding. Non-separating coplanar area overlap and actual face crossings still count as intersections. Scope selection per-link to avoid reporting unrelated geometry.
- **Name collisions**: Blender silently suffixes duplicates (`.001`) — including against orphaned datablocks left out of the scene after failed operations. Renaming to a "free-looking" name can no-op; check the result or purge orphans first.
- **Locked transforms**: Forge locks scale on most model objects (and location/rotation on some); scripts must respect `lock_location` / `lock_rotation` / `lock_scale` instead of assigning.
- **`forge_set_property` value types are not what the names suggest** — always read the returned `skipped` map. A write that lands in `skipped` did **not** happen, and the tool still returns success. Two traps seen in practice: several `Forge_*` flags are **uppercase string enums, not bools** (actuator `ctrllimited` takes `'FALSE'` / `'TRUE'` / `'AUTO'` — passing `true` or `"true"` is skipped), and array properties have **fixed arity** (actuator `gear` needs 6 elements, not 1). The `skipped` value carries the underlying `bpy_struct` message, which names the expected type or arity.

## Modify rules

### Modify order:
 1. Select target object(s).
 2. Change the type with the appropriate documented `bpy.ops.forge.define_*` operator when needed.
 3. Edit parameters supported by the model type through `obj.Forge_<Type>.<property>` directly; popup dialogs are UI-only.
 4. Adjust `location`, `rotation`, and `scale` as needed, respecting locked axes.

### Relationship retargeting:

Post-creation relationship changes go through `forge_set_property` Object-target properties — pass the target object's **name** as a string, `null` clears:

- `actuator.target` — any `link` / `joint` / `tendon` object; `target_type` re-detects from the new target.
- `equality.target1` / `target2` — `JOINT` equality uses `target1` and an optional `target2`; when present, both are exported as joint references.
- `contact.target1` / `target2`.
- `sensor.target` and `sensor.ref` (frame sensor types and Contact filters). For a Contact subtree sensor, both must reference existing `link` objects: `target` exports as `subtree1`, `ref` as `subtree2`. Set both explicitly when creating or retargeting; do not clear either endpoint. Verify `use_subtree=True`, `target_type="SUBTREE"` and both pointers after editing, and both named attributes in the exported `<contact>` sensor.
- `light.target` / `camera.target` — only meaningful while `mode` is `TARGETBODY` / `TARGETBODYCOM`.
- Tendon joint path: `forge_set_tendon_targets` (ordered replace). `attach` reference fields (`model` / `file` / `link` / `prefix`) are plain strings, not pointers.
- **Detach has no dedicated implementation**: `forge_define_parent` only assigns a parent; no operator or tool clears one. The only path is the `forge_execute` escape hatch (`obj.parent = None`; collection membership is not updated) — otherwise report the gap.

### Model modify rules:
#### `model type`:

`bpy.ops.forge.define_model_type(Model_Type='<type>')` only for selected `UNDEFINED` type object(s):

> - Available `Model_Type` decided by selected object type:
>
>     - `EMPTY` object: `LINK`
>     - `MESH` object: `VISUAL` or `COLLIDER`
>     - `LIGHT` object: `LIGHT`
>     - `CAMERA` object: `CAMERA`
>
> - `VISUAL`: set geometry type `MESH`, group `2`, `contype`/`conaffinity` `0`, rename with prefix `GEO_`.
> - `COLLIDER`: set geometry type `MESH`, group `3`, rename with prefix `COL_`.
> - `LINK`: rename with prefix `LNK_`.
> - `LIGHT`: set light type by Blender light type (`SUN` → `DIRECTIONAL`, else `SPOT`/`POINT`), mode `FIXED`, rename with prefix `LIT_`; `AREA` light not support.
> - `CAMERA`: set camera type by Blender camera type (`ORTHO` → `ORTHOGRAPHIC`, `PERSP` → `PERSPECTIVE`), mode `FIXED`, rename with prefix `CAM_`; only `PERSP`/`ORTHO` camera support.
> - Object with parent move to corresponding type collection, without parent move to `WORLD` collection.

#### `geometry type` (visual):

`bpy.ops.forge.define_geometry_type(geometry_type='<type>', apply_to_all=False)` based on selected `visual` object(s):

> - parameter `geometry_type` in `[BOX, CAPSULE, CYLINDER, SPHERE, MESH, SDF]`
> - `apply_to_all`: default `False` only apply to active object, `True` apply to all selected.
> - Size is preserved as the bounding-box equivalent; exact shape parameters may differ across a round-trip
>   through another shape (e.g. CYLINDER r=0.05 -> SPHERE -> CYLINDER yields r=0.1).
> - Switch to `MESH` / `SDF`: bake primitive geometry into mesh, scale unlock. Switching between MESH and SDF preserves the mesh and modifiers. SDF exports with a mesh asset reference.
> - Switch from `MESH` / `SDF`: use object dimensions as size.

#### `collider type`:

`bpy.ops.forge.define_collider_type(collider_type='<type>', apply_to_all=False)` based on selected `collider` object(s):

> - parameter `collider_type` in `[BOX, CAPSULE, CYLINDER, SPHERE, MESH, SDF]`
> - Size is preserved as the bounding-box equivalent; exact shape parameters may differ across a round-trip
>   through another shape (e.g. CYLINDER r=0.05 -> SPHERE -> CYLINDER yields r=0.1).
> - Switch to `MESH` / `SDF`: bake current primitive or convex modifier into mesh, scale unlock. Existing mesh geometry is preserved.
> - Switch from `MESH` / `SDF`: use object dimensions as size.

#### `site type`:

`bpy.ops.forge.define_site_type(site_type='<type>', apply_to_all=False)` based on selected `site` object(s):

> - parameter `site_type` in `[BOX, CAPSULE, CYLINDER, SPHERE]`
> - Size is preserved as the bounding-box equivalent; exact shape parameters may differ across a round-trip
>   through another shape.

#### `joint type`:

`bpy.ops.forge.define_joint_type(joint_type='<type>', apply_to_all=False)` based on selected `joint` object(s):

> - parameter `joint_type` in `[FREE, BALL, SLIDE, HINGE]`
> - Update joint shape gizmo when type changed.

#### `actuator type`:

`bpy.ops.forge.define_actuator_type(actuator_type='<type>', apply_to_all=False)` based on selected `actuator` object(s):

> - parameter `actuator_type` in `[GENERAL, MOTOR, POSITION, VELOCITY, ADHESION]`

#### `parent`:

`bpy.ops.forge.define_parent()` change parent of selected object(s) to active object:

> - Active object is `link` | `frame` | `replicate`: parent selected object(s) in `[LINK, VISUAL, COLLIDER, JOINT, SITE, LIGHT, CAMERA, FRAME, REPLICATE, ATTACH]` to it.
> - Active object is `visual`: refused (poll fails) — a `collider` under a `visual` is not exported; parent the `collider` to the `link` instead.
> - Children of a selected `visual` object (for example colliders still bound to it) are reparented to the active object first, so a legacy `collider`-under-`visual` nesting is repaired rather than recreated.
> - World position of child preserved after reparent.

#### `root link`:

`bpy.ops.forge.mark_root_link()` based on selected `link` | `frame` | `replicate` object(s):

> - Parentless objects are marked directly.
> - Objects with a parent are unparented while preserving their world transform, then marked.
> - Set `obj["Root Link"] = True`.

#### `mesh check`:

`bpy.ops.forge.mesh_check()` based on selected `visual` object(s):

> - Check mesh validation, report error info.
> - Use before compute inertial / export.

#### `gizmo size`:

`bpy.ops.forge.scale_gizmo_size()` change gizmo display size of selected object(s), or all objects when none selected:

> - Scale from scene `Forge_Props.gizmo_scale`.

### Utilities:

#### `batch rename`:

`bpy.ops.forge.batch_rename(new_name='', numerate='###')` based on selected object(s):

> - Rename selected objects to `{new_name}_{index}` with zero padding by `numerate` length, index start from 0.

#### `instance idname`:

`bpy.ops.forge.set_instance_idname()` based on selected `link` object(s):

> - Mark selected links as instances of scene `Forge_Props.instance_body` (`INSTANCE_IDNAME` custom property); run again with no instance body to clear. Links already marked `INSTANCE_LINK` are refused (warning).
> - Mark the instance source first with `bpy.ops.forge.mark_instance_link()` (`INSTANCE_LINK` custom property, toggle). A marked link never exports as a `<body>`; referenced ones provide assets for their copies, unreferenced ones export nothing at all (warned); `Forge_Props.instance_body` only lists marked links. The instance link's children are written into every `INSTANCE_IDNAME` link, element names prefixed `<instance>_<name>`; global sections (`actuator` / `sensor` / …) are not duplicated per instance.

#### `select by tag`:

`bpy.ops.forge.select_by_tag()` only in object mode:

> - Select objects whose name contains scene `Forge_Props.select_tag`.

#### `select hulls`:

`bpy.ops.forge.select_hulls()` only in object mode:

> - Select convex hull objects by name template from addon preferences (`coacd_name_template`).

### Parameter modify rules:

Each model type has its own parameter group `obj.Forge_<Type>` on the object — always change parameters by direct property assignment. `bpy.ops.forge.properties_*` popup dialogs are UI-only and ineffective for agents; never use them.

#### Direct property access:

Parameters grouped by model type, then by sub-type (set property `type` / `mode` directly to switch sub-type, same as `bpy.ops.forge.define_*`). Shape / gizmo sizes live in geometry-node modifier sockets `obj.modifiers[...]` — readable / writable as `mod.properties.inputs.Socket_N.value` on Blender 5.2+ and `mod["Socket_N"]` on Blender 4.x–5.1. Both surfaces are Forge edits, so `forge_set_property` and `forge_set_shape_size` ask for this guide.

- `link`: `obj.Forge_Link` — `mocap`, `gravcomp`
- `visual` / `collider` / `hfield` / `plane` (all mjcf `geom`): `obj.Forge_Geometry` — `group`, `condim`, `contype`, `conaffinity`, `priority`, `friction`, `mass`, `density`, `solmix`, `solref`, `solimp`, `margin`, `gap` (hfield / plane UI hides `friction` / `mass` / `density`, but they are exported when non-default)
    - shape size in geometry modifier `obj.modifiers[...]`:
        - `visual`: `BOX` size `Socket_0`; `SPHERE` size `Socket_0`; `CAPSULE` / `CYLINDER` size `Socket_0` + height `Socket_2`; `MESH` no size sockets. Material is the first object-level material slot, assigned by `forge_create_material`.
        - `collider`: `BOX` / `SPHERE` size `Socket_3`; `CAPSULE` / `CYLINDER` size `Socket_3` + height `Socket_4`; `MESH` no size sockets
        - `hfield`: `nrow` `Socket_0`, `ncol` `Socket_2`, `use_elevation` `Socket_3`, `radius_x` `Socket_4`, `radius_y` `Socket_5`, `elevation_z` `Socket_6`, `base_z` `Socket_7`, `height_map` `Socket_8`, `use_height_map` `Socket_10`, `offset` `Socket_11`; material is the first object-level material slot.
        - `plane`: `half_size_x` `Socket_2`, `half_size_y` `Socket_3`, `infinite` `Socket_4`; material is the first object-level material slot.
- `site`: `obj.Forge_Geometry` — `group`; shape size in site modifier: `BOX` / `SPHERE` size `Socket_3`; `CAPSULE` / `CYLINDER` size `Socket_3` + height `Socket_4`
- `joint`: `obj.Forge_Joint` per type:
    - `range` on `BALL` / `HINGE` is stored in **radians**. Export converts it to degrees only when `Forge_GlobalConfig.g_compiler.angle == "DEGREE"`; with `"RADIAN"` it is written unchanged. For a HINGE limit of ±90°, set `range = [-pi/2, pi/2]`, not `[-90, 90]`. `forge_object_info` returns the stored radians.
    - `ref` and `springref` on `HINGE` follow the same rule, and are **scalars**: a 90° reference is `ref = pi/2`, exported as `ref="90"`. A `SLIDE`'s `range`, `ref` and `springref` are linear values (meters) and are written unchanged whatever the compiler unit; `actuatorfrcrange` is a force range, not an angle. A `BALL` has no `ref` or `springref`: MJCF's ball joint does not carry them, so they are not exported at all.
    - `FREE`: `stiffness`, `armature`, `damping`, `frictionloss`
    - `BALL`: `springdamper`, `solreflimit`, `solimplimit`, `solreffriction`, `solimpfriction`, `stiffness`, `range`, `limited`, `margin`, `armature`, `damping`, `frictionloss`
    - `SLIDE` / `HINGE`: BALL params + `ref`, `springref`, `actuatorfrcrange`, `actuatorfrclimited`
    - gizmo modifier: `display_size` `Socket_0`, `range` display `Socket_3`
- `actuator`: `obj.Forge_Actuator` — `type`, `target`, `target_type` (auto-detected from `target`) always; per type:
    - `GENERAL` / `MOTOR`: `ctrllimited`, `ctrlrange`, `forcelimited`, `forcerange`, `gear`, `gaintype`, `biastype`, `dynprm`, `gainprm`, `biasprm`
    - `POSITION`: same as `GENERAL` + `kp`, `kv`, `inheritrange`
    - `VELOCITY`: same as `GENERAL` + `kv`
    - `ADHESION`: `ctrllimited`, `ctrlrange`, `forcelimited`, `forcerange`, `gain` (no `gear` / `dynprm` / `gainprm` / `biasprm`)
- `tendon`: `obj.Forge_Tendon` — `type`, `targets` (ordered target path; every `targets.items[]` has `target` and exported `coef`, default `0.5`; replace safely with `forge_set_tendon_targets`, or edit with `forge.add_tendon_target_item` / `forge.remove_tendon_target_item`), `range`, `limited`, `solreflimit`, `solimplimit`, `springlength`, `stiffness`, `damping`
- `equality`: `obj.Forge_Equality` — `active`, `type`, `target1`, `target2`, `target_type`; `target2` is optional, including for `JOINT` equality. Type-specific parameters:
    - `CONNECT`: `anchor`, `solref`, `solimp`
    - `WELD`: `anchor`, `solref`, `solimp`, `relpose`
    - `JOINT`: `solref`, `solimp`, `polycoef`
- `contact`: `obj.Forge_Contact` — `type`, `target1`, `target2` always; per type:
    - `EXCLUDE`: no extra params
    - `PAIR`: `condim`, `friction`, `solref`, `solreffriction`, `margin`, `gap`
- `sensor`: `obj.Forge_Sensor` — `type`, `target_type`, `target`, `noise`, `cutoff` always; per type:
    - `Framepos` / `Framequat` / `Framexaxis` / `Frameyaxis` / `Framezaxis` / `Framelinvel` / `Frameangvel`: `ref_type`, `ref`, `use_xbody`. `ref_type` is independent of `target_type` and exports as MJCF `reftype`; use the actual reference object's kind — MJCF `reftype` accepts only `BODY`, `XBODY`, `GEOM`, `SITE`, `CAMERA`, so a `JOINT` can never be a reference (`create_sensor` refuses a selection that pairs a joint with another object).
    - `Contact`: `ref`, `use_subtree`, `num` (auto-computed from `data`), `data`, `reduce`. With `use_subtree=True`, explicitly set both `target` (`subtree1`) and `ref` (`subtree2`) to `link` objects; a missing second root is incomplete under this authoring workflow.
    - `Touch` / `Accelerometer` / `Velocimeter` / `Gyro` / `Jointpos` / `Jointvel` / `Subtreecom` / `Subtreelinvel` / `Subtreeangmom`: no extra params
- `light`: `obj.Forge_Light` — `type`, `mode`; `target` only when `mode` is `TARGETBODY` / `TARGETBODYCOM`; Blender light data `obj.data`: `use_shadow`, `color`, `energy`; `SPOT` / `POINT` additionally `shadow_soft_size`, `cutoff_distance`; `DIRECTIONAL` instead `angle`; `SPOT` additionally `spot_size`, `spot_blend`
- `camera`: `obj.Forge_Camera` — `type`, `mode`; `target` only when `mode` is `TARGETBODY` / `TARGETBODYCOM`; Blender camera data `obj.data`: `PERSPECTIVE` `angle` / `ORTHOGRAPHIC` `ortho_scale`, plus `clip_start`, `clip_end`
- `inertial`: `obj.Forge_Inertial` — `mass`, `diaginertia`, `fullinertia` (position / quaternion from object transform)
- `attach`: `obj.Forge_Attach` — `model`, `file`, `link`, `prefix`
- `replicate`: `obj.Forge_Replicate` — `count`, `sep`, `offset`, `euler` (`count` / `offset` / `euler` mirrored to modifier sockets `Socket_0` / `Socket_2` / `Socket_3`)
- `include`: `obj.Forge_Include` — `file` is the user-facing/reference filename; `rawfile` is the resolved source path used by export. Preserve or update `rawfile` when relocating an include, otherwise export may read the stale source.

#### Scene-level configs — `Forge_GlobalConfig` / `Forge_VisualConfig`:

File workflow, compiler / option / statistic and visual settings live on the **scene**, not on objects. Use `forge_scene_config(group)` to inspect and `forge_set_scene_property(group, values)` to edit. The direct equivalents are `scene.Forge_Props`, `scene.Forge_GlobalConfig.<group>` and `scene.Forge_VisualConfig.<group>` (same rule as object params: popup operators are UI-only). Every global/visual group and sub-group has a `reset()` method; only non-default properties are exported.

- `Forge_Props` (`group="forge_props"`) — workflow/display settings: `scale_factor`, `gizmo_scale`, `rel_path`, `select_tag`, `import_file_path`, `export_path`, `import_material`, `update_forge_only`, `instance_body`, `world_collection`, `use_glb`. Treat `is_importing`, `is_exporting`, `is_attaching`, `is_including`, the modal-operation slot (`modal_operation_active`, `modal_operation_name`, `modal_operation_token`, `modal_operation_deferred`, `modal_operation_status`, `modal_operation_message`, `cancel_requested`), progress values and info strings as operation state; read them but do not manually drive them. Only one modal Forge operation may run at a time — a second one fails while `modal_operation_active` is set.

- `Forge_GlobalConfig` — exported as root-level mjcf sections:
    - `g_compiler` (`<compiler>`): `autolimits`, `angle` in `[RADIAN, DEGREE]`, `eulerseq` in `[XYZ, XZY, YXZ, YZX, ZXY, ZYX]`, `assetdir`, `meshdir`, `texturedir`
    - `g_option` (`<option>`): `timestep`, `iterations`, `tolerance`, `gravity` (float[3]), `o_solref` / `o_solimp` / `o_friction` (float arrays, contact override), `o_margin`
        - `g_option.flag` (`<flag>`): `constraint`, `equality`, `frictionloss`, `limit`, `contact`, `gravity`, `actuation`, `refsafe`, `override` — bool, exported as enable / disable
    - `g_statistic` (`<statistic>`): `extent`, `center` (float[3])
- `Forge_VisualConfig` — exported as the `<visual>` section:
    - `v_global` (`<global>`): `orthographic`, `fovy`, `azimuth`, `elevation` — angle props are **radians** (converted to degrees at export)
    - `v_headlight` (`<headlight>`): `active` (0/1), `ambient` / `diffuse` / `specular` (float[3] color)
    - `v_map` (`<map>`): `fogstart`, `fogend`, `znear`, `zfar`
    - `v_rgba` (`<rgba>`): `fog`, `haze`, `joint`, `bv`, `contactforce` (float[4] color)
    - `v_quality` (`<quality>`): `shadowsize`, `pointshadowsize`
    - `v_tonemapping` (`<tonemapping>`): `method` in `[none, aces]`
    - `v_ssgi` (`<ssgi>`) (Motphys extension): `active`, `resolutionscale`, `raycount`, `stepcount`, `thickness`, `intensity`, `gidenoiseoffset`, `rraycount`, `rdenoiseoffset`

#### Popup dialogs — ineffective for agents:

All `bpy.ops.forge.properties_*` popups (`properties_link`, `properties_shape`, `properties_shape_site`, `properties_hfield`, `properties_plane`, `properties_joint`, `properties_actuator`, `properties_tendon`, `properties_equality`, `properties_contact`, `properties_sensor`, `properties_light`, `properties_camera`, `properties_replicate`, and scene-level `properties_global` / `properties_visual`) open a modal UI window that cannot be driven programmatically — never use them. Every parameter they edit is reachable via the direct property access above.

The file-browser helpers are dialog-driven too — assign their target property directly instead:

- `forge.temp_file` / `forge.temp_link` / `forge.temp_include` → write `scene.Forge_Temp_Props.tmp_file` / `tmp_model` / `tmp_prefix` / `tmp_link` / `tmp_include` directly (this is what `forge_create_attach` / `forge_create_include` do).
- `forge.file_path` / `forge.export_path` → write `scene.Forge_Props.import_file_path` / `export_path` (plus `rel_path`) directly (this is what `forge_import_mjcf` / `forge_export_mjcf` do).
