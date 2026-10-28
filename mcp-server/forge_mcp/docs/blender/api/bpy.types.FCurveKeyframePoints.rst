FCurveKeyframePoints(bpy_struct)
================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FCurveKeyframePoints(bpy_struct)

   Collection of keyframe points

   .. method:: insert(frame, value, *, options={}, keyframe_type='KEYFRAME')

      Add a keyframe point to a F-Curve

      :arg frame: X Value of this keyframe point
      :type frame: float in [-inf, inf]
      :arg value: Y Value of this keyframe point
      :type value: float in [-inf, inf]
      :arg options: Keyframe options

         * ``REPLACE``
           Replace -- Don't add any new keyframes, but just replace existing ones.
         * ``NEEDED``
           Needed -- Only adds keyframes that are needed.
         * ``FAST``
           Fast -- Fast keyframe insertion to avoid recalculating the curve each time.
      :type options: enum set in {``'REPLACE'``, ``'NEEDED'``, ``'FAST'``}, (optional)
      :arg keyframe_type: Type of keyframe to insert
      :type keyframe_type: enum in :ref:`rna_enum_beztriple_keyframe_type_items`, (optional)
      :return: Newly created keyframe
      :rtype: :class:`Keyframe`

   .. method:: add(count)

      Add a keyframe point to a F-Curve

      :arg count: Number, Number of points to add to the spline
      :type count: int in [0, inf]

   .. method:: remove(keyframe, *, fast=False)

      Remove keyframe from an F-Curve

      :arg keyframe: Keyframe to remove
      :type keyframe: :class:`Keyframe`, (never None)
      :arg fast: Fast, Fast keyframe removal to avoid recalculating the curve each time
      :type fast: boolean, (optional)

   .. method:: clear()

      Remove all keyframes from an F-Curve


   .. method:: sort()

      Ensure all keyframe points are chronologically sorted


   .. method:: deduplicate()

      Ensure there are no duplicate keys. Assumes that the points have already been sorted


   .. method:: handles_recalc()

      Update handles after modifications to the keyframe points, to update things like auto-clamping


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

   * :class:`FCurve.keyframe_points`

