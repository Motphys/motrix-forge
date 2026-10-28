FModifierNoise(FModifier)
=========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`FModifier`

.. class:: FModifierNoise(FModifier)

   Give randomness to the modified F-Curve

   .. attribute:: blend_type

      Method of modifying the existing F-Curve

      :type: enum in [``'REPLACE'``, ``'ADD'``, ``'SUBTRACT'``, ``'MULTIPLY'``], default ``'REPLACE'``

   .. attribute:: depth

      Amount of fine level detail present in the noise

      :type: int in [0, 32767], default 0

   .. attribute:: lacunarity

      Gap between successive frequencies. Depth needs to be greater than 0 for this to have an effect

      :type: float in [-inf, inf], default 2.0

   .. attribute:: offset

      Time offset for the noise effect

      :type: float in [-inf, inf], default 0.0

   .. attribute:: phase

      A random seed for the noise effect

      :type: float in [-inf, inf], default 1.0

   .. attribute:: roughness

      Amount of high frequency detail. Depth needs to be greater than 0 for this to have an effect

      :type: float in [-inf, inf], default 0.5

   .. attribute:: scale

      Scaling (in time) of the noise

      :type: float in [-inf, inf], default 1.0

   .. attribute:: strength

      Amplitude of the noise - the amount that it modifies the underlying curve

      :type: float in [-inf, inf], default 1.0

   .. attribute:: use_legacy_noise

      Use the legacy way of generating noise. Has the issue that it can produce values outside of -1/1

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
   * :class:`FModifier.name`
   * :class:`FModifier.type`
   * :class:`FModifier.show_expanded`
   * :class:`FModifier.mute`
   * :class:`FModifier.is_valid`
   * :class:`FModifier.active`
   * :class:`FModifier.use_restricted_range`
   * :class:`FModifier.frame_start`
   * :class:`FModifier.frame_end`
   * :class:`FModifier.blend_in`
   * :class:`FModifier.blend_out`
   * :class:`FModifier.use_influence`
   * :class:`FModifier.influence`

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
   * :class:`FModifier.bl_rna_get_subclass`
   * :class:`FModifier.bl_rna_get_subclass_py`

