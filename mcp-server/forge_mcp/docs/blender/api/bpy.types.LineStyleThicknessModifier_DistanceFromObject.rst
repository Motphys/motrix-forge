LineStyleThicknessModifier_DistanceFromObject(LineStyleThicknessModifier)
=========================================================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`LineStyleModifier`, :class:`LineStyleThicknessModifier`

.. class:: LineStyleThicknessModifier_DistanceFromObject(LineStyleThicknessModifier)

   Change line thickness based on the distance from an object

   .. attribute:: blend

      Specify how the modifier value is blended into the base value

      :type: enum in [``'MIX'``, ``'ADD'``, ``'SUBTRACT'``, ``'MULTIPLY'``, ``'DIVIDE'``, ``'DIFFERENCE'``, ``'MINIMUM'``, ``'MAXIMUM'``], default ``'MIX'``

   .. data:: curve

      Curve used for the curve mapping

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: expanded

      True if the modifier tab is expanded

      :type: boolean, default False

   .. attribute:: influence

      Influence factor by which the modifier changes the property

      :type: float in [0, 1], default 0.0

   .. attribute:: invert

      Invert the fade-out direction of the linear mapping

      :type: boolean, default False

   .. attribute:: mapping

      Select the mapping type

      * ``LINEAR``
        Linear -- Use linear mapping.
      * ``CURVE``
        Curve -- Use curve mapping.

      :type: enum in [``'LINEAR'``, ``'CURVE'``], default ``'LINEAR'``

   .. attribute:: range_max

      Upper bound of the input range the mapping is applied

      :type: float in [-inf, inf], default 0.0

   .. attribute:: range_min

      Lower bound of the input range the mapping is applied

      :type: float in [-inf, inf], default 0.0

   .. attribute:: target

      Target object from which the distance is measured

      :type: :class:`Object`

   .. data:: type

      Type of the modifier

      :type: enum in :ref:`rna_enum_linestyle_thickness_modifier_type_items`, default ``'ALONG_STROKE'``, (readonly)

   .. attribute:: use

      Enable or disable this modifier during stroke rendering

      :type: boolean, default False

   .. attribute:: value_max

      Maximum output value of the mapping

      :type: float in [-inf, inf], default 0.0

   .. attribute:: value_min

      Minimum output value of the mapping

      :type: float in [-inf, inf], default 0.0

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
   * :class:`LineStyleThicknessModifier.name`

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
   * :class:`LineStyleModifier.bl_rna_get_subclass`
   * :class:`LineStyleModifier.bl_rna_get_subclass_py`
   * :class:`LineStyleThicknessModifier.bl_rna_get_subclass`
   * :class:`LineStyleThicknessModifier.bl_rna_get_subclass_py`

