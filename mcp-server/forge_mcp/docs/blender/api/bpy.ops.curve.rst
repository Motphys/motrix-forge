Curve Operators
===============

.. module:: bpy.ops.curve

.. function:: cyclic_toggle(*, direction='CYCLIC_U')

   Make active spline closed/opened loop

   :arg direction: Direction, Direction to make surface cyclic in
   :type direction: enum in [``'CYCLIC_U'``, ``'CYCLIC_V'``], (optional)

.. function:: de_select_first()

   (De)select first of visible part of each NURBS

.. function:: de_select_last()

   (De)select last of visible part of each NURBS

.. function:: decimate(*, ratio=1.0)

   Simplify selected curves

   :arg ratio: Ratio
   :type ratio: float in [0, 1], (optional)

.. function:: delete(*, type='VERT')

   Delete selected control points or segments

   :arg type: Type, Which elements to delete
   :type type: enum in [``'VERT'``, ``'SEGMENT'``], (optional)

.. function:: dissolve_verts()

   Delete selected control points, correcting surrounding handles

.. function:: draw(*, error_threshold=0.0, fit_method='REFIT', corner_angle=1.22173, use_cyclic=True, stroke=None, wait_for_input=True)

   Draw a freehand spline

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

.. function:: duplicate()

   Duplicate selected control points

.. function:: duplicate_move(*, CURVE_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Duplicate curve and move

   :arg CURVE_OT_duplicate: Duplicate Curve, Duplicate selected control points
   :type CURVE_OT_duplicate: :class:`CURVE_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: extrude(*, mode='TRANSLATION')

   Extrude selected control point(s)

   :arg mode: Mode
   :type mode: enum in :ref:`rna_enum_transform_mode_type_items`, (optional)

.. function:: extrude_move(*, CURVE_OT_extrude=None, TRANSFORM_OT_translate=None)

   Extrude curve and move result

   :arg CURVE_OT_extrude: Extrude, Extrude selected control point(s)
   :type CURVE_OT_extrude: :class:`CURVE_OT_extrude`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: handle_type_set(*, type='AUTOMATIC')

   Set type of handles for selected control points

   :arg type: Type, Spline type
   :type type: enum in [``'AUTOMATIC'``, ``'VECTOR'``, ``'ALIGNED'``, ``'FREE_ALIGN'``, ``'TOGGLE_FREE_ALIGN'``], (optional)

.. function:: hide(*, unselected=False)

   Hide (un)selected control points

   :arg unselected: Unselected, Hide unselected rather than selected
   :type unselected: boolean, (optional)

.. function:: make_segment()

   Join two curves by their selected ends

.. function:: match_texture_space()

   Match texture space to object's bounding box

.. function:: normals_make_consistent(*, calc_length=False)

   Recalculate the direction of selected handles

   :arg calc_length: Length, Recalculate handle length
   :type calc_length: boolean, (optional)

.. function:: pen(*, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, extrude_point=False, extrude_handle='VECTOR', delete_point=False, insert_point=False, move_segment=False, select_point=False, move_point=False, close_spline=True, close_spline_method='OFF', toggle_vector=False, cycle_handle_type=False)

   Construct and edit splines

   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)
   :arg deselect: Deselect, Remove from selection
   :type deselect: boolean, (optional)
   :arg toggle: Toggle Selection, Toggle the selection
   :type toggle: boolean, (optional)
   :arg deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
   :type deselect_all: boolean, (optional)
   :arg select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
   :type select_passthrough: boolean, (optional)
   :arg extrude_point: Extrude Point, Add a point connected to the last selected point
   :type extrude_point: boolean, (optional)
   :arg extrude_handle: Extrude Handle Type, Type of the extruded handle
   :type extrude_handle: enum in [``'AUTO'``, ``'VECTOR'``], (optional)
   :arg delete_point: Delete Point, Delete an existing point
   :type delete_point: boolean, (optional)
   :arg insert_point: Insert Point, Insert Point into a curve segment
   :type insert_point: boolean, (optional)
   :arg move_segment: Move Segment, Delete an existing point
   :type move_segment: boolean, (optional)
   :arg select_point: Select Point, Select a point or its handles
   :type select_point: boolean, (optional)
   :arg move_point: Move Point, Move a point or its handles
   :type move_point: boolean, (optional)
   :arg close_spline: Close Spline, Make a spline cyclic by clicking endpoints
   :type close_spline: boolean, (optional)
   :arg close_spline_method: Close Spline Method, The condition for close spline to activate

      * ``OFF``
        None.
      * ``ON_PRESS``
        On Press -- Move handles after closing the spline.
      * ``ON_CLICK``
        On Click -- Spline closes on release if not dragged.
   :type close_spline_method: enum in [``'OFF'``, ``'ON_PRESS'``, ``'ON_CLICK'``], (optional)
   :arg toggle_vector: Toggle Vector, Toggle between Vector and Auto handles
   :type toggle_vector: boolean, (optional)
   :arg cycle_handle_type: Cycle Handle Type, Cycle between all four handle types
   :type cycle_handle_type: boolean, (optional)

.. function:: primitive_bezier_circle_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Bézier Circle

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

.. function:: primitive_bezier_curve_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Bézier Curve

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

.. function:: primitive_nurbs_circle_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Nurbs Circle

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

.. function:: primitive_nurbs_curve_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Nurbs Curve

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

.. function:: primitive_nurbs_path_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Path

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

.. function:: radius_set(*, radius=1.0)

   Set per-point radius which is used for bevel tapering

   :arg radius: Radius
   :type radius: float in [0, inf], (optional)

.. function:: reveal(*, select=True)

   Reveal hidden control points

   :arg select: Select
   :type select: boolean, (optional)

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

.. function:: select_less()

   Deselect control points at the boundary of each selection region

.. function:: select_linked()

   Select all control points linked to the current selection

.. function:: select_linked_pick(*, deselect=False)

   Select all control points linked to already selected ones

   :arg deselect: Deselect, Deselect linked control points rather than selecting them
   :type deselect: boolean, (optional)

.. function:: select_more()

   Select control points at the boundary of each selection region

.. function:: select_next()

   Select control points following already selected ones along the curves

.. function:: select_nth(*, skip=1, nth=1, offset=0)

   Deselect every Nth point starting from the active one

   :arg skip: Deselected, Number of deselected elements in the repetitive sequence
   :type skip: int in [1, inf], (optional)
   :arg nth: Selected, Number of selected elements in the repetitive sequence
   :type nth: int in [1, inf], (optional)
   :arg offset: Offset, Offset from the starting point
   :type offset: int in [-inf, inf], (optional)

.. function:: select_previous()

   Select control points preceding already selected ones along the curves

.. function:: select_random(*, ratio=0.5, seed=0, action='SELECT')

   Randomly select some control points

   :arg ratio: Ratio, Portion of items to select randomly
   :type ratio: float in [0, 1], (optional)
   :arg seed: Random Seed, Seed for the random number generator
   :type seed: int in [0, inf], (optional)
   :arg action: Action, Selection action to execute

      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
   :type action: enum in [``'SELECT'``, ``'DESELECT'``], (optional)

.. function:: select_row()

   Select a row of control points including active one. Successive use on the same point switches between U/V directions

.. function:: select_similar(*, type='WEIGHT', compare='EQUAL', threshold=0.1)

   Select similar curve points by property type

   :arg type: Type
   :type type: enum in [``'TYPE'``, ``'RADIUS'``, ``'WEIGHT'``, ``'DIRECTION'``], (optional)
   :arg compare: Compare
   :type compare: enum in [``'EQUAL'``, ``'GREATER'``, ``'LESS'``], (optional)
   :arg threshold: Threshold
   :type threshold: float in [0, inf], (optional)

.. function:: separate()

   Separate selected points from connected unselected points into a new object

.. function:: shade_flat()

   Set shading to flat

.. function:: shade_smooth()

   Set shading to smooth

.. function:: shortest_path_pick()

   Select shortest path between two selections

.. function:: smooth()

   Flatten angles of selected points

.. function:: smooth_radius()

   Interpolate radii of selected points

.. function:: smooth_tilt()

   Interpolate tilt of selected points

.. function:: smooth_weight()

   Interpolate weight of selected points

.. function:: spin(*, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0))

   Extrude selected boundary row around pivot point and current view axis

   :arg center: Center, Center in global view space
   :type center: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg axis: Axis, Axis in global view space
   :type axis: :class:`mathutils.Vector` of 3 items in [-1, 1], (optional)

.. function:: spline_type_set(*, type='POLY', use_handles=False)

   Set type of active spline

   :arg type: Type, Spline type
   :type type: enum in [``'POLY'``, ``'BEZIER'``, ``'NURBS'``], (optional)
   :arg use_handles: Handles, Use handles when converting Bézier curves into polygons
   :type use_handles: boolean, (optional)

.. function:: spline_weight_set(*, weight=1.0)

   Set softbody goal weight for selected points

   :arg weight: Weight
   :type weight: float in [0, 1], (optional)

.. function:: split()

   Split off selected points from connected unselected points

.. function:: subdivide(*, number_cuts=1)

   Subdivide selected segments

   :arg number_cuts: Number of Cuts
   :type number_cuts: int in [1, 1000], (optional)

.. function:: switch_direction()

   Switch direction of selected splines

.. function:: tilt_clear()

   Clear the tilt of selected control points

.. function:: vertex_add(*, location=(0.0, 0.0, 0.0))

   Add a new control point (linked to only selected end-curve one, if any)

   :arg location: Location, Location to add new vertex at
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

