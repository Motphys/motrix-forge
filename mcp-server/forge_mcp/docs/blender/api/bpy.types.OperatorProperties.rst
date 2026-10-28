OperatorProperties(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: OperatorProperties(bpy_struct)

   Input properties of an operator

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

   * :class:`Gizmo.target_set_operator`
   * :class:`KeyConfigurations.find_item_from_operator`
   * :class:`KeyMapItem.properties`
   * :class:`KeyMapItems.find_from_operator`
   * :class:`Macro.properties`
   * :class:`Operator.description`
   * :class:`Operator.properties`
   * :class:`OperatorMacro.properties`
   * :class:`UILayout.operator`
   * :class:`UILayout.operator_menu_enum`
   * :class:`UILayout.operator_menu_hold`
   * :class:`UILayout.template_asset_view`
   * :class:`UILayout.template_asset_view`
   * :class:`UILayout.template_popup_confirm`
   * :class:`WindowManager.operator_properties_last`
   * :class:`WorkSpaceTool.operator_properties`
   * :class:`XrActionMapItem.op_properties`

