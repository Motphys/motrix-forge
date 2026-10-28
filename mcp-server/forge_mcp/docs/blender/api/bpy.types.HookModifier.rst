HookModifier(Modifier)
======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: HookModifier(Modifier)

   Hook modifier to modify the location of vertices

   .. attribute:: center

      Center of the hook, used for falloff and display

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. data:: falloff_curve

      Custom falloff curve

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: falloff_radius

      If not zero, the distance from the hook where influence ends

      :type: float in [0, inf], default 0.0

   .. attribute:: falloff_type

      :type: enum in [``'NONE'``, ``'CURVE'``, ``'SMOOTH'``, ``'SPHERE'``, ``'ROOT'``, ``'INVERSE_SQUARE'``, ``'SHARP'``, ``'LINEAR'``, ``'CONSTANT'``], default ``'SMOOTH'``

   .. attribute:: invert_vertex_group

      Invert vertex group influence

      :type: boolean, default False

   .. attribute:: matrix_inverse

      Reverse the transformation between this object and its target

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0))

   .. attribute:: object

      Parent Object for hook, also recalculates and clears offset

      :type: :class:`Object`

   .. attribute:: strength

      Relative force of the hook

      :type: float in [0, 1], default 1.0

   .. attribute:: subtarget

      Name of Parent Bone for hook (if applicable), also recalculates and clears offset

      :type: string, default "", (never None)

   .. attribute:: use_falloff_uniform

      Compensate for non-uniform object scale

      :type: boolean, default False

   .. attribute:: vertex_group

      Name of Vertex Group which determines influence of modifier per point

      :type: string, default "", (never None)

   .. data:: vertex_indices

      Indices of vertices bound to the modifier. For Bézier curves, handles count as additional vertices.

      :type: int array of 64 items in [0, inf], default (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (readonly)

   .. method:: vertex_indices_set(indices)

      Validates and assigns the array of vertex indices bound to the modifier

      :arg indices: Vertex Indices
      :type indices: int array of 64 items in [-inf, inf]

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

