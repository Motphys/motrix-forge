XrSessionState(bpy_struct)
==========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: XrSessionState(bpy_struct)

   Runtime state information about the VR session

   .. data:: actionmaps

      :type: :class:`XrActionMaps` :class:`bpy_prop_collection` of :class:`XrActionMap`, (readonly)

   .. attribute:: active_actionmap

      :type: int in [-inf, inf], default 0

   .. attribute:: navigation_location

      Location offset to apply to base pose when determining viewer location

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: navigation_rotation

      Rotation offset to apply to base pose when determining viewer rotation

      :type: :class:`mathutils.Quaternion` rotation of 4 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: navigation_scale

      Additional scale multiplier to apply to base scale when determining viewer scale

      :type: float in [-inf, inf], default 0.0

   .. attribute:: selected_actionmap

      :type: int in [-inf, inf], default 0

   .. data:: viewer_pose_location

      Last known location of the viewer pose (center between the eyes) in world space

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. data:: viewer_pose_rotation

      Last known rotation of the viewer pose (center between the eyes) in world space

      :type: :class:`mathutils.Quaternion` rotation of 4 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0), (readonly)

   .. classmethod:: is_running(context)

      Query if the VR session is currently running

      :type context: :class:`Context`, (never None)
      :return: Result
      :rtype: boolean

   .. classmethod:: reset_to_base_pose(context)

      Force resetting of position and rotation deltas

      :type context: :class:`Context`, (never None)

   .. classmethod:: action_set_create(context, actionmap)

      Create a VR action set

      :type context: :class:`Context`, (never None)
      :type actionmap: :class:`XrActionMap`, (never None)
      :return: Result
      :rtype: boolean

   .. classmethod:: action_create(context, actionmap, actionmap_item)

      Create a VR action

      :type context: :class:`Context`, (never None)
      :type actionmap: :class:`XrActionMap`, (never None)
      :type actionmap_item: :class:`XrActionMapItem`, (never None)
      :return: Result
      :rtype: boolean

   .. classmethod:: action_binding_create(context, actionmap, actionmap_item, actionmap_binding)

      Create a VR action binding

      :type context: :class:`Context`, (never None)
      :type actionmap: :class:`XrActionMap`, (never None)
      :type actionmap_item: :class:`XrActionMapItem`, (never None)
      :type actionmap_binding: :class:`XrActionMapBinding`, (never None)
      :return: Result
      :rtype: boolean

   .. classmethod:: active_action_set_set(context, action_set)

      Set the active VR action set

      :type context: :class:`Context`, (never None)
      :arg action_set: Action Set, Action set name
      :type action_set: string, (never None)
      :return: Result
      :rtype: boolean

   .. classmethod:: controller_pose_actions_set(context, action_set, grip_action, aim_action)

      Set the actions that determine the VR controller poses

      :type context: :class:`Context`, (never None)
      :arg action_set: Action Set, Action set name
      :type action_set: string, (never None)
      :arg grip_action: Grip Action, Name of the action representing the controller grips
      :type grip_action: string, (never None)
      :arg aim_action: Aim Action, Name of the action representing the controller aims
      :type aim_action: string, (never None)
      :return: Result
      :rtype: boolean

   .. classmethod:: action_state_get(context, action_set_name, action_name, user_path)

      Get the current state of a VR action

      :type context: :class:`Context`, (never None)
      :arg action_set_name: Action Set, Action set name
      :type action_set_name: string, (never None)
      :arg action_name: Action, Action name
      :type action_name: string, (never None)
      :arg user_path: User Path, OpenXR user path
      :type user_path: string, (never None)
      :return: Action State, Current state of the VR action. Second float value is only set for 2D vector type actions.
      :rtype: float array of 2 items in [-inf, inf], (never None)

   .. classmethod:: haptic_action_apply(context, action_set_name, action_name, user_path, duration, frequency, amplitude)

      Apply a VR haptic action

      :type context: :class:`Context`, (never None)
      :arg action_set_name: Action Set, Action set name
      :type action_set_name: string, (never None)
      :arg action_name: Action, Action name
      :type action_name: string, (never None)
      :arg user_path: User Path, Optional OpenXR user path. If not set, the action will be applied to all paths.
      :type user_path: string, (never None)
      :arg duration: Duration, Haptic duration in seconds. 0.0 is the minimum supported duration.
      :type duration: float in [0, inf]
      :arg frequency: Frequency, Frequency of the haptic vibration in hertz. 0.0 specifies the OpenXR runtime's default frequency.
      :type frequency: float in [0, inf]
      :arg amplitude: Amplitude, Haptic amplitude, ranging from 0.0 to 1.0
      :type amplitude: float in [0, 1]
      :return: Result
      :rtype: boolean

   .. classmethod:: haptic_action_stop(context, action_set_name, action_name, user_path)

      Stop a VR haptic action

      :type context: :class:`Context`, (never None)
      :arg action_set_name: Action Set, Action set name
      :type action_set_name: string, (never None)
      :arg action_name: Action, Action name
      :type action_name: string, (never None)
      :arg user_path: User Path, Optional OpenXR user path. If not set, the action will be stopped for all paths.
      :type user_path: string, (never None)

   .. classmethod:: controller_grip_location_get(context, index)

      Get the last known controller grip location in world space

      :type context: :class:`Context`, (never None)
      :arg index: Index, Controller index
      :type index: int in [0, 255]
      :return: Location, Controller grip location
      :rtype: :class:`mathutils.Vector` of 3 items in [-inf, inf], (never None)

   .. classmethod:: controller_grip_rotation_get(context, index)

      Get the last known controller grip rotation (quaternion) in world space

      :type context: :class:`Context`, (never None)
      :arg index: Index, Controller index
      :type index: int in [0, 255]
      :return: Rotation, Controller grip quaternion rotation
      :rtype: :class:`mathutils.Quaternion` rotation of 4 items in [-inf, inf], (never None)

   .. classmethod:: controller_aim_location_get(context, index)

      Get the last known controller aim location in world space

      :type context: :class:`Context`, (never None)
      :arg index: Index, Controller index
      :type index: int in [0, 255]
      :return: Location, Controller aim location
      :rtype: :class:`mathutils.Vector` of 3 items in [-inf, inf], (never None)

   .. classmethod:: controller_aim_rotation_get(context, index)

      Get the last known controller aim rotation (quaternion) in world space

      :type context: :class:`Context`, (never None)
      :arg index: Index, Controller index
      :type index: int in [0, 255]
      :return: Rotation, Controller aim quaternion rotation
      :rtype: :class:`mathutils.Quaternion` rotation of 4 items in [-inf, inf], (never None)

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

   * :class:`WindowManager.xr_session_state`
   * :class:`XrActionMaps.find`
   * :class:`XrActionMaps.new`
   * :class:`XrActionMaps.new_from_actionmap`
   * :class:`XrActionMaps.remove`

