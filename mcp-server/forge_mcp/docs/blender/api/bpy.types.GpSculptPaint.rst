GpSculptPaint(Paint)
====================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Paint`

.. class:: GpSculptPaint(Paint)


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
   * :class:`Paint.brush`
   * :class:`Paint.brush_asset_reference`
   * :class:`Paint.eraser_brush`
   * :class:`Paint.eraser_brush_asset_reference`
   * :class:`Paint.palette`
   * :class:`Paint.show_brush`
   * :class:`Paint.show_brush_on_surface`
   * :class:`Paint.show_low_resolution`
   * :class:`Paint.use_sculpt_delay_updates`
   * :class:`Paint.use_symmetry_x`
   * :class:`Paint.use_symmetry_y`
   * :class:`Paint.use_symmetry_z`
   * :class:`Paint.use_symmetry_feather`
   * :class:`Paint.cavity_curve`
   * :class:`Paint.use_cavity`
   * :class:`Paint.tile_offset`
   * :class:`Paint.tile_x`
   * :class:`Paint.tile_y`
   * :class:`Paint.tile_z`

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
   * :class:`Paint.bl_rna_get_subclass`
   * :class:`Paint.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   * :class:`ToolSettings.gpencil_sculpt_paint`

