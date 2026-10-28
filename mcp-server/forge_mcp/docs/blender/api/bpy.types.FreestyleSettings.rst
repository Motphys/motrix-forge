FreestyleSettings(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FreestyleSettings(bpy_struct)

   Freestyle settings for a ViewLayer data-block

   .. attribute:: as_render_pass

      Renders Freestyle output to a separate pass instead of overlaying it on the Combined pass

      :type: boolean, default False

   .. attribute:: crease_angle

      Angular threshold for detecting crease edges

      :type: float in [0, 3.14159], default 0.0

   .. attribute:: kr_derivative_epsilon

      Kr derivative epsilon for computing suggestive contours

      :type: float in [-1000, 1000], default 0.0

   .. data:: linesets

      :type: :class:`Linesets` :class:`bpy_prop_collection` of :class:`FreestyleLineSet`, (readonly)

   .. attribute:: mode

      Select the Freestyle control mode

      * ``SCRIPT``
        Python Scripting -- Advanced mode for using style modules written in Python.
      * ``EDITOR``
        Parameter Editor -- Basic mode for interactive style parameter editing.

      :type: enum in [``'SCRIPT'``, ``'EDITOR'``], default ``'SCRIPT'``

   .. data:: modules

      A list of style modules (to be applied from top to bottom)

      :type: :class:`FreestyleModules` :class:`bpy_prop_collection` of :class:`FreestyleModuleSettings`, (readonly)

   .. attribute:: sphere_radius

      Sphere radius for computing curvatures

      :type: float in [0, 1000], default 1.0

   .. attribute:: use_culling

      If enabled, out-of-view edges are ignored

      :type: boolean, default False

   .. attribute:: use_material_boundaries

      Enable material boundaries

      :type: boolean, default False

   .. attribute:: use_ridges_and_valleys

      Enable ridges and valleys

      :type: boolean, default False

   .. attribute:: use_smoothness

      Take face smoothness into account in view map calculation

      :type: boolean, default False

   .. attribute:: use_suggestive_contours

      Enable suggestive contours

      :type: boolean, default False

   .. attribute:: use_view_map_cache

      Keep the computed view map and avoid recalculating it if mesh geometry is unchanged

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

   * :class:`ViewLayer.freestyle_settings`

