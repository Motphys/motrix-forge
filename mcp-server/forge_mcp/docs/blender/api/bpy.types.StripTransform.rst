StripTransform(bpy_struct)
==========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: StripTransform(bpy_struct)

   Transform parameters for a sequence strip

   .. attribute:: filter

      Type of filter to use for image transformation

      * ``AUTO``
        Auto -- Automatically choose filter based on scaling factor.
      * ``NEAREST``
        Nearest -- Use nearest sample.
      * ``BILINEAR``
        Bilinear -- Interpolate between 2×2 samples.
      * ``CUBIC_MITCHELL``
        Cubic Mitchell -- Cubic Mitchell filter on 4×4 samples.
      * ``CUBIC_BSPLINE``
        Cubic B-Spline -- Cubic B-Spline filter (blurry but no ringing) on 4×4 samples.
      * ``BOX``
        Box -- Averages source image samples that fall under destination pixel.

      :type: enum in [``'AUTO'``, ``'NEAREST'``, ``'BILINEAR'``, ``'CUBIC_MITCHELL'``, ``'CUBIC_BSPLINE'``, ``'BOX'``], default ``'AUTO'``

   .. attribute:: offset_x

      Move along X axis

      :type: float in [-inf, inf], default 0.0

   .. attribute:: offset_y

      Move along Y axis

      :type: float in [-inf, inf], default 0.0

   .. attribute:: origin

      Origin of image for transformation

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: rotation

      Rotate around image center

      :type: float in [-inf, inf], default 0.0

   .. attribute:: scale_x

      Scale along X axis

      :type: float in [0, inf], default 1.0

   .. attribute:: scale_y

      Scale along Y axis

      :type: float in [0, inf], default 1.0

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

   * :class:`EffectStrip.transform`
   * :class:`ImageStrip.transform`
   * :class:`MaskStrip.transform`
   * :class:`MetaStrip.transform`
   * :class:`MovieClipStrip.transform`
   * :class:`MovieStrip.transform`
   * :class:`SceneStrip.transform`

