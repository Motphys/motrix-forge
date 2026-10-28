Sequencer Operators
===================

.. module:: bpy.ops.sequencer

.. function:: change_effect_type(*, type='CROSS')

   Replace effect strip with another that takes the same number of inputs

   :arg type: Type, Strip effect type

      * ``CROSS``
        Crossfade -- Fade out of one video, fading into another.
      * ``ADD``
        Add -- Add together color channels from two videos.
      * ``SUBTRACT``
        Subtract -- Subtract one strip's color from another.
      * ``ALPHA_OVER``
        Alpha Over -- Blend alpha on top of another video.
      * ``ALPHA_UNDER``
        Alpha Under -- Blend alpha below another video.
      * ``GAMMA_CROSS``
        Gamma Crossfade -- Crossfade with color correction.
      * ``MULTIPLY``
        Multiply -- Multiply color channels from two videos.
      * ``WIPE``
        Wipe -- Sweep a transition line across the frame.
      * ``GLOW``
        Glow -- Add blur and brightness to light areas.
      * ``TRANSFORM``
        Transform -- Apply scale, rotation, or translation.
      * ``COLOR``
        Color -- Add a simple color strip.
      * ``SPEED``
        Speed -- Timewarp video strips, modifying playback speed.
      * ``MULTICAM``
        Multicam Selector -- Control active camera angles.
      * ``ADJUSTMENT``
        Adjustment Layer -- Apply nondestructive effects.
      * ``GAUSSIAN_BLUR``
        Gaussian Blur -- Soften details along axes.
      * ``TEXT``
        Text -- Add a simple text strip.
      * ``COLORMIX``
        Color Mix -- Combine two strips using blend modes.
   :type type: enum in [``'CROSS'``, ``'ADD'``, ``'SUBTRACT'``, ``'ALPHA_OVER'``, ``'ALPHA_UNDER'``, ``'GAMMA_CROSS'``, ``'MULTIPLY'``, ``'WIPE'``, ``'GLOW'``, ``'TRANSFORM'``, ``'COLOR'``, ``'SPEED'``, ``'MULTICAM'``, ``'ADJUSTMENT'``, ``'GAUSSIAN_BLUR'``, ``'TEXT'``, ``'COLORMIX'``], (optional)

.. function:: change_path(*, filepath="", directory="", files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', use_placeholders=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
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
   :arg use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
   :type use_placeholders: boolean, (optional)

.. function:: change_scene(*, scene='')

   Change Scene assigned to Strip

   :arg scene: Scene
   :type scene: enum in [], (optional)

.. function:: connect(*, toggle=True)

   Link selected strips together for simplified group selection

   :arg toggle: Toggle, Toggle strip connections
   :type toggle: boolean, (optional)

.. function:: copy()

   Copy the selected strips to the internal clipboard

.. function:: crossfade_sounds()

   Do cross-fading volume animation of two selected sound strips

   :File: `startup\bl_operators\sequencer.py\:40 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\sequencer.py#L40>`__

.. function:: cursor_set(*, location=(0.0, 0.0))

   Set 2D cursor location

   :arg location: Location, Cursor location in normalized preview coordinates
   :type location: :class:`mathutils.Vector` of 2 items in [-inf, inf], (optional)

.. function:: deinterlace_selected_movies()

   Deinterlace all selected movie sources

   :File: `startup\bl_operators\sequencer.py\:128 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\sequencer.py#L128>`__

.. function:: delete(*, delete_data=False)

   Delete selected strips from the sequencer

   :arg delete_data: Delete Data, After removing the Strip, delete the associated data also
   :type delete_data: boolean, (optional)

.. function:: disconnect()

   Unlink selected strips so that they can be selected individually

.. function:: duplicate()

   Duplicate the selected strips

.. function:: duplicate_move(*, SEQUENCER_OT_duplicate=None, TRANSFORM_OT_seq_slide=None)

   Duplicate selected strips and move them

   :arg SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips
   :type SEQUENCER_OT_duplicate: :class:`SEQUENCER_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
   :type TRANSFORM_OT_seq_slide: :class:`TRANSFORM_OT_seq_slide`, (optional)

.. function:: effect_strip_add(*, type='CROSS', frame_start=0, frame_end=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, color=(0.0, 0.0, 0.0))

   Add an effect to the sequencer, most are applied on top of existing strips

   :arg type: Type, Sequencer effect type

      * ``CROSS``
        Crossfade -- Fade out of one video, fading into another.
      * ``ADD``
        Add -- Add together color channels from two videos.
      * ``SUBTRACT``
        Subtract -- Subtract one strip's color from another.
      * ``ALPHA_OVER``
        Alpha Over -- Blend alpha on top of another video.
      * ``ALPHA_UNDER``
        Alpha Under -- Blend alpha below another video.
      * ``GAMMA_CROSS``
        Gamma Crossfade -- Crossfade with color correction.
      * ``MULTIPLY``
        Multiply -- Multiply color channels from two videos.
      * ``WIPE``
        Wipe -- Sweep a transition line across the frame.
      * ``GLOW``
        Glow -- Add blur and brightness to light areas.
      * ``TRANSFORM``
        Transform -- Apply scale, rotation, or translation.
      * ``COLOR``
        Color -- Add a simple color strip.
      * ``SPEED``
        Speed -- Timewarp video strips, modifying playback speed.
      * ``MULTICAM``
        Multicam Selector -- Control active camera angles.
      * ``ADJUSTMENT``
        Adjustment Layer -- Apply nondestructive effects.
      * ``GAUSSIAN_BLUR``
        Gaussian Blur -- Soften details along axes.
      * ``TEXT``
        Text -- Add a simple text strip.
      * ``COLORMIX``
        Color Mix -- Combine two strips using blend modes.
   :type type: enum in [``'CROSS'``, ``'ADD'``, ``'SUBTRACT'``, ``'ALPHA_OVER'``, ``'ALPHA_UNDER'``, ``'GAMMA_CROSS'``, ``'MULTIPLY'``, ``'WIPE'``, ``'GLOW'``, ``'TRANSFORM'``, ``'COLOR'``, ``'SPEED'``, ``'MULTICAM'``, ``'ADJUSTMENT'``, ``'GAUSSIAN_BLUR'``, ``'TEXT'``, ``'COLORMIX'``], (optional)
   :arg frame_start: Start Frame, Start frame of the sequence strip
   :type frame_start: int in [-inf, inf], (optional)
   :arg frame_end: End Frame, End frame for the color strip
   :type frame_end: int in [-inf, inf], (optional)
   :arg channel: Channel, Channel to place this strip into
   :type channel: int in [1, 128], (optional)
   :arg replace_sel: Replace Selection, Deselect previously selected strips
   :type replace_sel: boolean, (optional)
   :arg overlap: Allow Overlap, Don't correct overlap on new sequence strips
   :type overlap: boolean, (optional)
   :arg overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
   :type overlap_shuffle_override: boolean, (optional)
   :arg skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
   :type skip_locked_or_muted_channels: boolean, (optional)
   :arg color: Color, Initialize the strip with this color
   :type color: :class:`mathutils.Color` of 3 items in [0, 1], (optional)

.. function:: enable_proxies(*, proxy_25=False, proxy_50=False, proxy_75=False, proxy_100=False, overwrite=False)

   Enable selected proxies on all selected Movie and Image strips

   :arg proxy_25: 25%
   :type proxy_25: boolean, (optional)
   :arg proxy_50: 50%
   :type proxy_50: boolean, (optional)
   :arg proxy_75: 75%
   :type proxy_75: boolean, (optional)
   :arg proxy_100: 100%
   :type proxy_100: boolean, (optional)
   :arg overwrite: Overwrite
   :type overwrite: boolean, (optional)

.. function:: export_subtitles(*, filepath="", hide_props_region=True, check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='')

   Export .srt file containing text strips

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

.. function:: fades_add(*, duration_seconds=1.0, type='IN_OUT')

   Adds or updates a fade animation for either visual or audio strips

   :arg duration_seconds: Fade Duration, Duration of the fade in seconds
   :type duration_seconds: float in [0.01, inf], (optional)
   :arg type: Fade Type, Fade in, out, both in and out, to, or from the current frame. Default is both in and out

      * ``IN_OUT``
        Fade In and Out -- Fade selected strips in and out.
      * ``IN``
        Fade In -- Fade in selected strips.
      * ``OUT``
        Fade Out -- Fade out selected strips.
      * ``CURSOR_FROM``
        From Current Frame -- Fade from the time cursor to the end of overlapping strips.
      * ``CURSOR_TO``
        To Current Frame -- Fade from the start of strips under the time cursor to the current frame.
   :type type: enum in [``'IN_OUT'``, ``'IN'``, ``'OUT'``, ``'CURSOR_FROM'``, ``'CURSOR_TO'``], (optional)
   :File: `startup\bl_operators\sequencer.py\:206 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\sequencer.py#L206>`__


.. function:: fades_clear()

   Removes fade animation from selected strips

   :File: `startup\bl_operators\sequencer.py\:147 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\sequencer.py#L147>`__

.. function:: gap_insert(*, frames=10)

   Insert gap at current frame to first strips at the right, independent of selection or locked state of strips

   :arg frames: Frames, Frames to insert after current strip
   :type frames: int in [0, inf], (optional)

.. function:: gap_remove(*, all=False)

   Remove gap at current frame to first strip at the right, independent of selection or locked state of strips

   :arg all: All Gaps, Do all gaps to right of current frame
   :type all: boolean, (optional)

.. function:: image_strip_add(*, directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', frame_start=0, frame_end=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, fit_method='FIT', set_view_transform=True, use_placeholders=False)

   Add an image or image sequence to the sequencer

   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
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

      * ``DEFAULT``
        Default -- Automatically determine sort method for files.
      * ``FILE_SORT_ALPHA``
        Name -- Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION``
        Extension -- Sort the file list by extension/type.
      * ``FILE_SORT_TIME``
        Modified Date -- Sort files by modification time.
      * ``FILE_SORT_SIZE``
        Size -- Sort files by size.
      * ``ASSET_CATALOG``
        Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
   :type sort_method: enum in [``'DEFAULT'``, ``'FILE_SORT_ALPHA'``, ``'FILE_SORT_EXTENSION'``, ``'FILE_SORT_TIME'``, ``'FILE_SORT_SIZE'``, ``'ASSET_CATALOG'``], (optional)
   :arg frame_start: Start Frame, Start frame of the sequence strip
   :type frame_start: int in [-inf, inf], (optional)
   :arg frame_end: End Frame, End frame for the color strip
   :type frame_end: int in [-inf, inf], (optional)
   :arg channel: Channel, Channel to place this strip into
   :type channel: int in [1, 128], (optional)
   :arg replace_sel: Replace Selection, Deselect previously selected strips
   :type replace_sel: boolean, (optional)
   :arg overlap: Allow Overlap, Don't correct overlap on new sequence strips
   :type overlap: boolean, (optional)
   :arg overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
   :type overlap_shuffle_override: boolean, (optional)
   :arg skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
   :type skip_locked_or_muted_channels: boolean, (optional)
   :arg fit_method: Fit Method, Scale fit method

      * ``FIT``
        Scale to Fit -- Scale image to fit within the canvas.
      * ``FILL``
        Scale to Fill -- Scale image to completely fill the canvas.
      * ``STRETCH``
        Stretch to Fill -- Stretch image to fill the canvas.
      * ``ORIGINAL``
        Use Original Size -- Keep image at its original size.
   :type fit_method: enum in [``'FIT'``, ``'FILL'``, ``'STRETCH'``, ``'ORIGINAL'``], (optional)
   :arg set_view_transform: Set View Transform, Set appropriate view transform based on media color space
   :type set_view_transform: boolean, (optional)
   :arg use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
   :type use_placeholders: boolean, (optional)

.. function:: images_separate(*, length=1)

   On image sequence strips, it returns a strip for each image

   :arg length: Length, Length of each frame
   :type length: int in [1, inf], (optional)

.. function:: lock()

   Lock strips so they can't be transformed

.. function:: mask_strip_add(*, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, mask='')

   Add a mask strip to the sequencer

   :arg frame_start: Start Frame, Start frame of the sequence strip
   :type frame_start: int in [-inf, inf], (optional)
   :arg channel: Channel, Channel to place this strip into
   :type channel: int in [1, 128], (optional)
   :arg replace_sel: Replace Selection, Deselect previously selected strips
   :type replace_sel: boolean, (optional)
   :arg overlap: Allow Overlap, Don't correct overlap on new sequence strips
   :type overlap: boolean, (optional)
   :arg overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
   :type overlap_shuffle_override: boolean, (optional)
   :arg skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
   :type skip_locked_or_muted_channels: boolean, (optional)
   :arg mask: Mask
   :type mask: enum in [], (optional)

.. function:: meta_make()

   Group selected strips into a meta-strip

.. function:: meta_separate()

   Put the contents of a meta-strip back in the sequencer

.. function:: meta_toggle()

   Toggle a meta-strip (to edit enclosed strips)

.. function:: movie_strip_add(*, filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, fit_method='FIT', set_view_transform=True, adjust_playback_rate=True, sound=True, use_framerate=True)

   Add a movie strip to the sequencer

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
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

      * ``DEFAULT``
        Default -- Automatically determine sort method for files.
      * ``FILE_SORT_ALPHA``
        Name -- Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION``
        Extension -- Sort the file list by extension/type.
      * ``FILE_SORT_TIME``
        Modified Date -- Sort files by modification time.
      * ``FILE_SORT_SIZE``
        Size -- Sort files by size.
      * ``ASSET_CATALOG``
        Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
   :type sort_method: enum in [``'DEFAULT'``, ``'FILE_SORT_ALPHA'``, ``'FILE_SORT_EXTENSION'``, ``'FILE_SORT_TIME'``, ``'FILE_SORT_SIZE'``, ``'ASSET_CATALOG'``], (optional)
   :arg frame_start: Start Frame, Start frame of the sequence strip
   :type frame_start: int in [-inf, inf], (optional)
   :arg channel: Channel, Channel to place this strip into
   :type channel: int in [1, 128], (optional)
   :arg replace_sel: Replace Selection, Deselect previously selected strips
   :type replace_sel: boolean, (optional)
   :arg overlap: Allow Overlap, Don't correct overlap on new sequence strips
   :type overlap: boolean, (optional)
   :arg overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
   :type overlap_shuffle_override: boolean, (optional)
   :arg skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
   :type skip_locked_or_muted_channels: boolean, (optional)
   :arg fit_method: Fit Method, Scale fit method

      * ``FIT``
        Scale to Fit -- Scale image to fit within the canvas.
      * ``FILL``
        Scale to Fill -- Scale image to completely fill the canvas.
      * ``STRETCH``
        Stretch to Fill -- Stretch image to fill the canvas.
      * ``ORIGINAL``
        Use Original Size -- Keep image at its original size.
   :type fit_method: enum in [``'FIT'``, ``'FILL'``, ``'STRETCH'``, ``'ORIGINAL'``], (optional)
   :arg set_view_transform: Set View Transform, Set appropriate view transform based on media color space
   :type set_view_transform: boolean, (optional)
   :arg adjust_playback_rate: Adjust Playback Rate, Play at normal speed regardless of scene FPS
   :type adjust_playback_rate: boolean, (optional)
   :arg sound: Sound, Load sound with the movie
   :type sound: boolean, (optional)
   :arg use_framerate: Set Scene Frame Rate, Set frame rate of the current scene to the frame rate of the movie
   :type use_framerate: boolean, (optional)

.. function:: movieclip_strip_add(*, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, clip='')

   Add a movieclip strip to the sequencer

   :arg frame_start: Start Frame, Start frame of the sequence strip
   :type frame_start: int in [-inf, inf], (optional)
   :arg channel: Channel, Channel to place this strip into
   :type channel: int in [1, 128], (optional)
   :arg replace_sel: Replace Selection, Deselect previously selected strips
   :type replace_sel: boolean, (optional)
   :arg overlap: Allow Overlap, Don't correct overlap on new sequence strips
   :type overlap: boolean, (optional)
   :arg overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
   :type overlap_shuffle_override: boolean, (optional)
   :arg skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
   :type skip_locked_or_muted_channels: boolean, (optional)
   :arg clip: Clip
   :type clip: enum in [], (optional)

.. function:: mute(*, unselected=False)

   Mute (un)selected strips

   :arg unselected: Unselected, Mute unselected rather than selected strips
   :type unselected: boolean, (optional)

.. function:: offset_clear()

   Clear strip offsets from the start and end frames

.. function:: paste(*, keep_offset=False)

   Paste strips from the internal clipboard

   :arg keep_offset: Keep Offset, Keep strip offset relative to the current frame when pasting
   :type keep_offset: boolean, (optional)

.. function:: preview_duplicate_move(*, SEQUENCER_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Duplicate selected strips and move them

   :arg SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips
   :type SEQUENCER_OT_duplicate: :class:`SEQUENCER_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: reassign_inputs()

   Reassign the inputs for the effect strip

.. function:: rebuild_proxy()

   Rebuild all selected proxies and timecode indices

.. function:: refresh_all()

   Refresh the sequencer editor

.. function:: reload(*, adjust_length=False)

   Reload strips in the sequencer

   :arg adjust_length: Adjust Length, Adjust length of strips to their data length
   :type adjust_length: boolean, (optional)

.. function:: rename_channel()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

.. function:: rendersize()

   Set render size and aspect from active strip

.. function:: retiming_add_freeze_frame_slide(*, SEQUENCER_OT_retiming_freeze_frame_add=None, TRANSFORM_OT_seq_slide=None)

   Add freeze frame and move it

   :arg SEQUENCER_OT_retiming_freeze_frame_add: Add Freeze Frame, Add freeze frame
   :type SEQUENCER_OT_retiming_freeze_frame_add: :class:`SEQUENCER_OT_retiming_freeze_frame_add`, (optional)
   :arg TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
   :type TRANSFORM_OT_seq_slide: :class:`TRANSFORM_OT_seq_slide`, (optional)

.. function:: retiming_add_transition_slide(*, SEQUENCER_OT_retiming_transition_add=None, TRANSFORM_OT_seq_slide=None)

   Add smooth transition between 2 retimed segments and change its duration

   :arg SEQUENCER_OT_retiming_transition_add: Add Speed Transition, Add smooth transition between 2 retimed segments
   :type SEQUENCER_OT_retiming_transition_add: :class:`SEQUENCER_OT_retiming_transition_add`, (optional)
   :arg TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
   :type TRANSFORM_OT_seq_slide: :class:`TRANSFORM_OT_seq_slide`, (optional)

.. function:: retiming_freeze_frame_add(*, duration=0)

   Add freeze frame

   :arg duration: Duration, Duration of freeze frame segment
   :type duration: int in [0, inf], (optional)

.. function:: retiming_key_add(*, timeline_frame=0)

   Add retiming Key

   :arg timeline_frame: Timeline Frame, Frame where key will be added
   :type timeline_frame: int in [0, inf], (optional)

.. function:: retiming_key_delete()

   Delete selected retiming keys from the sequencer

.. function:: retiming_reset()

   Reset strip retiming

.. function:: retiming_segment_speed_set(*, speed=100.0, keep_retiming=True)

   Set speed of retimed segment

   :arg speed: Speed, New speed of retimed segment
   :type speed: float in [0.001, inf], (optional)
   :arg keep_retiming: Preserve Current Retiming, Keep speed of other segments unchanged, change strip length instead
   :type keep_retiming: boolean, (optional)

.. function:: retiming_show()

   Show retiming keys in selected strips

.. function:: retiming_transition_add(*, duration=0)

   Add smooth transition between 2 retimed segments

   :arg duration: Duration, Duration of freeze frame segment
   :type duration: int in [0, inf], (optional)

.. function:: sample(*, size=1)

   Use mouse to sample color in current frame

   :arg size: Sample Size
   :type size: int in [1, 128], (optional)

.. function:: scene_frame_range_update()

   Update frame range of scene strip

.. function:: scene_strip_add(*, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, scene='')

   Add a strip to the sequencer using a Blender scene as a source

   :arg frame_start: Start Frame, Start frame of the sequence strip
   :type frame_start: int in [-inf, inf], (optional)
   :arg channel: Channel, Channel to place this strip into
   :type channel: int in [1, 128], (optional)
   :arg replace_sel: Replace Selection, Deselect previously selected strips
   :type replace_sel: boolean, (optional)
   :arg overlap: Allow Overlap, Don't correct overlap on new sequence strips
   :type overlap: boolean, (optional)
   :arg overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
   :type overlap_shuffle_override: boolean, (optional)
   :arg skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
   :type skip_locked_or_muted_channels: boolean, (optional)
   :arg scene: Scene
   :type scene: enum in [], (optional)

.. function:: scene_strip_add_new(*, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, type='NEW')

   Create a new Strip and assign a new Scene as source

   :arg frame_start: Start Frame, Start frame of the sequence strip
   :type frame_start: int in [-inf, inf], (optional)
   :arg channel: Channel, Channel to place this strip into
   :type channel: int in [1, 128], (optional)
   :arg replace_sel: Replace Selection, Deselect previously selected strips
   :type replace_sel: boolean, (optional)
   :arg overlap: Allow Overlap, Don't correct overlap on new sequence strips
   :type overlap: boolean, (optional)
   :arg overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
   :type overlap_shuffle_override: boolean, (optional)
   :arg skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
   :type skip_locked_or_muted_channels: boolean, (optional)
   :arg type: Type

      * ``NEW``
        New -- Add new Strip with a new empty Scene with default settings.
      * ``EMPTY``
        Copy Settings -- Add a new Strip, with an empty scene, and copy settings from the current scene.
      * ``LINK_COPY``
        Linked Copy -- Add a Strip and link in the collections from the current scene (shallow copy).
      * ``FULL_COPY``
        Full Copy -- Add a Strip and make a full copy of the current scene.
   :type type: enum in [``'NEW'``, ``'EMPTY'``, ``'LINK_COPY'``, ``'FULL_COPY'``], (optional)

.. function:: select(*, wait_to_deselect_others=False, mouse_x=0, mouse_y=0, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, center=False, linked_handle=False, linked_time=False, side_of_frame=False, ignore_connections=False)

   Select a strip (last selected becomes the "active strip")

   :arg wait_to_deselect_others: Wait to Deselect Others
   :type wait_to_deselect_others: boolean, (optional)
   :arg mouse_x: Mouse X
   :type mouse_x: int in [-inf, inf], (optional)
   :arg mouse_y: Mouse Y
   :type mouse_y: int in [-inf, inf], (optional)
   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)
   :arg deselect: Deselect, Remove from selection
   :type deselect: boolean, (optional)
   :arg toggle: Toggle Selection, Toggle the selection
   :type toggle: boolean, (optional)
   :arg deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
   :type deselect_all: boolean, (optional)
   :arg select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
   :type select_passthrough: boolean, (optional)
   :arg center: Center, Use the object center when selecting, in edit mode used to extend object selection
   :type center: boolean, (optional)
   :arg linked_handle: Linked Handle, Select handles next to the active strip
   :type linked_handle: boolean, (optional)
   :arg linked_time: Linked Time, Select other strips or handles at the same time, or all retiming keys after the current in retiming mode
   :type linked_time: boolean, (optional)
   :arg side_of_frame: Side of Frame, Select all strips on same side of the current frame as the mouse cursor
   :type side_of_frame: boolean, (optional)
   :arg ignore_connections: Ignore Connections, Select strips individually whether or not they are connected
   :type ignore_connections: boolean, (optional)

.. function:: select_all(*, action='TOGGLE')

   Select or deselect all strips

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

.. function:: select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET', tweak=False, include_handles=False, ignore_connections=False)

   Select strips using box selection

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
   :arg tweak: Tweak, Make box select pass through to sequence slide when the cursor is hovering on a strip
   :type tweak: boolean, (optional)
   :arg include_handles: Select Handles, Select the strips and their handles
   :type include_handles: boolean, (optional)
   :arg ignore_connections: Ignore Connections, Select strips individually whether or not they are connected
   :type ignore_connections: boolean, (optional)

.. function:: select_grouped(*, type='TYPE', extend=False, use_active_channel=False)

   Select all strips grouped by various properties

   :arg type: Type

      * ``TYPE``
        Type -- Shared strip type.
      * ``TYPE_BASIC``
        Global Type -- All strips of same basic type (graphical or sound).
      * ``TYPE_EFFECT``
        Effect Type -- Shared strip effect type (if active strip is not an effect one, select all non-effect strips).
      * ``DATA``
        Data -- Shared data (scene, image, sound, etc.).
      * ``EFFECT``
        Effect -- Shared effects.
      * ``EFFECT_LINK``
        Effect/Linked -- Other strips affected by the active one (sharing some time, and below or effect-assigned).
      * ``OVERLAP``
        Overlap -- Overlapping time.
   :type type: enum in [``'TYPE'``, ``'TYPE_BASIC'``, ``'TYPE_EFFECT'``, ``'DATA'``, ``'EFFECT'``, ``'EFFECT_LINK'``, ``'OVERLAP'``], (optional)
   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)
   :arg use_active_channel: Same Channel, Only consider strips on the same channel as the active one
   :type use_active_channel: boolean, (optional)

.. function:: select_handle(*, wait_to_deselect_others=False, mouse_x=0, mouse_y=0, ignore_connections=False)

   Select strip handle

   :arg wait_to_deselect_others: Wait to Deselect Others
   :type wait_to_deselect_others: boolean, (optional)
   :arg mouse_x: Mouse X
   :type mouse_x: int in [-inf, inf], (optional)
   :arg mouse_y: Mouse Y
   :type mouse_y: int in [-inf, inf], (optional)
   :arg ignore_connections: Ignore Connections, Select strips individually whether or not they are connected
   :type ignore_connections: boolean, (optional)

.. function:: select_handles(*, side='BOTH')

   Select gizmo handles on the sides of the selected strip

   :arg side: Side, The side of the handle that is selected
   :type side: enum in [``'LEFT'``, ``'RIGHT'``, ``'BOTH'``, ``'LEFT_NEIGHBOR'``, ``'RIGHT_NEIGHBOR'``, ``'BOTH_NEIGHBORS'``], (optional)

.. function:: select_less()

   Shrink the current selection of adjacent selected strips

.. function:: select_linked()

   Select all strips adjacent to the current selection

.. function:: select_linked_pick(*, extend=False)

   Select a chain of linked strips nearest to the mouse pointer

   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)

.. function:: select_more()

   Select more strips adjacent to the current selection

.. function:: select_side(*, side='BOTH')

   Select strips on the nominated side of the selected strips

   :arg side: Side, The side to which the selection is applied
   :type side: enum in [``'MOUSE'``, ``'LEFT'``, ``'RIGHT'``, ``'BOTH'``, ``'NO_CHANGE'``], (optional)

.. function:: select_side_of_frame(*, extend=False, side='LEFT')

   Select strips relative to the current frame

   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)
   :arg side: Side

      * ``LEFT``
        Left -- Select to the left of the current frame.
      * ``RIGHT``
        Right -- Select to the right of the current frame.
      * ``CURRENT``
        Current Frame -- Select intersecting with the current frame.
   :type side: enum in [``'LEFT'``, ``'RIGHT'``, ``'CURRENT'``], (optional)

.. function:: set_range_to_strips(*, preview=False)

   Set the frame range to the selected strips start and end

   :arg preview: Preview, Set the preview range instead
   :type preview: boolean, (optional)

.. function:: slip(*, offset=0.0, slip_keyframes=False)

   Slip the contents of selected strips

   :arg offset: Offset, Offset to the data of the strip
   :type offset: float in [-inf, inf], (optional)
   :arg slip_keyframes: Slip Keyframes, Move the keyframes alongside the media
   :type slip_keyframes: boolean, (optional)

.. function:: snap(*, frame=0)

   Frame where selected strips will be snapped

   :arg frame: Frame, Frame where selected strips will be snapped
   :type frame: int in [-inf, inf], (optional)

.. function:: sound_strip_add(*, filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, cache=False, mono=False)

   Add a sound strip to the sequencer

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
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

      * ``DEFAULT``
        Default -- Automatically determine sort method for files.
      * ``FILE_SORT_ALPHA``
        Name -- Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION``
        Extension -- Sort the file list by extension/type.
      * ``FILE_SORT_TIME``
        Modified Date -- Sort files by modification time.
      * ``FILE_SORT_SIZE``
        Size -- Sort files by size.
      * ``ASSET_CATALOG``
        Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
   :type sort_method: enum in [``'DEFAULT'``, ``'FILE_SORT_ALPHA'``, ``'FILE_SORT_EXTENSION'``, ``'FILE_SORT_TIME'``, ``'FILE_SORT_SIZE'``, ``'ASSET_CATALOG'``], (optional)
   :arg frame_start: Start Frame, Start frame of the sequence strip
   :type frame_start: int in [-inf, inf], (optional)
   :arg channel: Channel, Channel to place this strip into
   :type channel: int in [1, 128], (optional)
   :arg replace_sel: Replace Selection, Deselect previously selected strips
   :type replace_sel: boolean, (optional)
   :arg overlap: Allow Overlap, Don't correct overlap on new sequence strips
   :type overlap: boolean, (optional)
   :arg overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
   :type overlap_shuffle_override: boolean, (optional)
   :arg skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
   :type skip_locked_or_muted_channels: boolean, (optional)
   :arg cache: Cache, Cache the sound in memory
   :type cache: boolean, (optional)
   :arg mono: Mono, Merge all the sound's channels into one
   :type mono: boolean, (optional)

.. function:: split(*, frame=0, channel=0, type='SOFT', use_cursor_position=False, side='MOUSE', ignore_selection=False, ignore_connections=False)

   Split the selected strips in two

   :arg frame: Frame, Frame where selected strips will be split
   :type frame: int in [-inf, inf], (optional)
   :arg channel: Channel, Channel in which strip will be cut
   :type channel: int in [-inf, inf], (optional)
   :arg type: Type, The type of split operation to perform on strips
   :type type: enum in [``'SOFT'``, ``'HARD'``], (optional)
   :arg use_cursor_position: Use Cursor Position, Split at position of the cursor instead of current frame
   :type use_cursor_position: boolean, (optional)
   :arg side: Side, The side that remains selected after splitting
   :type side: enum in [``'MOUSE'``, ``'LEFT'``, ``'RIGHT'``, ``'BOTH'``, ``'NO_CHANGE'``], (optional)
   :arg ignore_selection: Ignore Selection, Make cut even if strip is not selected preserving selection state after cut
   :type ignore_selection: boolean, (optional)
   :arg ignore_connections: Ignore Connections, Don't propagate split to connected strips
   :type ignore_connections: boolean, (optional)

.. function:: split_multicam(*, camera=1)

   Split multicam strip and select camera

   :arg camera: Camera
   :type camera: int in [1, 32], (optional)
   :File: `startup\bl_operators\sequencer.py\:95 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\sequencer.py#L95>`__


.. function:: strip_color_tag_set(*, color='NONE')

   Set a color tag for the selected strips

   :arg color: Color Tag
   :type color: enum in :ref:`rna_enum_strip_color_items`, (optional)

.. function:: strip_jump(*, next=True, center=True)

   Move frame to previous edit point

   :arg next: Next Strip
   :type next: boolean, (optional)
   :arg center: Use Strip Center
   :type center: boolean, (optional)

.. function:: strip_modifier_add(*, type='')

   Add a modifier to the strip

   :arg type: Type
   :type type: enum in [], (optional)

.. function:: strip_modifier_copy(*, type='REPLACE')

   Copy modifiers of the active strip to all selected strips

   :arg type: Type

      * ``REPLACE``
        Replace -- Replace modifiers in destination.
      * ``APPEND``
        Append -- Append active modifiers to selected strips.
   :type type: enum in [``'REPLACE'``, ``'APPEND'``], (optional)

.. function:: strip_modifier_equalizer_redefine(*, graphs='SIMPLE', name="Name")

   Redefine equalizer graphs

   :arg graphs: Graphs, Number of graphs

      * ``SIMPLE``
        Unique -- One unique graphical definition.
      * ``DOUBLE``
        Double -- Graphical definition in 2 sections.
      * ``TRIPLE``
        Triplet -- Graphical definition in 3 sections.
   :type graphs: enum in [``'SIMPLE'``, ``'DOUBLE'``, ``'TRIPLE'``], (optional)
   :arg name: Name, Name of modifier to redefine
   :type name: string, (optional, never None)

.. function:: strip_modifier_move(*, name="Name", direction='UP')

   Move modifier up and down in the stack

   :arg name: Name, Name of modifier to remove
   :type name: string, (optional, never None)
   :arg direction: Type

      * ``UP``
        Up -- Move modifier up in the stack.
      * ``DOWN``
        Down -- Move modifier down in the stack.
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: strip_modifier_remove(*, name="Name")

   Remove a modifier from the strip

   :arg name: Name, Name of modifier to remove
   :type name: string, (optional, never None)

.. function:: strip_transform_clear(*, property='ALL')

   Reset image transformation to default value

   :arg property: Property, Strip transform property to be reset

      * ``POSITION``
        Position -- Reset strip transform location.
      * ``SCALE``
        Scale -- Reset strip transform scale.
      * ``ROTATION``
        Rotation -- Reset strip transform rotation.
      * ``ALL``
        All -- Reset strip transform location, scale and rotation.
   :type property: enum in [``'POSITION'``, ``'SCALE'``, ``'ROTATION'``, ``'ALL'``], (optional)

.. function:: strip_transform_fit(*, fit_method='FIT')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg fit_method: Fit Method, Scale fit fit_method

      * ``FIT``
        Scale to Fit -- Scale image so fits in preview.
      * ``FILL``
        Scale to Fill -- Scale image so it fills preview completely.
      * ``STRETCH``
        Stretch to Fill -- Stretch image so it fills preview.
   :type fit_method: enum in [``'FIT'``, ``'FILL'``, ``'STRETCH'``], (optional)

.. function:: swap(*, side='RIGHT')

   Swap active strip with strip to the right or left

   :arg side: Side, Side of the strip to swap
   :type side: enum in [``'LEFT'``, ``'RIGHT'``], (optional)

.. function:: swap_data()

   Swap 2 sequencer strips

.. function:: swap_inputs()

   Swap the two inputs of the effect strip

.. function:: text_cursor_move(*, type='LINE_BEGIN', select_text=False)

   Move cursor in text

   :arg type: Type, Where to move cursor to, to make a selection
   :type type: enum in [``'LINE_BEGIN'``, ``'LINE_END'``, ``'TEXT_BEGIN'``, ``'TEXT_END'``, ``'PREVIOUS_CHARACTER'``, ``'NEXT_CHARACTER'``, ``'PREVIOUS_WORD'``, ``'NEXT_WORD'``, ``'PREVIOUS_LINE'``, ``'NEXT_LINE'``], (optional)
   :arg select_text: Select Text, Select text while moving cursor
   :type select_text: boolean, (optional)

.. function:: text_cursor_set(*, select_text=False)

   Set cursor position in text

   :arg select_text: Select Text, Select text while moving cursor
   :type select_text: boolean, (optional)

.. function:: text_delete(*, type='NEXT_OR_SELECTION')

   Delete text at cursor position

   :arg type: Type, Which part of the text to delete
   :type type: enum in [``'NEXT_OR_SELECTION'``, ``'PREVIOUS_OR_SELECTION'``], (optional)

.. function:: text_deselect_all()

   Deselect all characters

.. function:: text_edit_copy()

   Copy text to clipboard

.. function:: text_edit_cut()

   Cut text to clipboard

.. function:: text_edit_mode_toggle()

   Toggle text editing

.. function:: text_edit_paste()

   Paste text from clipboard

.. function:: text_insert(*, string="")

   Insert text at cursor position

   :arg string: String, String to be inserted at cursor position
   :type string: string, (optional, never None)

.. function:: text_line_break()

   Insert line break at cursor position

.. function:: text_select_all()

   Select all characters

.. function:: unlock()

   Unlock strips so they can be transformed

.. function:: unmute(*, unselected=False)

   Unmute (un)selected strips

   :arg unselected: Unselected, Unmute unselected rather than selected strips
   :type unselected: boolean, (optional)

.. function:: view_all()

   View all the strips in the sequencer

.. function:: view_all_preview()

   Zoom preview to fit in the area

.. function:: view_frame()

   Move the view to the current frame

.. function:: view_ghost_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Set the boundaries of the border used for offset view

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

.. function:: view_selected()

   Zoom the sequencer on the selected strips

.. function:: view_zoom_ratio(*, ratio=1.0)

   Change zoom ratio of sequencer preview

   :arg ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
   :type ratio: float in [-inf, inf], (optional)

