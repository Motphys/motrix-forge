UILayout(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UILayout(bpy_struct)

   User interface layout in a panel or header

   .. attribute:: activate_init

      When true, buttons defined in popups will be activated on first display (use so you can type into a field without having to click on it first)

      :type: boolean, default False

   .. attribute:: active

      :type: boolean, default False

   .. attribute:: active_default

      When true, an operator button defined after this will be activated when pressing return(use with popup dialogs)

      :type: boolean, default False

   .. attribute:: alert

      :type: boolean, default False

   .. attribute:: alignment

      :type: enum in [``'EXPAND'``, ``'LEFT'``, ``'CENTER'``, ``'RIGHT'``], default ``'EXPAND'``

   .. data:: direction

      :type: enum in [``'HORIZONTAL'``, ``'VERTICAL'``], default ``'HORIZONTAL'``, (readonly)

   .. attribute:: emboss

      * ``NORMAL``
        Regular -- Draw standard button emboss style.
      * ``NONE``
        None -- Draw only text and icons.
      * ``PULLDOWN_MENU``
        Pull-down Menu -- Draw pull-down menu style.
      * ``RADIAL_MENU``
        Pie Menu -- Draw radial menu style.
      * ``NONE_OR_STATUS``
        None or Status -- Draw with no emboss unless the button has a coloring status like an animation state.

      :type: enum in [``'NORMAL'``, ``'NONE'``, ``'PULLDOWN_MENU'``, ``'RADIAL_MENU'``, ``'NONE_OR_STATUS'``], default ``'NORMAL'``

   .. attribute:: enabled

      When false, this (sub)layout is grayed out

      :type: boolean, default False

   .. attribute:: operator_context

      Typically set to 'INVOKE_REGION_WIN', except some cases in :class:`bpy.types.Menu` when it's set to 'EXEC_REGION_WIN'.

      :type: enum in :ref:`rna_enum_operator_context_items`, default ``'INVOKE_DEFAULT'``

   .. attribute:: scale_x

      Scale factor along the X for items in this (sub)layout

      :type: float in [0, inf], default 0.0

   .. attribute:: scale_y

      Scale factor along the Y for items in this (sub)layout

      :type: float in [0, inf], default 0.0

   .. attribute:: ui_units_x

      Fixed size along the X for items in this (sub)layout

      :type: float in [0, inf], default 0.0

   .. attribute:: ui_units_y

      Fixed size along the Y for items in this (sub)layout

      :type: float in [0, inf], default 0.0

   .. attribute:: use_property_decorate

      :type: boolean, default False

   .. attribute:: use_property_split

      :type: boolean, default False

   .. method:: row(*, align=False, heading="", heading_ctxt="", translate=True)

      Sub-layout. Items placed in this sublayout are placed next to each other in a row.

      :arg align: Align buttons to each other
      :type align: boolean, (optional)
      :arg heading: Heading, Label to insert into the layout for this sub-layout
      :type heading: string, (optional, never None)
      :arg heading_ctxt: Override automatic translation context of the given heading
      :type heading_ctxt: string, (optional, never None)
      :arg translate: Translate the given heading, when UI translation is enabled
      :type translate: boolean, (optional)
      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. method:: column(*, align=False, heading="", heading_ctxt="", translate=True)

      Sub-layout. Items placed in this sublayout are placed under each other in a column.

      :arg align: Align buttons to each other
      :type align: boolean, (optional)
      :arg heading: Heading, Label to insert into the layout for this sub-layout
      :type heading: string, (optional, never None)
      :arg heading_ctxt: Override automatic translation context of the given heading
      :type heading_ctxt: string, (optional, never None)
      :arg translate: Translate the given heading, when UI translation is enabled
      :type translate: boolean, (optional)
      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. method:: panel(idname, *, default_closed=False)

      Creates a collapsable panel. Whether it is open or closed is stored in the region using the given idname. This can only be used when the panel has the full width of the panel region available to it. So it can't be used in e.g. in a box or columns.

      :arg idname: Identifier of the panel
      :type idname: string, (never None)
      :arg default_closed: Open by Default, When true, the panel will be open the first time it is shown
      :type default_closed: boolean, (optional)
      :return:
         `layout_header`, Sub-layout to put items in, :class:`UILayout`

         `layout_body`, Sub-layout to put items in. Will be none if the panel is collapsed., :class:`UILayout`

      :rtype: (:class:`UILayout`, :class:`UILayout`)

   .. method:: panel_prop(data, property)

      Similar to `.panel(...)` but instead of storing whether it is open or closed in the region, it is stored in the provided boolean property. This should be used when multiple instances of the same panel can exist. For example one for every item in a collection property or list. This can only be used when the panel has the full width of the panel region available to it. So it can't be used in e.g. in a box or columns.

      :arg data: Data from which to take the open-state property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of the boolean property that determines whether the panel is open or closed
      :type property: string, (never None)
      :return:
         `layout_header`, Sub-layout to put items in, :class:`UILayout`

         `layout_body`, Sub-layout to put items in. Will be none if the panel is collapsed., :class:`UILayout`

      :rtype: (:class:`UILayout`, :class:`UILayout`)

   .. method:: column_flow(*, columns=0, align=False)

      column_flow

      :arg columns: Number of columns, 0 is automatic
      :type columns: int in [0, inf], (optional)
      :arg align: Align buttons to each other
      :type align: boolean, (optional)
      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. method:: grid_flow(*, row_major=False, columns=0, even_columns=False, even_rows=False, align=False)

      grid_flow

      :arg row_major: Fill row by row, instead of column by column
      :type row_major: boolean, (optional)
      :arg columns: Number of columns, positive are absolute fixed numbers, 0 is automatic, negative are automatic multiple numbers along major axis (e.g. -2 will only produce 2, 4, 6 etc. columns for row major layout, and 2, 4, 6 etc. rows for column major layout).
      :type columns: int in [-inf, inf], (optional)
      :arg even_columns: All columns will have the same width
      :type even_columns: boolean, (optional)
      :arg even_rows: All rows will have the same height
      :type even_rows: boolean, (optional)
      :arg align: Align buttons to each other
      :type align: boolean, (optional)
      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. method:: box()

      Sublayout (items placed in this sublayout are placed under each other in a column and are surrounded by a box)

      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. method:: split(*, factor=0.0, align=False)

      split

      :arg factor: Percentage, Percentage of width to split at (leave unset for automatic calculation)
      :type factor: float in [0, 1], (optional)
      :arg align: Align buttons to each other
      :type align: boolean, (optional)
      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. method:: menu_pie()

      Sublayout. Items placed in this sublayout are placed in a radial fashion around the menu center).

      :return: Sub-layout to put items in
      :rtype: :class:`UILayout`

   .. classmethod:: icon(data)

      Return the custom icon for this data, use it e.g. to get materials or texture icons.

      :arg data: Data from which to take the icon
      :type data: :class:`AnyType`, (never None)
      :return: Icon identifier
      :rtype: int in [0, inf]

   .. classmethod:: enum_item_name(data, property, identifier)

      Return the UI name for this enum item

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg identifier: Identifier of the enum item
      :type identifier: string, (never None)
      :return: UI name of the enum item
      :rtype: string, (never None)

   .. classmethod:: enum_item_description(data, property, identifier)

      Return the UI description for this enum item

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg identifier: Identifier of the enum item
      :type identifier: string, (never None)
      :return: UI description of the enum item
      :rtype: string, (never None)

   .. classmethod:: enum_item_icon(data, property, identifier)

      Return the icon for this enum item

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg identifier: Identifier of the enum item
      :type identifier: string, (never None)
      :return: Icon identifier
      :rtype: int in [0, inf]

   .. method:: prop(data, property, *, text="", text_ctxt="", translate=True, icon='NONE', placeholder="", expand=False, slider=False, toggle=-1, icon_only=False, event=False, full_event=False, emboss=True, index=-1, icon_value=0, invert_checkbox=False)

      Item. Exposes an RNA item and places it into the layout.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)
      :arg placeholder: Hint describing the expected value when empty
      :type placeholder: string, (optional)
      :arg expand: Expand button to show more detail
      :type expand: boolean, (optional)
      :arg slider: Use slider widget for numeric values
      :type slider: boolean, (optional)
      :arg toggle: Use toggle widget for boolean values, or a checkbox when disabled (the default is -1 which uses toggle only when an icon is displayed)
      :type toggle: int in [-1, 1], (optional)
      :arg icon_only: Draw only icons in buttons, no text
      :type icon_only: boolean, (optional)
      :arg event: Use button to input key events
      :type event: boolean, (optional)
      :arg full_event: Use button to input full events including modifiers
      :type full_event: boolean, (optional)
      :arg emboss: Draw the button itself, not just the icon/text. When false, corresponds to the 'NONE_OR_STATUS' layout emboss type.
      :type emboss: boolean, (optional)
      :arg index: The index of this button, when set a single member of an array can be accessed, when set to -1 all array members are used
      :type index: int in [-2, inf], (optional)
      :arg icon_value: Icon Value, Override automatic icon of the item
      :type icon_value: int in [0, inf], (optional)
      :arg invert_checkbox: Draw checkbox value inverted
      :type invert_checkbox: boolean, (optional)

   .. method:: props_enum(data, property)

      props_enum

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: prop_menu_enum(data, property, *, text="", text_ctxt="", translate=True, icon='NONE')

      prop_menu_enum

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)

   .. method:: prop_with_popover(data, property, *, text="", text_ctxt="", translate=True, icon='NONE', icon_only=False, panel)

      prop_with_popover

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)
      :arg icon_only: Draw only icons in tabs, no text
      :type icon_only: boolean, (optional)
      :arg panel: Identifier of the panel
      :type panel: string, (never None)

   .. method:: prop_with_menu(data, property, *, text="", text_ctxt="", translate=True, icon='NONE', icon_only=False, menu)

      prop_with_menu

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)
      :arg icon_only: Draw only icons in tabs, no text
      :type icon_only: boolean, (optional)
      :arg menu: Identifier of the menu
      :type menu: string, (never None)

   .. method:: prop_tabs_enum(data, property, *, data_highlight=None, property_highlight="", icon_only=False)

      prop_tabs_enum

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg data_highlight: Data from which to take highlight property
      :type data_highlight: :class:`AnyType`, (optional, never None)
      :arg property_highlight: Identifier of highlight property in data
      :type property_highlight: string, (optional, never None)
      :arg icon_only: Draw only icons in tabs, no text
      :type icon_only: boolean, (optional)

   .. method:: prop_enum(data, property, value, *, text="", text_ctxt="", translate=True, icon='NONE')

      prop_enum

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg value: Enum property value
      :type value: string, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)

   .. method:: prop_search(data, property, search_data, search_property, *, text="", text_ctxt="", translate=True, icon='NONE', results_are_suggestions=False)

      prop_search

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg search_data: Data from which to take collection to search in
      :type search_data: :class:`AnyType`, (never None)
      :arg search_property: Identifier of search collection property
      :type search_property: string, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)
      :arg results_are_suggestions: Accept inputs that do not match any item
      :type results_are_suggestions: boolean, (optional)

   .. method:: prop_decorator(data, property, *, index=-1)

      prop_decorator

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg index: The index of this button, when set a single member of an array can be accessed, when set to -1 all array members are used
      :type index: int in [-2, inf], (optional)

   .. method:: operator(operator, *, text="", text_ctxt="", translate=True, icon='NONE', emboss=True, depress=False, icon_value=0, search_weight=0.0)

      Item. Places a button into the layout to call an Operator.

      :arg operator: Identifier of the operator
      :type operator: string, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)
      :arg emboss: Draw the button itself, not just the icon/text
      :type emboss: boolean, (optional)
      :arg depress: Draw pressed in
      :type depress: boolean, (optional)
      :arg icon_value: Icon Value, Override automatic icon of the item
      :type icon_value: int in [0, inf], (optional)
      :arg search_weight: Search Weight, Influences the sorting when using menu-seach
      :type search_weight: float in [-inf, inf], (optional)
      :return: Operator properties to fill in
      :rtype: :class:`OperatorProperties`

   .. method:: operator_menu_hold(operator, *, text="", text_ctxt="", translate=True, icon='NONE', emboss=True, depress=False, icon_value=0, menu)

      Item. Places a button into the layout to call an Operator.

      :arg operator: Identifier of the operator
      :type operator: string, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)
      :arg emboss: Draw the button itself, not just the icon/text
      :type emboss: boolean, (optional)
      :arg depress: Draw pressed in
      :type depress: boolean, (optional)
      :arg icon_value: Icon Value, Override automatic icon of the item
      :type icon_value: int in [0, inf], (optional)
      :arg menu: Identifier of the menu
      :type menu: string, (never None)
      :return: Operator properties to fill in
      :rtype: :class:`OperatorProperties`

   .. method:: operator_enum(operator, property, *, icon_only=False)

      operator_enum

      :arg operator: Identifier of the operator
      :type operator: string, (never None)
      :arg property: Identifier of property in operator
      :type property: string, (never None)
      :arg icon_only: Draw only icons in buttons, no text
      :type icon_only: boolean, (optional)

   .. method:: operator_menu_enum(operator, property, *, text="", text_ctxt="", translate=True, icon='NONE')

      operator_menu_enum

      :arg operator: Identifier of the operator
      :type operator: string, (never None)
      :arg property: Identifier of property in operator
      :type property: string, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)
      :return: Operator properties to fill in
      :rtype: :class:`OperatorProperties`

   .. method:: label(*, text="", text_ctxt="", translate=True, icon='NONE', icon_value=0)

      Item. Displays text and/or icon in the layout.

      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)
      :arg icon_value: Icon Value, Override automatic icon of the item
      :type icon_value: int in [0, inf], (optional)

   .. method:: menu(menu, *, text="", text_ctxt="", translate=True, icon='NONE', icon_value=0)

      menu

      :arg menu: Identifier of the menu
      :type menu: string, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)
      :arg icon_value: Icon Value, Override automatic icon of the item
      :type icon_value: int in [0, inf], (optional)

   .. method:: menu_contents(menu)

      menu_contents

      :arg menu: Identifier of the menu
      :type menu: string, (never None)

   .. method:: popover(panel, *, text="", text_ctxt="", translate=True, icon='NONE', icon_value=0)

      popover

      :arg panel: Identifier of the panel
      :type panel: string, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)
      :arg icon_value: Icon Value, Override automatic icon of the item
      :type icon_value: int in [0, inf], (optional)

   .. method:: popover_group(space_type, region_type, context, category)

      popover_group

      :arg space_type: Space Type
      :type space_type: enum in :ref:`rna_enum_space_type_items`
      :arg region_type: Region Type
      :type region_type: enum in :ref:`rna_enum_region_type_items`
      :arg context: panel type context
      :type context: string, (never None)
      :arg category: panel type category
      :type category: string, (never None)

   .. method:: separator(*, factor=1.0, type='AUTO')

      Item. Inserts empty space into the layout between items.

      :arg factor: Percentage, Percentage of width to space (leave unset for default space)
      :type factor: float in [0, inf], (optional)
      :arg type: Type, The type of the separator

         * ``AUTO``
           Auto -- Best guess at what type of separator is needed..
         * ``SPACE``
           Empty space -- Horizontal or Vertical empty space, depending on layout direction..
         * ``LINE``
           Line -- Horizontal or Vertical line, depending on layout direction..
      :type type: enum in [``'AUTO'``, ``'SPACE'``, ``'LINE'``], (optional)

   .. method:: separator_spacer()

      Item. Inserts horizontal spacing empty space into the layout between items.


   .. method:: progress(*, text="", text_ctxt="", translate=True, factor=0.0, type='BAR')

      Progress indicator

      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg factor: Factor, Amount of progress from 0.0f to 1.0f
      :type factor: float in [0, 1], (optional)
      :arg type: Type, The type of progress indicator
      :type type: enum in [``'BAR'``, ``'RING'``], (optional)

   .. method:: context_pointer_set(name, data)

      context_pointer_set

      :arg name: Name, Name of entry in the context
      :type name: string, (never None)
      :arg data: Pointer to put in context
      :type data: :class:`AnyType`

   .. method:: context_string_set(name, value)

      context_string_set

      :arg name: Name, Name of entry in the context
      :type name: string, (never None)
      :arg value: Value, String to put in context
      :type value: string, (never None)

   .. method:: template_header()

      Inserts common Space header UI (editor type selector)


   .. method:: template_ID(data, property, *, new="", open="", unlink="", filter='ALL', live_icon=False, text="", text_ctxt="", translate=True)

      template_ID

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg new: Operator identifier to create a new ID block
      :type new: string, (optional, never None)
      :arg open: Operator identifier to open a file for creating a new ID block
      :type open: string, (optional, never None)
      :arg unlink: Operator identifier to unlink the ID block
      :type unlink: string, (optional, never None)
      :arg filter: Optionally limit the items which can be selected
      :type filter: enum in [``'ALL'``, ``'AVAILABLE'``], (optional)
      :arg live_icon: Show preview instead of fixed icon
      :type live_icon: boolean, (optional)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)

   .. method:: template_ID_preview(data, property, *, new="", open="", unlink="", rows=0, cols=0, filter='ALL', hide_buttons=False)

      template_ID_preview

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg new: Operator identifier to create a new ID block
      :type new: string, (optional, never None)
      :arg open: Operator identifier to open a file for creating a new ID block
      :type open: string, (optional, never None)
      :arg unlink: Operator identifier to unlink the ID block
      :type unlink: string, (optional, never None)
      :arg rows: Number of thumbnail preview rows to display
      :type rows: int in [0, inf], (optional)
      :arg cols: Number of thumbnail preview columns to display
      :type cols: int in [0, inf], (optional)
      :arg filter: Optionally limit the items which can be selected
      :type filter: enum in [``'ALL'``, ``'AVAILABLE'``], (optional)
      :arg hide_buttons: Show only list, no buttons
      :type hide_buttons: boolean, (optional)

   .. method:: template_any_ID(data, property, type_property, *, text="", text_ctxt="", translate=True)

      template_any_ID

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg type_property: Identifier of property in data giving the type of the ID-blocks to use
      :type type_property: string, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)

   .. method:: template_ID_tabs(data, property, *, new="", menu="", filter='ALL')

      template_ID_tabs

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg new: Operator identifier to create a new ID block
      :type new: string, (optional, never None)
      :arg menu: Context menu identifier
      :type menu: string, (optional, never None)
      :arg filter: Optionally limit the items which can be selected
      :type filter: enum in [``'ALL'``, ``'AVAILABLE'``], (optional)

   .. method:: template_action(id, *, new="", unlink="", text="", text_ctxt="", translate=True)

      template_action

      :arg id: The data-block for which to select an Action
      :type id: :class:`ID`, (never None)
      :arg new: Operator identifier to create a new ID block
      :type new: string, (optional, never None)
      :arg unlink: Operator identifier to unlink the ID block
      :type unlink: string, (optional, never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)

   .. method:: template_search(data, property, search_data, search_property, *, new="", unlink="", text="", text_ctxt="", translate=True)

      template_search

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg search_data: Data from which to take collection to search in
      :type search_data: :class:`AnyType`, (never None)
      :arg search_property: Identifier of search collection property
      :type search_property: string, (never None)
      :arg new: Operator identifier to create a new item for the collection
      :type new: string, (optional, never None)
      :arg unlink: Operator identifier to unlink or delete the active item from the collection
      :type unlink: string, (optional, never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)

   .. method:: template_search_preview(data, property, search_data, search_property, *, new="", unlink="", text="", text_ctxt="", translate=True, rows=0, cols=0)

      template_search_preview

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg search_data: Data from which to take collection to search in
      :type search_data: :class:`AnyType`, (never None)
      :arg search_property: Identifier of search collection property
      :type search_property: string, (never None)
      :arg new: Operator identifier to create a new item for the collection
      :type new: string, (optional, never None)
      :arg unlink: Operator identifier to unlink or delete the active item from the collection
      :type unlink: string, (optional, never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg rows: Number of thumbnail preview rows to display
      :type rows: int in [0, inf], (optional)
      :arg cols: Number of thumbnail preview columns to display
      :type cols: int in [0, inf], (optional)

   .. method:: template_path_builder(data, property, root, *, text="", text_ctxt="", translate=True)

      template_path_builder

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg root: ID-block from which path is evaluated from
      :type root: :class:`ID`
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)

   .. method:: template_modifiers()

      Generates the UI layout for the modifier stack


   .. method:: template_collection_exporters()

      Generates the UI layout for collection exporters


   .. method:: template_constraints(*, use_bone_constraints=True)

      Generates the panels for the constraint stack

      :arg use_bone_constraints: Add panels for bone constraints instead of object constraints
      :type use_bone_constraints: boolean, (optional)

   .. method:: template_shaderfx()

      Generates the panels for the shader effect stack


   .. method:: template_greasepencil_color(data, property, *, rows=0, cols=0, scale=1.0, filter='ALL')

      template_greasepencil_color

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg rows: Number of thumbnail preview rows to display
      :type rows: int in [0, inf], (optional)
      :arg cols: Number of thumbnail preview columns to display
      :type cols: int in [0, inf], (optional)
      :arg scale: Scale of the image thumbnails
      :type scale: float in [0.1, 1.5], (optional)
      :arg filter: Optionally limit the items which can be selected
      :type filter: enum in [``'ALL'``, ``'AVAILABLE'``], (optional)

   .. method:: template_constraint_header(data)

      Generates the header for constraint panels

      :arg data: Constraint data
      :type data: :class:`Constraint`, (never None)

   .. method:: template_preview(id, *, show_buttons=True, parent=None, slot=None, preview_id="")

      Item. A preview window for materials, textures, lights or worlds.

      :arg id: ID data-block
      :type id: :class:`ID`
      :arg show_buttons: Show preview buttons?
      :type show_buttons: boolean, (optional)
      :arg parent: ID data-block
      :type parent: :class:`ID`, (optional)
      :arg slot: Texture slot
      :type slot: :class:`TextureSlot`, (optional)
      :arg preview_id: Identifier of this preview widget, if not set the ID type will be used (i.e. all previews of materials without explicit ID will have the same size...).
      :type preview_id: string, (optional, never None)

   .. method:: template_curve_mapping(data, property, *, type='NONE', levels=False, brush=False, use_negative_slope=False, show_tone=False)

      Item. A curve mapping widget used for e.g falloff curves for lights.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg type: Type, Type of curves to display
      :type type: enum in [``'NONE'``, ``'VECTOR'``, ``'COLOR'``, ``'HUE'``], (optional)
      :arg levels: Show black/white levels
      :type levels: boolean, (optional)
      :arg brush: Show brush options
      :type brush: boolean, (optional)
      :arg use_negative_slope: Use a negative slope by default
      :type use_negative_slope: boolean, (optional)
      :arg show_tone: Show tone options
      :type show_tone: boolean, (optional)

   .. method:: template_curveprofile(data, property)

      A profile path editor used for custom profiles

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: template_color_ramp(data, property, *, expand=False)

      Item. A color ramp widget.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg expand: Expand button to show more detail
      :type expand: boolean, (optional)

   .. method:: template_icon(icon_value, *, scale=1.0)

      Display a large icon

      :arg icon_value: Icon to display
      :type icon_value: int in [0, inf]
      :arg scale: Scale, Scale the icon size (by the button size)
      :type scale: float in [1, 100], (optional)

   .. method:: template_icon_view(data, property, *, show_labels=False, scale=6.0, scale_popup=5.0)

      Enum. Large widget showing Icon previews.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg show_labels: Show enum label in preview buttons
      :type show_labels: boolean, (optional)
      :arg scale: UI Units, Scale the button icon size (by the button size)
      :type scale: float in [1, 100], (optional)
      :arg scale_popup: Scale, Scale the popup icon size (by the button size)
      :type scale_popup: float in [1, 100], (optional)

   .. method:: template_histogram(data, property)

      Item. A histogramm widget to analyze imaga data.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: template_waveform(data, property)

      Item. A waveform widget to analyze imaga data.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: template_vectorscope(data, property)

      Item. A vectorscope widget to analyze imaga data.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: template_layers(data, property, used_layers_data, used_layers_property, active_layer)

      template_layers

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg used_layers_data: Data from which to take property
      :type used_layers_data: :class:`AnyType`
      :arg used_layers_property: Identifier of property in data
      :type used_layers_property: string, (never None)
      :arg active_layer: Active Layer
      :type active_layer: int in [0, inf]

   .. method:: template_color_picker(data, property, *, value_slider=False, lock=False, lock_luminosity=False, cubic=False)

      Item. A color wheel widget to pick colors.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg value_slider: Display the value slider to the right of the color wheel
      :type value_slider: boolean, (optional)
      :arg lock: Lock the color wheel display to value 1.0 regardless of actual color
      :type lock: boolean, (optional)
      :arg lock_luminosity: Keep the color at its original vector length
      :type lock_luminosity: boolean, (optional)
      :arg cubic: Cubic saturation for picking values close to white
      :type cubic: boolean, (optional)

   .. method:: template_palette(data, property, *, color=False)

      Item. A palette used to pick colors.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg color: Display the colors as colors or values
      :type color: boolean, (optional)

   .. method:: template_image_layers(image, image_user)

      template_image_layers

      :type image: :class:`Image`
      :type image_user: :class:`ImageUser`

   .. method:: template_image(data, property, image_user, *, compact=False, multiview=False)

      Item(s). User interface for selecting images and their source paths.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :type image_user: :class:`ImageUser`, (never None)
      :arg compact: Use more compact layout
      :type compact: boolean, (optional)
      :arg multiview: Expose Multi-View options
      :type multiview: boolean, (optional)

   .. method:: template_image_settings(image_settings, *, color_management=False)

      User interface for setting image format options

      :type image_settings: :class:`ImageFormatSettings`, (never None)
      :arg color_management: Show color management settings
      :type color_management: boolean, (optional)

   .. method:: template_image_stereo_3d(stereo_3d_format)

      User interface for setting image stereo 3d options

      :type stereo_3d_format: :class:`Stereo3dFormat`, (never None)

   .. method:: template_image_views(image_settings)

      User interface for setting image views output options

      :type image_settings: :class:`ImageFormatSettings`, (never None)

   .. method:: template_movieclip(data, property, *, compact=False)

      Item(s). User interface for selecting movie clips and their source paths.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :arg compact: Use more compact layout
      :type compact: boolean, (optional)

   .. method:: template_track(data, property)

      Item. A movie-track widget to preview tracking image.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: template_marker(data, property, clip_user, track, *, compact=False)

      Item. A widget to control single marker settings.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :type clip_user: :class:`MovieClipUser`, (never None)
      :type track: :class:`MovieTrackingTrack`, (never None)
      :arg compact: Use more compact layout
      :type compact: boolean, (optional)

   .. method:: template_movieclip_information(data, property, clip_user)

      Item. Movie clip information data.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :type clip_user: :class:`MovieClipUser`, (never None)

   .. method:: template_list(listtype_name, list_id, dataptr, propname, active_dataptr, active_propname, *, item_dyntip_propname="", rows=5, maxrows=5, type='DEFAULT', columns=9, sort_reverse=False, sort_lock=False)

      Item. A list widget to display data, e.g. vertexgroups.

      :arg listtype_name: Identifier of the list type to use
      :type listtype_name: string, (never None)
      :arg list_id: Identifier of this list widget. Necessary to tell apart different list widgets. Mandatory when using default "UI_UL_list" class. If this not an empty string, the uilist gets a custom ID, otherwise it takes the name of the class used to define the uilist (for example, if the class name is "OBJECT_UL_vgroups", and list_id is not set by the script, then bl_idname = "OBJECT_UL_vgroups")
      :type list_id: string, (never None)
      :arg dataptr: Data from which to take the Collection property
      :type dataptr: :class:`AnyType`
      :arg propname: Identifier of the Collection property in data
      :type propname: string, (never None)
      :arg active_dataptr: Data from which to take the integer property, index of the active item
      :type active_dataptr: :class:`AnyType`, (never None)
      :arg active_propname: Identifier of the integer property in active_data, index of the active item
      :type active_propname: string, (never None)
      :arg item_dyntip_propname: Identifier of a string property in items, to use as tooltip content
      :type item_dyntip_propname: string, (optional, never None)
      :arg rows: Default and minimum number of rows to display
      :type rows: int in [0, inf], (optional)
      :arg maxrows: Default maximum number of rows to display
      :type maxrows: int in [0, inf], (optional)
      :arg type: Type, Type of layout to use
      :type type: enum in :ref:`rna_enum_uilist_layout_type_items`, (optional)
      :arg columns: Number of items to display per row, for GRID layout
      :type columns: int in [0, inf], (optional)
      :arg sort_reverse: Display items in reverse order by default
      :type sort_reverse: boolean, (optional)
      :arg sort_lock: Lock display order to default value
      :type sort_lock: boolean, (optional)

   .. method:: template_running_jobs()

      template_running_jobs


   .. method:: template_operator_search()

      template_operator_search


   .. method:: template_menu_search()

      template_menu_search


   .. method:: template_header_3D_mode()

      


   .. method:: template_edit_mode_selection()

      Inserts common 3DView Edit modes header UI (selector for selection mode)


   .. method:: template_reports_banner()

      template_reports_banner


   .. method:: template_input_status()

      template_input_status


   .. method:: template_status_info()

      template_status_info


   .. method:: template_node_link(ntree, node, socket)

      template_node_link

      :type ntree: :class:`NodeTree`
      :type node: :class:`Node`
      :type socket: :class:`NodeSocket`

   .. method:: template_node_view(ntree, node, socket)

      template_node_view

      :type ntree: :class:`NodeTree`
      :type node: :class:`Node`
      :type socket: :class:`NodeSocket`

   .. method:: template_node_asset_menu_items(*, catalog_path="")

      template_node_asset_menu_items

      :type catalog_path: string, (optional, never None)

   .. method:: template_modifier_asset_menu_items(*, catalog_path="")

      template_modifier_asset_menu_items

      :type catalog_path: string, (optional, never None)

   .. method:: template_node_operator_asset_menu_items(*, catalog_path="")

      template_node_operator_asset_menu_items

      :type catalog_path: string, (optional, never None)

   .. method:: template_node_operator_asset_root_items()

      template_node_operator_asset_root_items


   .. method:: template_texture_user()

      template_texture_user


   .. method:: template_keymap_item_properties(item)

      template_keymap_item_properties

      :type item: :class:`KeyMapItem`, (never None)

   .. method:: template_component_menu(data, property, *, name="")

      Item. Display expanded property in a popup menu

      :arg data: Data from which to take property
      :type data: :class:`AnyType`
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :type name: string, (optional, never None)

   .. method:: template_colorspace_settings(data, property)

      Item. A widget to control input color space settings.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: template_colormanaged_view_settings(data, property)

      Item. A widget to control color managed view settings.

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: template_node_socket(*, color=(0.0, 0.0, 0.0, 1.0))

      Node Socket Icon

      :arg color: Color
      :type color: float array of 4 items in [0, 1], (optional)

   .. method:: template_cache_file(data, property)

      Item(s). User interface for selecting cache files and their source paths

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: template_cache_file_velocity(data, property)

      Show cache files velocity properties

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: template_cache_file_procedural(data, property)

      Show cache files render procedural properties

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: template_cache_file_time_settings(data, property)

      Show cache files time settings

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: template_cache_file_layers(data, property)

      Show cache files override layers properties

      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: template_recent_files(*, rows=5)

      Show list of recently saved .blend files

      :arg rows: Maximum number of items to show
      :type rows: int in [1, inf], (optional)
      :return: Number of items drawn
      :rtype: int in [0, inf]

   .. method:: template_file_select_path(params)

      Item. A text button to set the active file browser path.

      :type params: :class:`FileSelectParams`

   .. method:: template_event_from_keymap_item(item, *, text="", text_ctxt="", translate=True)

      Display keymap item as icons/text

      :arg item: Item
      :type item: :class:`KeyMapItem`, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)

   .. method:: template_asset_view(list_id, asset_library_dataptr, asset_library_propname, assets_dataptr, assets_propname, active_dataptr, active_propname, *, filter_id_types={}, display_options={}, activate_operator="", drag_operator="")

      Item. A scrollable list of assets in a grid view

      :arg list_id: Identifier of this asset view. Necessary to tell apart different asset views and to identify an asset view read from a .blend
      :type list_id: string, (never None)
      :arg asset_library_dataptr: Data from which to take the active asset library property
      :type asset_library_dataptr: :class:`AnyType`, (never None)
      :arg asset_library_propname: Identifier of the asset library property
      :type asset_library_propname: string, (never None)
      :arg assets_dataptr: Data from which to take the asset list property
      :type assets_dataptr: :class:`AnyType`, (never None)
      :arg assets_propname: Identifier of the asset list property
      :type assets_propname: string, (never None)
      :arg active_dataptr: Data from which to take the integer property, index of the active item
      :type active_dataptr: :class:`AnyType`, (never None)
      :arg active_propname: Identifier of the integer property in active_data, index of the active item
      :type active_propname: string, (never None)
      :arg filter_id_types: filter_id_types
      :type filter_id_types: enum set in {}, (optional)
      :arg display_options: Displaying options for the asset view

         * ``NO_NAMES``
           Do not display the name of each asset underneath preview images.
         * ``NO_FILTER``
           Do not display buttons for filtering the available assets.
         * ``NO_LIBRARY``
           Do not display buttons to choose or refresh an asset library.
      :type display_options: enum set in {``'NO_NAMES'``, ``'NO_FILTER'``, ``'NO_LIBRARY'``}, (optional)
      :arg activate_operator: Name of a custom operator to invoke when activating an item
      :type activate_operator: string, (optional, never None)
      :arg drag_operator: Name of a custom operator to invoke when starting to drag an item. Never invoked together with the ``active_operator`` (if set), it's either the drag or the activate one
      :type drag_operator: string, (optional, never None)
      :return:
         `activate_operator_properties`, Operator properties to fill in for the custom activate operator passed to the template, :class:`OperatorProperties`

         `drag_operator_properties`, Operator properties to fill in for the custom drag operator passed to the template, :class:`OperatorProperties`

      :rtype: (:class:`OperatorProperties`, :class:`OperatorProperties`)

   .. method:: template_light_linking_collection(context_layout, data, property)

      Visualization of a content of a light linking collection

      :arg context_layout: Layout to set active list element as context properties
      :type context_layout: :class:`UILayout`, (never None)
      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)

   .. method:: template_bone_collection_tree()

      Show bone collections tree


   .. method:: template_grease_pencil_layer_tree()

      View of the active Grease Pencil layer tree


   .. method:: template_node_tree_interface(interface)

      Show a node tree interface

      :arg interface: Node Tree Interface, Interface of a node tree to display
      :type interface: :class:`NodeTreeInterface`, (never None)

   .. method:: template_node_inputs(node)

      Show a node settings and input socket values

      :arg node: Node, Display inputs of this node
      :type node: :class:`Node`, (never None)

   .. method:: template_asset_shelf_popover(asset_shelf, *, name="", icon='NONE', icon_value=0)

      Create a button to open an asset shelf in a popover

      :arg asset_shelf: Identifier of the asset shelf to display (``bl_idname``)
      :type asset_shelf: string, (never None)
      :arg name: Optional name to indicate the active asset
      :type name: string, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)
      :arg icon_value: Icon Value, Override automatic icon of the item
      :type icon_value: int in [0, inf], (optional)

   .. method:: template_popup_confirm(operator, *, text="", text_ctxt="", translate=True, icon='NONE', cancel_text="", cancel_default=False)

      Add confirm & cancel buttons into a popup which will close the popup when pressed

      :arg operator: Identifier of the operator
      :type operator: string, (never None)
      :arg text: Override automatic text of the item
      :type text: string, (optional)
      :arg text_ctxt: Override automatic translation context of the given text
      :type text_ctxt: string, (optional)
      :arg translate: Translate the given text, when UI translation is enabled
      :type translate: boolean, (optional)
      :arg icon: Icon, Override automatic icon of the item
      :type icon: enum in :ref:`rna_enum_icon_items`, (optional)
      :arg cancel_text: Optional text to use for the cancel, not shown when an empty string
      :type cancel_text: string, (optional, never None)
      :arg cancel_default: Cancel button by default
      :type cancel_default: boolean, (optional)
      :return: Operator properties to fill in
      :rtype: :class:`OperatorProperties`

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


   .. method:: introspect()
   
      Return a dictionary containing a textual representation of the UI layout.


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

   * :class:`AssetShelf.draw_context_menu`
   * :class:`Header.layout`
   * :class:`Menu.layout`
   * :class:`Node.draw_buttons`
   * :class:`Node.draw_buttons_ext`
   * :class:`NodeInternal.draw_buttons`
   * :class:`NodeInternal.draw_buttons_ext`
   * :class:`NodeSocket.draw`
   * :class:`NodeSocketStandard.draw`
   * :class:`NodeTreeInterfaceSocket.draw`
   * :class:`NodeTreeInterfaceSocketBool.draw`
   * :class:`NodeTreeInterfaceSocketBundle.draw`
   * :class:`NodeTreeInterfaceSocketClosure.draw`
   * :class:`NodeTreeInterfaceSocketCollection.draw`
   * :class:`NodeTreeInterfaceSocketColor.draw`
   * :class:`NodeTreeInterfaceSocketFloat.draw`
   * :class:`NodeTreeInterfaceSocketFloatAngle.draw`
   * :class:`NodeTreeInterfaceSocketFloatColorTemperature.draw`
   * :class:`NodeTreeInterfaceSocketFloatDistance.draw`
   * :class:`NodeTreeInterfaceSocketFloatFactor.draw`
   * :class:`NodeTreeInterfaceSocketFloatFrequency.draw`
   * :class:`NodeTreeInterfaceSocketFloatPercentage.draw`
   * :class:`NodeTreeInterfaceSocketFloatTime.draw`
   * :class:`NodeTreeInterfaceSocketFloatTimeAbsolute.draw`
   * :class:`NodeTreeInterfaceSocketFloatUnsigned.draw`
   * :class:`NodeTreeInterfaceSocketFloatWavelength.draw`
   * :class:`NodeTreeInterfaceSocketGeometry.draw`
   * :class:`NodeTreeInterfaceSocketImage.draw`
   * :class:`NodeTreeInterfaceSocketInt.draw`
   * :class:`NodeTreeInterfaceSocketIntFactor.draw`
   * :class:`NodeTreeInterfaceSocketIntPercentage.draw`
   * :class:`NodeTreeInterfaceSocketIntUnsigned.draw`
   * :class:`NodeTreeInterfaceSocketMaterial.draw`
   * :class:`NodeTreeInterfaceSocketMatrix.draw`
   * :class:`NodeTreeInterfaceSocketMenu.draw`
   * :class:`NodeTreeInterfaceSocketObject.draw`
   * :class:`NodeTreeInterfaceSocketRotation.draw`
   * :class:`NodeTreeInterfaceSocketShader.draw`
   * :class:`NodeTreeInterfaceSocketString.draw`
   * :class:`NodeTreeInterfaceSocketStringFilePath.draw`
   * :class:`NodeTreeInterfaceSocketTexture.draw`
   * :class:`NodeTreeInterfaceSocketVector.draw`
   * :class:`NodeTreeInterfaceSocketVector2D.draw`
   * :class:`NodeTreeInterfaceSocketVector4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorAcceleration.draw`
   * :class:`NodeTreeInterfaceSocketVectorAcceleration2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorAcceleration4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorDirection.draw`
   * :class:`NodeTreeInterfaceSocketVectorDirection2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorDirection4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorEuler.draw`
   * :class:`NodeTreeInterfaceSocketVectorEuler2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorEuler4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorFactor.draw`
   * :class:`NodeTreeInterfaceSocketVectorFactor2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorFactor4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorPercentage.draw`
   * :class:`NodeTreeInterfaceSocketVectorPercentage2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorPercentage4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorTranslation.draw`
   * :class:`NodeTreeInterfaceSocketVectorTranslation2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorTranslation4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorVelocity.draw`
   * :class:`NodeTreeInterfaceSocketVectorVelocity2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorVelocity4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorXYZ.draw`
   * :class:`NodeTreeInterfaceSocketVectorXYZ2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorXYZ4D.draw`
   * :class:`Operator.layout`
   * :class:`Panel.layout`
   * :class:`UILayout.box`
   * :class:`UILayout.column`
   * :class:`UILayout.column_flow`
   * :class:`UILayout.grid_flow`
   * :class:`UILayout.menu_pie`
   * :class:`UILayout.panel`
   * :class:`UILayout.panel`
   * :class:`UILayout.panel_prop`
   * :class:`UILayout.panel_prop`
   * :class:`UILayout.row`
   * :class:`UILayout.split`
   * :class:`UILayout.template_light_linking_collection`
   * :class:`UIList.draw_filter`
   * :class:`UIList.draw_item`
   * :class:`UIPieMenu.layout`
   * :class:`UIPopover.layout`
   * :class:`UIPopupMenu.layout`

