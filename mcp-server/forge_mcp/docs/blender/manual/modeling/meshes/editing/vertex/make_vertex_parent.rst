.. _bpy.ops.object.vertex_parent_set:

******************
Make Vertex Parent
******************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Vertex --> Make Vertex Parent`
   :Shortcut:  :kbd:`Ctrl-P`

Creates a parent-child relationship between the active object and selected vertex or triangle from the edited mesh.

This operator is used to make the active object follow a vertex (or triangle of vertices) on the edited mesh,
so that when the vertex moves, the child object follows.
This is particularly useful for attaching objects to deforming geometry,
such as having an accessory follow a character mesh during animation.


Usage
=====

#. Shift-select the object to be parented (the child object).
#. Select the parent mesh object and enter *Edit Mode*.
#. Select **one or three** vertices that will define the parent relationship.
#. Press :kbd:`Ctrl-P`


Notes
=====

- Parenting to one vertex tracks only the vertex's position.
- Parenting to three vertices allows the child to follow both position and rotation, based on the triangle's surface.
- The child object remains in Object Mode while the mesh stays in Edit Mode.
- Only one child object can be parented at a time using this method.

.. seealso::

   - :doc:`/scene_layout/object/editing/parent` -- Parenting overview.
   - :ref:`bpy.ops.object.parent_set` -- General object parenting.
