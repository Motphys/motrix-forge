StripModifier(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`BrightContrastModifier`, :class:`ColorBalanceModifier`, :class:`CurvesModifier`, :class:`HueCorrectModifier`, :class:`SequencerTonemapModifierData`, :class:`SoundEqualizerModifier`, :class:`WhiteBalanceModifier`

.. class:: StripModifier(bpy_struct)

   Modifier for sequence strip

   .. attribute:: input_mask_id

      Mask ID used as mask input for the modifier

      :type: :class:`Mask`

   .. attribute:: input_mask_strip

      Strip used as mask input for the modifier

      :type: :class:`Strip`

   .. attribute:: input_mask_type

      Type of input data used for mask

      * ``STRIP``
        Strip -- Use sequencer strip as mask input.
      * ``ID``
        Mask -- Use mask ID as mask input.

      :type: enum in [``'STRIP'``, ``'ID'``], default ``'STRIP'``

   .. attribute:: mask_time

      Time to use for the Mask animation

      * ``RELATIVE``
        Relative -- Mask animation is offset to start of strip.
      * ``ABSOLUTE``
        Absolute -- Mask animation is in sync with scene frame.

      :type: enum in [``'RELATIVE'``, ``'ABSOLUTE'``], default ``'RELATIVE'``

   .. attribute:: mute

      Mute this modifier

      :type: boolean, default False

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: show_expanded

      Mute expanded settings for the modifier

      :type: boolean, default False

   .. data:: type

      :type: enum in :ref:`rna_enum_strip_modifier_type_items`, default ``'BRIGHT_CONTRAST'``, (readonly)

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

   * :class:`Strip.modifiers`
   * :class:`StripModifiers.new`
   * :class:`StripModifiers.remove`

