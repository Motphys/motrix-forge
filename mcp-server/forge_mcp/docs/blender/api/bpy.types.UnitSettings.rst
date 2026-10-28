UnitSettings(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UnitSettings(bpy_struct)


   .. attribute:: length_unit

      Unit that will be used to display length values

      :type: enum in [``'DEFAULT'``], default ``'DEFAULT'``

   .. attribute:: mass_unit

      Unit that will be used to display mass values

      :type: enum in [``'DEFAULT'``], default ``'DEFAULT'``

   .. attribute:: scale_length

      Scale to use when converting between Blender units and dimensions. When working at microscopic or astronomical scale, a small or large unit scale respectively can be used to avoid numerical precision problems

      :type: float in [1e-09, inf], default 0.0

   .. attribute:: system

      The unit system to use for user interface controls

      :type: enum in [``'NONE'``, ``'METRIC'``, ``'IMPERIAL'``], default ``'NONE'``

   .. attribute:: system_rotation

      Unit to use for displaying/editing rotation values

      * ``DEGREES``
        Degrees -- Use degrees for measuring angles and rotations.
      * ``RADIANS``
        Radians.

      :type: enum in [``'DEGREES'``, ``'RADIANS'``], default ``'DEGREES'``

   .. attribute:: temperature_unit

      Unit that will be used to display temperature values

      :type: enum in [``'DEFAULT'``], default ``'DEFAULT'``

   .. attribute:: time_unit

      Unit that will be used to display time values

      :type: enum in [``'DEFAULT'``], default ``'DEFAULT'``

   .. attribute:: use_separate

      Display units in pairs (e.g. 1m 0cm)

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

   * :class:`Scene.unit_settings`

