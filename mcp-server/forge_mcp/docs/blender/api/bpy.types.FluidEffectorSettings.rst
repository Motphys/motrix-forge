FluidEffectorSettings(bpy_struct)
=================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FluidEffectorSettings(bpy_struct)

   Smoke collision settings

   .. attribute:: effector_type

      Change type of effector in the simulation

      * ``COLLISION``
        Collision -- Create collision object.
      * ``GUIDE``
        Guide -- Create guide object.

      :type: enum in [``'COLLISION'``, ``'GUIDE'``], default ``'COLLISION'``

   .. attribute:: guide_mode

      How to create guiding velocities

      * ``MAXIMUM``
        Maximize -- Compare velocities from previous frame with new velocities from current frame and keep the maximum.
      * ``MINIMUM``
        Minimize -- Compare velocities from previous frame with new velocities from current frame and keep the minimum.
      * ``OVERRIDE``
        Override -- Always write new guide velocities for every frame (each frame only contains current velocities from guiding objects).
      * ``AVERAGED``
        Averaged -- Take average of velocities from previous frame and new velocities from current frame.

      :type: enum in [``'MAXIMUM'``, ``'MINIMUM'``, ``'OVERRIDE'``, ``'AVERAGED'``], default ``'OVERRIDE'``

   .. attribute:: subframes

      Number of additional samples to take between frames to improve quality of fast moving effector objects

      :type: int in [0, 200], default 0

   .. attribute:: surface_distance

      Additional distance around mesh surface to consider as effector

      :type: float in [0, 10], default 0.0

   .. attribute:: use_effector

      Control when to apply the effector

      :type: boolean, default True

   .. attribute:: use_plane_init

      Treat this object as a planar, unclosed mesh

      :type: boolean, default False

   .. attribute:: velocity_factor

      Multiplier of obstacle velocity

      :type: float in [-100, 100], default 1.0

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

   * :class:`FluidModifier.effector_settings`

