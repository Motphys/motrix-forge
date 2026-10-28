MovieTrackingMarkers(bpy_struct)
================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingMarkers(bpy_struct)

   Collection of markers for movie tracking track

   .. method:: find_frame(frame, *, exact=True)

      Get marker for specified frame

      :arg frame: Frame, Frame number to find marker for
      :type frame: int in [0, 1048574]
      :arg exact: Exact, Get marker at exact frame number rather than get estimated marker
      :type exact: boolean, (optional)
      :return: Marker for specified frame
      :rtype: :class:`MovieTrackingMarker`

   .. method:: insert_frame(frame, *, co=(0.0, 0.0))

      Insert a new marker at the specified frame

      :arg frame: Frame, Frame number to insert marker to
      :type frame: int in [0, 1048574]
      :arg co: Coordinate, Place new marker at the given frame using specified in normalized space coordinates
      :type co: :class:`mathutils.Vector` of 2 items in [-1, 1], (optional)
      :return: Newly created marker
      :rtype: :class:`MovieTrackingMarker`

   .. method:: delete_frame(frame)

      Delete marker at specified frame

      :arg frame: Frame, Frame number to delete marker from
      :type frame: int in [0, 1048574]

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

   * :class:`MovieTrackingTrack.markers`

