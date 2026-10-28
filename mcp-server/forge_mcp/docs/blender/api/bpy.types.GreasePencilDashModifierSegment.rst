GreasePencilDashModifierSegment(bpy_struct)
===========================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GreasePencilDashModifierSegment(bpy_struct)

   Configuration for a single dash segment

   .. attribute:: dash

      The number of consecutive points from the original stroke to include in this segment

      :type: int in [1, 32767], default 2

   .. attribute:: gap

      The number of points skipped after this segment

      :type: int in [0, 32767], default 1

   .. attribute:: material_index

      Use this index on generated segment. -1 means using the existing material.

      :type: int in [-1, 32767], default -1

   .. attribute:: name

      Name of the dash segment

      :type: string, default "", (never None)

   .. attribute:: opacity

      The factor to apply to the original point's opacity for the new points

      :type: float in [0, 1], default 1.0

   .. attribute:: radius

      The factor to apply to the original point's radius for the new points

      :type: float in [0, 1], default 1.0

   .. attribute:: use_cyclic

      Enable cyclic on individual stroke dashes

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

   * :class:`GreasePencilDashModifierData.segments`

