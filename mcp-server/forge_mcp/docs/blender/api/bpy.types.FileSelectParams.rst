FileSelectParams(bpy_struct)
============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`FileAssetSelectParams`

.. class:: FileSelectParams(bpy_struct)

   File Select Parameters

   .. attribute:: directory

      Directory displayed in the file browser

      :type: byte string, default "", (never None)

   .. attribute:: display_size

      Change the size of thumbnails

      :type: int in [16, 256], default 96

   .. attribute:: display_size_discrete

      Change the size of thumbnails in discrete steps

      :type: enum in [``'TINY'``, ``'SMALL'``, ``'NORMAL'``, ``'BIG'``, ``'LARGE'``], default ``'TINY'``

   .. attribute:: display_type

      Display mode for the file list

      * ``LIST_VERTICAL``
        Vertical List -- Display files as a vertical list.
      * ``LIST_HORIZONTAL``
        Horizontal List -- Display files as a horizontal list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.

      :type: enum in [``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], default ``'LIST_VERTICAL'``

   .. attribute:: filename

      Active file in the file browser

      :type: string, default "", (never None)

   .. attribute:: filter_glob

      UNIX shell-like filename patterns matching, supports wildcards ('*') and list of patterns separated by ';'

      :type: string, default "", (never None)

   .. data:: filter_id

      Which ID types to show/hide, when browsing a library

      :type: :class:`FileSelectIDFilter`, (readonly, never None)

   .. attribute:: filter_search

      Filter by name or tag, supports '*' wildcard

      :type: string, default "", (never None)

   .. attribute:: list_column_size

      The width of columns in horizontal list views

      :type: int in [32, 750], default 32

   .. attribute:: list_display_size

      Change the size of thumbnails in list views

      :type: int in [16, 128], default 32

   .. attribute:: recursion_level

      Numbers of dirtree levels to show simultaneously

      * ``NONE``
        None -- Only list current directory's content, with no recursion.
      * ``BLEND``
        Blend File -- List .blend files' content.
      * ``ALL_1``
        One Level -- List all sub-directories' content, one level of recursion.
      * ``ALL_2``
        Two Levels -- List all sub-directories' content, two levels of recursion.
      * ``ALL_3``
        Three Levels -- List all sub-directories' content, three levels of recursion.

      :type: enum in [``'NONE'``, ``'BLEND'``, ``'ALL_1'``, ``'ALL_2'``, ``'ALL_3'``], default ``'NONE'``

   .. attribute:: show_details_datetime

      Show a column listing the date and time of modification for each file

      :type: boolean, default False

   .. attribute:: show_details_size

      Show a column listing the size of each file

      :type: boolean, default False

   .. attribute:: show_hidden

      Show hidden dot files

      :type: boolean, default False

   .. attribute:: sort_method

      :type: enum in :ref:`rna_enum_fileselect_params_sort_items`, default ``'FILE_SORT_ALPHA'``

   .. data:: title

      Title for the file browser

      :type: string, default "", (readonly, never None)

   .. attribute:: use_filter

      Enable filtering of files

      :type: boolean, default False

   .. attribute:: use_filter_asset_only

      Hide .blend files items that are not data-blocks with asset metadata

      :type: boolean, default False

   .. attribute:: use_filter_backup

      Show .blend1, .blend2, etc. files

      :type: boolean, default False

   .. attribute:: use_filter_blender

      Show .blend files

      :type: boolean, default False

   .. attribute:: use_filter_blendid

      Show .blend files items (objects, materials, etc.)

      :type: boolean, default False

   .. attribute:: use_filter_folder

      Show folders

      :type: boolean, default False

   .. attribute:: use_filter_font

      Show font files

      :type: boolean, default False

   .. attribute:: use_filter_image

      Show image files

      :type: boolean, default False

   .. attribute:: use_filter_movie

      Show movie files

      :type: boolean, default False

   .. attribute:: use_filter_script

      Show script files

      :type: boolean, default False

   .. attribute:: use_filter_sound

      Show sound files

      :type: boolean, default False

   .. attribute:: use_filter_text

      Show text files

      :type: boolean, default False

   .. attribute:: use_filter_volume

      Show 3D volume files

      :type: boolean, default False

   .. data:: use_library_browsing

      Whether we may browse Blender files' content or not

      :type: boolean, default False, (readonly)

   .. attribute:: use_sort_invert

      Sort items descending, from highest value to lowest

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

   * :class:`SpaceFileBrowser.params`
   * :class:`UILayout.template_file_select_path`

