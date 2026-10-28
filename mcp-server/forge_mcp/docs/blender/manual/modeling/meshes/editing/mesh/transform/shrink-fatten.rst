.. _bpy.ops.transform.shrink_fatten:
.. _tool-mesh-shrink-fatten:

*************
Shrink/Fatten
*************

.. reference::

   :Mode:      Edit Mode
   :Tool:      :menuselection:`Toolbar --> Shrink/Fatten`
   :Menu:      :menuselection:`Mesh --> Transform --> Shrink/Fatten`
   :Shortcut:  :kbd:`Alt-S`

Moves the selected vertices "inwards" or "outwards" along their normal,
all by the same distance. You can control this distance by moving the mouse up or down,
typing a number, or using the slider in the :ref:`bpy.ops.screen.redo_last` panel.

Even Thickness :kbd:`S`, :kbd:`Alt`
   Applies a larger offset to vertices that are part of a sharp corner, for a more uniform result.
   You can toggle this option by pressing :kbd:`S`, holding :kbd:`Alt`, or clicking the
   checkbox in the Adjust Last Operation panel.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_transform_shrink-fatten_before.png
          :width: 200px

          Mesh before shrink/fatten.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_shrink-fatten_inflate-positive.png
          :width: 200px

          Inflated using a positive value.

     - .. figure:: /images/modeling_meshes_editing_mesh_transform_shrink-fatten_inflate-negative.png
          :width: 200px

          Shrunk using a negative value.
