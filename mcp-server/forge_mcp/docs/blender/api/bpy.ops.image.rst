Image Operators
===============

.. module:: bpy.ops.image

.. function:: add_render_slot()

   Add a new render slot

.. function:: change_frame(*, frame=0)

   Interactively change the current frame number

   :arg frame: Frame
   :type frame: int in [-1048574, 1048574], (optional)

.. function:: clear_render_border()

   Clear the boundaries of the render region and disable render region

.. function:: clear_render_slot()

   Clear the currently selected render slot

.. function:: clipboard_copy()

   Copy the image to the clipboard

.. function:: clipboard_paste()

   Paste new image from the clipboard

.. function:: convert_to_mesh_plane(*, interpolation='Linear', extension='CLIP', alpha_mode='STRAIGHT', use_auto_refresh=True, relative=True, shader='PRINCIPLED', emit_strength=1.0, use_transparency=True, render_method='DITHERED', use_backface_culling=False, show_transparent_back=True, overwrite_material=True, name_from='OBJECT', delete_ref=True)

   Convert selected reference images to textured mesh plane

   :arg interpolation: Interpolation, Texture interpolation

      * ``Linear``
        Linear -- Linear interpolation.
      * ``Closest``
        Closest -- No interpolation (sample closest texel).
      * ``Cubic``
        Cubic -- Cubic interpolation.
      * ``Smart``
        Smart -- Bicubic when magnifying, else bilinear (OSL only).
   :type interpolation: enum in [``'Linear'``, ``'Closest'``, ``'Cubic'``, ``'Smart'``], (optional)
   :arg extension: Extension, How the image is extrapolated past its original bounds

      * ``CLIP``
        Clip -- Clip to image size and set exterior pixels as transparent.
      * ``EXTEND``
        Extend -- Extend by repeating edge pixels of the image.
      * ``REPEAT``
        Repeat -- Cause the image to repeat horizontally and vertically.
   :type extension: enum in [``'CLIP'``, ``'EXTEND'``, ``'REPEAT'``], (optional)
   :arg alpha_mode: Alpha Mode, Representation of alpha in the image file, to convert to and from when saving and loading the image

      * ``STRAIGHT``
        Straight -- Store RGB and alpha channels separately with alpha acting as a mask, also known as unassociated alpha. Commonly used by image editing applications and file formats like PNG..
      * ``PREMUL``
        Premultiplied -- Store RGB channels with alpha multiplied in, also known as associated alpha. The natural format for renders and used by file formats like OpenEXR..
      * ``CHANNEL_PACKED``
        Channel Packed -- Different images are packed in the RGB and alpha channels, and they should not affect each other. Channel packing is commonly used by game engines to save memory..
      * ``NONE``
        None -- Ignore alpha channel from the file and make image fully opaque.
   :type alpha_mode: enum in [``'STRAIGHT'``, ``'PREMUL'``, ``'CHANNEL_PACKED'``, ``'NONE'``], (optional)
   :arg use_auto_refresh: Auto Refresh, Always refresh image on frame changes
   :type use_auto_refresh: boolean, (optional)
   :arg relative: Relative Paths, Use relative file paths
   :type relative: boolean, (optional)
   :arg shader: Shader, Node shader to use

      * ``PRINCIPLED``
        Principled -- Principled shader.
      * ``SHADELESS``
        Shadeless -- Only visible to camera and reflections.
      * ``EMISSION``
        Emission -- Emission shader.
   :type shader: enum in [``'PRINCIPLED'``, ``'SHADELESS'``, ``'EMISSION'``], (optional)
   :arg emit_strength: Emission Strength, Strength of emission
   :type emit_strength: float in [0, inf], (optional)
   :arg use_transparency: Use Alpha, Use alpha channel for transparency
   :type use_transparency: boolean, (optional)
   :arg render_method: Render Method

      * ``DITHERED``
        Dithered -- Allows for grayscale hashed transparency, and compatible with render passes and ray-tracing. Also known as deferred rendering..
      * ``BLENDED``
        Blended -- Allows for colored transparency, but incompatible with render passes and ray-tracing. Also known as forward rendering..
   :type render_method: enum in [``'DITHERED'``, ``'BLENDED'``], (optional)
   :arg use_backface_culling: Backface Culling, Use backface culling to hide the back side of faces
   :type use_backface_culling: boolean, (optional)
   :arg show_transparent_back: Show Backface, Render multiple transparent layers (may introduce transparency sorting problems)
   :type show_transparent_back: boolean, (optional)
   :arg overwrite_material: Overwrite Material, Overwrite existing material with the same name
   :type overwrite_material: boolean, (optional)
   :arg name_from: Name After, Name for new mesh object and material

      * ``OBJECT``
        Source Object -- Name after object source with a suffix.
      * ``IMAGE``
        Source Image -- Name from loaded image.
   :type name_from: enum in [``'OBJECT'``, ``'IMAGE'``], (optional)
   :arg delete_ref: Delete Reference Object, Delete empty image object once mesh plane is created
   :type delete_ref: boolean, (optional)
   :File: `startup\bl_operators\image_as_planes.py\:1146 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\image_as_planes.py#L1146>`__


.. function:: curves_point_set(*, point='BLACK_POINT', size=1)

   Set black point or white point for curves

   :arg point: Point, Set black point or white point for curves
   :type point: enum in [``'BLACK_POINT'``, ``'WHITE_POINT'``], (optional)
   :arg size: Sample Size
   :type size: int in [1, 128], (optional)

.. function:: cycle_render_slot(*, reverse=False)

   Cycle through all non-void render slots

   :arg reverse: Cycle in Reverse
   :type reverse: boolean, (optional)

.. function:: external_edit(*, filepath="")

   Edit image in an external application

   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :File: `startup\bl_operators\image.py\:54 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\image.py#L54>`__


.. function:: file_browse(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='')

   Open an image file browser, hold Shift to open the file, Alt to browse containing directory

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

.. function:: flip(*, use_flip_x=False, use_flip_y=False)

   Flip the image

   :arg use_flip_x: Horizontal, Flip the image horizontally
   :type use_flip_x: boolean, (optional)
   :arg use_flip_y: Vertical, Flip the image vertically
   :type use_flip_y: boolean, (optional)

.. function:: import_as_mesh_planes(*, interpolation='Linear', extension='CLIP', alpha_mode='STRAIGHT', use_auto_refresh=True, relative=True, shader='PRINCIPLED', emit_strength=1.0, use_transparency=True, render_method='DITHERED', use_backface_culling=False, show_transparent_back=True, overwrite_material=True, filepath="", align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), files=None, directory="", filter_image=True, filter_movie=True, filter_folder=True, force_reload=False, image_sequence=False, offset=True, offset_axis='+X', offset_amount=0.1, align_axis='CAM_AX', prev_align_axis='NONE', align_track=False, size_mode='ABSOLUTE', fill_mode='FILL', height=1.0, factor=600.0)

   Create mesh plane(s) from image files with the appropriate aspect ratio

   :arg interpolation: Interpolation, Texture interpolation

      * ``Linear``
        Linear -- Linear interpolation.
      * ``Closest``
        Closest -- No interpolation (sample closest texel).
      * ``Cubic``
        Cubic -- Cubic interpolation.
      * ``Smart``
        Smart -- Bicubic when magnifying, else bilinear (OSL only).
   :type interpolation: enum in [``'Linear'``, ``'Closest'``, ``'Cubic'``, ``'Smart'``], (optional)
   :arg extension: Extension, How the image is extrapolated past its original bounds

      * ``CLIP``
        Clip -- Clip to image size and set exterior pixels as transparent.
      * ``EXTEND``
        Extend -- Extend by repeating edge pixels of the image.
      * ``REPEAT``
        Repeat -- Cause the image to repeat horizontally and vertically.
   :type extension: enum in [``'CLIP'``, ``'EXTEND'``, ``'REPEAT'``], (optional)
   :arg alpha_mode: Alpha Mode, Representation of alpha in the image file, to convert to and from when saving and loading the image

      * ``STRAIGHT``
        Straight -- Store RGB and alpha channels separately with alpha acting as a mask, also known as unassociated alpha. Commonly used by image editing applications and file formats like PNG..
      * ``PREMUL``
        Premultiplied -- Store RGB channels with alpha multiplied in, also known as associated alpha. The natural format for renders and used by file formats like OpenEXR..
      * ``CHANNEL_PACKED``
        Channel Packed -- Different images are packed in the RGB and alpha channels, and they should not affect each other. Channel packing is commonly used by game engines to save memory..
      * ``NONE``
        None -- Ignore alpha channel from the file and make image fully opaque.
   :type alpha_mode: enum in [``'STRAIGHT'``, ``'PREMUL'``, ``'CHANNEL_PACKED'``, ``'NONE'``], (optional)
   :arg use_auto_refresh: Auto Refresh, Always refresh image on frame changes
   :type use_auto_refresh: boolean, (optional)
   :arg relative: Relative Paths, Use relative file paths
   :type relative: boolean, (optional)
   :arg shader: Shader, Node shader to use

      * ``PRINCIPLED``
        Principled -- Principled shader.
      * ``SHADELESS``
        Shadeless -- Only visible to camera and reflections.
      * ``EMISSION``
        Emission -- Emission shader.
   :type shader: enum in [``'PRINCIPLED'``, ``'SHADELESS'``, ``'EMISSION'``], (optional)
   :arg emit_strength: Emission Strength, Strength of emission
   :type emit_strength: float in [0, inf], (optional)
   :arg use_transparency: Use Alpha, Use alpha channel for transparency
   :type use_transparency: boolean, (optional)
   :arg render_method: Render Method

      * ``DITHERED``
        Dithered -- Allows for grayscale hashed transparency, and compatible with render passes and ray-tracing. Also known as deferred rendering..
      * ``BLENDED``
        Blended -- Allows for colored transparency, but incompatible with render passes and ray-tracing. Also known as forward rendering..
   :type render_method: enum in [``'DITHERED'``, ``'BLENDED'``], (optional)
   :arg use_backface_culling: Backface Culling, Use backface culling to hide the back side of faces
   :type use_backface_culling: boolean, (optional)
   :arg show_transparent_back: Show Backface, Render multiple transparent layers (may introduce transparency sorting problems)
   :type show_transparent_back: boolean, (optional)
   :arg overwrite_material: Overwrite Material, Overwrite existing material with the same name
   :type overwrite_material: boolean, (optional)
   :arg filepath: File Path, Filepath used for importing the file
   :type filepath: string, (optional, never None)
   :arg align: Align

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg files: files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg directory: directory
   :type directory: string, (optional, never None)
   :arg filter_image: filter_image
   :type filter_image: boolean, (optional)
   :arg filter_movie: filter_movie
   :type filter_movie: boolean, (optional)
   :arg filter_folder: filter_folder
   :type filter_folder: boolean, (optional)
   :arg force_reload: Force Reload, Force reload the image if it is already opened elsewhere in Blender
   :type force_reload: boolean, (optional)
   :arg image_sequence: Detect Image Sequences, Import sequentially numbered images as an animated image sequence instead of separate planes
   :type image_sequence: boolean, (optional)
   :arg offset: Offset Planes, Offset planes from each other. If disabled, multiple planes will be created at the same location
   :type offset: boolean, (optional)
   :arg offset_axis: Offset Direction, How planes are oriented relative to each others' local axis

      * ``+X``
        +X -- Side by Side to the Left.
      * ``+Y``
        +Y -- Side by Side, Downward.
      * ``+Z``
        +Z -- Stacked Above.
      * ``-X``
        -X -- Side by Side to the Right.
      * ``-Y``
        -Y -- Side by Side, Upward.
      * ``-Z``
        -Z -- Stacked Below.
   :type offset_axis: enum in [``'+X'``, ``'+Y'``, ``'+Z'``, ``'-X'``, ``'-Y'``, ``'-Z'``], (optional)
   :arg offset_amount: Offset Distance, Set distance between each plane
   :type offset_amount: float in [-inf, inf], (optional)
   :arg align_axis: Align, How to align the planes

      * ``+X``
        +X -- Facing positive X.
      * ``+Y``
        +Y -- Facing positive Y.
      * ``+Z``
        +Z -- Facing positive Z.
      * ``-X``
        -X -- Facing negative X.
      * ``-Y``
        -Y -- Facing negative Y.
      * ``-Z``
        -Z -- Facing negative Z.
      * ``CAM``
        Face Camera -- Facing camera.
      * ``CAM_AX``
        Camera's Main Axis -- Facing the camera's dominant axis.
   :type align_axis: enum in [``'+X'``, ``'+Y'``, ``'+Z'``, ``'-X'``, ``'-Y'``, ``'-Z'``, ``'CAM'``, ``'CAM_AX'``], (optional)
   :arg prev_align_axis: prev_align_axis

      * ``+X``
        +X -- Facing positive X.
      * ``+Y``
        +Y -- Facing positive Y.
      * ``+Z``
        +Z -- Facing positive Z.
      * ``-X``
        -X -- Facing negative X.
      * ``-Y``
        -Y -- Facing negative Y.
      * ``-Z``
        -Z -- Facing negative Z.
      * ``CAM``
        Face Camera -- Facing camera.
      * ``CAM_AX``
        Camera's Main Axis -- Facing the camera's dominant axis.
      * ``NONE``
        Undocumented.
   :type prev_align_axis: enum in [``'+X'``, ``'+Y'``, ``'+Z'``, ``'-X'``, ``'-Y'``, ``'-Z'``, ``'CAM'``, ``'CAM_AX'``, ``'NONE'``], (optional)
   :arg align_track: Track Camera, Add a constraint to make the planes track the camera
   :type align_track: boolean, (optional)
   :arg size_mode: Size Mode, Method for computing the plane size

      * ``ABSOLUTE``
        Absolute -- Use absolute size.
      * ``CAMERA``
        Scale to Camera Frame -- Scale to fit or fill the camera frame.
      * ``DPI``
        Pixels per Inch -- Scale based on pixels per inch.
      * ``DPBU``
        Pixels per Blender Unit -- Scale based on pixels per Blender Unit.
   :type size_mode: enum in [``'ABSOLUTE'``, ``'CAMERA'``, ``'DPI'``, ``'DPBU'``], (optional)
   :arg fill_mode: Scale, Method to scale the plane with the camera frame

      * ``FILL``
        Fill -- Fill camera frame, spilling outside the frame.
      * ``FIT``
        Fit -- Fit entire image within the camera frame.
   :type fill_mode: enum in [``'FILL'``, ``'FIT'``], (optional)
   :arg height: Height, Height of the created plane
   :type height: float in [0.001, inf], (optional)
   :arg factor: Definition, Number of pixels per inch or Blender Unit
   :type factor: float in [1, inf], (optional)
   :File: `startup\bl_operators\image_as_planes.py\:868 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\image_as_planes.py#L868>`__


.. function:: invert(*, invert_r=False, invert_g=False, invert_b=False, invert_a=False)

   Invert image's channels

   :arg invert_r: Red, Invert red channel
   :type invert_r: boolean, (optional)
   :arg invert_g: Green, Invert green channel
   :type invert_g: boolean, (optional)
   :arg invert_b: Blue, Invert blue channel
   :type invert_b: boolean, (optional)
   :arg invert_a: Alpha, Invert alpha channel
   :type invert_a: boolean, (optional)

.. function:: match_movie_length()

   Set image's user's length to the one of this video

.. function:: new(*, name="Untitled", width=1024, height=1024, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='BLANK', float=False, use_stereo_3d=False, tiled=False)

   Create a new image

   :arg name: Name, Image data-block name
   :type name: string, (optional, never None)
   :arg width: Width, Image width
   :type width: int in [1, inf], (optional)
   :arg height: Height, Image height
   :type height: int in [1, inf], (optional)
   :arg color: Color, Default fill color
   :type color: float array of 4 items in [0, inf], (optional)
   :arg alpha: Alpha, Create an image with an alpha channel
   :type alpha: boolean, (optional)
   :arg generated_type: Generated Type, Fill the image with a grid for UV map testing
   :type generated_type: enum in :ref:`rna_enum_image_generated_type_items`, (optional)
   :arg float: 32-bit Float, Create image with 32-bit floating-point bit depth
   :type float: boolean, (optional)
   :arg use_stereo_3d: Stereo 3D, Create an image with left and right views
   :type use_stereo_3d: boolean, (optional)
   :arg tiled: Tiled, Create a tiled image
   :type tiled: boolean, (optional)

.. function:: open(*, allow_path_tokens=True, filepath="", directory="", files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', use_sequence_detection=True, use_udim_detecting=True)

   Open image

   :arg allow_path_tokens: Allow the path to contain substitution tokens
   :type allow_path_tokens: boolean, (optional)
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
   :arg use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected images (based on file names)
   :type use_sequence_detection: boolean, (optional)
   :arg use_udim_detecting: Detect UDIMs, Detect selected UDIM files and load all matching tiles
   :type use_udim_detecting: boolean, (optional)

.. function:: open_images(*, directory="", files=None, relative_path=True, use_sequence_detection=True, use_udim_detection=True)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg directory: directory
   :type directory: string, (optional, never None)
   :arg files: files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg relative_path: Use relative path
   :type relative_path: boolean, (optional)
   :arg use_sequence_detection: Use sequence detection
   :type use_sequence_detection: boolean, (optional)
   :arg use_udim_detection: Use UDIM detection
   :type use_udim_detection: boolean, (optional)
   :File: `startup\bl_operators\image.py\:238 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\image.py#L238>`__


.. function:: pack()

   Pack an image as embedded data into the .blend file

.. function:: project_apply()

   Project edited image back onto the object

   :File: `startup\bl_operators\image.py\:192 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\image.py#L192>`__

.. function:: project_edit()

   Edit a snapshot of the 3D Viewport in an external image editor

   :File: `startup\bl_operators\image.py\:122 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\image.py#L122>`__

.. function:: read_viewlayers()

   Read all the current scene's view layers from cache, as needed

.. function:: reload()

   Reload current image from disk

.. function:: remove_render_slot()

   Remove the current render slot

.. function:: render_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Set the boundaries of the render region and enable render region

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

.. function:: replace(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='')

   Replace current image by another one from disk

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

.. function:: resize(*, size=(0, 0), all_udims=False)

   Resize the image

   :arg size: Size
   :type size: int array of 2 items in [1, inf], (optional)
   :arg all_udims: All UDIM Tiles, Scale all the image's UDIM tiles
   :type all_udims: boolean, (optional)

.. function:: rotate_orthogonal(*, degrees='90')

   Rotate the image

   :arg degrees: Degrees, Amount of rotation in degrees (90, 180, 270)

      * ``90``
        90 Degrees -- Rotate 90 degrees clockwise.
      * ``180``
        180 Degrees -- Rotate 180 degrees clockwise.
      * ``270``
        270 Degrees -- Rotate 270 degrees clockwise.
   :type degrees: enum in [``'90'``, ``'180'``, ``'270'``], (optional)

.. function:: sample(*, size=1)

   Use mouse to sample a color in current image

   :arg size: Sample Size
   :type size: int in [1, 128], (optional)

.. function:: sample_line(*, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5)

   Sample a line and show it in Scope panels

   :arg xstart: X Start
   :type xstart: int in [-inf, inf], (optional)
   :arg xend: X End
   :type xend: int in [-inf, inf], (optional)
   :arg ystart: Y Start
   :type ystart: int in [-inf, inf], (optional)
   :arg yend: Y End
   :type yend: int in [-inf, inf], (optional)
   :arg flip: Flip
   :type flip: boolean, (optional)
   :arg cursor: Cursor, Mouse cursor style to use during the modal operator
   :type cursor: int in [0, inf], (optional)

.. function:: save()

   Save the image with current name and settings

.. function:: save_all_modified()

   Save all modified images

.. function:: save_as(*, save_as_render=False, copy=False, allow_path_tokens=True, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='')

   Save the image with another name and/or settings

   :arg save_as_render: Save As Render, Save image with render color management.For display image formats like PNG, apply view and display transform.For intermediate image formats like OpenEXR, use the default render output color space
   :type save_as_render: boolean, (optional)
   :arg copy: Copy, Create a new image file without modifying the current image in Blender
   :type copy: boolean, (optional)
   :arg allow_path_tokens: Allow the path to contain substitution tokens
   :type allow_path_tokens: boolean, (optional)
   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
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
   :type sort_method: enum in [], (optional)

.. function:: save_sequence()

   Save a sequence of images

.. function:: tile_add(*, number=1002, count=1, label="", fill=True, color=(0.0, 0.0, 0.0, 1.0), generated_type='BLANK', width=1024, height=1024, float=False, alpha=True)

   Adds a tile to the image

   :arg number: Number, UDIM number of the tile
   :type number: int in [1001, 2000], (optional)
   :arg count: Count, How many tiles to add
   :type count: int in [1, inf], (optional)
   :arg label: Label, Optional tile label
   :type label: string, (optional, never None)
   :arg fill: Fill, Fill new tile with a generated image
   :type fill: boolean, (optional)
   :arg color: Color, Default fill color
   :type color: float array of 4 items in [0, inf], (optional)
   :arg generated_type: Generated Type, Fill the image with a grid for UV map testing
   :type generated_type: enum in :ref:`rna_enum_image_generated_type_items`, (optional)
   :arg width: Width, Image width
   :type width: int in [1, inf], (optional)
   :arg height: Height, Image height
   :type height: int in [1, inf], (optional)
   :arg float: 32-bit Float, Create image with 32-bit floating-point bit depth
   :type float: boolean, (optional)
   :arg alpha: Alpha, Create an image with an alpha channel
   :type alpha: boolean, (optional)

.. function:: tile_fill(*, color=(0.0, 0.0, 0.0, 1.0), generated_type='BLANK', width=1024, height=1024, float=False, alpha=True)

   Fill the current tile with a generated image

   :arg color: Color, Default fill color
   :type color: float array of 4 items in [0, inf], (optional)
   :arg generated_type: Generated Type, Fill the image with a grid for UV map testing
   :type generated_type: enum in :ref:`rna_enum_image_generated_type_items`, (optional)
   :arg width: Width, Image width
   :type width: int in [1, inf], (optional)
   :arg height: Height, Image height
   :type height: int in [1, inf], (optional)
   :arg float: 32-bit Float, Create image with 32-bit floating-point bit depth
   :type float: boolean, (optional)
   :arg alpha: Alpha, Create an image with an alpha channel
   :type alpha: boolean, (optional)

.. function:: tile_remove()

   Removes a tile from the image

.. function:: unpack(*, method='USE_LOCAL', id="")

   Save an image packed in the .blend file to disk

   :arg method: Method, How to unpack
   :type method: enum in :ref:`rna_enum_unpack_method_items`, (optional)
   :arg id: Image Name, Image data-block name to unpack
   :type id: string, (optional, never None)

.. function:: view_all(*, fit_view=False)

   View the entire image

   :arg fit_view: Fit View, Fit frame to the viewport
   :type fit_view: boolean, (optional)

.. function:: view_center_cursor()

   Center the view so that the cursor is in the middle of the view

.. function:: view_cursor_center(*, fit_view=False)

   Set 2D Cursor To Center View location

   :arg fit_view: Fit View, Fit frame to the viewport
   :type fit_view: boolean, (optional)

.. function:: view_ndof()

   Use a 3D mouse device to pan/zoom the view

.. function:: view_pan(*, offset=(0.0, 0.0))

   Pan the view

   :arg offset: Offset, Offset in floating-point units, 1.0 is the width and height of the image
   :type offset: :class:`mathutils.Vector` of 2 items in [-inf, inf], (optional)

.. function:: view_selected()

   View all selected UVs

.. function:: view_zoom(*, factor=0.0, use_cursor_init=True)

   Zoom in/out the image

   :arg factor: Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out
   :type factor: float in [-inf, inf], (optional)
   :arg use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
   :type use_cursor_init: boolean, (optional)

.. function:: view_zoom_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, zoom_out=False)

   Zoom in the view to the nearest item contained in the border

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
   :arg zoom_out: Zoom Out
   :type zoom_out: boolean, (optional)

.. function:: view_zoom_in(*, location=(0.0, 0.0))

   Zoom in the image (centered around 2D cursor)

   :arg location: Location, Cursor location in screen coordinates
   :type location: :class:`mathutils.Vector` of 2 items in [-inf, inf], (optional)

.. function:: view_zoom_out(*, location=(0.0, 0.0))

   Zoom out the image (centered around 2D cursor)

   :arg location: Location, Cursor location in screen coordinates
   :type location: :class:`mathutils.Vector` of 2 items in [-inf, inf], (optional)

.. function:: view_zoom_ratio(*, ratio=0.0)

   Set zoom ratio of the view

   :arg ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
   :type ratio: float in [-inf, inf], (optional)

