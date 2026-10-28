
********
Segments
********

Subdivide
=========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Segments --> Subdivide`

The *Subdivide* operator divides selected surface segments by adding control points,
effectively increasing the segment resolution.
This is useful for refining shapes, creating smoother transitions, or adding detail to surfaces.

For 2D surface grids, this operation splits selected grids into four smaller grids,
increasing the density of control points. For 1D surfaces (also referred to as "surface curves"),
the operator behaves the same as it does with :ref:`curves <bpy.ops.curve.subdivide>`.

Number of Cuts
   Specifies the number of divisions for each selected segment; each cut adds one new control point per segment.


.. _modeling_surfaces_editing_segments_switch-direction:

Switch Direction
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Segments --> Switch Direction`

The *Switch Direction* operator reverses the direction of the selected surface segments.
The start point of the curve becomes the end point, and vice versa.

Reversing the direction of surface segments flips their "normals". Normals determine the "front" and "back" faces of
the surface and are essential for proper shading, lighting, and rendering.
