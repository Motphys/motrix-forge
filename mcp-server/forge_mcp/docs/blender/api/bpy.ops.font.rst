Font Operators
==============

.. module:: bpy.ops.font

.. function:: case_set(*, case='LOWER')

   Set font case

   :arg case: Case, Lower or upper case
   :type case: enum in [``'LOWER'``, ``'UPPER'``], (optional)

.. function:: case_toggle()

   Toggle font case

.. function:: change_character(*, delta=1)

   Change font character code

   :arg delta: Delta, Number to increase or decrease character code with
   :type delta: int in [-255, 255], (optional)

.. function:: change_spacing(*, delta=1.0)

   Change font spacing

   :arg delta: Delta, Amount to decrease or increase character spacing with
   :type delta: float in [-inf, inf], (optional)

.. function:: delete(*, type='PREVIOUS_CHARACTER')

   Delete text by cursor position

   :arg type: Type, Which part of the text to delete
   :type type: enum in [``'NEXT_CHARACTER'``, ``'PREVIOUS_CHARACTER'``, ``'NEXT_WORD'``, ``'PREVIOUS_WORD'``, ``'SELECTION'``, ``'NEXT_OR_SELECTION'``, ``'PREVIOUS_OR_SELECTION'``], (optional)

.. function:: line_break()

   Insert line break at cursor position

.. function:: move(*, type='LINE_BEGIN')

   Move cursor to position type

   :arg type: Type, Where to move cursor to
   :type type: enum in [``'LINE_BEGIN'``, ``'LINE_END'``, ``'TEXT_BEGIN'``, ``'TEXT_END'``, ``'PREVIOUS_CHARACTER'``, ``'NEXT_CHARACTER'``, ``'PREVIOUS_WORD'``, ``'NEXT_WORD'``, ``'PREVIOUS_LINE'``, ``'NEXT_LINE'``, ``'PREVIOUS_PAGE'``, ``'NEXT_PAGE'``], (optional)

.. function:: move_select(*, type='LINE_BEGIN')

   Move the cursor while selecting

   :arg type: Type, Where to move cursor to, to make a selection
   :type type: enum in [``'LINE_BEGIN'``, ``'LINE_END'``, ``'TEXT_BEGIN'``, ``'TEXT_END'``, ``'PREVIOUS_CHARACTER'``, ``'NEXT_CHARACTER'``, ``'PREVIOUS_WORD'``, ``'NEXT_WORD'``, ``'PREVIOUS_LINE'``, ``'NEXT_LINE'``, ``'PREVIOUS_PAGE'``, ``'NEXT_PAGE'``], (optional)

.. function:: open(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=True, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='THUMBNAIL', sort_method='')

   Load a new font from a file

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
   :arg relative_path: Relative Path, Select the file relative to the blend file
   :type relative_path: boolean, (optional)
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

.. function:: select_all()

   Select all text

.. function:: select_word()

   Select word under cursor

.. function:: selection_set()

   Set cursor selection

.. function:: style_set(*, style='BOLD', clear=False)

   Set font style

   :arg style: Style, Style to set selection to
   :type style: enum in [``'BOLD'``, ``'ITALIC'``, ``'UNDERLINE'``, ``'SMALL_CAPS'``], (optional)
   :arg clear: Clear, Clear style rather than setting it
   :type clear: boolean, (optional)

.. function:: style_toggle(*, style='BOLD')

   Toggle font style

   :arg style: Style, Style to set selection to
   :type style: enum in [``'BOLD'``, ``'ITALIC'``, ``'UNDERLINE'``, ``'SMALL_CAPS'``], (optional)

.. function:: text_copy()

   Copy selected text to clipboard

.. function:: text_cut()

   Cut selected text to clipboard

.. function:: text_insert(*, text="", accent=False)

   Insert text at cursor position

   :arg text: Text, Text to insert at the cursor position
   :type text: string, (optional, never None)
   :arg accent: Accent Mode, Next typed character will strike through previous, for special character input
   :type accent: boolean, (optional)

.. function:: text_insert_unicode()

   Insert Unicode Character

.. function:: text_paste(*, selection=False)

   Paste text from clipboard

   :arg selection: Selection, Paste text selected elsewhere rather than copied (X11/Wayland only)
   :type selection: boolean, (optional)

.. function:: text_paste_from_file(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=True, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='')

   Paste contents from file

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

.. function:: textbox_add()

   Add a new text box

.. function:: textbox_remove(*, index=0)

   Remove the text box

   :arg index: Index, The current text box
   :type index: int in [0, inf], (optional)

.. function:: unlink()

   Unlink active font data-block

