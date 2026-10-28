SpaceClipEditor(Space)
======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceClipEditor(Space)

   Clip editor space data

   .. attribute:: annotation_source

      Where the annotation comes from

      * ``CLIP``
        Clip -- Show annotation data-block which belongs to movie clip.
      * ``TRACK``
        Track -- Show annotation data-block which belongs to active track.

      :type: enum in [``'CLIP'``, ``'TRACK'``], default ``'CLIP'``

   .. attribute:: blend_factor

      Overlay blending factor of rasterized mask

      :type: float in [0, 1], default 0.7

   .. attribute:: clip

      Movie clip displayed and edited in this space

      :type: :class:`MovieClip`

   .. data:: clip_user

      Parameters defining which frame of the movie clip is displayed

      :type: :class:`MovieClipUser`, (readonly, never None)

   .. attribute:: cursor_location

      2D cursor location for this view

      :type: :class:`mathutils.Vector` of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: lock_selection

      Lock viewport to selected markers during playback

      :type: boolean, default False

   .. attribute:: lock_time_cursor

      Lock curves view to time cursor during playback and tracking

      :type: boolean, default False

   .. attribute:: mask

      Mask displayed and edited in this space

      :type: :class:`Mask`

   .. attribute:: mask_display_type

      Display type for mask splines

      * ``OUTLINE``
        Outline -- Display white edges with black outline.
      * ``DASH``
        Dash -- Display dashed black-white edges.
      * ``BLACK``
        Black -- Display black edges.
      * ``WHITE``
        White -- Display white edges.

      :type: enum in [``'OUTLINE'``, ``'DASH'``, ``'BLACK'``, ``'WHITE'``], default ``'OUTLINE'``

   .. attribute:: mask_overlay_mode

      Overlay mode of rasterized mask

      * ``ALPHACHANNEL``
        Alpha Channel -- Show alpha channel of the mask.
      * ``COMBINED``
        Combined -- Combine space background image with the mask.

      :type: enum in [``'ALPHACHANNEL'``, ``'COMBINED'``], default ``'ALPHACHANNEL'``

   .. attribute:: mode

      Editing context being displayed

      :type: enum in :ref:`rna_enum_clip_editor_mode_items`, default ``'TRACKING'``

   .. attribute:: path_length

      Length of displaying path, in frames

      :type: int in [0, inf], default 20

   .. attribute:: pivot_point

      Pivot center for rotation/scaling

      * ``BOUNDING_BOX_CENTER``
        Bounding Box Center -- Pivot around bounding box center of selected object(s).
      * ``CURSOR``
        2D Cursor -- Pivot around the 2D cursor.
      * ``INDIVIDUAL_ORIGINS``
        Individual Origins -- Pivot around each object's own origin.
      * ``MEDIAN_POINT``
        Median Point -- Pivot around the median point of selected objects.

      :type: enum in [``'BOUNDING_BOX_CENTER'``, ``'CURSOR'``, ``'INDIVIDUAL_ORIGINS'``, ``'MEDIAN_POINT'``], default ``'MEDIAN_POINT'``

   .. data:: scopes

      Scopes to visualize movie clip statistics

      :type: :class:`MovieClipScopes`, (readonly)

   .. attribute:: show_annotation

      Show annotations for this view

      :type: boolean, default True

   .. attribute:: show_blue_channel

      Show blue channel in the frame

      :type: boolean, default True

   .. attribute:: show_bundles

      Show projection of 3D markers into footage

      :type: boolean, default False

   .. attribute:: show_disabled

      Show disabled tracks from the footage

      :type: boolean, default True

   .. attribute:: show_filters

      Show filters for graph editor

      :type: boolean, default False

   .. attribute:: show_gizmo

      Show gizmos of all types

      :type: boolean, default True

   .. attribute:: show_gizmo_navigate

      Viewport navigation gizmo

      :type: boolean, default True

   .. attribute:: show_graph_frames

      Show curve for per-frame average error (camera motion should be solved first)

      :type: boolean, default True

   .. attribute:: show_graph_hidden

      Include channels from objects/bone that are not visible

      :type: boolean, default False

   .. attribute:: show_graph_only_selected

      Only include channels relating to selected objects and data

      :type: boolean, default False

   .. attribute:: show_graph_tracks_error

      Display the reprojection error curve for selected tracks

      :type: boolean, default False

   .. attribute:: show_graph_tracks_motion

      Display the speed curves (in "x" direction red, in "y" direction green) for the selected tracks

      :type: boolean, default True

   .. attribute:: show_green_channel

      Show green channel in the frame

      :type: boolean, default True

   .. attribute:: show_grid

      Show grid showing lens distortion

      :type: boolean, default False

   .. attribute:: show_marker_pattern

      Show pattern boundbox for markers

      :type: boolean, default True

   .. attribute:: show_marker_search

      Show search boundbox for markers

      :type: boolean, default False

   .. attribute:: show_mask_overlay

      :type: boolean, default False

   .. attribute:: show_mask_spline

      :type: boolean, default True

   .. attribute:: show_metadata

      Show metadata of clip

      :type: boolean, default False

   .. attribute:: show_names

      Show track names and status

      :type: boolean, default False

   .. attribute:: show_red_channel

      Show red channel in the frame

      :type: boolean, default True

   .. attribute:: show_region_channels

      :type: boolean, default False

   .. attribute:: show_region_hud

      :type: boolean, default False

   .. attribute:: show_region_toolbar

      :type: boolean, default False

   .. attribute:: show_region_ui

      :type: boolean, default False

   .. attribute:: show_seconds

      Show timing as a timecode instead of frames

      :type: boolean, default False

   .. attribute:: show_stable

      Show stable footage in editor (if stabilization is enabled)

      :type: boolean, default False

   .. attribute:: show_tiny_markers

      Show markers in a more compact manner

      :type: boolean, default False

   .. attribute:: show_track_path

      Show path of how track moves

      :type: boolean, default True

   .. attribute:: use_grayscale_preview

      Display frame in grayscale mode

      :type: boolean, default False

   .. attribute:: use_manual_calibration

      Use manual calibration helpers

      :type: boolean, default False

   .. attribute:: use_mute_footage

      Mute footage and show black background instead

      :type: boolean, default False

   .. attribute:: view

      Type of the clip editor view

      * ``CLIP``
        Clip -- Show editing clip preview.
      * ``GRAPH``
        Graph -- Show graph view for active element.
      * ``DOPESHEET``
        Dope Sheet -- Dope Sheet view for tracking data.

      :type: enum in [``'CLIP'``, ``'GRAPH'``, ``'DOPESHEET'``], default ``'CLIP'``

   .. attribute:: zoom_percentage

      Zoom percentage

      :type: float in [0.4, 80000], default 100.0

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


   .. classmethod:: draw_handler_add(callback, args, region_type, draw_type)
   
      Add a new draw handler to this space type.
      It will be called every time the specified region in the space type will be drawn.
      Note: All arguments are positional only for now.
   
      :arg callback:
         A function that will be called when the region is drawn.
         It gets the specified arguments as input, it's return value is ignored.
      :type callback: Callable[..., Any]
      :arg args: Arguments that will be passed to the callback.
      :type args: tuple[Any, ...]
      :arg region_type: The region type the callback draws in; usually ``WINDOW``. (:class:`bpy.types.Region.type`)
      :type region_type: str
      :arg draw_type: Usually ``POST_PIXEL`` for 2D drawing and ``POST_VIEW`` for 3D drawing. In some cases ``PRE_VIEW`` can be used. ``BACKDROP`` can be used for backdrops in the node editor.
      :type draw_type: str
      :return: Handler that can be removed later on.
      :rtype: object


   .. classmethod:: draw_handler_remove(handler, region_type)
   
      Remove a draw handler that was added previously.
   
      :arg handler: The draw handler that should be removed.
      :type handler: object
      :arg region_type: Region type the callback was added to.
      :type region_type: str


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Space.type`
   * :class:`Space.show_locked_time`
   * :class:`Space.show_region_header`

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
   * :class:`Space.bl_rna_get_subclass`
   * :class:`Space.bl_rna_get_subclass_py`
   * :class:`Space.draw_handler_add`
   * :class:`Space.draw_handler_remove`

