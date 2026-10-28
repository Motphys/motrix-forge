UDIMTile(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UDIMTile(bpy_struct)

   Properties of the UDIM tile

   .. data:: channels

      Number of channels in the tile pixels buffer

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: generated_color

      Fill color for the generated image

      :type: float array of 4 items in [0, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: generated_height

      Generated image height

      :type: int in [1, 65536], default 0

   .. attribute:: generated_type

      Generated image type

      :type: enum in :ref:`rna_enum_image_generated_type_items`, default ``'BLANK'``

   .. attribute:: generated_width

      Generated image width

      :type: int in [1, 65536], default 0

   .. data:: is_generated_tile

      Is this image tile generated

      :type: boolean, default False, (readonly)

   .. attribute:: label

      Tile label

      :type: string, default "", (never None)

   .. attribute:: number

      Number of the position that this tile covers

      :type: int in [-inf, inf], default 0

   .. data:: size

      Width and height of the tile buffer in pixels, zero when image data can't be loaded

      :type: int array of 2 items in [-inf, inf], default (0, 0), (readonly)

   .. attribute:: use_generated_float

      Generate floating-point buffer

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

   * :class:`Image.tiles`
   * :class:`UDIMTiles.active`
   * :class:`UDIMTiles.get`
   * :class:`UDIMTiles.new`
   * :class:`UDIMTiles.remove`

