Spreadsheet Operators
=====================

.. module:: bpy.ops.spreadsheet

.. function:: add_row_filter_rule()

   Add a filter to remove rows from the displayed data

.. function:: change_spreadsheet_data_source(*, component_type=0, attribute_domain_type=0)

   Change visible data source in the spreadsheet

   :arg component_type: Component Type
   :type component_type: int in [0, 32767], (optional)
   :arg attribute_domain_type: Attribute Domain Type
   :type attribute_domain_type: int in [0, 32767], (optional)

.. function:: fit_column()

   Resize a spreadsheet column to the width of the data

.. function:: remove_row_filter_rule(*, index=0)

   Remove a row filter from the rules

   :arg index: Index
   :type index: int in [0, inf], (optional)

.. function:: reorder_columns()

   Change the order of columns

.. function:: resize_column()

   Resize a spreadsheet column

.. function:: toggle_pin()

   Turn on or off pinning

   :File: `startup\bl_operators\spreadsheet.py\:21 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\spreadsheet.py#L21>`__

