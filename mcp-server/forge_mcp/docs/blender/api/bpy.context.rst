Context Access (bpy.context)
============================

.. module:: bpy.context

The context members available depend on the area of Blender which is currently being accessed.

Note that all context values are read-only,
but may be modified through the data API or by running operators.

Global Context
--------------

These properties are available in any contexts.

.. data:: area

   :type: :class:`bpy.types.Area`, (readonly)

.. data:: asset

   :type: :class:`bpy.types.AssetRepresentation`, (readonly)

.. data:: blend_data

   :type: :class:`bpy.types.BlendData`, (readonly)

.. data:: collection

   :type: :class:`bpy.types.Collection`, (readonly)

.. data:: engine

   :type: string, default "", (readonly, never None)

.. data:: gizmo_group

   :type: :class:`bpy.types.GizmoGroup`, (readonly)

.. data:: layer_collection

   :type: :class:`bpy.types.LayerCollection`, (readonly)

.. data:: mode

   :type: enum in :ref:`rna_enum_context_mode_items`, default ``'EDIT_MESH'``, (readonly)

.. data:: preferences

   :type: :class:`bpy.types.Preferences`, (readonly)

.. data:: region

   :type: :class:`bpy.types.Region`, (readonly)

.. data:: region_data

   :type: :class:`bpy.types.RegionView3D`, (readonly)

.. data:: region_popup

   The temporary region for pop-ups (including menus and pop-overs)

   :type: :class:`bpy.types.Region`, (readonly)

.. data:: scene

   :type: :class:`bpy.types.Scene`, (readonly)

.. data:: screen

   :type: :class:`bpy.types.Screen`, (readonly)

.. data:: space_data

   The current space, may be None in background-mode, when the cursor is outside the window or when using menu-search

   :type: :class:`bpy.types.Space`, (readonly)

.. data:: tool_settings

   :type: :class:`bpy.types.ToolSettings`, (readonly)

.. data:: view_layer

   :type: :class:`bpy.types.ViewLayer`, (readonly)

.. data:: window

   :type: :class:`bpy.types.Window`, (readonly)

.. data:: window_manager

   :type: :class:`bpy.types.WindowManager`, (readonly)

.. data:: workspace

   :type: :class:`bpy.types.WorkSpace`, (readonly)


Buttons Context
---------------

.. data:: texture_slot

   :type: :class:`bpy.types.TextureSlot`

.. data:: scene
   :noindex:

   :type: :class:`bpy.types.Scene`

.. data:: world

   :type: :class:`bpy.types.World`

.. data:: object

   :type: :class:`bpy.types.Object`

.. data:: mesh

   :type: :class:`bpy.types.Mesh`

.. data:: armature

   :type: :class:`bpy.types.Armature`

.. data:: lattice

   :type: :class:`bpy.types.Lattice`

.. data:: curve

   :type: :class:`bpy.types.Curve`

.. data:: meta_ball

   :type: :class:`bpy.types.MetaBall`

.. data:: light

   :type: :class:`bpy.types.Light`

.. data:: speaker

   :type: :class:`bpy.types.Speaker`

.. data:: lightprobe

   :type: :class:`bpy.types.LightProbe`

.. data:: camera

   :type: :class:`bpy.types.Camera`

.. data:: material

   :type: :class:`bpy.types.Material`

.. data:: material_slot

   :type: :class:`bpy.types.MaterialSlot`

.. data:: texture

   :type: :class:`bpy.types.Texture`

.. data:: texture_user

   :type: :class:`bpy.types.ID`

.. data:: texture_user_property

   :type: :class:`bpy.types.Property`

.. data:: texture_node

   :type: :class:`bpy.types.Node`

.. data:: bone

   :type: :class:`bpy.types.Bone`

.. data:: edit_bone

   :type: :class:`bpy.types.EditBone`

.. data:: pose_bone

   :type: :class:`bpy.types.PoseBone`

.. data:: particle_system

   :type: :class:`bpy.types.ParticleSystem`

.. data:: particle_system_editable

   :type: :class:`bpy.types.ParticleSystem`

.. data:: particle_settings

   :type: :class:`bpy.types.ParticleSettings`

.. data:: cloth

   :type: :class:`bpy.types.ClothModifier`

.. data:: soft_body

   :type: :class:`bpy.types.SoftBodyModifier`

.. data:: fluid

   :type: :class:`bpy.types.FluidSimulationModifier`

.. data:: collision

   :type: :class:`bpy.types.CollisionModifier`

.. data:: brush

   :type: :class:`bpy.types.Brush`

.. data:: dynamic_paint

   :type: :class:`bpy.types.DynamicPaintModifier`

.. data:: line_style

   :type: :class:`bpy.types.FreestyleLineStyle`

.. data:: collection
   :noindex:

   :type: :class:`bpy.types.LayerCollection`

.. data:: gpencil

   :type: :class:`bpy.types.GreasePencil`

.. data:: grease_pencil

   :type: :class:`bpy.types.GreasePencilv3`

.. data:: curves

   :type: Hair Curves

.. data:: pointcloud

   :type: :class:`bpy.types.PointCloud`

.. data:: volume

   :type: :class:`bpy.types.Volume`


Clip Context
------------

.. data:: edit_movieclip

   :type: :class:`bpy.types.MovieClip`

.. data:: edit_mask

   :type: :class:`bpy.types.Mask`


File Context
------------

.. data:: active_file

   :type: :class:`bpy.types.FileSelectEntry`

.. data:: selected_files

   :type: sequence of :class:`bpy.types.FileSelectEntry`

.. data:: asset_library_reference

   :type: :class:`bpy.types.AssetLibraryReference`

.. data:: selected_assets

   :type: sequence of :class:`bpy.types.AssetRepresentation`

.. data:: id

   :type: :class:`bpy.types.ID`

.. data:: selected_ids

   :type: sequence of :class:`bpy.types.ID`


Image Context
-------------

.. data:: edit_image

   :type: :class:`bpy.types.Image`

.. data:: edit_mask
   :noindex:

   :type: :class:`bpy.types.Mask`


Node Context
------------

.. data:: selected_nodes

   :type: sequence of :class:`bpy.types.Node`

.. data:: active_node

   :type: :class:`bpy.types.Node`

.. data:: light
   :noindex:

   :type: :class:`bpy.types.Light`

.. data:: material
   :noindex:

   :type: :class:`bpy.types.Material`

.. data:: world
   :noindex:

   :type: :class:`bpy.types.World`


Screen Context
--------------

.. data:: scene
   :noindex:

   :type: :class:`bpy.types.Scene`

.. data:: view_layer
   :noindex:

   :type: :class:`bpy.types.ViewLayer`

.. data:: visible_objects

   :type: sequence of :class:`bpy.types.Object`

.. data:: selectable_objects

   :type: sequence of :class:`bpy.types.Object`

.. data:: selected_objects

   :type: sequence of :class:`bpy.types.Object`

.. data:: editable_objects

   :type: sequence of :class:`bpy.types.Object`

.. data:: selected_editable_objects

   :type: sequence of :class:`bpy.types.Object`

.. data:: objects_in_mode

   :type: sequence of :class:`bpy.types.Object`

.. data:: objects_in_mode_unique_data

   :type: sequence of :class:`bpy.types.Object`

.. data:: visible_bones

   :type: sequence of :class:`bpy.types.EditBone`

.. data:: editable_bones

   :type: sequence of :class:`bpy.types.EditBone`

.. data:: selected_bones

   :type: sequence of :class:`bpy.types.EditBone`

.. data:: selected_editable_bones

   :type: sequence of :class:`bpy.types.EditBone`

.. data:: visible_pose_bones

   :type: sequence of :class:`bpy.types.PoseBone`

.. data:: selected_pose_bones

   :type: sequence of :class:`bpy.types.PoseBone`

.. data:: selected_pose_bones_from_active_object

   :type: sequence of :class:`bpy.types.PoseBone`

.. data:: active_bone

   :type: :class:`bpy.types.EditBone` or :class:`bpy.types.Bone`

.. data:: active_pose_bone

   :type: :class:`bpy.types.PoseBone`

.. data:: active_object

   :type: :class:`bpy.types.Object`

.. data:: object
   :noindex:

   :type: :class:`bpy.types.Object`

.. data:: edit_object

   :type: :class:`bpy.types.Object`

.. data:: sculpt_object

   :type: :class:`bpy.types.Object`

.. data:: vertex_paint_object

   :type: :class:`bpy.types.Object`

.. data:: weight_paint_object

   :type: :class:`bpy.types.Object`

.. data:: image_paint_object

   :type: :class:`bpy.types.Object`

.. data:: particle_edit_object

   :type: :class:`bpy.types.Object`

.. data:: pose_object

   :type: :class:`bpy.types.Object`

.. data:: active_sequence_strip

   :type: :class:`bpy.types.Strip`

.. data:: sequences

   :type: sequence of :class:`bpy.types.Strip`

.. data:: selected_sequences

   :type: sequence of :class:`bpy.types.Strip`

.. data:: selected_editable_sequences

   :type: sequence of :class:`bpy.types.Strip`

.. data:: active_nla_track

   :type: :class:`bpy.types.NlaTrack`

.. data:: active_nla_strip

   :type: :class:`bpy.types.NlaStrip`

.. data:: selected_nla_strips

   :type: sequence of :class:`bpy.types.NlaStrip`

.. data:: selected_movieclip_tracks

   :type: sequence of :class:`bpy.types.MovieTrackingTrack`

.. data:: annotation_data

   :type: :class:`bpy.types.GreasePencil`

.. data:: annotation_data_owner

   :type: :class:`bpy.types.ID`

.. data:: active_annotation_layer

   :type: :class:`bpy.types.GPencilLayer`

.. data:: grease_pencil
   :noindex:

   :type: :class:`bpy.types.GreasePencilv3`

.. data:: active_operator

   :type: :class:`bpy.types.Operator`

.. data:: active_action

   :type: :class:`bpy.types.Action`

.. data:: selected_visible_actions

   :type: sequence of :class:`bpy.types.Action`

.. data:: selected_editable_actions

   :type: sequence of :class:`bpy.types.Action`

.. data:: visible_fcurves

   :type: sequence of :class:`bpy.types.FCurve`

.. data:: editable_fcurves

   :type: sequence of :class:`bpy.types.FCurve`

.. data:: selected_visible_fcurves

   :type: sequence of :class:`bpy.types.FCurve`

.. data:: selected_editable_fcurves

   :type: sequence of :class:`bpy.types.FCurve`

.. data:: active_editable_fcurve

   :type: :class:`bpy.types.FCurve`

.. data:: selected_editable_keyframes

   :type: sequence of :class:`bpy.types.Keyframe`

.. data:: ui_list

   :type: :class:`bpy.types.UIList`

.. data:: property

   :type: :class:`bpy.types.AnyType` or :class:`str` or :class:`int`


   Get the property associated with a hovered button.
   Returns a tuple of the data-block, data path to the property, and array index.

   .. note::

      When the property doesn't have an associated :class:`bpy.types.ID` non-ID data may be returned.
      This may occur when accessing windowing data, for example, operator properties.

   .. literalinclude:: ..\examples\bpy.context.property.py
      :lines: 11-

.. data:: asset_library_reference
   :noindex:

   :type: :class:`bpy.types.AssetLibraryReference`

.. data:: active_strip

   :type: :class:`bpy.types.Strip`

.. data:: strips

   :type: sequence of :class:`bpy.types.Strip`

.. data:: selected_strips

   :type: sequence of :class:`bpy.types.Strip`

.. data:: selected_editable_strips

   :type: sequence of :class:`bpy.types.Strip`


Sequencer Context
-----------------

.. data:: edit_mask
   :noindex:

   :type: :class:`bpy.types.Mask`


Text Context
------------

.. data:: edit_text

   :type: :class:`bpy.types.Text`


View3D Context
--------------

.. data:: active_object
   :noindex:

   :type: :class:`bpy.types.Object`

.. data:: selected_ids
   :noindex:

   :type: sequence of :class:`bpy.types.ID`

