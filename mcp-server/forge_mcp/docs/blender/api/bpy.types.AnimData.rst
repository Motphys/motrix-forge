AnimData(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AnimData(bpy_struct)

   Animation data for data-block

   .. attribute:: action

      Active Action for this data-block

      :type: :class:`Action`

   .. attribute:: action_blend_type

      Method used for combining Active Action's result with result of NLA stack

      * ``REPLACE``
        Replace -- The strip values replace the accumulated results by amount specified by influence.
      * ``COMBINE``
        Combine -- The strip values are combined with accumulated results by appropriately using addition, multiplication, or quaternion math, based on channel type.
      * ``ADD``
        Add -- Weighted result of strip is added to the accumulated results.
      * ``SUBTRACT``
        Subtract -- Weighted result of strip is removed from the accumulated results.
      * ``MULTIPLY``
        Multiply -- Weighted result of strip is multiplied with the accumulated results.

      :type: enum in [``'REPLACE'``, ``'COMBINE'``, ``'ADD'``, ``'SUBTRACT'``, ``'MULTIPLY'``], default ``'REPLACE'``

   .. attribute:: action_extrapolation

      Action to take for gaps past the Active Action's range (when evaluating with NLA)

      * ``NOTHING``
        Nothing -- Strip has no influence past its extents.
      * ``HOLD``
        Hold -- Hold the first frame if no previous strips in track, and always hold last frame.
      * ``HOLD_FORWARD``
        Hold Forward -- Only hold last frame.

      :type: enum in [``'NOTHING'``, ``'HOLD'``, ``'HOLD_FORWARD'``], default ``'HOLD'``

   .. attribute:: action_influence

      Amount the Active Action contributes to the result of the NLA stack

      :type: float in [0, 1], default 1.0

   .. attribute:: action_slot

      The slot identifies which sub-set of the Action is considered to be for this data-block, and its name is used to find the right slot when assigning an Action

      :type: :class:`ActionSlot`

   .. attribute:: action_slot_handle

      A number that identifies which sub-set of the Action is considered to be for this data-block

      :type: int in [-inf, inf], default 0

   .. attribute:: action_slot_handle_tweak_storage

      Storage to temporarily hold the main action slot while in tweak mode

      :type: int in [-inf, inf], default 0

   .. data:: action_suitable_slots

      The list of slots in this animation data-block

      :type: :class:`bpy_prop_collection` of :class:`ActionSlot`, (readonly)

   .. attribute:: action_tweak_storage

      Storage to temporarily hold the main action while in tweak mode

      :type: :class:`Action`

   .. data:: drivers

      The Drivers/Expressions for this data-block

      :type: :class:`AnimDataDrivers` :class:`bpy_prop_collection` of :class:`FCurve`, (readonly)

   .. attribute:: last_slot_identifier

      The identifier of the most recently assigned action slot. The slot identifies which sub-set of the Action is considered to be for this data-block, and its identifier is used to find the right slot when assigning an Action.

      :type: string, default "", (never None)

   .. data:: nla_tracks

      NLA Tracks (i.e. Animation Layers)

      :type: :class:`NlaTracks` :class:`bpy_prop_collection` of :class:`NlaTrack`, (readonly)

   .. attribute:: use_nla

      NLA stack is evaluated when evaluating this block

      :type: boolean, default False

   .. attribute:: use_pin

      :type: boolean, default False

   .. attribute:: use_tweak_mode

      Whether to enable or disable tweak mode in NLA

      :type: boolean, default False

   .. method:: nla_tweak_strip_time_to_scene(frame, *, invert=False)

      Convert a time value from the local time of the tweaked strip to scene time, exactly as done by built-in key editing tools. Returns the input time unchanged if not tweaking.

      :arg frame: Input time
      :type frame: float in [-1.04857e+06, 1.04857e+06]
      :arg invert: Invert, Convert scene time to action time
      :type invert: boolean, (optional)
      :return: Converted time
      :rtype: float in [-1.04857e+06, 1.04857e+06]

   .. method:: fix_paths_rename_all(*, prefix="", old_name="", new_name="")

      Rename the property paths in the animation system, since properties are animated via string paths, it's needed to keep them valid after properties has been renamed

      :arg prefix: Prefix, Name prefix
      :type prefix: string, (optional, never None)
      :arg old_name: Old Name, Old name
      :type old_name: string, (optional, never None)
      :arg new_name: New Name, New name
      :type new_name: string, (optional, never None)

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

   * :class:`Armature.animation_data`
   * :class:`CacheFile.animation_data`
   * :class:`Camera.animation_data`
   * :class:`Curve.animation_data`
   * :class:`Curves.animation_data`
   * :class:`FreestyleLineStyle.animation_data`
   * :class:`GreasePencil.animation_data`
   * :class:`GreasePencilv3.animation_data`
   * :class:`ID.animation_data_create`
   * :class:`Key.animation_data`
   * :class:`Lattice.animation_data`
   * :class:`Light.animation_data`
   * :class:`LightProbe.animation_data`
   * :class:`Mask.animation_data`
   * :class:`Material.animation_data`
   * :class:`Mesh.animation_data`
   * :class:`MetaBall.animation_data`
   * :class:`MovieClip.animation_data`
   * :class:`NodeTree.animation_data`
   * :class:`Object.animation_data`
   * :class:`ParticleSettings.animation_data`
   * :class:`PointCloud.animation_data`
   * :class:`Scene.animation_data`
   * :class:`Speaker.animation_data`
   * :class:`Texture.animation_data`
   * :class:`Volume.animation_data`
   * :class:`World.animation_data`

