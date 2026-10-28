NodesModifierBake(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: NodesModifierBake(bpy_struct)


   .. data:: bake_id

      Identifier for this bake which remains unchanged even when the bake node is renamed, grouped or ungrouped

      :type: int in [-inf, inf], default 0, (readonly)

   .. attribute:: bake_mode

      * ``ANIMATION``
        Animation -- Bake a frame range.
      * ``STILL``
        Still -- Bake a single frame.

      :type: enum in [``'ANIMATION'``, ``'STILL'``], default ``'ANIMATION'``

   .. attribute:: bake_target

      Where to store the baked data

      * ``INHERIT``
        Inherit from Modifier -- Use setting from the modifier.
      * ``PACKED``
        Packed -- Pack the baked data into the .blend file.
      * ``DISK``
        Disk -- Store the baked data in a directory on disk.

      :type: enum in [``'INHERIT'``, ``'PACKED'``, ``'DISK'``], default ``'INHERIT'``

   .. data:: data_blocks

      :type: :class:`NodesModifierBakeDataBlocks` :class:`bpy_prop_collection` of :class:`NodesModifierDataBlock`, (readonly)

   .. attribute:: directory

      Location on disk where the bake data is stored

      :type: string, default "", (never None, blend relative ``//`` prefix supported)

   .. attribute:: frame_end

      Frame where the baking ends

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_start

      Frame where the baking starts

      :type: int in [-inf, inf], default 0

   .. data:: node

      Bake node or simulation output node that corresponds to this bake. This node may be deeply nested in the modifier node group. It can be none in some cases like missing linked data blocks.

      :type: :class:`Node`, (readonly)

   .. attribute:: use_custom_path

      Specify a path where the baked data should be stored manually

      :type: boolean, default False

   .. attribute:: use_custom_simulation_frame_range

      Override the simulation frame range from the scene

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

   * :class:`NodesModifier.bakes`

