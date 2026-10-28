Function(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Function(bpy_struct)

   RNA function definition

   .. data:: description

      Description of the Function's purpose

      :type: string, default "", (readonly, never None)

   .. data:: identifier

      Unique name used in the code and scripting

      :type: string, default "", (readonly, never None)

   .. data:: is_registered

      Function is registered as callback as part of type registration

      :type: boolean, default False, (readonly)

   .. data:: is_registered_optional

      Function is optionally registered as callback part of type registration

      :type: boolean, default False, (readonly)

   .. data:: parameters

      Parameters for the function

      :type: :class:`bpy_prop_collection` of :class:`Property`, (readonly)

   .. data:: use_self

      Function does not pass itself as an argument (becomes a static method in Python)

      :type: boolean, default False, (readonly)

   .. data:: use_self_type

      Function passes itself type as an argument (becomes a class method in Python if use_self is false)

      :type: boolean, default False, (readonly)

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

   * :class:`Struct.functions`

