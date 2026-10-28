Brush Operators
===============

.. module:: bpy.ops.brush

.. function:: asset_activate(*, asset_library_type='LOCAL', asset_library_identifier="", relative_asset_identifier="", use_toggle=False)

   Activate a brush asset as current sculpt and paint tool

   :arg asset_library_type: Asset Library Type
   :type asset_library_type: enum in :ref:`rna_enum_asset_library_type_items`, (optional)
   :arg asset_library_identifier: Asset Library Identifier
   :type asset_library_identifier: string, (optional, never None)
   :arg relative_asset_identifier: Relative Asset Identifier
   :type relative_asset_identifier: string, (optional, never None)
   :arg use_toggle: Toggle, Switch between the current and assigned brushes on consecutive uses.
   :type use_toggle: boolean, (optional)

.. function:: asset_delete()

   Delete the active brush asset

.. function:: asset_edit_metadata(*, catalog_path="", author="", description="")

   Edit asset information like the catalog, preview image, tags, or author

   :arg catalog_path: Catalog, The asset's catalog path
   :type catalog_path: string, (optional, never None)
   :arg author: Author
   :type author: string, (optional, never None)
   :arg description: Description
   :type description: string, (optional, never None)

.. function:: asset_load_preview(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='')

   Choose a preview image for the brush

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
   :type hide_props_region: boolean, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg show_multiview: Enable Multi-View
   :type show_multiview: boolean, (optional)
   :arg use_multiview: Use Multi-View
   :type use_multiview: boolean, (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)

.. function:: asset_revert()

   Revert the active brush settings to the default values from the asset library

.. function:: asset_save()

   Update the active brush asset in the asset library with current settings

.. function:: asset_save_as(*, name="", asset_library_reference='', catalog_path="")

   Save a copy of the active brush asset into the default asset library, and make it the active brush

   :arg name: Name, Name for the new brush asset
   :type name: string, (optional, never None)
   :arg asset_library_reference: Library, Asset library used to store the new brush
   :type asset_library_reference: enum in [], (optional)
   :arg catalog_path: Catalog, Catalog to use for the new asset
   :type catalog_path: string, (optional, never None)

.. function:: curve_preset(*, shape='SMOOTH')

   Set brush shape

   :arg shape: Mode
   :type shape: enum in [``'SHARP'``, ``'SMOOTH'``, ``'MAX'``, ``'LINE'``, ``'ROUND'``, ``'ROOT'``], (optional)

.. function:: scale_size(*, scalar=1.0)

   Change brush size by a scalar

   :arg scalar: Scalar, Factor to scale brush size by
   :type scalar: float in [0, 2], (optional)

.. function:: sculpt_curves_falloff_preset(*, shape='SMOOTH')

   Set Curve Falloff Preset

   :arg shape: Mode
   :type shape: enum in [``'SHARP'``, ``'SMOOTH'``, ``'MAX'``, ``'LINE'``, ``'ROUND'``, ``'ROOT'``], (optional)

.. function:: stencil_control(*, mode='TRANSLATION', texmode='PRIMARY')

   Control the stencil brush

   :arg mode: Tool
   :type mode: enum in [``'TRANSLATION'``, ``'SCALE'``, ``'ROTATION'``], (optional)
   :arg texmode: Tool
   :type texmode: enum in [``'PRIMARY'``, ``'SECONDARY'``], (optional)

.. function:: stencil_fit_image_aspect(*, use_repeat=True, use_scale=True, mask=False)

   When using an image texture, adjust the stencil size to fit the image aspect ratio

   :arg use_repeat: Use Repeat, Use repeat mapping values
   :type use_repeat: boolean, (optional)
   :arg use_scale: Use Scale, Use texture scale values
   :type use_scale: boolean, (optional)
   :arg mask: Modify Mask Stencil, Modify either the primary or mask stencil
   :type mask: boolean, (optional)

.. function:: stencil_reset_transform(*, mask=False)

   Reset the stencil transformation to the default

   :arg mask: Modify Mask Stencil, Modify either the primary or mask stencil
   :type mask: boolean, (optional)

