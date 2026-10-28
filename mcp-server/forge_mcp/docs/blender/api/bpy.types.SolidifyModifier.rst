SolidifyModifier(Modifier)
==========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: SolidifyModifier(Modifier)

   Create a solid skin, compensating for sharp angles

   .. attribute:: bevel_convex

      Edge bevel weight to be added to outside edges

      :type: float in [-1, 1], default 0.0

   .. attribute:: edge_crease_inner

      Assign a crease to inner edges

      :type: float in [0, 1], default 0.0

   .. attribute:: edge_crease_outer

      Assign a crease to outer edges

      :type: float in [0, 1], default 0.0

   .. attribute:: edge_crease_rim

      Assign a crease to the edges making up the rim

      :type: float in [0, 1], default 0.0

   .. attribute:: invert_vertex_group

      Invert the vertex group influence

      :type: boolean, default False

   .. attribute:: material_offset

      Offset material index of generated faces

      :type: int in [-32768, 32767], default 0

   .. attribute:: material_offset_rim

      Offset material index of generated rim faces

      :type: int in [-32768, 32767], default 0

   .. attribute:: nonmanifold_boundary_mode

      Selects the boundary adjustment algorithm

      * ``NONE``
        None -- No shape correction.
      * ``ROUND``
        Round -- Round open perimeter shape.
      * ``FLAT``
        Flat -- Flat open perimeter shape.

      :type: enum in [``'NONE'``, ``'ROUND'``, ``'FLAT'``], default ``'NONE'``

   .. attribute:: nonmanifold_merge_threshold

      Distance within which degenerated geometry is merged

      :type: float in [0, 1], default 0.0001

   .. attribute:: nonmanifold_thickness_mode

      Selects the used thickness algorithm

      * ``FIXED``
        Fixed -- Most basic thickness calculation.
      * ``EVEN``
        Even -- Even thickness calculation which takes the angle between faces into account.
      * ``CONSTRAINTS``
        Constraints -- Thickness calculation using constraints, most advanced.

      :type: enum in [``'FIXED'``, ``'EVEN'``, ``'CONSTRAINTS'``], default ``'CONSTRAINTS'``

   .. attribute:: offset

      Offset the thickness from the center

      :type: float in [-inf, inf], default -1.0

   .. attribute:: rim_vertex_group

      Vertex group that the generated rim geometry will be weighted to

      :type: string, default "", (never None)

   .. attribute:: shell_vertex_group

      Vertex group that the generated shell geometry will be weighted to

      :type: string, default "", (never None)

   .. attribute:: solidify_mode

      Selects the used algorithm

      * ``EXTRUDE``
        Simple -- Output a solidified version of a mesh by simple extrusion.
      * ``NON_MANIFOLD``
        Complex -- Output a manifold mesh even if the base mesh is non-manifold, where edges have 3 or more connecting faces. This method is slower..

      :type: enum in [``'EXTRUDE'``, ``'NON_MANIFOLD'``], default ``'EXTRUDE'``

   .. attribute:: thickness

      Thickness of the shell

      :type: float in [-inf, inf], default 0.01

   .. attribute:: thickness_clamp

      Offset clamp based on geometry scale

      :type: float in [0, 100], default 0.0

   .. attribute:: thickness_vertex_group

      Thickness factor to use for zero vertex group influence

      :type: float in [0, 1], default 0.0

   .. attribute:: use_even_offset

      Maintain thickness by adjusting for sharp corners (slow, disable when not needed)

      :type: boolean, default False

   .. attribute:: use_flat_faces

      Make faces use the minimal vertex weight assigned to their vertices (ensures new faces remain parallel to their original ones, slow, disable when not needed)

      :type: boolean, default False

   .. attribute:: use_flip_normals

      Invert the face direction

      :type: boolean, default False

   .. attribute:: use_quality_normals

      Calculate normals which result in more even thickness (slow, disable when not needed)

      :type: boolean, default False

   .. attribute:: use_rim

      Create edge loops between the inner and outer surfaces on face edges (slow, disable when not needed)

      :type: boolean, default True

   .. attribute:: use_rim_only

      Only add the rim to the original data

      :type: boolean, default False

   .. attribute:: use_thickness_angle_clamp

      Clamp thickness based on angles

      :type: boolean, default False

   .. attribute:: vertex_group

      Vertex group name

      :type: string, default "", (never None)

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

