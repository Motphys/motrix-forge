SpaceFileBrowser(Space)
=======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceFileBrowser(Space)

   File browser space data

   .. data:: active_operator

      :type: :class:`Operator`, (readonly)

   .. attribute:: bookmarks

      User's bookmarks

      :type: :class:`bpy_prop_collection` of :class:`FileBrowserFSMenuEntry`

   .. attribute:: bookmarks_active

      Index of active bookmark (-1 if none)

      :type: int in [-32768, 32767], default -1

   .. attribute:: browse_mode

      Type of the File Editor view (regular file browsing or asset browsing)

      :type: enum in :ref:`rna_enum_space_file_browse_mode_items`, default ``'FILES'``

   .. data:: operator

      :type: :class:`Operator`, (readonly)

   .. data:: params

      Parameters and Settings for the Filebrowser

      :type: :class:`FileSelectParams`, (readonly)

   .. attribute:: recent_folders

      :type: :class:`bpy_prop_collection` of :class:`FileBrowserFSMenuEntry`

   .. attribute:: recent_folders_active

      Index of active recent folder (-1 if none)

      :type: int in [-32768, 32767], default -1

   .. attribute:: show_region_tool_props

      :type: boolean, default False

   .. attribute:: show_region_toolbar

      :type: boolean, default False

   .. attribute:: show_region_ui

      :type: boolean, default False

   .. data:: system_bookmarks

      System's bookmarks

      :type: :class:`bpy_prop_collection` of :class:`FileBrowserFSMenuEntry`, (readonly)

   .. attribute:: system_bookmarks_active

      Index of active system bookmark (-1 if none)

      :type: int in [-32768, 32767], default -1

   .. data:: system_folders

      System's folders (usually root, available hard drives, etc)

      :type: :class:`bpy_prop_collection` of :class:`FileBrowserFSMenuEntry`, (readonly)

   .. attribute:: system_folders_active

      Index of active system folder (-1 if none)

      :type: int in [-32768, 32767], default -1

   .. method:: activate_asset_by_id(id_to_activate, *, deferred=False)

      Activate and select the asset entry that represents the given ID

      :arg id_to_activate: id_to_activate
      :type id_to_activate: :class:`ID`
      :arg deferred: Whether to activate the ID immediately (false) or after the file browser refreshes (true)
      :type deferred: boolean, (optional)

   .. method:: activate_file_by_relative_path(*, relative_path="")

      Set active file and add to selection based on relative path to current File Browser directory

      :arg relative_path: relative_path
      :type relative_path: string, (optional, never None)

   .. method:: deselect_all()

      Deselect all files


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


   .. classmethod:: draw_handler_add(callback, args, region_type, draw_type)
   
      Add a new draw handler to this space type.
      It will be called every time the specified region in the space type will be drawn.
      Note: All arguments are positional only for now.
   
      :arg callback:
         A function that will be called when the region is drawn.
         It gets the specified arguments as input, it's return value is ignored.
      :type callback: Callable[..., Any]
      :arg args: Arguments that will be passed to the callback.
      :type args: tuple[Any, ...]
      :arg region_type: The region type the callback draws in; usually ``WINDOW``. (:class:`bpy.types.Region.type`)
      :type region_type: str
      :arg draw_type: Usually ``POST_PIXEL`` for 2D drawing and ``POST_VIEW`` for 3D drawing. In some cases ``PRE_VIEW`` can be used. ``BACKDROP`` can be used for backdrops in the node editor.
      :type draw_type: str
      :return: Handler that can be removed later on.
      :rtype: object


   .. classmethod:: draw_handler_remove(handler, region_type)
   
      Remove a draw handler that was added previously.
   
      :arg handler: The draw handler that should be removed.
      :type handler: object
      :arg region_type: Region type the callback was added to.
      :type region_type: str


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Space.type`
   * :class:`Space.show_locked_time`
   * :class:`Space.show_region_header`

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
   * :class:`Space.bl_rna_get_subclass`
   * :class:`Space.bl_rna_get_subclass_py`
   * :class:`Space.draw_handler_add`
   * :class:`Space.draw_handler_remove`

