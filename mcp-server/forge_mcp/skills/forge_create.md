# Forge create

Create mjcf hierarchy relationship use forge tool.

## General rules

- **Specification compliance**: these guides are the authoritative specification of the Forge tool surface — strictly follow the rules, signatures, parameter ranges and workflows documented here. Never read, search or infer behavior from the addon source code (`addon/Forge/**`); source internals are not part of the interface. Runtime inspection through the MCP tools (`forge_object_info`, `forge_scene_config`, ...) is allowed.
- **No undocumented operations**: work only through what these guides document. When a needed operation, parameter or enum value has no documented implementation, do not improvise with raw `bpy` or undocumented APIs — stop and report the gap (what was attempted, what is missing) as feedback.
- **Main scene**: the main scene must be named `Scene`. Forge resolves the active scene through `scene.Main_Scene` (defaults to `"Scene"`), e.g. `bpy.data.scenes[scene.Main_Scene].Forge_Props`. Create the model in the scene named `Scene` only — do not rename or delete it, and do not create objects in another scene.
- **Collider selection**: prefer shape colliders (`BOX`, `CAPSULE`, `CYLINDER`, `SPHERE`). Consider a `MESH` collider only when shape colliders cannot meet the required collision geometry or accuracy. A mesh visual alone is not a reason to choose a mesh collider.

### MCP tool workflow

- Prefer the dedicated MCP tools over raw `bpy`: inspect with `forge_blendfile_summary`, `forge_scene_info`, `forge_object_info` and `forge_measure`; create with `forge_create_*`; change types/parenting with `forge_define_*`; edit with `forge_set_transform`, `forge_set_shape_size`, `forge_set_property` and `forge_rename`; validate with `forge_mesh_check`. Use `forge_execute` only when no dedicated tool represents the operation.
- **Skill gate scope**: generic Blender deletion/removal operations remain available without a Forge guide. Use Forge operations for Forge hierarchy changes, especially `forge_define_parent`; do not assign `obj.parent` directly when establishing a Forge parent relationship.
- Every `bpy.ops.forge.*` operator (signature, defaults, `poll`, MCP wrapper) is inventoried in the `operators` skill — `forge_skill(name="operators", section="<operator name>")` for a single entry.
- Follow **inspect → create/edit → verify → validate → save/export**. Check the main scene and existing names first; after every creation capture the returned `created` names, inspect those exact objects, measure relevant world bounds, run `forge_mesh_check` on related visuals, and use `forge_screenshot` when visual confirmation adds value.
- Every MCP `select=[...]` argument is ordered. The first name becomes Blender's active object and every name receives a `selected_order` matching its list index. This order determines target/reference roles for tendon, equality, sensor, light/camera targeting and parent operations; never rely on `bpy.context.selected_objects` iteration order.
- Before a destructive or file-writing operation, inspect its explicit targets and destination. `forge_delete` recursively removes every descendant of each named root, so inspect `children` first and pass only intended roots.

## Forge mjcf model types

In Forge treat all MJCF tags—including `body`, `inertial`, `geom`, `joint`, `site`, `actuator`, `tendon`, `equality`, `contact`, `sensor`, `light`, `camera`, `frame`, `replicate`, `attach` and `include` are treated as Blender objects, distinguished by the `Forge_Model_Type` attribute of the `Object` type.

Code example:
```python
# register with bpy.types.Object.Forge_Model_Type
bpy.data.objects["name_of_object"].Forge_Model_Type
bpy.context.active_object.Forge_Model_Type
bpy.context.selected_objects[0].Forge_Model_Type
```

Forge model types are:

`UNDEFINED`, `LINK`, `INERTIAL`, `VISUAL`, `COLLIDER`, `HFIELD`, `PLANE`, `JOINT`, `SITE`, `ACTUATOR`, `TENDON`, `EQUALITY`, `CONTACT`, `SENSOR`, `LIGHT`, `CAMERA`, `FRAME`, `REPLICATE`, `ATTACH`, `INCLUDE`.

 - `UNDEFINED` objects are not MJCF elements and are not exported as model elements.
 - `LINK` represents an MJCF `body` in Blender's model hierarchy.
 - `VISUAL`, `COLLIDER`, `HFIELD`, and `PLANE` all represent MJCF `geom` elements but have distinct Forge types and parameters.
 - The remaining types each also have their own unique set of parameters.

## Hierarchy rules

An articulated model starts with a root `link`. An `inertial`, `joint`, or `site` must be a child of a `link`.

`visual`, `collider`, `light`, `camera`, `frame`, `replicate` and `attach` can either be children of a `link`, or exist as root nodes without a parent. A `collider` is never parented under a `visual`: keep it a sibling of its `visual`, under the same `link`. A `collider` under a `visual` is not exported — it vanishes from the MJCF — and `forge_define_parent` refuses to create that nesting.

`hfield` and `plane` exist as root nodes without a parent for now.

In mjcf `actuator`, `tendon`, `equality`, `contact` and `sensor` do not use a hierarchy. In Forge, they will be created as children of their corresponding target model type.

## Create rules

### Creation order:
 1. Create elements with `bpy.ops.forge.create_<type>`, optionally using selected existing model elements as targets.
 2. Adjust `location`, `rotation`, and `scale` as needed, respecting locked axes.
    - Do not change a component when the corresponding `lock_scale`, `lock_rotation`, or `lock_location` flag is `True`.
 3. Edit the parameters supported by the model type as needed.

### File workflow and mesh preprocessing

- `forge_import_mjcf(filepath, import_material=True)` wraps `bpy.ops.forge.import_mjcf` and waits for its modal job. **Import is destructive**: it clears scene objects, collections, non-main scenes and orphaned data before rebuilding, so save first when current work matters. `envhdr` textures are imported into a Blender World environment texture and assigned to the main scene.
- Mesh assets support OBJ, STL and GLB. GLB accepts exactly one Mesh object; non-Mesh elements are discarded, and zero/multiple Mesh objects fail during asset loading. The Mesh node's transform is baked, file-space coordinates/UVs are preserved, and MJCF mesh `scale` is applied afterwards. MJCF defines the materials; embedded GLB materials are discarded. Missing/unsupported mesh files fail during asset loading.
- `forge_export_mjcf(filepath, update_forge_only=False, use_glb=False, overwrite=False)` wraps `bpy.ops.forge.export_mjcf`, waits for completion and reports whether the XML exists. Existing destinations require explicit `overwrite=True`. Export writes a linked World environment image as an MJCF `<texture type="envhdr">`; empty mesh assets (zero vertices or triangles) are skipped and do not produce mesh or geom references.
- `forge_save_blendfile(filepath=None, overwrite=False, save_copy=False)` saves the current blend or a named destination. Existing files—including the current blend path—require explicit `overwrite=True`; `save_copy=True` does not change the active blend path.
- `forge_coacd(name, ...)` wraps `bpy.ops.forge.coacds` for one selected `VISUAL` mesh. It reads triangle faces from the evaluated mesh and creates collider hulls while preserving the source object; generated hull names are returned in `created`. Important parameters: `threshold`, `max_convex_hull`, `preprocess_mode`, sampling/MCTS controls, `merge`, `decimate`/`max_ch_vertex`, `extrude`/`extrude_margin`, and `seed`.

### Create tips:

 - **Joints**: 
    - Joint in forge is Z-UP based and use local +Z in parent space; 
    - Rotate the joint object so Z points along the desired rotation axis. Position the joint at the pivot (e.g. top of a pendulum), not at the body center.
    - First consider the location is at link local space location `[0, 0, 0]`, then consider location by needing.
 - **Inertials**: `create_inertial` defaults to `inertial_model_type='VISUAL'` and `check_mesh_valid=False`. The operator can also use `COLLIDER`; enable `check_mesh_valid=True` for validation before calculation. The dedicated MCP wrapper uses the defaults. Primitive shapes use analytic mass and inertia; mesh geometry requires TetGen. When validation is enabled, boundary-only contact and separating coplanar faces are valid; actual crossings and non-separating coplanar overlap fail. An epsilon gap is not required for valid contact.
 - **Names**: operators use type prefixes for object names. If a name already exists, Blender automatically appends a numeric suffix such as `.001` or `.002` to keep it unique. Read the actual names from the tool's `created` result instead of guessing them, then use `forge_batch_rename` if needed.
 - **Spacing**: geometry sizes given at creation are full dimensions (BOX) / true radius & height (SPHERE / CYLINDER / CAPSULE), exported to mjcf half-extents automatically; all in parent-local meters.
 - **Collider**: create collider for shape geometry is not necessary, if really necessary need set visual shape geometry `obj.Forge_Geometry` props `contype` and `conaffinity` to `0`.

### Model create rules:

#### `link`: 

Create use `bpy.ops.forge.create_link()` optionally based on selected existing object(s):

> - With no selection, the default location is the 3D cursor. Otherwise, placement depends on the selected object's type.
> - Select object in type `[LINK, FRAME, REPLICATE]` location will at local space `[0, 0, 0]`.
> - Select object in type `[VISUAL, COLLIDER]` whose parent is `[LINK, FRAME, REPLICATE]`: new link parented under that parent, location at selected object's local position and rotation zeroed.
> - Select object in type `[VISUAL, COLLIDER]` without parent in `[LINK, FRAME, REPLICATE]`: location at selected object's location, marked as `Root Link`.
> - With no selection, the link is created in the `World` collection as a root candidate. Use `bpy.ops.forge.mark_root_link()` to mark it. Export also discovers parentless roots in the `Link` and `Frame` collections; those roots are not exported twice.

#### `inertial`:

Use `bpy.ops.forge.create_inertial(inertial_model_type='VISUAL', check_mesh_valid=False)` with selected existing `link` objects.

> - Compute mass, center of mass, and principal inertia from children of the chosen type (`VISUAL` or `COLLIDER`), recursively through `FRAME` descendants. Child `LINK` hierarchies are excluded; at least one matching geometry object is required.
> - Geometry validation is optional and off by default. Mesh geometry requires TetGen; primitive shapes do not.
> - Create one new `INERTIAL` child per successful Link calculation. Existing inertials are not replaced.

#### `joint`:

Create use `bpy.ops.forge.create_joint(joint_type='<ENUM>')` based on selected existing `link` object.

> - Parameter `joint_type` in `[FREE, BALL, SLIDE, HINGE]`, default is `HINGE`.

#### `geometry shape`: 
 
- `visual`: use `bpy.ops.forge.create_geometry(geometry_type='<ENUM>', size_box=(1, 1, 1), size_radius=0.5, size_height=1)`

>    - Select object in type `[LINK, FRAME, REPLICATE]`: create one geometry per selected object as child of it, location at local space `[0, 0, 0]`.
>    - Select none objects: create at 3d cursor location.
>    - Parameter `geometry_type` in `[BOX, CAPSULE, CYLINDER, SPHERE]`
>    - Parameter used corresponding to `geometry_type`:
>      - `BOX`: `size_box`
>      - `CAPSULE`: `size_radius`, `size_height`
>      - `CYLINDER`: `size_radius`, `size_height`
>      - `SPHERE`: `size_radius`
>    - Size unit is `meter`

- `collider`: use `bpy.ops.forge.create_collider(collider_type='<ENUM>', create_method='<ENUM>', auto_size=False, use_min_as_height=False, size_box=(1, 1, 1), size_radius=0.5, size_height=1)`

>    Method of `create_method` is `GEOMETRY_TYPE` or `COLLIDER_TYPE`:
> 
>    - `GEOMETRY_TYPE`: only for selected `visual` object(s), will auto detect shape from selected visual, other parameter not need for this method — `collider_type` is ignored, the collider takes the visual's own geometry type.
>      For a mesh visual, prefer `COLLIDER_TYPE` with an explicit shape collider whenever that shape meets the collision requirements; use `GEOMETRY_TYPE` only when its resulting collider type follows the collider selection rule above.
>    - `COLLIDER_TYPE`: will need explicit choose `collider_type`, this is the only method when select none or select `link`/`frame` object.
>    - Parameter `collider_type` in `[BOX, CAPSULE, CYLINDER, SPHERE, MESH, SDF]`
>    - Parameter used corresponding to `collider_type` when `create_method='COLLIDER_TYPE'`:
>      - `BOX`: `size_box` or `auto_size`
>      - `CAPSULE`: `size_radius`, `size_height` or `auto_size`
>      - `CYLINDER`: `size_radius`, `size_height` or `auto_size`
>      - `SPHERE`: `size_radius` or `auto_size`
>      - `MESH`: no other parameter need, only available when `visual` object(s) selected, bake visual geometry to convex mesh collider
>      - `SDF`: only with selected visuals; shares the visual's Mesh Data as a linked duplicate, preserving its parent and transform. Vertex edits affect both objects.
>    `auto_size`: auto-detect the selected `visual` geometry size; off by default. With a `link`/`frame` selection or no selection, explicit `size_*` values (or defaults) are used instead. A `replicate` selection is not accepted by this operator.
>    `use_min_as_height`: `CAPSULE` / `CYLINDER` only, default is off. When on, the height is taken from the selected `visual`'s **smallest** bounding-box axis instead of its largest, and the shape is oriented along that axis. Only takes effect together with `auto_size=True` — with explicit `size_radius`/`size_height` the values are used as given and the flag is ignored. The MCP tool `forge_create_collider` exposes this as `min_is_height`.
>    - Size unit is `meter`

#### `geometry mesh`: 

Create with traditional method. Use `bpy.ops.forge.define_model_type(Model_Type='<ENUM>')` to set object to corresponding model type.

> - `Model_Type` is corresponding to: `VISUAL` for visual object, `COLLIDER` for collider object.

#### `hfield`: 

Create use `bpy.ops.forge.create_height_field()`:

> - Only can create when nothing selected, exist as root node without parent.
> - Default location at 3d cursor location.

#### `plane`: 

Create use `bpy.ops.forge.create_plane()`:

> - Only can create when nothing selected, exist as root node without parent.
> - Default location at 3d cursor location.

#### `site`: 

Create use `bpy.ops.forge.create_site(site_type='<ENUM>', size_box=(0.2, 0.2, 0.2), size_radius=0.1, size_height=0.2)` based on selected existing `link` object(s).

> - Parameter `site_type` in `[BOX, CAPSULE, CYLINDER, SPHERE]`
> - Parameter used corresponding to `site_type`:
>   - `BOX`: `size_box`
>   - `CAPSULE`: `size_radius`, `size_height`
>   - `CYLINDER`: `size_radius`, `size_height`
>   - `SPHERE`: `size_radius`
> - Size unit is `meter`

#### `actuator`: 

Create use `bpy.ops.forge.create_actuator(actuator_type='<ENUM>')` based on selected existing `link` | `joint` | `tendon` object(s).

> - Parameter `actuator_type` in `[GENERAL, MOTOR, POSITION, VELOCITY, ADHESION]`

#### `tendon`: 

Create use `bpy.ops.forge.create_tendon(tendon_type='<ENUM>')` based on selected existing `joint` object(s).

> - Need select at least 2 `joint` objects, create single `tendon` from ordered selection.
> - Only support `joint` subtype in `[SLIDE, HINGE]`.
> - Parameter `tendon_type` currently only `FIXED`.
> - Every ordered target item contains both `target` and exported `coef` (default `0.5`). Use `forge_set_tendon_targets(name, [{"target": "JNT_A", "coef": 0.25}, ...])` to replace the path without raw collection scripting.

#### `equality`: 

Create use `bpy.ops.forge.create_equality(equality_type='<ENUM>')` based on exactly 2 selected existing `link` | `joint` | `site` objects.

> - Selected `joint` objects → `equality_type` is `JOINT`.
> - Selected `link` / `site` objects → `equality_type` is `CONNECT` or `WELD`.

#### `contact`: 

Create use `bpy.ops.forge.create_contact(contact_type='<ENUM>')` based on selected existing `link` | `visual` | `collider` | `plane` | `hfield` objects.

> - Need select at least 2 objects.
> - Selected `link` objects → `contact_type` is `EXCLUDE`.
> - Selected `visual` / `collider` / `plane` / `hfield` objects → `contact_type` is `PAIR`.
> - Create one `contact` for each pair combination of selected objects.

#### `sensor`: 

Create use `bpy.ops.forge.create_sensor(Sensor_Type='<ENUM>', set_ref=False, set_xbody=False, set_subtree=False)` based on selected existing `link` | `joint` | `site` | `visual` | `collider` | `camera` objects.

> - `Sensor_Type` available values are decided by selected target model type:
>     - `joint`: `Jointpos`, `Jointvel`
>     - `site`: `Touch`, `Accelerometer`, `Velocimeter`, `Gyro`, `Framepos`, `Framequat`, `Framexaxis`, `Frameyaxis`, `Framezaxis`, `Framelinvel`, `Frameangvel`, `Contact`
>     - `link`: `Framepos`, `Framequat`, `Framexaxis`, `Frameyaxis`, `Framezaxis`, `Framelinvel`, `Frameangvel`, `Contact`, `Subtreecom`, `Subtreelinvel`, `Subtreeangmom`
>     - `link` with `set_xbody=True`: `Framepos`, `Framequat`, `Framexaxis`, `Frameyaxis`, `Framezaxis`, `Framelinvel`, `Frameangvel`
>     - `link` with `set_subtree=True`: `Contact`
>     - `visual` / `collider`: `Framepos`, `Framequat`, `Framexaxis`, `Frameyaxis`, `Framezaxis`, `Framelinvel`, `Frameangvel`, `Contact`
>     - `camera`: `Framepos`, `Framequat`, `Framexaxis`, `Frameyaxis`, `Framezaxis`, `Framelinvel`, `Frameangvel`
>     - mixed selection in `[LINK, SITE, VISUAL, COLLIDER, CAMERA]` (e.g. 2 objects with different types): `Framepos`, `Framequat`, `Framexaxis`, `Frameyaxis`, `Framezaxis`, `Framelinvel`, `Frameangvel`, `Contact`
> - `set_ref=True`: need select 2 objects, first selected is target, second is reference; `Sensor_Type` range as `Framepos` ~ `Contact`; with `site` target start from `Touch`; with `link` target and `set_xbody=True` end at `Frameangvel`.
> - `set_xbody` / `set_subtree` only for `link` target, mutual exclusive.
> - **Contact subtree sensors must explicitly set both `subtree1` and `subtree2`.** Select exactly two existing `link` objects in order `[subtree1_root, subtree2_root]`, then call `forge_create_sensor(sensor_type="Contact", set_ref=True, set_subtree=True, select=[subtree1_root, subtree2_root])`. The first root becomes `Forge_Sensor.target` (MJCF `subtree1`), the second becomes `Forge_Sensor.ref` (MJCF `subtree2`). Do not create a one-sided subtree sensor or leave `ref` unset. Verify both pointers, `use_subtree=True` and `target_type="SUBTREE"`; after export, verify the `<contact>` sensor contains both attributes with the intended body names.

#### `light`: 

Create use `bpy.ops.forge.create_light(light_type='<ENUM>', light_mode='<ENUM>')` optionally based on selected existing `link` object(s).

> - Select none objects create world light at 3d cursor location, `light_type` in `[DIRECTIONAL, SPOT, POINT]`, `light_mode` in `[FIXED, TRACK, TRACKCOM]`.
> - Select 1 `link`: `light_type` in `[SPOT, POINT]`, `light_mode` in `[TARGETBODY, TARGETBODYCOM, FIXED, TRACK, TRACKCOM]`; when `light_mode` is `[TARGETBODY, TARGETBODYCOM]` create single world light at 3d cursor location targeting the selected `link`, other modes create child light of it.
> - Select 2 `link`s: when `light_mode` is `[TARGETBODY, TARGETBODYCOM]` create single light, first selected is light position, second is target; other modes create one light per selected `link` as child of it.
> - Select 3+ `link`s: `light_mode` restricted to `[FIXED, TRACK, TRACKCOM]`, create one light per selected `link` as child of it.

#### `camera`: 

Create use `bpy.ops.forge.create_camera(camera_type='<ENUM>', camera_mode='<ENUM>')` optionally based on selected existing `link` object(s).

> - `camera_type` in `[PERSPECTIVE, ORTHOGRAPHIC]`.
> - Select none objects create world camera at 3d cursor location, `camera_mode` in `[FIXED, TRACK, TRACKCOM]`.
> - Select 1 `link`: `camera_mode` in `[TARGETBODY, TARGETBODYCOM, FIXED, TRACK, TRACKCOM]`; when `camera_mode` is `[TARGETBODY, TARGETBODYCOM]` create single world camera at 3d cursor location targeting the selected `link`, other modes create child camera of it.
> - Select 2 `link`s: when `camera_mode` is `[TARGETBODY, TARGETBODYCOM]` create single camera, first selected is camera position, second is target; other modes create one camera per selected `link` as child of it.
> - Select 3+ `link`s: `camera_mode` restricted to `[FIXED, TRACK, TRACKCOM]`, create one camera per selected `link` as child of it.

#### `frame`: 

Create use `bpy.ops.forge.create_frame()` optionally based on selected existing `link` | `frame` | `replicate` object(s).

> - Select none objects create at 3d cursor location.
> - Select objects create one frame per selected object as child of it.
> - Shift + Click: reverse parent, selected objects become child of new frame.

#### `replicate`: 

Create use `bpy.ops.forge.create_replicate(count=0, sep='', offset=(0, 0, 0), euler=(0, 0, 0))` based on selected existing `camera` | `light` | `visual` | `collider` | `site` | `link` | `frame` | `attach` | `replicate` objects.

> - Parameter `count`: replicate count.
> - Parameter `sep`: separator string.
> - Parameter `offset`: offset vector between copies.
> - Parameter `euler`: euler rotation between copies.
> - Create single `replicate` object, selected objects as its source.
> - A `replicate` owns its source: the selected objects move into the replicate's own viewport-hidden collection and cannot be selected afterwards. Replicate objects that no later operation still needs to select.

#### `attach`: 

Create use `bpy.ops.forge.create_attach()` optionally based on selected existing `link` | `frame` | `replicate` object.

> - Need select exactly 1 object or none.
> - Choose file in dialog via `Forge_Temp_Props`: `tmp_file`, `tmp_model`, `tmp_prefix`, `tmp_link`.
> - Import the model from external mjcf file into scene, then create attach reference.
> - Requires `Forge Library` asset library (Preferences -> File Paths -> Asset Libraries).
> - The file must not be one already `include`d in the scene — attach and include take separate files. Sharing one reports `Attach fail: list index out of range`.

#### `include`: 

Create use `bpy.ops.forge.create_include()` only when nothing selected.

> - Choose file in dialog via `Forge_Temp_Props.tmp_include`.
> - Only add `include` tag when export, content of the file will not be exported.

### Material creation rules:

Materials are PBR datablocks from the bundled Forge library — not mjcf model objects; they attach to `visual`, `hfield` or `plane` geometry.

#### `material`: 

Use MCP `forge_create_material(category, material, use_existing=True, select=[...])`, which wraps `bpy.ops.forge.create_material(category='<str>', material='<str>')`, based on selected `visual`, `hfield` or `plane` object(s):

> - Requires a non-empty selection where every object is type `VISUAL`, `HFIELD` or `PLANE` — poll fails when nothing is selected or any other type is selected.
> - Parameter `category` in `[Crystal, Human, Liquid, Manmade, Metal, Organic, Plastic]` (~110 materials total).
> - Parameter `material` is the exact library name inside the category — e.g. `Gold`, `Water`, `Skin I`, `Titanium (Anodized)`; names carry parenthesized variants, match them exactly. Enumerate at runtime:
>
> - Builds a Principled BSDF material datablock named after the library entry (base color is linear, set directly), non-render fields (`density`, `viscosity`, ...) stored as custom ID properties.
> - Parameter `use_existing` (default `True`): when an existing datablock with the same name is present it is assigned as-is — user tweaks are preserved, it is NOT rebuilt from the library. Pass `use_existing=False` to always build a fresh datablock from the library (Blender suffixes the taken name `.001`).
> - Assigns to the first object-level material slot of every selected object (creating the slot when empty). This applies equally to mesh and primitive `visual`, `hfield`, and `plane` objects; shape/material modifier sockets are not edited by the operator.

Enumerate categories / names from Python running inside Blender:

```python
import bpy
import importlib

# Resolve both legacy and extension-managed installs without assuming the
# extension repository is named vscode_development or user_default.
module_name = next(
    (name for name in bpy.context.preferences.addons.keys() if name == "Forge" or name.endswith(".Forge")),
    None,
)
if module_name is None:
    raise RuntimeError("Enable the Forge add-on before inspecting its material library")
materials = importlib.import_module(f"{module_name}.core.materials")

materials.get_categories()  # ['Crystal', 'Human', 'Liquid', ...]
materials.get_material_names("Metal")  # ['Aluminum', 'Brass', 'Chromium', ...]
```
