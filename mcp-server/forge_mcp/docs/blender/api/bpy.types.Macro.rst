Macro(bpy_struct)
=================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Macro(bpy_struct)

   Storage of a macro operator being executed, or registered after execution

   .. attribute:: bl_cursor_pending

      Cursor to use when waiting for the user to select a location to activate the operator (when ``bl_options`` has ``DEPENDS_ON_CURSOR`` set)

      :type: enum in :ref:`rna_enum_window_cursor_items`, default ``'DEFAULT'``

   .. attribute:: bl_description

      :type: string, default "", (never None)

   .. attribute:: bl_idname

      :type: string, default "", (never None)

   .. attribute:: bl_label

      :type: string, default "", (never None)

   .. attribute:: bl_options

      Options for this operator type

      :type: enum set in :ref:`rna_enum_operator_type_flag_items`, default {``'REGISTER'``}

   .. attribute:: bl_translation_context

      :type: string, default "Operator", (never None)

   .. attribute:: bl_undo_group

      :type: string, default "", (never None)

   .. data:: has_reports

      Operator has a set of reports (warnings and errors) from last execution

      :type: boolean, default False, (readonly)

   .. data:: name

      :type: string, default "", (readonly, never None)

   .. data:: properties

      :type: :class:`OperatorProperties`, (readonly, never None)

   .. method:: report(type, message)

      report

      :arg type: Type
      :type type: enum set in :ref:`rna_enum_wm_report_items`
      :arg message: Report Message
      :type message: string, (never None)

   .. classmethod:: poll(context)

      Test if the operator can be called or not

      :type context: :class:`Context`, (never None)
      :rtype: boolean

   .. method:: draw(context)

      Draw function for the operator

      :type context: :class:`Context`, (never None)

   .. classmethod:: define(operator)

      Append an operator to a registered macro class.
      
      :arg operator: Identifier of the operator. This does not have to be defined when this function is called.
      :type operator: str
      :return: The operator macro for property access.
      :rtype: :class:`OperatorMacro`

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

   * :class:`Operator.macros`

