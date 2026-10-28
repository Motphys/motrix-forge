
*******
Extrude
*******

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Extrude`
   :Shortcut:  :kbd:`Alt-E`

This operators shown in this menu are dependent of what part of a mesh is currently selected.
Many of the operators are also available in the :doc:`Vertex </modeling/meshes/editing/vertex/index>`,
:doc:`Edge </modeling/meshes/editing/edge/index>`, and :doc:`Face </modeling/meshes/editing/face/index>` menus.


Extrude Faces
=============

Available when a :term:`Face` is selected.

See :ref:`bpy.ops.view3d.edit_mesh_extrude_move_normal`.


Extrude Faces Along Normals
===========================

Available when a :term:`Face` is selected.

See :ref:`bpy.ops.view3d.edit_mesh_extrude_move_shrink_fatten`.


Extrude Individual Faces
========================

Available when a :term:`Face` is selected.

See :ref:`tool-mesh-extrude_individual`.


Extrude Manifold
================

Available when a :term:`Face` is selected.

See :doc:`/modeling/meshes/tools/extrude_manifold`.


Extrude Edges
=============

Available when a :term:`Edge` is selected.

See :ref:`bpy.ops.mesh.extrude_edges_move`.


Extrude Vertices
================

Available when a :term:`Vertex` is selected.

See :ref:`bpy.ops.mesh.extrude_vertices_move`.


.. _bpy.ops.mesh.extrude_repeat:

Extrude Repeat
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Extrude --> Extrude Repeat`

This tool behaves similar to the :doc:`/modeling/modifiers/generate/array`,
by extruding the selection along the Z axis of the view.
If the selection is not :term:`Manifold` it's extruded the specified number of times.

Offset X, Y, Z
   Distance between the instances.
Steps
   Number of instances.
Scale Offset
   Multiplication factor to increase or decrease the offset.


Spin
====

See :doc:`/modeling/meshes/tools/spin`.
