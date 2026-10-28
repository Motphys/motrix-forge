Marker Operators
================

.. module:: bpy.ops.marker

.. function:: add()

   Add a new time marker

.. function:: camera_bind()

   Bind the selected camera to a marker on the current frame

.. function:: delete(*, confirm=True)

   Delete selected time marker(s)

   :arg confirm: Confirm, Prompt for confirmation
   :type confirm: boolean, (optional)

.. function:: duplicate(*, frames=0)

   Duplicate selected time marker(s)

   :arg frames: Frames
   :type frames: int in [-inf, inf], (optional)

.. function:: make_links_scene(*, scene='')

   Copy selected markers to another scene

   :arg scene: Scene
   :type scene: enum in [], (optional)

.. function:: move(*, frames=0, tweak=False)

   Move selected time marker(s)

   :arg frames: Frames
   :type frames: int in [-inf, inf], (optional)
   :arg tweak: Tweak, Operator has been activated using a click-drag event
   :type tweak: boolean, (optional)

.. function:: rename(*, name="RenamedMarker")

   Rename first selected time marker

   :arg name: Name, New name for marker
   :type name: string, (optional, never None)

.. function:: select(*, wait_to_deselect_others=False, mouse_x=0, mouse_y=0, extend=False, camera=False)

   Select time marker(s)

   :arg wait_to_deselect_others: Wait to Deselect Others
   :type wait_to_deselect_others: boolean, (optional)
   :arg mouse_x: Mouse X
   :type mouse_x: int in [-inf, inf], (optional)
   :arg mouse_y: Mouse Y
   :type mouse_y: int in [-inf, inf], (optional)
   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)
   :arg camera: Camera, Select the camera
   :type camera: boolean, (optional)

.. function:: select_all(*, action='TOGGLE')

   Change selection of all time markers

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

.. function:: select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET', tweak=False)

   Select all time markers using box selection

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
   :arg tweak: Tweak, Operator has been activated using a click-drag event
   :type tweak: boolean, (optional)

.. function:: select_leftright(*, mode='LEFT', extend=False)

   Select markers on and left/right of the current frame

   :arg mode: Mode
   :type mode: enum in [``'LEFT'``, ``'RIGHT'``], (optional)
   :arg extend: Extend Select
   :type extend: boolean, (optional)

