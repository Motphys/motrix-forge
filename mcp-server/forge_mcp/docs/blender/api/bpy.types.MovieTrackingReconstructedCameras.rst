MovieTrackingReconstructedCameras(bpy_struct)
=============================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingReconstructedCameras(bpy_struct)

   Collection of solved cameras

   .. method:: find_frame(*, frame=1)

      Find a reconstructed camera for a give frame number

      :arg frame: Frame, Frame number to find camera for
      :type frame: int in [0, 1048574], (optional)
      :return: Camera for a given frame
      :rtype: :class:`MovieReconstructedCamera`

   .. method:: matrix_from_frame(*, frame=1)

      Return interpolated camera matrix for a given frame

      :arg frame: Frame, Frame number to find camera for
      :type frame: int in [0, 1048574], (optional)
      :return: Matrix, Interpolated camera matrix for a given frame
      :rtype: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf]

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

   * :class:`MovieTrackingReconstruction.cameras`

