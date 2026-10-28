ColorManagedViewSettings(bpy_struct)
====================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ColorManagedViewSettings(bpy_struct)

   Color management settings used for displaying images on the display

   .. data:: curve_mapping

      Color curve mapping applied before display transform

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: exposure

      Exposure (stops) applied before display transform, multiplying by 2^exposure

      :type: float in [-32, 32], default 0.0

   .. attribute:: gamma

      Additional gamma encoding after display transform, for output with custom gamma

      :type: float in [0, 5], default 1.0

   .. attribute:: look

      Additional transform applied before view transform for artistic needs

      * ``NONE``
        None -- Do not modify image in an artistic manner.

      :type: enum in [``'NONE'``], default ``'NONE'``

   .. attribute:: use_curve_mapping

      Use RGB curved for pre-display transformation

      :type: boolean, default False

   .. attribute:: use_hdr_view

      Enable high dynamic range display in rendered viewport, uncapping display brightness. This requires a monitor with HDR support and a view transform designed for HDR. 'Filmic' and 'AgX' do not generate HDR colors.

      :type: boolean, default False

   .. attribute:: use_white_balance

      Perform chromatic adaption from a different white point

      :type: boolean, default False

   .. attribute:: view_transform

      View used when converting image to a display space

      * ``NONE``
        None -- Do not perform any color transform on display, use old non-color managed technique for display.

      :type: enum in [``'NONE'``], default ``'NONE'``

   .. attribute:: white_balance_temperature

      Color temperature of the scene's white point

      :type: float in [1800, 100000], default 6500.0

   .. attribute:: white_balance_tint

      Color tint of the scene's white point (the default of 10 matches daylight)

      :type: float in [-500, 500], default 10.0

   .. attribute:: white_balance_whitepoint

      The color which gets mapped to white (automatically converted to/from temperature and tint)

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.0, 0.0, 0.0)

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

   * :class:`ImageFormatSettings.view_settings`
   * :class:`Scene.view_settings`

