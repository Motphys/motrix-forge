ThemeUserInterface(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeUserInterface(bpy_struct)

   Theme settings for user interface elements

   .. attribute:: axis_x

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: axis_y

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: axis_z

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: editor_border

      Color of the border between editors

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: editor_outline

      Color of the outline of each editor, except the active one

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: editor_outline_active

      Color of the outline of the active editor

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: gizmo_a

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gizmo_b

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gizmo_hi

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gizmo_primary

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gizmo_secondary

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gizmo_view_align

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: icon_alpha

      Transparency of icons in the interface, to reduce contrast

      :type: float in [0, 1], default 0.0

   .. attribute:: icon_autokey

      Color of Auto Keying indicator when enabled

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: icon_border_intensity

      Control the intensity of the border around themes icons

      :type: float in [0, 1], default 0.0

   .. attribute:: icon_collection

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: icon_folder

      Color of folders in the file browser

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: icon_modifier

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: icon_object

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: icon_object_data

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: icon_saturation

      Saturation of icons in the interface

      :type: float in [0, 1], default 0.0

   .. attribute:: icon_scene

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: icon_shading

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: menu_shadow_fac

      Blending factor for menu shadows

      :type: float in [0.01, 1], default 0.0

   .. attribute:: menu_shadow_width

      Width of menu shadows, set to zero to disable

      :type: int in [0, 24], default 0

   .. attribute:: panel_roundness

      Roundness of the corners of panels and sub-panels

      :type: float in [0, 1], default 0.4

   .. attribute:: transparent_checker_primary

      Primary color of checkerboard pattern indicating transparent areas

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: transparent_checker_secondary

      Secondary color of checkerboard pattern indicating transparent areas

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: transparent_checker_size

      Size of checkerboard pattern indicating transparent areas

      :type: int in [2, 48], default 0

   .. data:: wcol_box

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_list_item

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_menu

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_menu_back

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_menu_item

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_num

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_numslider

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_option

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_pie_menu

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_progress

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_pulldown

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_radio

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_regular

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_scroll

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_state

      :type: :class:`ThemeWidgetStateColors`, (readonly, never None)

   .. data:: wcol_tab

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_text

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_toggle

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_tool

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_toolbar_item

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. data:: wcol_tooltip

      :type: :class:`ThemeWidgetColors`, (readonly, never None)

   .. attribute:: widget_emboss

      Color of the 1px shadow line underlying widgets

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: widget_text_cursor

      Color of the text insertion cursor (caret)

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

   * :class:`Theme.user_interface`

