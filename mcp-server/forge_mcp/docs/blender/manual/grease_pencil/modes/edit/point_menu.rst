
**********
Point Menu
**********

.. _bpy.ops.grease_pencil.extrude_move:

Extrude
=======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Point --> Extrude`
   :Tool:      :menuselection:`Toolbar --> Extrude`
   :Shortcut:  :kbd:`E`

Extrudes points by duplicating the selected points, which then can be moved.
The new points stay connected with the original points of the edit line.

.. note::

   Since Grease Pencil strokes can only have one start an end point,
   a new stroke will be created when extrude intermediate points in the strokes.


.. _bpy.ops.grease_pencil.stroke_smooth:

Smooth
======

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Point --> Smooth`

Softens strokes by reducing the differences in the locations of the points along the line,
while trying to maintain similar values that make the line fluid and smoother.

Iterations
   The number of times to repeat the procedure.
Factor
   The amount of the smoothness to apply.
Smooth Endpoints
   Smooths the stroke's endpoints.
Keep Shape
   Preserves the strokes shape.
Position
   When enabled, the operator affect the points location.
Radius
   When enabled, the operator affect the points thickness.
Opacity
   When enabled, the operator affect the points strength (alpha).


Vertex Groups
=============

Operators for working with vertex groups.


.. _bpy.ops.grease_pencil.set_handle_type:

Set Handle Type
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Point --> Set Handle Type`
   :Shortcut:  :kbd:`V`

Sets the handle type for the points on the Bézier curve that are in the selection.

Type
   The handle type to switch to.

   :Free:
      The handles are independent of each other.
   :Auto:
      This handle has a completely automatic length and direction
      which is set by Blender to ensure the smoothest result.
      These handles convert to *Aligned* handles when moved.
   :Vector:
      Both parts of a handle always point to the previous handle or the next handle which allows
      you to create curves or sections thereof made of straight lines or with sharp corners.
      Vector handles convert to *Free* handles when moved.
   :Aligned:
      These handles always lie in a straight line,
      and give a continuous curve without sharp angles.
