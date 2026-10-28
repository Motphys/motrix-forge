GPencilSculptSettings(bpy_struct)
=================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilSculptSettings(bpy_struct)

   General properties for Grease Pencil stroke sculpting tools

   .. data:: guide

      :type: :class:`GPencilSculptGuide`, (readonly)

   .. attribute:: intersection_threshold

      Threshold for stroke intersections

      :type: float in [0, 10], default 0.1

   .. attribute:: lock_axis

      * ``VIEW``
        View -- Align strokes to current view plane.
      * ``AXIS_Y``
        Front (X-Z) -- Project strokes to plane locked to Y.
      * ``AXIS_X``
        Side (Y-Z) -- Project strokes to plane locked to X.
      * ``AXIS_Z``
        Top (X-Y) -- Project strokes to plane locked to Z.
      * ``CURSOR``
        Cursor -- Align strokes to current 3D cursor orientation.

      :type: enum in [``'VIEW'``, ``'AXIS_Y'``, ``'AXIS_X'``, ``'AXIS_Z'``, ``'CURSOR'``], default ``'VIEW'``

   .. data:: multiframe_falloff_curve

      Custom curve to control falloff of brush effect by Grease Pencil frames

      :type: :class:`CurveMapping`, (readonly)

   .. data:: thickness_primitive_curve

      Custom curve to control primitive thickness

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: use_automasking_layer_active

      Affect only the Active Layer

      :type: boolean, default False

   .. attribute:: use_automasking_layer_stroke

      Affect only strokes below the cursor

      :type: boolean, default False

   .. attribute:: use_automasking_material_active

      Affect only the Active Material

      :type: boolean, default False

   .. attribute:: use_automasking_material_stroke

      Affect only strokes below the cursor

      :type: boolean, default False

   .. attribute:: use_automasking_stroke

      Affect only strokes below the cursor

      :type: boolean, default False

   .. attribute:: use_multiframe_falloff

      Use falloff effect when edit in multiframe mode to compute brush effect by frame

      :type: boolean, default False

   .. attribute:: use_scale_thickness

      Scale the stroke thickness when transforming strokes

      :type: boolean, default False

   .. attribute:: use_thickness_curve

      Use curve to define primitive stroke thickness

      :type: boolean, default False

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

References
----------

.. hlist::
   :columns: 2

   * :class:`ToolSettings.gpencil_sculpt`

