Panel(bpy_struct)
=================

.. currentmodule:: bpy.types


Basic Panel Example
+++++++++++++++++++

This script is a simple panel which will draw into the object properties
section.

Notice the 'CATEGORY_PT_name' :class:`Panel.bl_idname`, this is a naming
convention for panels.

.. note::

   Panel subclasses must be registered for Blender to use them.

.. literalinclude:: ..\examples\bpy.types.Panel.py
   :lines: 15-


Simple Object Panel
+++++++++++++++++++

This panel has a :class:`Panel.poll` and :class:`Panel.draw_header` function,
even though the contents is basic this closely resembles blenders panels.

.. literalinclude:: ..\examples\bpy.types.Panel.1.py
   :lines: 8-


Mix-in Classes
++++++++++++++
A mix-in parent class can be used to share common properties and
:class:`Menu.poll` function.

.. literalinclude:: ..\examples\bpy.types.Panel.2.py
   :lines: 7-

base class --- :class:`bpy_struct`

.. class:: Panel(bpy_struct)

   Panel containing UI elements

   .. attribute:: bl_category

      The category (tab) in which the panel will be displayed, when applicable

      :type: string, default "", (never None)

   .. attribute:: bl_context

      The context in which the panel belongs to. (TODO: explain the possible combinations bl_context/bl_region_type/bl_space_type)

      :type: string, default "", (never None)

   .. attribute:: bl_description

      The panel tooltip

      :type: string, default ""

   .. attribute:: bl_idname

      If this is set, the panel gets a custom ID, otherwise it takes the name of the class used to define the panel. For example, if the class name is "OBJECT_PT_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_PT_hello".

      :type: string, default "", (never None)

   .. attribute:: bl_label

      The panel label, shows up in the panel header at the right of the triangle used to collapse the panel

      :type: string, default "", (never None)

   .. attribute:: bl_options

      Options for this panel type

      * ``DEFAULT_CLOSED``
        Default Closed -- Defines if the panel has to be open or collapsed at the time of its creation.
      * ``HIDE_HEADER``
        Hide Header -- If set to False, the panel shows a header, which contains a clickable arrow to collapse the panel and the label (see bl_label).
      * ``INSTANCED``
        Instanced Panel -- Multiple panels with this type can be used as part of a list depending on data external to the UI. Used to create panels for the modifiers and other stacks..
      * ``HEADER_LAYOUT_EXPAND``
        Expand Header Layout -- Allow buttons in the header to stretch and shrink to fill the entire layout width.

      :type: enum set in {``'DEFAULT_CLOSED'``, ``'HIDE_HEADER'``, ``'INSTANCED'``, ``'HEADER_LAYOUT_EXPAND'``}, default {``'DEFAULT_CLOSED'``}

   .. attribute:: bl_order

      Panels with lower numbers are default ordered before panels with higher numbers

      :type: int in [0, inf], default 0

   .. attribute:: bl_owner_id

      The ID owning the data displayed in the panel, if any

      :type: string, default "", (never None)

   .. attribute:: bl_parent_id

      If this is set, the panel becomes a sub-panel

      :type: string, default "", (never None)

   .. attribute:: bl_region_type

      The region where the panel is going to be used in

      :type: enum in :ref:`rna_enum_region_type_items`, default ``'WINDOW'``

   .. attribute:: bl_space_type

      The space where the panel is going to be used in

      :type: enum in :ref:`rna_enum_space_type_items`, default ``'EMPTY'``

   .. attribute:: bl_translation_context

      Specific translation context, only define when the label needs to be disambiguated from others using the exact same label

      :type: string, default "*", (never None)

   .. attribute:: bl_ui_units_x

      When set, defines popup panel width

      :type: int in [0, inf], default 0

   .. data:: custom_data

      Panel data

      :type: :class:`Constraint`, (readonly)

   .. data:: is_popover

      :type: boolean, default False, (readonly)

   .. data:: layout

      Defines the structure of the panel in the UI

      :type: :class:`UILayout`, (readonly)

   .. attribute:: text

      XXX todo

      :type: string, default "", (never None)

   .. attribute:: use_pin

      Show the panel on all tabs

      :type: boolean, default False

   .. classmethod:: poll(context)

      If this method returns a non-null output, then the panel can be drawn

      :type context: :class:`Context`, (never None)
      :rtype: boolean

   .. method:: draw(context)

      Draw UI elements into the panel UI layout

      :type context: :class:`Context`, (never None)

   .. method:: draw_header(context)

      Draw UI elements into the panel's header UI layout

      :type context: :class:`Context`, (never None)

   .. method:: draw_header_preset(context)

      Draw UI elements for presets in the panel's header

      :type context: :class:`Context`, (never None)

   .. classmethod:: append(draw_func)

      Append a draw function to this menu,
      takes the same arguments as the menus draw function

   .. classmethod:: is_extended()

   .. classmethod:: prepend(draw_func)

      Prepend a draw function to this menu, takes the same arguments as
      the menus draw function

   .. classmethod:: remove(draw_func)

      Remove a draw function that has been added to this menu

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

