Preferences Operators
=====================

.. module:: bpy.ops.preferences

.. function:: addon_disable(*, module="")

   Turn off this add-on

   :arg module: Module, Module name of the add-on to disable
   :type module: string, (optional, never None)
   :File: `startup\bl_operators\userpref.py\:547 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L547>`__


.. function:: addon_enable(*, module="")

   Turn on this add-on

   :arg module: Module, Module name of the add-on to enable
   :type module: string, (optional, never None)
   :File: `startup\bl_operators\userpref.py\:483 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L483>`__


.. function:: addon_expand(*, module="")

   Display information and preferences for this add-on

   :arg module: Module, Module name of the add-on to expand
   :type module: string, (optional, never None)
   :File: `startup\bl_operators\userpref.py\:924 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L924>`__


.. function:: addon_install(*, overwrite=True, enable_on_install=False, target='', filepath="", filter_folder=True, filter_python=True, filter_glob="*.py;*.zip")

   Install an add-on

   :arg overwrite: Overwrite, Remove existing add-ons with the same ID
   :type overwrite: boolean, (optional)
   :arg enable_on_install: Enable on Install, Enable after installing
   :type enable_on_install: boolean, (optional)
   :arg target: Target Path
   :type target: enum in [], (optional)
   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_python: Filter Python
   :type filter_python: boolean, (optional)
   :arg filter_glob: filter_glob
   :type filter_glob: string, (optional, never None)
   :File: `startup\bl_operators\userpref.py\:712 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L712>`__


.. function:: addon_refresh()

   Scan add-on directories for new modules

   :File: `startup\bl_operators\userpref.py\:645 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L645>`__

.. function:: addon_remove(*, module="")

   Delete the add-on from the file system

   :arg module: Module, Module name of the add-on to remove
   :type module: string, (optional, never None)
   :File: `startup\bl_operators\userpref.py\:873 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L873>`__


.. function:: addon_show(*, module="")

   Show add-on preferences

   :arg module: Module, Module name of the add-on to expand
   :type module: string, (optional, never None)
   :File: `startup\bl_operators\userpref.py\:950 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L950>`__


.. function:: app_template_install(*, overwrite=True, filepath="", filter_folder=True, filter_glob="*.zip")

   Install an application template

   :arg overwrite: Overwrite, Remove existing template with the same ID
   :type overwrite: boolean, (optional)
   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_glob: filter_glob
   :type filter_glob: string, (optional, never None)
   :File: `startup\bl_operators\userpref.py\:1000 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L1000>`__


.. function:: asset_library_add(*, directory="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='')

   Add a directory to be used by the Asset Browser as source of assets

   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
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

.. function:: asset_library_remove(*, index=0)

   Remove a path to a .blend file, so the Asset Browser will not attempt to show it anymore

   :arg index: Index
   :type index: int in [0, inf], (optional)

.. function:: associate_blend()

   Use this installation for .blend files and to display thumbnails

.. function:: autoexec_path_add()

   Add path to exclude from auto-execution

.. function:: autoexec_path_remove(*, index=0)

   Remove path to exclude from auto-execution

   :arg index: Index
   :type index: int in [0, inf], (optional)

.. function:: copy_prev()

   Copy settings from previous version

   :File: `startup\bl_operators\userpref.py\:170 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L170>`__

.. function:: extension_repo_add(*, name="", remote_url="", use_access_token=False, access_token="", use_sync_on_startup=False, use_custom_directory=False, custom_directory="", type='REMOTE')

   Add a new repository used to store extensions

   :arg name: Name, Unique repository name
   :type name: string, (optional, never None)
   :arg remote_url: URL, Remote URL to the extension repository, the file-system may be referenced using the file URI scheme: "file://"
   :type remote_url: string, (optional, never None)
   :arg use_access_token: Requires Access Token, Repository requires an access token
   :type use_access_token: boolean, (optional)
   :arg access_token: Secret, Personal access token, may be required by some repositories
   :type access_token: string, (optional, never None)
   :arg use_sync_on_startup: Check for Updates on Startup, Allow Blender to check for updates upon launch
   :type use_sync_on_startup: boolean, (optional)
   :arg use_custom_directory: Custom Directory, Manually set the path for extensions to be stored. When disabled a user's extensions directory is created.
   :type use_custom_directory: boolean, (optional)
   :arg custom_directory: Custom Directory, The local directory containing extensions
   :type custom_directory: string, (optional, never None)
   :arg type: Type, The kind of repository to add

      * ``REMOTE``
        Add Remote Repository -- Add a repository referencing a remote repository with support for listing and updating extensions.
      * ``LOCAL``
        Add Local Repository -- Add a repository managed manually without referencing an external repository.
   :type type: enum in [``'REMOTE'``, ``'LOCAL'``], (optional)

.. function:: extension_repo_remove(*, index=0, remove_files=False)

   Remove an extension repository

   :arg index: Index
   :type index: int in [0, inf], (optional)
   :arg remove_files: Remove Files, Remove extension files when removing the repository
   :type remove_files: boolean, (optional)

.. function:: extension_url_drop(*, url="")

   Handle dropping an extension URL

   :arg url: URL, Location of the extension to install
   :type url: string, (optional, never None)

.. function:: keyconfig_activate(*, filepath="")

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :File: `startup\bl_operators\userpref.py\:91 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L91>`__


.. function:: keyconfig_export(*, all=False, filepath="", filter_folder=True, filter_text=True, filter_python=True)

   Export key configuration to a Python script

   :arg all: All Keymaps, Write all keymaps (not just user modified)
   :type all: boolean, (optional)
   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_text: Filter text
   :type filter_text: boolean, (optional)
   :arg filter_python: Filter Python
   :type filter_python: boolean, (optional)
   :File: `startup\bl_operators\userpref.py\:324 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L324>`__


.. function:: keyconfig_import(*, filepath="keymap.py", filter_folder=True, filter_text=True, filter_python=True, keep_original=True)

   Import key configuration from a Python script

   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_text: Filter text
   :type filter_text: boolean, (optional)
   :arg filter_python: Filter Python
   :type filter_python: boolean, (optional)
   :arg keep_original: Keep Original, Keep original file after copying to configuration folder
   :type keep_original: boolean, (optional)
   :File: `startup\bl_operators\userpref.py\:259 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L259>`__


.. function:: keyconfig_remove()

   Remove key config

   :File: `startup\bl_operators\userpref.py\:463 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L463>`__

.. function:: keyconfig_test()

   Test key configuration for conflicts

   :File: `startup\bl_operators\userpref.py\:194 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L194>`__

.. function:: keyitem_add()

   Add key map item

   :File: `startup\bl_operators\userpref.py\:411 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L411>`__

.. function:: keyitem_remove(*, item_id=0)

   Remove key map item

   :arg item_id: Item Identifier, Identifier of the item to remove
   :type item_id: int in [-inf, inf], (optional)
   :File: `startup\bl_operators\userpref.py\:443 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L443>`__


.. function:: keyitem_restore(*, item_id=0)

   Restore key map item

   :arg item_id: Item Identifier, Identifier of the item to restore
   :type item_id: int in [-inf, inf], (optional)
   :File: `startup\bl_operators\userpref.py\:395 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L395>`__


.. function:: keymap_restore(*, all=False)

   Restore key map(s)

   :arg all: All Keymaps, Restore all keymaps to default
   :type all: boolean, (optional)
   :File: `startup\bl_operators\userpref.py\:366 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L366>`__


.. function:: reset_default_theme()

   Reset to the default theme colors

.. function:: script_directory_add(*, directory="", filter_folder=True)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg directory: directory
   :type directory: string, (optional, never None)
   :arg filter_folder: Filter Folders
   :type filter_folder: boolean, (optional)
   :File: `startup\bl_operators\userpref.py\:1256 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L1256>`__


.. function:: script_directory_remove(*, index=0)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg index: Index, Index of the script directory to remove
   :type index: int in [-inf, inf], (optional)
   :File: `startup\bl_operators\userpref.py\:1286 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L1286>`__


.. function:: studiolight_copy_settings(*, index=0)

   Copy Studio Light settings to the Studio Light editor

   :arg index: index
   :type index: int in [-inf, inf], (optional)
   :File: `startup\bl_operators\userpref.py\:1227 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L1227>`__


.. function:: studiolight_install(*, files=None, directory="", filter_folder=True, filter_glob="*.png;*.jpg;*.hdr;*.exr", type='MATCAP')

   Install a user defined light

   :arg files: File Path
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg directory: directory
   :type directory: string, (optional, never None)
   :arg filter_folder: Filter Folders
   :type filter_folder: boolean, (optional)
   :arg filter_glob: filter_glob
   :type filter_glob: string, (optional, never None)
   :arg type: Type

      * ``MATCAP``
        MatCap -- Install custom MatCaps.
      * ``WORLD``
        World -- Install custom HDRIs.
      * ``STUDIO``
        Studio -- Install custom Studio Lights.
   :type type: enum in [``'MATCAP'``, ``'WORLD'``, ``'STUDIO'``], (optional)
   :File: `startup\bl_operators\userpref.py\:1110 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L1110>`__


.. function:: studiolight_new(*, filename="StudioLight")

   Save custom studio light from the studio light editor settings

   :arg filename: Name
   :type filename: string, (optional, never None)
   :File: `startup\bl_operators\userpref.py\:1157 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L1157>`__


.. function:: studiolight_uninstall(*, index=0)

   Delete Studio Light

   :arg index: index
   :type index: int in [-inf, inf], (optional)
   :File: `startup\bl_operators\userpref.py\:1208 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L1208>`__


.. function:: theme_install(*, overwrite=True, filepath="", filter_folder=True, filter_glob="*.xml")

   Load and apply a Blender XML theme file

   :arg overwrite: Overwrite, Remove existing theme file if exists
   :type overwrite: boolean, (optional)
   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_glob: filter_glob
   :type filter_glob: string, (optional, never None)
   :File: `startup\bl_operators\userpref.py\:598 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\userpref.py#L598>`__


.. function:: unassociate_blend()

   Remove this installation's associations with .blend files

