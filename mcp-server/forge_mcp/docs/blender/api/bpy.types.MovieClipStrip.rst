MovieClipStrip(Strip)
=====================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Strip`

.. class:: MovieClipStrip(Strip)

   Sequence strip to load a video from the clip editor

   .. attribute:: alpha_mode

      Representation of alpha information in the RGBA pixels

      * ``STRAIGHT``
        Straight -- RGB channels in transparent pixels are unaffected by the alpha channel.
      * ``PREMUL``
        Premultiplied -- RGB channels in transparent pixels are multiplied by the alpha channel.

      :type: enum in [``'STRAIGHT'``, ``'PREMUL'``], default ``'STRAIGHT'``

   .. attribute:: animation_offset_end

      Animation end offset (trim end)

      :type: int in [0, inf], default 0

   .. attribute:: animation_offset_start

      Animation start offset (trim start)

      :type: int in [0, inf], default 0

   .. attribute:: clip

      Movie clip that this sequence uses

      :type: :class:`MovieClip`

   .. attribute:: color_multiply

      :type: float in [0, 20], default 1.0

   .. attribute:: color_saturation

      Adjust the intensity of the input's color

      :type: float in [0, 20], default 1.0

   .. data:: crop

      :type: :class:`StripCrop`, (readonly)

   .. data:: fps

      Frames per second

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. attribute:: multiply_alpha

      Multiply alpha along with color channels

      :type: boolean, default False

   .. attribute:: stabilize2d

      Use the 2D stabilized version of the clip

      :type: boolean, default False

   .. attribute:: strobe

      Only display every nth frame

      :type: float in [1, 30], default 0.0

   .. data:: transform

      :type: :class:`StripTransform`, (readonly)

   .. attribute:: undistort

      Use the undistorted version of the clip

      :type: boolean, default False

   .. attribute:: use_deinterlace

      Remove fields from video movies

      :type: boolean, default False

   .. attribute:: use_flip_x

      Flip on the X axis

      :type: boolean, default False

   .. attribute:: use_flip_y

      Flip on the Y axis

      :type: boolean, default False

   .. attribute:: use_float

      Convert input to float data

      :type: boolean, default False

   .. attribute:: use_reverse_frames

      Reverse frame order

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
   * :class:`Strip.name`
   * :class:`Strip.type`
   * :class:`Strip.select`
   * :class:`Strip.select_left_handle`
   * :class:`Strip.select_right_handle`
   * :class:`Strip.mute`
   * :class:`Strip.lock`
   * :class:`Strip.frame_final_duration`
   * :class:`Strip.frame_duration`
   * :class:`Strip.frame_start`
   * :class:`Strip.frame_final_start`
   * :class:`Strip.frame_final_end`
   * :class:`Strip.frame_offset_start`
   * :class:`Strip.frame_offset_end`
   * :class:`Strip.channel`
   * :class:`Strip.use_linear_modifiers`
   * :class:`Strip.blend_type`
   * :class:`Strip.blend_alpha`
   * :class:`Strip.effect_fader`
   * :class:`Strip.use_default_fade`
   * :class:`Strip.color_tag`
   * :class:`Strip.modifiers`
   * :class:`Strip.show_retiming_keys`

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
   * :class:`Strip.strip_elem_from_frame`
   * :class:`Strip.swap`
   * :class:`Strip.move_to_meta`
   * :class:`Strip.parent_meta`
   * :class:`Strip.invalidate_cache`
   * :class:`Strip.split`
   * :class:`Strip.bl_rna_get_subclass`
   * :class:`Strip.bl_rna_get_subclass_py`

