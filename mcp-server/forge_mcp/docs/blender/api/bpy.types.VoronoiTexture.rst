VoronoiTexture(Texture)
=======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`, :class:`Texture`

.. class:: VoronoiTexture(Texture)

   Procedural voronoi texture

   .. attribute:: color_mode

      * ``INTENSITY``
        Intensity -- Only calculate intensity.
      * ``POSITION``
        Position -- Color cells by position.
      * ``POSITION_OUTLINE``
        Position and Outline -- Use position plus an outline based on F2-F1.
      * ``POSITION_OUTLINE_INTENSITY``
        Position, Outline, and Intensity -- Multiply position and outline by intensity.

      :type: enum in [``'INTENSITY'``, ``'POSITION'``, ``'POSITION_OUTLINE'``, ``'POSITION_OUTLINE_INTENSITY'``], default ``'INTENSITY'``

   .. attribute:: distance_metric

      Algorithm used to calculate distance of sample points to feature points

      * ``DISTANCE``
        Actual Distance -- sqrt(x\*x+y\*y+z\*z).
      * ``DISTANCE_SQUARED``
        Distance Squared -- (x\*x+y\*y+z\*z).
      * ``MANHATTAN``
        Manhattan -- The length of the distance in axial directions.
      * ``CHEBYCHEV``
        Chebychev -- The length of the longest Axial journey.
      * ``MINKOVSKY_HALF``
        Minkowski 1/2 -- Set Minkowski variable to 0.5.
      * ``MINKOVSKY_FOUR``
        Minkowski 4 -- Set Minkowski variable to 4.
      * ``MINKOVSKY``
        Minkowski -- Use the Minkowski function to calculate distance (exponent value determines the shape of the boundaries).

      :type: enum in [``'DISTANCE'``, ``'DISTANCE_SQUARED'``, ``'MANHATTAN'``, ``'CHEBYCHEV'``, ``'MINKOVSKY_HALF'``, ``'MINKOVSKY_FOUR'``, ``'MINKOVSKY'``], default ``'DISTANCE'``

   .. attribute:: minkovsky_exponent

      Minkowski exponent

      :type: float in [0.01, 10], default 2.5

   .. attribute:: nabla

      Size of derivative offset used for calculating normal

      :type: float in [0.001, 0.1], default 0.025

   .. attribute:: noise_intensity

      Scales the intensity of the noise

      :type: float in [0.01, 10], default 1.0

   .. attribute:: noise_scale

      Scaling for noise input

      :type: float in [0.0001, inf], default 0.25

   .. attribute:: weight_1

      Voronoi feature weight 1

      :type: float in [-2, 2], default 1.0

   .. attribute:: weight_2

      Voronoi feature weight 2

      :type: float in [-2, 2], default 0.0

   .. attribute:: weight_3

      Voronoi feature weight 3

      :type: float in [-2, 2], default 0.0

   .. attribute:: weight_4

      Voronoi feature weight 4

      :type: float in [-2, 2], default 0.0

   .. data:: users_material

      Materials that use this texture
      
              :type: tuple of :class:`Material`
      
              .. note:: Takes ``O(len(bpy.data.materials) * len(material.texture_slots))`` time.

      (readonly)

   .. data:: users_object_modifier

      Object modifiers that use this texture
      
              :type: tuple of :class:`Object`
      
              .. note:: Takes ``O(len(bpy.data.objects) * len(obj.modifiers))`` time.

      (readonly)

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
   * :class:`Texture.type`
   * :class:`Texture.use_clamp`
   * :class:`Texture.use_color_ramp`
   * :class:`Texture.color_ramp`
   * :class:`Texture.intensity`
   * :class:`Texture.contrast`
   * :class:`Texture.saturation`
   * :class:`Texture.factor_red`
   * :class:`Texture.factor_green`
   * :class:`Texture.factor_blue`
   * :class:`Texture.use_preview_alpha`
   * :class:`Texture.use_nodes`
   * :class:`Texture.node_tree`
   * :class:`Texture.animation_data`
   * :class:`Texture.users_material`
   * :class:`Texture.users_object_modifier`

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
   * :class:`Texture.evaluate`
   * :class:`Texture.bl_rna_get_subclass`
   * :class:`Texture.bl_rna_get_subclass_py`

