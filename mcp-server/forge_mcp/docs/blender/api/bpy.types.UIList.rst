UIList(bpy_struct)
==================

.. currentmodule:: bpy.types


Basic UIList Example
++++++++++++++++++++

This script is the UIList subclass used to show material slots, with a bunch of additional commentaries.

Notice the name of the class, this naming convention is similar as the one for panels or menus.

.. note::

   UIList subclasses must be registered for Blender to use them.

.. literalinclude:: ..\examples\bpy.types.UIList.1.py
   :lines: 13-


Advanced UIList Example - Filtering and Reordering
++++++++++++++++++++++++++++++++++++++++++++++++++

This script is an extended version of the ``UIList`` subclass used to show vertex groups. It is not used 'as is',
because iterating over all vertices in a 'draw' function is a very bad idea for UI performance! However, it's a good
example of how to create/use filtering/reordering callbacks.

.. literalinclude:: ..\examples\bpy.types.UIList.2.py
   :lines: 9-

base class --- :class:`bpy_struct`

subclasses --- 
:class:`ASSETBROWSER_UL_metadata_tags`, :class:`CLIP_UL_tracking_objects`, :class:`CURVES_UL_attributes`, :class:`DATA_UL_bone_collections`, :class:`FILEBROWSER_UL_dir`, :class:`GPENCIL_UL_annotation_layer`, :class:`GPENCIL_UL_layer`, :class:`GPENCIL_UL_masks`, :class:`GPENCIL_UL_matslots`, :class:`GREASE_PENCIL_UL_attributes`, :class:`GREASE_PENCIL_UL_masks`, :class:`IMAGE_UL_render_slots`, :class:`IMAGE_UL_udim_tiles`, :class:`MASK_UL_layers`, :class:`MATERIAL_UL_matslots`, :class:`MESH_UL_attributes`, :class:`MESH_UL_color_attributes`, :class:`MESH_UL_color_attributes_selector`, :class:`MESH_UL_shape_keys`, :class:`MESH_UL_uvmaps`, :class:`MESH_UL_vgroups`, :class:`PARTICLE_UL_particle_systems`, :class:`PHYSICS_UL_dynapaint_surfaces`, :class:`POINTCLOUD_UL_attributes`, :class:`POSE_UL_selection_set`, :class:`RENDER_UL_renderviews`, :class:`SCENE_UL_gltf2_filter_action`, :class:`SCENE_UL_keying_set_paths`, :class:`TEXTURE_UL_texpaintslots`, :class:`TEXTURE_UL_texslots`, :class:`UI_UL_list`, :class:`USERPREF_UL_asset_libraries`, :class:`USERPREF_UL_extension_repos`, :class:`VIEWLAYER_UL_aov`, :class:`VIEWLAYER_UL_linesets`, :class:`VOLUME_UL_grids`, :class:`WORKSPACE_UL_addons_items`

.. class:: UIList(bpy_struct)

   UI list containing the elements of a collection

   .. data:: bitflag_filter_item

      The value of the reserved bitflag 'FILTER_ITEM' (in filter_flags values)

      :type: int in [0, inf], default 0, (readonly)

   .. data:: bitflag_item_never_show

      Skip the item from displaying in the list

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: bl_idname

      If this is set, the uilist gets a custom ID, otherwise it takes the name of the class used to define the uilist (for example, if the class name is "OBJECT_UL_vgroups", and bl_idname is not set by the script, then bl_idname = "OBJECT_UL_vgroups")

      :type: string, default "", (never None)

   .. attribute:: filter_name

      Only show items matching this name (use '*' as wildcard)

      :type: string, default "", (never None)

   .. data:: layout_type

      :type: enum in :ref:`rna_enum_uilist_layout_type_items`, default ``'DEFAULT'``, (readonly)

   .. data:: list_id

      Identifier of the list, if any was passed to the "list_id" parameter of "template_list()"

      :type: string, default "", (readonly, never None)

   .. attribute:: use_filter_invert

      Invert filtering (show hidden items, and vice versa)

      :type: boolean, default False

   .. attribute:: use_filter_show

      Show filtering options

      :type: boolean, default False

   .. attribute:: use_filter_sort_alpha

      Sort items by their name

      :type: boolean, default False

   .. attribute:: use_filter_sort_lock

      Lock the order of shown items (user cannot change it)

      :type: boolean, default False

   .. attribute:: use_filter_sort_reverse

      Reverse the order of shown items

      :type: boolean, default False

   .. method:: draw_item(context, layout, data, item, icon, active_data, active_property, index, flt_flag)

      Draw an item in the list (NOTE: when you define your own draw_item function, you may want to check given 'item' is of the right type...)

      :type context: :class:`Context`
      :arg layout: Layout to draw the item
      :type layout: :class:`UILayout`, (never None)
      :arg data: Data from which to take Collection property
      :type data: :class:`AnyType`
      :arg item: Item of the collection property
      :type item: :class:`AnyType`
      :arg icon: Icon of the item in the collection
      :type icon: int in [0, inf]
      :arg active_data: Data from which to take property for the active element
      :type active_data: :class:`AnyType`, (never None)
      :arg active_property: Identifier of property in active_data, for the active element
      :type active_property: string, (optional for registration, never None)
      :arg index: Index of the item in the collection
      :type index: int in [0, inf]
      :arg flt_flag: The filter-flag result for this item
      :type flt_flag: int in [0, inf]

   .. method:: draw_filter(context, layout)

      Draw filtering options

      :type context: :class:`Context`
      :arg layout: Layout to draw the item
      :type layout: :class:`UILayout`, (never None)

   .. method:: filter_items(context, data, property)

      Filter and/or re-order items of the collection (output filter results in filter_flags, and reorder results in filter_neworder arrays)

      :type context: :class:`Context`
      :arg data: Data from which to take Collection property
      :type data: :class:`AnyType`
      :arg property: Identifier of property in data, for the collection
      :type property: string, (never None)
      :return:
         `filter_flags`, An array of filter flags, one for each item in the collection (NOTE: The upper 16 bits, including FILTER_ITEM, are reserved, only use the lower 16 bits for custom usages), int array of 1 items in [0, inf]

         `filter_neworder`, An array of indices, one for each item in the collection, mapping the org index to the new one, int array of 1 items in [0, inf]

      :rtype: (int array of 1 items in [0, inf], int array of 1 items in [0, inf])

   .. classmethod:: append(draw_func)

      Append a draw function to this menu,
      takes the same arguments as the menus draw function

   .. classmethod:: is_extended()

   .. classmethod:: prepend(draw_func)

      Prepend a draw function to this menu, takes the same arguments as
      the menus draw function

   .. classmethod:: remove(draw_func)

      Remove a draw function that has been added to this menu

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

