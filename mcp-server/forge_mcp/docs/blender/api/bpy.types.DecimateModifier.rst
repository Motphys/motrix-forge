DecimateModifier(Modifier)
==========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: DecimateModifier(Modifier)

   Decimation modifier

   .. attribute:: angle_limit

      Only dissolve angles below this (planar only)

      :type: float in [0, 3.14159], default 0.0872665

   .. attribute:: decimate_type

      * ``COLLAPSE``
        Collapse -- Use edge collapsing.
      * ``UNSUBDIV``
        Un-Subdivide -- Use un-subdivide face reduction.
      * ``DISSOLVE``
        Planar -- Dissolve geometry to form planar polygons.

      :type: enum in [``'COLLAPSE'``, ``'UNSUBDIV'``, ``'DISSOLVE'``], default ``'COLLAPSE'``

   .. attribute:: delimit

      Limit merging geometry

      :type: enum set in :ref:`rna_enum_mesh_delimit_mode_items`, default {``'NORMAL'``}

   .. data:: face_count

      The current number of faces in the decimated mesh

      :type: int in [-inf, inf], default 0, (readonly)

   .. attribute:: invert_vertex_group

      Invert vertex group influence (collapse only)

      :type: boolean, default False

   .. attribute:: iterations

      Number of times reduce the geometry (unsubdivide only)

      :type: int in [0, 32767], default 0

   .. attribute:: ratio

      Ratio of triangles to reduce to (collapse only)

      :type: float in [0, 1], default 1.0

   .. attribute:: symmetry_axis

      Axis of symmetry

      :type: enum in :ref:`rna_enum_axis_xyz_items`, default ``'X'``

   .. attribute:: use_collapse_triangulate

      Keep triangulated faces resulting from decimation (collapse only)

      :type: boolean, default False

   .. attribute:: use_dissolve_boundaries

      Dissolve all vertices in between face boundaries (planar only)

      :type: boolean, default False

   .. attribute:: use_symmetry

      Maintain symmetry on an axis

      :type: boolean, default False

   .. attribute:: vertex_group

      Vertex group name (collapse only)

      :type: string, default "", (never None)

   .. attribute:: vertex_group_factor

      Vertex group strength

      :type: float in [0, 1000], default 1.0

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

