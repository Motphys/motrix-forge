StripsTopLevel(bpy_struct)
==========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: StripsTopLevel(bpy_struct)

   Collection of Strips

   .. method:: new_clip(name, clip, channel, frame_start)

      Add a new movie clip strip

      :arg name: Name for the new strip
      :type name: string, (never None)
      :arg clip: Movie clip to add
      :type clip: :class:`MovieClip`, (never None)
      :arg channel: Channel, The channel for the new strip
      :type channel: int in [1, 128]
      :arg frame_start: The start frame for the new strip
      :type frame_start: int in [-1048574, 1048574]
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_mask(name, mask, channel, frame_start)

      Add a new mask strip

      :arg name: Name for the new strip
      :type name: string, (never None)
      :arg mask: Mask to add
      :type mask: :class:`Mask`, (never None)
      :arg channel: Channel, The channel for the new strip
      :type channel: int in [1, 128]
      :arg frame_start: The start frame for the new strip
      :type frame_start: int in [-1048574, 1048574]
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_scene(name, scene, channel, frame_start)

      Add a new scene strip

      :arg name: Name for the new strip
      :type name: string, (never None)
      :arg scene: Scene to add
      :type scene: :class:`Scene`, (never None)
      :arg channel: Channel, The channel for the new strip
      :type channel: int in [1, 128]
      :arg frame_start: The start frame for the new strip
      :type frame_start: int in [-1048574, 1048574]
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_image(name, filepath, channel, frame_start, *, fit_method='ORIGINAL')

      Add a new image strip

      :arg name: Name for the new strip
      :type name: string, (never None)
      :arg filepath: Filepath to image
      :type filepath: string, (never None)
      :arg channel: Channel, The channel for the new strip
      :type channel: int in [1, 128]
      :arg frame_start: The start frame for the new strip
      :type frame_start: int in [-1048574, 1048574]
      :arg fit_method: Image Fit Method

         * ``FIT``
           Scale to Fit -- Scale image so fits in preview.
         * ``FILL``
           Scale to Fill -- Scale image so it fills preview completely.
         * ``STRETCH``
           Stretch to Fill -- Stretch image so it fills preview.
         * ``ORIGINAL``
           Use Original Size -- Don't scale the image.
      :type fit_method: enum in [``'FIT'``, ``'FILL'``, ``'STRETCH'``, ``'ORIGINAL'``], (optional)
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_movie(name, filepath, channel, frame_start, *, fit_method='ORIGINAL')

      Add a new movie strip

      :arg name: Name for the new strip
      :type name: string, (never None)
      :arg filepath: Filepath to movie
      :type filepath: string, (never None)
      :arg channel: Channel, The channel for the new strip
      :type channel: int in [1, 128]
      :arg frame_start: The start frame for the new strip
      :type frame_start: int in [-1048574, 1048574]
      :arg fit_method: Image Fit Method

         * ``FIT``
           Scale to Fit -- Scale image so fits in preview.
         * ``FILL``
           Scale to Fill -- Scale image so it fills preview completely.
         * ``STRETCH``
           Stretch to Fill -- Stretch image so it fills preview.
         * ``ORIGINAL``
           Use Original Size -- Don't scale the image.
      :type fit_method: enum in [``'FIT'``, ``'FILL'``, ``'STRETCH'``, ``'ORIGINAL'``], (optional)
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_sound(name, filepath, channel, frame_start)

      Add a new sound strip

      :arg name: Name for the new strip
      :type name: string, (never None)
      :arg filepath: Filepath to movie
      :type filepath: string, (never None)
      :arg channel: Channel, The channel for the new strip
      :type channel: int in [1, 128]
      :arg frame_start: The start frame for the new strip
      :type frame_start: int in [-1048574, 1048574]
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_meta(name, channel, frame_start)

      Add a new meta strip

      :arg name: Name for the new strip
      :type name: string, (never None)
      :arg channel: Channel, The channel for the new strip
      :type channel: int in [1, 128]
      :arg frame_start: The start frame for the new strip
      :type frame_start: int in [-1048574, 1048574]
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: new_effect(name, type, channel, frame_start, *, frame_end=0, input1=None, input2=None)

      Add a new effect strip

      :arg name: Name for the new strip
      :type name: string, (never None)
      :arg type: Type, type for the new strip

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
      :type type: enum in [``'CROSS'``, ``'ADD'``, ``'SUBTRACT'``, ``'ALPHA_OVER'``, ``'ALPHA_UNDER'``, ``'GAMMA_CROSS'``, ``'MULTIPLY'``, ``'WIPE'``, ``'GLOW'``, ``'TRANSFORM'``, ``'COLOR'``, ``'SPEED'``, ``'MULTICAM'``, ``'ADJUSTMENT'``, ``'GAUSSIAN_BLUR'``, ``'TEXT'``, ``'COLORMIX'``]
      :arg channel: Channel, The channel for the new strip
      :type channel: int in [1, 128]
      :arg frame_start: The start frame for the new strip
      :type frame_start: int in [-inf, inf]
      :arg frame_end: The end frame for the new strip
      :type frame_end: int in [-inf, inf], (optional)
      :arg input1: First input strip for effect
      :type input1: :class:`Strip`, (optional)
      :arg input2: Second input strip for effect
      :type input2: :class:`Strip`, (optional)
      :return: New Strip
      :rtype: :class:`Strip`

   .. method:: remove(sequence)

      Remove a Strip

      :arg sequence: Strip to remove
      :type sequence: :class:`Strip`, (never None)

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

   * :class:`SequenceEditor.sequences`
   * :class:`SequenceEditor.strips`

