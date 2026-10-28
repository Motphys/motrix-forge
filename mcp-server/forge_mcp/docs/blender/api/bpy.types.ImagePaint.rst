ImagePaint(Paint)
=================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Paint`

.. class:: ImagePaint(Paint)

   Properties of image and texture painting mode

   .. attribute:: canvas

      Image used as canvas

      :type: :class:`Image`

   .. attribute:: clone_alpha

      Opacity of clone image display

      :type: float in [0, 1], default 0.5

   .. attribute:: clone_image

      Image used as clone source

      :type: :class:`Image`

   .. attribute:: clone_offset

      :type: :class:`mathutils.Vector` of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: dither

      Amount of dithering when painting on byte images

      :type: float in [0, 2], default 0.0

   .. attribute:: interpolation

      Texture filtering type

      * ``LINEAR``
        Linear -- Linear interpolation.
      * ``CLOSEST``
        Closest -- No interpolation (sample closest texel).

      :type: enum in [``'LINEAR'``, ``'CLOSEST'``], default ``'LINEAR'``

   .. attribute:: invert_stencil

      Invert the stencil layer

      :type: boolean, default False

   .. data:: missing_materials

      The mesh is missing materials

      :type: boolean, default False, (readonly)

   .. data:: missing_stencil

      Image Painting does not have a stencil

      :type: boolean, default False, (readonly)

   .. data:: missing_texture

      Image Painting does not have a texture to paint on

      :type: boolean, default False, (readonly)

   .. data:: missing_uvs

      A UV layer is missing on the mesh

      :type: boolean, default False, (readonly)

   .. attribute:: mode

      Mode of operation for projection painting

      * ``MATERIAL``
        Material -- Detect image slots from the material.
      * ``IMAGE``
        Single Image -- Set image for texture painting directly.

      :type: enum in [``'MATERIAL'``, ``'IMAGE'``], default ``'MATERIAL'``

   .. attribute:: normal_angle

      Paint most on faces pointing towards the view according to this angle

      :type: int in [0, 90], default 80

   .. attribute:: screen_grab_size

      Size to capture the image for re-projecting

      :type: int array of 2 items in [512, 16384], default (0, 0)

   .. attribute:: seam_bleed

      Extend paint beyond the faces' UVs to reduce seams (in pixels, slower)

      :type: int in [-32768, 32767], default 2

   .. attribute:: stencil_color

      Stencil color in the viewport

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: stencil_image

      Image used as stencil

      :type: :class:`Image`

   .. attribute:: use_backface_culling

      Ignore faces pointing away from the view (faster)

      :type: boolean, default True

   .. attribute:: use_clone_layer

      Use another UV map as clone source, otherwise use the 3D cursor as the source

      :type: boolean, default False

   .. attribute:: use_normal_falloff

      Paint most on faces pointing towards the view

      :type: boolean, default True

   .. attribute:: use_occlude

      Only paint onto the faces directly under the brush (slower)

      :type: boolean, default True

   .. attribute:: use_stencil_layer

      Set the mask layer from the UV map buttons

      :type: boolean, default False

   .. method:: detect_data()

      Check if required texpaint data exist

      :rtype: boolean

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
   * :class:`Paint.brush`
   * :class:`Paint.brush_asset_reference`
   * :class:`Paint.eraser_brush`
   * :class:`Paint.eraser_brush_asset_reference`
   * :class:`Paint.palette`
   * :class:`Paint.show_brush`
   * :class:`Paint.show_brush_on_surface`
   * :class:`Paint.show_low_resolution`
   * :class:`Paint.use_sculpt_delay_updates`
   * :class:`Paint.use_symmetry_x`
   * :class:`Paint.use_symmetry_y`
   * :class:`Paint.use_symmetry_z`
   * :class:`Paint.use_symmetry_feather`
   * :class:`Paint.cavity_curve`
   * :class:`Paint.use_cavity`
   * :class:`Paint.tile_offset`
   * :class:`Paint.tile_x`
   * :class:`Paint.tile_y`
   * :class:`Paint.tile_z`

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
   * :class:`Paint.bl_rna_get_subclass`
   * :class:`Paint.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   * :class:`ToolSettings.image_paint`

