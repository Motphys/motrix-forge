Curves Operators
================

.. module:: bpy.ops.curves

.. function:: add_bezier(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add new bezier curve

   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: add_circle(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Add new circle curve

   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: attribute_set(*, value_float=0.0, value_float_vector_2d=(0.0, 0.0), value_float_vector_3d=(0.0, 0.0, 0.0), value_int=0, value_int_vector_2d=(0, 0), value_color=(1.0, 1.0, 1.0, 1.0), value_bool=False)

   Set values of the active attribute for selected elements

   :arg value_float: Value
   :type value_float: float in [-inf, inf], (optional)
   :arg value_float_vector_2d: Value
   :type value_float_vector_2d: float array of 2 items in [-inf, inf], (optional)
   :arg value_float_vector_3d: Value
   :type value_float_vector_3d: float array of 3 items in [-inf, inf], (optional)
   :arg value_int: Value
   :type value_int: int in [-inf, inf], (optional)
   :arg value_int_vector_2d: Value
   :type value_int_vector_2d: int array of 2 items in [-inf, inf], (optional)
   :arg value_color: Value
   :type value_color: float array of 4 items in [-inf, inf], (optional)
   :arg value_bool: Value
   :type value_bool: boolean, (optional)

.. function:: convert_from_particle_system()

   Add a new curves object based on the current state of the particle system

.. function:: convert_to_particle_system()

   Add a new or update an existing hair particle system on the surface object

.. function:: curve_type_set(*, type='POLY', use_handles=False)

   Set type of selected curves

   :arg type: Type, Curve type
   :type type: enum in :ref:`rna_enum_curves_type_items`, (optional)
   :arg use_handles: Handles, Take handle information into account in the conversion
   :type use_handles: boolean, (optional)

.. function:: cyclic_toggle()

   Make active curve closed/opened loop

.. function:: delete()

   Remove selected control points or curves

.. function:: draw(*, error_threshold=0.0, fit_method='REFIT', corner_angle=1.22173, use_cyclic=True, stroke=None, wait_for_input=True, is_curve_2d=False, bezier_as_nurbs=False)

   Draw a freehand curve

   :arg error_threshold: Error, Error distance threshold (in object units)
   :type error_threshold: float in [0, 10], (optional)
   :arg fit_method: Fit Method
   :type fit_method: enum in :ref:`rna_enum_curve_fit_method_items`, (optional)
   :arg corner_angle: Corner Angle
   :type corner_angle: float in [0, 3.14159], (optional)
   :arg use_cyclic: Cyclic
   :type use_cyclic: boolean, (optional)
   :arg stroke: Stroke
   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)
   :arg is_curve_2d: Curve 2D
   :type is_curve_2d: boolean, (optional)
   :arg bezier_as_nurbs: As NURBS
   :type bezier_as_nurbs: boolean, (optional)

.. function:: duplicate()

   Copy selected points or curves

.. function:: duplicate_move(*, CURVES_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Make copies of selected elements and move them

   :arg CURVES_OT_duplicate: Duplicate, Copy selected points or curves
   :type CURVES_OT_duplicate: :class:`CURVES_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: extrude()

   Extrude selected control point(s)

.. function:: extrude_move(*, CURVES_OT_extrude=None, TRANSFORM_OT_translate=None)

   Extrude curve and move result

   :arg CURVES_OT_extrude: Extrude, Extrude selected control point(s)
   :type CURVES_OT_extrude: :class:`CURVES_OT_extrude`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: handle_type_set(*, type='AUTO')

   Set the handle type for bezier curves

   :arg type: Type
   :type type: enum in :ref:`rna_enum_curves_handle_type_items`, (optional)

.. function:: sculptmode_toggle()

   Enter/Exit sculpt mode for curves

.. function:: select_all(*, action='TOGGLE')

   (De)select all control points

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

.. function:: select_ends(*, amount_start=0, amount_end=1)

   Select end points of curves

   :arg amount_start: Amount Front, Number of points to select from the front
   :type amount_start: int in [0, inf], (optional)
   :arg amount_end: Amount Back, Number of points to select from the back
   :type amount_end: int in [0, inf], (optional)

.. function:: select_less()

   Shrink the selection by one point

.. function:: select_linked()

   Select all points in curves with any point selection

.. function:: select_linked_pick(*, deselect=False)

   Select all points in the curve under the cursor

   :arg deselect: Deselect, Deselect linked control points rather than selecting them
   :type deselect: boolean, (optional)

.. function:: select_more()

   Grow the selection by one point

.. function:: select_random(*, seed=0, probability=0.5)

   Randomizes existing selection or create new random selection

   :arg seed: Seed, Source of randomness
   :type seed: int in [-inf, inf], (optional)
   :arg probability: Probability, Chance of every point or curve being included in the selection
   :type probability: float in [0, 1], (optional)

.. function:: separate()

   Separate selected geometry into a new object

.. function:: set_selection_domain(*, domain='POINT')

   Change the mode used for selection masking in curves sculpt mode

   :arg domain: Domain
   :type domain: enum in :ref:`rna_enum_attribute_curves_domain_items`, (optional)

.. function:: snap_curves_to_surface(*, attach_mode='NEAREST')

   Move curves so that the first point is exactly on the surface mesh

   :arg attach_mode: Attach Mode, How to find the point on the surface to attach to

      * ``NEAREST``
        Nearest -- Find the closest point on the surface for the root point of every curve and move the root there.
      * ``DEFORM``
        Deform -- Re-attach curves to a deformed surface using the existing attachment information. This only works when the topology of the surface mesh has not changed.
   :type attach_mode: enum in [``'NEAREST'``, ``'DEFORM'``], (optional)

.. function:: split()

   Split selected points

.. function:: subdivide(*, number_cuts=1)

   Subdivide selected curve segments

   :arg number_cuts: Number of Cuts
   :type number_cuts: int in [1, 1000], (optional)

.. function:: surface_set()

   Use the active object as surface for selected curves objects and set it as the parent

.. function:: switch_direction()

   Reverse the direction of the selected curves

.. function:: tilt_clear()

   Clear the tilt of selected control points

