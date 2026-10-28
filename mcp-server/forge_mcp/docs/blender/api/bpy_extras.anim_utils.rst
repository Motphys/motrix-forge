bpy_extras submodule (bpy_extras.anim_utils)
============================================

.. module:: bpy_extras.anim_utils

.. function:: bake_action(obj, *, action, frames, bake_options)

   :arg obj: Object to bake.
   :type obj: :class:`bpy.types.Object`
   :arg action: An action to bake the data into, or None for a new action
      to be created.
   :type action: :class:`bpy.types.Action` | None
   :arg frames: Frames to bake.
   :type frames: int
   :arg bake_options: Options for baking.
   :type bake_options: :class:`anim_utils.BakeOptions`
   :return: Action or None.
   :rtype: :class:`bpy.types.Action` | None

.. function:: bake_action_objects(object_action_pairs, *, frames, bake_options)

   A version of :func:`bake_action_objects_iter` that takes frames and returns the output.
   
   :arg frames: Frames to bake.
   :type frames: iterable of int
   :arg bake_options: Options for baking.
   :type bake_options: :class:`anim_utils.BakeOptions`
   
   :return: A sequence of Action or None types (aligned with ``object_action_pairs``)
   :rtype: Sequence[:class:`bpy.types.Action`]

.. function:: bake_action_iter(obj, *, action, bake_options)

   An coroutine that bakes action for a single object.
   
   :arg obj: Object to bake.
   :type obj: :class:`bpy.types.Object`
   :arg action: An action to bake the data into, or None for a new action
      to be created.
   :type action: :class:`bpy.types.Action` | None
   :arg bake_options: Boolean options of what to include into the action bake.
   :type bake_options: :class:`anim_utils.BakeOptions`
   
   :return: an action or None
   :rtype: :class:`bpy.types.Action`

.. function:: bake_action_objects_iter(object_action_pairs, bake_options)

   An coroutine that bakes actions for multiple objects.
   
   :arg object_action_pairs: Sequence of object action tuples,
      action is the destination for the baked data. When None a new action will be created.
   :type object_action_pairs: Sequence of (:class:`bpy.types.Object`, :class:`bpy.types.Action`)
   :arg bake_options: Options for baking.
   :type bake_options: :class:`anim_utils.BakeOptions`

.. class:: bpy_extras.anim_utils.BakeOptions

   BakeOptions(only_selected: bool, do_pose: bool, do_object: bool, do_visual_keying: bool, do_constraint_clear: bool, do_parents_clear: bool, do_clean: bool, do_location: bool, do_rotation: bool, do_scale: bool, do_bbone: bool, do_custom_props: bool)



