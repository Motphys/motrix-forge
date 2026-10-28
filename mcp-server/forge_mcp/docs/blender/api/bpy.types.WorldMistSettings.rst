WorldMistSettings(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: WorldMistSettings(bpy_struct)

   Mist settings for a World data-block

   .. attribute:: depth

      Distance over which the mist effect fades in

      :type: float in [0, inf], default 25.0

   .. attribute:: falloff

      Type of transition used to fade mist

      * ``QUADRATIC``
        Quadratic -- Use quadratic progression.
      * ``LINEAR``
        Linear -- Use linear progression.
      * ``INVERSE_QUADRATIC``
        Inverse Quadratic -- Use inverse quadratic progression.

      :type: enum in [``'QUADRATIC'``, ``'LINEAR'``, ``'INVERSE_QUADRATIC'``], default ``'QUADRATIC'``

   .. attribute:: height

      Control how much mist density decreases with height

      :type: float in [0, 100], default 0.0

   .. attribute:: intensity

      Overall minimum intensity of the mist effect

      :type: float in [0, 1], default 0.0

   .. attribute:: start

      Starting distance of the mist, measured from the camera

      :type: float in [0, inf], default 5.0

   .. attribute:: use_mist

      Occlude objects with the environment color as they are further away

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

   * :class:`World.mist_settings`

