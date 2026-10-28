World(ID)
=========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: World(ID)

   World data-block describing the environment and ambient lighting of a scene

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: color

      Color of the background

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.05, 0.05, 0.05)

   .. data:: cycles

      Cycles world settings

      :type: :class:`CyclesWorldSettings`, (readonly)

   .. data:: cycles_visibility

      Cycles visibility settings

      :type: :class:`CyclesVisibilitySettings`, (readonly)

   .. data:: light_settings

      World lighting settings

      :type: :class:`WorldLighting`, (readonly, never None)

   .. attribute:: lightgroup

      Lightgroup that the world belongs to

      :type: string, default "", (never None)

   .. data:: mist_settings

      World mist settings

      :type: :class:`WorldMistSettings`, (readonly, never None)

   .. data:: node_tree

      Node tree for node based worlds

      :type: :class:`NodeTree`, (readonly)

   .. attribute:: probe_resolution

      Resolution when baked to a texture

      :type: enum in [``'128'``, ``'256'``, ``'512'``, ``'1024'``, ``'2048'``, ``'4096'``], default ``'1024'``

   .. attribute:: sun_angle

      Angular diameter of the Sun as seen from the Earth

      :type: float in [0, 3.14159], default 0.00918043

   .. attribute:: sun_shadow_filter_radius

      Blur shadow aliasing using Percentage Closer Filtering

      :type: float in [0, inf], default 1.0

   .. attribute:: sun_shadow_jitter_overblur

      Apply shadow tracing to each jittered sample to reduce under-sampling artifacts

      :type: float in [0, 100], default 10.0

   .. attribute:: sun_shadow_maximum_resolution

      Maximum size of a shadow map pixel. Higher values use less memory at the cost of shadow quality.

      :type: float in [0, inf], default 0.001

   .. attribute:: sun_threshold

      If non-zero, the maximum value for world contribution that will be recorded inside the world light probe. The excess contribution is converted to a sun light. This reduces the light bleeding caused by very bright light sources.

      :type: float in [0, inf], default 10.0

   .. attribute:: use_eevee_finite_volume

      The world's volume used to be rendered by EEVEE Legacy. Conversion is needed for it to render properly.

      :type: boolean, default False

   .. attribute:: use_nodes

      Use shader nodes to render the world

      :type: boolean, default False

   .. attribute:: use_sun_shadow

      Enable sun shadow casting

      :type: boolean, default True

   .. attribute:: use_sun_shadow_jitter

      Enable jittered soft shadows to increase shadow precision (disabled in viewport unless enabled in the render settings). Has a high performance impact.

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

   * :mod:`bpy.context.world`
   * :class:`BlendData.worlds`
   * :class:`BlendDataWorlds.new`
   * :class:`BlendDataWorlds.remove`
   * :class:`Scene.world`
   * :class:`ViewLayer.world_override`

