ToolSettings(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ToolSettings(bpy_struct)


   .. attribute:: annotation_stroke_placement_view2d

      * ``IMAGE``
        Image -- Stick stroke to the image.
      * ``VIEW``
        View -- Stick stroke to the view.

      :type: enum in [``'IMAGE'``, ``'VIEW'``], default ``'VIEW'``

   .. attribute:: annotation_stroke_placement_view3d

      How annotation strokes are orientated in 3D space

      * ``CURSOR``
        3D Cursor -- Draw stroke at 3D cursor location.
      * ``VIEW``
        View -- Stick stroke to the view.
      * ``SURFACE``
        Surface -- Stick stroke to surfaces.

      :type: enum in [``'CURSOR'``, ``'VIEW'``, ``'SURFACE'``], default ``'CURSOR'``

   .. attribute:: annotation_thickness

      Thickness of annotation strokes

      :type: int in [1, 10], default 3

   .. attribute:: auto_keying_mode

      Mode of automatic keyframe insertion for objects, bones and masks

      :type: enum in [``'ADD_REPLACE_KEYS'``, ``'REPLACE_KEYS'``], default ``'ADD_REPLACE_KEYS'``

   .. data:: curve_paint_settings

      :type: :class:`CurvePaintSettings`, (readonly, never None)

   .. data:: curves_sculpt

      :type: :class:`CurvesSculpt`, (readonly)

   .. data:: custom_bevel_profile_preset

      Used for defining a profile's path

      :type: :class:`CurveProfile`, (readonly)

   .. attribute:: double_threshold

      Threshold distance for Auto Merge

      :type: float in [0, 1], default 0.001

   .. data:: gpencil_interpolate

      Settings for Grease Pencil interpolation tools

      :type: :class:`GPencilInterpolateSettings`, (readonly)

   .. data:: gpencil_paint

      :type: :class:`GpPaint`, (readonly)

   .. data:: gpencil_sculpt

      Settings for stroke sculpting tools and brushes

      :type: :class:`GPencilSculptSettings`, (readonly)

   .. data:: gpencil_sculpt_paint

      :type: :class:`GpSculptPaint`, (readonly)

   .. attribute:: gpencil_selectmode_edit

      :type: enum in :ref:`rna_enum_grease_pencil_selectmode_items`, default ``'POINT'``

   .. attribute:: gpencil_stroke_placement_view3d

      * ``ORIGIN``
        Origin -- Draw stroke at Object origin.
      * ``CURSOR``
        3D Cursor -- Draw stroke at 3D cursor location.
      * ``SURFACE``
        Surface -- Stick stroke to surfaces.
      * ``STROKE``
        Stroke -- Stick stroke to other strokes.

      :type: enum in [``'ORIGIN'``, ``'CURSOR'``, ``'SURFACE'``, ``'STROKE'``], default ``'ORIGIN'``

   .. attribute:: gpencil_stroke_snap_mode

      * ``NONE``
        All Points -- Snap to all points.
      * ``ENDS``
        End Points -- Snap to first and last points and interpolate.
      * ``FIRST``
        First Point -- Snap to first point.

      :type: enum in [``'NONE'``, ``'ENDS'``, ``'FIRST'``], default ``'NONE'``

   .. attribute:: gpencil_surface_offset

      Offset along the normal when drawing on surfaces

      :type: float in [-inf, inf], default 0.15

   .. data:: gpencil_vertex_paint

      :type: :class:`GpVertexPaint`, (readonly)

   .. data:: gpencil_weight_paint

      :type: :class:`GpWeightPaint`, (readonly)

   .. data:: image_paint

      :type: :class:`ImagePaint`, (readonly)

   .. attribute:: keyframe_type

      Type of keyframes to create when inserting keyframes

      :type: enum in :ref:`rna_enum_beztriple_keyframe_type_items`, default ``'KEYFRAME'``

   .. attribute:: lock_markers

      Prevent marker editing

      :type: boolean, default False

   .. attribute:: lock_object_mode

      Restrict selection to objects using the same mode as the active object, to prevent accidental mode switch when selecting

      :type: boolean, default True

   .. attribute:: mesh_select_mode

      Which mesh elements selection works on

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: normal_vector

      Normal vector used to copy, add or multiply

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. data:: paint_mode

      :type: :class:`PaintModeSettings`, (readonly)

   .. data:: particle_edit

      :type: :class:`ParticleEdit`, (readonly)

   .. attribute:: plane_axis

      The axis used for placing the base region

      :type: enum in :ref:`rna_enum_axis_xyz_items`, default ``'Z'``

   .. attribute:: plane_axis_auto

      Select the closest axis when placing objects (surface overrides)

      :type: boolean, default True

   .. attribute:: plane_depth

      The initial depth used when placing the cursor

      * ``SURFACE``
        Surface -- Start placing on the surface, using the 3D cursor position as a fallback.
      * ``CURSOR_PLANE``
        Cursor Plane -- Start placement using a point projected onto the orientation axis at the 3D cursor position.
      * ``CURSOR_VIEW``
        Cursor View -- Start placement using a point projected onto the view plane at the 3D cursor position.

      :type: enum in [``'SURFACE'``, ``'CURSOR_PLANE'``, ``'CURSOR_VIEW'``], default ``'SURFACE'``

   .. attribute:: plane_orientation

      The initial depth used when placing the cursor

      * ``SURFACE``
        Surface -- Use the surface normal (using the transform orientation as a fallback).
      * ``DEFAULT``
        Default -- Use the current transform orientation.

      :type: enum in [``'SURFACE'``, ``'DEFAULT'``], default ``'SURFACE'``

   .. attribute:: playhead_snap_distance

      Maximum distance for snapping in pixels

      :type: int in [-inf, inf], default 20

   .. attribute:: proportional_distance

      Display size for proportional editing circle

      :type: float in [1e-05, 5000], default 1.0

   .. attribute:: proportional_edit_falloff

      Falloff type for proportional editing mode

      :type: enum in :ref:`rna_enum_proportional_falloff_items`, default ``'SMOOTH'``

   .. attribute:: proportional_size

      Display size for proportional editing circle

      :type: float in [1e-05, 5000], default 1.0

   .. data:: sculpt

      :type: :class:`Sculpt`, (readonly)

   .. data:: sequencer_tool_settings

      :type: :class:`SequencerToolSettings`, (readonly, never None)

   .. attribute:: show_uv_local_view

      Display only faces with the currently displayed image assigned

      :type: boolean, default False

   .. attribute:: snap_angle_increment_2d

      Angle used for rotation increments in 2D editors

      :type: float in [0, 3.14159], default 0.0872665

   .. attribute:: snap_angle_increment_2d_precision

      Precision angle used for rotation increments in 2D editors

      :type: float in [0, 3.14159], default 0.0174533

   .. attribute:: snap_angle_increment_3d

      Angle used for rotation increments in 3D editors

      :type: float in [0, 3.14159], default 0.0872665

   .. attribute:: snap_angle_increment_3d_precision

      Precision angle used for rotation increments in 3D editors

      :type: float in [0, 3.14159], default 0.0174533

   .. attribute:: snap_anim_element

      Type of element to snap to

      :type: enum in :ref:`rna_enum_snap_animation_element_items`, default ``'FRAME'``

   .. attribute:: snap_elements

      Type of element to snap to

      :type: enum set in :ref:`rna_enum_snap_element_items`, default {``'INCREMENT'``}

   .. attribute:: snap_elements_base

      Type of element for the "Snap Base" to snap to

      * ``INCREMENT``
        Increment -- Snap to increments.
      * ``GRID``
        Grid -- Snap to grid.
      * ``VERTEX``
        Vertex -- Snap to vertices.
      * ``EDGE``
        Edge -- Snap to edges.
      * ``FACE``
        Face -- Snap by projecting onto faces.
      * ``VOLUME``
        Volume -- Snap to volume.
      * ``EDGE_MIDPOINT``
        Edge Center -- Snap to the middle of edges.
      * ``EDGE_PERPENDICULAR``
        Edge Perpendicular -- Snap to the nearest point on an edge.

      :type: enum set in {``'INCREMENT'``, ``'GRID'``, ``'VERTEX'``, ``'EDGE'``, ``'FACE'``, ``'VOLUME'``, ``'EDGE_MIDPOINT'``, ``'EDGE_PERPENDICULAR'``}, default {``'INCREMENT'``}

   .. attribute:: snap_elements_individual

      Type of element for individual transformed elements to snap to

      * ``FACE_PROJECT``
        Face Project -- Snap by projecting onto faces.
      * ``FACE_NEAREST``
        Face Nearest -- Snap to nearest point on faces.

      :type: enum set in {``'FACE_PROJECT'``, ``'FACE_NEAREST'``}, default {``'FACE_PROJECT'``}

   .. attribute:: snap_elements_tool

      The target to use while snapping

      * ``GEOMETRY``
        Geometry -- Snap to all geometry.
      * ``DEFAULT``
        Default -- Use the current snap settings.

      :type: enum in [``'GEOMETRY'``, ``'DEFAULT'``], default ``'GEOMETRY'``

   .. attribute:: snap_face_nearest_steps

      Number of steps to break transformation into for face nearest snapping

      :type: int in [1, 100], default 1

   .. attribute:: snap_playhead_element

      Type of element to snap to

      * ``FRAME``
        Frames -- Snap to frame increments.
      * ``SECOND``
        Seconds -- Snap to second increments.
      * ``MARKER``
        Markers -- Snap to markers.
      * ``KEY``
        Keyframes -- Snap to keyframes.
      * ``Strip``
        Strips -- Snap to Strips.

      :type: enum set in {``'FRAME'``, ``'SECOND'``, ``'MARKER'``, ``'KEY'``, ``'Strip'``}, default {``'FRAME'``}

   .. attribute:: snap_playhead_frame_step

      At which interval to snap to frames

      :type: int in [1, 32768], default 2

   .. attribute:: snap_playhead_second_step

      At which interval to snap to seconds

      :type: int in [1, 32768], default 1

   .. attribute:: snap_target

      Which part to snap onto the target

      :type: enum in :ref:`rna_enum_snap_source_items`, default ``'CLOSEST'``

   .. attribute:: snap_uv_element

      Type of element to snap to

      * ``INCREMENT``
        Increment -- Snap to increments of grid.
      * ``GRID``
        Grid -- Snap to grid.
      * ``VERTEX``
        Vertex -- Snap to vertices.

      :type: enum set in {``'INCREMENT'``, ``'GRID'``, ``'VERTEX'``}, default {``'INCREMENT'``}

   .. data:: statvis

      :type: :class:`MeshStatVis`, (readonly, never None)

   .. attribute:: transform_pivot_point

      Pivot center for rotation/scaling

      * ``BOUNDING_BOX_CENTER``
        Bounding Box Center -- Pivot around bounding box center of selected object(s).
      * ``CURSOR``
        3D Cursor -- Pivot around the 3D cursor.
      * ``INDIVIDUAL_ORIGINS``
        Individual Origins -- Pivot around each object's own origin.
      * ``MEDIAN_POINT``
        Median Point -- Pivot around the median point of selected objects.
      * ``ACTIVE_ELEMENT``
        Active Element -- Pivot around active object.

      :type: enum in [``'BOUNDING_BOX_CENTER'``, ``'CURSOR'``, ``'INDIVIDUAL_ORIGINS'``, ``'MEDIAN_POINT'``, ``'ACTIVE_ELEMENT'``], default ``'MEDIAN_POINT'``

   .. data:: unified_paint_settings

      :type: :class:`UnifiedPaintSettings`, (readonly, never None)

   .. attribute:: use_annotation_project_only_selected

      Project the strokes only onto selected objects

      :type: boolean, default False

   .. attribute:: use_annotation_stroke_endpoints

      Only use the first and last parts of the stroke for snapping

      :type: boolean, default False

   .. attribute:: use_auto_normalize

      Ensure all bone-deforming vertex groups add up to 1.0 while weight painting or assigning to vertices

      :type: boolean, default False

   .. attribute:: use_edge_path_live_unwrap

      Changing edge seams recalculates UV unwrap

      :type: boolean, default False

   .. attribute:: use_gpencil_automerge_strokes

      Join the last drawn stroke with previous strokes in the active layer by distance

      :type: boolean, default False

   .. attribute:: use_gpencil_draw_additive

      When creating new frames, the strokes from the previous/active frame are included as the basis for the new one

      :type: boolean, default False

   .. attribute:: use_gpencil_draw_onback

      New strokes are drawn below of all strokes in the layer

      :type: boolean, default False

   .. attribute:: use_gpencil_project_only_selected

      Project the strokes only onto selected objects

      :type: boolean, default False

   .. attribute:: use_gpencil_select_mask_point

      Only sculpt selected stroke points

      :type: boolean, default False

   .. attribute:: use_gpencil_select_mask_segment

      Only sculpt selected stroke points between other strokes

      :type: boolean, default False

   .. attribute:: use_gpencil_select_mask_stroke

      Only sculpt selected strokes

      :type: boolean, default False

   .. attribute:: use_gpencil_thumbnail_list

      Show compact list of colors instead of thumbnails

      :type: boolean, default True

   .. attribute:: use_gpencil_vertex_select_mask_point

      Only paint selected stroke points

      :type: boolean, default False

   .. attribute:: use_gpencil_vertex_select_mask_segment

      Only paint selected stroke points between other strokes

      :type: boolean, default False

   .. attribute:: use_gpencil_vertex_select_mask_stroke

      Only paint selected strokes

      :type: boolean, default False

   .. attribute:: use_gpencil_weight_data_add

      Weight data for new strokes is added according to the current vertex group and weight. If no vertex group selected, weight is not added.

      :type: boolean, default False

   .. attribute:: use_grease_pencil_multi_frame_editing

      Enable multi-frame editing

      :type: boolean, default False

   .. attribute:: use_keyframe_cycle_aware

      For channels with cyclic extrapolation, keyframe insertion is automatically remapped inside the cycle time range, and keeps ends in sync. Curves newly added to actions with a Manual Frame Range and Cyclic Animation are automatically made cyclic.

      :type: boolean, default False

   .. attribute:: use_keyframe_insert_auto

      Automatic keyframe insertion for objects, bones and masks

      :type: boolean, default True

   .. attribute:: use_keyframe_insert_keyingset

      Automatic keyframe insertion using active Keying Set only

      :type: boolean, default False

   .. attribute:: use_lock_relative

      Display bone-deforming groups as if all locked deform groups were deleted, and the remaining ones were re-normalized

      :type: boolean, default False

   .. attribute:: use_mesh_automerge

      Automatically merge vertices moved to the same location

      :type: boolean, default False

   .. attribute:: use_mesh_automerge_and_split

      Automatically split edges and faces

      :type: boolean, default False

   .. attribute:: use_multipaint

      Paint across the weights of all selected bones, maintaining their relative influence

      :type: boolean, default False

   .. attribute:: use_proportional_action

      Proportional editing in action editor

      :type: boolean, default False

   .. attribute:: use_proportional_connected

      Proportional Editing using connected geometry only

      :type: boolean, default False

   .. attribute:: use_proportional_edit

      Proportional edit mode

      :type: boolean, default False

   .. attribute:: use_proportional_edit_mask

      Proportional editing mask mode

      :type: boolean, default False

   .. attribute:: use_proportional_edit_objects

      Proportional editing object mode

      :type: boolean, default False

   .. attribute:: use_proportional_fcurve

      Proportional editing in F-Curve editor

      :type: boolean, default False

   .. attribute:: use_proportional_projected

      Proportional Editing using screen space locations

      :type: boolean, default False

   .. attribute:: use_record_with_nla

      Add a new NLA Track + Strip for every loop/pass made over the animation to allow non-destructive tweaking

      :type: boolean, default False

   .. attribute:: use_snap

      Snap during transform

      :type: boolean, default False

   .. attribute:: use_snap_align_rotation

      Align rotation with the snapping target

      :type: boolean, default False

   .. attribute:: use_snap_anim

      Enable snapping when transforming keyframes

      :type: boolean, default True

   .. attribute:: use_snap_backface_culling

      Exclude back facing geometry from snapping

      :type: boolean, default False

   .. attribute:: use_snap_driver

      Enable snapping when transforming keys in the Driver Editor

      :type: boolean, default False

   .. attribute:: use_snap_driver_absolute

      Snap to full values

      :type: boolean, default False

   .. attribute:: use_snap_edit

      Snap onto non-active objects in edit mode (edit mode only)

      :type: boolean, default True

   .. attribute:: use_snap_grid_absolute

      Absolute grid alignment while translating (based on the pivot center)

      :type: boolean, default False

   .. attribute:: use_snap_node

      Snap Node during transform

      :type: boolean, default False

   .. attribute:: use_snap_nonedit

      Snap onto objects not in edit mode (edit mode only)

      :type: boolean, default True

   .. attribute:: use_snap_peel_object

      Consider objects as whole when finding volume center

      :type: boolean, default False

   .. attribute:: use_snap_playhead

      Snap playhead when scrubbing

      :type: boolean, default False

   .. attribute:: use_snap_rotate

      Rotate is affected by the snapping settings

      :type: boolean, default False

   .. attribute:: use_snap_scale

      Scale is affected by snapping settings

      :type: boolean, default False

   .. attribute:: use_snap_selectable

      Snap only onto objects that are selectable

      :type: boolean, default False

   .. attribute:: use_snap_self

      Snap onto itself only if enabled (edit mode only)

      :type: boolean, default True

   .. attribute:: use_snap_sequencer

      Snap strips during transform

      :type: boolean, default True

   .. attribute:: use_snap_time_absolute

      Absolute time alignment when transforming keyframes

      :type: boolean, default False

   .. attribute:: use_snap_to_same_target

      Snap only to target that source was initially near ("Face Nearest" only)

      :type: boolean, default False

   .. attribute:: use_snap_translate

      Move is affected by snapping settings

      :type: boolean, default True

   .. attribute:: use_snap_uv

      Snap UV during transform

      :type: boolean, default False

   .. attribute:: use_transform_correct_face_attributes

      Correct data such as UVs and color attributes when transforming

      :type: boolean, default False

   .. attribute:: use_transform_correct_keep_connected

      During the Face Attributes correction, merge attributes connected to the same vertex

      :type: boolean, default False

   .. attribute:: use_transform_data_origin

      Transform object origins, while leaving the shape in place

      :type: boolean, default False

   .. attribute:: use_transform_pivot_point_align

      Only transform object locations, without affecting rotation or scaling

      :type: boolean, default False

   .. attribute:: use_transform_skip_children

      Transform the parents, leaving the children in place

      :type: boolean, default False

   .. attribute:: use_uv_select_sync

      Keep UV and edit mode mesh selection in sync

      :type: boolean, default False

   .. data:: uv_sculpt

      :type: :class:`UvSculpt`, (readonly)

   .. attribute:: uv_sculpt_all_islands

      Brush operates on all islands

      :type: boolean, default False

   .. attribute:: uv_sculpt_lock_borders

      Disable editing of boundary edges

      :type: boolean, default False

   .. attribute:: uv_select_mode

      UV selection and display mode

      :type: enum in :ref:`rna_enum_mesh_select_mode_uv_items`, default ``'VERTEX'``

   .. attribute:: uv_sticky_select_mode

      Method for extending UV vertex selection

      * ``DISABLED``
        Disabled -- Sticky vertex selection disabled.
      * ``SHARED_LOCATION``
        Shared Location -- Select UVs that are at the same location and share a mesh vertex.
      * ``SHARED_VERTEX``
        Shared Vertex -- Select UVs that share a mesh vertex, whether or not they are at the same location.

      :type: enum in [``'DISABLED'``, ``'SHARED_LOCATION'``, ``'SHARED_VERTEX'``], default ``'SHARED_LOCATION'``

   .. attribute:: vertex_group_subset

      Filter Vertex groups for Display

      * ``ALL``
        All -- All Vertex Groups.
      * ``BONE_DEFORM``
        Deform -- Vertex Groups assigned to Deform Bones.
      * ``OTHER_DEFORM``
        Other -- Vertex Groups assigned to non Deform Bones.

      :type: enum in [``'ALL'``, ``'BONE_DEFORM'``, ``'OTHER_DEFORM'``], default ``'ALL'``

   .. attribute:: vertex_group_user

      Display unweighted vertices

      * ``NONE``
        None.
      * ``ACTIVE``
        Active -- Show vertices with no weights in the active group.
      * ``ALL``
        All -- Show vertices with no weights in any group.

      :type: enum in [``'NONE'``, ``'ACTIVE'``, ``'ALL'``], default ``'NONE'``

   .. attribute:: vertex_group_weight

      Weight to assign in vertex groups

      :type: float in [0, 1], default 1.0

   .. data:: vertex_paint

      :type: :class:`VertexPaint`, (readonly)

   .. data:: weight_paint

      :type: :class:`VertexPaint`, (readonly)

   .. attribute:: workspace_tool_type

      Action when dragging in the viewport

      :type: enum in [``'DEFAULT'``, ``'FALLBACK'``], default ``'FALLBACK'``

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct` subclass


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.id_properties_clear`
   * :class:`bpy_struct.id_properties_ensure`
   * :class:`bpy_struct.id_properties_ui`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_overridable_library`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.pop`
   * :class:`bpy_struct.property_overridable_library_set`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.rna_ancestors`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   * :class:`Context.tool_settings`
   * :class:`Scene.tool_settings`

