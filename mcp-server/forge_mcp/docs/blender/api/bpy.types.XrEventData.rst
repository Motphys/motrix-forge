XrEventData(bpy_struct)
=======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: XrEventData(bpy_struct)

   XR Data for Window Manager Event

   .. data:: action

      XR action name

      :type: string, default "", (readonly, never None)

   .. data:: action_set

      XR action set name

      :type: string, default "", (readonly, never None)

   .. data:: bimanual

      Whether bimanual interaction is occurring

      :type: boolean, default False, (readonly)

   .. data:: controller_location

      Location of the action's corresponding controller aim in world space

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. data:: controller_location_other

      Controller aim location of the other user path for bimanual actions

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. data:: controller_rotation

      Rotation of the action's corresponding controller aim in world space

      :type: :class:`mathutils.Quaternion` rotation of 4 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0), (readonly)

   .. data:: controller_rotation_other

      Controller aim rotation of the other user path for bimanual actions

      :type: :class:`mathutils.Quaternion` rotation of 4 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0), (readonly)

   .. data:: float_threshold

      Input threshold for float/2D vector actions

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. data:: state

      XR action values corresponding to type

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0), (readonly)

   .. data:: state_other

      State of the other user path for bimanual actions

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0), (readonly)

   .. data:: type

      XR action type

      * ``FLOAT``
        Float -- Float action, representing either a digital or analog button.
      * ``VECTOR2D``
        Vector2D -- 2D float vector action, representing a thumbstick or trackpad.
      * ``POSE``
        Pose -- 3D pose action, representing a controller's location and rotation.
      * ``VIBRATION``
        Vibration -- Haptic vibration output action, to be applied with a duration, frequency, and amplitude.

      :type: enum in [``'FLOAT'``, ``'VECTOR2D'``, ``'POSE'``, ``'VIBRATION'``], default ``'FLOAT'``, (readonly)

   .. data:: user_path

      User path of the action. E.g. "/user/hand/left"

      :type: string, default "", (readonly, never None)

   .. data:: user_path_other

      Other user path, for bimanual actions. E.g. "/user/hand/right"

      :type: string, default "", (readonly, never None)

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

   * :class:`Event.xr`

