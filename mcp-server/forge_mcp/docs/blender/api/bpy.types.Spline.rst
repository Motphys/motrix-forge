Spline(bpy_struct)
==================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Spline(bpy_struct)

   Element of a curve, either NURBS, Bézier or Polyline or a character with text objects

   .. data:: bezier_points

      Collection of points for Bézier curves only

      :type: :class:`SplineBezierPoints` :class:`bpy_prop_collection` of :class:`BezierSplinePoint`, (readonly)

   .. data:: character_index

      Location of this character in the text data (only for text curves)

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: hide

      Hide this curve in Edit mode

      :type: boolean, default False

   .. attribute:: material_index

      Material slot index of this curve

      :type: int in [0, 32767], default 0

   .. attribute:: order_u

      NURBS order in the U direction. Higher values make each point influence a greater area, but have worse performance.

      :type: int in [2, 64], default 0

   .. attribute:: order_v

      NURBS order in the V direction. Higher values make each point influence a greater area, but have worse performance.

      :type: int in [2, 64], default 0

   .. data:: point_count_u

      Total number points for the curve or surface in the U direction

      :type: int in [0, inf], default 0, (readonly)

   .. data:: point_count_v

      Total number points for the surface on the V direction

      :type: int in [0, inf], default 0, (readonly)

   .. data:: points

      Collection of points that make up this poly or nurbs spline

      :type: :class:`SplinePoints` :class:`bpy_prop_collection` of :class:`SplinePoint`, (readonly)

   .. attribute:: radius_interpolation

      The type of radius interpolation for Bézier curves

      :type: enum in [``'LINEAR'``, ``'CARDINAL'``, ``'BSPLINE'``, ``'EASE'``], default ``'LINEAR'``

   .. attribute:: resolution_u

      Curve or Surface subdivisions per segment

      :type: int in [1, 1024], default 0

   .. attribute:: resolution_v

      Surface subdivisions per segment

      :type: int in [1, 1024], default 0

   .. attribute:: tilt_interpolation

      The type of tilt interpolation for 3D, Bézier curves

      :type: enum in [``'LINEAR'``, ``'CARDINAL'``, ``'BSPLINE'``, ``'EASE'``], default ``'LINEAR'``

   .. attribute:: type

      The interpolation type for this curve element

      :type: enum in [``'POLY'``, ``'BEZIER'``, ``'NURBS'``], default ``'POLY'``

   .. attribute:: use_bezier_u

      Make this nurbs curve or surface act like a Bézier spline in the U direction

      :type: boolean, default False

   .. attribute:: use_bezier_v

      Make this nurbs surface act like a Bézier spline in the V direction

      :type: boolean, default False

   .. attribute:: use_cyclic_u

      Make this curve or surface a closed loop in the U direction

      :type: boolean, default False

   .. attribute:: use_cyclic_v

      Make this surface a closed loop in the V direction

      :type: boolean, default False

   .. attribute:: use_endpoint_u

      Make this nurbs curve or surface meet the endpoints in the U direction

      :type: boolean, default False

   .. attribute:: use_endpoint_v

      Make this nurbs surface meet the endpoints in the V direction

      :type: boolean, default False

   .. attribute:: use_smooth

      Smooth the normals of the surface or beveled curve

      :type: boolean, default False

   .. method:: calc_length(*, resolution=0)

      Calculate spline length

      :arg resolution: Resolution, Spline resolution to be used, 0 defaults to the resolution_u
      :type resolution: int in [0, 1024], (optional)
      :return: Length, Length of the polygonaly approximated spline
      :rtype: float in [0, inf]

   .. method:: valid_message(direction)

      Return the message

      :arg direction: Direction, The direction where 0-1 maps to U-V
      :type direction: int in [0, 1]
      :return: Return value, The message or an empty string when there is no error
      :rtype: string

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

   * :class:`Curve.splines`
   * :class:`CurveSplines.active`
   * :class:`CurveSplines.new`
   * :class:`CurveSplines.remove`

