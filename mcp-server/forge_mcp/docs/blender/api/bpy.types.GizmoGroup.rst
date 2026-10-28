GizmoGroup(bpy_struct)
======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GizmoGroup(bpy_struct)

   Storage of an operator being executed, or registered after execution

   .. attribute:: bl_idname

      :type: string, default "", (never None)

   .. attribute:: bl_label

      :type: string, default "", (never None)

   .. attribute:: bl_options

      Options for this operator type

      * ``3D``
        3D -- Use in 3D viewport.
      * ``SCALE``
        Scale -- Scale to respect zoom (otherwise zoom independent display size).
      * ``DEPTH_3D``
        Depth 3D -- Supports culled depth by other objects in the view.
      * ``SELECT``
        Select -- Supports selection.
      * ``PERSISTENT``
        Persistent.
      * ``SHOW_MODAL_ALL``
        Show Modal All -- Show all while interacting, as well as this group when another is being interacted with.
      * ``EXCLUDE_MODAL``
        Exclude Modal -- Show all except this group while interacting.
      * ``TOOL_INIT``
        Tool Init -- Postpone running until tool operator run (when used with a tool).
      * ``TOOL_FALLBACK_KEYMAP``
        Use fallback tools keymap -- Add fallback tools keymap to this gizmo type.
      * ``VR_REDRAWS``
        VR Redraws -- The gizmos are made for use with virtual reality sessions and require special redraw management.

      :type: enum set in {``'3D'``, ``'SCALE'``, ``'DEPTH_3D'``, ``'SELECT'``, ``'PERSISTENT'``, ``'SHOW_MODAL_ALL'``, ``'EXCLUDE_MODAL'``, ``'TOOL_INIT'``, ``'TOOL_FALLBACK_KEYMAP'``, ``'VR_REDRAWS'``}, default {``'3D'``}

   .. attribute:: bl_owner_id

      :type: string, default "", (never None)

   .. attribute:: bl_region_type

      The region where the panel is going to be used in

      :type: enum in :ref:`rna_enum_region_type_items`, default ``'WINDOW'``

   .. attribute:: bl_space_type

      The space where the panel is going to be used in

      :type: enum in :ref:`rna_enum_space_type_items`, default ``'EMPTY'``

   .. data:: gizmos

      List of gizmos in the Gizmo Map

      :type: :class:`Gizmos` :class:`bpy_prop_collection` of :class:`Gizmo`, (readonly)

   .. data:: name

      :type: string, default "", (readonly, never None)

   .. classmethod:: poll(context)

      Test if the gizmo group can be called or not

      :type context: :class:`Context`, (never None)
      :rtype: boolean

   .. classmethod:: setup_keymap(keyconfig)

      Initialize keymaps for this gizmo group, use fallback keymap when not present

      :type keyconfig: :class:`KeyConfig`, (never None)
      :rtype: :class:`KeyMap`, (never None)

   .. method:: setup(context)

      Create gizmos function for the gizmo group

      :type context: :class:`Context`, (never None)

   .. method:: refresh(context)

      Refresh data (called on common state changes such as selection)

      :type context: :class:`Context`, (never None)

   .. method:: draw_prepare(context)

      Run before each redraw

      :type context: :class:`Context`, (never None)

   .. method:: invoke_prepare(context, gizmo)

      Run before invoke

      :type context: :class:`Context`, (never None)
      :type gizmo: :class:`Gizmo`, (never None)

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

   * :class:`Context.gizmo_group`
   * :class:`Gizmo.group`

