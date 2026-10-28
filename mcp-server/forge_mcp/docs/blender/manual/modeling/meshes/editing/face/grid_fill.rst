.. _bpy.ops.mesh.fill_grid:

*********
Grid Fill
*********

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Grid Fill`

*Grid Fill* fills a selected region with a quad grid, using either edge loops or selected faces
as input to determine the boundary.

It supports two main use cases:

- **Edge Loops**: A pair of open edge loops, or a single closed edge loop.
- **Selected Faces**: A connected selection of faces with a clear outer boundary.

The operator attempts to fit a grid of quads within the defined boundary using a predictable and structured pattern.

Span
   Specifies the number of columns in the grid.
Offset
   Defines the vertex that is considered to be the corner of the grid.
   By default, this is the active vertex. Use this to rotate the grid layout.
Simple Blending
   Use a simpler interpolation algorithm for generating grid geometry from boundary loops.
   This method is better suited for flat surfaces or cases where preserving curvature gives undesirable results.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_grid-fill_before.png
          :width: 320px

          Input.

     - .. figure:: /images/modeling_meshes_editing_face_grid-fill_after.png
          :width: 320px

          Grid Fill result.

.. note::

   - If the boundary conditions are not met (e.g., more than one exterior loop or mismatched edge counts),
     the operation will cancel with an error.
   - Selection order and active vertex can influence grid orientation and layout.


Usage
=====

Edge Loop Input
---------------

When using edge loops as input, the most predictable results occur when two opposite loops
have an equal number of vertices. For a single, closed loop, Blender tries to detect two
opposite edges and build a grid accordingly.


Face Input
----------

If a region of faces is selected, Grid Fill replaces the selected faces with a new quad grid.
This works if the selected faces form a continuous region with a clear boundary (i.e., a single exterior loop).

This method preserves UVs and custom data (e.g., face sets, edge creases, and vertex groups) across the new geometry.
UV islands and seams are respected where possible, and data from selected elements will be transferred to the result.
