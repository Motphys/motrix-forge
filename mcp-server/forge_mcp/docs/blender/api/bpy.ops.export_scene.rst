Export Scene Operators
======================

.. module:: bpy.ops.export_scene

.. function:: fbx(*, filepath="", check_existing=True, filter_glob="*.fbx", use_selection=False, use_visible=False, use_active_collection=False, collection="", global_scale=1.0, apply_unit_scale=True, apply_scale_options='FBX_SCALE_NONE', use_space_transform=True, bake_space_transform=False, object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LIGHT', 'MESH', 'OTHER'}, use_mesh_modifiers=True, use_mesh_modifiers_render=True, mesh_smooth_type='OFF', colors_type='SRGB', prioritize_active_color=False, use_subsurf=False, use_mesh_edges=False, use_tspace=False, use_triangles=False, use_custom_props=False, add_leaf_bones=True, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, armature_nodetype='NULL', bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True, axis_forward='-Z', axis_up='Y')

   Write a FBX file

   :arg filepath: File Path, Filepath used for exporting the file
   :type filepath: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_glob: filter_glob
   :type filter_glob: string, (optional, never None)
   :arg use_selection: Selected Objects, Export selected and visible objects only
   :type use_selection: boolean, (optional)
   :arg use_visible: Visible Objects, Export visible objects only
   :type use_visible: boolean, (optional)
   :arg use_active_collection: Active Collection, Export only objects from the active collection (and its children)
   :type use_active_collection: boolean, (optional)
   :arg collection: Source Collection, Export only objects from this collection (and its children)
   :type collection: string, (optional, never None)
   :arg global_scale: Scale, Scale all data (Some importers do not support scaled armatures!)
   :type global_scale: float in [0.001, 1000], (optional)
   :arg apply_unit_scale: Apply Unit, Take into account current Blender units settings (if unset, raw Blender Units values are used as-is)
   :type apply_unit_scale: boolean, (optional)
   :arg apply_scale_options: Apply Scalings, How to apply custom and units scalings in generated FBX file (Blender uses FBX scale to detect units on import, but many other applications do not handle the same way)

      * ``FBX_SCALE_NONE``
        All Local -- Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0.
      * ``FBX_SCALE_UNITS``
        FBX Units Scale -- Apply custom scaling to each object transformation, and units scaling to FBX scale.
      * ``FBX_SCALE_CUSTOM``
        FBX Custom Scale -- Apply custom scaling to FBX scale, and units scaling to each object transformation.
      * ``FBX_SCALE_ALL``
        FBX All -- Apply custom scaling and units scaling to FBX scale.
   :type apply_scale_options: enum in [``'FBX_SCALE_NONE'``, ``'FBX_SCALE_UNITS'``, ``'FBX_SCALE_CUSTOM'``, ``'FBX_SCALE_ALL'``], (optional)
   :arg use_space_transform: Use Space Transform, Apply global space transform to the object rotations. When disabled only the axis space is written to the file and all object transforms are left as-is
   :type use_space_transform: boolean, (optional)
   :arg bake_space_transform: Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risk, known to be broken with armatures/animations)
   :type bake_space_transform: boolean, (optional)
   :arg object_types: Object Types, Which kind of object to export

      * ``EMPTY``
        Empty.
      * ``CAMERA``
        Camera.
      * ``LIGHT``
        Lamp.
      * ``ARMATURE``
        Armature -- WARNING: not supported in dupli/group instances.
      * ``MESH``
        Mesh.
      * ``OTHER``
        Other -- Other geometry types, like curve, metaball, etc. (converted to meshes).
   :type object_types: enum set in {``'EMPTY'``, ``'CAMERA'``, ``'LIGHT'``, ``'ARMATURE'``, ``'MESH'``, ``'OTHER'``}, (optional)
   :arg use_mesh_modifiers: Apply Modifiers, Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys
   :type use_mesh_modifiers: boolean, (optional)
   :arg use_mesh_modifiers_render: Use Modifiers Render Setting, Use render settings when applying modifiers to mesh objects (DISABLED in Blender 2.8)
   :type use_mesh_modifiers_render: boolean, (optional)
   :arg mesh_smooth_type: Smoothing, Export smoothing information (prefer 'Normals Only' option if your target importer understand split normals)

      * ``OFF``
        Normals Only -- Export only normals instead of writing edge or face smoothing data.
      * ``FACE``
        Face -- Write face smoothing.
      * ``EDGE``
        Edge -- Write edge smoothing.
      * ``SMOOTH_GROUP``
        Smoothing Groups -- Write face smoothing groups.
   :type mesh_smooth_type: enum in [``'OFF'``, ``'FACE'``, ``'EDGE'``, ``'SMOOTH_GROUP'``], (optional)
   :arg colors_type: Vertex Colors, Export vertex color attributes

      * ``NONE``
        None -- Do not export color attributes.
      * ``SRGB``
        sRGB -- Export colors in sRGB color space.
      * ``LINEAR``
        Linear -- Export colors in linear color space.
   :type colors_type: enum in [``'NONE'``, ``'SRGB'``, ``'LINEAR'``], (optional)
   :arg prioritize_active_color: Prioritize Active Color, Make sure active color will be exported first. Could be important since some other software can discard other color attributes besides the first one
   :type prioritize_active_color: boolean, (optional)
   :arg use_subsurf: Export Subdivision Surface, Export the last Catmull-Rom subdivision modifier as FBX subdivision (does not apply the modifier even if 'Apply Modifiers' is enabled)
   :type use_subsurf: boolean, (optional)
   :arg use_mesh_edges: Loose Edges, Export loose edges (as two-vertices polygons)
   :type use_mesh_edges: boolean, (optional)
   :arg use_tspace: Tangent Space, Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!)
   :type use_tspace: boolean, (optional)
   :arg use_triangles: Triangulate Faces, Convert all faces to triangles
   :type use_triangles: boolean, (optional)
   :arg use_custom_props: Custom Properties, Export custom properties
   :type use_custom_props: boolean, (optional)
   :arg add_leaf_bones: Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)
   :type add_leaf_bones: boolean, (optional)
   :arg primary_bone_axis: Primary Bone Axis
   :type primary_bone_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'-X'``, ``'-Y'``, ``'-Z'``], (optional)
   :arg secondary_bone_axis: Secondary Bone Axis
   :type secondary_bone_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'-X'``, ``'-Y'``, ``'-Z'``], (optional)
   :arg use_armature_deform_only: Only Deform Bones, Only write deforming bones (and non-deforming ones when they have deforming children)
   :type use_armature_deform_only: boolean, (optional)
   :arg armature_nodetype: Armature FBXNode Type, FBX type of node (object) used to represent Blender's armatures (use the Null type unless you experience issues with the other app, as other choices may not import back perfectly into Blender...)

      * ``NULL``
        Null -- 'Null' FBX node, similar to Blender's Empty (default).
      * ``ROOT``
        Root -- 'Root' FBX node, supposed to be the root of chains of bones....
      * ``LIMBNODE``
        LimbNode -- 'LimbNode' FBX node, a regular joint between two bones....
   :type armature_nodetype: enum in [``'NULL'``, ``'ROOT'``, ``'LIMBNODE'``], (optional)
   :arg bake_anim: Baked Animation, Export baked keyframe animation
   :type bake_anim: boolean, (optional)
   :arg bake_anim_use_all_bones: Key All Bones, Force exporting at least one key of animation for all bones (needed with some target applications, like UE4)
   :type bake_anim_use_all_bones: boolean, (optional)
   :arg bake_anim_use_nla_strips: NLA Strips, Export each non-muted NLA strip as a separated FBX's AnimStack, if any, instead of global scene animation
   :type bake_anim_use_nla_strips: boolean, (optional)
   :arg bake_anim_use_all_actions: All Actions, Export each action as a separated FBX's AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all)
   :type bake_anim_use_all_actions: boolean, (optional)
   :arg bake_anim_force_startend_keying: Force Start/End Keying, Always add a keyframe at start and end of actions for animated channels
   :type bake_anim_force_startend_keying: boolean, (optional)
   :arg bake_anim_step: Sampling Rate, How often to evaluate animated values (in frames)
   :type bake_anim_step: float in [0.01, 100], (optional)
   :arg bake_anim_simplify_factor: Simplify, How much to simplify baked values (0.0 to disable, the higher the more simplified)
   :type bake_anim_simplify_factor: float in [0, 100], (optional)
   :arg path_mode: Path Mode, Method used to reference paths

      * ``AUTO``
        Auto -- Use relative paths with subdirectories only.
      * ``ABSOLUTE``
        Absolute -- Always write absolute paths.
      * ``RELATIVE``
        Relative -- Write relative paths where possible.
      * ``MATCH``
        Match -- Match absolute/relative setting with input path.
      * ``STRIP``
        Strip -- Filename only.
      * ``COPY``
        Copy -- Copy the file to the destination path (or subdirectory).
   :type path_mode: enum in [``'AUTO'``, ``'ABSOLUTE'``, ``'RELATIVE'``, ``'MATCH'``, ``'STRIP'``, ``'COPY'``], (optional)
   :arg embed_textures: Embed Textures, Embed textures in FBX binary file (only for "Copy" path mode!)
   :type embed_textures: boolean, (optional)
   :arg batch_mode: Batch Mode

      * ``OFF``
        Off -- Active scene to file.
      * ``SCENE``
        Scene -- Each scene as a file.
      * ``COLLECTION``
        Collection -- Each collection (data-block ones) as a file, does not include content of children collections.
      * ``SCENE_COLLECTION``
        Scene Collections -- Each collection (including master, non-data-block ones) of each scene as a file, including content from children collections.
      * ``ACTIVE_SCENE_COLLECTION``
        Active Scene Collections -- Each collection (including master, non-data-block one) of the active scene as a file, including content from children collections.
   :type batch_mode: enum in [``'OFF'``, ``'SCENE'``, ``'COLLECTION'``, ``'SCENE_COLLECTION'``, ``'ACTIVE_SCENE_COLLECTION'``], (optional)
   :arg use_batch_own_dir: Batch Own Dir, Create a dir for each exported file
   :type use_batch_own_dir: boolean, (optional)
   :arg use_metadata: Use Metadata
   :type use_metadata: boolean, (optional)
   :arg axis_forward: Forward
   :type axis_forward: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'-X'``, ``'-Y'``, ``'-Z'``], (optional)
   :arg axis_up: Up
   :type axis_up: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'-X'``, ``'-Y'``, ``'-Z'``], (optional)
   :File: `addons_core\io_scene_fbx\__init__.py\:582 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\io_scene_fbx\__init__.py#L582>`__


.. function:: gltf(*, filepath="", check_existing=True, export_import_convert_lighting_mode='SPEC', gltf_export_id="", export_use_gltfpack=False, export_gltfpack_tc=True, export_gltfpack_tq=8, export_gltfpack_si=1.0, export_gltfpack_sa=False, export_gltfpack_slb=False, export_gltfpack_vp=14, export_gltfpack_vt=12, export_gltfpack_vn=8, export_gltfpack_vc=8, export_gltfpack_vpi='Integer', export_gltfpack_noq=True, export_gltfpack_kn=False, export_format='', ui_tab='GENERAL', export_copyright="", export_image_format='AUTO', export_image_add_webp=False, export_image_webp_fallback=False, export_texture_dir="", export_jpeg_quality=75, export_image_quality=75, export_keep_originals=False, export_texcoords=True, export_normals=True, export_gn_mesh=False, export_draco_mesh_compression_enable=False, export_draco_mesh_compression_level=6, export_draco_position_quantization=14, export_draco_normal_quantization=10, export_draco_texcoord_quantization=12, export_draco_color_quantization=10, export_draco_generic_quantization=12, export_tangents=False, export_materials='EXPORT', export_unused_images=False, export_unused_textures=False, export_vertex_color='MATERIAL', export_vertex_color_name="Color", export_all_vertex_colors=True, export_active_vertex_color_when_no_material=True, export_attributes=False, use_mesh_edges=False, use_mesh_vertices=False, export_cameras=False, use_selection=False, use_visible=False, use_renderable=False, use_active_collection_with_nested=True, use_active_collection=False, use_active_scene=False, collection="", at_collection_center=False, export_extras=False, export_yup=True, export_apply=False, export_shared_accessors=False, export_animations=True, export_frame_range=False, export_frame_step=1, export_force_sampling=True, export_sampling_interpolation_fallback='LINEAR', export_pointer_animation=False, export_animation_mode='ACTIONS', export_nla_strips_merged_animation_name="Animation", export_def_bones=False, export_hierarchy_flatten_bones=False, export_hierarchy_flatten_objs=False, export_armature_object_remove=False, export_leaf_bone=False, export_optimize_animation_size=True, export_optimize_animation_keep_anim_armature=True, export_optimize_animation_keep_anim_object=False, export_optimize_disable_viewport=False, export_negative_frame='SLIDE', export_anim_slide_to_zero=False, export_bake_animation=False, export_merge_animation='ACTION', export_anim_single_armature=True, export_reset_pose_bones=True, export_current_frame=False, export_rest_position_armature=True, export_anim_scene_split_object=True, export_skins=True, export_influence_nb=4, export_all_influences=False, export_morph=True, export_morph_normal=True, export_morph_tangent=False, export_morph_animation=True, export_morph_reset_sk_data=True, export_lights=False, export_try_sparse_sk=True, export_try_omit_sparse_sk=False, export_gpu_instances=False, export_action_filter=False, export_convert_animation_pointer=False, export_nla_strips=True, export_original_specular=False, will_save_settings=False, export_hierarchy_full_collections=False, export_extra_animations=False, export_loglevel=-1, filter_glob="*.glb")

   Export scene as glTF 2.0 file

   :arg filepath: File Path, Filepath used for exporting the file
   :type filepath: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg export_import_convert_lighting_mode: Lighting Mode, Optional backwards compatibility for non-standard render engines. Applies to lights

      * ``SPEC``
        Standard -- Physically-based glTF lighting units (cd, lx, nt).
      * ``COMPAT``
        Unitless -- Non-physical, unitless lighting. Useful when exposure controls are not available.
      * ``RAW``
        Raw (Deprecated) -- Blender lighting strengths with no conversion.
   :type export_import_convert_lighting_mode: enum in [``'SPEC'``, ``'COMPAT'``, ``'RAW'``], (optional)
   :arg gltf_export_id: Identifier, Identifier of caller (in case of add-on calling this exporter). Can be useful in case of Extension added by other add-ons
   :type gltf_export_id: string, (optional, never None)
   :arg export_use_gltfpack: Use Gltfpack, Use gltfpack to simplify the mesh and/or compress its textures
   :type export_use_gltfpack: boolean, (optional)
   :arg export_gltfpack_tc: KTX2 Compression, Convert all textures to KTX2 with BasisU supercompression
   :type export_gltfpack_tc: boolean, (optional)
   :arg export_gltfpack_tq: Texture Encoding Quality, Texture encoding quality
   :type export_gltfpack_tq: int in [1, 10], (optional)
   :arg export_gltfpack_si: Mesh Simplification Ratio, Simplify meshes targeting triangle count ratio
   :type export_gltfpack_si: float in [0, 1], (optional)
   :arg export_gltfpack_sa: Aggressive Mesh Simplification, Aggressively simplify to the target ratio disregarding quality
   :type export_gltfpack_sa: boolean, (optional)
   :arg export_gltfpack_slb: Lock Mesh Border Vertices, Lock border vertices during simplification to avoid gaps on connected meshes
   :type export_gltfpack_slb: boolean, (optional)
   :arg export_gltfpack_vp: Position Quantization, Use N-bit quantization for positions
   :type export_gltfpack_vp: int in [1, 16], (optional)
   :arg export_gltfpack_vt: Texture Coordinate Quantization, Use N-bit quantization for texture coordinates
   :type export_gltfpack_vt: int in [1, 16], (optional)
   :arg export_gltfpack_vn: Normal/Tangent Quantization, Use N-bit quantization for normals and tangents
   :type export_gltfpack_vn: int in [1, 16], (optional)
   :arg export_gltfpack_vc: Vertex Color Quantization, Use N-bit quantization for colors
   :type export_gltfpack_vc: int in [1, 16], (optional)
   :arg export_gltfpack_vpi: Vertex Position Attributes, Type to use for vertex position attributes

      * ``Integer``
        Integer -- Use integer attributes for positions.
      * ``Normalized``
        Normalized -- Use normalized attributes for positions.
      * ``Floating-point``
        Floating-point -- Use floating-point attributes for positions.
   :type export_gltfpack_vpi: enum in [``'Integer'``, ``'Normalized'``, ``'Floating-point'``], (optional)
   :arg export_gltfpack_noq: Disable Quantization, Disable quantization; produces much larger glTF files with no extensions
   :type export_gltfpack_noq: boolean, (optional)
   :arg export_gltfpack_kn: Keep Named Nodes, Restrict some optimization to keep named nodes and meshes attached to named nodes so that named nodes can be transformed externally
   :type export_gltfpack_kn: boolean, (optional)
   :arg export_format: Format, Output format. Binary is most efficient, but JSON may be easier to edit later
   :type export_format: enum in [], (optional)
   :arg ui_tab: ui_tab, Export setting categories

      * ``GENERAL``
        General -- General settings.
      * ``MESHES``
        Meshes -- Mesh settings.
      * ``OBJECTS``
        Objects -- Object settings.
      * ``ANIMATION``
        Animation -- Animation settings.
   :type ui_tab: enum in [``'GENERAL'``, ``'MESHES'``, ``'OBJECTS'``, ``'ANIMATION'``], (optional)
   :arg export_copyright: Copyright, Legal rights and conditions for the model
   :type export_copyright: string, (optional, never None)
   :arg export_image_format: Images, Output format for images. PNG is lossless and generally preferred, but JPEG might be preferable for web applications due to the smaller file size. Alternatively they can be omitted if they are not needed

      * ``AUTO``
        Automatic -- Save PNGs as PNGs, JPEGs as JPEGs, WebPs as WebPs. For other formats, use PNG.
      * ``JPEG``
        JPEG Format (.jpg) -- Save images as JPEGs. (Images that need alpha are saved as PNGs though.) Be aware of a possible loss in quality.
      * ``WEBP``
        WebP Format -- Save images as WebPs as main image (no fallback).
      * ``NONE``
        None -- Don't export images.
   :type export_image_format: enum in [``'AUTO'``, ``'JPEG'``, ``'WEBP'``, ``'NONE'``], (optional)
   :arg export_image_add_webp: Create WebP, Creates WebP textures for every texture. For already WebP textures, nothing happens
   :type export_image_add_webp: boolean, (optional)
   :arg export_image_webp_fallback: WebP Fallback, For all WebP textures, create a PNG fallback texture
   :type export_image_webp_fallback: boolean, (optional)
   :arg export_texture_dir: Textures, Folder to place texture files in. Relative to the .gltf file
   :type export_texture_dir: string, (optional, never None)
   :arg export_jpeg_quality: JPEG Quality, Quality of JPEG export
   :type export_jpeg_quality: int in [0, 100], (optional)
   :arg export_image_quality: Image Quality, Quality of image export
   :type export_image_quality: int in [0, 100], (optional)
   :arg export_keep_originals: Keep Original, Keep original textures files if possible. WARNING: if you use more than one texture, where pbr standard requires only one, only one texture will be used. This can lead to unexpected results
   :type export_keep_originals: boolean, (optional)
   :arg export_texcoords: UVs, Export UVs (texture coordinates) with meshes
   :type export_texcoords: boolean, (optional)
   :arg export_normals: Normals, Export vertex normals with meshes
   :type export_normals: boolean, (optional)
   :arg export_gn_mesh: Geometry Nodes Instances (Experimental), Export Geometry nodes instance meshes
   :type export_gn_mesh: boolean, (optional)
   :arg export_draco_mesh_compression_enable: Draco Mesh Compression, Compress mesh using Draco
   :type export_draco_mesh_compression_enable: boolean, (optional)
   :arg export_draco_mesh_compression_level: Compression Level, Compression level (0 = most speed, 6 = most compression, higher values currently not supported)
   :type export_draco_mesh_compression_level: int in [0, 10], (optional)
   :arg export_draco_position_quantization: Position Quantization Bits, Quantization bits for position values (0 = no quantization)
   :type export_draco_position_quantization: int in [0, 30], (optional)
   :arg export_draco_normal_quantization: Normal Quantization Bits, Quantization bits for normal values (0 = no quantization)
   :type export_draco_normal_quantization: int in [0, 30], (optional)
   :arg export_draco_texcoord_quantization: Texcoord Quantization Bits, Quantization bits for texture coordinate values (0 = no quantization)
   :type export_draco_texcoord_quantization: int in [0, 30], (optional)
   :arg export_draco_color_quantization: Color Quantization Bits, Quantization bits for color values (0 = no quantization)
   :type export_draco_color_quantization: int in [0, 30], (optional)
   :arg export_draco_generic_quantization: Generic Quantization Bits, Quantization bits for generic values like weights or joints (0 = no quantization)
   :type export_draco_generic_quantization: int in [0, 30], (optional)
   :arg export_tangents: Tangents, Export vertex tangents with meshes
   :type export_tangents: boolean, (optional)
   :arg export_materials: Materials, Export materials

      * ``EXPORT``
        Export -- Export all materials used by included objects.
      * ``PLACEHOLDER``
        Placeholder -- Do not export materials, but write multiple primitive groups per mesh, keeping material slot information.
      * ``VIEWPORT``
        Viewport -- Export minimal materials as defined in Viewport display properties.
      * ``NONE``
        No export -- Do not export materials, and combine mesh primitive groups, losing material slot information.
   :type export_materials: enum in [``'EXPORT'``, ``'PLACEHOLDER'``, ``'VIEWPORT'``, ``'NONE'``], (optional)
   :arg export_unused_images: Unused Images, Export images not assigned to any material
   :type export_unused_images: boolean, (optional)
   :arg export_unused_textures: Prepare Unused Textures, Export image texture nodes not assigned to any material. This feature is not standard and needs an external extension to be included in the glTF file
   :type export_unused_textures: boolean, (optional)
   :arg export_vertex_color: Use Vertex Color, How to export vertex color

      * ``MATERIAL``
        Material -- Export vertex color when used by material.
      * ``ACTIVE``
        Active -- Export active vertex color.
      * ``NAME``
        Name -- Export vertex color with this name.
      * ``NONE``
        None -- Do not export vertex color.
   :type export_vertex_color: enum in [``'MATERIAL'``, ``'ACTIVE'``, ``'NAME'``, ``'NONE'``], (optional)
   :arg export_vertex_color_name: Vertex Color Name, Name of vertex color to export
   :type export_vertex_color_name: string, (optional, never None)
   :arg export_all_vertex_colors: Export All Vertex Colors, Export all vertex colors, even if not used by any material. If no Vertex Color is used in the mesh materials, a fake COLOR_0 will be created, in order to keep material unchanged
   :type export_all_vertex_colors: boolean, (optional)
   :arg export_active_vertex_color_when_no_material: Export Active Vertex Color When No Material, When there is no material on object, export active vertex color
   :type export_active_vertex_color_when_no_material: boolean, (optional)
   :arg export_attributes: Attributes, Export Attributes (when starting with underscore)
   :type export_attributes: boolean, (optional)
   :arg use_mesh_edges: Loose Edges, Export loose edges as lines, using the material from the first material slot
   :type use_mesh_edges: boolean, (optional)
   :arg use_mesh_vertices: Loose Points, Export loose points as glTF points, using the material from the first material slot
   :type use_mesh_vertices: boolean, (optional)
   :arg export_cameras: Cameras, Export cameras
   :type export_cameras: boolean, (optional)
   :arg use_selection: Selected Objects, Export selected objects only
   :type use_selection: boolean, (optional)
   :arg use_visible: Visible Objects, Export visible objects only
   :type use_visible: boolean, (optional)
   :arg use_renderable: Renderable Objects, Export renderable objects only
   :type use_renderable: boolean, (optional)
   :arg use_active_collection_with_nested: Include Nested Collections, Include active collection and nested collections
   :type use_active_collection_with_nested: boolean, (optional)
   :arg use_active_collection: Active Collection, Export objects in the active collection only
   :type use_active_collection: boolean, (optional)
   :arg use_active_scene: Active Scene, Export active scene only
   :type use_active_scene: boolean, (optional)
   :arg collection: Source Collection, Export only objects from this collection (and its children)
   :type collection: string, (optional, never None)
   :arg at_collection_center: Export at Collection Center, Export at Collection center of mass of root objects of the collection
   :type at_collection_center: boolean, (optional)
   :arg export_extras: Custom Properties, Export custom properties as glTF extras
   :type export_extras: boolean, (optional)
   :arg export_yup: +Y Up, Export using glTF convention, +Y up
   :type export_yup: boolean, (optional)
   :arg export_apply: Apply Modifiers, Apply modifiers (excluding Armatures) to mesh objects -WARNING: prevents exporting shape keys
   :type export_apply: boolean, (optional)
   :arg export_shared_accessors: Shared Accessors, Export Primitives using shared accessors for attributes
   :type export_shared_accessors: boolean, (optional)
   :arg export_animations: Animations, Exports active actions and NLA tracks as glTF animations
   :type export_animations: boolean, (optional)
   :arg export_frame_range: Limit to Playback Range, Clips animations to selected playback range
   :type export_frame_range: boolean, (optional)
   :arg export_frame_step: Sampling Rate, How often to evaluate animated values (in frames)
   :type export_frame_step: int in [1, 120], (optional)
   :arg export_force_sampling: Always Sample Animations, Apply sampling to all animations
   :type export_force_sampling: boolean, (optional)
   :arg export_sampling_interpolation_fallback: Sampling Interpolation Fallback, Interpolation fallback for sampled animations, when the property is not keyed

      * ``LINEAR``
        Linear -- Linear interpolation between keyframes.
      * ``STEP``
        Step -- No interpolation between keyframes.
   :type export_sampling_interpolation_fallback: enum in [``'LINEAR'``, ``'STEP'``], (optional)
   :arg export_pointer_animation: Export Animation Pointer (Experimental), Export material, Light & Camera animation as Animation Pointer. Available only for baked animation mode 'NLA Tracks' and 'Scene'
   :type export_pointer_animation: boolean, (optional)
   :arg export_animation_mode: Animation Mode, Export Animation mode

      * ``ACTIONS``
        Actions -- Export actions (actives and on NLA tracks) as separate animations.
      * ``ACTIVE_ACTIONS``
        Active actions merged -- All the currently assigned actions become one glTF animation.
      * ``BROADCAST``
        Broadcast actions -- Broadcast all compatible actions to all objects. Animated objects will get all actions compatible with them, others will get no animation at all.
      * ``NLA_TRACKS``
        NLA Tracks -- Export individual NLA Tracks as separate animation.
      * ``SCENE``
        Scene -- Export baked scene as a single animation.
   :type export_animation_mode: enum in [``'ACTIONS'``, ``'ACTIVE_ACTIONS'``, ``'BROADCAST'``, ``'NLA_TRACKS'``, ``'SCENE'``], (optional)
   :arg export_nla_strips_merged_animation_name: Merged Animation Name, Name of single glTF animation to be exported
   :type export_nla_strips_merged_animation_name: string, (optional, never None)
   :arg export_def_bones: Export Deformation Bones Only, Export Deformation bones only
   :type export_def_bones: boolean, (optional)
   :arg export_hierarchy_flatten_bones: Flatten Bone Hierarchy, Flatten Bone Hierarchy. Useful in case of non decomposable transformation matrix
   :type export_hierarchy_flatten_bones: boolean, (optional)
   :arg export_hierarchy_flatten_objs: Flatten Object Hierarchy, Flatten Object Hierarchy. Useful in case of non decomposable transformation matrix
   :type export_hierarchy_flatten_objs: boolean, (optional)
   :arg export_armature_object_remove: Remove Armature Object, Remove Armature object if possible. If Armature has multiple root bones, object will not be removed
   :type export_armature_object_remove: boolean, (optional)
   :arg export_leaf_bone: Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)
   :type export_leaf_bone: boolean, (optional)
   :arg export_optimize_animation_size: Optimize Animation Size, Reduce exported file size by removing duplicate keyframes
   :type export_optimize_animation_size: boolean, (optional)
   :arg export_optimize_animation_keep_anim_armature: Force Keeping Channels for Bones, If all keyframes are identical in a rig, force keeping the minimal animation. When off, all possible channels for the bones will be exported, even if empty (minimal animation, 2 keyframes)
   :type export_optimize_animation_keep_anim_armature: boolean, (optional)
   :arg export_optimize_animation_keep_anim_object: Force Keeping Channel for Objects, If all keyframes are identical for object transformations, force keeping the minimal animation
   :type export_optimize_animation_keep_anim_object: boolean, (optional)
   :arg export_optimize_disable_viewport: Disable Viewport for Other Objects, When exporting animations, disable viewport for other objects, for performance
   :type export_optimize_disable_viewport: boolean, (optional)
   :arg export_negative_frame: Negative Frames, Negative Frames are slid or cropped

      * ``SLIDE``
        Slide -- Slide animation to start at frame 0.
      * ``CROP``
        Crop -- Keep only frames above frame 0.
   :type export_negative_frame: enum in [``'SLIDE'``, ``'CROP'``], (optional)
   :arg export_anim_slide_to_zero: Set All glTF Animation Starting at 0, Set all glTF animation starting at 0.0s. Can be useful for looping animations
   :type export_anim_slide_to_zero: boolean, (optional)
   :arg export_bake_animation: Bake All Objects Animations, Force exporting animation on every object. Can be useful when using constraints or driver. Also useful when exporting only selection
   :type export_bake_animation: boolean, (optional)
   :arg export_merge_animation: Merge Animation, Merge Animations

      * ``NLA_TRACK``
        NLA Track Names -- Merge by NLA Track Names.
      * ``ACTION``
        Actions -- Merge by Actions.
      * ``NONE``
        No Merge -- Do Not Merge Animations.
   :type export_merge_animation: enum in [``'NLA_TRACK'``, ``'ACTION'``, ``'NONE'``], (optional)
   :arg export_anim_single_armature: Export all Armature Actions, Export all actions, bound to a single armature. WARNING: Option does not support exports including multiple armatures
   :type export_anim_single_armature: boolean, (optional)
   :arg export_reset_pose_bones: Reset Pose Bones Between Actions, Reset pose bones between each action exported. This is needed when some bones are not keyed on some animations
   :type export_reset_pose_bones: boolean, (optional)
   :arg export_current_frame: Use Current Frame as Object Rest Transformations, Export the scene in the current animation frame. When off, frame 0 is used as rest transformations for objects
   :type export_current_frame: boolean, (optional)
   :arg export_rest_position_armature: Use Rest Position Armature, Export armatures using rest position as joints' rest pose. When off, current frame pose is used as rest pose
   :type export_rest_position_armature: boolean, (optional)
   :arg export_anim_scene_split_object: Split Animation by Object, Export Scene as seen in Viewport, But split animation by Object
   :type export_anim_scene_split_object: boolean, (optional)
   :arg export_skins: Skinning, Export skinning (armature) data
   :type export_skins: boolean, (optional)
   :arg export_influence_nb: Bone Influences, Choose how many Bone influences to export
   :type export_influence_nb: int in [1, inf], (optional)
   :arg export_all_influences: Include All Bone Influences, Allow export of all joint vertex influences. Models may appear incorrectly in many viewers
   :type export_all_influences: boolean, (optional)
   :arg export_morph: Shape Keys, Export shape keys (morph targets)
   :type export_morph: boolean, (optional)
   :arg export_morph_normal: Shape Key Normals, Export vertex normals with shape keys (morph targets)
   :type export_morph_normal: boolean, (optional)
   :arg export_morph_tangent: Shape Key Tangents, Export vertex tangents with shape keys (morph targets)
   :type export_morph_tangent: boolean, (optional)
   :arg export_morph_animation: Shape Key Animations, Export shape keys animations (morph targets)
   :type export_morph_animation: boolean, (optional)
   :arg export_morph_reset_sk_data: Reset Shape Keys Between Actions, Reset shape keys between each action exported. This is needed when some SK channels are not keyed on some animations
   :type export_morph_reset_sk_data: boolean, (optional)
   :arg export_lights: Punctual Lights, Export directional, point, and spot lights. Uses "KHR_lights_punctual" glTF extension
   :type export_lights: boolean, (optional)
   :arg export_try_sparse_sk: Use Sparse Accessor if Better, Try using Sparse Accessor if it saves space
   :type export_try_sparse_sk: boolean, (optional)
   :arg export_try_omit_sparse_sk: Omitting Sparse Accessor if Data is Empty, Omitting Sparse Accessor if data is empty
   :type export_try_omit_sparse_sk: boolean, (optional)
   :arg export_gpu_instances: GPU Instances, Export using EXT_mesh_gpu_instancing. Limited to children of a given Empty. Multiple materials might be omitted
   :type export_gpu_instances: boolean, (optional)
   :arg export_action_filter: Filter Actions, Filter Actions to be exported
   :type export_action_filter: boolean, (optional)
   :arg export_convert_animation_pointer: Convert TRS/Weights to Animation Pointer, Export TRS and weights as Animation Pointer. Using KHR_animation_pointer extension
   :type export_convert_animation_pointer: boolean, (optional)
   :arg export_nla_strips: Group by NLA Track, When on, multiple actions become part of the same glTF animation if they're pushed onto NLA tracks with the same name. When off, all the currently assigned actions become one glTF animation
   :type export_nla_strips: boolean, (optional)
   :arg export_original_specular: Export Original PBR Specular, Export original glTF PBR Specular, instead of Blender Principled Shader Specular
   :type export_original_specular: boolean, (optional)
   :arg will_save_settings: Remember Export Settings, Store glTF export settings in the Blender project
   :type will_save_settings: boolean, (optional)
   :arg export_hierarchy_full_collections: Full Collection Hierarchy, Export full hierarchy, including intermediate collections
   :type export_hierarchy_full_collections: boolean, (optional)
   :arg export_extra_animations: Prepare Extra Animations, Export additional animations.This feature is not standard and needs an external extension to be included in the glTF file
   :type export_extra_animations: boolean, (optional)
   :arg export_loglevel: Log Level, Log Level
   :type export_loglevel: int in [-inf, inf], (optional)
   :arg filter_glob: filter_glob
   :type filter_glob: string, (optional, never None)
   :File: `addons_core\io_scene_gltf2\__init__.py\:1082 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\io_scene_gltf2\__init__.py#L1082>`__


