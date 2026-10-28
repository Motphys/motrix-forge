UDIMTiles(bpy_struct)
=====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UDIMTiles(bpy_struct)

   Collection of UDIM tiles

   .. attribute:: active

      Active Image Tile

      :type: :class:`UDIMTile`, (never None)

   .. attribute:: active_index

      Active index in tiles array

      :type: int in [0, inf], default 0

   .. method:: new(tile_number, *, label="")

      Add a tile to the image

      :arg tile_number: Number of the newly created tile
      :type tile_number: int in [1, inf]
      :arg label: Optional label for the tile
      :type label: string, (optional, never None)
      :return: Newly created image tile
      :rtype: :class:`UDIMTile`

   .. method:: get(tile_number)

      Get a tile based on its tile number

      :arg tile_number: Number of the tile
      :type tile_number: int in [0, inf]
      :return: The tile
      :rtype: :class:`UDIMTile`

   .. method:: remove(tile)

      Remove an image tile

      :arg tile: Image tile to remove
      :type tile: :class:`UDIMTile`, (never None)

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

   * :class:`Image.tiles`

