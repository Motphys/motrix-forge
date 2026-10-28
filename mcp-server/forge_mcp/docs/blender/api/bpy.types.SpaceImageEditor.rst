SpaceImageEditor(Space)
=======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceImageEditor(Space)

   Image and UV editor space data

   .. attribute:: blend_factor

      Overlay blending factor of rasterized mask

      :type: float in [0, 1], default 0.0

   .. attribute:: cursor_location

      2D cursor location for this view

      :type: :class:`mathutils.Vector` of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: display_channels

      Channels of the image to display

      * ``COLOR_ALPHA``
        Color & Alpha -- Display image with RGB colors and alpha transparency.
      * ``COLOR``
        Color -- Display image with RGB colors.
      * ``ALPHA``
        Alpha -- Display alpha transparency channel.
      * ``Z_BUFFER``
        Z-Buffer -- Display Z-buffer associated with image (mapped from camera clip start to end).
      * ``RED``
        Red.
      * ``GREEN``
        Green.
      * ``BLUE``
        Blue.

      :type: enum in [``'COLOR_ALPHA'``, ``'COLOR'``, ``'ALPHA'``, ``'Z_BUFFER'``, ``'RED'``, ``'GREEN'``, ``'BLUE'``], default ``'COLOR'``

   .. attribute:: grease_pencil

      Grease Pencil data for this space

      :type: :class:`GreasePencil`

   .. attribute:: image

      Image displayed and edited in this space

      :type: :class:`Image`

   .. data:: image_user

      Parameters defining which layer, pass and frame of the image is displayed

      :type: :class:`ImageUser`, (readonly, never None)

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

      :type: enum in :ref:`rna_enum_space_image_mode_all_items`, default ``'VIEW'``

   .. data:: overlay

      Settings for display of overlays in the UV/Image editor

      :type: :class:`SpaceImageOverlay`, (readonly, never None)

   .. attribute:: pivot_point

      Rotation/Scaling Pivot

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

      :type: enum in [``'BOUNDING_BOX_CENTER'``, ``'CURSOR'``, ``'INDIVIDUAL_ORIGINS'``, ``'MEDIAN_POINT'``, ``'ACTIVE_ELEMENT'``], default ``'BOUNDING_BOX_CENTER'``

   .. data:: sample_histogram

      Sampled colors along line

      :type: :class:`Histogram`, (readonly)

   .. data:: scopes

      Scopes to visualize image statistics

      :type: :class:`Scopes`, (readonly)

   .. attribute:: show_annotation

      Show annotations for this view

      :type: boolean, default False

   .. attribute:: show_gizmo

      Show gizmos of all types

      :type: boolean, default False

   .. attribute:: show_gizmo_navigate

      Viewport navigation gizmo

      :type: boolean, default False

   .. attribute:: show_mask_overlay

      :type: boolean, default False

   .. attribute:: show_mask_spline

      :type: boolean, default False

   .. data:: show_maskedit

      Show Mask editing related properties

      :type: boolean, default False, (readonly)

   .. data:: show_paint

      Show paint related properties

      :type: boolean, default False, (readonly)

   .. attribute:: show_region_asset_shelf

      :type: boolean, default False

   .. attribute:: show_region_hud

      :type: boolean, default False

   .. attribute:: show_region_tool_header

      :type: boolean, default False

   .. attribute:: show_region_toolbar

      :type: boolean, default False

   .. attribute:: show_region_ui

      :type: boolean, default False

   .. data:: show_render

      Show render related properties

      :type: boolean, default False, (readonly)

   .. attribute:: show_repeat

      Display the image repeated outside of the main view

      :type: boolean, default False

   .. attribute:: show_stereo_3d

      Display the image in Stereo 3D

      :type: boolean, default False

   .. data:: show_uvedit

      Show UV editing related properties

      :type: boolean, default False, (readonly)

   .. attribute:: ui_mode

      Editing context being displayed

      * ``VIEW``
        View -- View the image.
      * ``PAINT``
        Paint -- 2D image painting mode.
      * ``MASK``
        Mask -- Mask editing.

      :type: enum in [``'VIEW'``, ``'PAINT'``, ``'MASK'``], default ``'VIEW'``

   .. attribute:: use_image_pin

      Display current image regardless of object selection

      :type: boolean, default False

   .. attribute:: use_realtime_update

      Update other affected window spaces automatically to reflect changes during interactive operations such as transform

      :type: boolean, default False

   .. data:: uv_editor

      UV editor settings

      :type: :class:`SpaceUVEditor`, (readonly, never None)

   .. data:: zoom

      Zoom factor

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0), (readonly)

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

