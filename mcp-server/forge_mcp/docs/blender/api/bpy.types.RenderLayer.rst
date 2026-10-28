RenderLayer(bpy_struct)
=======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RenderLayer(bpy_struct)


   .. data:: name

      View layer name

      :type: string, default "", (readonly, never None)

   .. data:: passes

      :type: :class:`RenderPasses` :class:`bpy_prop_collection` of :class:`RenderPass`, (readonly)

   .. data:: use_ao

      Render Ambient Occlusion in this Layer

      :type: boolean, default False, (readonly)

   .. data:: use_grease_pencil

      Render Grease Pencil on this layer

      :type: boolean, default False, (readonly)

   .. data:: use_motion_blur

      Render motion blur in this Layer, if enabled in the scene

      :type: boolean, default False, (readonly)

   .. data:: use_pass_ambient_occlusion

      Deliver Ambient Occlusion pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_combined

      Deliver full combined RGBA buffer

      :type: boolean, default False, (readonly)

   .. data:: use_pass_diffuse_color

      Deliver diffuse color pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_diffuse_direct

      Deliver diffuse direct pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_diffuse_indirect

      Deliver diffuse indirect pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_emit

      Deliver emission pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_environment

      Deliver environment lighting pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_glossy_color

      Deliver glossy color pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_glossy_direct

      Deliver glossy direct pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_glossy_indirect

      Deliver glossy indirect pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_material_index

      Deliver material index pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_mist

      Deliver mist factor pass (0.0 to 1.0)

      :type: boolean, default False, (readonly)

   .. data:: use_pass_normal

      Deliver normal pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_object_index

      Deliver object index pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_position

      Deliver position pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_shadow

      Deliver shadow pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_subsurface_color

      Deliver subsurface color pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_subsurface_direct

      Deliver subsurface direct pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_subsurface_indirect

      Deliver subsurface indirect pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_transmission_color

      Deliver transmission color pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_transmission_direct

      Deliver transmission direct pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_transmission_indirect

      Deliver transmission indirect pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_uv

      Deliver texture UV pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_vector

      Deliver speed vector pass

      :type: boolean, default False, (readonly)

   .. data:: use_pass_z

      Deliver Z values pass

      :type: boolean, default False, (readonly)

   .. data:: use_sky

      Render Sky in this Layer

      :type: boolean, default False, (readonly)

   .. data:: use_solid

      Render Solid faces in this Layer

      :type: boolean, default False, (readonly)

   .. data:: use_strand

      Render Strands in this Layer

      :type: boolean, default False, (readonly)

   .. data:: use_volumes

      Render volumes in this Layer

      :type: boolean, default False, (readonly)

   .. method:: load_from_file(filepath, *, x=0, y=0)

      Copies the pixels of this renderlayer from an image file

      :arg filepath: File Path, File path to load into this render tile, must be no smaller than the renderlayer
      :type filepath: string, (never None)
      :arg x: Offset X, Offset the position to copy from if the image is larger than the render layer
      :type x: int in [0, inf], (optional)
      :arg y: Offset Y, Offset the position to copy from if the image is larger than the render layer
      :type y: int in [0, inf], (optional)

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

   * :class:`RenderResult.layers`

