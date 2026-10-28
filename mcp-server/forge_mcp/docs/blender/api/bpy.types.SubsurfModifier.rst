SubsurfModifier(Modifier)
=========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: SubsurfModifier(Modifier)

   Subdivision surface modifier

   .. attribute:: boundary_smooth

      Controls how open boundaries are smoothed

      :type: enum in :ref:`rna_enum_subdivision_boundary_smooth_items`, default ``'ALL'``

   .. attribute:: levels

      Number of subdivisions to perform in the 3D viewport

      :type: int in [0, 11], default 1

   .. attribute:: open_adaptive_subdivision_panel

      :type: boolean, default False

   .. attribute:: open_advanced_panel

      :type: boolean, default False

   .. attribute:: quality

      Accuracy of vertex positions, lower value is faster but less precise

      :type: int in [1, 10], default 3

   .. attribute:: render_levels

      Number of subdivisions to perform when rendering

      :type: int in [0, 11], default 2

   .. attribute:: show_only_control_edges

      Skip displaying interior subdivided edges

      :type: boolean, default True

   .. attribute:: subdivision_type

      Select type of subdivision algorithm

      * ``CATMULL_CLARK``
        Catmull-Clark -- Create a smooth curved surface using the Catmull-Clark subdivision scheme.
      * ``SIMPLE``
        Simple -- Subdivide faces without changing shape.

      :type: enum in [``'CATMULL_CLARK'``, ``'SIMPLE'``], default ``'CATMULL_CLARK'``

   .. attribute:: use_creases

      Use mesh crease information to sharpen edges or corners

      :type: boolean, default True

   .. attribute:: use_custom_normals

      Interpolates existing custom normals to resulting mesh

      :type: boolean, default False

   .. attribute:: use_limit_surface

      Place vertices at the surface that would be produced with infinite levels of subdivision (smoothest possible shape)

      :type: boolean, default True

   .. attribute:: uv_smooth

      Controls how smoothing is applied to UVs

      :type: enum in :ref:`rna_enum_subdivision_uv_smooth_items`, default ``'PRESERVE_BOUNDARIES'``

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct` subclass


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.is_active`
   * :class:`Modifier.use_pin_to_last`
   * :class:`Modifier.is_override_data`
   * :class:`Modifier.use_apply_on_spline`
   * :class:`Modifier.execution_time`
   * :class:`Modifier.persistent_uid`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.id_properties_clear`
   * :class:`bpy_struct.id_properties_ensure`
   * :class:`bpy_struct.id_properties_ui`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_overridable_library`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.pop`
   * :class:`bpy_struct.property_overridable_library_set`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.rna_ancestors`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`
   * :class:`Modifier.bl_rna_get_subclass`
   * :class:`Modifier.bl_rna_get_subclass_py`

