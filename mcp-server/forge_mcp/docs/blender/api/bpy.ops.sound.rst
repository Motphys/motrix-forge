Sound Operators
===============

.. module:: bpy.ops.sound

.. function:: bake_animation()

   Update the audio animation cache

.. function:: mixdown(*, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', accuracy=1024, container='FLAC', codec='FLAC', channels='STEREO', format='S16', mixrate=48000, bitrate=192, split_channels=False)

   Mix the scene's audio to a sound file

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
   :arg accuracy: Accuracy, Sample accuracy, important for animation data (the lower the value, the more accurate)
   :type accuracy: int in [1, inf], (optional)
   :arg container: Container, File format

      * ``AAC``
        AAC -- Advanced Audio Coding.
      * ``AC3``
        AC3 -- Dolby Digital ATRAC 3.
      * ``FLAC``
        FLAC -- Free Lossless Audio Codec.
      * ``MATROSKA``
        MKV -- Matroska.
      * ``MP2``
        MP2 -- MPEG-1 Audio Layer II.
      * ``MP3``
        MP3 -- MPEG-2 Audio Layer III.
      * ``OGG``
        OGG -- Xiph.Org Ogg Container.
      * ``WAV``
        WAV -- Waveform Audio File Format.
   :type container: enum in [``'AAC'``, ``'AC3'``, ``'FLAC'``, ``'MATROSKA'``, ``'MP2'``, ``'MP3'``, ``'OGG'``, ``'WAV'``], (optional)
   :arg codec: Codec, Audio Codec

      * ``AAC``
        AAC -- Advanced Audio Coding.
      * ``AC3``
        AC3 -- Dolby Digital ATRAC 3.
      * ``FLAC``
        FLAC -- Free Lossless Audio Codec.
      * ``MP2``
        MP2 -- MPEG-1 Audio Layer II.
      * ``MP3``
        MP3 -- MPEG-2 Audio Layer III.
      * ``PCM``
        PCM -- Pulse Code Modulation (RAW).
      * ``VORBIS``
        Vorbis -- Xiph.Org Vorbis Codec.
   :type codec: enum in [``'AAC'``, ``'AC3'``, ``'FLAC'``, ``'MP2'``, ``'MP3'``, ``'PCM'``, ``'VORBIS'``], (optional)
   :arg channels: Channels, Audio channel count

      * ``MONO``
        Mono -- Single audio channel.
      * ``STEREO``
        Stereo -- Stereo audio channels.
      * ``STEREO_LFE``
        Stereo LFE -- Stereo with LFE channel.
      * ``SURROUND4``
        4 Channels -- 4 channel surround sound.
      * ``SURROUND5``
        5 Channels -- 5 channel surround sound.
      * ``SURROUND51``
        5.1 Surround -- 5.1 surround sound.
      * ``SURROUND61``
        6.1 Surround -- 6.1 surround sound.
      * ``SURROUND71``
        7.1 Surround -- 7.1 surround sound.
   :type channels: enum in [``'MONO'``, ``'STEREO'``, ``'STEREO_LFE'``, ``'SURROUND4'``, ``'SURROUND5'``, ``'SURROUND51'``, ``'SURROUND61'``, ``'SURROUND71'``], (optional)
   :arg format: Format, Sample format

      * ``U8``
        U8 -- 8-bit unsigned.
      * ``S16``
        S16 -- 16-bit signed.
      * ``S24``
        S24 -- 24-bit signed.
      * ``S32``
        S32 -- 32-bit signed.
      * ``F32``
        F32 -- 32-bit floating-point.
      * ``F64``
        F64 -- 64-bit floating-point.
   :type format: enum in [``'U8'``, ``'S16'``, ``'S24'``, ``'S32'``, ``'F32'``, ``'F64'``], (optional)
   :arg mixrate: Sample Rate, Sample rate in samples/s
   :type mixrate: int in [8000, 192000], (optional)
   :arg bitrate: Bitrate, Bitrate in kbit/s
   :type bitrate: int in [32, 512], (optional)
   :arg split_channels: Split channels, Each channel will be rendered into a mono file
   :type split_channels: boolean, (optional)

.. function:: open(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', cache=False, mono=False)

   Load a sound file

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
   :arg cache: Cache, Cache the sound in memory
   :type cache: boolean, (optional)
   :arg mono: Mono, Merge all the sound's channels into one
   :type mono: boolean, (optional)

.. function:: open_mono(*, filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', cache=False, mono=True)

   Load a sound file as mono

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
   :arg cache: Cache, Cache the sound in memory
   :type cache: boolean, (optional)
   :arg mono: Mono, Mixdown the sound to mono
   :type mono: boolean, (optional)

.. function:: pack()

   Pack the sound into the current blend file

.. function:: unpack(*, method='USE_LOCAL', id="")

   Unpack the sound to the samples filename

   :arg method: Method, How to unpack
   :type method: enum in :ref:`rna_enum_unpack_method_items`, (optional)
   :arg id: Sound Name, Sound data-block name to unpack
   :type id: string, (optional, never None)

.. function:: update_animation_flags()

   Update animation flags

