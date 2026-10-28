
*********
Face Data
*********

.. _bpy.ops.mesh.colors_rotate:

Rotate Colors
=============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Rotate Colors`

Rotates the Color Attribute's colors inside faces either clockwise or counterclockwise.


.. _bpy.ops.mesh.colors_reverse:

Reverse Colors
==============

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Reverse Colors`

Flips the direction of Color Attribute's colors inside the selected faces.


Rotate UVs
==========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Rotate UVs`

See :ref:`bpy.ops.mesh.uvs_rotate`.


Reverse UVs
===========

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Reverse UVs`

See :ref:`bpy.ops.mesh.uvs_reverse`.


.. _bpy.ops.mesh.flip_quad_tessellation:

Flip Quad Tessellation
======================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Flip Quad Tessellation`

Internally, all :term:`quads <Quad>` are :term:`Tessellated <Tessellation>` into 2 triangles,
this operator swaps which way the quad is split into triangles.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_flip-tesselation_before.png
     - .. figure:: /images/modeling_meshes_editing_face_flip-tesselation_after.png


.. _bpy.ops.mesh.mark_freestyle_face:

Mark/Clear Freestyle Face
=========================

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Face Data --> Mark/Clear Freestyle Face`

Marks or unmarks the selected faces as requiring special Freestyle behavior.
See :ref:`freestyle-face-marks`.
