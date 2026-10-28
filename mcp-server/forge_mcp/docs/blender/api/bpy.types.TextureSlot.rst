TextureSlot(bpy_struct)
=======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`BrushTextureSlot`, :class:`LineStyleTextureSlot`, :class:`ParticleSettingsTextureSlot`

.. class:: TextureSlot(bpy_struct)

   Texture slot defining the mapping and influence of a texture

   .. attribute:: blend_type

      Mode used to apply the texture

      :type: enum in [``'MIX'``, ``'DARKEN'``, ``'MULTIPLY'``, ``'LIGHTEN'``, ``'SCREEN'``, ``'ADD'``, ``'OVERLAY'``, ``'SOFT_LIGHT'``, ``'LINEAR_LIGHT'``, ``'DIFFERENCE'``, ``'SUBTRACT'``, ``'DIVIDE'``, ``'HUE'``, ``'SATURATION'``, ``'COLOR'``, ``'VALUE'``], default ``'MIX'``

   .. attribute:: color

      Default color for textures that don't return RGB or when RGB to intensity is enabled

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. attribute:: default_value

      Value to use for Ref, Spec, Amb, Emit, Alpha, RayMir, TransLu and Hard

      :type: float in [-inf, inf], default 1.0

   .. data:: name

      Texture slot name

      :type: string, default "", (readonly, never None)

   .. attribute:: offset

      Fine tune of the texture mapping X, Y and Z locations

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: output_node

      Which output node to use, for node-based textures

      :type: enum in [``'DEFAULT'``], default ``'DEFAULT'``

   .. attribute:: scale

      Set scaling for the texture's X, Y and Z sizes

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (1.0, 1.0, 1.0)

   .. attribute:: texture

      Texture data-block used by this texture slot

      :type: :class:`Texture`

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

   * :mod:`bpy.context.texture_slot`
   * :class:`UILayout.template_preview`

