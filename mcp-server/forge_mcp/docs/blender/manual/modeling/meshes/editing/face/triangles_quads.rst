.. _bpy.ops.mesh.tris_convert_to_quads:

******************
Triangles to Quads
******************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Face --> Triangles to Quads`
   :Shortcut:  :kbd:`Alt-J`

This operator converts selected triangles into quads by merging adjacent triangles and removing
the shared edge to form a quad, based on a threshold.

It works with a selection of multiple triangles at once.
This means you can select the entire mesh to convert triangles that already form square shapes into quads,
without worrying about individual faces. Alternatively, manually select pairs of faces to guide the
operator to join them as desired (see hint below for more joining options).

To create a quad, the operator requires at least two adjacent triangles. If you have an even number
of selected triangles, not all triangles may be converted to quads. The operator aims to create the
most even rectangular quads, so some triangles may remain.

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_face_triangles-quads_before.png
          :width: 320px

          Before converting triangles to quads.

     - .. figure:: /images/modeling_meshes_editing_face_triangles-quads_after.png
          :width: 320px

          After converting triangles to quads.

Max Angle
   Controls the threshold for this operator to work on adjacent triangles, with values between 0
   and 180 degrees. At 0.0, only adjacent triangles that form a perfect rectangle are joined
   (i.e. right-angled triangles sharing their hypotenuses). Larger values are required for
   triangles with a shared edge that is small, relative to the size of the other edges of the triangles.
Topology Influence
   Prioritizes edge joins that create quads with geometry that matches existing quads' topology.
   Useful for preserving topology, especially in areas with dense or irregular geometry.

   .. tip::

      For best results, set Topology Influence between 100-130% and Max Angle to 180 degrees.
      Lower values may leave behind parallelograms and triangles, while higher values may cause errors.
Compare UVs
   Prevents the union of triangles that are not also adjacent in the active UV map.
Compare Color Attributes
   Prevents the union of triangles that do not have matching
   :ref:`Color Attributes <modeling-meshes-properties-object_data-color-attributes>`.
Compare Sharp
   Prevents the union of triangles that share an edge marked as sharp.
Compare Materials
   Prevents the union of triangles that do not have the same material assigned.
Deselect Joined
   Deselects the triangles that were successfully merged into quads during the operation.
   Useful for identifying the remaining triangles that still need to be converted.

.. hint::

   When isolated groups of faces are selected, they can be combined
   with :ref:`Create Face <modeling-mesh-make-face-edge-dissolve>` or :ref:`bpy.ops.mesh.dissolve_faces`;
   this is not limited to quads.
