Import Scene Operators
======================

.. module:: bpy.ops.import_scene

.. function:: fbx(*, filepath="", directory="", filter_glob="*.fbx", files=None, ui_tab='MAIN', use_manual_orientation=False, global_scale=1.0, bake_space_transform=False, use_custom_normals=True, colors_type='SRGB', use_image_search=True, use_alpha_decals=False, decal_offset=0.0, use_anim=True, anim_offset=1.0, use_subsurf=False, use_custom_props=True, use_custom_props_enum_as_string=True, ignore_leaf_bones=False, force_connect_children=False, automatic_bone_orientation=False, primary_bone_axis='Y', secondary_bone_axis='X', use_prepost_rot=True, axis_forward='-Z', axis_up='Y')

   Load a FBX file

   :arg filepath: File Path, Filepath used for importing the file
   :type filepath: string, (optional, never None)
   :arg directory: directory
   :type directory: string, (optional, never None)
   :arg filter_glob: filter_glob
   :type filter_glob: string, (optional, never None)
   :arg files: File Path
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg ui_tab: ui_tab, Import options categories

      * ``MAIN``
        Main -- Main basic settings.
      * ``ARMATURE``
        Armatures -- Armature-related settings.
   :type ui_tab: enum in [``'MAIN'``, ``'ARMATURE'``], (optional)
   :arg use_manual_orientation: Manual Orientation, Specify orientation and scale, instead of using embedded data in FBX file
   :type use_manual_orientation: boolean, (optional)
   :arg global_scale: Scale
   :type global_scale: float in [0.001, 1000], (optional)
   :arg bake_space_transform: Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risk, known to be broken with armatures/animations)
   :type bake_space_transform: boolean, (optional)
   :arg use_custom_normals: Custom Normals, Import custom normals, if available (otherwise Blender will recompute them)
   :type use_custom_normals: boolean, (optional)
   :arg colors_type: Vertex Colors, Import vertex color attributes

      * ``NONE``
        None -- Do not import color attributes.
      * ``SRGB``
        sRGB -- Expect file colors in sRGB color space.
      * ``LINEAR``
        Linear -- Expect file colors in linear color space.
   :type colors_type: enum in [``'NONE'``, ``'SRGB'``, ``'LINEAR'``], (optional)
   :arg use_image_search: Image Search, Search subdirs for any associated images (WARNING: may be slow)
   :type use_image_search: boolean, (optional)
   :arg use_alpha_decals: Alpha Decals, Treat materials with alpha as decals (no shadow casting)
   :type use_alpha_decals: boolean, (optional)
   :arg decal_offset: Decal Offset, Displace geometry of alpha meshes
   :type decal_offset: float in [0, 1], (optional)
   :arg use_anim: Import Animation, Import FBX animation
   :type use_anim: boolean, (optional)
   :arg anim_offset: Animation Offset, Offset to apply to animation during import, in frames
   :type anim_offset: float in [-inf, inf], (optional)
   :arg use_subsurf: Subdivision Data, Import FBX subdivision information as subdivision surface modifiers
   :type use_subsurf: boolean, (optional)
   :arg use_custom_props: Custom Properties, Import user properties as custom properties
   :type use_custom_props: boolean, (optional)
   :arg use_custom_props_enum_as_string: Import Enums As Strings, Store enumeration values as strings
   :type use_custom_props_enum_as_string: boolean, (optional)
   :arg ignore_leaf_bones: Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone)
   :type ignore_leaf_bones: boolean, (optional)
   :arg force_connect_children: Force Connect Children, Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures)
   :type force_connect_children: boolean, (optional)
   :arg automatic_bone_orientation: Automatic Bone Orientation, Try to align the major bone axis with the bone children
   :type automatic_bone_orientation: boolean, (optional)
   :arg primary_bone_axis: Primary Bone Axis
   :type primary_bone_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'-X'``, ``'-Y'``, ``'-Z'``], (optional)
   :arg secondary_bone_axis: Secondary Bone Axis
   :type secondary_bone_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'-X'``, ``'-Y'``, ``'-Z'``], (optional)
   :arg use_prepost_rot: Use Pre/Post Rotation, Use pre/post rotation from FBX transform (you may have to disable that in some cases)
   :type use_prepost_rot: boolean, (optional)
   :arg axis_forward: Forward
   :type axis_forward: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'-X'``, ``'-Y'``, ``'-Z'``], (optional)
   :arg axis_up: Up
   :type axis_up: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'-X'``, ``'-Y'``, ``'-Z'``], (optional)
   :File: `addons_core\io_scene_fbx\__init__.py\:210 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\io_scene_fbx\__init__.py#L210>`__


.. function:: gltf(*, filepath="", export_import_convert_lighting_mode='SPEC', filter_glob="*.glb;*.gltf", directory="", files=None, loglevel=0, import_pack_images=True, merge_vertices=False, import_shading='NORMALS', bone_heuristic='BLENDER', disable_bone_shape=False, bone_shape_scale_factor=1.0, guess_original_bind_pose=True, import_webp_texture=False, import_unused_materials=False, import_select_created_objects=True, import_scene_extras=True, import_scene_as_collection=True, import_merge_material_slots=True)

   Load a glTF 2.0 file

   :arg filepath: File Path, Filepath used for importing the file
   :type filepath: string, (optional, never None)
   :arg export_import_convert_lighting_mode: Lighting Mode, Optional backwards compatibility for non-standard render engines. Applies to lights

      * ``SPEC``
        Standard -- Physically-based glTF lighting units (cd, lx, nt).
      * ``COMPAT``
        Unitless -- Non-physical, unitless lighting. Useful when exposure controls are not available.
      * ``RAW``
        Raw (Deprecated) -- Blender lighting strengths with no conversion.
   :type export_import_convert_lighting_mode: enum in [``'SPEC'``, ``'COMPAT'``, ``'RAW'``], (optional)
   :arg filter_glob: filter_glob
   :type filter_glob: string, (optional, never None)
   :arg directory: directory
   :type directory: string, (optional, never None)
   :arg files: File Path
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg loglevel: Log Level, Log Level
   :type loglevel: int in [-inf, inf], (optional)
   :arg import_pack_images: Pack Images, Pack all images into .blend file
   :type import_pack_images: boolean, (optional)
   :arg merge_vertices: Merge Vertices, The glTF format requires discontinuous normals, UVs, and other vertex attributes to be stored as separate vertices, as required for rendering on typical graphics hardware. This option attempts to combine co-located vertices where possible. Currently cannot combine verts with different normals
   :type merge_vertices: boolean, (optional)
   :arg import_shading: Shading, How normals are computed during import
   :type import_shading: enum in [``'NORMALS'``, ``'FLAT'``, ``'SMOOTH'``], (optional)
   :arg bone_heuristic: Bone Dir, Heuristic for placing bones. Tries to make bones pretty

      * ``BLENDER``
        Blender (best for import/export round trip) -- Good for re-importing glTFs exported from Blender, and re-exporting glTFs to glTFs after Blender editing. Bone tips are placed on their local +Y axis (in glTF space).
      * ``TEMPERANCE``
        Temperance (average) -- Decent all-around strategy. A bone with one child has its tip placed on the local axis closest to its child.
      * ``FORTUNE``
        Fortune (may look better, less accurate) -- Might look better than Temperance, but also might have errors. A bone with one child has its tip placed at its child's root. Non-uniform scalings may get messed up though, so beware.
   :type bone_heuristic: enum in [``'BLENDER'``, ``'TEMPERANCE'``, ``'FORTUNE'``], (optional)
   :arg disable_bone_shape: Disable Bone Shape, Do not create bone shapes
   :type disable_bone_shape: boolean, (optional)
   :arg bone_shape_scale_factor: Bone Shape Scale, Scale factor for bone shapes
   :type bone_shape_scale_factor: float in [-inf, inf], (optional)
   :arg guess_original_bind_pose: Guess Original Bind Pose, Try to guess the original bind pose for skinned meshes from the inverse bind matrices. When off, use default/rest pose as bind pose
   :type guess_original_bind_pose: boolean, (optional)
   :arg import_webp_texture: Import WebP Textures, If a texture exists in WebP format, loads the WebP texture instead of the fallback PNG/JPEG one
   :type import_webp_texture: boolean, (optional)
   :arg import_unused_materials: Import Unused Materials & Images, Import materials & Images not assigned to any mesh
   :type import_unused_materials: boolean, (optional)
   :arg import_select_created_objects: Select Imported Objects, Select created objects at the end of the import
   :type import_select_created_objects: boolean, (optional)
   :arg import_scene_extras: Import Scene Extras, Import scene extras as custom properties. Existing custom properties will be overwritten
   :type import_scene_extras: boolean, (optional)
   :arg import_scene_as_collection: Import Scene as Collection, Import the scene as a collection
   :type import_scene_as_collection: boolean, (optional)
   :arg import_merge_material_slots: Merge Material Slot when possible, Merge material slots when possible
   :type import_merge_material_slots: boolean, (optional)
   :File: `addons_core\io_scene_gltf2\__init__.py\:2010 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\io_scene_gltf2\__init__.py#L2010>`__


