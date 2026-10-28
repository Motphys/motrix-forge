Window(bpy_struct)
==================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Window(bpy_struct)

   Open window

   .. data:: height

      Window height

      :type: int in [0, 32767], default 0, (readonly)

   .. data:: modal_operators

      A list of currently running modal operators

      :type: :class:`bpy_prop_collection` of :class:`Operator`, (readonly)

   .. data:: parent

      Active workspace and scene follow this window

      :type: :class:`Window`, (readonly)

   .. attribute:: scene

      Active scene to be edited in the window

      :type: :class:`Scene`, (never None)

   .. attribute:: screen

      Active workspace screen showing in the window

      :type: :class:`Screen`, (never None)

   .. data:: stereo_3d_display

      Settings for stereo 3D display

      :type: :class:`Stereo3dDisplay`, (readonly, never None)

   .. attribute:: view_layer

      The active workspace view layer showing in the window

      :type: :class:`ViewLayer`, (never None)

   .. data:: width

      Window width

      :type: int in [0, 32767], default 0, (readonly)

   .. attribute:: workspace

      Active workspace showing in the window

      :type: :class:`WorkSpace`, (never None)

   .. data:: x

      Horizontal location of the window

      :type: int in [-32768, 32767], default 0, (readonly)

   .. data:: y

      Vertical location of the window

      :type: int in [-32768, 32767], default 0, (readonly)

   .. method:: cursor_warp(x, y)

      Set the cursor position

      :type x: int in [-inf, inf]
      :type y: int in [-inf, inf]

   .. method:: cursor_set(cursor)

      Set the cursor

      :arg cursor: cursor
      :type cursor: enum in :ref:`rna_enum_window_cursor_items`

   .. method:: cursor_modal_set(cursor)

      Set the cursor, so the previous cursor can be restored

      :arg cursor: cursor
      :type cursor: enum in :ref:`rna_enum_window_cursor_items`

   .. method:: cursor_modal_restore()

      Restore the previous cursor after calling ``cursor_modal_set``


   .. method:: event_simulate(type, value, *, unicode="", x=0, y=0, shift=False, ctrl=False, alt=False, oskey=False, hyper=False)

      event_simulate

      :arg type: Type
      :type type: enum in :ref:`rna_enum_event_type_items`
      :arg value: Value
      :type value: enum in :ref:`rna_enum_event_value_items`
      :type unicode: string, (optional)
      :type x: int in [-inf, inf], (optional)
      :type y: int in [-inf, inf], (optional)
      :arg shift: Shift
      :type shift: boolean, (optional)
      :arg ctrl: Ctrl
      :type ctrl: boolean, (optional)
      :arg alt: Alt
      :type alt: boolean, (optional)
      :arg oskey: OS Key
      :type oskey: boolean, (optional)
      :arg hyper: Hyper
      :type hyper: boolean, (optional)
      :return: Item, Added key map item
      :rtype: :class:`Event`

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

   * :class:`Context.window`
   * :class:`Window.parent`
   * :class:`WindowManager.event_timer_add`
   * :class:`WindowManager.windows`

