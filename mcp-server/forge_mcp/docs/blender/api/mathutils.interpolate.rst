Interpolation Utilities (mathutils.interpolate)
===============================================

.. module:: mathutils.interpolate

The Blender interpolate module

.. function:: poly_3d_calc(veclist, pt)

   Calculate barycentric weights for a point on a polygon.

   :arg veclist: Sequence of 3D positions.
   :type veclist: Sequence[Sequence[float]]
   :arg pt: 2D or 3D position.   :type pt: Sequence[float]   :return: list of per-vector weights.
   :rtype: list[float]


