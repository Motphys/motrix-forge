Wm Operators
============

.. module:: bpy.ops.wm

.. function:: alembic_export(*, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=True, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', filter_glob="*.abc", start=-2147483648, end=-2147483648, xsamples=1, gsamples=1, sh_open=0.0, sh_close=1.0, selected=False, visible_objects_only=False, flatten=False, collection="", uvs=True, packuv=True, normals=True, vcolors=False, orcos=True, face_sets=False, subdiv_schema=False, apply_subdiv=False, curves_as_mesh=False, use_instancing=True, global_scale=1.0, triangulate=False, quad_method='SHORTEST_DIAGONAL', ngon_method='BEAUTY', export_hair=True, export_particles=True, export_custom_properties=True, as_background_job=False, evaluation_mode='RENDER', init_scene_frame_range=True)

   Export current scene in an Alembic archive

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :type filter_glob: string, (optional, never None)
   :arg start: Start Frame, Start frame of the export, use the default value to take the start frame of the current scene
   :type start: int in [-inf, inf], (optional)
   :arg end: End Frame, End frame of the export, use the default value to take the end frame of the current scene
   :type end: int in [-inf, inf], (optional)
   :arg xsamples: Transform Samples, Number of times per frame transformations are sampled
   :type xsamples: int in [1, 128], (optional)
   :arg gsamples: Geometry Samples, Number of times per frame object data are sampled
   :type gsamples: int in [1, 128], (optional)
   :arg sh_open: Shutter Open, Time at which the shutter is open
   :type sh_open: float in [-1, 1], (optional)
   :arg sh_close: Shutter Close, Time at which the shutter is closed
   :type sh_close: float in [-1, 1], (optional)
   :arg selected: Selected Objects Only, Export only selected objects
   :type selected: boolean, (optional)
   :arg visible_objects_only: Visible Objects Only, Export only objects that are visible
   :type visible_objects_only: boolean, (optional)
   :arg flatten: Flatten Hierarchy, Do not preserve objects' parent/children relationship
   :type flatten: boolean, (optional)
   :arg collection: Collection
   :type collection: string, (optional, never None)
   :arg uvs: UV Coordinates, Export UV coordinates
   :type uvs: boolean, (optional)
   :arg packuv: Merge UVs
   :type packuv: boolean, (optional)
   :arg normals: Normals, Export normals
   :type normals: boolean, (optional)
   :arg vcolors: Color Attributes, Export color attributes
   :type vcolors: boolean, (optional)
   :arg orcos: Generated Coordinates, Export undeformed mesh vertex coordinates
   :type orcos: boolean, (optional)
   :arg face_sets: Face Sets, Export per face shading group assignments
   :type face_sets: boolean, (optional)
   :arg subdiv_schema: Use Subdivision Schema, Export meshes using Alembic's subdivision schema
   :type subdiv_schema: boolean, (optional)
   :arg apply_subdiv: Apply Subdivision Surface, Export subdivision surfaces as meshes
   :type apply_subdiv: boolean, (optional)
   :arg curves_as_mesh: Curves as Mesh, Export curves and NURBS surfaces as meshes
   :type curves_as_mesh: boolean, (optional)
   :arg use_instancing: Use Instancing, Export data of duplicated objects as Alembic instances; speeds up the export and can be disabled for compatibility with other software
   :type use_instancing: boolean, (optional)
   :arg global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
   :type global_scale: float in [0.0001, 1000], (optional)
   :arg triangulate: Triangulate, Export polygons (quads and n-gons) as triangles
   :type triangulate: boolean, (optional)
   :arg quad_method: Quad Method, Method for splitting the quads into triangles
   :type quad_method: enum in :ref:`rna_enum_modifier_triangulate_quad_method_items`, (optional)
   :arg ngon_method: N-gon Method, Method for splitting the n-gons into triangles
   :type ngon_method: enum in :ref:`rna_enum_modifier_triangulate_ngon_method_items`, (optional)
   :arg export_hair: Export Hair, Exports hair particle systems as animated curves
   :type export_hair: boolean, (optional)
   :arg export_particles: Export Particles, Exports non-hair particle systems
   :type export_particles: boolean, (optional)
   :arg export_custom_properties: Export Custom Properties, Export custom properties to Alembic .userProperties
   :type export_custom_properties: boolean, (optional)
   :arg as_background_job: Run as Background Job, Enable this to run the import in the background, disable to block Blender while importing. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
   :type as_background_job: boolean, (optional)
   :arg evaluation_mode: Settings, Determines visibility of objects, modifier settings, and other areas where there are different settings for viewport and rendering

      * ``RENDER``
        Render -- Use Render settings for object visibility, modifier settings, etc.
      * ``VIEWPORT``
        Viewport -- Use Viewport settings for object visibility, modifier settings, etc.
   :type evaluation_mode: enum in [``'RENDER'``, ``'VIEWPORT'``], (optional)
   :type init_scene_frame_range: boolean, (optional)

.. function:: alembic_import(*, filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=True, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='', filter_glob="*.abc", scale=1.0, set_frame_range=True, validate_meshes=False, always_add_cache_reader=False, is_sequence=False, as_background_job=False)

   Load an Alembic archive

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg relative_path: Relative Path, Select the file relative to the blend file
   :type relative_path: boolean, (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :type filter_glob: string, (optional, never None)
   :arg scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
   :type scale: float in [0.0001, 1000], (optional)
   :arg set_frame_range: Set Frame Range, If checked, update scene's start and end frame to match those of the Alembic archive
   :type set_frame_range: boolean, (optional)
   :arg validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)
   :type validate_meshes: boolean, (optional)
   :arg always_add_cache_reader: Always Add Cache Reader, Add cache modifiers and constraints to imported objects even if they are not animated so that they can be updated when reloading the Alembic archive
   :type always_add_cache_reader: boolean, (optional)
   :arg is_sequence: Is Sequence, Set to true if the cache is split into separate files
   :type is_sequence: boolean, (optional)
   :arg as_background_job: Run as Background Job, Enable this to run the export in the background, disable to block Blender while exporting. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
   :type as_background_job: boolean, (optional)

.. function:: append(*, filepath="", directory="", filename="", files=None, check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=True, filemode=1, display_type='DEFAULT', sort_method='', link=False, do_reuse_local_id=False, clear_asset_data=False, autoselect=True, active_collection=True, instance_collections=False, instance_object_data=True, set_fake=False, use_recursive=True)

   Append from a Library .blend file

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg filename: File Name, Name of the file
   :type filename: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg link: Link, Link the objects or data-blocks rather than appending
   :type link: boolean, (optional)
   :arg do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy
   :type do_reuse_local_id: boolean, (optional)
   :arg clear_asset_data: Clear Asset Data, Don't add asset meta-data or tags from the original data-block
   :type clear_asset_data: boolean, (optional)
   :arg autoselect: Select, Select new objects
   :type autoselect: boolean, (optional)
   :arg active_collection: Active Collection, Put new objects on the active collection
   :type active_collection: boolean, (optional)
   :arg instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
   :type instance_collections: boolean, (optional)
   :arg instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects
   :type instance_object_data: boolean, (optional)
   :arg set_fake: Fake User, Set "Fake User" for appended items (except objects and collections)
   :type set_fake: boolean, (optional)
   :arg use_recursive: Localize All, Localize all appended data, including those indirectly linked from other libraries
   :type use_recursive: boolean, (optional)

.. function:: batch_rename(*, data_type='OBJECT', data_source='SELECT', actions=None)

   Rename multiple items at once

   :arg data_type: Type, Type of data to rename
   :type data_type: enum in [``'OBJECT'``, ``'COLLECTION'``, ``'MATERIAL'``, ``'MESH'``, ``'CURVE'``, ``'META'``, ``'VOLUME'``, ``'GPENCIL'``, ``'ARMATURE'``, ``'LATTICE'``, ``'LIGHT'``, ``'LIGHT_PROBE'``, ``'CAMERA'``, ``'SPEAKER'``, ``'BONE'``, ``'NODE'``, ``'SEQUENCE_STRIP'``, ``'ACTION_CLIP'``, ``'SCENE'``, ``'BRUSH'``], (optional)
   :arg data_source: Source
   :type data_source: enum in [``'SELECT'``, ``'ALL'``], (optional)
   :arg actions: actions
   :type actions: :class:`bpy_prop_collection` of :class:`BatchRenameAction`, (optional)
   :File: `startup\bl_operators\wm.py\:3270 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L3270>`__


.. function:: blend_strings_utf8_validate()

   Check and fix all strings in current .blend file to be valid UTF-8 Unicode (needed for some old, 2.4x area files)

   :File: `startup\bl_operators\file.py\:289 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\file.py#L289>`__

.. function:: call_asset_shelf_popover(*, name="")

   Open a predefined asset shelf in a popup

   :arg name: Asset Shelf Name, Identifier of the asset shelf to display
   :type name: string, (optional, never None)

.. function:: call_menu(*, name="")

   Open a predefined menu

   :arg name: Name, Name of the menu
   :type name: string, (optional, never None)

.. function:: call_menu_pie(*, name="")

   Open a predefined pie menu

   :arg name: Name, Name of the pie menu
   :type name: string, (optional, never None)

.. function:: call_panel(*, name="", keep_open=True)

   Open a predefined panel

   :arg name: Name, Name of the menu
   :type name: string, (optional, never None)
   :arg keep_open: Keep Open
   :type keep_open: boolean, (optional)

.. function:: clear_recent_files(*, remove='ALL')

   Clear the recent files list

   :arg remove: Remove
   :type remove: enum in [``'ALL'``, ``'MISSING'``], (optional)

.. function:: collada_export(*, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=True, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', filter_glob="*.dae", prop_bc_export_ui_section='main', apply_modifiers=False, export_mesh_type=0, export_mesh_type_selection='view', export_global_forward_selection='Y', export_global_up_selection='Z', apply_global_orientation=False, selected=False, include_children=False, include_armatures=False, include_shapekeys=False, deform_bones_only=False, include_animations=True, include_all_actions=True, export_animation_type_selection='sample', sampling_rate=1, keep_smooth_curves=False, keep_keyframes=False, keep_flat_curves=False, active_uv_only=False, use_texture_copies=True, triangulate=True, use_object_instantiation=True, use_blender_profile=True, sort_by_name=False, export_object_transformation_type=0, export_object_transformation_type_selection='matrix', export_animation_transformation_type=0, export_animation_transformation_type_selection='matrix', open_sim=False, limit_precision=False, keep_bind_info=False)

   Save a Collada file (Deprecated)

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :type filter_glob: string, (optional, never None)
   :arg prop_bc_export_ui_section: Export Section, Only for User Interface organization

      * ``main``
        Main -- Data export section.
      * ``geometry``
        Geom -- Geometry export section.
      * ``armature``
        Arm -- Armature export section.
      * ``animation``
        Anim -- Animation export section.
      * ``collada``
        Extra -- Collada export section.
   :type prop_bc_export_ui_section: enum in [``'main'``, ``'geometry'``, ``'armature'``, ``'animation'``, ``'collada'``], (optional)
   :arg apply_modifiers: Apply Modifiers, Apply modifiers to exported mesh (non destructive)
   :type apply_modifiers: boolean, (optional)
   :arg export_mesh_type: Resolution, Modifier resolution for export
   :type export_mesh_type: int in [-inf, inf], (optional)
   :arg export_mesh_type_selection: Resolution, Modifier resolution for export

      * ``view``
        Viewport -- Apply modifier's viewport settings.
      * ``render``
        Render -- Apply modifier's render settings.
   :type export_mesh_type_selection: enum in [``'view'``, ``'render'``], (optional)
   :arg export_global_forward_selection: Global Forward Axis, Global Forward axis for export

      * ``X``
        X -- Global Forward is positive X Axis.
      * ``Y``
        Y -- Global Forward is positive Y Axis.
      * ``Z``
        Z -- Global Forward is positive Z Axis.
      * ``-X``
        -X -- Global Forward is negative X Axis.
      * ``-Y``
        -Y -- Global Forward is negative Y Axis.
      * ``-Z``
        -Z -- Global Forward is negative Z Axis.
   :type export_global_forward_selection: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'-X'``, ``'-Y'``, ``'-Z'``], (optional)
   :arg export_global_up_selection: Global Up Axis, Global Up axis for export

      * ``X``
        X -- Global UP is positive X Axis.
      * ``Y``
        Y -- Global UP is positive Y Axis.
      * ``Z``
        Z -- Global UP is positive Z Axis.
      * ``-X``
        -X -- Global UP is negative X Axis.
      * ``-Y``
        -Y -- Global UP is negative Y Axis.
      * ``-Z``
        -Z -- Global UP is negative Z Axis.
   :type export_global_up_selection: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'-X'``, ``'-Y'``, ``'-Z'``], (optional)
   :arg apply_global_orientation: Apply Global Orientation, Rotate all root objects to match the global orientation settings otherwise set the global orientation per Collada asset
   :type apply_global_orientation: boolean, (optional)
   :arg selected: Selection Only, Export only selected elements
   :type selected: boolean, (optional)
   :arg include_children: Include Children, Export all children of selected objects (even if not selected)
   :type include_children: boolean, (optional)
   :arg include_armatures: Include Armatures, Export related armatures (even if not selected)
   :type include_armatures: boolean, (optional)
   :arg include_shapekeys: Include Shape Keys, Export all Shape Keys from Mesh Objects
   :type include_shapekeys: boolean, (optional)
   :arg deform_bones_only: Deform Bones Only, Only export deforming bones with armatures
   :type deform_bones_only: boolean, (optional)
   :arg include_animations: Include Animations, Export animations if available (exporting animations will enforce the decomposition of node transforms into <translation> <rotation> and <scale> components)
   :type include_animations: boolean, (optional)
   :arg include_all_actions: Include all Actions, Export also unassigned actions (this allows you to export entire animation libraries for your character(s))
   :type include_all_actions: boolean, (optional)
   :arg export_animation_type_selection: Key Type, Type for exported animations (use sample keys or Curve keys)

      * ``sample``
        Samples -- Export Sampled points guided by sampling rate.
      * ``keys``
        Curves -- Export Curves (note: guided by curve keys).
   :type export_animation_type_selection: enum in [``'sample'``, ``'keys'``], (optional)
   :arg sampling_rate: Sampling Rate, The distance between 2 keyframes (1 to key every frame)
   :type sampling_rate: int in [1, inf], (optional)
   :arg keep_smooth_curves: Keep Smooth curves, Export also the curve handles (if available) (this does only work when the inverse parent matrix is the unity matrix, otherwise you may end up with odd results)
   :type keep_smooth_curves: boolean, (optional)
   :arg keep_keyframes: Keep Keyframes, Use existing keyframes as additional sample points (this helps when you want to keep manual tweaks)
   :type keep_keyframes: boolean, (optional)
   :arg keep_flat_curves: All Keyed Curves, Export also curves which have only one key or are totally flat
   :type keep_flat_curves: boolean, (optional)
   :arg active_uv_only: Only Selected UV Map, Export only the selected UV Map
   :type active_uv_only: boolean, (optional)
   :arg use_texture_copies: Copy, Copy textures to same folder where the .dae file is exported
   :type use_texture_copies: boolean, (optional)
   :arg triangulate: Triangulate, Export polygons (quads and n-gons) as triangles
   :type triangulate: boolean, (optional)
   :arg use_object_instantiation: Use Object Instances, Instantiate multiple Objects from same Data
   :type use_object_instantiation: boolean, (optional)
   :arg use_blender_profile: Use Blender Profile, Export additional Blender specific information (for material, shaders, bones, etc.)
   :type use_blender_profile: boolean, (optional)
   :arg sort_by_name: Sort by Object name, Sort exported data by Object name
   :type sort_by_name: boolean, (optional)
   :arg export_object_transformation_type: Transform, Object Transformation type for translation, scale and rotation
   :type export_object_transformation_type: int in [-inf, inf], (optional)
   :arg export_object_transformation_type_selection: Transform, Object Transformation type for translation, scale and rotation

      * ``matrix``
        Matrix -- Use <matrix> representation for exported transformations.
      * ``decomposed``
        Decomposed -- Use <rotate>, <translate> and <scale> representation for exported transformations.
   :type export_object_transformation_type_selection: enum in [``'matrix'``, ``'decomposed'``], (optional)
   :arg export_animation_transformation_type: Transform, Transformation type for translation, scale and rotation. Note: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab
   :type export_animation_transformation_type: int in [-inf, inf], (optional)
   :arg export_animation_transformation_type_selection: Transform, Transformation type for translation, scale and rotation. Note: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab

      * ``matrix``
        Matrix -- Use <matrix> representation for exported transformations.
      * ``decomposed``
        Decomposed -- Use <rotate>, <translate> and <scale> representation for exported transformations.
   :type export_animation_transformation_type_selection: enum in [``'matrix'``, ``'decomposed'``], (optional)
   :arg open_sim: Export to SL/OpenSim, Compatibility mode for Second Life, OpenSimulator and other compatible online worlds
   :type open_sim: boolean, (optional)
   :arg limit_precision: Limit Precision, Reduce the precision of the exported data to 6 digits
   :type limit_precision: boolean, (optional)
   :arg keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
   :type keep_bind_info: boolean, (optional)

.. function:: collada_import(*, filepath="", check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=True, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', filter_glob="*.dae", import_units=False, custom_normals=True, fix_orientation=False, find_chains=False, auto_connect=False, min_chain_length=0, keep_bind_info=False)

   Load a Collada file (Deprecated)

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :type filter_glob: string, (optional, never None)
   :arg import_units: Import Units, If disabled match import to Blender's current Unit settings, otherwise use the settings from the Imported scene
   :type import_units: boolean, (optional)
   :arg custom_normals: Custom Normals, Import custom normals, if available (otherwise Blender will compute them)
   :type custom_normals: boolean, (optional)
   :arg fix_orientation: Fix Leaf Bones, Fix Orientation of Leaf Bones (Collada does only support Joints)
   :type fix_orientation: boolean, (optional)
   :arg find_chains: Find Bone Chains, Find best matching Bone Chains and ensure bones in chain are connected
   :type find_chains: boolean, (optional)
   :arg auto_connect: Auto Connect, Set use_connect for parent bones which have exactly one child bone
   :type auto_connect: boolean, (optional)
   :arg min_chain_length: Minimum Chain Length, When searching Bone Chains disregard chains of length below this value
   :type min_chain_length: int in [0, inf], (optional)
   :arg keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
   :type keep_bind_info: boolean, (optional)

.. function:: collection_export_all()

   Invoke all configured exporters for all collections

.. function:: console_toggle()

   Toggle System Console

.. function:: context_collection_boolean_set(*, data_path_iter="", data_path_item="", type='TOGGLE')

   Set boolean values for a collection of items

   :arg data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
   :type data_path_iter: string, (optional, never None)
   :arg data_path_item: data_path_item, The data path from each iterable to the value (int or float)
   :type data_path_item: string, (optional, never None)
   :arg type: Type
   :type type: enum in [``'TOGGLE'``, ``'ENABLE'``, ``'DISABLE'``], (optional)
   :File: `startup\bl_operators\wm.py\:875 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L875>`__


.. function:: context_cycle_array(*, data_path="", reverse=False)

   Set a context array value (useful for cycling the active mesh edit mode)

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg reverse: Reverse, Cycle backwards
   :type reverse: boolean, (optional)
   :File: `startup\bl_operators\wm.py\:673 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L673>`__


.. function:: context_cycle_enum(*, data_path="", reverse=False, wrap=False)

   Toggle a context value

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg reverse: Reverse, Cycle backwards
   :type reverse: boolean, (optional)
   :arg wrap: Wrap, Wrap back to the first/last values
   :type wrap: boolean, (optional)
   :File: `startup\bl_operators\wm.py\:624 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L624>`__


.. function:: context_cycle_int(*, data_path="", reverse=False, wrap=False)

   Set a context value (useful for cycling active material, shape keys, groups, etc.)

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg reverse: Reverse, Cycle backwards
   :type reverse: boolean, (optional)
   :arg wrap: Wrap, Wrap back to the first/last values
   :type wrap: boolean, (optional)
   :File: `startup\bl_operators\wm.py\:584 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L584>`__


.. function:: context_menu_enum(*, data_path="")

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:703 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L703>`__


.. function:: context_modal_mouse(*, data_path_iter="", data_path_item="", header_text="", input_scale=0.01, invert=False, initial_x=0)

   Adjust arbitrary values with mouse input

   :arg data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
   :type data_path_iter: string, (optional, never None)
   :arg data_path_item: data_path_item, The data path from each iterable to the value (int or float)
   :type data_path_item: string, (optional, never None)
   :arg header_text: Header Text, Text to display in header during scale
   :type header_text: string, (optional, never None)
   :arg input_scale: input_scale, Scale the mouse movement by this value before applying the delta
   :type input_scale: float in [-inf, inf], (optional)
   :arg invert: invert, Invert the mouse input
   :type invert: boolean, (optional)
   :arg initial_x: initial_x
   :type initial_x: int in [-inf, inf], (optional)
   :File: `startup\bl_operators\wm.py\:1014 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L1014>`__


.. function:: context_pie_enum(*, data_path="")

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:735 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L735>`__


.. function:: context_scale_float(*, data_path="", value=1.0)

   Scale a float context value

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg value: Value, Assign value
   :type value: float in [-inf, inf], (optional)
   :File: `startup\bl_operators\wm.py\:338 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L338>`__


.. function:: context_scale_int(*, data_path="", value=1.0, always_step=True)

   Scale an int context value

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg value: Value, Assign value
   :type value: float in [-inf, inf], (optional)
   :arg always_step: Always Step, Always adjust the value by a minimum of 1 when 'value' is not 1.0
   :type always_step: boolean, (optional)
   :File: `startup\bl_operators\wm.py\:376 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L376>`__


.. function:: context_set_boolean(*, data_path="", value=True)

   Set a context value

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg value: Value, Assignment value
   :type value: boolean, (optional)
   :File: `startup\bl_operators\wm.py\:267 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L267>`__


.. function:: context_set_enum(*, data_path="", value="")

   Set a context value

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg value: Value, Assignment value (as a string)
   :type value: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:267 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L267>`__


.. function:: context_set_float(*, data_path="", value=0.0, relative=False)

   Set a context value

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg value: Value, Assignment value
   :type value: float in [-inf, inf], (optional)
   :arg relative: Relative, Apply relative to the current value (delta)
   :type relative: boolean, (optional)
   :File: `startup\bl_operators\wm.py\:267 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L267>`__


.. function:: context_set_id(*, data_path="", value="")

   Set a context value to an ID data-block

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg value: Value, Assign value
   :type value: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:817 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L817>`__


.. function:: context_set_int(*, data_path="", value=0, relative=False)

   Set a context value

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg value: Value, Assign value
   :type value: int in [-inf, inf], (optional)
   :arg relative: Relative, Apply relative to the current value (delta)
   :type relative: boolean, (optional)
   :File: `startup\bl_operators\wm.py\:267 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L267>`__


.. function:: context_set_string(*, data_path="", value="")

   Set a context value

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg value: Value, Assign value
   :type value: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:267 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L267>`__


.. function:: context_set_value(*, data_path="", value="")

   Set a context value

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg value: Value, Assignment value (as a string)
   :type value: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:480 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L480>`__


.. function:: context_toggle(*, data_path="", module="")

   Toggle a context value

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg module: Module, Optionally override the context with a module
   :type module: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:504 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L504>`__


.. function:: context_toggle_enum(*, data_path="", value_1="", value_2="")

   Toggle a context value

   :arg data_path: Context Attributes, Context data-path (expanded using visible windows in the current .blend file)
   :type data_path: string, (optional, never None)
   :arg value_1: Value, Toggle enum
   :type value_1: string, (optional, never None)
   :arg value_2: Value, Toggle enum
   :type value_2: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:545 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L545>`__


.. function:: debug_menu(*, debug_value=0)

   Open a popup to set the debug level

   :arg debug_value: Debug Value
   :type debug_value: int in [-32768, 32767], (optional)

.. function:: doc_view(*, doc_id="")

   Open online reference docs in a web browser

   :arg doc_id: Doc ID
   :type doc_id: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:1358 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L1358>`__


.. function:: doc_view_manual(*, doc_id="")

   Load online manual

   :arg doc_id: Doc ID
   :type doc_id: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:1331 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L1331>`__


.. function:: doc_view_manual_ui_context()

   View a context based online manual in a web browser

.. function:: drop_blend_file(*, filepath="")

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:3633 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L3633>`__


.. function:: drop_import_file(*, directory="", files=None)

   Operator that allows file handlers to receive file drops

   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)

.. function:: fbx_import(*, filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', global_scale=1.0, import_colors='SRGB', use_custom_normals=True, use_custom_props=True, use_custom_props_enum_as_string=True, import_subdivision=False, ignore_leaf_bones=False, validate_meshes=True, use_anim=True, anim_offset=1.0, filter_glob="*.fbx")

   Import FBX file into current scene

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg global_scale: Scale
   :type global_scale: float in [1e-06, 1e+06], (optional)
   :arg import_colors: Vertex Colors, Import vertex color attributes

      * ``NONE``
        None -- Do not import color attributes.
      * ``SRGB``
        sRGB -- Vertex colors in the file are in sRGB color space.
      * ``LINEAR``
        Linear -- Vertex colors in the file are in linear color space.
   :type import_colors: enum in [``'NONE'``, ``'SRGB'``, ``'LINEAR'``], (optional)
   :arg use_custom_normals: Custom Normals, Import custom normals, if available (otherwise Blender will compute them)
   :type use_custom_normals: boolean, (optional)
   :arg use_custom_props: Custom Properties, Import user properties as custom properties
   :type use_custom_props: boolean, (optional)
   :arg use_custom_props_enum_as_string: Enums As Strings, Store custom property enumeration values as strings
   :type use_custom_props_enum_as_string: boolean, (optional)
   :arg import_subdivision: Subdivision Data, Import FBX subdivision information as subdivision surface modifiers
   :type import_subdivision: boolean, (optional)
   :arg ignore_leaf_bones: Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone)
   :type ignore_leaf_bones: boolean, (optional)
   :arg validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)
   :type validate_meshes: boolean, (optional)
   :arg use_anim: Import Animation, Import FBX animation
   :type use_anim: boolean, (optional)
   :arg anim_offset: Offset, Offset to apply to animation timestamps, in frames
   :type anim_offset: float in [-1e+06, 1e+06], (optional)
   :arg filter_glob: Extension Filter
   :type filter_glob: string, (optional, never None)

.. function:: grease_pencil_export_pdf(*, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=True, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', use_fill=True, selected_object_type='ACTIVE', frame_mode='ACTIVE', stroke_sample=0.0, use_uniform_width=False)

   Export Grease Pencil to PDF

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg use_fill: Fill, Export strokes with fill enabled
   :type use_fill: boolean, (optional)
   :arg selected_object_type: Object, Which objects to include in the export

      * ``ACTIVE``
        Active -- Include only the active object.
      * ``SELECTED``
        Selected -- Include selected objects.
      * ``VISIBLE``
        Visible -- Include all visible objects.
   :type selected_object_type: enum in [``'ACTIVE'``, ``'SELECTED'``, ``'VISIBLE'``], (optional)
   :arg frame_mode: Frames, Which frames to include in the export

      * ``ACTIVE``
        Active -- Include only active frame.
      * ``SELECTED``
        Selected -- Include selected frames.
      * ``SCENE``
        Scene -- Include all scene frames.
   :type frame_mode: enum in [``'ACTIVE'``, ``'SELECTED'``, ``'SCENE'``], (optional)
   :arg stroke_sample: Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling
   :type stroke_sample: float in [0, 100], (optional)
   :arg use_uniform_width: Uniform Width, Export strokes with uniform width
   :type use_uniform_width: boolean, (optional)

.. function:: grease_pencil_export_svg(*, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=True, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', use_fill=True, selected_object_type='ACTIVE', frame_mode='ACTIVE', stroke_sample=0.0, use_uniform_width=False, use_clip_camera=False)

   Export Grease Pencil to SVG

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg use_fill: Fill, Export strokes with fill enabled
   :type use_fill: boolean, (optional)
   :arg selected_object_type: Object, Which objects to include in the export

      * ``ACTIVE``
        Active -- Include only the active object.
      * ``SELECTED``
        Selected -- Include selected objects.
      * ``VISIBLE``
        Visible -- Include all visible objects.
   :type selected_object_type: enum in [``'ACTIVE'``, ``'SELECTED'``, ``'VISIBLE'``], (optional)
   :arg frame_mode: Frames, Which frames to include in the export

      * ``ACTIVE``
        Active -- Include only active frame.
      * ``SELECTED``
        Selected -- Include selected frames.
      * ``SCENE``
        Scene -- Include all scene frames.
   :type frame_mode: enum in [``'ACTIVE'``, ``'SELECTED'``, ``'SCENE'``], (optional)
   :arg stroke_sample: Sampling, Precision of stroke sampling. Low values mean a more precise result, and zero disables sampling
   :type stroke_sample: float in [0, 100], (optional)
   :arg use_uniform_width: Uniform Width, Export strokes with uniform width
   :type use_uniform_width: boolean, (optional)
   :arg use_clip_camera: Clip Camera, Clip drawings to camera size when exporting in camera view
   :type use_clip_camera: boolean, (optional)

.. function:: grease_pencil_import_svg(*, filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=True, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='', resolution=10, scale=10.0, use_scene_unit=False)

   Import SVG into Grease Pencil

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg relative_path: Relative Path, Select the file relative to the blend file
   :type relative_path: boolean, (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg resolution: Resolution, Resolution of the generated strokes
   :type resolution: int in [1, 100000], (optional)
   :arg scale: Scale, Scale of the final strokes
   :type scale: float in [1e-06, 1e+06], (optional)
   :arg use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
   :type use_scene_unit: boolean, (optional)

.. function:: id_linked_relocate(*, id_session_uid=0, filepath="", directory="", filename="", check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=True, filemode=1, relative_path=True, display_type='DEFAULT', sort_method='', link=True, do_reuse_local_id=False, clear_asset_data=False, autoselect=True, active_collection=False, instance_collections=False, instance_object_data=False)

   Relocate a linked ID, i.e. select another ID to link, and remap its local usages to that newly linked data-block). Currently only designed as an internal operator, not directly exposed to the user

   :arg id_session_uid: Linked ID Session UID, Unique runtime identifier for the linked ID to relocate
   :type id_session_uid: int in [0, inf], (optional)
   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg filename: File Name, Name of the file
   :type filename: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg relative_path: Relative Path, Select the file relative to the blend file
   :type relative_path: boolean, (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg link: Link, Link the objects or data-blocks rather than appending
   :type link: boolean, (optional)
   :arg do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy
   :type do_reuse_local_id: boolean, (optional)
   :arg clear_asset_data: Clear Asset Data, Don't add asset meta-data or tags from the original data-block
   :type clear_asset_data: boolean, (optional)
   :arg autoselect: Select, Select new objects
   :type autoselect: boolean, (optional)
   :arg active_collection: Active Collection, Put new objects on the active collection
   :type active_collection: boolean, (optional)
   :arg instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
   :type instance_collections: boolean, (optional)
   :arg instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects
   :type instance_object_data: boolean, (optional)

.. function:: interface_theme_preset_add(*, name="", remove_name=False, remove_active=False)

   Add a custom theme to the preset list

   :arg name: Name, Name of the preset, used to make the path name
   :type name: string, (optional, never None)
   :arg remove_name: remove_name
   :type remove_name: boolean, (optional)
   :arg remove_active: remove_active
   :type remove_active: boolean, (optional)
   :File: `startup\bl_operators\presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\presets.py#L119>`__


.. function:: interface_theme_preset_remove(*, name="", remove_name=False, remove_active=True)

   Remove a custom theme from the preset list

   :arg name: Name, Name of the preset, used to make the path name
   :type name: string, (optional, never None)
   :arg remove_name: remove_name
   :type remove_name: boolean, (optional)
   :arg remove_active: remove_active
   :type remove_active: boolean, (optional)
   :File: `startup\bl_operators\presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\presets.py#L119>`__


.. function:: interface_theme_preset_save(*, name="", remove_name=False, remove_active=True)

   Save a custom theme in the preset list

   :arg name: Name, Name of the preset, used to make the path name
   :type name: string, (optional, never None)
   :arg remove_name: remove_name
   :type remove_name: boolean, (optional)
   :arg remove_active: remove_active
   :type remove_active: boolean, (optional)
   :File: `startup\bl_operators\presets.py\:711 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\presets.py#L711>`__


.. function:: keyconfig_preset_add(*, name="", remove_name=False, remove_active=False)

   Add a custom keymap configuration to the preset list

   :arg name: Name, Name of the preset, used to make the path name
   :type name: string, (optional, never None)
   :arg remove_name: remove_name
   :type remove_name: boolean, (optional)
   :arg remove_active: remove_active
   :type remove_active: boolean, (optional)
   :File: `startup\bl_operators\presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\presets.py#L119>`__


.. function:: keyconfig_preset_remove(*, name="", remove_name=False, remove_active=True)

   Remove a custom keymap configuration from the preset list

   :arg name: Name, Name of the preset, used to make the path name
   :type name: string, (optional, never None)
   :arg remove_name: remove_name
   :type remove_name: boolean, (optional)
   :arg remove_active: remove_active
   :type remove_active: boolean, (optional)
   :File: `startup\bl_operators\presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\presets.py#L119>`__


.. function:: lib_reload(*, library="", filepath="", directory="", filename="", hide_props_region=True, check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='')

   Reload the given library

   :arg library: Library, Library to reload
   :type library: string, (optional, never None)
   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg filename: File Name, Name of the file
   :type filename: string, (optional, never None)
   :arg hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
   :type hide_props_region: boolean, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg relative_path: Relative Path, Select the file relative to the blend file
   :type relative_path: boolean, (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)

.. function:: lib_relocate(*, library="", filepath="", directory="", filename="", files=None, hide_props_region=True, check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='')

   Relocate the given library to one or several others

   :arg library: Library, Library to relocate
   :type library: string, (optional, never None)
   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg filename: File Name, Name of the file
   :type filename: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
   :type hide_props_region: boolean, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg relative_path: Relative Path, Select the file relative to the blend file
   :type relative_path: boolean, (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)

.. function:: link(*, filepath="", directory="", filename="", files=None, check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=True, filemode=1, relative_path=True, display_type='DEFAULT', sort_method='', link=True, do_reuse_local_id=False, clear_asset_data=False, autoselect=True, active_collection=True, instance_collections=True, instance_object_data=True)

   Link from a Library .blend file

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg filename: File Name, Name of the file
   :type filename: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg relative_path: Relative Path, Select the file relative to the blend file
   :type relative_path: boolean, (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg link: Link, Link the objects or data-blocks rather than appending
   :type link: boolean, (optional)
   :arg do_reuse_local_id: Re-Use Local Data, Try to re-use previously matching appended data-blocks instead of appending a new copy
   :type do_reuse_local_id: boolean, (optional)
   :arg clear_asset_data: Clear Asset Data, Don't add asset meta-data or tags from the original data-block
   :type clear_asset_data: boolean, (optional)
   :arg autoselect: Select, Select new objects
   :type autoselect: boolean, (optional)
   :arg active_collection: Active Collection, Put new objects on the active collection
   :type active_collection: boolean, (optional)
   :arg instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
   :type instance_collections: boolean, (optional)
   :arg instance_object_data: Instance Object Data, Create instances for object data which are not referenced by any objects
   :type instance_object_data: boolean, (optional)

.. function:: memory_statistics()

   Print memory statistics to the console

.. function:: obj_export(*, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', export_animation=False, start_frame=-2147483648, end_frame=2147483647, forward_axis='NEGATIVE_Z', up_axis='Y', global_scale=1.0, apply_modifiers=True, export_eval_mode='DAG_EVAL_VIEWPORT', export_selected_objects=False, export_uv=True, export_normals=True, export_colors=False, export_materials=True, export_pbr_extensions=False, path_mode='AUTO', export_triangulated_mesh=False, export_curves_as_nurbs=False, export_object_groups=False, export_material_groups=False, export_vertex_groups=False, export_smooth_groups=False, smooth_group_bitflags=False, filter_glob="*.obj;*.mtl", collection="")

   Save the scene to a Wavefront OBJ file

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg export_animation: Export Animation, Export multiple frames instead of the current frame only
   :type export_animation: boolean, (optional)
   :arg start_frame: Start Frame, The first frame to be exported
   :type start_frame: int in [-inf, inf], (optional)
   :arg end_frame: End Frame, The last frame to be exported
   :type end_frame: int in [-inf, inf], (optional)
   :arg forward_axis: Forward Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type forward_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg up_axis: Up Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type up_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
   :type global_scale: float in [0.0001, 10000], (optional)
   :arg apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
   :type apply_modifiers: boolean, (optional)
   :arg export_eval_mode: Object Properties, Determines properties like object visibility, modifiers etc., where they differ for Render and Viewport

      * ``DAG_EVAL_RENDER``
        Render -- Export objects as they appear in render.
      * ``DAG_EVAL_VIEWPORT``
        Viewport -- Export objects as they appear in the viewport.
   :type export_eval_mode: enum in [``'DAG_EVAL_RENDER'``, ``'DAG_EVAL_VIEWPORT'``], (optional)
   :arg export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
   :type export_selected_objects: boolean, (optional)
   :arg export_uv: Export UVs
   :type export_uv: boolean, (optional)
   :arg export_normals: Export Normals, Export per-face normals if the face is flat-shaded, per-face-corner normals if smooth-shaded
   :type export_normals: boolean, (optional)
   :arg export_colors: Export Colors, Export per-vertex colors
   :type export_colors: boolean, (optional)
   :arg export_materials: Export Materials, Export MTL library. There must be a Principled-BSDF node for image textures to be exported to the MTL file
   :type export_materials: boolean, (optional)
   :arg export_pbr_extensions: Export Materials with PBR Extensions, Export MTL library using PBR extensions (roughness, metallic, sheen, coat, anisotropy, transmission)
   :type export_pbr_extensions: boolean, (optional)
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
        Strip -- Write filename only.
      * ``COPY``
        Copy -- Copy the file to the destination path.
   :type path_mode: enum in [``'AUTO'``, ``'ABSOLUTE'``, ``'RELATIVE'``, ``'MATCH'``, ``'STRIP'``, ``'COPY'``], (optional)
   :arg export_triangulated_mesh: Export Triangulated Mesh, All ngons with four or more vertices will be triangulated. Meshes in the scene will not be affected. Behaves like Triangulate Modifier with ngon-method: "Beauty", quad-method: "Shortest Diagonal", min vertices: 4
   :type export_triangulated_mesh: boolean, (optional)
   :arg export_curves_as_nurbs: Export Curves as NURBS, Export curves in parametric form instead of exporting as mesh
   :type export_curves_as_nurbs: boolean, (optional)
   :arg export_object_groups: Export Object Groups, Append mesh name to object name, separated by a '_'
   :type export_object_groups: boolean, (optional)
   :arg export_material_groups: Export Material Groups, Generate an OBJ group for each part of a geometry using a different material
   :type export_material_groups: boolean, (optional)
   :arg export_vertex_groups: Export Vertex Groups, Export the name of the vertex group of a face. It is approximated by choosing the vertex group with the most members among the vertices of a face
   :type export_vertex_groups: boolean, (optional)
   :arg export_smooth_groups: Export Smooth Groups, Generate smooth groups identifiers for each group of smooth faces, as unique integer values by default
   :type export_smooth_groups: boolean, (optional)
   :arg smooth_group_bitflags: Bitflags Smooth Groups, If exporting smoothgroups, generate 'bitflags' values for the groups, instead of unique integer values. The same bitflag value can be re-used for different groups of smooth faces, as long as they have no common sharp edges or vertices
   :type smooth_group_bitflags: boolean, (optional)
   :arg filter_glob: Extension Filter
   :type filter_glob: string, (optional, never None)
   :arg collection: Collection
   :type collection: string, (optional, never None)

.. function:: obj_import(*, filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', global_scale=1.0, clamp_size=0.0, forward_axis='NEGATIVE_Z', up_axis='Y', use_split_objects=True, use_split_groups=False, import_vertex_groups=False, validate_meshes=True, close_spline_loops=True, collection_separator="", filter_glob="*.obj;*.mtl")

   Load a Wavefront OBJ scene

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
   :type global_scale: float in [0.0001, 10000], (optional)
   :arg clamp_size: Clamp Bounding Box, Resize the objects to keep bounding box under this value. Value 0 disables clamping
   :type clamp_size: float in [0, 1000], (optional)
   :arg forward_axis: Forward Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type forward_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg up_axis: Up Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type up_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg use_split_objects: Split By Object, Import each OBJ 'o' as a separate object
   :type use_split_objects: boolean, (optional)
   :arg use_split_groups: Split By Group, Import each OBJ 'g' as a separate object
   :type use_split_groups: boolean, (optional)
   :arg import_vertex_groups: Vertex Groups, Import OBJ groups as vertex groups
   :type import_vertex_groups: boolean, (optional)
   :arg validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)
   :type validate_meshes: boolean, (optional)
   :arg close_spline_loops: Detect Cyclic Curves, Join curve endpoints if overlapping control points are detected (if disabled, no curves will be cyclic)
   :type close_spline_loops: boolean, (optional)
   :arg collection_separator: Path Separator, Character used to separate objects name into hierarchical structure
   :type collection_separator: string, (optional, never None)
   :arg filter_glob: Extension Filter
   :type filter_glob: string, (optional, never None)

.. function:: open_mainfile(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', load_ui=True, use_scripts=False, display_file_selector=True, state=0)

   Open a Blender file

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
   :type hide_props_region: boolean, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg load_ui: Load UI, Load user interface setup in the .blend file
   :type load_ui: boolean, (optional)
   :arg use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
   :type use_scripts: boolean, (optional)
   :arg display_file_selector: Display File Selector
   :type display_file_selector: boolean, (optional)
   :arg state: State
   :type state: int in [-inf, inf], (optional)

.. function:: operator_cheat_sheet()

   List all the operators in a text-block, useful for scripting

   :File: `startup\bl_operators\wm.py\:2246 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2246>`__

.. function:: operator_defaults()

   Set the active operator to its default values

.. function:: operator_pie_enum(*, data_path="", prop_string="")

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg data_path: Operator, Operator name (in Python as string)
   :type data_path: string, (optional, never None)
   :arg prop_string: Property, Property name (as a string)
   :type prop_string: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:777 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L777>`__


.. function:: operator_preset_add(*, name="", remove_name=False, remove_active=False, operator="")

   Add or remove an Operator Preset

   :arg name: Name, Name of the preset, used to make the path name
   :type name: string, (optional, never None)
   :arg remove_name: remove_name
   :type remove_name: boolean, (optional)
   :arg remove_active: remove_active
   :type remove_active: boolean, (optional)
   :arg operator: Operator
   :type operator: string, (optional, never None)
   :File: `startup\bl_operators\presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\presets.py#L119>`__


.. function:: operator_presets_cleanup(*, operator="", properties=None)

   Remove outdated operator properties from presets that may cause problems

   :arg operator: operator
   :type operator: string, (optional, never None)
   :arg properties: properties
   :type properties: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :File: `startup\bl_operators\presets.py\:924 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\presets.py#L924>`__


.. function:: owner_disable(*, owner_id="")

   Disable add-on for workspace

   :arg owner_id: UI Tag
   :type owner_id: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:2294 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2294>`__


.. function:: owner_enable(*, owner_id="")

   Enable add-on for workspace

   :arg owner_id: UI Tag
   :type owner_id: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:2279 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2279>`__


.. function:: path_open(*, filepath="")

   Open a path in a file browser

   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:1167 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L1167>`__


.. function:: ply_export(*, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', forward_axis='Y', up_axis='Z', global_scale=1.0, apply_modifiers=True, export_selected_objects=False, collection="", export_uv=True, export_normals=False, export_colors='SRGB', export_attributes=True, export_triangulated_mesh=False, ascii_format=False, filter_glob="*.ply")

   Save the scene to a PLY file

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg forward_axis: Forward Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type forward_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg up_axis: Up Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type up_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
   :type global_scale: float in [0.0001, 10000], (optional)
   :arg apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
   :type apply_modifiers: boolean, (optional)
   :arg export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
   :type export_selected_objects: boolean, (optional)
   :arg collection: Source Collection, Export only objects from this collection (and its children)
   :type collection: string, (optional, never None)
   :arg export_uv: Export UVs
   :type export_uv: boolean, (optional)
   :arg export_normals: Export Vertex Normals, Export specific vertex normals if available, export calculated normals otherwise
   :type export_normals: boolean, (optional)
   :arg export_colors: Export Vertex Colors, Export vertex color attributes

      * ``NONE``
        None -- Do not import/export color attributes.
      * ``SRGB``
        sRGB -- Vertex colors in the file are in sRGB color space.
      * ``LINEAR``
        Linear -- Vertex colors in the file are in linear color space.
   :type export_colors: enum in [``'NONE'``, ``'SRGB'``, ``'LINEAR'``], (optional)
   :arg export_attributes: Export Vertex Attributes, Export custom vertex attributes
   :type export_attributes: boolean, (optional)
   :arg export_triangulated_mesh: Export Triangulated Mesh, All ngons with four or more vertices will be triangulated. Meshes in the scene will not be affected. Behaves like Triangulate Modifier with ngon-method: "Beauty", quad-method: "Shortest Diagonal", min vertices: 4
   :type export_triangulated_mesh: boolean, (optional)
   :arg ascii_format: ASCII Format, Export file in ASCII format, export as binary otherwise
   :type ascii_format: boolean, (optional)
   :arg filter_glob: Extension Filter
   :type filter_glob: string, (optional, never None)

.. function:: ply_import(*, filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', global_scale=1.0, use_scene_unit=False, forward_axis='Y', up_axis='Z', merge_verts=False, import_colors='SRGB', import_attributes=True, filter_glob="*.ply")

   Import an PLY file as an object

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg global_scale: Scale
   :type global_scale: float in [1e-06, 1e+06], (optional)
   :arg use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
   :type use_scene_unit: boolean, (optional)
   :arg forward_axis: Forward Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type forward_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg up_axis: Up Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type up_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg merge_verts: Merge Vertices, Merges vertices by distance
   :type merge_verts: boolean, (optional)
   :arg import_colors: Vertex Colors, Import vertex color attributes

      * ``NONE``
        None -- Do not import/export color attributes.
      * ``SRGB``
        sRGB -- Vertex colors in the file are in sRGB color space.
      * ``LINEAR``
        Linear -- Vertex colors in the file are in linear color space.
   :type import_colors: enum in [``'NONE'``, ``'SRGB'``, ``'LINEAR'``], (optional)
   :arg import_attributes: Vertex Attributes, Import custom vertex attributes
   :type import_attributes: boolean, (optional)
   :arg filter_glob: Extension Filter
   :type filter_glob: string, (optional, never None)

.. function:: previews_batch_clear(*, files=None, directory="", filter_blender=True, filter_folder=True, use_scenes=True, use_collections=True, use_objects=True, use_intern_data=True, use_trusted=False, use_backups=True)

   Clear selected .blend file's previews

   :arg files: files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg directory: directory
   :type directory: string, (optional, never None)
   :arg filter_blender: filter_blender
   :type filter_blender: boolean, (optional)
   :arg filter_folder: filter_folder
   :type filter_folder: boolean, (optional)
   :arg use_scenes: Scenes, Clear scenes' previews
   :type use_scenes: boolean, (optional)
   :arg use_collections: Collections, Clear collections' previews
   :type use_collections: boolean, (optional)
   :arg use_objects: Objects, Clear objects' previews
   :type use_objects: boolean, (optional)
   :arg use_intern_data: Materials & Textures, Clear 'internal' previews (materials, textures, images, etc.)
   :type use_intern_data: boolean, (optional)
   :arg use_trusted: Trusted Blend Files, Enable Python evaluation for selected files
   :type use_trusted: boolean, (optional)
   :arg use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews
   :type use_backups: boolean, (optional)
   :File: `startup\bl_operators\file.py\:204 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\file.py#L204>`__


.. function:: previews_batch_generate(*, files=None, directory="", filter_blender=True, filter_folder=True, use_scenes=True, use_collections=True, use_objects=True, use_intern_data=True, use_trusted=False, use_backups=True)

   Generate selected .blend file's previews

   :arg files: Collection of file paths with common ``directory`` root
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg directory: Root path of all files listed in ``files`` collection
   :type directory: string, (optional, never None)
   :arg filter_blender: Show Blender files in the File Browser
   :type filter_blender: boolean, (optional)
   :arg filter_folder: Show folders in the File Browser
   :type filter_folder: boolean, (optional)
   :arg use_scenes: Scenes, Generate scenes' previews
   :type use_scenes: boolean, (optional)
   :arg use_collections: Collections, Generate collections' previews
   :type use_collections: boolean, (optional)
   :arg use_objects: Objects, Generate objects' previews
   :type use_objects: boolean, (optional)
   :arg use_intern_data: Materials & Textures, Generate 'internal' previews (materials, textures, images, etc.)
   :type use_intern_data: boolean, (optional)
   :arg use_trusted: Trusted Blend Files, Enable Python evaluation for selected files
   :type use_trusted: boolean, (optional)
   :arg use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews
   :type use_backups: boolean, (optional)
   :File: `startup\bl_operators\file.py\:95 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\file.py#L95>`__


.. function:: previews_clear(*, id_type={})

   Clear data-block previews (only for some types like objects, materials, textures, etc.)

   :arg id_type: Data-Block Type, Which data-block previews to clear

      * ``ALL``
        All Types.
      * ``GEOMETRY``
        All Geometry Types -- Clear previews for scenes, collections and objects.
      * ``SHADING``
        All Shading Types -- Clear previews for materials, lights, worlds, textures and images.
      * ``SCENE``
        Scenes.
      * ``COLLECTION``
        Collections.
      * ``OBJECT``
        Objects.
      * ``MATERIAL``
        Materials.
      * ``LIGHT``
        Lights.
      * ``WORLD``
        Worlds.
      * ``TEXTURE``
        Textures.
      * ``IMAGE``
        Images.
   :type id_type: enum set in {``'ALL'``, ``'GEOMETRY'``, ``'SHADING'``, ``'SCENE'``, ``'COLLECTION'``, ``'OBJECT'``, ``'MATERIAL'``, ``'LIGHT'``, ``'WORLD'``, ``'TEXTURE'``, ``'IMAGE'``}, (optional)

.. function:: previews_ensure()

   Ensure data-block previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.)

.. function:: properties_add(*, data_path="")

   Add your own property to the data-block

   :arg data_path: Property Edit, Property data_path edit
   :type data_path: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:2128 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2128>`__


.. function:: properties_context_change(*, context="")

   Jump to a different tab inside the properties editor

   :arg context: Context
   :type context: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:2171 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2171>`__


.. function:: properties_edit(*, data_path="", property_name="", property_type='FLOAT', is_overridable_library=False, description="", use_soft_limits=False, array_length=3, default_int=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), min_int=-10000, max_int=10000, soft_min_int=-10000, soft_max_int=10000, step_int=1, default_bool=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False), default_float=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), min_float=-10000.0, max_float=-10000.0, soft_min_float=-10000.0, soft_max_float=-10000.0, precision=3, step_float=0.1, subtype='', default_string="", id_type='OBJECT', eval_string="")

   Change a custom property's type, or adjust how it is displayed in the interface

   :arg data_path: Property Edit, Property data_path edit
   :type data_path: string, (optional, never None)
   :arg property_name: Property Name, Property name edit
   :type property_name: string, (optional, never None)
   :arg property_type: Type

      * ``FLOAT``
        Float -- A single floating-point value.
      * ``FLOAT_ARRAY``
        Float Array -- An array of floating-point values.
      * ``INT``
        Integer -- A single integer.
      * ``INT_ARRAY``
        Integer Array -- An array of integers.
      * ``BOOL``
        Boolean -- A true or false value.
      * ``BOOL_ARRAY``
        Boolean Array -- An array of true or false values.
      * ``STRING``
        String -- A string value.
      * ``DATA_BLOCK``
        Data-Block -- A data-block value.
      * ``PYTHON``
        Python -- Edit a Python value directly, for unsupported property types.
   :type property_type: enum in [``'FLOAT'``, ``'FLOAT_ARRAY'``, ``'INT'``, ``'INT_ARRAY'``, ``'BOOL'``, ``'BOOL_ARRAY'``, ``'STRING'``, ``'DATA_BLOCK'``, ``'PYTHON'``], (optional)
   :arg is_overridable_library: Library Overridable, Allow the property to be overridden when the data-block is linked
   :type is_overridable_library: boolean, (optional)
   :arg description: Description
   :type description: string, (optional, never None)
   :arg use_soft_limits: Soft Limits, Limits the Property Value slider to a range, values outside the range must be inputted numerically
   :type use_soft_limits: boolean, (optional)
   :arg array_length: Array Length
   :type array_length: int in [1, 32], (optional)
   :arg default_int: Default Value
   :type default_int: int array of 32 items in [-inf, inf], (optional)
   :arg min_int: Min
   :type min_int: int in [-inf, inf], (optional)
   :arg max_int: Max
   :type max_int: int in [-inf, inf], (optional)
   :arg soft_min_int: Soft Min
   :type soft_min_int: int in [-inf, inf], (optional)
   :arg soft_max_int: Soft Max
   :type soft_max_int: int in [-inf, inf], (optional)
   :arg step_int: Step
   :type step_int: int in [1, inf], (optional)
   :arg default_bool: Default Value
   :type default_bool: boolean array of 32 items, (optional)
   :arg default_float: Default Value
   :type default_float: float array of 32 items in [-inf, inf], (optional)
   :arg min_float: Min
   :type min_float: float in [-inf, inf], (optional)
   :arg max_float: Max
   :type max_float: float in [-inf, inf], (optional)
   :arg soft_min_float: Soft Min
   :type soft_min_float: float in [-inf, inf], (optional)
   :arg soft_max_float: Soft Max
   :type soft_max_float: float in [-inf, inf], (optional)
   :arg precision: Precision
   :type precision: int in [0, 8], (optional)
   :arg step_float: Step
   :type step_float: float in [0.001, inf], (optional)
   :arg subtype: Subtype
   :type subtype: enum in [], (optional)
   :arg default_string: Default Value
   :type default_string: string, (optional, never None)
   :arg id_type: ID Type
   :type id_type: enum in [``'ACTION'``, ``'ARMATURE'``, ``'BRUSH'``, ``'CACHEFILE'``, ``'CAMERA'``, ``'COLLECTION'``, ``'CURVE'``, ``'CURVES'``, ``'FONT'``, ``'GREASEPENCIL'``, ``'GREASEPENCIL_V3'``, ``'IMAGE'``, ``'KEY'``, ``'LATTICE'``, ``'LIBRARY'``, ``'LIGHT'``, ``'LIGHT_PROBE'``, ``'LINESTYLE'``, ``'MASK'``, ``'MATERIAL'``, ``'MESH'``, ``'META'``, ``'MOVIECLIP'``, ``'NODETREE'``, ``'OBJECT'``, ``'PAINTCURVE'``, ``'PALETTE'``, ``'PARTICLE'``, ``'POINTCLOUD'``, ``'SCENE'``, ``'SCREEN'``, ``'SOUND'``, ``'SPEAKER'``, ``'TEXT'``, ``'TEXTURE'``, ``'VOLUME'``, ``'WINDOWMANAGER'``, ``'WORKSPACE'``, ``'WORLD'``], (optional)
   :arg eval_string: Value, Python value for unsupported custom property types
   :type eval_string: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:1861 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L1861>`__


.. function:: properties_edit_value(*, data_path="", property_name="", eval_string="")

   Edit the value of a custom property

   :arg data_path: Property Edit, Property data_path edit
   :type data_path: string, (optional, never None)
   :arg property_name: Property Name, Property name edit
   :type property_name: string, (optional, never None)
   :arg eval_string: Value, Value for custom property types that can only be edited as a Python expression
   :type eval_string: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:2085 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2085>`__


.. function:: properties_remove(*, data_path="", property_name="")

   Internal use (edit a property data_path)

   :arg data_path: Property Edit, Property data_path edit
   :type data_path: string, (optional, never None)
   :arg property_name: Property Name, Property name edit
   :type property_name: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:2185 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2185>`__


.. function:: quit_blender()

   Quit Blender

.. function:: radial_control(*, data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False, release_confirm=False)

   Set some size property (e.g. brush size) with mouse wheel

   :arg data_path_primary: Primary Data Path, Primary path of property to be set by the radial control
   :type data_path_primary: string, (optional, never None)
   :arg data_path_secondary: Secondary Data Path, Secondary path of property to be set by the radial control
   :type data_path_secondary: string, (optional, never None)
   :arg use_secondary: Use Secondary, Path of property to select between the primary and secondary data paths
   :type use_secondary: string, (optional, never None)
   :arg rotation_path: Rotation Path, Path of property used to rotate the texture display
   :type rotation_path: string, (optional, never None)
   :arg color_path: Color Path, Path of property used to set the color of the control
   :type color_path: string, (optional, never None)
   :arg fill_color_path: Fill Color Path, Path of property used to set the fill color of the control
   :type fill_color_path: string, (optional, never None)
   :arg fill_color_override_path: Fill Color Override Path
   :type fill_color_override_path: string, (optional, never None)
   :arg fill_color_override_test_path: Fill Color Override Test
   :type fill_color_override_test_path: string, (optional, never None)
   :arg zoom_path: Zoom Path, Path of property used to set the zoom level for the control
   :type zoom_path: string, (optional, never None)
   :arg image_id: Image ID, Path of ID that is used to generate an image for the control
   :type image_id: string, (optional, never None)
   :arg secondary_tex: Secondary Texture, Tweak brush secondary/mask texture
   :type secondary_tex: boolean, (optional)
   :arg release_confirm: Confirm On Release, Finish operation on key release
   :type release_confirm: boolean, (optional)

.. function:: read_factory_settings(*, use_factory_startup_app_template_only=False, app_template="Template", use_empty=False)

   Load factory default startup file and preferences. To make changes permanent, use "Save Startup File" and "Save Preferences"

   :arg use_factory_startup_app_template_only: Factory Startup App-Template Only
   :type use_factory_startup_app_template_only: boolean, (optional)
   :type app_template: string, (optional, never None)
   :arg use_empty: Empty, After loading, remove everything except scenes, windows, and workspaces. This makes it possible to load the startup file with its scene configuration and window layout intact, but no objects, materials, animations, ...
   :type use_empty: boolean, (optional)

.. function:: read_factory_userpref(*, use_factory_startup_app_template_only=False)

   Load factory default preferences. To make changes to preferences permanent, use "Save Preferences"

   :arg use_factory_startup_app_template_only: Factory Startup App-Template Only
   :type use_factory_startup_app_template_only: boolean, (optional)

.. function:: read_history()

   Reloads history and bookmarks

.. function:: read_homefile(*, filepath="", load_ui=True, use_splash=False, use_factory_startup=False, use_factory_startup_app_template_only=False, app_template="Template", use_empty=False)

   Open the default file

   :arg filepath: File Path, Path to an alternative start-up file
   :type filepath: string, (optional, never None)
   :arg load_ui: Load UI, Load user interface setup from the .blend file
   :type load_ui: boolean, (optional)
   :arg use_splash: Splash
   :type use_splash: boolean, (optional)
   :arg use_factory_startup: Factory Startup, Load the default ('factory startup') blend file. This is independent of the normal start-up file that the user can save
   :type use_factory_startup: boolean, (optional)
   :arg use_factory_startup_app_template_only: Factory Startup App-Template Only
   :type use_factory_startup_app_template_only: boolean, (optional)
   :type app_template: string, (optional, never None)
   :arg use_empty: Empty, After loading, remove everything except scenes, windows, and workspaces. This makes it possible to load the startup file with its scene configuration and window layout intact, but no objects, materials, animations, ...
   :type use_empty: boolean, (optional)

.. function:: read_userpref()

   Load last saved preferences

.. function:: recover_auto_save(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=False, filter_blenlib=False, filemode=8, display_type='LIST_VERTICAL', sort_method='', use_scripts=False)

   Open an automatically saved file to recover it

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
   :type hide_props_region: boolean, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
   :type use_scripts: boolean, (optional)

.. function:: recover_last_session(*, use_scripts=False)

   Open the last closed file ("quit.blend")

   :arg use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
   :type use_scripts: boolean, (optional)

.. function:: redraw_timer(*, type='DRAW', iterations=10, time_limit=0.0)

   Simple redraw timer to test the speed of updating the interface

   :arg type: Type

      * ``DRAW``
        Draw Region -- Draw region.
      * ``DRAW_SWAP``
        Draw Region & Swap -- Draw region and swap.
      * ``DRAW_WIN``
        Draw Window -- Draw window.
      * ``DRAW_WIN_SWAP``
        Draw Window & Swap -- Draw window and swap.
      * ``ANIM_STEP``
        Animation Step -- Animation steps.
      * ``ANIM_PLAY``
        Animation Play -- Animation playback.
      * ``UNDO``
        Undo/Redo -- Undo and redo.
   :type type: enum in [``'DRAW'``, ``'DRAW_SWAP'``, ``'DRAW_WIN'``, ``'DRAW_WIN_SWAP'``, ``'ANIM_STEP'``, ``'ANIM_PLAY'``, ``'UNDO'``], (optional)
   :arg iterations: Iterations, Number of times to redraw
   :type iterations: int in [1, inf], (optional)
   :arg time_limit: Time Limit, Seconds to run the test for (override iterations)
   :type time_limit: float in [0, inf], (optional)

.. function:: revert_mainfile(*, use_scripts=False)

   Reload the saved file

   :arg use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
   :type use_scripts: boolean, (optional)

.. function:: save_as_mainfile(*, filepath="", hide_props_region=True, check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', compress=False, relative_remap=True, copy=False)

   Save the current file in the desired location

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
   :type hide_props_region: boolean, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg compress: Compress, Write compressed .blend file
   :type compress: boolean, (optional)
   :arg relative_remap: Remap Relative, Remap relative paths when saving to a different directory
   :type relative_remap: boolean, (optional)
   :arg copy: Save Copy, Save a copy of the actual working state but does not make saved file active
   :type copy: boolean, (optional)

.. function:: save_homefile()

   Make the current file the default startup file

.. function:: save_mainfile(*, filepath="", hide_props_region=True, check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', compress=False, relative_remap=False, exit=False, incremental=False)

   Save the current Blender file

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
   :type hide_props_region: boolean, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg compress: Compress, Write compressed .blend file
   :type compress: boolean, (optional)
   :arg relative_remap: Remap Relative, Remap relative paths when saving to a different directory
   :type relative_remap: boolean, (optional)
   :arg exit: Exit, Exit Blender after saving
   :type exit: boolean, (optional)
   :arg incremental: Incremental, Save the current Blender file with a numerically incremented name that does not overwrite any existing files
   :type incremental: boolean, (optional)

.. function:: save_userpref()

   Make the current preferences default

.. function:: search_menu()

   Pop-up a search over all menus in the current context

.. function:: search_operator()

   Pop-up a search over all available operators in current context

.. function:: search_single_menu(*, menu_idname="", initial_query="")

   Pop-up a search for a menu in current context

   :arg menu_idname: Menu Name, Menu to search in
   :type menu_idname: string, (optional, never None)
   :arg initial_query: Initial Query, Query to insert into the search box
   :type initial_query: string, (optional, never None)

.. function:: set_stereo_3d(*, display_mode='ANAGLYPH', anaglyph_type='RED_CYAN', interlace_type='ROW_INTERLEAVED', use_interlace_swap=False, use_sidebyside_crosseyed=False)

   Toggle 3D stereo support for current window (or change the display mode)

   :arg display_mode: Display Mode
   :type display_mode: enum in :ref:`rna_enum_stereo3d_display_items`, (optional)
   :arg anaglyph_type: Anaglyph Type
   :type anaglyph_type: enum in :ref:`rna_enum_stereo3d_anaglyph_type_items`, (optional)
   :arg interlace_type: Interlace Type
   :type interlace_type: enum in :ref:`rna_enum_stereo3d_interlace_type_items`, (optional)
   :arg use_interlace_swap: Swap Left/Right, Swap left and right stereo channels
   :type use_interlace_swap: boolean, (optional)
   :arg use_sidebyside_crosseyed: Cross-Eyed, Right eye should see left image and vice versa
   :type use_sidebyside_crosseyed: boolean, (optional)

.. function:: splash()

   Open the splash screen with release info

.. function:: splash_about()

   Open a window with information about Blender

.. function:: stl_export(*, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', ascii_format=False, use_batch=False, export_selected_objects=False, collection="", global_scale=1.0, use_scene_unit=False, forward_axis='Y', up_axis='Z', apply_modifiers=True, filter_glob="*.stl")

   Save the scene to an STL file

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg ascii_format: ASCII Format, Export file in ASCII format, export as binary otherwise
   :type ascii_format: boolean, (optional)
   :arg use_batch: Batch Export, Export each object to a separate file
   :type use_batch: boolean, (optional)
   :arg export_selected_objects: Export Selected Objects, Export only selected objects instead of all supported objects
   :type export_selected_objects: boolean, (optional)
   :arg collection: Source Collection, Export only objects from this collection (and its children)
   :type collection: string, (optional, never None)
   :arg global_scale: Scale
   :type global_scale: float in [1e-06, 1e+06], (optional)
   :arg use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to exported data
   :type use_scene_unit: boolean, (optional)
   :arg forward_axis: Forward Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type forward_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg up_axis: Up Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type up_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg apply_modifiers: Apply Modifiers, Apply modifiers to exported meshes
   :type apply_modifiers: boolean, (optional)
   :arg filter_glob: Extension Filter
   :type filter_glob: string, (optional, never None)

.. function:: stl_import(*, filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', global_scale=1.0, use_scene_unit=False, use_facet_normal=False, forward_axis='Y', up_axis='Z', use_mesh_validate=True, filter_glob="*.stl")

   Import an STL file as an object

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg global_scale: Scale
   :type global_scale: float in [1e-06, 1e+06], (optional)
   :arg use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
   :type use_scene_unit: boolean, (optional)
   :arg use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading)
   :type use_facet_normal: boolean, (optional)
   :arg forward_axis: Forward Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type forward_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg up_axis: Up Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type up_axis: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg use_mesh_validate: Validate Mesh, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)
   :type use_mesh_validate: boolean, (optional)
   :arg filter_glob: Extension Filter
   :type filter_glob: string, (optional, never None)

.. function:: sysinfo(*, filepath="")

   Generate system information, saved into a text file

   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:2214 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2214>`__


.. function:: tool_set_by_brush_type(*, brush_type="", space_type='EMPTY')

   Look up the most appropriate tool for the given brush type and activate that

   :arg brush_type: Brush Type, Brush type identifier for which the most appropriate tool will be looked up
   :type brush_type: string, (optional, never None)
   :arg space_type: Type
   :type space_type: enum in [``'EMPTY'``, ``'VIEW_3D'``, ``'IMAGE_EDITOR'``, ``'NODE_EDITOR'``, ``'SEQUENCE_EDITOR'``, ``'CLIP_EDITOR'``, ``'DOPESHEET_EDITOR'``, ``'GRAPH_EDITOR'``, ``'NLA_EDITOR'``, ``'TEXT_EDITOR'``, ``'CONSOLE'``, ``'INFO'``, ``'TOPBAR'``, ``'STATUSBAR'``, ``'OUTLINER'``, ``'PROPERTIES'``, ``'FILE_BROWSER'``, ``'SPREADSHEET'``, ``'PREFERENCES'``], (optional)
   :File: `startup\bl_operators\wm.py\:2428 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2428>`__


.. function:: tool_set_by_id(*, name="", cycle=False, as_fallback=False, space_type='EMPTY')

   Set the tool by name (for key-maps)

   :arg name: Identifier, Identifier of the tool
   :type name: string, (optional, never None)
   :arg cycle: Cycle, Cycle through tools in this group
   :type cycle: boolean, (optional)
   :arg as_fallback: Set Fallback, Set the fallback tool instead of the primary tool
   :type as_fallback: boolean, (optional)
   :arg space_type: Type
   :type space_type: enum in [``'EMPTY'``, ``'VIEW_3D'``, ``'IMAGE_EDITOR'``, ``'NODE_EDITOR'``, ``'SEQUENCE_EDITOR'``, ``'CLIP_EDITOR'``, ``'DOPESHEET_EDITOR'``, ``'GRAPH_EDITOR'``, ``'NLA_EDITOR'``, ``'TEXT_EDITOR'``, ``'CONSOLE'``, ``'INFO'``, ``'TOPBAR'``, ``'STATUSBAR'``, ``'OUTLINER'``, ``'PROPERTIES'``, ``'FILE_BROWSER'``, ``'SPREADSHEET'``, ``'PREFERENCES'``], (optional)
   :File: `startup\bl_operators\wm.py\:2337 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2337>`__


.. function:: tool_set_by_index(*, index=0, cycle=False, expand=True, as_fallback=False, space_type='EMPTY')

   Set the tool by index (for key-maps)

   :arg index: Index in Toolbar
   :type index: int in [-inf, inf], (optional)
   :arg cycle: Cycle, Cycle through tools in this group
   :type cycle: boolean, (optional)
   :arg expand: expand, Include tool subgroups
   :type expand: boolean, (optional)
   :arg as_fallback: Set Fallback, Set the fallback tool instead of the primary
   :type as_fallback: boolean, (optional)
   :arg space_type: Type
   :type space_type: enum in [``'EMPTY'``, ``'VIEW_3D'``, ``'IMAGE_EDITOR'``, ``'NODE_EDITOR'``, ``'SEQUENCE_EDITOR'``, ``'CLIP_EDITOR'``, ``'DOPESHEET_EDITOR'``, ``'GRAPH_EDITOR'``, ``'NLA_EDITOR'``, ``'TEXT_EDITOR'``, ``'CONSOLE'``, ``'INFO'``, ``'TOPBAR'``, ``'STATUSBAR'``, ``'OUTLINER'``, ``'PROPERTIES'``, ``'FILE_BROWSER'``, ``'SPREADSHEET'``, ``'PREFERENCES'``], (optional)
   :File: `startup\bl_operators\wm.py\:2387 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2387>`__


.. function:: toolbar()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :File: `startup\bl_operators\wm.py\:2495 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2495>`__

.. function:: toolbar_fallback_pie()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :File: `startup\bl_operators\wm.py\:2519 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2519>`__

.. function:: toolbar_prompt()

   Leader key like functionality for accessing tools

   :File: `startup\bl_operators\wm.py\:2619 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L2619>`__

.. function:: url_open(*, url="")

   Open a website in the web browser

   :arg url: URL, URL to open
   :type url: string, (optional, never None)
   :File: `startup\bl_operators\wm.py\:1074 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L1074>`__


.. function:: url_open_preset(*, type='')

   Open a preset website in the web browser

   :arg type: Site
   :type type: enum in [], (optional)
   :File: `startup\bl_operators\wm.py\:1144 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\wm.py#L1144>`__


.. function:: usd_export(*, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=True, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', filter_glob="*.usd", selected_objects_only=False, visible_objects_only=True, collection="", export_animation=False, export_hair=False, export_uvmaps=True, rename_uvmaps=True, export_mesh_colors=True, export_normals=True, export_materials=True, export_subdivision='BEST_MATCH', export_armatures=True, only_deform_bones=False, export_shapekeys=True, use_instancing=False, evaluation_mode='RENDER', generate_preview_surface=True, generate_materialx_network=False, convert_orientation=False, export_global_forward_selection='NEGATIVE_Z', export_global_up_selection='Y', export_textures=False, export_textures_mode='NEW', overwrite_textures=False, relative_paths=True, xform_op_mode='TRS', root_prim_path="/root", export_custom_properties=True, custom_properties_namespace="userProperties", author_blender_name=True, convert_world_material=True, allow_unicode=False, export_meshes=True, export_lights=True, export_cameras=True, export_curves=True, export_points=True, export_volumes=True, triangulate_meshes=False, quad_method='SHORTEST_DIAGONAL', ngon_method='BEAUTY', usdz_downscale_size='KEEP', usdz_downscale_custom_size=128, merge_parent_xform=False, convert_scene_units='METERS', meters_per_unit=1.0)

   Export current scene in a USD archive

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :type filter_glob: string, (optional, never None)
   :arg selected_objects_only: Selection Only, Only export selected objects. Unselected parents of selected objects are exported as empty transform
   :type selected_objects_only: boolean, (optional)
   :arg visible_objects_only: Visible Only, Only export visible objects. Invisible parents of exported objects are exported as empty transforms
   :type visible_objects_only: boolean, (optional)
   :arg collection: Collection
   :type collection: string, (optional, never None)
   :arg export_animation: Animation, Export all frames in the render frame range, rather than only the current frame
   :type export_animation: boolean, (optional)
   :arg export_hair: Hair, Export hair particle systems as USD curves
   :type export_hair: boolean, (optional)
   :arg export_uvmaps: UV Maps, Include all mesh UV maps in the export
   :type export_uvmaps: boolean, (optional)
   :arg rename_uvmaps: Rename UV Maps, Rename active render UV map to "st" to match USD conventions
   :type rename_uvmaps: boolean, (optional)
   :arg export_mesh_colors: Color Attributes, Include mesh color attributes in the export
   :type export_mesh_colors: boolean, (optional)
   :arg export_normals: Normals, Include normals of exported meshes in the export
   :type export_normals: boolean, (optional)
   :arg export_materials: Materials, Export viewport settings of materials as USD preview materials, and export material assignments as geometry subsets
   :type export_materials: boolean, (optional)
   :arg export_subdivision: Subdivision, Choose how subdivision modifiers will be mapped to the USD subdivision scheme during export

      * ``IGNORE``
        Ignore -- Scheme = None. Export base mesh without subdivision.
      * ``TESSELLATE``
        Tessellate -- Scheme = None. Export subdivided mesh.
      * ``BEST_MATCH``
        Best Match -- Scheme = Catmull-Clark, when possible. Reverts to exporting the subdivided mesh for the Simple subdivision type.
   :type export_subdivision: enum in [``'IGNORE'``, ``'TESSELLATE'``, ``'BEST_MATCH'``], (optional)
   :arg export_armatures: Armatures, Export armatures and meshes with armature modifiers as USD skeletons and skinned meshes
   :type export_armatures: boolean, (optional)
   :arg only_deform_bones: Only Deform Bones, Only export deform bones and their parents
   :type only_deform_bones: boolean, (optional)
   :arg export_shapekeys: Shape Keys, Export shape keys as USD blend shapes
   :type export_shapekeys: boolean, (optional)
   :arg use_instancing: Instancing, Export instanced objects as references in USD rather than real objects
   :type use_instancing: boolean, (optional)
   :arg evaluation_mode: Use Settings for, Determines visibility of objects, modifier settings, and other areas where there are different settings for viewport and rendering

      * ``RENDER``
        Render -- Use Render settings for object visibility, modifier settings, etc.
      * ``VIEWPORT``
        Viewport -- Use Viewport settings for object visibility, modifier settings, etc.
   :type evaluation_mode: enum in [``'RENDER'``, ``'VIEWPORT'``], (optional)
   :arg generate_preview_surface: USD Preview Surface Network, Generate an approximate USD Preview Surface shader representation of a Principled BSDF node network
   :type generate_preview_surface: boolean, (optional)
   :arg generate_materialx_network: MaterialX Network, Generate a MaterialX network representation of the materials
   :type generate_materialx_network: boolean, (optional)
   :arg convert_orientation: Convert Orientation, Convert orientation axis to a different convention to match other applications
   :type convert_orientation: boolean, (optional)
   :arg export_global_forward_selection: Forward Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type export_global_forward_selection: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg export_global_up_selection: Up Axis

      * ``X``
        X -- Positive X axis.
      * ``Y``
        Y -- Positive Y axis.
      * ``Z``
        Z -- Positive Z axis.
      * ``NEGATIVE_X``
        -X -- Negative X axis.
      * ``NEGATIVE_Y``
        -Y -- Negative Y axis.
      * ``NEGATIVE_Z``
        -Z -- Negative Z axis.
   :type export_global_up_selection: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NEGATIVE_X'``, ``'NEGATIVE_Y'``, ``'NEGATIVE_Z'``], (optional)
   :arg export_textures: Export Textures, If exporting materials, export textures referenced by material nodes to a 'textures' directory in the same directory as the USD file
   :type export_textures: boolean, (optional)
   :arg export_textures_mode: Export Textures, Texture export method

      * ``KEEP``
        Keep -- Use original location of textures.
      * ``PRESERVE``
        Preserve -- Preserve file paths of textures from already imported USD files.
        Export remaining textures to a 'textures' folder next to the USD file.
      * ``NEW``
        New Path -- Export textures to a 'textures' folder next to the USD file.
   :type export_textures_mode: enum in [``'KEEP'``, ``'PRESERVE'``, ``'NEW'``], (optional)
   :arg overwrite_textures: Overwrite Textures, Overwrite existing files when exporting textures
   :type overwrite_textures: boolean, (optional)
   :arg relative_paths: Relative Paths, Use relative paths to reference external files (i.e. textures, volumes) in USD, otherwise use absolute paths
   :type relative_paths: boolean, (optional)
   :arg xform_op_mode: Xform Ops, The type of transform operators to write

      * ``TRS``
        Translate, Rotate, Scale -- Export with translate, rotate, and scale Xform operators.
      * ``TOS``
        Translate, Orient, Scale -- Export with translate, orient quaternion, and scale Xform operators.
      * ``MAT``
        Matrix -- Export matrix operator.
   :type xform_op_mode: enum in [``'TRS'``, ``'TOS'``, ``'MAT'``], (optional)
   :arg root_prim_path: Root Prim, If set, add a transform primitive with the given path to the stage as the parent of all exported data
   :type root_prim_path: string, (optional, never None)
   :arg export_custom_properties: Custom Properties, Export custom properties as USD attributes
   :type export_custom_properties: boolean, (optional)
   :arg custom_properties_namespace: Namespace, If set, add the given namespace as a prefix to exported custom property names. This only applies to property names that do not already have a prefix (e.g., it would apply to name 'bar' but not 'foo:bar') and does not apply to blender object and data names which are always exported in the 'userProperties:blender' namespace
   :type custom_properties_namespace: string, (optional, never None)
   :arg author_blender_name: Blender Names, Author USD custom attributes containing the original Blender object and object data names
   :type author_blender_name: boolean, (optional)
   :arg convert_world_material: World Dome Light, Convert the world material to a USD dome light. Currently works for simple materials, consisting of an environment texture connected to a background shader, with an optional vector multiply of the texture color
   :type convert_world_material: boolean, (optional)
   :arg allow_unicode: Allow Unicode, Preserve UTF-8 encoded characters when writing USD prim and property names (requires software utilizing USD 24.03 or greater when opening the resulting files)
   :type allow_unicode: boolean, (optional)
   :arg export_meshes: Meshes, Export all meshes
   :type export_meshes: boolean, (optional)
   :arg export_lights: Lights, Export all lights
   :type export_lights: boolean, (optional)
   :arg export_cameras: Cameras, Export all cameras
   :type export_cameras: boolean, (optional)
   :arg export_curves: Curves, Export all curves
   :type export_curves: boolean, (optional)
   :arg export_points: Point Clouds, Export all point clouds
   :type export_points: boolean, (optional)
   :arg export_volumes: Volumes, Export all volumes
   :type export_volumes: boolean, (optional)
   :arg triangulate_meshes: Triangulate Meshes, Triangulate meshes during export
   :type triangulate_meshes: boolean, (optional)
   :arg quad_method: Quad Method, Method for splitting the quads into triangles
   :type quad_method: enum in :ref:`rna_enum_modifier_triangulate_quad_method_items`, (optional)
   :arg ngon_method: N-gon Method, Method for splitting the n-gons into triangles
   :type ngon_method: enum in :ref:`rna_enum_modifier_triangulate_ngon_method_items`, (optional)
   :arg usdz_downscale_size: USDZ Texture Downsampling, Choose a maximum size for all exported textures

      * ``KEEP``
        Keep -- Keep all current texture sizes.
      * ``256``
        256 -- Resize to a maximum of 256 pixels.
      * ``512``
        512 -- Resize to a maximum of 512 pixels.
      * ``1024``
        1024 -- Resize to a maximum of 1024 pixels.
      * ``2048``
        2048 -- Resize to a maximum of 2048 pixels.
      * ``4096``
        4096 -- Resize to a maximum of 4096 pixels.
      * ``CUSTOM``
        Custom -- Specify a custom size.
   :type usdz_downscale_size: enum in [``'KEEP'``, ``'256'``, ``'512'``, ``'1024'``, ``'2048'``, ``'4096'``, ``'CUSTOM'``], (optional)
   :arg usdz_downscale_custom_size: USDZ Custom Downscale Size, Custom size for downscaling exported textures
   :type usdz_downscale_custom_size: int in [64, 16384], (optional)
   :arg merge_parent_xform: Merge parent Xform, Merge USD primitives with their Xform parent if possible. USD does not allow nested UsdGeomGprims, intermediary Xform prims will be defined to keep the USD file valid when encountering object hierarchies.
   :type merge_parent_xform: boolean, (optional)
   :arg convert_scene_units: Units, Set the USD Stage meters per unit to the chosen measurement, or a custom value

      * ``METERS``
        Meters -- Scene meters per unit to 1.0.
      * ``KILOMETERS``
        Kilometers -- Scene meters per unit to 1000.0.
      * ``CENTIMETERS``
        Centimeters -- Scene meters per unit to 0.01.
      * ``MILLIMETERS``
        Millimeters -- Scene meters per unit to 0.001.
      * ``INCHES``
        Inches -- Scene meters per unit to 0.0254.
      * ``FEET``
        Feet -- Scene meters per unit to 0.3048.
      * ``YARDS``
        Yards -- Scene meters per unit to 0.9144.
      * ``CUSTOM``
        Custom -- Specify a custom scene meters per unit value.
   :type convert_scene_units: enum in [``'METERS'``, ``'KILOMETERS'``, ``'CENTIMETERS'``, ``'MILLIMETERS'``, ``'INCHES'``, ``'FEET'``, ``'YARDS'``, ``'CUSTOM'``], (optional)
   :arg meters_per_unit: Meters Per Unit, Custom value for meters per unit in the USD Stage
   :type meters_per_unit: float in [0.0001, 1000], (optional)

.. function:: usd_import(*, filepath="", check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=True, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='', filter_glob="*.usd", scale=1.0, set_frame_range=True, import_cameras=True, import_curves=True, import_lights=True, import_materials=True, import_meshes=True, import_volumes=True, import_shapes=True, import_skeletons=True, import_blendshapes=True, import_points=True, import_subdiv=False, support_scene_instancing=True, import_visible_only=True, create_collection=False, read_mesh_uvs=True, read_mesh_colors=True, read_mesh_attributes=True, prim_path_mask="", import_guide=False, import_proxy=False, import_render=True, import_all_materials=False, import_usd_preview=True, set_material_blend=True, light_intensity_scale=1.0, mtl_purpose='MTL_FULL', mtl_name_collision_mode='MAKE_UNIQUE', import_textures_mode='IMPORT_PACK', import_textures_dir="//textures/", tex_name_collision_mode='USE_EXISTING', attr_import_mode='ALL', validate_meshes=False, create_world_material=True, import_defined_only=True, merge_parent_xform=True, apply_unit_conversion_scale=True)

   Import USD stage into current scene

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg relative_path: Relative Path, Select the file relative to the blend file
   :type relative_path: boolean, (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :type filter_glob: string, (optional, never None)
   :arg scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
   :type scale: float in [0.0001, 1000], (optional)
   :arg set_frame_range: Set Frame Range, Update the scene's start and end frame to match those of the USD archive
   :type set_frame_range: boolean, (optional)
   :arg import_cameras: Cameras
   :type import_cameras: boolean, (optional)
   :arg import_curves: Curves
   :type import_curves: boolean, (optional)
   :arg import_lights: Lights
   :type import_lights: boolean, (optional)
   :arg import_materials: Materials
   :type import_materials: boolean, (optional)
   :arg import_meshes: Meshes
   :type import_meshes: boolean, (optional)
   :arg import_volumes: Volumes
   :type import_volumes: boolean, (optional)
   :arg import_shapes: USD Shapes
   :type import_shapes: boolean, (optional)
   :arg import_skeletons: Armatures
   :type import_skeletons: boolean, (optional)
   :arg import_blendshapes: Shape Keys
   :type import_blendshapes: boolean, (optional)
   :arg import_points: Point Clouds
   :type import_points: boolean, (optional)
   :arg import_subdiv: Import Subdivision Scheme, Create subdivision surface modifiers based on the USD SubdivisionScheme attribute
   :type import_subdiv: boolean, (optional)
   :arg support_scene_instancing: Scene Instancing, Import USD scene graph instances as collection instances
   :type support_scene_instancing: boolean, (optional)
   :arg import_visible_only: Visible Primitives Only, Do not import invisible USD primitives. Only applies to primitives with a non-animated visibility attribute. Primitives with animated visibility will always be imported
   :type import_visible_only: boolean, (optional)
   :arg create_collection: Create Collection, Add all imported objects to a new collection
   :type create_collection: boolean, (optional)
   :arg read_mesh_uvs: UV Coordinates, Read mesh UV coordinates
   :type read_mesh_uvs: boolean, (optional)
   :arg read_mesh_colors: Color Attributes, Read mesh color attributes
   :type read_mesh_colors: boolean, (optional)
   :arg read_mesh_attributes: Mesh Attributes, Read USD Primvars as mesh attributes
   :type read_mesh_attributes: boolean, (optional)
   :arg prim_path_mask: Path Mask, Import only the primitive at the given path and its descendants. Multiple paths may be specified in a list delimited by commas or semicolons
   :type prim_path_mask: string, (optional, never None)
   :arg import_guide: Guide, Import guide geometry
   :type import_guide: boolean, (optional)
   :arg import_proxy: Proxy, Import proxy geometry
   :type import_proxy: boolean, (optional)
   :arg import_render: Render, Import final render geometry
   :type import_render: boolean, (optional)
   :arg import_all_materials: Import All Materials, Also import materials that are not used by any geometry. Note that when this option is false, materials referenced by geometry will still be imported
   :type import_all_materials: boolean, (optional)
   :arg import_usd_preview: Import USD Preview, Convert UsdPreviewSurface shaders to Principled BSDF shader networks
   :type import_usd_preview: boolean, (optional)
   :arg set_material_blend: Set Material Blend, If the Import USD Preview option is enabled, the material blend method will automatically be set based on the shader's opacity and opacityThreshold inputs
   :type set_material_blend: boolean, (optional)
   :arg light_intensity_scale: Light Intensity Scale, Scale for the intensity of imported lights
   :type light_intensity_scale: float in [0.0001, 10000], (optional)
   :arg mtl_purpose: Material Purpose, Attempt to import materials with the given purpose. If no material with this purpose is bound to the primitive, fall back on loading any other bound material

      * ``MTL_ALL_PURPOSE``
        All Purpose -- Attempt to import 'allPurpose' materials..
      * ``MTL_PREVIEW``
        Preview -- Attempt to import 'preview' materials. Load 'allPurpose' materials as a fallback.
      * ``MTL_FULL``
        Full -- Attempt to import 'full' materials. Load 'allPurpose' or 'preview' materials, in that order, as a fallback.
   :type mtl_purpose: enum in [``'MTL_ALL_PURPOSE'``, ``'MTL_PREVIEW'``, ``'MTL_FULL'``], (optional)
   :arg mtl_name_collision_mode: Material Name Collision, Behavior when the name of an imported material conflicts with an existing material

      * ``MAKE_UNIQUE``
        Make Unique -- Import each USD material as a unique Blender material.
      * ``REFERENCE_EXISTING``
        Reference Existing -- If a material with the same name already exists, reference that instead of importing.
   :type mtl_name_collision_mode: enum in [``'MAKE_UNIQUE'``, ``'REFERENCE_EXISTING'``], (optional)
   :arg import_textures_mode: Import Textures, Behavior when importing textures from a USDZ archive

      * ``IMPORT_NONE``
        None -- Don't import textures.
      * ``IMPORT_PACK``
        Packed -- Import textures as packed data.
      * ``IMPORT_COPY``
        Copy -- Copy files to textures directory.
   :type import_textures_mode: enum in [``'IMPORT_NONE'``, ``'IMPORT_PACK'``, ``'IMPORT_COPY'``], (optional)
   :arg import_textures_dir: Textures Directory, Path to the directory where imported textures will be copied
   :type import_textures_dir: string, (optional, never None)
   :arg tex_name_collision_mode: File Name Collision, Behavior when the name of an imported texture file conflicts with an existing file

      * ``USE_EXISTING``
        Use Existing -- If a file with the same name already exists, use that instead of copying.
      * ``OVERWRITE``
        Overwrite -- Overwrite existing files.
   :type tex_name_collision_mode: enum in [``'USE_EXISTING'``, ``'OVERWRITE'``], (optional)
   :arg attr_import_mode: Custom Properties, Behavior when importing USD attributes as Blender custom properties

      * ``NONE``
        None -- Do not import USD custom attributes.
      * ``USER``
        User -- Import USD attributes in the 'userProperties' namespace as Blender custom properties. The namespace will be stripped from the property names.
      * ``ALL``
        All Custom -- Import all USD custom attributes as Blender custom properties. Namespaces will be retained in the property names.
   :type attr_import_mode: enum in [``'NONE'``, ``'USER'``, ``'ALL'``], (optional)
   :arg validate_meshes: Validate Meshes, Ensure the data is valid (when disabled, data may be imported which causes crashes displaying or editing)
   :type validate_meshes: boolean, (optional)
   :arg create_world_material: World Dome Light, Convert the first discovered USD dome light to a world background shader
   :type create_world_material: boolean, (optional)
   :arg import_defined_only: Defined Primitives Only, Import only defined USD primitives. When disabled this allows importing USD primitives which are not defined, such as those with an override specifier
   :type import_defined_only: boolean, (optional)
   :arg merge_parent_xform: Merge parent Xform, Allow USD primitives to merge with their Xform parent if they are the only child in the hierarchy
   :type merge_parent_xform: boolean, (optional)
   :arg apply_unit_conversion_scale: Apply Unit Conversion Scale, Scale the scene objects by the USD stage's meters per unit value. This scaling is applied in addition to the value specified in the Scale option
   :type apply_unit_conversion_scale: boolean, (optional)

.. function:: window_close()

   Close the current window

.. function:: window_fullscreen_toggle()

   Toggle the current window full-screen

.. function:: window_new()

   Create a new window

.. function:: window_new_main()

   Create a new main window with its own workspace and scene selection

.. function:: xr_navigation_fly(*, mode='VIEWER_FORWARD', lock_location_z=False, lock_direction=False, speed_frame_based=True, speed_min=0.018, speed_max=0.054, speed_interpolation0=(0.0, 0.0), speed_interpolation1=(1.0, 1.0))

   Move/turn relative to the VR viewer or controller

   :arg mode: Mode, Fly mode

      * ``FORWARD``
        Forward -- Move along navigation forward axis.
      * ``BACK``
        Back -- Move along navigation back axis.
      * ``LEFT``
        Left -- Move along navigation left axis.
      * ``RIGHT``
        Right -- Move along navigation right axis.
      * ``UP``
        Up -- Move along navigation up axis.
      * ``DOWN``
        Down -- Move along navigation down axis.
      * ``TURNLEFT``
        Turn Left -- Turn counter-clockwise around navigation up axis.
      * ``TURNRIGHT``
        Turn Right -- Turn clockwise around navigation up axis.
      * ``VIEWER_FORWARD``
        Viewer Forward -- Move along viewer's forward axis.
      * ``VIEWER_BACK``
        Viewer Back -- Move along viewer's back axis.
      * ``VIEWER_LEFT``
        Viewer Left -- Move along viewer's left axis.
      * ``VIEWER_RIGHT``
        Viewer Right -- Move along viewer's right axis.
      * ``CONTROLLER_FORWARD``
        Controller Forward -- Move along controller's forward axis.
   :type mode: enum in [``'FORWARD'``, ``'BACK'``, ``'LEFT'``, ``'RIGHT'``, ``'UP'``, ``'DOWN'``, ``'TURNLEFT'``, ``'TURNRIGHT'``, ``'VIEWER_FORWARD'``, ``'VIEWER_BACK'``, ``'VIEWER_LEFT'``, ``'VIEWER_RIGHT'``, ``'CONTROLLER_FORWARD'``], (optional)
   :arg lock_location_z: Lock Elevation, Prevent changes to viewer elevation
   :type lock_location_z: boolean, (optional)
   :arg lock_direction: Lock Direction, Limit movement to viewer's initial direction
   :type lock_direction: boolean, (optional)
   :arg speed_frame_based: Frame Based Speed, Apply fixed movement deltas every update
   :type speed_frame_based: boolean, (optional)
   :arg speed_min: Minimum Speed, Minimum move (turn) speed in meters (radians) per second or frame
   :type speed_min: float in [0, 1000], (optional)
   :arg speed_max: Maximum Speed, Maximum move (turn) speed in meters (radians) per second or frame
   :type speed_max: float in [0, 1000], (optional)
   :arg speed_interpolation0: Speed Interpolation 0, First cubic spline control point between min/max speeds
   :type speed_interpolation0: :class:`mathutils.Vector` of 2 items in [0, 1], (optional)
   :arg speed_interpolation1: Speed Interpolation 1, Second cubic spline control point between min/max speeds
   :type speed_interpolation1: :class:`mathutils.Vector` of 2 items in [0, 1], (optional)

.. function:: xr_navigation_grab(*, lock_location=False, lock_location_z=False, lock_rotation=False, lock_rotation_z=False, lock_scale=False)

   Navigate the VR scene by grabbing with controllers

   :arg lock_location: Lock Location, Prevent changes to viewer location
   :type lock_location: boolean, (optional)
   :arg lock_location_z: Lock Elevation, Prevent changes to viewer elevation
   :type lock_location_z: boolean, (optional)
   :arg lock_rotation: Lock Rotation, Prevent changes to viewer rotation
   :type lock_rotation: boolean, (optional)
   :arg lock_rotation_z: Lock Up Orientation, Prevent changes to viewer up orientation
   :type lock_rotation_z: boolean, (optional)
   :arg lock_scale: Lock Scale, Prevent changes to viewer scale
   :type lock_scale: boolean, (optional)

.. function:: xr_navigation_reset(*, location=True, rotation=True, scale=True)

   Reset VR navigation deltas relative to session base pose

   :arg location: Location, Reset location deltas
   :type location: boolean, (optional)
   :arg rotation: Rotation, Reset rotation deltas
   :type rotation: boolean, (optional)
   :arg scale: Scale, Reset scale deltas
   :type scale: boolean, (optional)

.. function:: xr_navigation_teleport(*, teleport_axes=(True, True, True), interpolation=1.0, offset=0.0, selectable_only=True, distance=1.70141e+38, from_viewer=False, axis=(0.0, 0.0, -1.0), color=(0.35, 0.35, 1.0, 1.0))

   Set VR viewer location to controller raycast hit location

   :arg teleport_axes: Teleport Axes, Enabled teleport axes in navigation space
   :type teleport_axes: boolean array of 3 items, (optional)
   :arg interpolation: Interpolation, Interpolation factor between viewer and hit locations
   :type interpolation: float in [0, 1], (optional)
   :arg offset: Offset, Offset along hit normal to subtract from final location
   :type offset: float in [0, inf], (optional)
   :arg selectable_only: Selectable Only, Only allow selectable objects to influence raycast result
   :type selectable_only: boolean, (optional)
   :arg distance: Maximum raycast distance
   :type distance: float in [0, inf], (optional)
   :arg from_viewer: From Viewer, Use viewer pose as raycast origin
   :type from_viewer: boolean, (optional)
   :arg axis: Axis, Raycast axis in controller/viewer space
   :type axis: :class:`mathutils.Vector` of 3 items in [-1, 1], (optional)
   :arg color: Color, Raycast color
   :type color: float array of 4 items in [0, 1], (optional)

.. function:: xr_session_toggle()

   Open a view for use with virtual reality headsets, or close it if already opened

