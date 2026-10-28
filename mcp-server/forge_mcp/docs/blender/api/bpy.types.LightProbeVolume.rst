LightProbeVolume(LightProbe)
============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`LightProbe`

.. class:: LightProbeVolume(LightProbe)

   Light probe that captures low frequency lighting inside a volume

   .. attribute:: bake_samples

      Number of ray directions to evaluate when baking

      :type: int in [1, inf], default 2048

   .. attribute:: capture_distance

      Distance around the probe volume that will be considered during the bake

      :type: float in [1e-06, inf], default 20.0

   .. attribute:: capture_emission

      Bake emissive surfaces for more accurate lighting

      :type: boolean, default True

   .. attribute:: capture_indirect

      Bake light bounces from light sources for more accurate lighting

      :type: boolean, default True

   .. attribute:: capture_world

      Bake incoming light from the world instead of just the visibility for more accurate lighting, but lose correct blending to surrounding irradiance volumes

      :type: boolean, default False

   .. attribute:: clamp_direct

      Clamp the direct lighting intensity to reduce noise (0 to disable)

      :type: float in [0, inf], default 0.0

   .. attribute:: clamp_indirect

      Clamp the indirect lighting intensity to reduce noise (0 to disable)

      :type: float in [0, inf], default 10.0

   .. attribute:: dilation_radius

      Radius in grid sample to search valid grid samples to copy into invalid grid samples

      :type: float in [1, 5], default 1.0

   .. attribute:: dilation_threshold

      Ratio of front-facing surface hits under which a grid sample will reuse neighbors grid sample lighting

      :type: float in [0, 1], default 0.5

   .. attribute:: escape_bias

      Distance to search for valid capture positions to prevent lighting artifacts

      :type: float in [0, 1], default 0.1

   .. attribute:: facing_bias

      Smoother irradiance interpolation but introduce light bleeding

      :type: float in [0, inf], default 0.5

   .. attribute:: intensity

      Modify the intensity of the lighting captured by this probe

      :type: float in [0, inf], default 1.0

   .. attribute:: normal_bias

      Offset sampling of the irradiance grid in the surface normal direction to reduce light bleeding

      :type: float in [0, inf], default 0.3

   .. attribute:: resolution_x

      Number of samples along the x axis of the volume

      :type: int in [1, 256], default 4

   .. attribute:: resolution_y

      Number of samples along the y axis of the volume

      :type: int in [1, 256], default 4

   .. attribute:: resolution_z

      Number of samples along the z axis of the volume

      :type: int in [1, 256], default 4

   .. attribute:: surface_bias

      Moves capture points away from surfaces to prevent artifacts

      :type: float in [0, 1], default 0.05

   .. attribute:: surfel_density

      Number of surfels to spawn in one local unit distance (higher values improve quality)

      :type: int in [1, inf], default 20

   .. attribute:: validity_threshold

      Ratio of front-facing surface hits under which a grid sample will not be considered for lighting

      :type: float in [0, 1], default 0.4

   .. attribute:: view_bias

      Offset sampling of the irradiance grid in the viewing direction to reduce light bleeding

      :type: float in [0, inf], default 0.0

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
   * :class:`LightProbe.type`
   * :class:`LightProbe.clip_start`
   * :class:`LightProbe.show_clip`
   * :class:`LightProbe.show_influence`
   * :class:`LightProbe.influence_distance`
   * :class:`LightProbe.visibility_buffer_bias`
   * :class:`LightProbe.visibility_bleed_bias`
   * :class:`LightProbe.visibility_blur`
   * :class:`LightProbe.visibility_collection`
   * :class:`LightProbe.invert_visibility_collection`
   * :class:`LightProbe.show_data`
   * :class:`LightProbe.use_data_display`
   * :class:`LightProbe.data_display_size`
   * :class:`LightProbe.animation_data`

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
   * :class:`LightProbe.bl_rna_get_subclass`
   * :class:`LightProbe.bl_rna_get_subclass_py`

