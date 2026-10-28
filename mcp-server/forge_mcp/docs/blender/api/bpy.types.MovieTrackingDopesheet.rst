MovieTrackingDopesheet(bpy_struct)
==================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieTrackingDopesheet(bpy_struct)

   Match-moving dopesheet data

   .. attribute:: show_hidden

      Include channels from objects/bone that are not visible

      :type: boolean, default False

   .. attribute:: show_only_selected

      Only include channels relating to selected objects and data

      :type: boolean, default False

   .. attribute:: sort_method

      Method to be used to sort channels in dopesheet view

      * ``NAME``
        Name -- Sort channels by their names.
      * ``LONGEST``
        Longest -- Sort channels by longest tracked segment.
      * ``TOTAL``
        Total -- Sort channels by overall amount of tracked segments.
      * ``AVERAGE_ERROR``
        Average Error -- Sort channels by average reprojection error of tracks after solve.
      * ``START``
        Start Frame -- Sort channels by first frame number.
      * ``END``
        End Frame -- Sort channels by last frame number.

      :type: enum in [``'NAME'``, ``'LONGEST'``, ``'TOTAL'``, ``'AVERAGE_ERROR'``, ``'START'``, ``'END'``], default ``'NAME'``

   .. attribute:: use_invert_sort

      Invert sort order of dopesheet channels

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

   * :class:`MovieTracking.dopesheet`

