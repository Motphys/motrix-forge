BlendDataParticles(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataParticles(bpy_struct)

   Collection of particle settings

   .. method:: new(name)

      Add a new particle settings instance to the main database

      :arg name: New name for the data-block
      :type name: string, (never None)
      :return: New particle settings data-block
      :rtype: :class:`ParticleSettings`

   .. method:: remove(particle, *, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a particle settings instance from the current blendfile

      :arg particle: Particle Settings to remove
      :type particle: :class:`ParticleSettings`, (never None)
      :arg do_unlink: Unlink all usages of those particle settings before deleting them
      :type do_unlink: boolean, (optional)
      :arg do_id_user: Decrement user counter of all datablocks used by this particle settings
      :type do_id_user: boolean, (optional)
      :arg do_ui_user: Make sure interface does not reference this particle settings
      :type do_ui_user: boolean, (optional)

   .. method:: tag(value)

      tag

      :arg value: Value
      :type value: boolean

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

   * :class:`BlendData.particles`

