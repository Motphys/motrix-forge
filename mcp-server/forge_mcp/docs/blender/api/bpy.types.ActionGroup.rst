ActionGroup(bpy_struct)
=======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ActionGroup(bpy_struct)

   Groups of F-Curves

   .. data:: channels

      F-Curves in this group

      :type: :class:`bpy_prop_collection` of :class:`FCurve`, (readonly)

   .. attribute:: color_set

      Custom color set to use

      :type: enum in :ref:`rna_enum_color_sets_items`, default ``'DEFAULT'``

   .. data:: colors

      Copy of the colors associated with the group's color set

      :type: :class:`ThemeBoneColorSet`, (readonly, never None)

   .. data:: is_custom_color_set

      Color set is user-defined instead of a fixed theme color set

      :type: boolean, default False, (readonly)

   .. attribute:: lock

      Action group is locked

      :type: boolean, default False

   .. attribute:: mute

      Action group is muted

      :type: boolean, default False

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: select

      Action group is selected

      :type: boolean, default False

   .. attribute:: show_expanded

      Action group is expanded except in graph editor

      :type: boolean, default False

   .. attribute:: show_expanded_graph

      Action group is expanded in graph editor

      :type: boolean, default False

   .. attribute:: use_pin

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

   * :class:`Action.groups`
   * :class:`ActionChannelbag.groups`
   * :class:`ActionChannelbagGroups.new`
   * :class:`ActionChannelbagGroups.remove`
   * :class:`ActionGroups.new`
   * :class:`ActionGroups.remove`
   * :class:`FCurve.group`

