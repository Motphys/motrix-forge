ThemeSpaceGradient(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeSpaceGradient(bpy_struct)


   .. attribute:: button

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: button_text

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: button_text_hi

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: button_title

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: execution_buts

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. data:: gradients

      :type: :class:`ThemeGradientColors`, (readonly, never None)

   .. attribute:: header

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: header_text

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: header_text_hi

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: navigation_bar

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. data:: panelcolors

      :type: :class:`ThemePanelColors`, (readonly, never None)

   .. attribute:: tab_active

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: tab_back

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: tab_inactive

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: tab_outline

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: text

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: text_hi

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: title

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

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

   * :class:`ThemeView3D.space`

