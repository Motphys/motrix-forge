
*******************
Select All by Trait
*******************

.. _bpy.ops.mesh.select_non_manifold:

Non-Manifold
============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select All by Trait --> Non-Manifold`

Selects the :term:`Non-manifold` geometry of a mesh.
This entry is available when editing a mesh, in Vertex and Edge selection modes only.

Extend
   Lets you extend the current selection.
Wire
   Selects all the edges that do not belong to any face.
Boundaries
   Selects edges in boundaries and holes.
Multiple Faces
   Selects edges that belong to three or more faces.
Non Contiguous
   Selects edges that belong to exactly two faces with opposite normals.
Vertices
   Selects vertices that belong to *wire* and *multiple face* edges,
   isolated vertices, and vertices that belong to non-adjoining faces.


.. _bpy.ops.mesh.select_loose:

Loose Geometry
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select All by Trait --> Loose Geometry`

This selection depends on the currently selected :ref:`Selection Modes <bpy.types.ToolSettings.mesh_select_mode>`;
In vertex and edge selection mode it selects all vertices or edges that do not form part of a face.
In face selection mode it selects all faces that do not share edges with other faces.


.. _bpy.ops.mesh.select_interior_faces:

Interior Faces
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select All by Trait --> Interior Faces`

Selects faces where all edges have more than two faces.


.. _bpy.ops.mesh.select_face_by_sides:

Faces by Sides
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select All by Trait --> Faces by Sides`

Selects all faces that have a specified number of edges.


.. _bpy.ops.mesh.select_by_pole_count:

Select By Pole Count
====================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select All by Trait --> Select by Pole Count`

This operator selects all elements connected to :term:`Pole` vertices,
based on the number of edges connected to each pole.

- In vertex selection mode, pole vertices are selected.
- In edge selection mode, pole vertices and all their connected edges are selected.
- In face selection mode, pole vertices and all their connected faces are selected.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_select_by_pole_count_before.webp

          Before selecting poles.

     - .. figure:: /images/modeling_meshes_editing_face_select_by_pole_count_after.webp

          After selecting poles.

Pole Count
   Specifies the number of edges a :term:`Pole` must have to be included in the selection.

Type
   Defines the comparison method for selecting poles:

   :Equal: Includes poles with the specified number of edges.
   :Not Equal: Includes poles with a number of edges different from the specified value.
   :Greater Than: Includes poles with more edges than the specified value.
   :Less Than: Includes poles with fewer edges than the specified value.

Extend
   Adds selected poles to the existing selection rather than replacing it.

Exclude Non-manifold
   Skips poles that are part of :term:`Non-manifold` geometry.

.. hint::

   Use this operator to inspect poles, which is particularly useful for identifying problematic poles
   during topology cleanup or for optimizing quad flow.


.. _bpy.ops.mesh.select_ungrouped:

Ungrouped Vertices
==================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select All by Trait --> Ungrouped Vertices`

Selects all vertices which are not part of
a :doc:`vertex group </modeling/meshes/properties/vertex_groups/index>`.
