Strip(bpy_struct)
=================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`EffectStrip`, :class:`ImageStrip`, :class:`MaskStrip`, :class:`MetaStrip`, :class:`MovieClipStrip`, :class:`MovieStrip`, :class:`SceneStrip`, :class:`SoundStrip`

.. class:: Strip(bpy_struct)

   Sequence strip in the sequence editor

   .. attribute:: blend_alpha

      Percentage of how much the strip's colors affect other strips

      :type: float in [0, 1], default 1.0

   .. attribute:: blend_type

      Method for controlling how the strip combines with other strips

      :type: enum in [``'REPLACE'``, ``'CROSS'``, ``'DARKEN'``, ``'MULTIPLY'``, ``'BURN'``, ``'LINEAR_BURN'``, ``'LIGHTEN'``, ``'SCREEN'``, ``'DODGE'``, ``'ADD'``, ``'OVERLAY'``, ``'SOFT_LIGHT'``, ``'HARD_LIGHT'``, ``'VIVID_LIGHT'``, ``'LINEAR_LIGHT'``, ``'PIN_LIGHT'``, ``'DIFFERENCE'``, ``'EXCLUSION'``, ``'SUBTRACT'``, ``'HUE'``, ``'SATURATION'``, ``'COLOR'``, ``'VALUE'``, ``'ALPHA_OVER'``, ``'ALPHA_UNDER'``, ``'GAMMA_CROSS'``], default ``'ALPHA_OVER'``

   .. attribute:: channel

      Y position of the sequence strip

      :type: int in [1, 128], default 0

   .. attribute:: color_tag

      Color tag for a strip

      :type: enum in :ref:`rna_enum_strip_color_items`, default ``'COLOR_01'``

   .. attribute:: effect_fader

      Custom fade value

      :type: float in [0, 1], default 0.0

   .. data:: frame_duration

      The length of the contents of this strip before the handles are applied

      :type: int in [1, 1048574], default 0, (readonly)

   .. attribute:: frame_final_duration

      The length of the contents of this strip after the handles are applied

      :type: int in [1, 1048574], default 0

   .. attribute:: frame_final_end

      End frame displayed in the sequence editor after offsets are applied

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_final_start

      Start frame displayed in the sequence editor after offsets are applied, setting this is equivalent to moving the handle, not the actual start frame

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_offset_end

      :type: float in [-inf, inf], default 0.0

   .. attribute:: frame_offset_start

      :type: float in [-inf, inf], default 0.0

   .. attribute:: frame_start

      X position where the strip begins

      :type: float in [-inf, inf], default 0.0

   .. attribute:: lock

      Lock strip so that it cannot be transformed

      :type: boolean, default False

   .. data:: modifiers

      Modifiers affecting this strip

      :type: :class:`StripModifiers` :class:`bpy_prop_collection` of :class:`StripModifier`, (readonly)

   .. attribute:: mute

      Disable strip so that it cannot be viewed in the output

      :type: boolean, default False

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: select

      :type: boolean, default False

   .. attribute:: select_left_handle

      :type: boolean, default False

   .. attribute:: select_right_handle

      :type: boolean, default False

   .. attribute:: show_retiming_keys

      Show retiming keys, so they can be moved

      :type: boolean, default False

   .. data:: type

      :type: enum in [``'IMAGE'``, ``'META'``, ``'SCENE'``, ``'MOVIE'``, ``'MOVIECLIP'``, ``'MASK'``, ``'SOUND'``, ``'CROSS'``, ``'ADD'``, ``'SUBTRACT'``, ``'ALPHA_OVER'``, ``'ALPHA_UNDER'``, ``'GAMMA_CROSS'``, ``'MULTIPLY'``, ``'WIPE'``, ``'GLOW'``, ``'TRANSFORM'``, ``'COLOR'``, ``'SPEED'``, ``'MULTICAM'``, ``'ADJUSTMENT'``, ``'GAUSSIAN_BLUR'``, ``'TEXT'``, ``'COLORMIX'``], default ``'IMAGE'``, (readonly)

   .. attribute:: use_default_fade

      Fade effect using the built-in default (usually makes the transition as long as the effect strip)

      :type: boolean, default False

   .. attribute:: use_linear_modifiers

      Calculate modifiers in linear space instead of sequencer's space

      :type: boolean, default False

   .. method:: strip_elem_from_frame(frame)

      Return the strip element from a given frame or None

      :arg frame: Frame, The frame to get the strip element from
      :type frame: int in [-1048574, 1048574]
      :return: strip element of the current frame
      :rtype: :class:`StripElement`

   .. method:: swap(other)

      swap

      :arg other: Other
      :type other: :class:`Strip`, (never None)

   .. method:: move_to_meta(meta_sequence)

      move_to_meta

      :arg meta_sequence: Destination Meta Strip, Meta to move the strip into
      :type meta_sequence: :class:`Strip`, (never None)

   .. method:: parent_meta()

      Parent meta

      :return: Parent Meta
      :rtype: :class:`Strip`

   .. method:: invalidate_cache(type)

      Invalidate cached images for strip and all dependent strips

      :arg type: Type, Cache Type
      :type type: enum in [``'RAW'``, ``'COMPOSITE'``], (never None)

   .. method:: split(frame, split_method, *, ignore_connections=False)

      Split Strip

      :arg frame: Frame where to split the strip
      :type frame: int in [-inf, inf]
      :type split_method: enum in [``'SOFT'``, ``'HARD'``], (never None)
      :arg ignore_connections: Don't propagate split to connected strips
      :type ignore_connections: boolean, (optional)
      :return: Right side Strip
      :rtype: :class:`Strip`

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

   * :mod:`bpy.context.active_sequence_strip`
   * :mod:`bpy.context.active_strip`
   * :mod:`bpy.context.selected_editable_sequences`
   * :mod:`bpy.context.selected_editable_strips`
   * :mod:`bpy.context.selected_sequences`
   * :mod:`bpy.context.selected_strips`
   * :mod:`bpy.context.sequences`
   * :mod:`bpy.context.strips`
   * :class:`AddStrip.input_1`
   * :class:`AddStrip.input_2`
   * :class:`AlphaOverStrip.input_1`
   * :class:`AlphaOverStrip.input_2`
   * :class:`AlphaUnderStrip.input_1`
   * :class:`AlphaUnderStrip.input_2`
   * :class:`ColorMixStrip.input_1`
   * :class:`ColorMixStrip.input_2`
   * :class:`CrossStrip.input_1`
   * :class:`CrossStrip.input_2`
   * :class:`GammaCrossStrip.input_1`
   * :class:`GammaCrossStrip.input_2`
   * :class:`GaussianBlurStrip.input_1`
   * :class:`GlowStrip.input_1`
   * :class:`MetaStrip.sequences`
   * :class:`MetaStrip.strips`
   * :class:`MultiplyStrip.input_1`
   * :class:`MultiplyStrip.input_2`
   * :class:`SequenceEditor.active_strip`
   * :class:`SequenceEditor.display_stack`
   * :class:`SequenceEditor.meta_stack`
   * :class:`SequenceEditor.sequences`
   * :class:`SequenceEditor.sequences_all`
   * :class:`SequenceEditor.strips`
   * :class:`SequenceEditor.strips_all`
   * :class:`SpeedControlStrip.input_1`
   * :class:`Strip.move_to_meta`
   * :class:`Strip.parent_meta`
   * :class:`Strip.split`
   * :class:`Strip.swap`
   * :class:`StripModifier.input_mask_strip`
   * :class:`StripsMeta.new_clip`
   * :class:`StripsMeta.new_effect`
   * :class:`StripsMeta.new_effect`
   * :class:`StripsMeta.new_effect`
   * :class:`StripsMeta.new_image`
   * :class:`StripsMeta.new_mask`
   * :class:`StripsMeta.new_meta`
   * :class:`StripsMeta.new_movie`
   * :class:`StripsMeta.new_scene`
   * :class:`StripsMeta.new_sound`
   * :class:`StripsMeta.remove`
   * :class:`StripsTopLevel.new_clip`
   * :class:`StripsTopLevel.new_effect`
   * :class:`StripsTopLevel.new_effect`
   * :class:`StripsTopLevel.new_effect`
   * :class:`StripsTopLevel.new_image`
   * :class:`StripsTopLevel.new_mask`
   * :class:`StripsTopLevel.new_meta`
   * :class:`StripsTopLevel.new_movie`
   * :class:`StripsTopLevel.new_scene`
   * :class:`StripsTopLevel.new_sound`
   * :class:`StripsTopLevel.remove`
   * :class:`SubtractStrip.input_1`
   * :class:`SubtractStrip.input_2`
   * :class:`TransformStrip.input_1`
   * :class:`WipeStrip.input_1`
   * :class:`WipeStrip.input_2`

