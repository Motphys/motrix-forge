.. _bpy.ops.uv.select:

*************
Selecting UVs
*************

Much like the 3D Viewport, the UV Editor has selection mode buttons in the header,
as well as a *Select* menu.


.. _bpy.types.ToolSettings.use_uv_select_sync:

Sync Selection
==============

If turned off (the default), the UV Editor only shows the faces that are selected in the
3D Viewport. Selecting an item in one editor does not automatically select it in the other.
If one 3D vertex/edge corresponds to multiple UV vertices/edges, you can select each
of those individually.

If turned on, the UV Editor always shows all faces. Selecting an item in one editor also
selects it in the other. If one 3D vertex/edge corresponds to multiple UV vertices/edges,
you can't select those individually (you can only select all of them).


.. _bpy.ops.uv.select_mode:
.. _bpy.types.ToolSettings.uv_select_mode:

Selection Mode
==============

:Vertex: :kbd:`1` Select vertices.
:Edge: :kbd:`2` Select edges.
:Face: :kbd:`3` Select faces.

If *Sync Selection* is enabled, you can hold :kbd:`Shift` while clicking a selection mode to
activate multiple ones at the same time, or :kbd:`Ctrl` to expand/contract the selection.

.. seealso::

   :doc:`Mesh Selection </modeling/meshes/selecting/introduction>`


.. _bpy.types.ToolSettings.use_uv_select_island:

UV Island Selection
===================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Header --> UV Island Selection`
   :Shortcut:  :kbd:`4`

Select contiguous groups of faces that are connected in the UV map.
Only available for *Face* select mode or if *Sync Selection* is disabled.


.. _bpy.types.ToolSettings.uv_sticky_select_mode:

Sticky Selection Mode
=====================

Options for automatically selecting additional UV vertices.
Only available for *Face* select mode or if *Sync Selection* is disabled.

Disabled
   Each UV vertex can be selected independently of the others.
Shared Location
   Automatically select UV vertices that correspond to the same mesh vertex and have the same UV coordinates.
   This is the default and gives the illusion that multiple faces in a UV map can share the same vertex;
   in reality, they have separate vertices that overlap.
Shared Vertex
   Automatically select UV vertices that correspond to the same mesh vertex,
   even if they have different UV coordinates.
   This is also the behavior when *Sync Selection* is enabled.


Select Menu
===========

.. _bpy.ops.uv.select_all:

All :kbd:`A`
   Selects all UV elements.
None :kbd:`Alt-A`
   Deselects all UV elements.
Invert :kbd:`Ctrl-I`
   Inverts the current selection.
Box Select :kbd:`B`
   See :ref:`Box Select <bpy.ops.*.select_box>`.
Box Select Pinned :kbd:`Ctrl-B`
   Like *Box Select*, but only selects :ref:`pinned <bpy.ops.uv.pin>` UV vertices.
Circle Select
   See :ref:`Circle Select <bpy.ops.*.select_circle>`.
Lasso Select
   See :ref:`Lasso Select <bpy.ops.*.select_lasso>`.
More/Less :kbd:`Ctrl-NumpadPlus`, :kbd:`Ctrl-NumpadMinus`
   Expands/contracts the selection to/from the adjacent elements.

.. _bpy.ops.uv.select_similar:

Select Similar :kbd:`Shift-G`
   Selects UV elements that are similar to the :term:`active` one in some way.
   The :ref:`bpy.ops.screen.redo_last` panel provides several options:

   Type
      The property to compare. Which properties are available depends on the
      :ref:`Selection Mode <bpy.types.ToolSettings.uv_select_mode>`.

      Vertex Selection Mode
         :Pinned: Selects vertices with the same :ref:`pinned <bpy.ops.uv.pin>` state.

      Edge Selection Mode
         :Length: Selects edges with a similar length in the UV map.
         :Length 3D: Selects edges with a similar length in the 3D mesh.
         :Pinned: Selects edges with the same pinned state.

      Face Selection Mode
         :Area: Selects faces with a similar area in the UV map.
         :Area 3D: Selects faces with a similar area in the 3D mesh.
         :Material: Selects faces that have the same :doc:`Material </render/materials/index>`.
         :Object:
            Selects faces that belong to the same object.
            This is useful when multiple objects are in Edit mode at once.
         :Polygon Sides: Selects faces with a similar number of edges.
         :Winding: Select faces that have the same orientation (facing upwards or downwards in the UV map).

      Island Selection Mode
         :Area: Selects islands with a similar area in the UV map.
         :Area 3D: Selects islands with a similar area in the 3D mesh.
         :Amount of Faces in Island: Selects islands with a similar number of faces.

   Compare
      The comparison operator.

      :Equal: Select elements whose value is equal.
      :Greater: Select elements whose value is greater or equal.
      :Less: Select elements whose value is less or equal.
   Threshold
      Tolerance for values that are almost, but not quite the same. A higher threshold will select more elements.

Select Linked
   Linked :kbd:`Ctrl-L`
      Selects all elements that are connected to the currently selected ones.
   Shortest Path
      Selects the path between two selected elements. (See below)
Select Pinned :kbd:`Shift-P`
   Selects all pinned UVs.
Select Split :kbd:`Y`
   "Detaches" the selected faces so they can be moved elsewhere without affecting their neighbors.

   .. hint::

      Unlike :doc:`Split Selection </modeling/meshes/editing/mesh/split>` for meshes, which physically disconnects
      faces, this is a pure selection operator. In UV space, the faces were never connected to begin with;
      it only seemed that way because *Sticky Selection* automatically selected the vertices of the neighboring faces.
      *Select Split* deselects those vertices again.

      As an alternative to *Select Split*, you can set the *Sticky Selection Mode* to *Disabled*.

Select Overlap
   Selects all UV faces that overlap each other.


.. _bpy.ops.uv.shortest_path_select:
.. _bpy.ops.uv.shortest_path_pick:

Shortest Path
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> Select Linked --> Shortest Path`
   :Shortcut:  :kbd:`Ctrl-LMB`

Selects all the UV elements along the shortest path between two elements: the two selected elements when
activated using the menu, or the active one and the clicked one when activated using the shortcut.

Face Stepping
   For vertices: allows the path to step across faces, following their diagonal rather than
   their edges.

   For edges: selects disconnected edges that are perpendicular to the path (edge ring),
   rather than connected edges along the path (edge loop).

   For faces: allows the path to go through faces that only share a vertex, rather than an edge.
Topology Distance
   Calculates the distance by simply counting edges rather than measuring their lengths.
Fill Region :kbd:`Shift-Ctrl-LMB`
   Selects all shortest paths (rather than just one).
Dashed Line Options
   Allows to only select elements at regular intervals, creating a "dashed line" rather
   than a continuous one.

   Deselected
      The number of deselected elements in the repetitive sequence.
   Selected
      The number of selected elements in the repetitive sequence.
   Offset
      The number of elements to offset the sequence by.

.. seealso::

   Mesh edit :ref:`Select Shortest Path <bpy.ops.mesh.shortest_path_select>`.

.. _bpy.ops.uv.select_edge_loop:

Select Edge Loop
================

.. reference::

   :Mode:      Edit Mode
   :Shortcut:  :kbd:`Alt-LMB`, or :kbd:`Shift-Alt-LMB` for extending the existing selection.

Holding :kbd:`Alt` while clicking an edge selects that edge and then expands the selection as far as
possible in the two directions parallel to it. (While this of course works for selecting edge "loops"
that go all the way around a mesh, it also works if there's no loop.)

You can additionally hold :kbd:`Shift` to extend the current selection rather than replacing it.

.. seealso::

   Mesh edit :ref:`Select Edge Loops <bpy.ops.mesh.loop_select>`.


.. _bpy.ops.uv.select_edge_ring:

Select Edge Ring
================

.. reference::

   :Mode:      Edit Mode
   :Shortcut:  :kbd:`Ctrl-Alt-LMB`, or :kbd:`Shift-Ctrl-Alt-LMB` for extending the existing selection.

Holding :kbd:`Ctrl-Alt` while clicking an edge selects that edge and then expands the selection
as far as possible in the two directions perpendicular to it. (While this of course works for selecting
edge "rings" that go all the way around a mesh, it also works if there's no ring.)

You can additionally hold :kbd:`Shift` to extend the current selection rather than replacing it.

.. seealso::

   Mesh edit :ref:`Select Edge Rings <bpy.ops.mesh.select_edge_ring>`.
