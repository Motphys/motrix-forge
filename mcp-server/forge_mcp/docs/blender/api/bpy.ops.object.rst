Object Operators
================

.. module:: bpy.ops.object

.. function:: add(*, radius=1.0, type='EMPTY', enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add an object to the scene

   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg type: Type
   :type type: enum in :ref:`rna_enum_object_type_items`, (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: add_modifier_menu()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :File: `startup\bl_ui\properties_data_modifier.py\:283 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_ui\properties_data_modifier.py#L283>`__

.. function:: add_named(*, linked=False, name="", session_uid=0, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), drop_x=0, drop_y=0)

   Add named object

   :arg linked: Linked, Duplicate object but not object data, linking to the original data
   :type linked: boolean, (optional)
   :arg name: Name, Name of the data-block to use by the operator
   :type name: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)
   :arg matrix: Matrix
   :type matrix: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], (optional)
   :arg drop_x: Drop X, X-coordinate (screen space) to place the new object under
   :type drop_x: int in [-inf, inf], (optional)
   :arg drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
   :type drop_y: int in [-inf, inf], (optional)

.. function:: align(*, bb_quality=True, align_mode='OPT_2', relative_to='OPT_4', align_axis={})

   Align objects

   :arg bb_quality: High Quality, Enables high quality but slow calculation of the bounding box for perfect results on complex shape meshes with rotation/scale
   :type bb_quality: boolean, (optional)
   :arg align_mode: Align Mode, Side of object to use for alignment
   :type align_mode: enum in [``'OPT_1'``, ``'OPT_2'``, ``'OPT_3'``], (optional)
   :arg relative_to: Relative To, Reference location to align to

      * ``OPT_1``
        Scene Origin -- Use the scene origin as the position for the selected objects to align to.
      * ``OPT_2``
        3D Cursor -- Use the 3D cursor as the position for the selected objects to align to.
      * ``OPT_3``
        Selection -- Use the selected objects as the position for the selected objects to align to.
      * ``OPT_4``
        Active -- Use the active object as the position for the selected objects to align to.
   :type relative_to: enum in [``'OPT_1'``, ``'OPT_2'``, ``'OPT_3'``, ``'OPT_4'``], (optional)
   :arg align_axis: Align, Align to axis
   :type align_axis: enum set in {``'X'``, ``'Y'``, ``'Z'``}, (optional)
   :File: `startup\bl_operators\object_align.py\:386 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object_align.py#L386>`__


.. function:: anim_transforms_to_deltas()

   Convert object animation for normal transforms to delta transforms

   :File: `startup\bl_operators\object.py\:821 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L821>`__

.. function:: armature_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add an armature object to the scene

   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: assign_property_defaults(*, process_data=True, process_bones=True)

   Assign the current values of custom properties as their defaults, for use as part of the rest pose state in NLA track mixing

   :arg process_data: Process data properties
   :type process_data: boolean, (optional)
   :arg process_bones: Process bone properties
   :type process_bones: boolean, (optional)
   :File: `startup\bl_operators\object.py\:973 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L973>`__


.. function:: bake(*, type='COMBINED', pass_filter={}, filepath="", width=512, height=512, margin=16, margin_type='EXTEND', use_selected_to_active=False, max_ray_distance=0.0, cage_extrusion=0.0, cage_object="", normal_space='TANGENT', normal_r='POS_X', normal_g='POS_Y', normal_b='POS_Z', target='IMAGE_TEXTURES', save_mode='INTERNAL', use_clear=False, use_cage=False, use_split_materials=False, use_automatic_name=False, uv_layer="")

   Bake image textures of selected objects

   :arg type: Type, Type of pass to bake, some of them may not be supported by the current render engine
   :type type: enum in :ref:`rna_enum_bake_pass_type_items`, (optional)
   :arg pass_filter: Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes
   :type pass_filter: enum set in :ref:`rna_enum_bake_pass_filter_type_items`, (optional)
   :arg filepath: File Path, Image filepath to use when saving externally
   :type filepath: string, (optional, never None)
   :arg width: Width, Horizontal dimension of the baking map (external only)
   :type width: int in [1, inf], (optional)
   :arg height: Height, Vertical dimension of the baking map (external only)
   :type height: int in [1, inf], (optional)
   :arg margin: Margin, Extends the baked result as a post process filter
   :type margin: int in [0, inf], (optional)
   :arg margin_type: Margin Type, Which algorithm to use to generate the margin
   :type margin_type: enum in :ref:`rna_enum_bake_margin_type_items`, (optional)
   :arg use_selected_to_active: Selected to Active, Bake shading on the surface of selected objects to the active object
   :type use_selected_to_active: boolean, (optional)
   :arg max_ray_distance: Max Ray Distance, The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit
   :type max_ray_distance: float in [0, inf], (optional)
   :arg cage_extrusion: Cage Extrusion, Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes
   :type cage_extrusion: float in [0, inf], (optional)
   :arg cage_object: Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion
   :type cage_object: string, (optional, never None)
   :arg normal_space: Normal Space, Choose normal space for baking
   :type normal_space: enum in :ref:`rna_enum_normal_space_items`, (optional)
   :arg normal_r: R, Axis to bake in red channel
   :type normal_r: enum in :ref:`rna_enum_normal_swizzle_items`, (optional)
   :arg normal_g: G, Axis to bake in green channel
   :type normal_g: enum in :ref:`rna_enum_normal_swizzle_items`, (optional)
   :arg normal_b: B, Axis to bake in blue channel
   :type normal_b: enum in :ref:`rna_enum_normal_swizzle_items`, (optional)
   :arg target: Target, Where to output the baked map
   :type target: enum in :ref:`rna_enum_bake_target_items`, (optional)
   :arg save_mode: Save Mode, Where to save baked image textures
   :type save_mode: enum in :ref:`rna_enum_bake_save_mode_items`, (optional)
   :arg use_clear: Clear, Clear images before baking (only for internal saving)
   :type use_clear: boolean, (optional)
   :arg use_cage: Cage, Cast rays to active object from a cage
   :type use_cage: boolean, (optional)
   :arg use_split_materials: Split Materials, Split baked maps per material, using material name in output file (external only)
   :type use_split_materials: boolean, (optional)
   :arg use_automatic_name: Automatic Name, Automatically name the output file with the pass type
   :type use_automatic_name: boolean, (optional)
   :arg uv_layer: UV Layer, UV layer to override active
   :type uv_layer: string, (optional, never None)

.. function:: bake_image()

   Bake image textures of selected objects

.. function:: camera_add(*, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a camera object to the scene

   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: camera_custom_update()

   Update custom camera with new parameters from the shader

.. function:: clear_override_library()

   Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable

.. function:: collection_add()

   Add an object to a new collection

.. function:: collection_external_asset_drop(*, session_uid=0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), use_instance=True, drop_x=0, drop_y=0, collection='')

   Add the dragged collection to the scene

   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg use_instance: Instance, Add the dropped collection as collection instance
   :type use_instance: boolean, (optional)
   :arg drop_x: Drop X, X-coordinate (screen space) to place the new object under
   :type drop_x: int in [-inf, inf], (optional)
   :arg drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
   :type drop_y: int in [-inf, inf], (optional)
   :arg collection: Collection
   :type collection: enum in [], (optional)

.. function:: collection_instance_add(*, name="Collection", collection='', align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), session_uid=0, drop_x=0, drop_y=0)

   Add a collection instance

   :arg name: Name, Collection name to add
   :type name: string, (optional, never None)
   :arg collection: Collection
   :type collection: enum in [], (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)
   :arg drop_x: Drop X, X-coordinate (screen space) to place the new object under
   :type drop_x: int in [-inf, inf], (optional)
   :arg drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
   :type drop_y: int in [-inf, inf], (optional)

.. function:: collection_link(*, collection='')

   Add an object to an existing collection

   :arg collection: Collection
   :type collection: enum in [], (optional)

.. function:: collection_objects_select()

   Select all objects in collection

.. function:: collection_remove()

   Remove the active object from this collection

.. function:: collection_unlink()

   Unlink the collection from all objects

.. function:: constraint_add(*, type='')

   Add a constraint to the active object

   :arg type: Type
   :type type: enum in [], (optional)

.. function:: constraint_add_with_targets(*, type='')

   Add a constraint to the active object, with target (where applicable) set to the selected objects/bones

   :arg type: Type
   :type type: enum in [], (optional)

.. function:: constraints_clear()

   Clear all constraints from the selected objects

.. function:: constraints_copy()

   Copy constraints to other selected objects

.. function:: convert(*, target='MESH', keep_original=False, merge_customdata=True, thickness=5, faces=True, offset=0.01)

   Convert selected objects to another type

   :arg target: Target, Type of object to convert to

      * ``CURVE``
        Curve -- Curve from Mesh or Text objects.
      * ``MESH``
        Mesh -- Mesh from Curve, Surface, Metaball, Text, or Point Cloud objects.
      * ``POINTCLOUD``
        Point Cloud -- Point Cloud from Mesh objects.
      * ``CURVES``
        Curves -- Curves from evaluated curve data.
      * ``GREASEPENCIL``
        Grease Pencil -- Grease Pencil from Curve or Mesh objects.
   :type target: enum in [``'CURVE'``, ``'MESH'``, ``'POINTCLOUD'``, ``'CURVES'``, ``'GREASEPENCIL'``], (optional)
   :arg keep_original: Keep Original, Keep original objects instead of replacing them
   :type keep_original: boolean, (optional)
   :arg merge_customdata: Merge UVs, Merge UV coordinates that share a vertex to account for imprecision in some modifiers
   :type merge_customdata: boolean, (optional)
   :arg thickness: Thickness
   :type thickness: int in [1, 100], (optional)
   :arg faces: Export Faces, Export faces as filled strokes
   :type faces: boolean, (optional)
   :arg offset: Stroke Offset, Offset strokes from fill
   :type offset: float in [0, inf], (optional)

.. function:: correctivesmooth_bind(*, modifier="")

   Bind base pose in Corrective Smooth modifier

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: curves_empty_hair_add(*, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add an empty curve object to the scene with the selected mesh as surface

   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: curves_random_add(*, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a curves object with random curves to the scene

   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: data_instance_add(*, name="", session_uid=0, type='ACTION', align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), drop_x=0, drop_y=0)

   Add an object data instance

   :arg name: Name, Name of the data-block to use by the operator
   :type name: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)
   :arg type: Type
   :type type: enum in :ref:`rna_enum_id_type_items`, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg drop_x: Drop X, X-coordinate (screen space) to place the new object under
   :type drop_x: int in [-inf, inf], (optional)
   :arg drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
   :type drop_y: int in [-inf, inf], (optional)

.. function:: data_transfer(*, use_reverse_transfer=False, use_freeze=False, data_type='', use_create=True, vert_mapping='NEAREST', edge_mapping='NEAREST', loop_mapping='NEAREST_POLYNOR', poly_mapping='NEAREST', use_auto_transform=False, use_object_transform=True, use_max_distance=False, max_distance=1.0, ray_radius=0.0, islands_precision=0.1, layers_select_src='ACTIVE', layers_select_dst='ACTIVE', mix_mode='REPLACE', mix_factor=1.0)

   Transfer data layer(s) (weights, edge sharp, etc.) from active to selected meshes

   :arg use_reverse_transfer: Reverse Transfer, Transfer from selected objects to active one
   :type use_reverse_transfer: boolean, (optional)
   :arg use_freeze: Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry
   :type use_freeze: boolean, (optional)
   :arg data_type: Data Type, Which data to transfer

      * ``VGROUP_WEIGHTS``
        Vertex Group(s) -- Transfer active or all vertex groups.
      * ``BEVEL_WEIGHT_VERT``
        Bevel Weight -- Transfer bevel weights.
      * ``COLOR_VERTEX``
        Colors -- Color Attributes.
      * ``SHARP_EDGE``
        Sharp -- Transfer sharp mark.
      * ``SEAM``
        UV Seam -- Transfer UV seam mark.
      * ``CREASE``
        Subdivision Crease -- Transfer crease values.
      * ``BEVEL_WEIGHT_EDGE``
        Bevel Weight -- Transfer bevel weights.
      * ``FREESTYLE_EDGE``
        Freestyle Mark -- Transfer Freestyle edge mark.
      * ``CUSTOM_NORMAL``
        Custom Normals -- Transfer custom normals.
      * ``COLOR_CORNER``
        Colors -- Color Attributes.
      * ``UV``
        UVs -- Transfer UV layers.
      * ``SMOOTH``
        Smooth -- Transfer flat/smooth mark.
      * ``FREESTYLE_FACE``
        Freestyle Mark -- Transfer Freestyle face mark.
   :type data_type: enum in [``'VGROUP_WEIGHTS'``, ``'BEVEL_WEIGHT_VERT'``, ``'COLOR_VERTEX'``, ``'SHARP_EDGE'``, ``'SEAM'``, ``'CREASE'``, ``'BEVEL_WEIGHT_EDGE'``, ``'FREESTYLE_EDGE'``, ``'CUSTOM_NORMAL'``, ``'COLOR_CORNER'``, ``'UV'``, ``'SMOOTH'``, ``'FREESTYLE_FACE'``], (optional)
   :arg use_create: Create Data, Add data layers on destination meshes if needed
   :type use_create: boolean, (optional)
   :arg vert_mapping: Vertex Mapping, Method used to map source vertices to destination ones
   :type vert_mapping: enum in :ref:`rna_enum_dt_method_vertex_items`, (optional)
   :arg edge_mapping: Edge Mapping, Method used to map source edges to destination ones
   :type edge_mapping: enum in :ref:`rna_enum_dt_method_edge_items`, (optional)
   :arg loop_mapping: Face Corner Mapping, Method used to map source faces' corners to destination ones
   :type loop_mapping: enum in :ref:`rna_enum_dt_method_loop_items`, (optional)
   :arg poly_mapping: Face Mapping, Method used to map source faces to destination ones
   :type poly_mapping: enum in :ref:`rna_enum_dt_method_poly_items`, (optional)
   :arg use_auto_transform: Auto Transform, Automatically compute transformation to get the best possible match between source and destination meshes.Warning: Results will never be as good as manual matching of objects
   :type use_auto_transform: boolean, (optional)
   :arg use_object_transform: Object Transform, Evaluate source and destination meshes in global space
   :type use_object_transform: boolean, (optional)
   :arg use_max_distance: Only Neighbor Geometry, Source elements must be closer than given distance from destination one
   :type use_max_distance: boolean, (optional)
   :arg max_distance: Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings
   :type max_distance: float in [0, inf], (optional)
   :arg ray_radius: Ray Radius, 'Width' of rays (especially useful when raycasting against vertices or edges)
   :type ray_radius: float in [0, inf], (optional)
   :arg islands_precision: Islands Precision, Factor controlling precision of islands handling (the higher, the better the results)
   :type islands_precision: float in [0, 10], (optional)
   :arg layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types
   :type layers_select_src: enum in :ref:`rna_enum_dt_layers_select_src_items`, (optional)
   :arg layers_select_dst: Destination Layers Matching, How to match source and destination layers
   :type layers_select_dst: enum in :ref:`rna_enum_dt_layers_select_dst_items`, (optional)
   :arg mix_mode: Mix Mode, How to affect destination elements with source values
   :type mix_mode: enum in :ref:`rna_enum_dt_mix_mode_items`, (optional)
   :arg mix_factor: Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode)
   :type mix_factor: float in [0, 1], (optional)

.. function:: datalayout_transfer(*, modifier="", data_type='', use_delete=False, layers_select_src='ACTIVE', layers_select_dst='ACTIVE')

   Transfer layout of data layer(s) from active to selected meshes

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)
   :arg data_type: Data Type, Which data to transfer

      * ``VGROUP_WEIGHTS``
        Vertex Group(s) -- Transfer active or all vertex groups.
      * ``BEVEL_WEIGHT_VERT``
        Bevel Weight -- Transfer bevel weights.
      * ``COLOR_VERTEX``
        Colors -- Color Attributes.
      * ``SHARP_EDGE``
        Sharp -- Transfer sharp mark.
      * ``SEAM``
        UV Seam -- Transfer UV seam mark.
      * ``CREASE``
        Subdivision Crease -- Transfer crease values.
      * ``BEVEL_WEIGHT_EDGE``
        Bevel Weight -- Transfer bevel weights.
      * ``FREESTYLE_EDGE``
        Freestyle Mark -- Transfer Freestyle edge mark.
      * ``CUSTOM_NORMAL``
        Custom Normals -- Transfer custom normals.
      * ``COLOR_CORNER``
        Colors -- Color Attributes.
      * ``UV``
        UVs -- Transfer UV layers.
      * ``SMOOTH``
        Smooth -- Transfer flat/smooth mark.
      * ``FREESTYLE_FACE``
        Freestyle Mark -- Transfer Freestyle face mark.
   :type data_type: enum in [``'VGROUP_WEIGHTS'``, ``'BEVEL_WEIGHT_VERT'``, ``'COLOR_VERTEX'``, ``'SHARP_EDGE'``, ``'SEAM'``, ``'CREASE'``, ``'BEVEL_WEIGHT_EDGE'``, ``'FREESTYLE_EDGE'``, ``'CUSTOM_NORMAL'``, ``'COLOR_CORNER'``, ``'UV'``, ``'SMOOTH'``, ``'FREESTYLE_FACE'``], (optional)
   :arg use_delete: Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source
   :type use_delete: boolean, (optional)
   :arg layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types
   :type layers_select_src: enum in :ref:`rna_enum_dt_layers_select_src_items`, (optional)
   :arg layers_select_dst: Destination Layers Matching, How to match source and destination layers
   :type layers_select_dst: enum in :ref:`rna_enum_dt_layers_select_dst_items`, (optional)

.. function:: delete(*, use_global=False, confirm=True)

   Delete selected objects

   :arg use_global: Delete Globally, Remove object from all scenes
   :type use_global: boolean, (optional)
   :arg confirm: Confirm, Prompt for confirmation
   :type confirm: boolean, (optional)

.. function:: drop_geometry_nodes(*, session_uid=0, show_datablock_in_modifier=True)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg session_uid: Session UID, Session UID of the geometry node group being dropped
   :type session_uid: int in [-inf, inf], (optional)
   :arg show_datablock_in_modifier: Show the datablock selector in the modifier
   :type show_datablock_in_modifier: boolean, (optional)

.. function:: drop_named_material(*, name="", session_uid=0)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg name: Name, Name of the data-block to use by the operator
   :type name: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)

.. function:: duplicate(*, linked=False, mode='TRANSLATION')

   Duplicate selected objects

   :arg linked: Linked, Duplicate object but not object data, linking to the original data
   :type linked: boolean, (optional)
   :arg mode: Mode
   :type mode: enum in :ref:`rna_enum_transform_mode_type_items`, (optional)

.. function:: duplicate_move(*, OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Duplicate the selected objects and move them

   :arg OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
   :type OBJECT_OT_duplicate: :class:`OBJECT_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: duplicate_move_linked(*, OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Duplicate the selected objects, but not their object data, and move them

   :arg OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
   :type OBJECT_OT_duplicate: :class:`OBJECT_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: duplicates_make_real(*, use_base_parent=False, use_hierarchy=False)

   Make instanced objects attached to this object real

   :arg use_base_parent: Parent, Parent newly created objects to the original instancer
   :type use_base_parent: boolean, (optional)
   :arg use_hierarchy: Keep Hierarchy, Maintain parent child relationships
   :type use_hierarchy: boolean, (optional)

.. function:: editmode_toggle()

   Toggle object's edit mode

.. function:: effector_add(*, type='FORCE', radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add an empty object with a physics effector to the scene

   :arg type: Type
   :type type: enum in [``'FORCE'``, ``'WIND'``, ``'VORTEX'``, ``'MAGNET'``, ``'HARMONIC'``, ``'CHARGE'``, ``'LENNARDJ'``, ``'TEXTURE'``, ``'GUIDE'``, ``'BOID'``, ``'TURBULENCE'``, ``'DRAG'``, ``'FLUID'``], (optional)
   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: empty_add(*, type='PLAIN_AXES', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add an empty object to the scene

   :arg type: Type
   :type type: enum in :ref:`rna_enum_object_empty_drawtype_items`, (optional)
   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: empty_image_add(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', name="", session_uid=0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), background=False)

   Add an empty image type to scene with data

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
   :arg relative_path: Relative Path, Select the file relative to the blend file
   :type relative_path: boolean, (optional)
   :arg show_multiview: Enable Multi-View
   :type show_multiview: boolean, (optional)
   :arg use_multiview: Use Multi-View
   :type use_multiview: boolean, (optional)
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

      * ``DEFAULT``
        Default -- Automatically determine sort method for files.
      * ``FILE_SORT_ALPHA``
        Name -- Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION``
        Extension -- Sort the file list by extension/type.
      * ``FILE_SORT_TIME``
        Modified Date -- Sort files by modification time.
      * ``FILE_SORT_SIZE``
        Size -- Sort files by size.
      * ``ASSET_CATALOG``
        Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
   :type sort_method: enum in [``'DEFAULT'``, ``'FILE_SORT_ALPHA'``, ``'FILE_SORT_EXTENSION'``, ``'FILE_SORT_TIME'``, ``'FILE_SORT_SIZE'``, ``'ASSET_CATALOG'``], (optional)
   :arg name: Name, Name of the data-block to use by the operator
   :type name: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg background: Put in Background, Make the image render behind all objects
   :type background: boolean, (optional)

.. function:: explode_refresh(*, modifier="")

   Refresh data in the Explode modifier

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: forcefield_toggle()

   Toggle object's force field

.. function:: geometry_node_bake_delete_single(*, session_uid=0, modifier_name="", bake_id=0)

   Delete baked data of a single bake node or simulation

   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)
   :arg modifier_name: Modifier Name, Name of the modifier that contains the node
   :type modifier_name: string, (optional, never None)
   :arg bake_id: Bake ID, Nested node id of the node
   :type bake_id: int in [0, inf], (optional)

.. function:: geometry_node_bake_pack_single(*, session_uid=0, modifier_name="", bake_id=0)

   Pack baked data from disk into the .blend file

   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)
   :arg modifier_name: Modifier Name, Name of the modifier that contains the node
   :type modifier_name: string, (optional, never None)
   :arg bake_id: Bake ID, Nested node id of the node
   :type bake_id: int in [0, inf], (optional)

.. function:: geometry_node_bake_single(*, session_uid=0, modifier_name="", bake_id=0)

   Bake a single bake node or simulation

   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)
   :arg modifier_name: Modifier Name, Name of the modifier that contains the node
   :type modifier_name: string, (optional, never None)
   :arg bake_id: Bake ID, Nested node id of the node
   :type bake_id: int in [0, inf], (optional)

.. function:: geometry_node_bake_unpack_single(*, session_uid=0, modifier_name="", bake_id=0, method='USE_LOCAL')

   Unpack baked data from the .blend file to disk

   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)
   :arg modifier_name: Modifier Name, Name of the modifier that contains the node
   :type modifier_name: string, (optional, never None)
   :arg bake_id: Bake ID, Nested node id of the node
   :type bake_id: int in [0, inf], (optional)
   :arg method: Method, How to unpack
   :type method: enum in [``'USE_LOCAL'``, ``'WRITE_LOCAL'``, ``'USE_ORIGINAL'``, ``'WRITE_ORIGINAL'``], (optional)

.. function:: geometry_node_tree_copy_assign()

   Copy the active geometry node group and assign it to the active modifier

.. function:: geometry_nodes_input_attribute_toggle(*, input_name="", modifier_name="")

   Switch between an attribute and a single value to define the data for every element

   :arg input_name: Input Name
   :type input_name: string, (optional, never None)
   :arg modifier_name: Modifier Name
   :type modifier_name: string, (optional, never None)

.. function:: geometry_nodes_move_to_nodes(*, use_selected_objects=False)

   Move inputs and outputs from in the modifier to a new node group

   :arg use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
   :type use_selected_objects: boolean, (optional)
   :File: `startup\bl_operators\geometry_nodes.py\:277 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\geometry_nodes.py#L277>`__


.. function:: grease_pencil_add(*, type='EMPTY', use_in_front=True, stroke_depth_offset=0.05, use_lights=True, stroke_depth_order='3D', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a Grease Pencil object to the scene

   :arg type: Type
   :type type: enum in :ref:`rna_enum_object_gpencil_type_items`, (optional)
   :arg use_in_front: Show In Front, Show Line Art Grease Pencil in front of everything
   :type use_in_front: boolean, (optional)
   :arg stroke_depth_offset: Stroke Offset, Stroke offset for the Line Art modifier
   :type stroke_depth_offset: float in [0, inf], (optional)
   :arg use_lights: Use Lights, Use lights for this Grease Pencil object
   :type use_lights: boolean, (optional)
   :arg stroke_depth_order: Stroke Depth Order, Defines how the strokes are ordered in 3D space (for objects not displayed 'In Front')

      * ``2D``
        2D Layers -- Display strokes using Grease Pencil layers to define order.
      * ``3D``
        3D Location -- Display strokes using real 3D position in 3D space.
   :type stroke_depth_order: enum in [``'2D'``, ``'3D'``], (optional)
   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: grease_pencil_dash_modifier_segment_add(*, modifier="")

   Add a segment to the dash modifier

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: grease_pencil_dash_modifier_segment_move(*, modifier="", type='UP')

   Move the active dash segment up or down

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)
   :arg type: Type
   :type type: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: grease_pencil_dash_modifier_segment_remove(*, modifier="", index=0)

   Remove the active segment from the dash modifier

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)
   :arg index: Index, Index of the segment to remove
   :type index: int in [0, inf], (optional)

.. function:: grease_pencil_time_modifier_segment_add(*, modifier="")

   Add a segment to the time modifier

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: grease_pencil_time_modifier_segment_move(*, modifier="", type='UP')

   Move the active time segment up or down

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)
   :arg type: Type
   :type type: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: grease_pencil_time_modifier_segment_remove(*, modifier="", index=0)

   Remove the active segment from the time modifier

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)
   :arg index: Index, Index of the segment to remove
   :type index: int in [0, inf], (optional)

.. function:: hide_collection(*, collection_index=-1, toggle=False, extend=False)

   Show only objects in collection (Shift to extend)

   :arg collection_index: Collection Index, Index of the collection to change visibility
   :type collection_index: int in [-1, inf], (optional)
   :arg toggle: Toggle, Toggle visibility
   :type toggle: boolean, (optional)
   :arg extend: Extend, Extend visibility
   :type extend: boolean, (optional)

.. function:: hide_render_clear_all()

   Reveal all render objects by setting the hide render flag

   :File: `startup\bl_operators\object.py\:728 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L728>`__

.. function:: hide_view_clear(*, select=True)

   Reveal temporarily hidden objects

   :arg select: Select, Select revealed objects
   :type select: boolean, (optional)

.. function:: hide_view_set(*, unselected=False)

   Temporarily hide objects from the viewport

   :arg unselected: Unselected, Hide unselected rather than selected objects
   :type unselected: boolean, (optional)

.. function:: hook_add_newob()

   Hook selected vertices to a newly created object

.. function:: hook_add_selob(*, use_bone=False)

   Hook selected vertices to the first selected object

   :arg use_bone: Active Bone, Assign the hook to the hook object's active bone
   :type use_bone: boolean, (optional)

.. function:: hook_assign(*, modifier='')

   Assign the selected vertices to a hook

   :arg modifier: Modifier, Modifier number to assign to
   :type modifier: enum in [], (optional)

.. function:: hook_recenter(*, modifier='')

   Set hook center to cursor position

   :arg modifier: Modifier, Modifier number to assign to
   :type modifier: enum in [], (optional)

.. function:: hook_remove(*, modifier='')

   Remove a hook from the active object

   :arg modifier: Modifier, Modifier number to remove
   :type modifier: enum in [], (optional)

.. function:: hook_reset(*, modifier='')

   Recalculate and clear offset transformation

   :arg modifier: Modifier, Modifier number to assign to
   :type modifier: enum in [], (optional)

.. function:: hook_select(*, modifier='')

   Select affected vertices on mesh

   :arg modifier: Modifier, Modifier number to remove
   :type modifier: enum in [], (optional)

.. function:: instance_offset_from_cursor()

   Set offset used for collection instances based on cursor position

   :File: `startup\bl_operators\object.py\:908 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L908>`__

.. function:: instance_offset_from_object()

   Set offset used for collection instances based on the active object position

   :File: `startup\bl_operators\object.py\:940 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L940>`__

.. function:: instance_offset_to_cursor()

   Set cursor position to the offset used for collection instances

   :File: `startup\bl_operators\object.py\:923 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L923>`__

.. function:: isolate_type_render()

   Hide unselected render objects of same type as active by setting the hide render flag

   :File: `startup\bl_operators\object.py\:708 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L708>`__

.. function:: join()

   Join selected objects into active object

.. function:: join_shapes()

   Add the vertex positions of selected objects as shape keys or update existing shape keys with matching names

.. function:: join_uvs()

   Transfer UV Maps from active to selected objects (needs matching geometry)

   :File: `startup\bl_operators\object.py\:609 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L609>`__

.. function:: laplaciandeform_bind(*, modifier="")

   Bind mesh to system in laplacian deform modifier

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: light_add(*, type='POINT', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a light object to the scene

   :arg type: Type
   :type type: enum in :ref:`rna_enum_light_type_items`, (optional)
   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: light_linking_blocker_collection_new()

   Create new light linking collection used by the active emitter

.. function:: light_linking_blockers_link(*, link_state='INCLUDE')

   Light link selected blockers to the active emitter object

   :arg link_state: Link State, State of the shadow linking

      * ``INCLUDE``
        Include -- Include selected blockers to cast shadows from the active emitter.
      * ``EXCLUDE``
        Exclude -- Exclude selected blockers from casting shadows from the active emitter.
   :type link_state: enum in [``'INCLUDE'``, ``'EXCLUDE'``], (optional)

.. function:: light_linking_blockers_select()

   Select all objects which block light from this emitter

.. function:: light_linking_receiver_collection_new()

   Create new light linking collection used by the active emitter

.. function:: light_linking_receivers_link(*, link_state='INCLUDE')

   Light link selected receivers to the active emitter object

   :arg link_state: Link State, State of the light linking

      * ``INCLUDE``
        Include -- Include selected receivers to receive light from the active emitter.
      * ``EXCLUDE``
        Exclude -- Exclude selected receivers from receiving light from the active emitter.
   :type link_state: enum in [``'INCLUDE'``, ``'EXCLUDE'``], (optional)

.. function:: light_linking_receivers_select()

   Select all objects which receive light from this emitter

.. function:: light_linking_unlink_from_collection()

   Remove this object or collection from the light linking collection

.. function:: lightprobe_add(*, type='SPHERE', radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a light probe object

   :arg type: Type

      * ``SPHERE``
        Sphere -- Light probe that captures precise lighting from all directions at a single point in space.
      * ``PLANE``
        Plane -- Light probe that captures incoming light from a single direction on a plane.
      * ``VOLUME``
        Volume -- Light probe that captures low frequency lighting inside a volume.
   :type type: enum in [``'SPHERE'``, ``'PLANE'``, ``'VOLUME'``], (optional)
   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: lightprobe_cache_bake(*, subset='ALL')

   Bake irradiance volume light cache

   :arg subset: Subset, Subset of probes to update

      * ``ALL``
        All Volumes -- Bake all light probe volumes.
      * ``SELECTED``
        Selected Only -- Only bake selected light probe volumes.
      * ``ACTIVE``
        Active Only -- Only bake the active light probe volume.
   :type subset: enum in [``'ALL'``, ``'SELECTED'``, ``'ACTIVE'``], (optional)

.. function:: lightprobe_cache_free(*, subset='SELECTED')

   Delete cached indirect lighting

   :arg subset: Subset, Subset of probes to update

      * ``ALL``
        All Light Probes -- Delete all light probes' baked lighting data.
      * ``SELECTED``
        Selected Only -- Only delete selected light probes' baked lighting data.
      * ``ACTIVE``
        Active Only -- Only delete the active light probe's baked lighting data.
   :type subset: enum in [``'ALL'``, ``'SELECTED'``, ``'ACTIVE'``], (optional)

.. function:: lineart_bake_strokes(*, bake_all=False)

   Bake Line Art for current Grease Pencil object

   :arg bake_all: Bake All, Bake all Line Art modifiers
   :type bake_all: boolean, (optional)

.. function:: lineart_clear(*, clear_all=False)

   Clear all strokes in current Grease Pencil object

   :arg clear_all: Clear All, Clear all Line Art modifier bakes
   :type clear_all: boolean, (optional)

.. function:: link_to_collection(*, collection_index=-1, is_new=False, new_collection_name="")

   Link objects to a collection

   :arg collection_index: Collection Index, Index of the collection to move to
   :type collection_index: int in [-1, inf], (optional)
   :arg is_new: New, Move objects to a new collection
   :type is_new: boolean, (optional)
   :arg new_collection_name: Name, Name of the newly added collection
   :type new_collection_name: string, (optional, never None)

.. function:: location_clear(*, clear_delta=False)

   Clear the object's location

   :arg clear_delta: Clear Delta, Clear delta location in addition to clearing the normal location transform
   :type clear_delta: boolean, (optional)

.. function:: make_dupli_face()

   Convert objects into instanced faces

   :File: `startup\bl_operators\object.py\:691 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L691>`__

.. function:: make_links_data(*, type='OBDATA')

   Transfer data from active object to selected objects

   :arg type: Type

      * ``OBDATA``
        Link Object Data -- Replace assigned Object Data.
      * ``MATERIAL``
        Link Materials -- Replace assigned Materials.
      * ``ANIMATION``
        Link Animation Data -- Replace assigned Animation Data.
      * ``GROUPS``
        Link Collections -- Replace assigned Collections.
      * ``DUPLICOLLECTION``
        Link Instance Collection -- Replace assigned Collection Instance.
      * ``FONTS``
        Link Fonts to Text -- Replace Text object Fonts.
      * ``MODIFIERS``
        Copy Modifiers -- Replace Modifiers.
      * ``EFFECTS``
        Copy Grease Pencil Effects -- Replace Grease Pencil Effects.
   :type type: enum in [``'OBDATA'``, ``'MATERIAL'``, ``'ANIMATION'``, ``'GROUPS'``, ``'DUPLICOLLECTION'``, ``'FONTS'``, ``'MODIFIERS'``, ``'EFFECTS'``], (optional)

.. function:: make_links_scene(*, scene='')

   Link selection to another scene

   :arg scene: Scene
   :type scene: enum in [], (optional)

.. function:: make_local(*, type='SELECT_OBJECT')

   Make library linked data-blocks local to this file

   :arg type: Type
   :type type: enum in [``'SELECT_OBJECT'``, ``'SELECT_OBDATA'``, ``'SELECT_OBDATA_MATERIAL'``, ``'ALL'``], (optional)

.. function:: make_override_library(*, collection=0)

   Create a local override of the selected linked objects, and their hierarchy of dependencies

   :arg collection: Override Collection, Session UID of the directly linked collection containing the selected object, to make an override from
   :type collection: int in [-inf, inf], (optional)

.. function:: make_single_user(*, type='SELECTED_OBJECTS', object=False, obdata=False, material=False, animation=False, obdata_animation=False)

   Make linked data local to each object

   :arg type: Type
   :type type: enum in [``'SELECTED_OBJECTS'``, ``'ALL'``], (optional)
   :arg object: Object, Make single user objects
   :type object: boolean, (optional)
   :arg obdata: Object Data, Make single user object data
   :type obdata: boolean, (optional)
   :arg material: Materials, Make materials local to each data-block
   :type material: boolean, (optional)
   :arg animation: Object Animation, Make object animation data local to each object
   :type animation: boolean, (optional)
   :arg obdata_animation: Object Data Animation, Make object data (mesh, curve etc.) animation data local to each object
   :type obdata_animation: boolean, (optional)

.. function:: material_slot_add()

   Add a new material slot

.. function:: material_slot_assign()

   Assign active material slot to selection

.. function:: material_slot_copy()

   Copy material to selected objects

.. function:: material_slot_deselect()

   Deselect by active material slot

.. function:: material_slot_move(*, direction='UP')

   Move the active material up/down in the list

   :arg direction: Direction, Direction to move the active material towards
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: material_slot_remove()

   Remove the selected material slot

.. function:: material_slot_remove_all()

   Remove all materials

.. function:: material_slot_remove_unused()

   Remove unused material slots

.. function:: material_slot_select()

   Select by active material slot

.. function:: meshdeform_bind(*, modifier="")

   Bind mesh to cage in mesh deform modifier

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: metaball_add(*, type='BALL', radius=2.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add an metaball object to the scene

   :arg type: Primitive
   :type type: enum in :ref:`rna_enum_metaelem_type_items`, (optional)
   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: mode_set(*, mode='OBJECT', toggle=False)

   Sets the object interaction mode

   :arg mode: Mode
   :type mode: enum in :ref:`rna_enum_object_mode_items`, (optional)
   :arg toggle: Toggle
   :type toggle: boolean, (optional)

.. function:: mode_set_with_submode(*, mode='OBJECT', toggle=False, mesh_select_mode={})

   Sets the object interaction mode

   :arg mode: Mode
   :type mode: enum in :ref:`rna_enum_object_mode_items`, (optional)
   :arg toggle: Toggle
   :type toggle: boolean, (optional)
   :arg mesh_select_mode: Mesh Mode
   :type mesh_select_mode: enum set in :ref:`rna_enum_mesh_select_mode_items`, (optional)

.. function:: modifier_add(*, type='SUBSURF', use_selected_objects=False)

   Add a procedural operation/effect to the active object

   :arg type: Type
   :type type: enum in :ref:`rna_enum_object_modifier_type_items`, (optional)
   :arg use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
   :type use_selected_objects: boolean, (optional)

.. function:: modifier_add_node_group(*, asset_library_type='LOCAL', asset_library_identifier="", relative_asset_identifier="", session_uid=0, use_selected_objects=False)

   Add a procedural operation/effect to the active object

   :arg asset_library_type: Asset Library Type
   :type asset_library_type: enum in :ref:`rna_enum_asset_library_type_items`, (optional)
   :arg asset_library_identifier: Asset Library Identifier
   :type asset_library_identifier: string, (optional, never None)
   :arg relative_asset_identifier: Relative Asset Identifier
   :type relative_asset_identifier: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)
   :arg use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
   :type use_selected_objects: boolean, (optional)

.. function:: modifier_apply(*, modifier="", report=False, merge_customdata=True, single_user=False, all_keyframes=False, use_selected_objects=False)

   Apply modifier and remove from the stack

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)
   :arg report: Report, Create a notification after the operation
   :type report: boolean, (optional)
   :arg merge_customdata: Merge UVs, For mesh objects, merge UV coordinates that share a vertex to account for imprecision in some modifiers
   :type merge_customdata: boolean, (optional)
   :arg single_user: Make Data Single User, Make the object's data single user if needed
   :type single_user: boolean, (optional)
   :arg all_keyframes: Apply to all keyframes, For Grease Pencil objects, apply the modifier to all the keyframes
   :type all_keyframes: boolean, (optional)
   :arg use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
   :type use_selected_objects: boolean, (optional)

.. function:: modifier_apply_as_shapekey(*, keep_modifier=False, modifier="", report=False, use_selected_objects=False)

   Apply modifier as a new shape key and remove from the stack

   :arg keep_modifier: Keep Modifier, Do not remove the modifier from stack
   :type keep_modifier: boolean, (optional)
   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)
   :arg report: Report, Create a notification after the operation
   :type report: boolean, (optional)
   :arg use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
   :type use_selected_objects: boolean, (optional)

.. function:: modifier_convert(*, modifier="")

   Convert particles to a mesh object

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: modifier_copy(*, modifier="", use_selected_objects=False)

   Duplicate modifier at the same position in the stack

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)
   :arg use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
   :type use_selected_objects: boolean, (optional)

.. function:: modifier_copy_to_selected(*, modifier="")

   Copy the modifier from the active object to all selected objects

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: modifier_move_down(*, modifier="")

   Move modifier down in the stack

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: modifier_move_to_index(*, modifier="", index=0, use_selected_objects=False)

   Change the modifier's index in the stack so it evaluates after the set number of others

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)
   :arg index: Index, The index to move the modifier to
   :type index: int in [0, inf], (optional)
   :arg use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
   :type use_selected_objects: boolean, (optional)

.. function:: modifier_move_up(*, modifier="")

   Move modifier up in the stack

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: modifier_remove(*, modifier="", report=False, use_selected_objects=False)

   Remove a modifier from the active object

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)
   :arg report: Report, Create a notification after the operation
   :type report: boolean, (optional)
   :arg use_selected_objects: Selected Objects, Affect all selected objects instead of just the active object
   :type use_selected_objects: boolean, (optional)

.. function:: modifier_set_active(*, modifier="")

   Activate the modifier to use as the context

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: modifiers_clear()

   Clear all modifiers from the selected objects

.. function:: modifiers_copy_to_selected()

   Copy modifiers to other selected objects

.. function:: move_to_collection(*, collection_index=-1, is_new=False, new_collection_name="")

   Move objects to a collection

   :arg collection_index: Collection Index, Index of the collection to move to
   :type collection_index: int in [-1, inf], (optional)
   :arg is_new: New, Move objects to a new collection
   :type is_new: boolean, (optional)
   :arg new_collection_name: Name, Name of the newly added collection
   :type new_collection_name: string, (optional, never None)

.. function:: multires_base_apply(*, modifier="")

   Modify the base mesh to conform to the displaced mesh

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: multires_external_pack()

   Pack displacements from an external file

.. function:: multires_external_save(*, filepath="", hide_props_region=True, check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=True, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', modifier="")

   Save displacements to an external file

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
   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: multires_higher_levels_delete(*, modifier="")

   Deletes the higher resolution mesh, potential loss of detail

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: multires_rebuild_subdiv(*, modifier="")

   Rebuilds all possible subdivisions levels to generate a lower resolution base mesh

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: multires_reshape(*, modifier="")

   Copy vertex coordinates from other object

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: multires_subdivide(*, modifier="", mode='CATMULL_CLARK')

   Add a new level of subdivision

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)
   :arg mode: Subdivision Mode, How the mesh is going to be subdivided to create a new level

      * ``CATMULL_CLARK``
        Catmull-Clark -- Create a new level using Catmull-Clark subdivisions.
      * ``SIMPLE``
        Simple -- Create a new level using simple subdivisions.
      * ``LINEAR``
        Linear -- Create a new level using linear interpolation of the sculpted displacement.
   :type mode: enum in [``'CATMULL_CLARK'``, ``'SIMPLE'``, ``'LINEAR'``], (optional)

.. function:: multires_unsubdivide(*, modifier="")

   Rebuild a lower subdivision level of the current base mesh

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: ocean_bake(*, modifier="", free=False)

   Bake an image sequence of ocean data

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)
   :arg free: Free, Free the bake, rather than generating it
   :type free: boolean, (optional)

.. function:: origin_clear()

   Clear the object's origin

.. function:: origin_set(*, type='GEOMETRY_ORIGIN', center='MEDIAN')

   Set the object's origin, by either moving the data, or set to center of data, or use 3D cursor

   :arg type: Type

      * ``GEOMETRY_ORIGIN``
        Geometry to Origin -- Move object geometry to object origin.
      * ``ORIGIN_GEOMETRY``
        Origin to Geometry -- Calculate the center of geometry based on the current pivot point (median, otherwise bounding box).
      * ``ORIGIN_CURSOR``
        Origin to 3D Cursor -- Move object origin to position of the 3D cursor.
      * ``ORIGIN_CENTER_OF_MASS``
        Origin to Center of Mass (Surface) -- Calculate the center of mass from the surface area.
      * ``ORIGIN_CENTER_OF_VOLUME``
        Origin to Center of Mass (Volume) -- Calculate the center of mass from the volume (must be manifold geometry with consistent normals).
   :type type: enum in [``'GEOMETRY_ORIGIN'``, ``'ORIGIN_GEOMETRY'``, ``'ORIGIN_CURSOR'``, ``'ORIGIN_CENTER_OF_MASS'``, ``'ORIGIN_CENTER_OF_VOLUME'``], (optional)
   :arg center: Center
   :type center: enum in [``'MEDIAN'``, ``'BOUNDS'``], (optional)

.. function:: parent_clear(*, type='CLEAR')

   Clear the object's parenting

   :arg type: Type

      * ``CLEAR``
        Clear Parent -- Completely clear the parenting relationship, including involved modifiers if any.
      * ``CLEAR_KEEP_TRANSFORM``
        Clear and Keep Transformation -- As 'Clear Parent', but keep the current visual transformations of the object.
      * ``CLEAR_INVERSE``
        Clear Parent Inverse -- Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.
   :type type: enum in [``'CLEAR'``, ``'CLEAR_KEEP_TRANSFORM'``, ``'CLEAR_INVERSE'``], (optional)

.. function:: parent_inverse_apply()

   Apply the object's parent inverse to its data

.. function:: parent_no_inverse_set(*, keep_transform=False)

   Set the object's parenting without setting the inverse parent correction

   :arg keep_transform: Keep Transform, Preserve the world transform throughout parenting
   :type keep_transform: boolean, (optional)

.. function:: parent_set(*, type='OBJECT', xmirror=False, keep_transform=False)

   Set the object's parenting

   :arg type: Type
   :type type: enum in [``'OBJECT'``, ``'ARMATURE'``, ``'ARMATURE_NAME'``, ``'ARMATURE_AUTO'``, ``'ARMATURE_ENVELOPE'``, ``'BONE'``, ``'BONE_RELATIVE'``, ``'CURVE'``, ``'FOLLOW'``, ``'PATH_CONST'``, ``'LATTICE'``, ``'VERTEX'``, ``'VERTEX_TRI'``], (optional)
   :arg xmirror: X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation
   :type xmirror: boolean, (optional)
   :arg keep_transform: Keep Transform, Apply transformation before parenting
   :type keep_transform: boolean, (optional)

.. function:: particle_system_add()

   Add a particle system

.. function:: particle_system_remove()

   Remove the selected particle system

.. function:: paths_calculate(*, display_type='RANGE', range='SCENE')

   Generate motion paths for the selected objects

   :arg display_type: Display type
   :type display_type: enum in :ref:`rna_enum_motionpath_display_type_items`, (optional)
   :arg range: Computation Range
   :type range: enum in :ref:`rna_enum_motionpath_range_items`, (optional)

.. function:: paths_clear(*, only_selected=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg only_selected: Only Selected, Only clear motion paths of selected objects
   :type only_selected: boolean, (optional)

.. function:: paths_update()

   Recalculate motion paths for selected objects

.. function:: paths_update_visible()

   Recalculate all visible motion paths for objects and poses

.. function:: pointcloud_random_add(*, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a point cloud object to the scene

   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: posemode_toggle()

   Enable or disable posing/selecting bones

.. function:: quadriflow_remesh(*, use_mesh_symmetry=True, use_preserve_sharp=False, use_preserve_boundary=False, preserve_attributes=False, smooth_normals=False, mode='FACES', target_ratio=1.0, target_edge_length=0.1, target_faces=4000, mesh_area=-1.0, seed=0)

   Create a new quad based mesh using the surface data of the current mesh. All data layers will be lost

   :arg use_mesh_symmetry: Use Mesh Symmetry, Generates a symmetrical mesh using the mesh symmetry configuration
   :type use_mesh_symmetry: boolean, (optional)
   :arg use_preserve_sharp: Preserve Sharp, Try to preserve sharp features on the mesh
   :type use_preserve_sharp: boolean, (optional)
   :arg use_preserve_boundary: Preserve Mesh Boundary, Try to preserve mesh boundary on the mesh
   :type use_preserve_boundary: boolean, (optional)
   :arg preserve_attributes: Preserve Attributes, Reproject attributes onto the new mesh
   :type preserve_attributes: boolean, (optional)
   :arg smooth_normals: Smooth Normals, Set the output mesh normals to smooth
   :type smooth_normals: boolean, (optional)
   :arg mode: Mode, How to specify the amount of detail for the new mesh

      * ``RATIO``
        Ratio -- Specify target number of faces relative to the current mesh.
      * ``EDGE``
        Edge Length -- Input target edge length in the new mesh.
      * ``FACES``
        Faces -- Input target number of faces in the new mesh.
   :type mode: enum in [``'RATIO'``, ``'EDGE'``, ``'FACES'``], (optional)
   :arg target_ratio: Ratio, Relative number of faces compared to the current mesh
   :type target_ratio: float in [0, inf], (optional)
   :arg target_edge_length: Edge Length, Target edge length in the new mesh
   :type target_edge_length: float in [1e-07, inf], (optional)
   :arg target_faces: Number of Faces, Approximate number of faces (quads) in the new mesh
   :type target_faces: int in [1, inf], (optional)
   :arg mesh_area: Old Object Face Area, This property is only used to cache the object area for later calculations
   :type mesh_area: float in [-inf, inf], (optional)
   :arg seed: Seed, Random seed to use with the solver. Different seeds will cause the remesher to come up with different quad layouts on the mesh
   :type seed: int in [0, inf], (optional)

.. function:: quick_explode(*, style='EXPLODE', amount=100, frame_duration=50, frame_start=1, frame_end=10, velocity=1.0, fade=True)

   Make selected objects explode

   :arg style: Explode Style
   :type style: enum in [``'EXPLODE'``, ``'BLEND'``], (optional)
   :arg amount: Number of Pieces
   :type amount: int in [2, 10000], (optional)
   :arg frame_duration: Duration
   :type frame_duration: int in [1, 300000], (optional)
   :arg frame_start: Start Frame
   :type frame_start: int in [1, 300000], (optional)
   :arg frame_end: End Frame
   :type frame_end: int in [1, 300000], (optional)
   :arg velocity: Outwards Velocity
   :type velocity: float in [0, 300000], (optional)
   :arg fade: Fade, Fade the pieces over time
   :type fade: boolean, (optional)
   :File: `startup\bl_operators\object_quick_effects.py\:260 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object_quick_effects.py#L260>`__


.. function:: quick_fur(*, density='MEDIUM', length=0.1, radius=0.001, view_percentage=1.0, apply_hair_guides=True, use_noise=True, use_frizz=True)

   Add a fur setup to the selected objects

   :arg density: Density
   :type density: enum in [``'LOW'``, ``'MEDIUM'``, ``'HIGH'``], (optional)
   :arg length: Length
   :type length: float in [0.001, 100], (optional)
   :arg radius: Hair Radius
   :type radius: float in [0, 10], (optional)
   :arg view_percentage: View Percentage
   :type view_percentage: float in [0, 1], (optional)
   :arg apply_hair_guides: Apply Hair Guides
   :type apply_hair_guides: boolean, (optional)
   :arg use_noise: Noise
   :type use_noise: boolean, (optional)
   :arg use_frizz: Frizz
   :type use_frizz: boolean, (optional)
   :File: `startup\bl_operators\object_quick_effects.py\:91 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object_quick_effects.py#L91>`__


.. function:: quick_liquid(*, show_flows=False)

   Make selected objects liquid

   :arg show_flows: Render Liquid Objects, Keep the liquid objects visible during rendering
   :type show_flows: boolean, (optional)
   :File: `startup\bl_operators\object_quick_effects.py\:543 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object_quick_effects.py#L543>`__


.. function:: quick_smoke(*, style='SMOKE', show_flows=False)

   Use selected objects as smoke emitters

   :arg style: Smoke Style
   :type style: enum in [``'SMOKE'``, ``'FIRE'``, ``'BOTH'``], (optional)
   :arg show_flows: Render Smoke Objects, Keep the smoke objects visible during rendering
   :type show_flows: boolean, (optional)
   :File: `startup\bl_operators\object_quick_effects.py\:437 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object_quick_effects.py#L437>`__


.. function:: randomize_transform(*, random_seed=0, use_delta=False, use_loc=True, loc=(0.0, 0.0, 0.0), use_rot=True, rot=(0.0, 0.0, 0.0), use_scale=True, scale_even=False, scale=(1.0, 1.0, 1.0))

   Randomize objects location, rotation, and scale

   :arg random_seed: Random Seed, Seed value for the random generator
   :type random_seed: int in [0, 10000], (optional)
   :arg use_delta: Transform Delta, Randomize delta transform values instead of regular transform
   :type use_delta: boolean, (optional)
   :arg use_loc: Randomize Location, Randomize the location values
   :type use_loc: boolean, (optional)
   :arg loc: Location, Maximum distance the objects can spread over each axis
   :type loc: :class:`mathutils.Vector` of 3 items in [-100, 100], (optional)
   :arg use_rot: Randomize Rotation, Randomize the rotation values
   :type use_rot: boolean, (optional)
   :arg rot: Rotation, Maximum rotation over each axis
   :type rot: :class:`mathutils.Euler` rotation of 3 items in [-3.14159, 3.14159], (optional)
   :arg use_scale: Randomize Scale, Randomize the scale values
   :type use_scale: boolean, (optional)
   :arg scale_even: Scale Even, Use the same scale value for all axis
   :type scale_even: boolean, (optional)
   :arg scale: Scale, Maximum scale randomization over each axis
   :type scale: float array of 3 items in [-100, 100], (optional)
   :File: `startup\bl_operators\object_randomize_transform.py\:161 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object_randomize_transform.py#L161>`__


.. function:: reset_override_library()

   Reset the selected local overrides to their linked references values

.. function:: rotation_clear(*, clear_delta=False)

   Clear the object's rotation

   :arg clear_delta: Clear Delta, Clear delta rotation in addition to clearing the normal rotation transform
   :type clear_delta: boolean, (optional)

.. function:: scale_clear(*, clear_delta=False)

   Clear the object's scale

   :arg clear_delta: Clear Delta, Clear delta scale in addition to clearing the normal scale transform
   :type clear_delta: boolean, (optional)

.. function:: select_all(*, action='TOGGLE')

   Change selection of all visible objects in scene

   :arg action: Action, Selection action to execute

      * ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
      * ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: enum in [``'TOGGLE'``, ``'SELECT'``, ``'DESELECT'``, ``'INVERT'``], (optional)

.. function:: select_by_type(*, extend=False, type='MESH')

   Select all visible objects that are of a type

   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)
   :arg type: Type
   :type type: enum in :ref:`rna_enum_object_type_items`, (optional)

.. function:: select_camera(*, extend=False)

   Select the active camera

   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)
   :File: `startup\bl_operators\object.py\:122 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L122>`__


.. function:: select_grouped(*, extend=False, type='CHILDREN_RECURSIVE')

   Select all visible objects grouped by various properties

   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)
   :arg type: Type

      * ``CHILDREN_RECURSIVE``
        Children.
      * ``CHILDREN``
        Immediate Children.
      * ``PARENT``
        Parent.
      * ``SIBLINGS``
        Siblings -- Shared parent.
      * ``TYPE``
        Type -- Shared object type.
      * ``COLLECTION``
        Collection -- Shared collection.
      * ``HOOK``
        Hook.
      * ``PASS``
        Pass -- Render pass index.
      * ``COLOR``
        Color -- Object color.
      * ``KEYINGSET``
        Keying Set -- Objects included in active Keying Set.
      * ``LIGHT_TYPE``
        Light Type -- Matching light types.
   :type type: enum in [``'CHILDREN_RECURSIVE'``, ``'CHILDREN'``, ``'PARENT'``, ``'SIBLINGS'``, ``'TYPE'``, ``'COLLECTION'``, ``'HOOK'``, ``'PASS'``, ``'COLOR'``, ``'KEYINGSET'``, ``'LIGHT_TYPE'``], (optional)

.. function:: select_hierarchy(*, direction='PARENT', extend=False)

   Select object relative to the active object's position in the hierarchy

   :arg direction: Direction, Direction to select in the hierarchy
   :type direction: enum in [``'PARENT'``, ``'CHILD'``], (optional)
   :arg extend: Extend, Extend the existing selection
   :type extend: boolean, (optional)
   :File: `startup\bl_operators\object.py\:172 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L172>`__


.. function:: select_less()

   Deselect objects at the boundaries of parent/child relationships

.. function:: select_linked(*, extend=False, type='OBDATA')

   Select all visible objects that are linked

   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)
   :arg type: Type
   :type type: enum in [``'OBDATA'``, ``'MATERIAL'``, ``'DUPGROUP'``, ``'PARTICLE'``, ``'LIBRARY'``, ``'LIBRARY_OBDATA'``], (optional)

.. function:: select_mirror(*, extend=False)

   Select the mirror objects of the selected object e.g. "L.sword" and "R.sword"

   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)

.. function:: select_more()

   Select connected parent/child objects

.. function:: select_pattern(*, pattern="*", case_sensitive=False, extend=True)

   Select objects matching a naming pattern

   :arg pattern: Pattern, Name filter using '*', '?' and '[abc]' unix style wildcards
   :type pattern: string, (optional, never None)
   :arg case_sensitive: Case Sensitive, Do a case sensitive compare
   :type case_sensitive: boolean, (optional)
   :arg extend: Extend, Extend the existing selection
   :type extend: boolean, (optional)
   :File: `startup\bl_operators\object.py\:45 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L45>`__


.. function:: select_random(*, ratio=0.5, seed=0, action='SELECT')

   Select or deselect random visible objects

   :arg ratio: Ratio, Portion of items to select randomly
   :type ratio: float in [0, 1], (optional)
   :arg seed: Random Seed, Seed for the random number generator
   :type seed: int in [0, inf], (optional)
   :arg action: Action, Selection action to execute

      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
   :type action: enum in [``'SELECT'``, ``'DESELECT'``], (optional)

.. function:: select_same_collection(*, collection="")

   Select object in the same collection

   :arg collection: Collection, Name of the collection to select
   :type collection: string, (optional, never None)

.. function:: shade_auto_smooth(*, use_auto_smooth=True, angle=0.523599)

   Add modifier to automatically set the sharpness of mesh edges based on the angle between the neighboring faces

   :arg use_auto_smooth: Auto Smooth, Add modifier to set edge sharpness automatically
   :type use_auto_smooth: boolean, (optional)
   :arg angle: Angle, Maximum angle between face normals that will be considered as smooth
   :type angle: float in [0, 3.14159], (optional)

.. function:: shade_flat(*, keep_sharp_edges=True)

   Render and display faces uniform, using face normals

   :arg keep_sharp_edges: Keep Sharp Edges, Don't remove sharp edges, which are redundant with faces shaded smooth
   :type keep_sharp_edges: boolean, (optional)

.. function:: shade_smooth(*, keep_sharp_edges=True)

   Render and display faces smooth, using interpolated vertex normals

   :arg keep_sharp_edges: Keep Sharp Edges, Don't remove sharp edges. Tagged edges will remain sharp
   :type keep_sharp_edges: boolean, (optional)

.. function:: shade_smooth_by_angle(*, angle=0.523599, keep_sharp_edges=True)

   Set the sharpness of mesh edges based on the angle between the neighboring faces

   :arg angle: Angle, Maximum angle between face normals that will be considered as smooth
   :type angle: float in [0, 3.14159], (optional)
   :arg keep_sharp_edges: Keep Sharp Edges, Only add sharp edges instead of clearing existing tags first
   :type keep_sharp_edges: boolean, (optional)

.. function:: shaderfx_add(*, type='FX_BLUR')

   Add a visual effect to the active object

   :arg type: Type
   :type type: enum in :ref:`rna_enum_object_shaderfx_type_items`, (optional)

.. function:: shaderfx_copy(*, shaderfx="")

   Duplicate effect at the same position in the stack

   :arg shaderfx: Shader, Name of the shaderfx to edit
   :type shaderfx: string, (optional, never None)

.. function:: shaderfx_move_down(*, shaderfx="")

   Move effect down in the stack

   :arg shaderfx: Shader, Name of the shaderfx to edit
   :type shaderfx: string, (optional, never None)

.. function:: shaderfx_move_to_index(*, shaderfx="", index=0)

   Change the effect's position in the list so it evaluates after the set number of others

   :arg shaderfx: Shader, Name of the shaderfx to edit
   :type shaderfx: string, (optional, never None)
   :arg index: Index, The index to move the effect to
   :type index: int in [0, inf], (optional)

.. function:: shaderfx_move_up(*, shaderfx="")

   Move effect up in the stack

   :arg shaderfx: Shader, Name of the shaderfx to edit
   :type shaderfx: string, (optional, never None)

.. function:: shaderfx_remove(*, shaderfx="", report=False)

   Remove a effect from the active Grease Pencil object

   :arg shaderfx: Shader, Name of the shaderfx to edit
   :type shaderfx: string, (optional, never None)
   :arg report: Report, Create a notification after the operation
   :type report: boolean, (optional)

.. function:: shape_key_add(*, from_mix=True)

   Add shape key to the object

   :arg from_mix: From Mix, Create the new shape key from the existing mix of keys
   :type from_mix: boolean, (optional)

.. function:: shape_key_clear()

   Reset the weights of all shape keys to 0 or to the closest value respecting the limits

.. function:: shape_key_copy()

   Duplicate the active shape key

.. function:: shape_key_lock(*, action='LOCK')

   Change the lock state of all shape keys of active object

   :arg action: Action, Lock action to execute on vertex groups

      * ``LOCK``
        Lock -- Lock all shape keys.
      * ``UNLOCK``
        Unlock -- Unlock all shape keys.
   :type action: enum in [``'LOCK'``, ``'UNLOCK'``], (optional)

.. function:: shape_key_mirror(*, use_topology=False)

   Mirror the current shape key along the local X axis

   :arg use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
   :type use_topology: boolean, (optional)

.. function:: shape_key_move(*, type='TOP')

   Move the active shape key up/down in the list

   :arg type: Type

      * ``TOP``
        Top -- Top of the list.
      * ``UP``
        Up.
      * ``DOWN``
        Down.
      * ``BOTTOM``
        Bottom -- Bottom of the list.
   :type type: enum in [``'TOP'``, ``'UP'``, ``'DOWN'``, ``'BOTTOM'``], (optional)

.. function:: shape_key_remove(*, all=False, apply_mix=False)

   Remove shape key from the object

   :arg all: All, Remove all shape keys
   :type all: boolean, (optional)
   :arg apply_mix: Apply Mix, Apply current mix of shape keys to the geometry before removing them
   :type apply_mix: boolean, (optional)

.. function:: shape_key_retime()

   Resets the timing for absolute shape keys

.. function:: shape_key_transfer(*, mode='OFFSET', use_clamp=False)

   Copy the active shape key of another selected object to this one

   :arg mode: Transformation Mode, Relative shape positions to the new shape method

      * ``OFFSET``
        Offset -- Apply the relative positional offset.
      * ``RELATIVE_FACE``
        Relative Face -- Calculate relative position (using faces).
      * ``RELATIVE_EDGE``
        Relative Edge -- Calculate relative position (using edges).
   :type mode: enum in [``'OFFSET'``, ``'RELATIVE_FACE'``, ``'RELATIVE_EDGE'``], (optional)
   :arg use_clamp: Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape
   :type use_clamp: boolean, (optional)
   :File: `startup\bl_operators\object.py\:501 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L501>`__


.. function:: simulation_nodes_cache_bake(*, selected=False)

   Bake simulations in geometry nodes modifiers

   :arg selected: Selected, Bake cache on all selected objects
   :type selected: boolean, (optional)

.. function:: simulation_nodes_cache_calculate_to_frame(*, selected=False)

   Calculate simulations in geometry nodes modifiers from the start to current frame

   :arg selected: Selected, Calculate all selected objects instead of just the active object
   :type selected: boolean, (optional)

.. function:: simulation_nodes_cache_delete(*, selected=False)

   Delete cached/baked simulations in geometry nodes modifiers

   :arg selected: Selected, Delete cache on all selected objects
   :type selected: boolean, (optional)

.. function:: skin_armature_create(*, modifier="")

   Create an armature that parallels the skin layout

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: skin_loose_mark_clear(*, action='MARK')

   Mark/clear selected vertices as loose

   :arg action: Action

      * ``MARK``
        Mark -- Mark selected vertices as loose.
      * ``CLEAR``
        Clear -- Set selected vertices as not loose.
   :type action: enum in [``'MARK'``, ``'CLEAR'``], (optional)

.. function:: skin_radii_equalize()

   Make skin radii of selected vertices equal on each axis

.. function:: skin_root_mark()

   Mark selected vertices as roots

.. function:: speaker_add(*, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a speaker object to the scene

   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: subdivision_set(*, level=1, relative=False, ensure_modifier=True)

   Sets a Subdivision Surface level (1 to 5)

   :arg level: Level
   :type level: int in [-100, 100], (optional)
   :arg relative: Relative, Apply the subdivision surface level as an offset relative to the current level
   :type relative: boolean, (optional)
   :arg ensure_modifier: Ensure Modifier, Create the corresponding modifier if it does not exist
   :type ensure_modifier: boolean, (optional)
   :File: `startup\bl_operators\object.py\:245 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L245>`__


.. function:: surfacedeform_bind(*, modifier="")

   Bind mesh to target in surface deform modifier

   :arg modifier: Modifier, Name of the modifier to edit
   :type modifier: string, (optional, never None)

.. function:: text_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a text object to the scene

   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: track_clear(*, type='CLEAR')

   Clear tracking constraint or flag from object

   :arg type: Type
   :type type: enum in [``'CLEAR'``, ``'CLEAR_KEEP_TRANSFORM'``], (optional)

.. function:: track_set(*, type='DAMPTRACK')

   Make the object track another object, using various methods/constraints

   :arg type: Type
   :type type: enum in [``'DAMPTRACK'``, ``'TRACKTO'``, ``'LOCKTRACK'``], (optional)

.. function:: transfer_mode(*, use_flash_on_transfer=True)

   Switches the active object and assigns the same mode to a new one under the mouse cursor, leaving the active mode in the current one

   :arg use_flash_on_transfer: Flash On Transfer, Flash the target object when transferring the mode
   :type use_flash_on_transfer: boolean, (optional)

.. function:: transform_apply(*, location=True, rotation=True, scale=True, properties=True, isolate_users=False)

   Apply the object's transformation to its data

   :arg location: Location
   :type location: boolean, (optional)
   :arg rotation: Rotation
   :type rotation: boolean, (optional)
   :arg scale: Scale
   :type scale: boolean, (optional)
   :arg properties: Apply Properties, Modify properties such as curve vertex radius, font size and bone envelope
   :type properties: boolean, (optional)
   :arg isolate_users: Isolate Multi User Data, Create new object-data users if needed
   :type isolate_users: boolean, (optional)

.. function:: transform_axis_target()

   Interactively point cameras and lights to a location (Ctrl translates)

.. function:: transform_to_mouse(*, name="", session_uid=0, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), drop_x=0, drop_y=0)

   Snap selected item(s) to the mouse location

   :arg name: Name, Object name to place (uses the active object when this and 'session_uid' are unset)
   :type name: string, (optional, never None)
   :arg session_uid: Session UUID, Session UUID of the object to place (uses the active object when this and 'name' are unset)
   :type session_uid: int in [-inf, inf], (optional)
   :arg matrix: Matrix
   :type matrix: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], (optional)
   :arg drop_x: Drop X, X-coordinate (screen space) to place the new object under
   :type drop_x: int in [-inf, inf], (optional)
   :arg drop_y: Drop Y, Y-coordinate (screen space) to place the new object under
   :type drop_y: int in [-inf, inf], (optional)

.. function:: transforms_to_deltas(*, mode='ALL', reset_values=True)

   Convert normal object transforms to delta transforms, any existing delta transforms will be included as well

   :arg mode: Mode, Which transforms to transfer

      * ``ALL``
        All Transforms -- Transfer location, rotation, and scale transforms.
      * ``LOC``
        Location -- Transfer location transforms only.
      * ``ROT``
        Rotation -- Transfer rotation transforms only.
      * ``SCALE``
        Scale -- Transfer scale transforms only.
   :type mode: enum in [``'ALL'``, ``'LOC'``, ``'ROT'``, ``'SCALE'``], (optional)
   :arg reset_values: Reset Values, Clear transform values after transferring to deltas
   :type reset_values: boolean, (optional)
   :File: `startup\bl_operators\object.py\:763 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\object.py#L763>`__


.. function:: unlink_data()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

.. function:: update_shapes()

   Update existing shape keys with the vertex positions of selected objects with matching names

.. function:: vertex_group_add()

   Add a new vertex group to the active object

.. function:: vertex_group_assign()

   Assign the selected vertices to the active vertex group

.. function:: vertex_group_assign_new()

   Assign the selected vertices to a new vertex group

.. function:: vertex_group_clean(*, group_select_mode='', limit=0.0, keep_single=False)

   Remove vertex group assignments which are not required

   :arg group_select_mode: Subset, Define which subset of groups shall be used
   :type group_select_mode: enum in [], (optional)
   :arg limit: Limit, Remove vertices which weight is below or equal to this limit
   :type limit: float in [0, 1], (optional)
   :arg keep_single: Keep Single, Keep verts assigned to at least one group when cleaning
   :type keep_single: boolean, (optional)

.. function:: vertex_group_copy()

   Make a copy of the active vertex group

.. function:: vertex_group_copy_to_selected()

   Replace vertex groups of selected objects by vertex groups of active object

.. function:: vertex_group_deselect()

   Deselect all selected vertices assigned to the active vertex group

.. function:: vertex_group_invert(*, group_select_mode='', auto_assign=True, auto_remove=True)

   Invert active vertex group's weights

   :arg group_select_mode: Subset, Define which subset of groups shall be used
   :type group_select_mode: enum in [], (optional)
   :arg auto_assign: Add Weights, Add vertices from groups that have zero weight before inverting
   :type auto_assign: boolean, (optional)
   :arg auto_remove: Remove Weights, Remove vertices from groups that have zero weight after inverting
   :type auto_remove: boolean, (optional)

.. function:: vertex_group_levels(*, group_select_mode='', offset=0.0, gain=1.0)

   Add some offset and multiply with some gain the weights of the active vertex group

   :arg group_select_mode: Subset, Define which subset of groups shall be used
   :type group_select_mode: enum in [], (optional)
   :arg offset: Offset, Value to add to weights
   :type offset: float in [-1, 1], (optional)
   :arg gain: Gain, Value to multiply weights by
   :type gain: float in [0, inf], (optional)

.. function:: vertex_group_limit_total(*, group_select_mode='', limit=4)

   Limit deform weights associated with a vertex to a specified number by removing lowest weights

   :arg group_select_mode: Subset, Define which subset of groups shall be used
   :type group_select_mode: enum in [], (optional)
   :arg limit: Limit, Maximum number of deform weights
   :type limit: int in [1, 32], (optional)

.. function:: vertex_group_lock(*, action='TOGGLE', mask='ALL')

   Change the lock state of all or some vertex groups of active object

   :arg action: Action, Lock action to execute on vertex groups

      * ``TOGGLE``
        Toggle -- Unlock all vertex groups if there is at least one locked group, lock all in other case.
      * ``LOCK``
        Lock -- Lock all vertex groups.
      * ``UNLOCK``
        Unlock -- Unlock all vertex groups.
      * ``INVERT``
        Invert -- Invert the lock state of all vertex groups.
   :type action: enum in [``'TOGGLE'``, ``'LOCK'``, ``'UNLOCK'``, ``'INVERT'``], (optional)
   :arg mask: Mask, Apply the action based on vertex group selection

      * ``ALL``
        All -- Apply action to all vertex groups.
      * ``SELECTED``
        Selected -- Apply to selected vertex groups.
      * ``UNSELECTED``
        Unselected -- Apply to unselected vertex groups.
      * ``INVERT_UNSELECTED``
        Invert Unselected -- Apply the opposite of Lock/Unlock to unselected vertex groups.
   :type mask: enum in [``'ALL'``, ``'SELECTED'``, ``'UNSELECTED'``, ``'INVERT_UNSELECTED'``], (optional)

.. function:: vertex_group_mirror(*, mirror_weights=True, flip_group_names=True, all_groups=False, use_topology=False)

   Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected

   :arg mirror_weights: Mirror Weights, Mirror weights
   :type mirror_weights: boolean, (optional)
   :arg flip_group_names: Flip Group Names, Flip vertex group names
   :type flip_group_names: boolean, (optional)
   :arg all_groups: All Groups, Mirror all vertex groups weights
   :type all_groups: boolean, (optional)
   :arg use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
   :type use_topology: boolean, (optional)

.. function:: vertex_group_move(*, direction='UP')

   Move the active vertex group up/down in the list

   :arg direction: Direction, Direction to move the active vertex group towards
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: vertex_group_normalize()

   Normalize weights of the active vertex group, so that the highest ones are now 1.0

.. function:: vertex_group_normalize_all(*, group_select_mode='', lock_active=True)

   Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

   :arg group_select_mode: Subset, Define which subset of groups shall be used
   :type group_select_mode: enum in [], (optional)
   :arg lock_active: Lock Active, Keep the values of the active group while normalizing others
   :type lock_active: boolean, (optional)

.. function:: vertex_group_quantize(*, group_select_mode='', steps=4)

   Set weights to a fixed number of steps

   :arg group_select_mode: Subset, Define which subset of groups shall be used
   :type group_select_mode: enum in [], (optional)
   :arg steps: Steps, Number of steps between 0 and 1
   :type steps: int in [1, 1000], (optional)

.. function:: vertex_group_remove(*, all=False, all_unlocked=False)

   Delete the active or all vertex groups from the active object

   :arg all: All, Remove all vertex groups
   :type all: boolean, (optional)
   :arg all_unlocked: All Unlocked, Remove all unlocked vertex groups
   :type all_unlocked: boolean, (optional)

.. function:: vertex_group_remove_from(*, use_all_groups=False, use_all_verts=False)

   Remove the selected vertices from active or all vertex group(s)

   :arg use_all_groups: All Groups, Remove from all groups
   :type use_all_groups: boolean, (optional)
   :arg use_all_verts: All Vertices, Clear the active group
   :type use_all_verts: boolean, (optional)

.. function:: vertex_group_select()

   Select all the vertices assigned to the active vertex group

.. function:: vertex_group_set_active(*, group='')

   Set the active vertex group

   :arg group: Group, Vertex group to set as active
   :type group: enum in [], (optional)

.. function:: vertex_group_smooth(*, group_select_mode='', factor=0.5, repeat=1, expand=0.0)

   Smooth weights for selected vertices

   :arg group_select_mode: Subset, Define which subset of groups shall be used
   :type group_select_mode: enum in [], (optional)
   :arg factor: Factor
   :type factor: float in [0, 1], (optional)
   :arg repeat: Iterations
   :type repeat: int in [1, 10000], (optional)
   :arg expand: Expand/Contract, Expand/contract weights
   :type expand: float in [-1, 1], (optional)

.. function:: vertex_group_sort(*, sort_type='NAME')

   Sort vertex groups

   :arg sort_type: Sort Type, Sort type
   :type sort_type: enum in [``'NAME'``, ``'BONE_HIERARCHY'``], (optional)

.. function:: vertex_parent_set()

   Parent selected objects to the selected vertices

.. function:: vertex_weight_copy()

   Copy weights from active to selected

.. function:: vertex_weight_delete(*, weight_group=-1)

   Delete this weight from the vertex (disabled if vertex group is locked)

   :arg weight_group: Weight Index, Index of source weight in active vertex group
   :type weight_group: int in [-1, inf], (optional)

.. function:: vertex_weight_normalize_active_vertex()

   Normalize active vertex's weights

.. function:: vertex_weight_paste(*, weight_group=-1)

   Copy this group's weight to other selected vertices (disabled if vertex group is locked)

   :arg weight_group: Weight Index, Index of source weight in active vertex group
   :type weight_group: int in [-1, inf], (optional)

.. function:: vertex_weight_set_active(*, weight_group=-1)

   Set as active vertex group

   :arg weight_group: Weight Index, Index of source weight in active vertex group
   :type weight_group: int in [-1, inf], (optional)

.. function:: visual_geometry_to_objects()

   Convert geometry and instances into editable objects and collections

.. function:: visual_transform_apply()

   Apply the object's visual transformation to its data

.. function:: volume_add(*, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add a volume object to the scene

   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: volume_import(*, filepath="", directory="", files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=True, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', use_sequence_detection=True, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Import OpenVDB volume file

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
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
   :arg use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected volume files (based on file names)
   :type use_sequence_detection: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: voxel_remesh()

   Calculates a new manifold mesh based on the volume of the current mesh. All data layers will be lost

.. function:: voxel_size_edit()

   Modify the mesh voxel size interactively used in the voxel remesher

