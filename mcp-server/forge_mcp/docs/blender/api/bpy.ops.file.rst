File Operators
==============

.. module:: bpy.ops.file

.. function:: autopack_toggle()

   Automatically pack all external files into the .blend file

.. function:: bookmark_add()

   Add a bookmark for the selected/active directory

.. function:: bookmark_cleanup()

   Delete all invalid bookmarks

.. function:: bookmark_delete(*, index=-1)

   Delete selected bookmark

   :arg index: Index
   :type index: int in [-1, 20000], (optional)

.. function:: bookmark_move(*, direction='TOP')

   Move the active bookmark up/down in the list

   :arg direction: Direction, Direction to move the active bookmark towards

      * ``TOP``
        Top -- Top of the list.
      * ``UP``
        Up.
      * ``DOWN``
        Down.
      * ``BOTTOM``
        Bottom -- Bottom of the list.
   :type direction: enum in [``'TOP'``, ``'UP'``, ``'DOWN'``, ``'BOTTOM'``], (optional)

.. function:: cancel()

   Cancel file operation

.. function:: delete()

   Move selected files to the trash or recycle bin

.. function:: directory_new(*, directory="", open=False, confirm=True)

   Create a new directory

   :arg directory: Directory, Name of new directory
   :type directory: string, (optional, never None)
   :arg open: Open, Open new directory
   :type open: boolean, (optional)
   :arg confirm: Confirm, Prompt for confirmation
   :type confirm: boolean, (optional)

.. function:: edit_directory_path()

   Start editing directory field

.. function:: execute()

   Execute selected file

.. function:: external_operation(*, filepath="", operation='OPEN')

   Perform external operation on a file or folder

   :arg filepath: File or folder path
   :type filepath: string, (optional, never None)
   :arg operation: Operation, Operation to perform on the file or path

      * ``OPEN``
        Open -- Open the file.
      * ``FOLDER_OPEN``
        Open Folder -- Open the folder.
      * ``EDIT``
        Edit -- Edit the file.
      * ``NEW``
        New -- Create a new file of this type.
      * ``FIND``
        Find File -- Search for files of this type.
      * ``SHOW``
        Show -- Show this file.
      * ``PLAY``
        Play -- Play this file.
      * ``BROWSE``
        Browse -- Browse this file.
      * ``PREVIEW``
        Preview -- Preview this file.
      * ``PRINT``
        Print -- Print this file.
      * ``INSTALL``
        Install -- Install this file.
      * ``RUNAS``
        Run As User -- Run as specific user.
      * ``PROPERTIES``
        Properties -- Show OS Properties for this item.
      * ``FOLDER_FIND``
        Find in Folder -- Search for items in this folder.
      * ``CMD``
        Command Prompt Here -- Open a command prompt here.
   :type operation: enum in [``'OPEN'``, ``'FOLDER_OPEN'``, ``'EDIT'``, ``'NEW'``, ``'FIND'``, ``'SHOW'``, ``'PLAY'``, ``'BROWSE'``, ``'PREVIEW'``, ``'PRINT'``, ``'INSTALL'``, ``'RUNAS'``, ``'PROPERTIES'``, ``'FOLDER_FIND'``, ``'CMD'``], (optional)

.. function:: filenum(*, increment=1)

   Increment number in filename

   :arg increment: Increment
   :type increment: int in [-100, 100], (optional)

.. function:: filepath_drop(*, filepath="Path")

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :type filepath: string, (optional, never None)

.. function:: find_missing_files(*, find_all=False, directory="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=False, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='')

   Try to find missing external files

   :arg find_all: Find All, Find all files in the search path (not just missing)
   :type find_all: boolean, (optional)
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

.. function:: hidedot()

   Toggle hide hidden dot files

.. function:: highlight()

   Highlight selected file(s)

.. function:: make_paths_absolute()

   Make all paths to external files absolute

.. function:: make_paths_relative()

   Make all paths to external files relative to current .blend

.. function:: mouse_execute()

   Perform the current execute action for the file under the cursor (e.g. open the file)

.. function:: next()

   Move to next folder

.. function:: pack_all()

   Pack all used external files into this .blend

.. function:: pack_libraries()

   Store all data-blocks linked from other .blend files in the current .blend file. Library references are preserved so the linked data-blocks can be unpacked again

.. function:: parent()

   Move to parent directory

.. function:: previous()

   Move to previous folder

.. function:: refresh()

   Refresh the file list

.. function:: rename()

   Rename file or file directory

.. function:: report_missing_files()

   Report all missing external files

.. function:: reset_recent()

   Reset recent files

.. function:: select(*, wait_to_deselect_others=False, mouse_x=0, mouse_y=0, extend=False, fill=False, open=True, deselect_all=False, only_activate_if_selected=False, pass_through=False)

   Handle mouse clicks to select and activate items

   :arg wait_to_deselect_others: Wait to Deselect Others
   :type wait_to_deselect_others: boolean, (optional)
   :arg mouse_x: Mouse X
   :type mouse_x: int in [-inf, inf], (optional)
   :arg mouse_y: Mouse Y
   :type mouse_y: int in [-inf, inf], (optional)
   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)
   :arg fill: Fill, Select everything beginning with the last selection
   :type fill: boolean, (optional)
   :arg open: Open, Open a directory when selecting it
   :type open: boolean, (optional)
   :arg deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
   :type deselect_all: boolean, (optional)
   :arg only_activate_if_selected: Only Activate if Selected, Do not change selection if the item under the cursor is already selected, only activate it
   :type only_activate_if_selected: boolean, (optional)
   :arg pass_through: Pass Through, Even on successful execution, pass the event on so other operators can execute on it as well
   :type pass_through: boolean, (optional)

.. function:: select_all(*, action='TOGGLE')

   Select or deselect all files

   :arg action: Action, Selection action to execute

      * ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
      * ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: enum in [``'TOGGLE'``, ``'SELECT'``, ``'DESELECT'``, ``'INVERT'``], (optional)

.. function:: select_bookmark(*, dir="")

   Select a bookmarked directory

   :arg dir: Directory
   :type dir: string, (optional, never None)

.. function:: select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Activate/select the file(s) contained in the border

   :arg xmin: X Min
   :type xmin: int in [-inf, inf], (optional)
   :arg xmax: X Max
   :type xmax: int in [-inf, inf], (optional)
   :arg ymin: Y Min
   :type ymin: int in [-inf, inf], (optional)
   :arg ymax: Y Max
   :type ymax: int in [-inf, inf], (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)
   :arg mode: Mode

      * ``SET``
        Set -- Set a new selection.
      * ``ADD``
        Extend -- Extend existing selection.
      * ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: enum in [``'SET'``, ``'ADD'``, ``'SUB'``], (optional)

.. function:: select_walk(*, direction='UP', extend=False, fill=False)

   Select/Deselect files by walking through them

   :arg direction: Walk Direction, Select/Deselect element in this direction
   :type direction: enum in [``'UP'``, ``'DOWN'``, ``'LEFT'``, ``'RIGHT'``], (optional)
   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)
   :arg fill: Fill, Select everything beginning with the last selection
   :type fill: boolean, (optional)

.. function:: smoothscroll()

   Smooth scroll to make editable file visible

.. function:: sort_column_ui_context()

   Change sorting to use column under cursor

.. function:: start_filter()

   Start entering filter text

.. function:: unpack_all(*, method='USE_LOCAL')

   Unpack all files packed into this .blend to external ones

   :arg method: Method, How to unpack
   :type method: enum in [``'USE_LOCAL'``, ``'WRITE_LOCAL'``, ``'USE_ORIGINAL'``, ``'WRITE_ORIGINAL'``, ``'KEEP'``, ``'REMOVE'``], (optional)

.. function:: unpack_item(*, method='USE_LOCAL', id_name="", id_type=19785)

   Unpack this file to an external file

   :arg method: Method, How to unpack
   :type method: enum in [``'USE_LOCAL'``, ``'WRITE_LOCAL'``, ``'USE_ORIGINAL'``, ``'WRITE_ORIGINAL'``], (optional)
   :arg id_name: ID Name, Name of ID block to unpack
   :type id_name: string, (optional, never None)
   :arg id_type: ID Type, Identifier type of ID block
   :type id_type: int in [0, inf], (optional)

.. function:: unpack_libraries()

   Restore all packed linked data-blocks to their original locations

.. function:: view_selected()

   Scroll the selected files into view

