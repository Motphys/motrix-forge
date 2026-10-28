GreasePencilTextureModifier(Modifier)
=====================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: GreasePencilTextureModifier(Modifier)

   Transform stroke texture coordinates Modifier

   .. attribute:: alignment_rotation

      Additional rotation applied to dots and square strokes

      :type: float in [-1.5708, 1.5708], default 0.0

   .. attribute:: fill_offset

      Additional offset of the fill UV

      :type: :class:`mathutils.Vector` of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: fill_rotation

      Additional rotation of the fill UV

      :type: float in [-inf, inf], default 0.0

   .. attribute:: fill_scale

      Additional scale of the fill UV

      :type: float in [0.01, 100], default 1.0

   .. attribute:: fit_method

      * ``CONSTANT_LENGTH``
        Constant Length -- Keep the texture at a constant length regardless of the length of each stroke.
      * ``FIT_STROKE``
        Stroke Length -- Scale the texture to fit the length of each stroke.

      :type: enum in [``'CONSTANT_LENGTH'``, ``'FIT_STROKE'``], default ``'CONSTANT_LENGTH'``

   .. attribute:: invert_layer_filter

      Invert layer filter

      :type: boolean, default False

   .. attribute:: invert_layer_pass_filter

      Invert layer pass filter

      :type: boolean, default False

   .. attribute:: invert_material_filter

      Invert material filter

      :type: boolean, default False

   .. attribute:: invert_material_pass_filter

      Invert material pass filter

      :type: boolean, default False

   .. attribute:: layer_pass_filter

      Layer pass filter

      :type: int in [0, 100], default 0

   .. attribute:: material_filter

      Material used for filtering

      :type: :class:`Material`

   .. attribute:: material_pass_filter

      Material pass

      :type: int in [0, 100], default 0

   .. attribute:: mode

      * ``STROKE``
        Stroke -- Manipulate only stroke texture coordinates.
      * ``FILL``
        Fill -- Manipulate only fill texture coordinates.
      * ``STROKE_AND_FILL``
        Stroke & Fill -- Manipulate both stroke and fill texture coordinates.

      :type: enum in [``'STROKE'``, ``'FILL'``, ``'STROKE_AND_FILL'``], default ``'STROKE'``

   .. attribute:: open_influence_panel

      :type: boolean, default False

   .. attribute:: tree_node_filter

      Layer name

      :type: string, default "", (never None)

   .. attribute:: use_layer_group_filter

      Filter by layer group name

      :type: boolean, default False

   .. attribute:: use_layer_pass_filter

      Use layer pass filter

      :type: boolean, default False

   .. attribute:: use_material_pass_filter

      Use material pass filter

      :type: boolean, default False

   .. attribute:: uv_offset

      Offset value to add to stroke UVs

      :type: float in [-inf, inf], default 0.0

   .. attribute:: uv_scale

      Factor to scale the UVs

      :type: float in [0, inf], default 1.0

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

