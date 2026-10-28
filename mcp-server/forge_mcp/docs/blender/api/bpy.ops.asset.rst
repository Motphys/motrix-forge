Asset Operators
===============

.. module:: bpy.ops.asset

.. function:: assign_action()

   Set this pose Action as active Action on the active Object

   :File: `addons_core\pose_library\operators.py\:103 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\pose_library\operators.py#L103>`__

.. function:: bundle_install(*, asset_library_reference='', filepath="", hide_props_region=True, check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='')

   Copy the current .blend file into an Asset Library. Only works on standalone .blend files (i.e. when no other files are referenced)

   :arg asset_library_reference: asset_library_reference
   :type asset_library_reference: enum in [], (optional)
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

.. function:: catalog_delete(*, catalog_id="")

   Remove an asset catalog from the asset library (contained assets will not be affected and show up as unassigned)

   :arg catalog_id: Catalog ID, ID of the catalog to delete
   :type catalog_id: string, (optional, never None)

.. function:: catalog_new(*, parent_path="")

   Create a new catalog to put assets in

   :arg parent_path: Parent Path, Optional path defining the location to put the new catalog under
   :type parent_path: string, (optional, never None)

.. function:: catalog_redo()

   Redo the last undone edit to the asset catalogs

.. function:: catalog_undo()

   Undo the last edit to the asset catalogs

.. function:: catalog_undo_push()

   Store the current state of the asset catalogs in the undo buffer

.. function:: catalogs_save()

   Make any edits to any catalogs permanent by writing the current set up to the asset library

.. function:: clear(*, set_fake_user=False)

   Delete all asset metadata and turn the selected asset data-blocks back into normal data-blocks

   :arg set_fake_user: Set Fake User, Ensure the data-block is saved, even when it is no longer marked as asset
   :type set_fake_user: boolean, (optional)

.. function:: clear_single(*, set_fake_user=False)

   Delete all asset metadata and turn the asset data-block back into a normal data-block

   :arg set_fake_user: Set Fake User, Ensure the data-block is saved, even when it is no longer marked as asset
   :type set_fake_user: boolean, (optional)

.. function:: library_refresh()

   Reread assets and asset catalogs from the asset library on disk

.. function:: mark()

   Enable easier reuse of selected data-blocks through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)

.. function:: mark_single()

   Enable easier reuse of a data-block through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)

.. function:: open_containing_blend_file()

   Open the blend file that contains the active asset

   :File: `startup\bl_operators\assets.py\:103 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\assets.py#L103>`__

.. function:: screenshot_preview(*, p1=(0, 0), p2=(0, 0), force_square=True)

   Capture a screenshot to use as a preview for the selected asset

   :arg p1: Point 1, First point of the screenshot in screenspace
   :type p1: int array of 2 items in [0, inf], (optional)
   :arg p2: Point 2, Second point of the screenshot in screenspace
   :type p2: int array of 2 items in [0, inf], (optional)
   :arg force_square: Force Square, If enabled, the screenshot will have the same height as width
   :type force_square: boolean, (optional)

.. function:: tag_add()

   Add a new keyword tag to the active asset

   :File: `startup\bl_operators\assets.py\:42 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\assets.py#L42>`__

.. function:: tag_remove()

   Remove an existing keyword tag from the active asset

   :File: `startup\bl_operators\assets.py\:65 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\assets.py#L65>`__

