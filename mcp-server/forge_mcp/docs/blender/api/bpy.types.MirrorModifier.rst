MirrorModifier(Modifier)
========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: MirrorModifier(Modifier)

   Mirroring modifier

   .. attribute:: bisect_threshold

      Distance from the bisect plane within which vertices are removed

      :type: float in [0, inf], default 0.001

   .. attribute:: merge_threshold

      Distance within which mirrored vertices are merged

      :type: float in [0, inf], default 0.001

   .. attribute:: mirror_object

      Object to use as mirror

      :type: :class:`Object`

   .. attribute:: mirror_offset_u

      Amount to offset mirrored UVs flipping point from the 0.5 on the U axis

      :type: float in [-1, 1], default 0.0

   .. attribute:: mirror_offset_v

      Amount to offset mirrored UVs flipping point from the 0.5 point on the V axis

      :type: float in [-1, 1], default 0.0

   .. attribute:: offset_u

      Mirrored UV offset on the U axis

      :type: float in [-10000, 10000], default 0.0

   .. attribute:: offset_v

      Mirrored UV offset on the V axis

      :type: float in [-10000, 10000], default 0.0

   .. attribute:: use_axis

      Enable axis mirror

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: use_bisect_axis

      Cuts the mesh across the mirror plane

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: use_bisect_flip_axis

      Flips the direction of the slice

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: use_clip

      Prevent vertices from going through the mirror during transform

      :type: boolean, default False

   .. attribute:: use_mirror_merge

      Merge vertices within the merge threshold

      :type: boolean, default True

   .. attribute:: use_mirror_u

      Mirror the U texture coordinate around the flip offset point

      :type: boolean, default False

   .. attribute:: use_mirror_udim

      Mirror the texture coordinate around each tile center

      :type: boolean, default False

   .. attribute:: use_mirror_v

      Mirror the V texture coordinate around the flip offset point

      :type: boolean, default False

   .. attribute:: use_mirror_vertex_groups

      Mirror vertex groups (e.g. .R->.L)

      :type: boolean, default True

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
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.is_active`
   * :class:`Modifier.use_pin_to_last`
   * :class:`Modifier.is_override_data`
   * :class:`Modifier.use_apply_on_spline`
   * :class:`Modifier.execution_time`
   * :class:`Modifier.persistent_uid`

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
   * :class:`Modifier.bl_rna_get_subclass`
   * :class:`Modifier.bl_rna_get_subclass_py`

