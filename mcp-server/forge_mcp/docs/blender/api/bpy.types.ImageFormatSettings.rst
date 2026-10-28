ImageFormatSettings(bpy_struct)
===============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ImageFormatSettings(bpy_struct)

   Settings for image formats

   .. attribute:: cineon_black

      Log conversion reference blackpoint

      :type: int in [0, 1024], default 0

   .. attribute:: cineon_gamma

      Log conversion gamma

      :type: float in [0, 10], default 0.0

   .. attribute:: cineon_white

      Log conversion reference whitepoint

      :type: int in [0, 1024], default 0

   .. attribute:: color_depth

      Bit depth per channel

      :type: enum in :ref:`rna_enum_image_color_depth_items`, default ``'8'``

   .. attribute:: color_management

      Which color management settings to use for file saving

      :type: enum in [``'FOLLOW_SCENE'``, ``'OVERRIDE'``], default ``'FOLLOW_SCENE'``

   .. attribute:: color_mode

      Choose BW for saving grayscale images, RGB for saving red, green and blue channels, and RGBA for saving red, green, blue and alpha channels

      :type: enum in :ref:`rna_enum_image_color_mode_items`, default ``'BW'``

   .. attribute:: compression

      Amount of time to determine best compression: 0 = no compression with fast file output, 100 = maximum lossless compression with slow file output

      :type: int in [0, 100], default 15

   .. data:: display_settings

      Settings of device saved image would be displayed on

      :type: :class:`ColorManagedDisplaySettings`, (readonly)

   .. attribute:: exr_codec

      Compression codec settings for OpenEXR

      :type: enum in :ref:`rna_enum_exr_codec_items`, default ``'NONE'``

   .. attribute:: file_format

      File format to save the rendered images as

      :type: enum in :ref:`rna_enum_image_type_items`, default ``'PNG'``

   .. data:: has_linear_colorspace

      File format expects linear color space

      :type: boolean, default False, (readonly)

   .. attribute:: jpeg2k_codec

      Codec settings for JPEG 2000

      :type: enum in [``'JP2'``, ``'J2K'``], default ``'JP2'``

   .. data:: linear_colorspace_settings

      Output color space settings

      :type: :class:`ColorManagedInputColorspaceSettings`, (readonly)

   .. attribute:: quality

      Quality for image formats that support lossy compression

      :type: int in [0, 100], default 90

   .. data:: stereo_3d_format

      Settings for stereo 3D

      :type: :class:`Stereo3dFormat`, (readonly, never None)

   .. attribute:: tiff_codec

      Compression mode for TIFF

      :type: enum in [``'NONE'``, ``'DEFLATE'``, ``'LZW'``, ``'PACKBITS'``], default ``'DEFLATE'``

   .. attribute:: use_cineon_log

      Convert to logarithmic color space

      :type: boolean, default False

   .. attribute:: use_jpeg2k_cinema_48

      Use OpenJPEG Cinema Preset (48fps)

      :type: boolean, default False

   .. attribute:: use_jpeg2k_cinema_preset

      Use OpenJPEG Cinema Preset

      :type: boolean, default False

   .. attribute:: use_jpeg2k_ycc

      Save luminance-chrominance-chrominance channels instead of RGB colors

      :type: boolean, default False

   .. attribute:: use_preview

      When rendering animations, save JPG preview images in same directory

      :type: boolean, default False

   .. data:: view_settings

      Color management settings applied on image before saving

      :type: :class:`ColorManagedViewSettings`, (readonly)

   .. attribute:: views_format

      Format of multiview media

      :type: enum in :ref:`rna_enum_views_format_multiview_items`, default ``'INDIVIDUAL'``

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

   * :class:`CompositorNodeOutputFile.format`
   * :class:`NodeOutputFileSlotFile.format`
   * :class:`BakeSettings.image_settings`
   * :class:`RenderSettings.image_settings`
   * :class:`UILayout.template_image_settings`
   * :class:`UILayout.template_image_views`

