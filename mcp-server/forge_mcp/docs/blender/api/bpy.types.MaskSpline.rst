MaskSpline(bpy_struct)
======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaskSpline(bpy_struct)

   Single spline used for defining mask shape

   .. attribute:: offset_mode

      The method used for calculating the feather offset

      * ``EVEN``
        Even -- Calculate even feather offset.
      * ``SMOOTH``
        Smooth -- Calculate feather offset as a second curve.

      :type: enum in [``'EVEN'``, ``'SMOOTH'``], default ``'EVEN'``

   .. data:: points

      Collection of points

      :type: :class:`MaskSplinePoints` :class:`bpy_prop_collection` of :class:`MaskSplinePoint`, (readonly)

   .. attribute:: use_cyclic

      Make this spline a closed loop

      :type: boolean, default False

   .. attribute:: use_fill

      Make this spline filled

      :type: boolean, default False

   .. attribute:: use_self_intersection_check

      Prevent feather from self-intersections

      :type: boolean, default False

   .. attribute:: weight_interpolation

      The type of weight interpolation for spline

      :type: enum in [``'LINEAR'``, ``'EASE'``], default ``'LINEAR'``

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

   * :class:`MaskLayer.splines`
   * :class:`MaskSplines.active`
   * :class:`MaskSplines.new`
   * :class:`MaskSplines.remove`

