SequencerToolSettings(bpy_struct)
=================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SequencerToolSettings(bpy_struct)


   .. attribute:: fit_method

      Scale fit method

      * ``FIT``
        Scale to Fit -- Scale image to fit within the canvas.
      * ``FILL``
        Scale to Fill -- Scale image to completely fill the canvas.
      * ``STRETCH``
        Stretch to Fill -- Stretch image to fill the canvas.
      * ``ORIGINAL``
        Use Original Size -- Keep image at its original size.

      :type: enum in [``'FIT'``, ``'FILL'``, ``'STRETCH'``, ``'ORIGINAL'``], default ``'FIT'``

   .. attribute:: overlap_mode

      How to resolve overlap after transformation

      * ``EXPAND``
        Expand -- Move strips so transformed strips fit.
      * ``OVERWRITE``
        Overwrite -- Trim or split strips to resolve overlap.
      * ``SHUFFLE``
        Shuffle -- Move transformed strips to nearest free space to resolve overlap.

      :type: enum in [``'EXPAND'``, ``'OVERWRITE'``, ``'SHUFFLE'``], default ``'EXPAND'``

   .. attribute:: pivot_point

      Rotation or scaling pivot point

      * ``CENTER``
        Bounding Box Center.
      * ``MEDIAN``
        Median Point.
      * ``CURSOR``
        2D Cursor -- Pivot around the 2D cursor.
      * ``INDIVIDUAL_ORIGINS``
        Individual Origins -- Pivot around each selected island's own median point.

      :type: enum in [``'CENTER'``, ``'MEDIAN'``, ``'CURSOR'``, ``'INDIVIDUAL_ORIGINS'``], default ``'CENTER'``

   .. attribute:: snap_distance

      Maximum distance for snapping in pixels

      :type: int in [-inf, inf], default 15

   .. attribute:: snap_ignore_muted

      Don't snap to hidden strips

      :type: boolean, default False

   .. attribute:: snap_ignore_sound

      Don't snap to sound strips

      :type: boolean, default False

   .. attribute:: snap_to_borders

      Snap to preview borders

      :type: boolean, default False

   .. attribute:: snap_to_center

      Snap to preview center

      :type: boolean, default False

   .. attribute:: snap_to_current_frame

      Snap to current frame

      :type: boolean, default False

   .. attribute:: snap_to_frame_range

      Snap to preview or scene start and end frame

      :type: boolean, default False

   .. attribute:: snap_to_hold_offset

      Snap to strip hold offsets

      :type: boolean, default False

   .. attribute:: snap_to_markers

      Snap to markers

      :type: boolean, default False

   .. attribute:: snap_to_retiming_keys

      Snap to retiming keys

      :type: boolean, default False

   .. attribute:: snap_to_strips_preview

      Snap to borders and origins of deselected, visible strips

      :type: boolean, default False

   .. attribute:: use_snap_current_frame_to_strips

      Snap current frame to strip start or end

      :type: boolean, default False

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

   * :class:`ToolSettings.sequencer_tool_settings`

