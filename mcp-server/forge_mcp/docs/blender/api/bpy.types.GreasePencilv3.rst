GreasePencilv3(ID)
==================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: GreasePencilv3(ID)

   Grease Pencil data-block

   .. attribute:: after_color

      Base color for ghosts after the active frame

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.12549, 0.082353, 0.529412)

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. data:: attributes

      Geometry attributes

      :type: :class:`AttributeGroupGreasePencil` :class:`bpy_prop_collection` of :class:`Attribute`, (readonly)

   .. attribute:: before_color

      Base color for ghosts before the active frame

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.145098, 0.419608, 0.137255)

   .. data:: color_attributes

      Geometry color attributes

      :type: :class:`AttributeGroupGreasePencil` :class:`bpy_prop_collection` of :class:`Attribute`, (readonly)

   .. attribute:: ghost_after_range

      Maximum number of frames to show after current frame (0 = don't show any frames after current)

      :type: int in [0, 120], default 1

   .. attribute:: ghost_before_range

      Maximum number of frames to show before current frame (0 = don't show any frames before current)

      :type: int in [0, 120], default 1

   .. data:: layer_groups

      Grease Pencil layer groups

      :type: :class:`GreasePencilv3LayerGroup` :class:`bpy_prop_collection` of :class:`GreasePencilLayerGroup`, (readonly)

   .. data:: layers

      Grease Pencil layers

      :type: :class:`GreasePencilv3Layers` :class:`bpy_prop_collection` of :class:`GreasePencilLayer`, (readonly)

   .. data:: materials

      :type: :class:`IDMaterials` :class:`bpy_prop_collection` of :class:`Material`, (readonly)

   .. attribute:: onion_factor

      Change fade opacity of displayed onion frames

      :type: float in [0, 1], default 0.5

   .. attribute:: onion_keyframe_type

      Type of keyframe (for filtering)

      * ``ALL``
        All -- Include all Keyframe types.
      * ``KEYFRAME``
        Keyframe -- Normal keyframe, e.g. for key poses.
      * ``BREAKDOWN``
        Breakdown -- A breakdown pose, e.g. for transitions between key poses.
      * ``MOVING_HOLD``
        Moving Hold -- A keyframe that is part of a moving hold.
      * ``EXTREME``
        Extreme -- An 'extreme' pose, or some other purpose as needed.
      * ``JITTER``
        Jitter -- A filler or baked keyframe for keying on ones, or some other purpose as needed.
      * ``GENERATED``
        Generated -- A key generated automatically by a tool, not manually created.

      :type: enum in [``'ALL'``, ``'KEYFRAME'``, ``'BREAKDOWN'``, ``'MOVING_HOLD'``, ``'EXTREME'``, ``'JITTER'``, ``'GENERATED'``], default ``'ALL'``

   .. attribute:: onion_mode

      Mode to display frames

      * ``ABSOLUTE``
        Frames -- Frames in absolute range of the scene frame.
      * ``RELATIVE``
        Keyframes -- Frames in relative range of the Grease Pencil keyframes.
      * ``SELECTED``
        Selected -- Only selected keyframes.

      :type: enum in [``'ABSOLUTE'``, ``'RELATIVE'``, ``'SELECTED'``], default ``'ABSOLUTE'``

   .. attribute:: stroke_depth_order

      Defines how the strokes are ordered in 3D space (for objects not displayed 'In Front')

      :type: enum in :ref:`rna_enum_stroke_depth_order_items`, default ``'2D'``

   .. attribute:: use_autolock_layers

      Automatically lock all layers except the active one to avoid accidental changes

      :type: boolean, default False

   .. attribute:: use_ghost_custom_colors

      Use custom colors for ghost frames

      :type: boolean, default False

   .. attribute:: use_onion_fade

      Display onion keyframes with a fade in color transparency

      :type: boolean, default False

   .. attribute:: use_onion_loop

      Display onion keyframes for looping animations

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

   * :mod:`bpy.context.grease_pencil`
   * :class:`BlendData.grease_pencils_v3`
   * :class:`BlendDataGreasePencilsV3.new`
   * :class:`BlendDataGreasePencilsV3.remove`

