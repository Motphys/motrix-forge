ActionKeyframeStrip(ActionStrip)
================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ActionStrip`

.. class:: ActionKeyframeStrip(ActionStrip)

   Strip with a set of F-Curves for each action slot

   .. data:: channelbags

      :type: :class:`ActionChannelbags` :class:`bpy_prop_collection` of :class:`ActionChannelbag`, (readonly)

   .. method:: channelbag(slot, *, ensure=False)

      Find the ActionChannelbag for a specific Slot

      :arg slot: Slot, The slot for which to find the channelbag
      :type slot: :class:`ActionSlot`
      :arg ensure: Create if necessary, Ensure the channelbag exists for this slot, creating it if necessary
      :type ensure: boolean, (optional)
      :return: Channels
      :rtype: :class:`ActionChannelbag`

   .. method:: key_insert(slot, data_path, array_index, value, time)

      key_insert

      :arg slot: Slot, The slot that identifies which 'thing' should be keyed
      :type slot: :class:`ActionSlot`
      :arg data_path: Data Path, F-Curve data path
      :type data_path: string, (never None)
      :arg array_index: Array Index, Index of the animated array element, or -1 if the property is not an array
      :type array_index: int in [-inf, inf]
      :arg value: Value to key, Value of the animated property
      :type value: float in [-inf, inf]
      :arg time: Time of the key, Time, in frames, of the key
      :type time: float in [-inf, inf]
      :return: Success, Whether the key was successfully inserted
      :rtype: boolean

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
   * :class:`ActionStrip.type`

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
   * :class:`ActionStrip.bl_rna_get_subclass`
   * :class:`ActionStrip.bl_rna_get_subclass_py`

