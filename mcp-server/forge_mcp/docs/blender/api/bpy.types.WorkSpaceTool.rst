WorkSpaceTool(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: WorkSpaceTool(bpy_struct)


   .. data:: brush_type

      If the tool uses brushes and is limited to a specific brush type, the identifier of the brush type

      :type: enum in [``'DEFAULT'``], default ``'DEFAULT'``, (readonly)

   .. data:: has_datablock

      :type: boolean, default False, (readonly)

   .. attribute:: idname

      :type: string, default "", (never None)

   .. attribute:: idname_fallback

      :type: string, default "", (never None)

   .. data:: index

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: mode

      :type: enum in [``'DEFAULT'``], default ``'DEFAULT'``, (readonly)

   .. data:: space_type

      :type: enum in :ref:`rna_enum_space_type_items`, default ``'EMPTY'``, (readonly)

   .. data:: use_brushes

      :type: boolean, default False, (readonly)

   .. data:: use_paint_canvas

      Does this tool use a painting canvas

      :type: boolean, default False, (readonly)

   .. data:: widget

      :type: string, default "", (readonly, never None)

   .. method:: setup(idname, *, cursor='DEFAULT', keymap="", gizmo_group="", brush_type='', data_block="", operator="", index=0, options={}, idname_fallback="", keymap_fallback="")

      Set the tool settings

      :arg idname: Identifier
      :type idname: string, (never None)
      :arg cursor: cursor
      :type cursor: enum in :ref:`rna_enum_window_cursor_items`, (optional)
      :arg keymap: Key Map
      :type keymap: string, (optional, never None)
      :arg gizmo_group: Gizmo Group
      :type gizmo_group: string, (optional, never None)
      :arg brush_type: Brush Type, Limit this tool to a specific type of brush
      :type brush_type: enum in [], (optional)
      :arg data_block: Data Block
      :type data_block: string, (optional, never None)
      :arg operator: Operator
      :type operator: string, (optional, never None)
      :arg index: Index
      :type index: int in [-inf, inf], (optional)
      :arg options: Tool Options

         * ``KEYMAP_FALLBACK``
           Fallback.
         * ``USE_BRUSHES``
           Uses Brushes -- Allow this tool to use brushes via the asset system.
      :type options: enum set in {``'KEYMAP_FALLBACK'``, ``'USE_BRUSHES'``}, (optional)
      :arg idname_fallback: Fallback Identifier
      :type idname_fallback: string, (optional, never None)
      :arg keymap_fallback: Fallback Key Map
      :type keymap_fallback: string, (optional, never None)

   .. method:: operator_properties(operator)

      operator_properties

      :type operator: string, (never None)
      :rtype: :class:`OperatorProperties`, (never None)

   .. method:: gizmo_group_properties(group)

      gizmo_group_properties

      :type group: string, (never None)
      :rtype: :class:`GizmoGroupProperties`, (never None)

   .. method:: refresh_from_context()

      refresh_from_context


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

   * :class:`WorkSpace.tools`
   * :class:`wmTools.from_space_image_mode`
   * :class:`wmTools.from_space_node`
   * :class:`wmTools.from_space_sequencer`
   * :class:`wmTools.from_space_view3d_mode`

