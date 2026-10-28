BakeSettings(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BakeSettings(bpy_struct)

   Bake data for a Scene data-block

   .. attribute:: cage_extrusion

      Inflate the active object by the specified distance for baking. This helps matching to points nearer to the outside of the selected object meshes.

      :type: float in [0, inf], default 0.0

   .. attribute:: cage_object

      Object to use as cage instead of calculating the cage from the active object with cage extrusion

      :type: :class:`Object`

   .. attribute:: filepath

      Image filepath to use when saving externally

      :type: string, default "", (never None, blend relative ``//`` prefix supported)

   .. attribute:: height

      Vertical dimension of the baking map

      :type: int in [4, 10000], default 512

   .. data:: image_settings

      :type: :class:`ImageFormatSettings`, (readonly, never None)

   .. attribute:: margin

      Extends the baked result as a post process filter

      :type: int in [0, 32767], default 16

   .. attribute:: margin_type

      Algorithm to extend the baked result

      :type: enum in :ref:`rna_enum_bake_margin_type_items`, default ``'ADJACENT_FACES'``

   .. attribute:: max_ray_distance

      The maximum ray distance for matching points between the active and selected objects. If zero, there is no limit.

      :type: float in [0, inf], default 0.0

   .. attribute:: normal_b

      Axis to bake in blue channel

      :type: enum in :ref:`rna_enum_normal_swizzle_items`, default ``'POS_X'``

   .. attribute:: normal_g

      Axis to bake in green channel

      :type: enum in :ref:`rna_enum_normal_swizzle_items`, default ``'POS_X'``

   .. attribute:: normal_r

      Axis to bake in red channel

      :type: enum in :ref:`rna_enum_normal_swizzle_items`, default ``'POS_X'``

   .. attribute:: normal_space

      Choose normal space for baking

      :type: enum in :ref:`rna_enum_normal_space_items`, default ``'OBJECT'``

   .. data:: pass_filter

      Passes to include in the active baking pass

      :type: enum set in :ref:`rna_enum_bake_pass_filter_type_items`, default set(), (readonly)

   .. attribute:: save_mode

      Where to save baked image textures

      :type: enum in :ref:`rna_enum_bake_save_mode_items`, default ``'INTERNAL'``

   .. attribute:: target

      Where to output the baked map

      :type: enum in :ref:`rna_enum_bake_target_items`, default ``'IMAGE_TEXTURES'``

   .. attribute:: use_automatic_name

      Automatically name the output file with the pass type (external only)

      :type: boolean, default False

   .. attribute:: use_cage

      Cast rays to active object from a cage

      :type: boolean, default False

   .. attribute:: use_clear

      Clear Images before baking (internal only)

      :type: boolean, default True

   .. attribute:: use_pass_color

      Color the pass

      :type: boolean, default True

   .. attribute:: use_pass_diffuse

      Add diffuse contribution

      :type: boolean, default True

   .. attribute:: use_pass_direct

      Add direct lighting contribution

      :type: boolean, default True

   .. attribute:: use_pass_emit

      Add emission contribution

      :type: boolean, default True

   .. attribute:: use_pass_glossy

      Add glossy contribution

      :type: boolean, default True

   .. attribute:: use_pass_indirect

      Add indirect lighting contribution

      :type: boolean, default True

   .. attribute:: use_pass_transmission

      Add transmission contribution

      :type: boolean, default True

   .. attribute:: use_selected_to_active

      Bake shading on the surface of selected objects to the active object

      :type: boolean, default False

   .. attribute:: use_split_materials

      Split external images per material (external only)

      :type: boolean, default False

   .. attribute:: view_from

      Source of reflection ray directions

      * ``ABOVE_SURFACE``
        Above Surface -- Cast rays from above the surface.
      * ``ACTIVE_CAMERA``
        Active Camera -- Use the active camera's position to cast rays.

      :type: enum in [``'ABOVE_SURFACE'``, ``'ACTIVE_CAMERA'``], default ``'ABOVE_SURFACE'``

   .. attribute:: width

      Horizontal dimension of the baking map

      :type: int in [4, 10000], default 512

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

   * :class:`RenderSettings.bake`

