RegionView3D(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RegionView3D(bpy_struct)

   3D View region data

   .. attribute:: clip_planes

      :type: float multi-dimensional array of 6 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: is_orthographic_side_view

      Whether the current view is aligned to an axis (does not check whether the view is orthographic, use "is_perspective" for that). Setting this will rotate the view to the closest axis

      :type: boolean, default False

   .. attribute:: is_perspective

      :type: boolean, default False

   .. attribute:: lock_rotation

      Lock view rotation of side views to Top/Front/Right

      :type: boolean, default False

   .. data:: perspective_matrix

      Current perspective matrix (``window_matrix * view_matrix``)

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), (readonly)

   .. attribute:: show_sync_view

      Sync view position between side views

      :type: boolean, default False

   .. attribute:: use_box_clip

      Clip view contents based on what is visible in other side views

      :type: boolean, default False

   .. attribute:: use_clip_planes

      :type: boolean, default False

   .. attribute:: view_camera_offset

      View shift in camera view

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: view_camera_zoom

      Zoom factor in camera view

      :type: float in [-30, 600], default 0.0

   .. attribute:: view_distance

      Distance to the view location

      :type: float in [0, inf], default 0.0

   .. attribute:: view_location

      View pivot location

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: view_matrix

      Current view matrix

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: view_perspective

      View Perspective

      :type: enum in [``'PERSP'``, ``'ORTHO'``, ``'CAMERA'``], default ``'ORTHO'``

   .. attribute:: view_rotation

      Rotation in quaternions (keep normalized)

      :type: :class:`mathutils.Quaternion` rotation of 4 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0)

   .. data:: window_matrix

      Current window matrix

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), (readonly)

   .. method:: update()

      Recalculate the view matrices


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

   * :class:`Context.region_data`
   * :class:`SpaceView3D.region_3d`
   * :class:`SpaceView3D.region_quadviews`

