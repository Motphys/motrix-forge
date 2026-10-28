Ui Operators
============

.. module:: bpy.ops.ui

.. function:: assign_default_button()

   Set this property's current value as the new default

.. function:: button_execute(*, skip_depressed=False)

   Presses active button

   :arg skip_depressed: Skip Depressed
   :type skip_depressed: boolean, (optional)

.. function:: button_string_clear()

   Unsets the text of the active button

.. function:: copy_as_driver_button()

   Create a new driver with this property as input, and copy it to the internal clipboard. Use Paste Driver to add it to the target property, or Paste Driver Variables to extend an existing driver

.. function:: copy_data_path_button(*, full_path=False)

   Copy the RNA data path for this property to the clipboard

   :arg full_path: full_path, Copy full data path
   :type full_path: boolean, (optional)

.. function:: copy_driver_to_selected_button(*, all=False)

   Copy the property's driver from the active item to the same property of all selected items, if the same property exists

   :arg all: All, Copy to selected the drivers of all elements of the array
   :type all: boolean, (optional)

.. function:: copy_python_command_button()

   Copy the Python command matching this button

.. function:: copy_to_selected_button(*, all=True)

   Copy the property's value from the active item to the same property of all selected items if the same property exists

   :arg all: All, Copy to selected all elements of the array
   :type all: boolean, (optional)

.. function:: drop_color(*, color=(0.0, 0.0, 0.0, 0.0), gamma=False, has_alpha=False)

   Drop colors to buttons

   :arg color: Color, Source color
   :type color: float array of 4 items in [0, inf], (optional)
   :arg gamma: Gamma Corrected, The source color is gamma corrected
   :type gamma: boolean, (optional)
   :arg has_alpha: Has Alpha, The source color contains an Alpha component
   :type has_alpha: boolean, (optional)

.. function:: drop_material(*, session_uid=0)

   Drag material to Material slots in Properties

   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)

.. function:: drop_name(*, string="")

   Drop name to button

   :arg string: String, The string value to drop into the button
   :type string: string, (optional, never None)

.. function:: editsource()

   Edit UI source code of the active button

.. function:: eyedropper_bone()

   Sample a bone from the 3D View or the Outliner to store in a property

.. function:: eyedropper_color(*, prop_data_path="")

   Sample a color from the Blender window to store in a property

   :arg prop_data_path: Data Path, Path of property to be set with the depth
   :type prop_data_path: string, (optional, never None)

.. function:: eyedropper_colorramp()

   Sample a color band

.. function:: eyedropper_colorramp_point()

   Point-sample a color band

.. function:: eyedropper_depth(*, prop_data_path="")

   Sample depth from the 3D view

   :arg prop_data_path: Data Path, Path of property to be set with the depth
   :type prop_data_path: string, (optional, never None)

.. function:: eyedropper_driver(*, mapping_type='SINGLE_MANY')

   Pick a property to use as a driver target

   :arg mapping_type: Mapping Type, Method used to match target and driven properties

      * ``SINGLE_MANY``
        All from Target -- Drive all components of this property using the target picked.
      * ``DIRECT``
        Single from Target -- Drive this component of this property using the target picked.
      * ``MATCH``
        Match Indices -- Create drivers for each pair of corresponding elements.
      * ``NONE_ALL``
        Manually Create Later -- Create drivers for all properties without assigning any targets yet.
      * ``NONE_SINGLE``
        Manually Create Later (Single) -- Create driver for this property only and without assigning any targets yet.
   :type mapping_type: enum in [``'SINGLE_MANY'``, ``'DIRECT'``, ``'MATCH'``, ``'NONE_ALL'``, ``'NONE_SINGLE'``], (optional)

.. function:: eyedropper_grease_pencil_color(*, mode='MATERIAL', material_mode='STROKE')

   Sample a color from the Blender Window and create Grease Pencil material

   :arg mode: Mode
   :type mode: enum in [``'MATERIAL'``, ``'PALETTE'``, ``'BRUSH'``], (optional)
   :arg material_mode: Material Mode
   :type material_mode: enum in [``'STROKE'``, ``'FILL'``, ``'BOTH'``], (optional)

.. function:: eyedropper_id()

   Sample a data-block from the 3D View to store in a property

.. function:: jump_to_target_button()

   Switch to the target object or bone

.. function:: list_start_filter()

   Start entering filter text for the list in focus

.. function:: override_idtemplate_clear()

   Delete the selected local override and relink its usages to the linked data-block if possible, else reset it and mark it as non editable

.. function:: override_idtemplate_make()

   Create a local override of the selected linked data-block, and its hierarchy of dependencies

.. function:: override_idtemplate_reset()

   Reset the selected local override to its linked reference values

.. function:: override_remove_button(*, all=True)

   Remove an override operation

   :arg all: All, Reset to default values all elements of the array
   :type all: boolean, (optional)

.. function:: override_type_set_button(*, all=True, type='REPLACE')

   Create an override operation, or set the type of an existing one

   :arg all: All, Reset to default values all elements of the array
   :type all: boolean, (optional)
   :arg type: Type, Type of override operation

      * ``NOOP``
        NoOp -- 'No-Operation', place holder preventing automatic override to ever affect the property.
      * ``REPLACE``
        Replace -- Completely replace value from linked data by local one.
      * ``DIFFERENCE``
        Difference -- Store difference to linked data value.
      * ``FACTOR``
        Factor -- Store factor to linked data value (useful e.g. for scale).
   :type type: enum in [``'NOOP'``, ``'REPLACE'``, ``'DIFFERENCE'``, ``'FACTOR'``], (optional)

.. function:: reloadtranslation()

   Force a full reload of UI translation

.. function:: reset_default_button(*, all=True)

   Reset this property's value to its default value

   :arg all: All, Reset to default values all elements of the array
   :type all: boolean, (optional)

.. function:: unset_property_button()

   Clear the property and use default or generated value in operators

.. function:: view_drop()

   Drag and drop onto a data-set or item within the data-set

.. function:: view_item_rename()

   Rename the active item in the data-set view

.. function:: view_scroll()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

.. function:: view_start_filter()

   Start entering filter text for the data-set in focus

