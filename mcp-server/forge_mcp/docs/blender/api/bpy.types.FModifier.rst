FModifier(bpy_struct)
=====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`FModifierCycles`, :class:`FModifierEnvelope`, :class:`FModifierFunctionGenerator`, :class:`FModifierGenerator`, :class:`FModifierLimits`, :class:`FModifierNoise`, :class:`FModifierStepped`

.. class:: FModifier(bpy_struct)

   Modifier for values of F-Curve

   .. attribute:: active

      F-Curve modifier will show settings in the editor

      :type: boolean, default False

   .. attribute:: blend_in

      Number of frames from start frame for influence to take effect

      :type: float in [-inf, inf], default 0.0

   .. attribute:: blend_out

      Number of frames from end frame for influence to fade out

      :type: float in [-inf, inf], default 0.0

   .. attribute:: frame_end

      Frame that modifier's influence ends (if Restrict Frame Range is in use)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: frame_start

      Frame that modifier's influence starts (if Restrict Frame Range is in use)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: influence

      Amount of influence F-Curve Modifier will have when not fading in/out

      :type: float in [0, 1], default 1.0

   .. data:: is_valid

      F-Curve Modifier has invalid settings and will not be evaluated

      :type: boolean, default False, (readonly)

   .. attribute:: mute

      Enable F-Curve modifier evaluation

      :type: boolean, default False

   .. attribute:: name

      F-Curve Modifier name

      :type: string, default "", (never None)

   .. attribute:: show_expanded

      F-Curve Modifier's panel is expanded in UI

      :type: boolean, default False

   .. data:: type

      F-Curve Modifier Type

      :type: enum in :ref:`rna_enum_fmodifier_type_items`, default ``'NULL'``, (readonly)

   .. attribute:: use_influence

      F-Curve Modifier's effects will be tempered by a default factor

      :type: boolean, default False

   .. attribute:: use_restricted_range

      F-Curve Modifier is only applied for the specified frame range to help mask off effects in order to chain them

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

   * :class:`FCurve.modifiers`
   * :class:`FCurveModifiers.active`
   * :class:`FCurveModifiers.new`
   * :class:`FCurveModifiers.remove`
   * :class:`NlaStrip.modifiers`

