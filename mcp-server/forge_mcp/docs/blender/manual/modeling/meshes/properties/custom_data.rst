
*************
Geometry Data
*************

This panel is used to manage any generic data attributes that a mesh could have.

.. warning::

   Clearing any data will result in the data loss of these values.

.. _bpy.ops.mesh.customdata_mask_clear:

Clear Sculpt Mask Data
   Deletes the internal ``sculpt_mask`` attribute.
   This attribute is used by the :ref:`Sculpt Masking Feature <face_sets>`.

.. _bpy.ops.mesh.customdata_skin_clear:
.. _bpy.ops.mesh.customdata_skin_add:

Add/Clear Skin Data
   Used to manage the skin data which is used by the :doc:`/modeling/modifiers/generate/skin`.
   This operator can be needed in case a Skin modifier is created but no skin data exist.

.. _bpy.ops.mesh.customdata_custom_splitnormals_clear:
.. _bpy.ops.mesh.customdata_custom_splitnormals_add:

Add/Clear Custom Split Normals Data
   Adds :ref:`Custom Split Normals <modeling_meshes_normals_custom>` data, if none exists yet.
