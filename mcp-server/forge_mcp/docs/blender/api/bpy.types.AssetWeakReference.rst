AssetWeakReference(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AssetWeakReference(bpy_struct)

   Weak reference to some asset

   .. data:: asset_library_identifier

      :type: string, default "", (readonly, never None)

   .. data:: asset_library_type

      * ``ALL``
        All Libraries -- Show assets from all of the listed asset libraries.
      * ``LOCAL``
        Current File -- Show the assets currently available in this Blender session.
      * ``ESSENTIALS``
        Essentials -- Show the basic building blocks and utilities coming with Blender.
      * ``CUSTOM``
        Custom -- Show assets from the asset libraries configured in the Preferences.

      :type: enum in [``'ALL'``, ``'LOCAL'``, ``'ESSENTIALS'``, ``'CUSTOM'``], default ``'ALL'``, (readonly)

   .. data:: relative_asset_identifier

      :type: string, default "", (readonly, never None)

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

   * :class:`AssetShelf.get_active_asset`
   * :class:`Paint.brush_asset_reference`
   * :class:`Paint.eraser_brush_asset_reference`

