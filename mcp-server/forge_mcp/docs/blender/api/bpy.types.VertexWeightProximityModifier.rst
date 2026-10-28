VertexWeightProximityModifier(Modifier)
=======================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: VertexWeightProximityModifier(Modifier)

   Set the weights of vertices in a group from a target object's distance

   .. attribute:: falloff_type

      How weights are mapped to their new values

      * ``LINEAR``
        Linear -- Null action.
      * ``CURVE``
        Custom Curve.
      * ``SHARP``
        Sharp.
      * ``SMOOTH``
        Smooth.
      * ``ROOT``
        Root.
      * ``ICON_SPHERECURVE``
        Sphere.
      * ``RANDOM``
        Random.
      * ``STEP``
        Median Step -- Map all values below 0.5 to 0.0, and all others to 1.0.

      :type: enum in [``'LINEAR'``, ``'CURVE'``, ``'SHARP'``, ``'SMOOTH'``, ``'ROOT'``, ``'ICON_SPHERECURVE'``, ``'RANDOM'``, ``'STEP'``], default ``'LINEAR'``

   .. attribute:: invert_falloff

      Invert the resulting falloff weight

      :type: boolean, default False

   .. attribute:: invert_mask_vertex_group

      Invert vertex group mask influence

      :type: boolean, default False

   .. data:: map_curve

      Custom mapping curve

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: mask_constant

      Global influence of current modifications on vgroup

      :type: float in [-inf, inf], default 1.0

   .. attribute:: mask_tex_map_bone

      Which bone to take texture coordinates from

      :type: string, default "", (never None)

   .. attribute:: mask_tex_map_object

      Which object to take texture coordinates from

      :type: :class:`Object`

   .. attribute:: mask_tex_mapping

      Which texture coordinates to use for mapping

      * ``LOCAL``
        Local -- Use local generated coordinates.
      * ``GLOBAL``
        Global -- Use global coordinates.
      * ``OBJECT``
        Object -- Use local generated coordinates of another object.
      * ``UV``
        UV -- Use coordinates from a UV layer.

      :type: enum in [``'LOCAL'``, ``'GLOBAL'``, ``'OBJECT'``, ``'UV'``], default ``'LOCAL'``

   .. attribute:: mask_tex_use_channel

      Which texture channel to use for masking

      :type: enum in [``'INT'``, ``'RED'``, ``'GREEN'``, ``'BLUE'``, ``'HUE'``, ``'SAT'``, ``'VAL'``, ``'ALPHA'``], default ``'INT'``

   .. attribute:: mask_tex_uv_layer

      UV map name

      :type: string, default "", (never None)

   .. attribute:: mask_texture

      Masking texture

      :type: :class:`Texture`

   .. attribute:: mask_vertex_group

      Masking vertex group name

      :type: string, default "", (never None)

   .. attribute:: max_dist

      Distance mapping to weight 1.0

      :type: float in [0, inf], default 1.0

   .. attribute:: min_dist

      Distance mapping to weight 0.0

      :type: float in [0, inf], default 0.0

   .. attribute:: normalize

      Normalize the resulting weights (otherwise they are only clamped within 0.0 to 1.0 range)

      :type: boolean, default False

   .. attribute:: proximity_geometry

      Use the shortest computed distance to target object's geometry as weight

      * ``VERTEX``
        Vertex -- Compute distance to nearest vertex.
      * ``EDGE``
        Edge -- Compute distance to nearest edge.
      * ``FACE``
        Face -- Compute distance to nearest face.

      :type: enum set in {``'VERTEX'``, ``'EDGE'``, ``'FACE'``}, default {``'FACE'``}

   .. attribute:: proximity_mode

      Which distances to target object to use

      * ``OBJECT``
        Object -- Use distance between affected and target objects.
      * ``GEOMETRY``
        Geometry -- Use distance between affected object's vertices and target object, or target object's geometry.

      :type: enum in [``'OBJECT'``, ``'GEOMETRY'``], default ``'GEOMETRY'``

   .. attribute:: target

      Object to calculate vertices distances from

      :type: :class:`Object`

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

