ViewLayer(bpy_struct)
=====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ViewLayer(bpy_struct)

   View layer

   .. data:: active_aov

      Active AOV

      :type: :class:`AOV`, (readonly)

   .. attribute:: active_aov_index

      Index of active AOV

      :type: int in [0, inf], default 0

   .. attribute:: active_layer_collection

      Active layer collection in this view layer's hierarchy

      :type: :class:`LayerCollection`, (never None)

   .. data:: active_lightgroup

      Active Lightgroup

      :type: :class:`Lightgroup`, (readonly)

   .. attribute:: active_lightgroup_index

      Index of active lightgroup

      :type: int in [0, inf], default 0

   .. data:: aovs

      :type: :class:`AOVs` :class:`bpy_prop_collection` of :class:`AOV`, (readonly)

   .. data:: cycles

      Cycles ViewLayer Settings

      :type: :class:`CyclesRenderLayerSettings`, (readonly)

   .. data:: depsgraph

      Dependencies in the scene data

      :type: :class:`Depsgraph`, (readonly)

   .. data:: eevee

      View layer settings for EEVEE

      :type: :class:`ViewLayerEEVEE`, (readonly, never None)

   .. data:: freestyle_settings

      :type: :class:`FreestyleSettings`, (readonly, never None)

   .. data:: has_export_collections

      At least one Collection in this View Layer has an exporter

      :type: boolean, default False, (readonly)

   .. data:: layer_collection

      Root of collections hierarchy of this view layer, its 'collection' pointer property is the same as the scene's master collection

      :type: :class:`LayerCollection`, (readonly, never None)

   .. data:: lightgroups

      :type: :class:`Lightgroups` :class:`bpy_prop_collection` of :class:`Lightgroup`, (readonly)

   .. attribute:: material_override

      Material to override all other materials in this view layer

      :type: :class:`Material`

   .. attribute:: name

      View layer name

      :type: string, default "", (never None)

   .. data:: objects

      All the objects in this layer

      :type: :class:`LayerObjects` :class:`bpy_prop_collection` of :class:`Object`, (readonly)

   .. attribute:: pass_alpha_threshold

      Z, Index, normal, UV and vector passes are only affected by surfaces with alpha transparency equal to or higher than this threshold

      :type: float in [0, 1], default 0.0

   .. attribute:: pass_cryptomatte_depth

      Sets how many unique objects can be distinguished per pixel

      :type: int in [2, 16], default 6

   .. attribute:: samples

      Override number of render samples for this view layer, 0 will use the scene setting

      :type: int in [0, inf], default 0

   .. attribute:: use

      Enable or disable rendering of this View Layer

      :type: boolean, default False

   .. attribute:: use_ao

      Render Ambient Occlusion in this Layer

      :type: boolean, default False

   .. attribute:: use_freestyle

      Render stylized strokes in this Layer

      :type: boolean, default False

   .. attribute:: use_grease_pencil

      Render Grease Pencil on this layer

      :type: boolean, default False

   .. attribute:: use_motion_blur

      Render motion blur in this Layer, if enabled in the scene

      :type: boolean, default False

   .. attribute:: use_pass_ambient_occlusion

      Deliver Ambient Occlusion pass

      :type: boolean, default False

   .. attribute:: use_pass_combined

      Deliver full combined RGBA buffer

      :type: boolean, default False

   .. attribute:: use_pass_cryptomatte_accurate

      Generate a more accurate cryptomatte pass

      :type: boolean, default True

   .. attribute:: use_pass_cryptomatte_asset

      Render cryptomatte asset pass, for isolating groups of objects with the same parent

      :type: boolean, default False

   .. attribute:: use_pass_cryptomatte_material

      Render cryptomatte material pass, for isolating materials in compositing

      :type: boolean, default False

   .. attribute:: use_pass_cryptomatte_object

      Render cryptomatte object pass, for isolating objects in compositing

      :type: boolean, default False

   .. attribute:: use_pass_diffuse_color

      Deliver diffuse color pass

      :type: boolean, default False

   .. attribute:: use_pass_diffuse_direct

      Deliver diffuse direct pass

      :type: boolean, default False

   .. attribute:: use_pass_diffuse_indirect

      Deliver diffuse indirect pass

      :type: boolean, default False

   .. attribute:: use_pass_emit

      Deliver emission pass

      :type: boolean, default False

   .. attribute:: use_pass_environment

      Deliver environment lighting pass

      :type: boolean, default False

   .. attribute:: use_pass_glossy_color

      Deliver glossy color pass

      :type: boolean, default False

   .. attribute:: use_pass_glossy_direct

      Deliver glossy direct pass

      :type: boolean, default False

   .. attribute:: use_pass_glossy_indirect

      Deliver glossy indirect pass

      :type: boolean, default False

   .. attribute:: use_pass_grease_pencil

      Deliver Grease Pencil render result in a separate pass

      :type: boolean, default False

   .. attribute:: use_pass_material_index

      Deliver material index pass

      :type: boolean, default False

   .. attribute:: use_pass_mist

      Deliver mist factor pass (0.0 to 1.0)

      :type: boolean, default False

   .. attribute:: use_pass_normal

      Deliver normal pass

      :type: boolean, default False

   .. attribute:: use_pass_object_index

      Deliver object index pass

      :type: boolean, default False

   .. attribute:: use_pass_position

      Deliver position pass

      :type: boolean, default False

   .. attribute:: use_pass_shadow

      Deliver shadow pass

      :type: boolean, default False

   .. attribute:: use_pass_subsurface_color

      Deliver subsurface color pass

      :type: boolean, default False

   .. attribute:: use_pass_subsurface_direct

      Deliver subsurface direct pass

      :type: boolean, default False

   .. attribute:: use_pass_subsurface_indirect

      Deliver subsurface indirect pass

      :type: boolean, default False

   .. attribute:: use_pass_transmission_color

      Deliver transmission color pass

      :type: boolean, default False

   .. attribute:: use_pass_transmission_direct

      Deliver transmission direct pass

      :type: boolean, default False

   .. attribute:: use_pass_transmission_indirect

      Deliver transmission indirect pass

      :type: boolean, default False

   .. attribute:: use_pass_uv

      Deliver texture UV pass

      :type: boolean, default False

   .. attribute:: use_pass_vector

      Deliver speed vector pass

      :type: boolean, default False

   .. attribute:: use_pass_z

      Deliver Z values pass

      :type: boolean, default False

   .. attribute:: use_sky

      Render Sky in this Layer

      :type: boolean, default False

   .. attribute:: use_solid

      Render Solid faces in this Layer

      :type: boolean, default False

   .. attribute:: use_strand

      Render Strands in this Layer

      :type: boolean, default False

   .. attribute:: use_volumes

      Render volumes in this Layer

      :type: boolean, default False

   .. attribute:: world_override

      Override world in this view layer

      :type: :class:`World`

   .. classmethod:: update_render_passes()

      Requery the enabled render passes from the render engine


   .. method:: update()

      Update data tagged to be updated from previous access to data or operators


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

   * :mod:`bpy.context.view_layer`
   * :class:`Context.view_layer`
   * :class:`Depsgraph.view_layer`
   * :class:`Depsgraph.view_layer_eval`
   * :class:`ID.override_hierarchy_create`
   * :class:`IDOverrideLibrary.resync`
   * :class:`LayerCollection.has_selected_objects`
   * :class:`Object.hide_get`
   * :class:`Object.hide_set`
   * :class:`Object.holdout_get`
   * :class:`Object.indirect_only_get`
   * :class:`Object.select_get`
   * :class:`Object.select_set`
   * :class:`Object.visible_get`
   * :class:`RenderEngine.register_pass`
   * :class:`RenderEngine.update_render_passes`
   * :class:`Scene.statistics`
   * :class:`Scene.view_layers`
   * :class:`ViewLayers.new`
   * :class:`ViewLayers.remove`
   * :class:`Window.view_layer`

