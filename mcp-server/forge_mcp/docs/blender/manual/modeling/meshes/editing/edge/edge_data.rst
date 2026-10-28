
*********
Edge Data
*********

Edges can have several different properties that affect how certain other tools affect the mesh.

.. _bpy.ops.transform.edge_crease:

Edge Crease
===========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Edge Crease`
   :Shortcut:  :kbd:`Shift-E`

This operator interactively sets the :ref:`Edge Crease <modeling-edges-crease-subdivision>` amount
by moving the mouse (or typing a value with the keyboard).
Selecting more than one edge will adjust the mean (average) crease value.
A negative value will subtract from the actual crease value, if present.
To clear the crease edge property, enter a value of -1.


.. _bpy.ops.transform.edge_bevelweight:

Edge Bevel Weight
=================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Edge Bevel Weight`

Sets the value for the ``bevel_weight_edge`` attribute, a value between (0.0 to 1.0).

This attribute is used by the :doc:`Bevel Modifier </modeling/modifiers/generate/bevel>`
to control the bevel intensity of the edges.

This operator enters an interactive mode (a bit like transform tools),
where by moving the mouse (or typing a value with the keyboard)
you can set the bevel weight of selected edges. If more than one edge is selected,
this operator alters the average weight of the edges.

.. seealso::

   :ref:`Vertex Bevel Weight <modeling-vertex-bevel-weight>`


.. _bpy.ops.mesh.mark_seam:

Mark/Clear Seam
===============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Mark/Clear Seam`

These operators set or unset this mark for selected edges.
Seams are a way to create separations, "islands", in UV maps.
See the :ref:`UV Mapping section <editors-uv-index>` for more details.


.. _bpy.ops.mesh.mark_sharp:

Mark/Clear Sharp
================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Mark/Clear Sharp`

Signifies the selected edge(s) as being "sharp".
This edge attribute can either be set (mark) or unset (clear).

This influences the rendering of :ref:`modeling-meshes-structure-normals`
to appear flat if smooth shading is enabled for the connecting face or object.
This attribute can also be used by many modifiers or operators to mask their effect.

Internally, this uses the :ref:`sharp edge attribute <geometry-nodes_builtin-attributes>`.


.. _bpy.ops.mesh.set_sharpness_by_angle:

Set Sharpness by Angle
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Set Sharpness by Angle`

Sets the :ref:`sharp edge attribute <geometry-nodes_builtin-attributes>`
based on the angle between neighboring faces.

Angle
   Maximum angle between face normals that will be considered as smooth.
Extend
   Add new sharp edges without clearing existing sharp edges.


.. _bpy.ops.mesh.mark_freestyle_edge:

Mark/Clear Freestyle Edge
=========================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Edge --> Mark/Clear Freestyle Edge`

Marks or unmarks the selected edges as requiring Freestyle lines.
See :ref:`freestyle-edge-marks`.
