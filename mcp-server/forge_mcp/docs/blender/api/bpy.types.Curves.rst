Curves(ID)
==========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Curves(ID)

   Hair data-block for hair curves

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. data:: attributes

      Geometry attributes

      :type: :class:`AttributeGroupCurves` :class:`bpy_prop_collection` of :class:`Attribute`, (readonly)

   .. data:: color_attributes

      Geometry color attributes

      :type: :class:`AttributeGroupCurves` :class:`bpy_prop_collection` of :class:`Attribute`, (readonly)

   .. data:: curve_offset_data

      :type: :class:`bpy_prop_collection` of :class:`IntAttributeValue`, (readonly)

   .. data:: curves

      All curves in the data-block

      :type: :class:`bpy_prop_collection` of :class:`CurveSlice`, (readonly)

   .. data:: materials

      :type: :class:`IDMaterials` :class:`bpy_prop_collection` of :class:`Material`, (readonly)

   .. data:: normals

      The curve normal value at each of the curve's control points

      :type: :class:`bpy_prop_collection` of :class:`FloatVectorValueReadOnly`, (readonly)

   .. data:: points

      Control points of all curves

      :type: :class:`bpy_prop_collection` of :class:`CurvePoint`, (readonly)

   .. data:: position_data

      :type: :class:`bpy_prop_collection` of :class:`FloatVectorAttributeValue`, (readonly)

   .. attribute:: selection_domain

      :type: enum in :ref:`rna_enum_attribute_curves_domain_items`, default ``'POINT'``

   .. attribute:: surface

      Mesh object that the curves can be attached to

      :type: :class:`Object`

   .. attribute:: surface_collision_distance

      Distance to keep the curves away from the surface

      :type: float in [1.192e-07, inf], default 0.005

   .. attribute:: surface_uv_map

      The name of the attribute on the surface mesh used to define the attachment of each curve

      :type: string, default "", (never None)

   .. attribute:: use_mirror_x

      Enable symmetry in the X axis

      :type: boolean, default False

   .. attribute:: use_mirror_y

      Enable symmetry in the Y axis

      :type: boolean, default False

   .. attribute:: use_mirror_z

      Enable symmetry in the Z axis

      :type: boolean, default False

   .. attribute:: use_sculpt_collision

      Enable collision with the surface while sculpting

      :type: boolean, default False

   .. method:: add_curves(sizes)

      add_curves

      :arg sizes: Sizes, The number of points in each curve
      :type sizes: int array of 1 items in [0, inf]

   .. method:: remove_curves(*, indices=(0,))

      Remove all curves. If indices are provided, remove only the curves with the given indices.

      :arg indices: Indices, The indices of the curves to remove
      :type indices: int array of 1 items in [0, inf], (optional)

   .. method:: resize_curves(sizes, *, indices=(0,))

      Resize all existing curves. If indices are provided, resize only the curves with the given indices. If the new size for a curve is smaller, the curve is trimmed. If the new size for a curve is larger, the new end values are default initialized.

      :arg sizes: Sizes, The number of points in each curve
      :type sizes: int array of 1 items in [1, inf]
      :arg indices: Indices, The indices of the curves to resize
      :type indices: int array of 1 items in [0, inf], (optional)

   .. method:: reorder_curves(new_indices)

      Reorder the curves by the new indices.

      :arg new_indices: New indices, The new index for each of the curves
      :type new_indices: int array of 1 items in [0, inf]

   .. method:: set_types(*, type='CATMULL_ROM', indices=(0,))

      Set the curve type. If indices are provided, set only the types with the given curve indices.

      :arg type: Type
      :type type: enum in :ref:`rna_enum_curves_type_items`, (optional)
      :arg indices: Indices, The indices of the curves to resize
      :type indices: int array of 1 items in [0, inf], (optional)

   .. method:: unit_test_compare(*, curves=None, threshold=7.1526e-06)

      unit_test_compare

      :arg curves: Curves to compare to
      :type curves: :class:`Curves`, (optional)
      :arg threshold: Threshold, Comparison tolerance threshold
      :type threshold: float in [0, inf], (optional)
      :return: Return value, String description of result of comparison
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
   * :class:`ID.name`
   * :class:`ID.name_full`
   * :class:`ID.id_type`
   * :class:`ID.session_uid`
   * :class:`ID.is_evaluated`
   * :class:`ID.original`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.use_extra_user`
   * :class:`ID.is_embedded_data`
   * :class:`ID.is_missing`
   * :class:`ID.is_runtime_data`
   * :class:`ID.is_editable`
   * :class:`ID.tag`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.library_weak_reference`
   * :class:`ID.asset_data`
   * :class:`ID.override_library`
   * :class:`ID.preview`

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
   * :class:`ID.rename`
   * :class:`ID.evaluated_get`
   * :class:`ID.copy`
   * :class:`ID.asset_mark`
   * :class:`ID.asset_clear`
   * :class:`ID.asset_generate_preview`
   * :class:`ID.override_create`
   * :class:`ID.override_hierarchy_create`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`
   * :class:`ID.preview_ensure`
   * :class:`ID.bl_rna_get_subclass`
   * :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   * :class:`BlendData.hair_curves`
   * :class:`BlendDataHairCurves.new`
   * :class:`BlendDataHairCurves.remove`
   * :class:`Curves.unit_test_compare`

