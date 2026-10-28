RenderSettings(bpy_struct)
==========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RenderSettings(bpy_struct)

   Rendering settings for a Scene data-block

   .. data:: bake

      :type: :class:`BakeSettings`, (readonly, never None)

   .. attribute:: bake_bias

      Bias towards faces further away from the object (in Blender units)

      :type: float in [0, 1000], default 0.001

   .. attribute:: bake_margin

      Extends the baked result as a post process filter

      :type: int in [0, 64], default 16

   .. attribute:: bake_margin_type

      Algorithm to generate the margin

      * ``ADJACENT_FACES``
        Adjacent Faces -- Use pixels from adjacent faces across UV seams.
      * ``EXTEND``
        Extend -- Extend border pixels outwards.

      :type: enum in [``'ADJACENT_FACES'``, ``'EXTEND'``], default ``'ADJACENT_FACES'``

   .. attribute:: bake_samples

      Number of samples used for ambient occlusion baking from multires

      :type: int in [64, 1024], default 256

   .. attribute:: bake_type

      Choose shading information to bake into the image

      * ``NORMALS``
        Normals -- Bake normals.
      * ``DISPLACEMENT``
        Displacement -- Bake displacement.

      :type: enum in [``'NORMALS'``, ``'DISPLACEMENT'``], default ``'NORMALS'``

   .. attribute:: bake_user_scale

      Instead of automatically normalizing to the range 0 to 1, apply a user scale to the derivative map

      :type: float in [0, 1000], default 0.0

   .. attribute:: border_max_x

      Maximum X value for the render region

      :type: float in [0, 1], default 1.0

   .. attribute:: border_max_y

      Maximum Y value for the render region

      :type: float in [0, 1], default 1.0

   .. attribute:: border_min_x

      Minimum X value for the render region

      :type: float in [0, 1], default 0.0

   .. attribute:: border_min_y

      Minimum Y value for the render region

      :type: float in [0, 1], default 0.0

   .. attribute:: compositor_denoise_device

      The device to use to process the denoise nodes in the compositor

      * ``AUTO``
        Auto -- Use the same device used by the compositor to process the denoise node.
      * ``CPU``
        CPU -- Use the CPU to process the denoise node.
      * ``GPU``
        GPU -- Use the GPU to process the denoise node if available, otherwise fallback to CPU.

      :type: enum in [``'AUTO'``, ``'CPU'``, ``'GPU'``], default ``'AUTO'``

   .. attribute:: compositor_denoise_final_quality

      The quality used by denoise nodes during the compositing of final renders if the nodes' quality option is set to Follow Scene

      * ``HIGH``
        High -- High quality.
      * ``BALANCED``
        Balanced -- Balanced between performance and quality.
      * ``FAST``
        Fast -- High perfomance.

      :type: enum in [``'HIGH'``, ``'BALANCED'``, ``'FAST'``], default ``'HIGH'``

   .. attribute:: compositor_denoise_preview_quality

      The quality used by denoise nodes during viewport and interactive compositing if the nodes' quality option is set to Follow Scene

      * ``HIGH``
        High -- High quality.
      * ``BALANCED``
        Balanced -- Balanced between performance and quality.
      * ``FAST``
        Fast -- High perfomance.

      :type: enum in [``'HIGH'``, ``'BALANCED'``, ``'FAST'``], default ``'BALANCED'``

   .. attribute:: compositor_device

      Set how compositing is executed

      :type: enum in [``'CPU'``, ``'GPU'``], default ``'CPU'``

   .. attribute:: compositor_precision

      The precision of compositor intermediate result

      * ``AUTO``
        Auto -- Full precision for final renders, half precision otherwise.
      * ``FULL``
        Full -- Full precision.

      :type: enum in [``'AUTO'``, ``'FULL'``], default ``'AUTO'``

   .. attribute:: dither_intensity

      Amount of dithering noise added to the rendered image to break up banding

      :type: float in [0, inf], default 1.0

   .. attribute:: engine

      Engine to use for rendering

      :type: enum in [``'BLENDER_EEVEE_NEXT'``], default ``'BLENDER_EEVEE_NEXT'``

   .. data:: ffmpeg

      FFmpeg related settings for the scene

      :type: :class:`FFmpegSettings`, (readonly)

   .. data:: file_extension

      The file extension used for saving renders

      :type: string, default "", (readonly, never None)

   .. attribute:: filepath

      Directory/name to save animations, # characters define the position and padding of frame numbers

      :type: string, default "", (never None, blend relative ``//`` prefix supported, Supports `template expressions <https://docs.blender.org/manual/en/4.5/files/file_paths.html#path-templates>`_)

   .. attribute:: film_transparent

      World background is transparent, for compositing the render over another background

      :type: boolean, default False

   .. attribute:: filter_size

      Width over which the reconstruction filter combines samples

      :type: float in [0, 500], default 1.5

   .. attribute:: fps

      Framerate, expressed in frames per second

      :type: int in [1, 32767], default 24

   .. attribute:: fps_base

      Framerate base

      :type: float in [1e-05, 1e+06], default 1.0

   .. attribute:: frame_map_new

      How many frames the Map Old will last

      :type: int in [1, 900], default 100

   .. attribute:: frame_map_old

      Old mapping value in frames

      :type: int in [1, 900], default 100

   .. attribute:: hair_subdiv

      Additional subdivision along the curves

      :type: int in [0, 3], default 0

   .. attribute:: hair_type

      Curves shape type

      :type: enum in [``'STRAND'``, ``'STRIP'``], default ``'STRAND'``

   .. data:: has_multiple_engines

      More than one rendering engine is available

      :type: boolean, default False, (readonly)

   .. data:: image_settings

      :type: :class:`ImageFormatSettings`, (readonly, never None)

   .. data:: is_movie_format

      When true the format is a movie

      :type: boolean, default False, (readonly)

   .. attribute:: line_thickness

      Line thickness in pixels

      :type: float in [0, 10000], default 1.0

   .. attribute:: line_thickness_mode

      Line thickness mode for Freestyle line drawing

      * ``ABSOLUTE``
        Absolute -- Specify unit line thickness in pixels.
      * ``RELATIVE``
        Relative -- Unit line thickness is scaled by the proportion of the present vertical image resolution to 480 pixels.

      :type: enum in [``'ABSOLUTE'``, ``'RELATIVE'``], default ``'ABSOLUTE'``

   .. attribute:: metadata_input

      Where to take the metadata from

      * ``SCENE``
        Scene -- Use metadata from the current scene.
      * ``STRIPS``
        Sequencer Strips -- Use metadata from the strips in the sequencer.

      :type: enum in [``'SCENE'``, ``'STRIPS'``], default ``'SCENE'``

   .. attribute:: motion_blur_position

      Offset for the shutter's time interval, allows to change the motion blur trails

      * ``START``
        Start on Frame -- The shutter opens at the current frame.
      * ``CENTER``
        Center on Frame -- The shutter is open during the current frame.
      * ``END``
        End on Frame -- The shutter closes at the current frame.

      :type: enum in [``'START'``, ``'CENTER'``, ``'END'``], default ``'CENTER'``

   .. attribute:: motion_blur_shutter

      Time taken in frames between shutter open and close

      :type: float in [0, inf], default 0.5

   .. data:: motion_blur_shutter_curve

      Curve defining the shutter's openness over time

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: pixel_aspect_x

      Horizontal aspect ratio - for anamorphic or non-square pixel output

      :type: float in [1, 200], default 1.0

   .. attribute:: pixel_aspect_y

      Vertical aspect ratio - for anamorphic or non-square pixel output

      :type: float in [1, 200], default 1.0

   .. attribute:: ppm_base

      The base unit for pixels per meter.

      :type: float in [1e-05, 1e+06], default 0.0254

   .. attribute:: ppm_factor

      The pixel density meta-data written to supported image formats. This value is multiplied by the PPM-base which defines the unit (typically inches or meters)

      :type: float in [1e-05, 1e+06], default 72.0

   .. attribute:: preview_pixel_size

      Pixel size for viewport rendering

      * ``AUTO``
        Automatic -- Automatic pixel size, depends on the user interface scale.
      * ``1``
        1× -- Render at full resolution.
      * ``2``
        2× -- Render at 50% resolution.
      * ``4``
        4× -- Render at 25% resolution.
      * ``8``
        8× -- Render at 12.5% resolution.

      :type: enum in [``'AUTO'``, ``'1'``, ``'2'``, ``'4'``, ``'8'``], default ``'AUTO'``

   .. attribute:: resolution_percentage

      Percentage scale for render resolution

      :type: int in [1, 32767], default 100

   .. attribute:: resolution_x

      Number of horizontal pixels in the rendered image

      :type: int in [4, 65536], default 1920

   .. attribute:: resolution_y

      Number of vertical pixels in the rendered image

      :type: int in [4, 65536], default 1080

   .. attribute:: sequencer_gl_preview

      Display method used in the sequencer view

      :type: enum in :ref:`rna_enum_shading_type_items`, default ``'SOLID'``

   .. attribute:: simplify_child_particles

      Global child particles percentage

      :type: float in [0, 1], default 1.0

   .. attribute:: simplify_child_particles_render

      Global child particles percentage during rendering

      :type: float in [0, 1], default 0.0

   .. attribute:: simplify_gpencil

      Simplify Grease Pencil drawing

      :type: boolean, default False

   .. attribute:: simplify_gpencil_antialiasing

      Use Antialiasing to smooth stroke edges

      :type: boolean, default True

   .. attribute:: simplify_gpencil_modifier

      Display modifiers

      :type: boolean, default True

   .. attribute:: simplify_gpencil_onplay

      Simplify Grease Pencil only during animation playback

      :type: boolean, default False

   .. attribute:: simplify_gpencil_shader_fx

      Display Shader Effects

      :type: boolean, default True

   .. attribute:: simplify_gpencil_tint

      Display layer tint

      :type: boolean, default True

   .. attribute:: simplify_gpencil_view_fill

      Display fill strokes in the viewport

      :type: boolean, default True

   .. attribute:: simplify_subdivision

      Global maximum subdivision level

      :type: int in [0, 32767], default 6

   .. attribute:: simplify_subdivision_render

      Global maximum subdivision level during rendering

      :type: int in [0, 32767], default 0

   .. attribute:: simplify_volumes

      Resolution percentage of volume objects in viewport

      :type: float in [0, 1], default 1.0

   .. attribute:: stamp_background

      Color to use behind stamp text

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.25)

   .. attribute:: stamp_font_size

      Size of the font used when rendering stamp text

      :type: int in [8, 64], default 12

   .. attribute:: stamp_foreground

      Color to use for stamp text

      :type: float array of 4 items in [0, 1], default (0.8, 0.8, 0.8, 1.0)

   .. attribute:: stamp_note_text

      Custom text to appear in the stamp note

      :type: string, default "", (never None)

   .. data:: stereo_views

      :type: :class:`bpy_prop_collection` of :class:`SceneRenderView`, (readonly)

   .. attribute:: threads

      Maximum number of CPU cores to use simultaneously while rendering (for multi-core/CPU systems)

      :type: int in [1, 1024], default 1

   .. attribute:: threads_mode

      Determine the amount of render threads used

      * ``AUTO``
        Auto-Detect -- Automatically determine the number of threads, based on CPUs.
      * ``FIXED``
        Fixed -- Manually determine the number of threads.

      :type: enum in [``'AUTO'``, ``'FIXED'``], default ``'AUTO'``

   .. attribute:: use_bake_clear

      Clear Images before baking

      :type: boolean, default True

   .. attribute:: use_bake_lores_mesh

      Calculate heights against unsubdivided low resolution mesh

      :type: boolean, default False

   .. attribute:: use_bake_multires

      Bake directly from multires object

      :type: boolean, default False

   .. attribute:: use_bake_selected_to_active

      Bake shading on the surface of selected objects to the active object

      :type: boolean, default False

   .. attribute:: use_bake_user_scale

      Use a user scale for the derivative map

      :type: boolean, default False

   .. attribute:: use_border

      Render a user-defined render region, within the frame size

      :type: boolean, default False

   .. attribute:: use_compositing

      Process the render result through the compositing pipeline, if compositing nodes are enabled

      :type: boolean, default True

   .. attribute:: use_crop_to_border

      Crop the rendered frame to the defined render region size

      :type: boolean, default False

   .. attribute:: use_file_extension

      Add the file format extensions to the rendered file name (eg: filename + .jpg)

      :type: boolean, default True

   .. attribute:: use_freestyle

      Draw stylized strokes using Freestyle

      :type: boolean, default False

   .. attribute:: use_high_quality_normals

      Use high quality tangent space at the cost of lower performance

      :type: boolean, default False

   .. attribute:: use_lock_interface

      Lock interface during rendering in favor of giving more memory to the renderer

      :type: boolean, default False

   .. attribute:: use_motion_blur

      Use multi-sampled 3D scene motion blur

      :type: boolean, default False

   .. attribute:: use_multiview

      Use multiple views in the scene

      :type: boolean, default False

   .. attribute:: use_overwrite

      Overwrite existing files while rendering

      :type: boolean, default True

   .. attribute:: use_persistent_data

      Keep render data around for faster re-renders and animation renders, at the cost of increased memory usage

      :type: boolean, default False

   .. attribute:: use_placeholder

      Create empty placeholder files while rendering frames (similar to Unix 'touch')

      :type: boolean, default False

   .. attribute:: use_render_cache

      Save render cache to EXR files (useful for heavy compositing, Note: affects indirectly rendered scenes)

      :type: boolean, default False

   .. attribute:: use_sequencer

      Process the render (and composited) result through the video sequence editor pipeline, if sequencer strips exist

      :type: boolean, default True

   .. attribute:: use_sequencer_override_scene_strip

      Use workbench render settings from the sequencer scene, instead of each individual scene used in the strip

      :type: boolean, default False

   .. attribute:: use_simplify

      Enable simplification of scene for quicker preview renders

      :type: boolean, default False

   .. attribute:: use_simplify_normals

      Skip computing custom normals and face corner normals for displaying meshes in the viewport

      :type: boolean, default False

   .. attribute:: use_single_layer

      Only render the active layer. Only affects rendering from the interface, ignored for rendering from command line.

      :type: boolean, default False

   .. data:: use_spherical_stereo

      Active render engine supports spherical stereo rendering

      :type: boolean, default False, (readonly)

   .. attribute:: use_stamp

      Render the stamp info text in the rendered image

      :type: boolean, default False

   .. attribute:: use_stamp_camera

      Include the name of the active camera in image metadata

      :type: boolean, default True

   .. attribute:: use_stamp_date

      Include the current date in image/video metadata

      :type: boolean, default True

   .. attribute:: use_stamp_filename

      Include the .blend filename in image/video metadata

      :type: boolean, default True

   .. attribute:: use_stamp_frame

      Include the frame number in image metadata

      :type: boolean, default True

   .. attribute:: use_stamp_frame_range

      Include the rendered frame range in image/video metadata

      :type: boolean, default False

   .. attribute:: use_stamp_hostname

      Include the hostname of the machine that rendered the frame

      :type: boolean, default False

   .. attribute:: use_stamp_labels

      Display stamp labels ("Camera" in front of camera name, etc.)

      :type: boolean, default True

   .. attribute:: use_stamp_lens

      Include the active camera's lens in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_marker

      Include the name of the last marker in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_memory

      Include the peak memory usage in image metadata

      :type: boolean, default True

   .. attribute:: use_stamp_note

      Include a custom note in image/video metadata

      :type: boolean, default False

   .. attribute:: use_stamp_render_time

      Include the render time in image metadata

      :type: boolean, default True

   .. attribute:: use_stamp_scene

      Include the name of the active scene in image/video metadata

      :type: boolean, default True

   .. attribute:: use_stamp_sequencer_strip

      Include the name of the foreground sequence strip in image metadata

      :type: boolean, default False

   .. attribute:: use_stamp_time

      Include the rendered frame timecode as HH:MM:SS.FF in image metadata

      :type: boolean, default True

   .. data:: views

      :type: :class:`RenderViews` :class:`bpy_prop_collection` of :class:`SceneRenderView`, (readonly)

   .. attribute:: views_format

      * ``STEREO_3D``
        Stereo 3D -- Single stereo camera system, adjust the stereo settings in the camera panel.
      * ``MULTIVIEW``
        Multi-View -- Multi camera system, adjust the cameras individually.

      :type: enum in [``'STEREO_3D'``, ``'MULTIVIEW'``], default ``'STEREO_3D'``

   .. method:: frame_path(*, frame=-2147483648, preview=False, view="")

      Return the absolute path to the filename to be written for a given frame

      :arg frame: Frame number to use, if unset the current frame will be used
      :type frame: int in [-inf, inf], (optional)
      :arg preview: Preview, Use preview range
      :type preview: boolean, (optional)
      :arg view: View, The name of the view to use to replace the "%" chars
      :type view: string, (optional, never None)
      :return: File Path, The resulting filepath from the scenes render settings
      :rtype: string, (never None)

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

   * :class:`RenderEngine.render`
   * :class:`Scene.render`

