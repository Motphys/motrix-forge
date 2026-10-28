Action(ID)
==========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Action(ID)

   A collection of F-Curves for animation

   .. data:: curve_frame_range

      The combined frame range of all F-Curves within this action

      :type: :class:`mathutils.Vector` of 2 items in [-inf, inf], default (0.0, 0.0), (readonly)

   .. data:: fcurves

      Legacy API, for backward compatibility with code that does not handle slotted actions yet. This collection contains the F-Curves for the action's first slot

      :type: :class:`ActionFCurves` :class:`bpy_prop_collection` of :class:`FCurve`, (readonly)

   .. attribute:: frame_end

      The end frame of the manually set intended playback range

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: frame_range

      The intended playback frame range of this action, using the manually set range if available, or the combined frame range of all F-Curves within this action if not (assigning sets the manual frame range)

      :type: :class:`mathutils.Vector` of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: frame_start

      The start frame of the manually set intended playback range

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. data:: groups

      Legacy API, for backward compatibility with code that does not handle slotted actions yet. This collection contains the F-Curve groups for the action's first slot

      :type: :class:`ActionGroups` :class:`bpy_prop_collection` of :class:`ActionGroup`, (readonly)

   .. attribute:: id_root

      Legacy API, for backward compatibility with code that does not handle slotted actions yet. Type of data-block that the action's first slot can be used on. Do not change unless you know what you are doing

      * ``ACTION``
        Action.
      * ``ARMATURE``
        Armature.
      * ``BRUSH``
        Brush.
      * ``CACHEFILE``
        Cache File.
      * ``CAMERA``
        Camera.
      * ``COLLECTION``
        Collection.
      * ``CURVE``
        Curve.
      * ``CURVES``
        Curves.
      * ``FONT``
        Font.
      * ``GREASEPENCIL``
        Grease Pencil.
      * ``GREASEPENCIL_V3``
        Grease Pencil v3.
      * ``IMAGE``
        Image.
      * ``KEY``
        Key.
      * ``LATTICE``
        Lattice.
      * ``LIBRARY``
        Library.
      * ``LIGHT``
        Light.
      * ``LIGHT_PROBE``
        Light Probe.
      * ``LINESTYLE``
        Line Style.
      * ``MASK``
        Mask.
      * ``MATERIAL``
        Material.
      * ``MESH``
        Mesh.
      * ``META``
        Metaball.
      * ``MOVIECLIP``
        Movie Clip.
      * ``NODETREE``
        Node Tree.
      * ``OBJECT``
        Object.
      * ``PAINTCURVE``
        Paint Curve.
      * ``PALETTE``
        Palette.
      * ``PARTICLE``
        Particle.
      * ``POINTCLOUD``
        Point Cloud.
      * ``SCENE``
        Scene.
      * ``SCREEN``
        Screen.
      * ``SOUND``
        Sound.
      * ``SPEAKER``
        Speaker.
      * ``TEXT``
        Text.
      * ``TEXTURE``
        Texture.
      * ``VOLUME``
        Volume.
      * ``WINDOWMANAGER``
        Window Manager.
      * ``WORKSPACE``
        Workspace.
      * ``WORLD``
        World.
      * ``UNSPECIFIED``
        Unspecified -- Not yet specified. When this slot is first assigned to a data-block, this will be set to the type of that data-block.

      :type: enum in [``'ACTION'``, ``'ARMATURE'``, ``'BRUSH'``, ``'CACHEFILE'``, ``'CAMERA'``, ``'COLLECTION'``, ``'CURVE'``, ``'CURVES'``, ``'FONT'``, ``'GREASEPENCIL'``, ``'GREASEPENCIL_V3'``, ``'IMAGE'``, ``'KEY'``, ``'LATTICE'``, ``'LIBRARY'``, ``'LIGHT'``, ``'LIGHT_PROBE'``, ``'LINESTYLE'``, ``'MASK'``, ``'MATERIAL'``, ``'MESH'``, ``'META'``, ``'MOVIECLIP'``, ``'NODETREE'``, ``'OBJECT'``, ``'PAINTCURVE'``, ``'PALETTE'``, ``'PARTICLE'``, ``'POINTCLOUD'``, ``'SCENE'``, ``'SCREEN'``, ``'SOUND'``, ``'SPEAKER'``, ``'TEXT'``, ``'TEXTURE'``, ``'VOLUME'``, ``'WINDOWMANAGER'``, ``'WORKSPACE'``, ``'WORLD'``, ``'UNSPECIFIED'``], default ``'UNSPECIFIED'``

   .. data:: is_action_layered

      Return whether this is a layered Action. An empty Action is considered as both a 'legacy' and a 'layered' Action.

      :type: boolean, default False, (readonly)

   .. data:: is_action_legacy

      Return whether this is a legacy Action. Legacy Actions have no layers or slots. An empty Action is considered as both a 'legacy' and a 'layered' Action. Since Blender 4.4 actions are automatically updated to layered actions, and thus this will only return True when the action is empty

      :type: boolean, default False, (readonly)

   .. data:: is_empty

      False when there is any Layer, Slot, or legacy F-Curve

      :type: boolean, default False, (readonly)

   .. data:: layers

      The list of layers that make up this Action

      :type: :class:`ActionLayers` :class:`bpy_prop_collection` of :class:`ActionLayer`, (readonly)

   .. data:: pose_markers

      Markers specific to this action, for labeling poses

      :type: :class:`ActionPoseMarkers` :class:`bpy_prop_collection` of :class:`TimelineMarker`, (readonly)

   .. data:: slots

      The list of slots in this Action

      :type: :class:`ActionSlots` :class:`bpy_prop_collection` of :class:`ActionSlot`, (readonly)

   .. attribute:: use_cyclic

      The action is intended to be used as a cycle looping over its manually set playback frame range (enabling this doesn't automatically make it loop)

      :type: boolean, default False

   .. attribute:: use_frame_range

      Manually specify the intended playback frame range for the action (this range is used by some tools, but does not affect animation evaluation)

      :type: boolean, default False

   .. method:: deselect_keys()

      Deselects all keys of the Action. The selection status of F-Curves is unchanged.


   .. method:: fcurve_ensure_for_datablock(datablock, data_path, *, index=0)

      Ensure that an F-Curve exists, with the given data path and array index, for the given data-block. This action must already be assigned to the data-block. This function will also create the layer, keyframe strip, and action slot if necessary, and take care of assigning the action slot too

      :arg datablock: The data-block animated by this action, for which to ensure the F-Curve exists. This action must already be assigned to the data-block
      :type datablock: :class:`ID`, (never None)
      :arg data_path: Data Path, F-Curve data path
      :type data_path: string, (never None)
      :arg index: Index, Array index
      :type index: int in [0, inf], (optional)
      :return: The found or created F-Curve
      :rtype: :class:`FCurve`

   .. method:: flip_with_pose(object)

      Flip the action around the X axis using a pose

      :arg object: The reference armature object to use when flipping
      :type object: :class:`Object`, (never None)

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
   * :class:`ID.name`
   * :class:`ID.name_full`
   * :class:`ID.id_type`
   * :class:`ID.session_uid`
   * :class:`ID.is_evaluated`
   * :class:`ID.original`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.use_extra_user`
   * :class:`ID.is_embedded_data`
   * :class:`ID.is_missing`
   * :class:`ID.is_runtime_data`
   * :class:`ID.is_editable`
   * :class:`ID.tag`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.library_weak_reference`
   * :class:`ID.asset_data`
   * :class:`ID.override_library`
   * :class:`ID.preview`

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
   * :class:`ID.rename`
   * :class:`ID.evaluated_get`
   * :class:`ID.copy`
   * :class:`ID.asset_mark`
   * :class:`ID.asset_clear`
   * :class:`ID.asset_generate_preview`
   * :class:`ID.override_create`
   * :class:`ID.override_hierarchy_create`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`
   * :class:`ID.preview_ensure`
   * :class:`ID.bl_rna_get_subclass`
   * :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   * :mod:`bpy.context.active_action`
   * :mod:`bpy.context.selected_editable_actions`
   * :mod:`bpy.context.selected_visible_actions`
   * :class:`ActionConstraint.action`
   * :class:`AnimData.action`
   * :class:`AnimData.action_tweak_storage`
   * :class:`BlendData.actions`
   * :class:`BlendDataActions.new`
   * :class:`BlendDataActions.remove`
   * :class:`GLTF2_filter_action.action`
   * :class:`NlaStrip.action`
   * :class:`NlaStrips.new`
   * :class:`Pose.apply_pose_from_action`
   * :class:`Pose.backup_create`
   * :class:`Pose.blend_pose_from_action`
   * :class:`SpaceDopeSheetEditor.action`
   * :class:`WindowManager.poselib_previous_action`

