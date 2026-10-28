AssetShelf(bpy_struct)
======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`IMAGE_AST_brush_paint`, :class:`VIEW3D_AST_brush_gpencil_paint`, :class:`VIEW3D_AST_brush_gpencil_sculpt`, :class:`VIEW3D_AST_brush_gpencil_vertex`, :class:`VIEW3D_AST_brush_gpencil_weight`, :class:`VIEW3D_AST_brush_sculpt`, :class:`VIEW3D_AST_brush_sculpt_curves`, :class:`VIEW3D_AST_brush_texture_paint`, :class:`VIEW3D_AST_brush_vertex_paint`, :class:`VIEW3D_AST_brush_weight_paint`, :class:`VIEW3D_AST_pose_library`

.. class:: AssetShelf(bpy_struct)

   Regions for quick access to assets

   .. attribute:: asset_library_reference

      Choose the asset library to display assets from

      * ``ALL``
        All Libraries -- Show assets from all of the listed asset libraries.
      * ``LOCAL``
        Current File -- Show the assets currently available in this Blender session.
      * ``ESSENTIALS``
        Essentials -- Show the basic building blocks and utilities coming with Blender.
      * ``CUSTOM``
        Custom -- Show assets from the asset libraries configured in the Preferences.

      :type: enum in [``'ALL'``, ``'LOCAL'``, ``'ESSENTIALS'``, ``'CUSTOM'``], default ``'ALL'``

   .. attribute:: bl_activate_operator

      Operator to call when activating an item with asset reference properties

      :type: string, default "", (never None)

   .. attribute:: bl_default_preview_size

      Default size of the asset preview thumbnails in pixels

      :type: int in [32, 256], default 0

   .. attribute:: bl_idname

      If this is set, the asset gets a custom ID, otherwise it takes the name of the class used to define the asset (for example, if the class name is "OBJECT_AST_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_AST_hello")

      :type: string, default "", (never None)

   .. attribute:: bl_options

      Options for this asset shelf type

      * ``NO_ASSET_DRAG``
        No Asset Dragging -- Disable the default asset dragging on drag events. Useful for implementing custom dragging via custom key-map items..
      * ``DEFAULT_VISIBLE``
        Visible by Default -- Unhide the asset shelf when it's available for the first time, otherwise it will be hidden.
      * ``STORE_ENABLED_CATALOGS_IN_PREFERENCES``
        Store Enabled Catalogs in Preferences -- Store the shelf's enabled catalogs in the preferences rather than the local asset shelf settings.

      :type: enum set in {``'NO_ASSET_DRAG'``, ``'DEFAULT_VISIBLE'``, ``'STORE_ENABLED_CATALOGS_IN_PREFERENCES'``}, default {``'NO_ASSET_DRAG'``}

   .. attribute:: bl_space_type

      The space where the asset shelf is going to be used in

      :type: enum in :ref:`rna_enum_space_type_items`, default ``'EMPTY'``

   .. attribute:: preview_size

      Size of the asset preview thumbnails in pixels

      :type: int in [32, 256], default 0

   .. attribute:: search_filter

      Filter assets by name

      :type: string, default "", (never None)

   .. attribute:: show_names

      Show the asset name together with the preview. Otherwise only the preview will be visible.

      :type: boolean, default False

   .. classmethod:: poll(context)

      If this method returns a non-null output, the asset shelf will be visible

      :type context: :class:`Context`
      :rtype: boolean

   .. classmethod:: asset_poll(asset)

      Determine if an asset should be visible in the asset shelf. If this method returns a non-null output, the asset will be visible.

      :type asset: :class:`AssetRepresentation`
      :rtype: boolean

   .. classmethod:: get_active_asset()

      Return a reference to the asset that should be highlighted as active in the asset shelf

      :return: The weak reference to the asset to be hightlighted as active, or None
      :rtype: :class:`AssetWeakReference`

   .. classmethod:: draw_context_menu(context, asset, layout)

      Draw UI elements into the context menu UI layout displayed on right click

      :type context: :class:`Context`
      :type asset: :class:`AssetRepresentation`
      :type layout: :class:`UILayout`

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

