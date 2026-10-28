Info Operators
==============

.. module:: bpy.ops.info

.. function:: report_copy()

   Copy selected reports to clipboard

.. function:: report_delete()

   Delete selected reports

.. function:: report_replay()

   Replay selected reports

.. function:: reports_display_update()

   Update the display of reports in Blender UI (internal use)

.. function:: select_all(*, action='SELECT')

   Change selection of all visible reports

   :arg action: Action, Selection action to execute

      * ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
      * ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: enum in [``'TOGGLE'``, ``'SELECT'``, ``'DESELECT'``, ``'INVERT'``], (optional)

.. function:: select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Toggle box selection

   :arg xmin: X Min
   :type xmin: int in [-inf, inf], (optional)
   :arg xmax: X Max
   :type xmax: int in [-inf, inf], (optional)
   :arg ymin: Y Min
   :type ymin: int in [-inf, inf], (optional)
   :arg ymax: Y Max
   :type ymax: int in [-inf, inf], (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)
   :arg mode: Mode

      * ``SET``
        Set -- Set a new selection.
      * ``ADD``
        Extend -- Extend existing selection.
      * ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: enum in [``'SET'``, ``'ADD'``, ``'SUB'``], (optional)

.. function:: select_pick(*, report_index=0, extend=False)

   Select reports by index

   :arg report_index: Report, Index of the report
   :type report_index: int in [0, inf], (optional)
   :arg extend: Extend, Extend report selection
   :type extend: boolean, (optional)

