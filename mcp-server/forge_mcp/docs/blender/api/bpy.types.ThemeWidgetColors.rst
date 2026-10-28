ThemeWidgetColors(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeWidgetColors(bpy_struct)

   Theme settings for widget color sets

   .. attribute:: inner

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: inner_sel

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: item

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: outline

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: roundness

      Amount of edge rounding

      :type: float in [0, 1], default 0.0

   .. attribute:: shadedown

      :type: int in [-100, 100], default 0

   .. attribute:: shadetop

      :type: int in [-100, 100], default 0

   .. attribute:: show_shaded

      :type: boolean, default False

   .. attribute:: text

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: text_sel

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

   * :class:`ThemeUserInterface.wcol_box`
   * :class:`ThemeUserInterface.wcol_list_item`
   * :class:`ThemeUserInterface.wcol_menu`
   * :class:`ThemeUserInterface.wcol_menu_back`
   * :class:`ThemeUserInterface.wcol_menu_item`
   * :class:`ThemeUserInterface.wcol_num`
   * :class:`ThemeUserInterface.wcol_numslider`
   * :class:`ThemeUserInterface.wcol_option`
   * :class:`ThemeUserInterface.wcol_pie_menu`
   * :class:`ThemeUserInterface.wcol_progress`
   * :class:`ThemeUserInterface.wcol_pulldown`
   * :class:`ThemeUserInterface.wcol_radio`
   * :class:`ThemeUserInterface.wcol_regular`
   * :class:`ThemeUserInterface.wcol_scroll`
   * :class:`ThemeUserInterface.wcol_tab`
   * :class:`ThemeUserInterface.wcol_text`
   * :class:`ThemeUserInterface.wcol_toggle`
   * :class:`ThemeUserInterface.wcol_tool`
   * :class:`ThemeUserInterface.wcol_toolbar_item`
   * :class:`ThemeUserInterface.wcol_tooltip`

