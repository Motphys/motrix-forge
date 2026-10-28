View2D Operators
================

.. module:: bpy.ops.view2d

.. function:: edge_pan(*, inside_padding=1.0, outside_padding=0.0, speed_ramp=1.0, max_speed=500.0, delay=1.0, zoom_influence=0.0)

   Pan the view when the mouse is held at an edge

   :arg inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning
   :type inside_padding: float in [0, 100], (optional)
   :arg outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning
   :type outside_padding: float in [0, 100], (optional)
   :arg speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge
   :type speed_ramp: float in [0, 100], (optional)
   :arg max_speed: Max Speed, Maximum speed in UI units per second
   :type max_speed: float in [0, 10000], (optional)
   :arg delay: Delay, Delay in seconds before maximum speed is reached
   :type delay: float in [0, 10], (optional)
   :arg zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed
   :type zoom_influence: float in [0, 1], (optional)

.. function:: ndof()

   Use a 3D mouse device to pan/zoom the view

.. function:: pan(*, deltax=0, deltay=0)

   Pan the view

   :arg deltax: Delta X
   :type deltax: int in [-inf, inf], (optional)
   :arg deltay: Delta Y
   :type deltay: int in [-inf, inf], (optional)

.. function:: reset()

   Reset the view

.. function:: scroll_down(*, deltax=0, deltay=0, page=False)

   Scroll the view down

   :arg deltax: Delta X
   :type deltax: int in [-inf, inf], (optional)
   :arg deltay: Delta Y
   :type deltay: int in [-inf, inf], (optional)
   :arg page: Page, Scroll down one page
   :type page: boolean, (optional)

.. function:: scroll_left(*, deltax=0, deltay=0)

   Scroll the view left

   :arg deltax: Delta X
   :type deltax: int in [-inf, inf], (optional)
   :arg deltay: Delta Y
   :type deltay: int in [-inf, inf], (optional)

.. function:: scroll_right(*, deltax=0, deltay=0)

   Scroll the view right

   :arg deltax: Delta X
   :type deltax: int in [-inf, inf], (optional)
   :arg deltay: Delta Y
   :type deltay: int in [-inf, inf], (optional)

.. function:: scroll_up(*, deltax=0, deltay=0, page=False)

   Scroll the view up

   :arg deltax: Delta X
   :type deltax: int in [-inf, inf], (optional)
   :arg deltay: Delta Y
   :type deltay: int in [-inf, inf], (optional)
   :arg page: Page, Scroll up one page
   :type page: boolean, (optional)

.. function:: scroller_activate()

   Scroll view by mouse click and drag

.. function:: smoothview(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

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

.. function:: zoom(*, deltax=0.0, deltay=0.0, use_cursor_init=True)

   Zoom in/out the view

   :arg deltax: Delta X
   :type deltax: float in [-inf, inf], (optional)
   :arg deltay: Delta Y
   :type deltay: float in [-inf, inf], (optional)
   :arg use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
   :type use_cursor_init: boolean, (optional)

.. function:: zoom_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, zoom_out=False)

   Zoom in the view to the nearest item contained in the border

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
   :arg zoom_out: Zoom Out
   :type zoom_out: boolean, (optional)

.. function:: zoom_in(*, zoomfacx=0.0, zoomfacy=0.0)

   Zoom in the view

   :arg zoomfacx: Zoom Factor X
   :type zoomfacx: float in [-inf, inf], (optional)
   :arg zoomfacy: Zoom Factor Y
   :type zoomfacy: float in [-inf, inf], (optional)

.. function:: zoom_out(*, zoomfacx=0.0, zoomfacy=0.0)

   Zoom out the view

   :arg zoomfacx: Zoom Factor X
   :type zoomfacx: float in [-inf, inf], (optional)
   :arg zoomfacy: Zoom Factor Y
   :type zoomfacy: float in [-inf, inf], (optional)

