SpaceUVEditor(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SpaceUVEditor(bpy_struct)

   UV editor data for the image editor space

   .. attribute:: custom_grid_subdivisions

      Number of grid units in UV space that make one UV Unit

      :type: int array of 2 items in [1, 5000], default (10, 10)

   .. attribute:: display_stretch_type

      Type of stretch to display

      * ``ANGLE``
        Angle -- Angular distortion between UV and 3D angles.
      * ``AREA``
        Area -- Area distortion between UV and 3D faces.

      :type: enum in [``'ANGLE'``, ``'AREA'``], default ``'ANGLE'``

   .. attribute:: edge_display_type

      Display style for UV edges

      * ``OUTLINE``
        Outline -- Display white edges with black outline.
      * ``DASH``
        Dash -- Display dashed black-white edges.
      * ``BLACK``
        Black -- Display black edges.
      * ``WHITE``
        White -- Display white edges.

      :type: enum in [``'OUTLINE'``, ``'DASH'``, ``'BLACK'``, ``'WHITE'``], default ``'OUTLINE'``

   .. attribute:: grid_shape_source

      Specify source for the grid shape

      * ``DYNAMIC``
        Dynamic -- Dynamic grid.
      * ``FIXED``
        Fixed -- Manually set grid divisions.
      * ``PIXEL``
        Pixel -- Grid aligns with pixels from image.

      :type: enum in [``'DYNAMIC'``, ``'FIXED'``, ``'PIXEL'``], default ``'DYNAMIC'``

   .. attribute:: lock_bounds

      Constraint to stay within the image bounds while editing

      :type: boolean, default False

   .. attribute:: pixel_round_mode

      Round UVs to pixels while editing

      * ``DISABLED``
        Disabled -- Don't round to pixels.
      * ``CORNER``
        Corner -- Round to pixel corners.
      * ``CENTER``
        Center -- Round to pixel centers.

      :type: enum in [``'DISABLED'``, ``'CORNER'``, ``'CENTER'``], default ``'DISABLED'``

   .. attribute:: show_faces

      Display faces over the image

      :type: boolean, default False

   .. attribute:: show_grid_over_image

      Show the grid over the image

      :type: boolean, default True

   .. attribute:: show_metadata

      Display metadata properties of the image

      :type: boolean, default False

   .. attribute:: show_modified_edges

      Display edges after modifiers are applied

      :type: boolean, default False

   .. attribute:: show_pixel_coords

      Display UV coordinates in pixels rather than from 0.0 to 1.0

      :type: boolean, default False

   .. attribute:: show_stretch

      Display faces colored according to the difference in shape between UVs and their 3D coordinates (blue for low distortion, red for high distortion)

      :type: boolean, default False

   .. attribute:: show_uv

      Display overlay of UV layer

      :type: boolean, default False

   .. attribute:: stretch_opacity

      Opacity of the UV Stretch overlay

      :type: float in [0, 1], default 0.0

   .. attribute:: tile_grid_shape

      How many tiles will be shown in the background

      :type: int array of 2 items in [1, 100], default (1, 1)

   .. attribute:: use_live_unwrap

      Continuously unwrap the selected UV island while transforming pinned vertices

      :type: boolean, default False

   .. attribute:: uv_face_opacity

      Opacity of faces in UV overlays

      :type: float in [0, 1], default 0.0

   .. attribute:: uv_opacity

      Opacity of UV overlays

      :type: float in [0, 1], default 0.0

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

   * :class:`SpaceImageEditor.uv_editor`

