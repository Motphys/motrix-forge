Screen Operators
================

.. module:: bpy.ops.screen

.. function:: actionzone(*, modifier=0)

   Handle area action zones for mouse actions/gestures

   :arg modifier: Modifier, Modifier state
   :type modifier: int in [0, 2], (optional)

.. function:: animation_cancel(*, restore_frame=True)

   Cancel animation, returning to the original frame

   :arg restore_frame: Restore Frame, Restore the frame when animation was initialized
   :type restore_frame: boolean, (optional)

.. function:: animation_play(*, reverse=False, sync=False)

   Play animation

   :arg reverse: Play in Reverse, Animation is played backwards
   :type reverse: boolean, (optional)
   :arg sync: Sync, Drop frames to maintain framerate
   :type sync: boolean, (optional)

.. function:: animation_step()

   Step through animation by position

.. function:: area_close()

   Close selected area

.. function:: area_dupli()

   Duplicate selected area into new window

.. function:: area_join(*, source_xy=(0, 0), target_xy=(0, 0))

   Join selected areas into new window

   :arg source_xy: Source location
   :type source_xy: int array of 2 items in [-inf, inf], (optional)
   :arg target_xy: Target location
   :type target_xy: int array of 2 items in [-inf, inf], (optional)

.. function:: area_move(*, x=0, y=0, delta=0)

   Move selected area edges

   :arg x: X
   :type x: int in [-inf, inf], (optional)
   :arg y: Y
   :type y: int in [-inf, inf], (optional)
   :arg delta: Delta
   :type delta: int in [-inf, inf], (optional)

.. function:: area_options()

   Operations for splitting and merging

.. function:: area_split(*, direction='HORIZONTAL', factor=0.5, cursor=(0, 0))

   Split selected area into new windows

   :arg direction: Direction
   :type direction: enum in [``'HORIZONTAL'``, ``'VERTICAL'``], (optional)
   :arg factor: Factor
   :type factor: float in [0, 1], (optional)
   :arg cursor: Cursor
   :type cursor: int array of 2 items in [-inf, inf], (optional)

.. function:: area_swap(*, cursor=(0, 0))

   Swap selected areas screen positions

   :arg cursor: Cursor
   :type cursor: int array of 2 items in [-inf, inf], (optional)

.. function:: back_to_previous()

   Revert back to the original screen layout, before fullscreen area overlay

.. function:: delete()

   Delete active screen

.. function:: drivers_editor_show()

   Show drivers editor in a separate window

.. function:: frame_jump(*, end=False)

   Jump to first/last frame in frame range

   :arg end: Last Frame, Jump to the last frame of the frame range
   :type end: boolean, (optional)

.. function:: frame_offset(*, delta=0)

   Move current frame forward/backward by a given number

   :arg delta: Delta
   :type delta: int in [-inf, inf], (optional)

.. function:: header_toggle_menus()

   Expand or collapse the header pull-down menus

.. function:: info_log_show()

   Show info log in a separate window

.. function:: keyframe_jump(*, next=True)

   Jump to previous/next keyframe

   :arg next: Next Keyframe
   :type next: boolean, (optional)

.. function:: marker_jump(*, next=True)

   Jump to previous/next marker

   :arg next: Next Marker
   :type next: boolean, (optional)

.. function:: new()

   Add a new screen

.. function:: redo_last()

   Display parameters for last action performed

.. function:: region_blend()

   Blend in and out overlapping region

.. function:: region_context_menu()

   Display region context menu

.. function:: region_flip()

   Toggle the region's alignment (left/right or top/bottom)

.. function:: region_quadview()

   Split selected area into camera, front, right, and top views

.. function:: region_scale()

   Scale selected area

.. function:: region_toggle(*, region_type='WINDOW')

   Hide or unhide the region

   :arg region_type: Region Type, Type of the region to toggle
   :type region_type: enum in :ref:`rna_enum_region_type_items`, (optional)

.. function:: repeat_history(*, index=0)

   Display menu for previous actions performed

   :arg index: Index
   :type index: int in [0, inf], (optional)

.. function:: repeat_last()

   Repeat last action

.. function:: screen_full_area(*, use_hide_panels=False)

   Toggle display selected area as fullscreen/maximized

   :arg use_hide_panels: Hide Panels, Hide all the panels
   :type use_hide_panels: boolean, (optional)

.. function:: screen_set(*, delta=1)

   Cycle through available screens

   :arg delta: Delta
   :type delta: int in [-1, 1], (optional)

.. function:: screenshot(*, filepath="", hide_props_region=True, check_existing=True, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='')

   Capture a picture of the whole Blender window

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

.. function:: screenshot_area(*, filepath="", hide_props_region=True, check_existing=True, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='')

   Capture a picture of an editor

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

.. function:: space_context_cycle(*, direction='NEXT')

   Cycle through the editor context by activating the next/previous one

   :arg direction: Direction, Direction to cycle through
   :type direction: enum in [``'PREV'``, ``'NEXT'``], (optional)

.. function:: space_type_set_or_cycle(*, space_type='EMPTY')

   Set the space type or cycle subtype

   :arg space_type: Type
   :type space_type: enum in :ref:`rna_enum_space_type_items`, (optional)

.. function:: spacedata_cleanup()

   Remove unused settings for invisible editors

.. function:: userpref_show(*, section='INTERFACE')

   Edit user preferences and system settings

   :arg section: Section to activate in the Preferences
   :type section: enum in :ref:`rna_enum_preference_section_items`, (optional)

.. function:: workspace_cycle(*, direction='NEXT')

   Cycle through workspaces

   :arg direction: Direction, Direction to cycle through
   :type direction: enum in [``'PREV'``, ``'NEXT'``], (optional)

