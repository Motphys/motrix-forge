SpaceOutliner(Space)
====================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceOutliner(Space)

   Outliner space data

   .. attribute:: display_mode

      Type of information to display

      * ``SCENES``
        Scenes -- Display scenes and their view layers, collections and objects.
      * ``VIEW_LAYER``
        View Layer -- Display collections and objects in the view layer.
      * ``SEQUENCE``
        Video Sequencer -- Display data belonging to the Video Sequencer.
      * ``LIBRARIES``
        Blender File -- Display data of current file and linked libraries.
      * ``DATA_API``
        Data API -- Display low level Blender data and its properties.
      * ``LIBRARY_OVERRIDES``
        Library Overrides -- Display data-blocks with library overrides and list their overridden properties.
      * ``ORPHAN_DATA``
        Unused Data -- Display data that is unused and/or will be lost when the file is reloaded.

      :type: enum in [``'SCENES'``, ``'VIEW_LAYER'``, ``'SEQUENCE'``, ``'LIBRARIES'``, ``'DATA_API'``, ``'LIBRARY_OVERRIDES'``, ``'ORPHAN_DATA'``], default ``'SCENES'``

   .. attribute:: filter_id_type

      Data-block type to show

      :type: enum in :ref:`rna_enum_id_type_items`, default ``'ACTION'``

   .. attribute:: filter_invert

      Invert the object state filter

      :type: boolean, default False

   .. attribute:: filter_state

      * ``ALL``
        All -- Show all objects in the view layer.
      * ``VISIBLE``
        Visible -- Show visible objects.
      * ``SELECTED``
        Selected -- Show selected objects.
      * ``ACTIVE``
        Active -- Show only the active object.
      * ``SELECTABLE``
        Selectable -- Show only selectable objects.

      :type: enum in [``'ALL'``, ``'VISIBLE'``, ``'SELECTED'``, ``'ACTIVE'``, ``'SELECTABLE'``], default ``'ALL'``

   .. attribute:: filter_text

      Live search filtering string

      :type: string, default "", (never None)

   .. attribute:: lib_override_view_mode

      Choose different visualizations of library override data

      * ``PROPERTIES``
        Properties -- Display all local override data-blocks with their overridden properties and buttons to edit them.
      * ``HIERARCHIES``
        Hierarchies -- Display library override relationships.

      :type: enum in [``'PROPERTIES'``, ``'HIERARCHIES'``], default ``'PROPERTIES'``

   .. attribute:: show_mode_column

      Show the mode column for mode toggle and activation

      :type: boolean, default False

   .. attribute:: show_restrict_column_enable

      Exclude from view layer

      :type: boolean, default False

   .. attribute:: show_restrict_column_hide

      Temporarily hide in viewport

      :type: boolean, default False

   .. attribute:: show_restrict_column_holdout

      Holdout

      :type: boolean, default False

   .. attribute:: show_restrict_column_indirect_only

      Indirect only

      :type: boolean, default False

   .. attribute:: show_restrict_column_render

      Globally disable in renders

      :type: boolean, default False

   .. attribute:: show_restrict_column_select

      Selectable

      :type: boolean, default False

   .. attribute:: show_restrict_column_viewport

      Globally disable in viewports

      :type: boolean, default False

   .. attribute:: use_filter_case_sensitive

      Only use case sensitive matches of search string

      :type: boolean, default False

   .. attribute:: use_filter_children

      Show children

      :type: boolean, default False

   .. attribute:: use_filter_collection

      Show collections

      :type: boolean, default False

   .. attribute:: use_filter_complete

      Only use complete matches of search string

      :type: boolean, default False

   .. attribute:: use_filter_id_type

      Show only data-blocks of one type

      :type: boolean, default False

   .. attribute:: use_filter_lib_override_system

      For libraries with overrides created, show the overridden values that are defined/controlled automatically (e.g. to make users of an overridden data-block point to the override data, not the original linked data)

      :type: boolean, default False

   .. attribute:: use_filter_object

      Show objects

      :type: boolean, default False

   .. attribute:: use_filter_object_armature

      Show armature objects

      :type: boolean, default False

   .. attribute:: use_filter_object_camera

      Show camera objects

      :type: boolean, default False

   .. attribute:: use_filter_object_content

      Show what is inside the objects elements

      :type: boolean, default False

   .. attribute:: use_filter_object_empty

      Show empty objects

      :type: boolean, default False

   .. attribute:: use_filter_object_grease_pencil

      Show Grease Pencil objects

      :type: boolean, default False

   .. attribute:: use_filter_object_light

      Show light objects

      :type: boolean, default False

   .. attribute:: use_filter_object_mesh

      Show mesh objects

      :type: boolean, default False

   .. attribute:: use_filter_object_others

      Show curves, lattices, light probes, fonts, ...

      :type: boolean, default False

   .. attribute:: use_filter_view_layers

      Show all the view layers

      :type: boolean, default False

   .. attribute:: use_sort_alpha

      :type: boolean, default False

   .. attribute:: use_sync_select

      Sync outliner selection with other editors

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

