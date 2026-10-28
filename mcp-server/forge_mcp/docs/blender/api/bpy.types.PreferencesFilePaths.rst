PreferencesFilePaths(bpy_struct)
================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PreferencesFilePaths(bpy_struct)

   Default paths for external files

   .. attribute:: active_asset_library

      Index of the asset library being edited in the Preferences UI

      :type: int in [-32768, 32767], default 0

   .. attribute:: animation_player

      Path to a custom animation/frame sequence player

      :type: string, default "", (never None)

   .. attribute:: animation_player_preset

      Preset configs for external animation players

      * ``INTERNAL``
        Internal -- Built-in animation player.
      * ``DJV``
        DJV -- Open source frame player.
      * ``FRAMECYCLER``
        FrameCycler -- Frame player from IRIDAS.
      * ``RV``
        RV -- Frame player from Tweak Software.
      * ``MPLAYER``
        MPlayer -- Media player for video and PNG/JPEG/SGI image sequences.
      * ``CUSTOM``
        Custom -- Custom animation player executable path.

      :type: enum in [``'INTERNAL'``, ``'DJV'``, ``'FRAMECYCLER'``, ``'RV'``, ``'MPLAYER'``, ``'CUSTOM'``], default ``'INTERNAL'``

   .. data:: asset_libraries

      :type: :class:`AssetLibraryCollection` :class:`bpy_prop_collection` of :class:`UserAssetLibrary`, (readonly)

   .. attribute:: auto_save_time

      The time (in minutes) to wait between automatic temporary saves

      :type: int in [1, 60], default 2

   .. attribute:: file_preview_type

      What type of blend preview to create

      * ``NONE``
        None -- Do not create blend previews.
      * ``AUTO``
        Auto -- Automatically select best preview type.
      * ``SCREENSHOT``
        Screenshot -- Capture the entire window.
      * ``CAMERA``
        Camera View -- Workbench render of scene.

      :type: enum in [``'NONE'``, ``'AUTO'``, ``'SCREENSHOT'``, ``'CAMERA'``], default ``'AUTO'``

   .. attribute:: font_directory

      The default directory to search for loading fonts

      :type: string, default "", (never None, blend relative ``//`` prefix supported)

   .. attribute:: i18n_branches_directory

      The path to the '/branches' directory of your local svn-translation copy, to allow translating from the UI

      :type: string, default "", (never None)

   .. attribute:: image_editor

      Path to an image editor

      :type: string, default "", (never None)

   .. attribute:: recent_files

      Maximum number of recently opened files to remember

      :type: int in [0, 30], default 20

   .. attribute:: render_cache_directory

      Where to cache raw render results

      :type: string, default "", (never None, blend relative ``//`` prefix supported)

   .. attribute:: render_output_directory

      The default directory for rendering output, for new scenes

      :type: string, default "", (never None, blend relative ``//`` prefix supported)

   .. attribute:: save_version

      The number of old versions to maintain in the current directory, when manually saving

      :type: int in [0, 32], default 1

   .. data:: script_directories

      :type: :class:`ScriptDirectoryCollection` :class:`bpy_prop_collection` of :class:`ScriptDirectory`, (readonly)

   .. attribute:: show_hidden_files_datablocks

      Show files and data-blocks that are normally hidden

      :type: boolean, default True

   .. attribute:: show_recent_locations

      Show Recent locations list in the File Browser

      :type: boolean, default True

   .. attribute:: show_system_bookmarks

      Show System locations list in the File Browser

      :type: boolean, default True

   .. attribute:: sound_directory

      The default directory to search for sounds

      :type: string, default "", (never None, blend relative ``//`` prefix supported)

   .. attribute:: temporary_directory

      The directory for storing temporary save files. The path must reference an existing directory or it will be ignored

      :type: string, default "", (never None)

   .. attribute:: text_editor

      Command to launch the text editor, either a full path or a command in $PATH.
      Use the internal editor when left blank

      :type: string, default "", (never None)

   .. attribute:: text_editor_args

      Defines the specific format of the arguments with which the text editor opens files. The supported expansions are as follows:
      
      $filepath The absolute path of the file.
      $line The line to open at (Optional).
      $column The column to open from the beginning of the line (Optional).
      $line0 & column0 start at zero.
      Example: -f $filepath -l $line -c $column

      :type: string, default "", (never None)

   .. attribute:: texture_directory

      The default directory to search for textures

      :type: string, default "", (never None, blend relative ``//`` prefix supported)

   .. attribute:: use_auto_save_temporary_files

      Automatic saving of temporary files in temp directory, uses process ID.
      Warning: Sculpt and edit mode data won't be saved

      :type: boolean, default True

   .. attribute:: use_extension_online_access_handled

      The user has been shown the "Online Access" prompt and made a choice

      :type: boolean, default False

   .. attribute:: use_file_compression

      Enable file compression when saving .blend files

      :type: boolean, default False

   .. attribute:: use_filter_files

      Enable filtering of files in the File Browser

      :type: boolean, default True

   .. attribute:: use_load_ui

      Load user interface setup when loading .blend files

      :type: boolean, default True

   .. attribute:: use_relative_paths

      Default relative path option for the file selector, when no path is defined yet

      :type: boolean, default True

   .. attribute:: use_scripts_auto_execute

      Allow any .blend file to run scripts automatically (unsafe with blend files from an untrusted source)

      :type: boolean, default False

   .. attribute:: use_tabs_as_spaces

      Automatically convert all new tabs into spaces for new and loaded text files

      :type: boolean, default True

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

   * :class:`Preferences.filepaths`

