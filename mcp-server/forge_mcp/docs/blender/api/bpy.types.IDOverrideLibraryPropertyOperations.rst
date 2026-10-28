IDOverrideLibraryPropertyOperations(bpy_struct)
===============================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: IDOverrideLibraryPropertyOperations(bpy_struct)

   Collection of override operations

   .. method:: add(operation, *, use_id=False, subitem_reference_name="", subitem_local_name="", subitem_reference_id=None, subitem_local_id=None, subitem_reference_index=-1, subitem_local_index=-1)

      Add a new operation

      :arg operation: Operation, What override operation is performed

         * ``NOOP``
           No-Op -- Does nothing, prevents adding actual overrides (NOT USED).
         * ``REPLACE``
           Replace -- Replace value of reference by overriding one.
         * ``DIFF_ADD``
           Differential -- Stores and apply difference between reference and local value (NOT USED).
         * ``DIFF_SUB``
           Differential -- Stores and apply difference between reference and local value (NOT USED).
         * ``FACT_MULTIPLY``
           Factor -- Stores and apply multiplication factor between reference and local value (NOT USED).
         * ``INSERT_AFTER``
           Insert After -- Insert a new item into collection after the one referenced in subitem_reference_name/_id or _index.
         * ``INSERT_BEFORE``
           Insert Before -- Insert a new item into collection before the one referenced in subitem_reference_name/_id or _index (NOT USED).
      :type operation: enum in [``'NOOP'``, ``'REPLACE'``, ``'DIFF_ADD'``, ``'DIFF_SUB'``, ``'FACT_MULTIPLY'``, ``'INSERT_AFTER'``, ``'INSERT_BEFORE'``]
      :arg use_id: Use ID Pointer Subitem, Whether the found or created liboverride operation should use ID pointers or not
      :type use_id: boolean, (optional)
      :arg subitem_reference_name: Subitem Reference Name, Used to handle insertions or ID replacements into collection
      :type subitem_reference_name: string, (optional, never None)
      :arg subitem_local_name: Subitem Local Name, Used to handle insertions or ID replacements into collection
      :type subitem_local_name: string, (optional, never None)
      :arg subitem_reference_id: Subitem Reference ID, Used to handle ID replacements into collection
      :type subitem_reference_id: :class:`ID`, (optional)
      :arg subitem_local_id: Subitem Local ID, Used to handle ID replacements into collection
      :type subitem_local_id: :class:`ID`, (optional)
      :arg subitem_reference_index: Subitem Reference Index, Used to handle insertions or ID replacements into collection
      :type subitem_reference_index: int in [-1, inf], (optional)
      :arg subitem_local_index: Subitem Local Index, Used to handle insertions or ID replacements into collection
      :type subitem_local_index: int in [-1, inf], (optional)
      :return: New Operation, Created operation
      :rtype: :class:`IDOverrideLibraryPropertyOperation`

   .. method:: remove(operation)

      Remove and delete an operation

      :arg operation: Operation, Override operation to be deleted
      :type operation: :class:`IDOverrideLibraryPropertyOperation`

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

   * :class:`IDOverrideLibraryProperty.operations`

