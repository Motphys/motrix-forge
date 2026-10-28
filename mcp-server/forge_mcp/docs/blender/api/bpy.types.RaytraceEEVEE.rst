RaytraceEEVEE(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RaytraceEEVEE(bpy_struct)

   Quality options for the raytracing pipeline

   .. attribute:: denoise_bilateral

      Blur the resolved radiance using a bilateral filter

      :type: boolean, default True

   .. attribute:: denoise_spatial

      Reuse neighbor pixels' rays

      :type: boolean, default True

   .. attribute:: denoise_temporal

      Accumulate samples by reprojecting last tracing results

      :type: boolean, default True

   .. attribute:: resolution_scale

      Determines the number of rays per pixel. Higher resolution uses more memory.

      * ``1``
        1:1 -- Full resolution.
      * ``2``
        1:2 -- Render this effect at 50% render resolution.
      * ``4``
        1:4 -- Render this effect at 25% render resolution.
      * ``8``
        1:8 -- Render this effect at 12.5% render resolution.
      * ``16``
        1:16 -- Render this effect at 6.25% render resolution.

      :type: enum in [``'1'``, ``'2'``, ``'4'``, ``'8'``, ``'16'``], default ``'2'``

   .. attribute:: screen_trace_quality

      Precision of the screen space ray-tracing

      :type: float in [0, 1], default 0.25

   .. attribute:: screen_trace_thickness

      Surface thickness used to detect intersection when using screen-tracing

      :type: float in [1e-06, inf], default 0.2

   .. attribute:: trace_max_roughness

      Maximum roughness to use the tracing pipeline for. Higher roughness surfaces will use fast GI approximation. A value of 1 will disable fast GI approximation.

      :type: float in [0, 1], default 0.5

   .. attribute:: use_denoise

      Enable noise reduction techniques for raytraced effects

      :type: boolean, default True

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

   * :class:`SceneEEVEE.ray_tracing_options`

