View3D Operators
================

.. module:: bpy.ops.view3d

.. function:: bone_select_menu(*, name='', extend=False, deselect=False, toggle=False)

   Menu bone selection

   :arg name: Bone Name
   :type name: enum in [], (optional)
   :arg extend: Extend
   :type extend: boolean, (optional)
   :arg deselect: Deselect
   :type deselect: boolean, (optional)
   :arg toggle: Toggle
   :type toggle: boolean, (optional)

.. function:: camera_background_image_add(*, filepath="", relative_path=True, name="", session_uid=0)

   Add a new background image to the active camera

   :arg filepath: Filepath, Path to image file
   :type filepath: string, (optional, never None, blend relative ``//`` prefix supported)
   :arg relative_path: Relative Path, Select the file relative to the blend file
   :type relative_path: boolean, (optional)
   :arg name: Name, Name of the data-block to use by the operator
   :type name: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)

.. function:: camera_background_image_remove(*, index=0)

   Remove a background image from the camera

   :arg index: Index, Background image index to remove
   :type index: int in [0, inf], (optional)

.. function:: camera_to_view()

   Set camera view to active view

.. function:: camera_to_view_selected()

   Move the camera so selected objects are framed

.. function:: clear_render_border()

   Clear the boundaries of the border render and disable border render

.. function:: clip_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Set the view clipping region

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

.. function:: copybuffer()

   Copy the selected objects to the internal clipboard

.. function:: cursor3d(*, use_depth=True, orientation='VIEW')

   Set the location of the 3D cursor

   :arg use_depth: Surface Project, Project onto the surface
   :type use_depth: boolean, (optional)
   :arg orientation: Orientation, Preset viewpoint to use

      * ``NONE``
        None -- Leave orientation unchanged.
      * ``VIEW``
        View -- Orient to the viewport.
      * ``XFORM``
        Transform -- Orient to the current transform setting.
      * ``GEOM``
        Geometry -- Match the surface normal.
   :type orientation: enum in [``'NONE'``, ``'VIEW'``, ``'XFORM'``, ``'GEOM'``], (optional)

.. function:: dolly(*, mx=0, my=0, delta=0, use_cursor_init=True)

   Dolly in/out in the view

   :arg mx: Region Position X
   :type mx: int in [0, inf], (optional)
   :arg my: Region Position Y
   :type my: int in [0, inf], (optional)
   :arg delta: Delta
   :type delta: int in [-inf, inf], (optional)
   :arg use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
   :type use_cursor_init: boolean, (optional)

.. function:: drop_world(*, name="", session_uid=0)

   Drop a world into the scene

   :arg name: Name, Name of the data-block to use by the operator
   :type name: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)

.. function:: edit_mesh_extrude_individual_move()

   Extrude each individual face separately along local normals

   :File: `startup\bl_operators\view3d.py\:30 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\view3d.py#L30>`__

.. function:: edit_mesh_extrude_manifold_normal()

   Extrude manifold region along normals

   :File: `startup\bl_operators\view3d.py\:198 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\view3d.py#L198>`__

.. function:: edit_mesh_extrude_move_normal(*, dissolve_and_intersect=False)

   Extrude region together along the average normal

   :arg dissolve_and_intersect: dissolve_and_intersect, Dissolves adjacent faces and intersects new geometry
   :type dissolve_and_intersect: boolean, (optional)
   :File: `startup\bl_operators\view3d.py\:166 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\view3d.py#L166>`__


.. function:: edit_mesh_extrude_move_shrink_fatten()

   Extrude region together along local normals

   :File: `startup\bl_operators\view3d.py\:182 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\view3d.py#L182>`__

.. function:: fly()

   Interactively fly around the scene

.. function:: interactive_add(*, primitive_type='CUBE', plane_origin_base='EDGE', plane_origin_depth='EDGE', plane_aspect_base='FREE', plane_aspect_depth='FREE', wait_for_input=True)

   Interactively add an object

   :arg primitive_type: Primitive
   :type primitive_type: enum in [``'CUBE'``, ``'CYLINDER'``, ``'CONE'``, ``'SPHERE_UV'``, ``'SPHERE_ICO'``], (optional)
   :arg plane_origin_base: Origin, The initial position for placement

      * ``EDGE``
        Edge -- Start placing the edge position.
      * ``CENTER``
        Center -- Start placing the center position.
   :type plane_origin_base: enum in [``'EDGE'``, ``'CENTER'``], (optional)
   :arg plane_origin_depth: Origin, The initial position for placement

      * ``EDGE``
        Edge -- Start placing the edge position.
      * ``CENTER``
        Center -- Start placing the center position.
   :type plane_origin_depth: enum in [``'EDGE'``, ``'CENTER'``], (optional)
   :arg plane_aspect_base: Aspect, The initial aspect setting

      * ``FREE``
        Free -- Use an unconstrained aspect.
      * ``FIXED``
        Fixed -- Use a fixed 1:1 aspect.
   :type plane_aspect_base: enum in [``'FREE'``, ``'FIXED'``], (optional)
   :arg plane_aspect_depth: Aspect, The initial aspect setting

      * ``FREE``
        Free -- Use an unconstrained aspect.
      * ``FIXED``
        Fixed -- Use a fixed 1:1 aspect.
   :type plane_aspect_depth: enum in [``'FREE'``, ``'FIXED'``], (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)

.. function:: localview(*, frame_selected=True)

   Toggle display of selected object(s) separately and centered in view

   :arg frame_selected: Frame Selected, Move the view to frame the selected objects
   :type frame_selected: boolean, (optional)

.. function:: localview_remove_from()

   Move selected objects out of local view

.. function:: move(*, use_cursor_init=True)

   Move the view

   :arg use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
   :type use_cursor_init: boolean, (optional)

.. function:: navigate()

   Interactively navigate around the scene (uses the mode (walk/fly) preference)

.. function:: ndof_all()

   Pan and rotate the view with the 3D mouse

.. function:: ndof_orbit()

   Orbit the view using the 3D mouse

.. function:: ndof_orbit_zoom()

   Orbit and zoom the view using the 3D mouse

.. function:: ndof_pan()

   Pan the view with the 3D mouse

.. function:: object_as_camera()

   Set the active object as the active camera for this view or scene

.. function:: object_mode_pie_or_toggle()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

.. function:: pastebuffer(*, autoselect=True, active_collection=True)

   Paste objects from the internal clipboard

   :arg autoselect: Select, Select pasted objects
   :type autoselect: boolean, (optional)
   :arg active_collection: Active Collection, Put pasted objects in the active collection
   :type active_collection: boolean, (optional)

.. function:: render_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Set the boundaries of the border render and enable border render

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

.. function:: rotate(*, use_cursor_init=True)

   Rotate the view

   :arg use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
   :type use_cursor_init: boolean, (optional)

.. function:: ruler_add()

   Add ruler

.. function:: ruler_remove()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

.. function:: select(*, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, center=False, enumerate=False, object=False, location=(0, 0))

   Select and activate item(s)

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
   :arg center: Center, Use the object center when selecting, in edit mode used to extend object selection
   :type center: boolean, (optional)
   :arg enumerate: Enumerate, List objects under the mouse (object mode only)
   :type enumerate: boolean, (optional)
   :arg object: Object, Use object selection (edit mode only)
   :type object: boolean, (optional)
   :arg location: Location, Mouse location
   :type location: int array of 2 items in [-inf, inf], (optional)

.. function:: select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Select items using box selection

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
      * ``XOR``
        Difference -- Invert existing selection.
      * ``AND``
        Intersect -- Intersect existing selection.
   :type mode: enum in [``'SET'``, ``'ADD'``, ``'SUB'``, ``'XOR'``, ``'AND'``], (optional)

.. function:: select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET')

   Select items using circle selection

   :arg x: X
   :type x: int in [-inf, inf], (optional)
   :arg y: Y
   :type y: int in [-inf, inf], (optional)
   :arg radius: Radius
   :type radius: int in [1, inf], (optional)
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

.. function:: select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

   Select items using lasso selection

   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
   :type use_smooth_stroke: boolean, (optional)
   :arg smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
   :type smooth_stroke_factor: float in [0.5, 0.99], (optional)
   :arg smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
   :type smooth_stroke_radius: int in [10, 200], (optional)
   :arg mode: Mode

      * ``SET``
        Set -- Set a new selection.
      * ``ADD``
        Extend -- Extend existing selection.
      * ``SUB``
        Subtract -- Subtract existing selection.
      * ``XOR``
        Difference -- Invert existing selection.
      * ``AND``
        Intersect -- Intersect existing selection.
   :type mode: enum in [``'SET'``, ``'ADD'``, ``'SUB'``, ``'XOR'``, ``'AND'``], (optional)

.. function:: select_menu(*, name='', extend=False, deselect=False, toggle=False)

   Menu object selection

   :arg name: Object Name
   :type name: enum in [], (optional)
   :arg extend: Extend
   :type extend: boolean, (optional)
   :arg deselect: Deselect
   :type deselect: boolean, (optional)
   :arg toggle: Toggle
   :type toggle: boolean, (optional)

.. function:: smoothview()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

.. function:: snap_cursor_to_active()

   Snap 3D cursor to the active item

.. function:: snap_cursor_to_center()

   Snap 3D cursor to the world origin

.. function:: snap_cursor_to_grid()

   Snap 3D cursor to the nearest grid division

.. function:: snap_cursor_to_selected()

   Snap 3D cursor to the middle of the selected item(s)

.. function:: snap_selected_to_active()

   Snap selected item(s) to the active item

.. function:: snap_selected_to_cursor(*, use_offset=True, use_rotation=False)

   Snap selected item(s) to the 3D cursor

   :arg use_offset: Offset, If the selection should be snapped as a whole or by each object center
   :type use_offset: boolean, (optional)
   :arg use_rotation: Rotation, If the selection should be rotated to match the cursor
   :type use_rotation: boolean, (optional)

.. function:: snap_selected_to_grid()

   Snap selected item(s) to their nearest grid division

.. function:: toggle_matcap_flip()

   Flip MatCap

.. function:: toggle_shading(*, type='WIREFRAME')

   Toggle shading type in 3D viewport

   :arg type: Type, Shading type to toggle

      * ``WIREFRAME``
        Wireframe -- Toggle wireframe shading.
      * ``SOLID``
        Solid -- Toggle solid shading.
      * ``MATERIAL``
        Material Preview -- Toggle material preview shading.
      * ``RENDERED``
        Rendered -- Toggle rendered shading.
   :type type: enum in [``'WIREFRAME'``, ``'SOLID'``, ``'MATERIAL'``, ``'RENDERED'``], (optional)

.. function:: toggle_xray()

   Transparent scene display. Allow selecting through items

.. function:: transform_gizmo_set(*, extend=False, type={})

   Set the current transform gizmo

   :arg extend: Extend
   :type extend: boolean, (optional)
   :arg type: Type
   :type type: enum set in {``'TRANSLATE'``, ``'ROTATE'``, ``'SCALE'``}, (optional)
   :File: `startup\bl_operators\view3d.py\:245 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\view3d.py#L245>`__


.. function:: view_all(*, use_all_regions=False, center=False)

   View all objects in scene

   :arg use_all_regions: All Regions, View selected for all regions
   :type use_all_regions: boolean, (optional)
   :arg center: Center
   :type center: boolean, (optional)

.. function:: view_axis(*, type='LEFT', align_active=False, relative=False)

   Use a preset viewpoint

   :arg type: View, Preset viewpoint to use

      * ``LEFT``
        Left -- View from the left.
      * ``RIGHT``
        Right -- View from the right.
      * ``BOTTOM``
        Bottom -- View from the bottom.
      * ``TOP``
        Top -- View from the top.
      * ``FRONT``
        Front -- View from the front.
      * ``BACK``
        Back -- View from the back.
   :type type: enum in [``'LEFT'``, ``'RIGHT'``, ``'BOTTOM'``, ``'TOP'``, ``'FRONT'``, ``'BACK'``], (optional)
   :arg align_active: Align Active, Align to the active object's axis
   :type align_active: boolean, (optional)
   :arg relative: Relative, Rotate relative to the current orientation
   :type relative: boolean, (optional)

.. function:: view_camera()

   Toggle the camera view

.. function:: view_center_camera()

   Center the camera view, resizing the view to fit its bounds

.. function:: view_center_cursor()

   Center the view so that the cursor is in the middle of the view

.. function:: view_center_lock()

   Center the view lock offset

.. function:: view_center_pick()

   Center the view to the Z-depth position under the mouse cursor

.. function:: view_lock_clear()

   Clear all view locking

.. function:: view_lock_to_active()

   Lock the view to the active object/bone

.. function:: view_orbit(*, angle=0.0, type='ORBITLEFT')

   Orbit the view

   :arg angle: Roll
   :type angle: float in [-inf, inf], (optional)
   :arg type: Orbit, Direction of View Orbit

      * ``ORBITLEFT``
        Orbit Left -- Orbit the view around to the left.
      * ``ORBITRIGHT``
        Orbit Right -- Orbit the view around to the right.
      * ``ORBITUP``
        Orbit Up -- Orbit the view up.
      * ``ORBITDOWN``
        Orbit Down -- Orbit the view down.
   :type type: enum in [``'ORBITLEFT'``, ``'ORBITRIGHT'``, ``'ORBITUP'``, ``'ORBITDOWN'``], (optional)

.. function:: view_pan(*, type='PANLEFT')

   Pan the view in a given direction

   :arg type: Pan, Direction of View Pan

      * ``PANLEFT``
        Pan Left -- Pan the view to the left.
      * ``PANRIGHT``
        Pan Right -- Pan the view to the right.
      * ``PANUP``
        Pan Up -- Pan the view up.
      * ``PANDOWN``
        Pan Down -- Pan the view down.
   :type type: enum in [``'PANLEFT'``, ``'PANRIGHT'``, ``'PANUP'``, ``'PANDOWN'``], (optional)

.. function:: view_persportho()

   Switch the current view from perspective/orthographic projection

.. function:: view_roll(*, angle=0.0, type='ANGLE')

   Roll the view

   :arg angle: Roll
   :type angle: float in [-inf, inf], (optional)
   :arg type: Roll Angle Source, How roll angle is calculated

      * ``ANGLE``
        Roll Angle -- Roll the view using an angle value.
      * ``LEFT``
        Roll Left -- Roll the view around to the left.
      * ``RIGHT``
        Roll Right -- Roll the view around to the right.
   :type type: enum in [``'ANGLE'``, ``'LEFT'``, ``'RIGHT'``], (optional)

.. function:: view_selected(*, use_all_regions=False)

   Move the view to the selection center

   :arg use_all_regions: All Regions, View selected for all regions
   :type use_all_regions: boolean, (optional)

.. function:: walk()

   Interactively walk around the scene

.. function:: zoom(*, mx=0, my=0, delta=0, use_cursor_init=True)

   Zoom in/out in the view

   :arg mx: Region Position X
   :type mx: int in [0, inf], (optional)
   :arg my: Region Position Y
   :type my: int in [0, inf], (optional)
   :arg delta: Delta
   :type delta: int in [-inf, inf], (optional)
   :arg use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
   :type use_cursor_init: boolean, (optional)

.. function:: zoom_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, zoom_out=False)

   Zoom in the view to the nearest object contained in the border

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

.. function:: zoom_camera_1_to_1()

   Match the camera to 1:1 to the render output

