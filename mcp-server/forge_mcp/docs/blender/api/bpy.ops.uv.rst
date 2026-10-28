Uv Operators
============

.. module:: bpy.ops.uv

.. function:: align(*, axis='ALIGN_AUTO')

   Aligns selected UV vertices on a line

   :arg axis: Axis, Axis to align UV locations on

      * ``ALIGN_S``
        Straighten -- Align UV vertices along the line defined by the endpoints.
      * ``ALIGN_T``
        Straighten X -- Align UV vertices, moving them horizontally to the line defined by the endpoints.
      * ``ALIGN_U``
        Straighten Y -- Align UV vertices, moving them vertically to the line defined by the endpoints.
      * ``ALIGN_AUTO``
        Align Auto -- Automatically choose the direction on which there is most alignment already.
      * ``ALIGN_X``
        Align Vertically -- Align UV vertices on a vertical line.
      * ``ALIGN_Y``
        Align Horizontally -- Align UV vertices on a horizontal line.
   :type axis: enum in [``'ALIGN_S'``, ``'ALIGN_T'``, ``'ALIGN_U'``, ``'ALIGN_AUTO'``, ``'ALIGN_X'``, ``'ALIGN_Y'``], (optional)

.. function:: align_rotation(*, method='AUTO', axis='X', correct_aspect=False)

   Align the UV island's rotation

   :arg method: Method, Method to calculate rotation angle

      * ``AUTO``
        Auto -- Align from all edges.
      * ``EDGE``
        Edge -- Only selected edges.
      * ``GEOMETRY``
        Geometry -- Align to Geometry axis.
   :type method: enum in [``'AUTO'``, ``'EDGE'``, ``'GEOMETRY'``], (optional)
   :arg axis: Axis, Axis to align to

      * ``X``
        X -- X axis.
      * ``Y``
        Y -- Y axis.
      * ``Z``
        Z -- Z axis.
   :type axis: enum in [``'X'``, ``'Y'``, ``'Z'``], (optional)
   :arg correct_aspect: Correct Aspect, Take image aspect ratio into account
   :type correct_aspect: boolean, (optional)
   :File: `startup\bl_operators\uvcalc_transform.py\:299 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\uvcalc_transform.py#L299>`__


.. function:: average_islands_scale(*, scale_uv=False, shear=False)

   Average the size of separate UV islands, based on their area in 3D space

   :arg scale_uv: Non-Uniform, Scale U and V independently
   :type scale_uv: boolean, (optional)
   :arg shear: Shear, Reduce shear within islands
   :type shear: boolean, (optional)

.. function:: copy()

   Copy selected UV vertices

.. function:: cube_project(*, cube_size=1.0, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False)

   Project the UV vertices of the mesh over the six faces of a cube

   :arg cube_size: Cube Size, Size of the cube to project on
   :type cube_size: float in [0, inf], (optional)
   :arg correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account
   :type correct_aspect: boolean, (optional)
   :arg clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
   :type clip_to_bounds: boolean, (optional)
   :arg scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
   :type scale_to_bounds: boolean, (optional)

.. function:: cursor_set(*, location=(0.0, 0.0))

   Set 2D cursor location

   :arg location: Location, Cursor location in normalized (0.0 to 1.0) coordinates
   :type location: :class:`mathutils.Vector` of 2 items in [-inf, inf], (optional)

.. function:: cylinder_project(*, direction='VIEW_ON_EQUATOR', align='POLAR_ZX', pole='PINCH', seam=False, radius=1.0, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False)

   Project the UV vertices of the mesh over the curved wall of a cylinder

   :arg direction: Direction, Direction of the sphere or cylinder

      * ``VIEW_ON_EQUATOR``
        View on Equator -- 3D view is on the equator.
      * ``VIEW_ON_POLES``
        View on Poles -- 3D view is on the poles.
      * ``ALIGN_TO_OBJECT``
        Align to Object -- Align according to object transform.
   :type direction: enum in [``'VIEW_ON_EQUATOR'``, ``'VIEW_ON_POLES'``, ``'ALIGN_TO_OBJECT'``], (optional)
   :arg align: Align, How to determine rotation around the pole

      * ``POLAR_ZX``
        Polar ZX -- Polar 0 is X.
      * ``POLAR_ZY``
        Polar ZY -- Polar 0 is Y.
   :type align: enum in [``'POLAR_ZX'``, ``'POLAR_ZY'``], (optional)
   :arg pole: Pole, How to handle faces at the poles

      * ``PINCH``
        Pinch -- UVs are pinched at the poles.
      * ``FAN``
        Fan -- UVs are fanned at the poles.
   :type pole: enum in [``'PINCH'``, ``'FAN'``], (optional)
   :arg seam: Preserve Seams, Separate projections by islands isolated by seams
   :type seam: boolean, (optional)
   :arg radius: Radius, Radius of the sphere or cylinder
   :type radius: float in [0, inf], (optional)
   :arg correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account
   :type correct_aspect: boolean, (optional)
   :arg clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
   :type clip_to_bounds: boolean, (optional)
   :arg scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
   :type scale_to_bounds: boolean, (optional)

.. function:: export_layout(*, filepath="", export_all=False, export_tiles='NONE', modified=False, mode='PNG', size=(1024, 1024), opacity=0.25, check_existing=True)

   Export UV layout to file

   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :arg export_all: All UVs, Export all UVs in this mesh (not just visible ones)
   :type export_all: boolean, (optional)
   :arg export_tiles: Export Tiles, Choose whether to export only the [0, 1] range, or all UV tiles

      * ``NONE``
        None -- Export only UVs in the [0, 1] range.
      * ``UDIM``
        UDIM -- Export tiles in the UDIM numbering scheme: 1001 + u_tile + 10\*v_tile.
      * ``UV``
        UVTILE -- Export tiles in the UVTILE numbering scheme: u(u_tile + 1)_v(v_tile + 1).
   :type export_tiles: enum in [``'NONE'``, ``'UDIM'``, ``'UV'``], (optional)
   :arg modified: Modified, Exports UVs from the modified mesh
   :type modified: boolean, (optional)
   :arg mode: Format, File format to export the UV layout to

      * ``SVG``
        Scalable Vector Graphic (.svg) -- Export the UV layout to a vector SVG file.
      * ``EPS``
        Encapsulated PostScript (.eps) -- Export the UV layout to a vector EPS file.
      * ``PNG``
        PNG Image (.png) -- Export the UV layout to a bitmap image.
   :type mode: enum in [``'SVG'``, ``'EPS'``, ``'PNG'``], (optional)
   :arg size: Size, Dimensions of the exported file
   :type size: int array of 2 items in [8, 32768], (optional)
   :arg opacity: Fill Opacity, Set amount of opacity for exported UV layout
   :type opacity: float in [0, 1], (optional)
   :arg check_existing: check_existing
   :type check_existing: boolean, (optional)
   :File: `addons_core\io_mesh_uv_layout\__init__.py\:137 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\io_mesh_uv_layout\__init__.py#L137>`__


.. function:: follow_active_quads(*, mode='LENGTH_AVERAGE')

   Follow UVs from active quads along continuous face loops

   :arg mode: Edge Length Mode, Method to space UV edge loops

      * ``EVEN``
        Even -- Space all UVs evenly.
      * ``LENGTH``
        Length -- Average space UVs edge length of each loop.
      * ``LENGTH_AVERAGE``
        Length Average -- Average space UVs edge length of each loop.
   :type mode: enum in [``'EVEN'``, ``'LENGTH'``, ``'LENGTH_AVERAGE'``], (optional)
   :File: `startup\bl_operators\uvcalc_follow_active.py\:297 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\uvcalc_follow_active.py#L297>`__


.. function:: hide(*, unselected=False)

   Hide (un)selected UV vertices

   :arg unselected: Unselected, Hide unselected rather than selected
   :type unselected: boolean, (optional)

.. function:: lightmap_pack(*, PREF_CONTEXT='SEL_FACES', PREF_PACK_IN_ONE=True, PREF_NEW_UVLAYER=False, PREF_BOX_DIV=12, PREF_MARGIN_DIV=0.1)

   Pack each face's UVs into the UV bounds

   :arg PREF_CONTEXT: Selection

      * ``SEL_FACES``
        Selected Faces -- Space all UVs evenly.
      * ``ALL_FACES``
        All Faces -- Average space UVs edge length of each loop.
   :type PREF_CONTEXT: enum in [``'SEL_FACES'``, ``'ALL_FACES'``], (optional)
   :arg PREF_PACK_IN_ONE: Share Texture Space, Objects share texture space, map all objects into a single UV map
   :type PREF_PACK_IN_ONE: boolean, (optional)
   :arg PREF_NEW_UVLAYER: New UV Map, Create a new UV map for every mesh packed
   :type PREF_NEW_UVLAYER: boolean, (optional)
   :arg PREF_BOX_DIV: Pack Quality, Quality of the packing. Higher values will be slower but waste less space
   :type PREF_BOX_DIV: int in [1, 48], (optional)
   :arg PREF_MARGIN_DIV: Margin, Size of the margin as a division of the UV
   :type PREF_MARGIN_DIV: float in [0.001, 1], (optional)
   :File: `startup\bl_operators\uvcalc_lightmap.py\:662 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\uvcalc_lightmap.py#L662>`__


.. function:: mark_seam(*, clear=False)

   Mark selected UV edges as seams

   :arg clear: Clear Seams, Clear instead of marking seams
   :type clear: boolean, (optional)

.. function:: minimize_stretch(*, fill_holes=True, blend=0.0, iterations=0)

   Reduce UV stretching by relaxing angles

   :arg fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
   :type fill_holes: boolean, (optional)
   :arg blend: Blend, Blend factor between stretch minimized and original
   :type blend: float in [0, 1], (optional)
   :arg iterations: Iterations, Number of iterations to run, 0 is unlimited when run interactively
   :type iterations: int in [0, inf], (optional)

.. function:: pack_islands(*, udim_source='CLOSEST_UDIM', rotate=True, rotate_method='ANY', scale=True, merge_overlap=False, margin_method='SCALED', margin=0.001, pin=False, pin_method='LOCKED', shape_method='CONCAVE')

   Transform all islands so that they fill up the UV/UDIM space as much as possible

   :arg udim_source: Pack to

      * ``CLOSEST_UDIM``
        Closest UDIM -- Pack islands to closest UDIM.
      * ``ACTIVE_UDIM``
        Active UDIM -- Pack islands to active UDIM image tile or UDIM grid tile where 2D cursor is located.
      * ``ORIGINAL_AABB``
        Original bounding box -- Pack to starting bounding box of islands.
   :type udim_source: enum in [``'CLOSEST_UDIM'``, ``'ACTIVE_UDIM'``, ``'ORIGINAL_AABB'``], (optional)
   :arg rotate: Rotate, Rotate islands to improve layout
   :type rotate: boolean, (optional)
   :arg rotate_method: Rotation Method

      * ``ANY``
        Any -- Any angle is allowed for rotation.
      * ``CARDINAL``
        Cardinal -- Only 90 degree rotations are allowed.
      * ``AXIS_ALIGNED``
        Axis-aligned -- Rotated to a minimal rectangle, either vertical or horizontal.
      * ``AXIS_ALIGNED_X``
        Axis-aligned (Horizontal) -- Rotate islands to be aligned horizontally.
      * ``AXIS_ALIGNED_Y``
        Axis-aligned (Vertical) -- Rotate islands to be aligned vertically.
   :type rotate_method: enum in [``'ANY'``, ``'CARDINAL'``, ``'AXIS_ALIGNED'``, ``'AXIS_ALIGNED_X'``, ``'AXIS_ALIGNED_Y'``], (optional)
   :arg scale: Scale, Scale islands to fill unit square
   :type scale: boolean, (optional)
   :arg merge_overlap: Merge Overlapping, Overlapping islands stick together
   :type merge_overlap: boolean, (optional)
   :arg margin_method: Margin Method

      * ``SCALED``
        Scaled -- Use scale of existing UVs to multiply margin.
      * ``ADD``
        Add -- Just add the margin, ignoring any UV scale.
      * ``FRACTION``
        Fraction -- Specify a precise fraction of final UV output.
   :type margin_method: enum in [``'SCALED'``, ``'ADD'``, ``'FRACTION'``], (optional)
   :arg margin: Margin, Space between islands
   :type margin: float in [0, 1], (optional)
   :arg pin: Lock Pinned Islands, Constrain islands containing any pinned UV's
   :type pin: boolean, (optional)
   :arg pin_method: Pin Method

      * ``SCALE``
        Scale -- Pinned islands won't rescale.
      * ``ROTATION``
        Rotation -- Pinned islands won't rotate.
      * ``ROTATION_SCALE``
        Rotation and Scale -- Pinned islands will translate only.
      * ``LOCKED``
        All -- Pinned islands are locked in place.
   :type pin_method: enum in [``'SCALE'``, ``'ROTATION'``, ``'ROTATION_SCALE'``, ``'LOCKED'``], (optional)
   :arg shape_method: Shape Method

      * ``CONCAVE``
        Exact Shape (Concave) -- Uses exact geometry.
      * ``CONVEX``
        Boundary Shape (Convex) -- Uses convex hull.
      * ``AABB``
        Bounding Box -- Uses bounding boxes.
   :type shape_method: enum in [``'CONCAVE'``, ``'CONVEX'``, ``'AABB'``], (optional)

.. function:: paste()

   Paste selected UV vertices

.. function:: pin(*, clear=False, invert=False)

   Set/clear selected UV vertices as anchored between multiple unwrap operations

   :arg clear: Clear, Clear pinning for the selection instead of setting it
   :type clear: boolean, (optional)
   :arg invert: Invert, Invert pinning for the selection instead of setting it
   :type invert: boolean, (optional)

.. function:: project_from_view(*, orthographic=False, camera_bounds=True, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False)

   Project the UV vertices of the mesh as seen in current 3D view

   :arg orthographic: Orthographic, Use orthographic projection
   :type orthographic: boolean, (optional)
   :arg camera_bounds: Camera Bounds, Map UVs to the camera region taking resolution and aspect into account
   :type camera_bounds: boolean, (optional)
   :arg correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account
   :type correct_aspect: boolean, (optional)
   :arg clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
   :type clip_to_bounds: boolean, (optional)
   :arg scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
   :type scale_to_bounds: boolean, (optional)

.. function:: randomize_uv_transform(*, random_seed=0, use_loc=True, loc=(0.0, 0.0), use_rot=True, rot=0.0, use_scale=True, scale_even=False, scale=(1.0, 1.0))

   Randomize the UV island's location, rotation, and scale

   :arg random_seed: Random Seed, Seed value for the random generator
   :type random_seed: int in [0, 10000], (optional)
   :arg use_loc: Randomize Location, Randomize the location values
   :type use_loc: boolean, (optional)
   :arg loc: Location, Maximum distance the objects can spread over each axis
   :type loc: :class:`mathutils.Vector` of 2 items in [-100, 100], (optional)
   :arg use_rot: Randomize Rotation, Randomize the rotation value
   :type use_rot: boolean, (optional)
   :arg rot: Rotation, Maximum rotation
   :type rot: float in [-6.28319, 6.28319], (optional)
   :arg use_scale: Randomize Scale, Randomize the scale values
   :type use_scale: boolean, (optional)
   :arg scale_even: Scale Even, Use the same scale value for both axes
   :type scale_even: boolean, (optional)
   :arg scale: Scale, Maximum scale randomization over each axis
   :type scale: float array of 2 items in [-100, 100], (optional)
   :File: `startup\bl_operators\uvcalc_transform.py\:473 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\uvcalc_transform.py#L473>`__


.. function:: remove_doubles(*, threshold=0.02, use_unselected=False, use_shared_vertex=False)

   Selected UV vertices that are within a radius of each other are welded together

   :arg threshold: Merge Distance, Maximum distance between welded vertices
   :type threshold: float in [0, 10], (optional)
   :arg use_unselected: Unselected, Merge selected to other unselected vertices
   :type use_unselected: boolean, (optional)
   :arg use_shared_vertex: Shared Vertex, Weld UVs based on shared vertices
   :type use_shared_vertex: boolean, (optional)

.. function:: reset()

   Reset UV projection

.. function:: reveal(*, select=True)

   Reveal all hidden UV vertices

   :arg select: Select
   :type select: boolean, (optional)

.. function:: rip(*, mirror=False, release_confirm=False, use_accurate=False, location=(0.0, 0.0))

   Rip selected vertices or a selected region

   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)
   :arg location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
   :type location: :class:`mathutils.Vector` of 2 items in [-inf, inf], (optional)

.. function:: rip_move(*, UV_OT_rip=None, TRANSFORM_OT_translate=None)

   Unstitch UVs and move the result

   :arg UV_OT_rip: UV Rip, Rip selected vertices or a selected region
   :type UV_OT_rip: :class:`UV_OT_rip`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: seams_from_islands(*, mark_seams=True, mark_sharp=False)

   Set mesh seams according to island setup in the UV editor

   :arg mark_seams: Mark Seams, Mark boundary edges as seams
   :type mark_seams: boolean, (optional)
   :arg mark_sharp: Mark Sharp, Mark boundary edges as sharp
   :type mark_sharp: boolean, (optional)

.. function:: select(*, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, location=(0.0, 0.0))

   Select UV vertices

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
   :arg location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
   :type location: :class:`mathutils.Vector` of 2 items in [-inf, inf], (optional)

.. function:: select_all(*, action='TOGGLE')

   Change selection of all UV vertices

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

.. function:: select_box(*, pinned=False, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Select UV vertices using box selection

   :arg pinned: Pinned, Border select pinned UVs only
   :type pinned: boolean, (optional)
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

.. function:: select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET')

   Select UV vertices using circle selection

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

.. function:: select_edge_ring(*, extend=False, location=(0.0, 0.0))

   Select an edge ring of connected UV vertices

   :arg extend: Extend, Extend selection rather than clearing the existing selection
   :type extend: boolean, (optional)
   :arg location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
   :type location: :class:`mathutils.Vector` of 2 items in [-inf, inf], (optional)

.. function:: select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

   Select UVs using lasso selection

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
   :type mode: enum in [``'SET'``, ``'ADD'``, ``'SUB'``], (optional)

.. function:: select_less()

   Deselect UV vertices at the boundary of each selection region

.. function:: select_linked()

   Select all UV vertices linked to the active UV map

.. function:: select_linked_pick(*, extend=False, deselect=False, location=(0.0, 0.0))

   Select all UV vertices linked under the mouse

   :arg extend: Extend, Extend selection rather than clearing the existing selection
   :type extend: boolean, (optional)
   :arg deselect: Deselect, Deselect linked UV vertices rather than selecting them
   :type deselect: boolean, (optional)
   :arg location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
   :type location: :class:`mathutils.Vector` of 2 items in [-inf, inf], (optional)

.. function:: select_loop(*, extend=False, location=(0.0, 0.0))

   Select a loop of connected UV vertices

   :arg extend: Extend, Extend selection rather than clearing the existing selection
   :type extend: boolean, (optional)
   :arg location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
   :type location: :class:`mathutils.Vector` of 2 items in [-inf, inf], (optional)

.. function:: select_mode(*, type='VERTEX')

   Change UV selection mode

   :arg type: Type
   :type type: enum in :ref:`rna_enum_mesh_select_mode_uv_items`, (optional)

.. function:: select_more()

   Select more UV vertices connected to initial selection

.. function:: select_overlap(*, extend=False)

   Select all UV faces which overlap each other

   :arg extend: Extend, Extend selection rather than clearing the existing selection
   :type extend: boolean, (optional)

.. function:: select_pinned()

   Select all pinned UV vertices

.. function:: select_similar(*, type='PIN', compare='EQUAL', threshold=0.0)

   Select similar UVs by property types

   :arg type: Type
   :type type: enum in [``'PIN'``, ``'LENGTH'``, ``'LENGTH_3D'``, ``'AREA'``, ``'AREA_3D'``, ``'MATERIAL'``, ``'OBJECT'``, ``'SIDES'``, ``'WINDING'``, ``'FACE'``], (optional)
   :arg compare: Compare
   :type compare: enum in [``'EQUAL'``, ``'GREATER'``, ``'LESS'``], (optional)
   :arg threshold: Threshold
   :type threshold: float in [0, 1], (optional)

.. function:: select_split()

   Select only entirely selected faces

.. function:: shortest_path_pick(*, use_face_step=False, use_topology_distance=False, use_fill=False, skip=0, nth=1, offset=0, object_index=-1, index=-1)

   Select shortest path between two selections

   :arg use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
   :type use_face_step: boolean, (optional)
   :arg use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
   :type use_topology_distance: boolean, (optional)
   :arg use_fill: Fill Region, Select all paths between the source/destination elements
   :type use_fill: boolean, (optional)
   :arg skip: Deselected, Number of deselected elements in the repetitive sequence
   :type skip: int in [0, inf], (optional)
   :arg nth: Selected, Number of selected elements in the repetitive sequence
   :type nth: int in [1, inf], (optional)
   :arg offset: Offset, Offset from the starting point
   :type offset: int in [-inf, inf], (optional)
   :type object_index: int in [-1, inf], (optional)
   :type index: int in [-1, inf], (optional)

.. function:: shortest_path_select(*, use_face_step=False, use_topology_distance=False, use_fill=False, skip=0, nth=1, offset=0)

   Selected shortest path between two vertices/edges/faces

   :arg use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
   :type use_face_step: boolean, (optional)
   :arg use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
   :type use_topology_distance: boolean, (optional)
   :arg use_fill: Fill Region, Select all paths between the source/destination elements
   :type use_fill: boolean, (optional)
   :arg skip: Deselected, Number of deselected elements in the repetitive sequence
   :type skip: int in [0, inf], (optional)
   :arg nth: Selected, Number of selected elements in the repetitive sequence
   :type nth: int in [1, inf], (optional)
   :arg offset: Offset, Offset from the starting point
   :type offset: int in [-inf, inf], (optional)

.. function:: smart_project(*, angle_limit=1.15192, margin_method='SCALED', rotate_method='AXIS_ALIGNED_Y', island_margin=0.0, area_weight=0.0, correct_aspect=True, scale_to_bounds=False)

   Projection unwraps the selected faces of mesh objects

   :arg angle_limit: Angle Limit, Lower for more projection groups, higher for less distortion
   :type angle_limit: float in [0, 1.5708], (optional)
   :arg margin_method: Margin Method

      * ``SCALED``
        Scaled -- Use scale of existing UVs to multiply margin.
      * ``ADD``
        Add -- Just add the margin, ignoring any UV scale.
      * ``FRACTION``
        Fraction -- Specify a precise fraction of final UV output.
   :type margin_method: enum in [``'SCALED'``, ``'ADD'``, ``'FRACTION'``], (optional)
   :arg rotate_method: Rotation Method

      * ``AXIS_ALIGNED``
        Axis-aligned -- Rotated to a minimal rectangle, either vertical or horizontal.
      * ``AXIS_ALIGNED_X``
        Axis-aligned (Horizontal) -- Rotate islands to be aligned horizontally.
      * ``AXIS_ALIGNED_Y``
        Axis-aligned (Vertical) -- Rotate islands to be aligned vertically.
   :type rotate_method: enum in [``'AXIS_ALIGNED'``, ``'AXIS_ALIGNED_X'``, ``'AXIS_ALIGNED_Y'``], (optional)
   :arg island_margin: Island Margin, Margin to reduce bleed from adjacent islands
   :type island_margin: float in [0, 1], (optional)
   :arg area_weight: Area Weight, Weight projection's vector by faces with larger areas
   :type area_weight: float in [0, 1], (optional)
   :arg correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account
   :type correct_aspect: boolean, (optional)
   :arg scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
   :type scale_to_bounds: boolean, (optional)

.. function:: snap_cursor(*, target='PIXELS')

   Snap cursor to target type

   :arg target: Target, Target to snap the selected UVs to
   :type target: enum in [``'PIXELS'``, ``'SELECTED'``, ``'ORIGIN'``], (optional)

.. function:: snap_selected(*, target='PIXELS')

   Snap selected UV vertices to target type

   :arg target: Target, Target to snap the selected UVs to
   :type target: enum in [``'PIXELS'``, ``'CURSOR'``, ``'CURSOR_OFFSET'``, ``'ADJACENT_UNSELECTED'``], (optional)

.. function:: sphere_project(*, direction='VIEW_ON_EQUATOR', align='POLAR_ZX', pole='PINCH', seam=False, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False)

   Project the UV vertices of the mesh over the curved surface of a sphere

   :arg direction: Direction, Direction of the sphere or cylinder

      * ``VIEW_ON_EQUATOR``
        View on Equator -- 3D view is on the equator.
      * ``VIEW_ON_POLES``
        View on Poles -- 3D view is on the poles.
      * ``ALIGN_TO_OBJECT``
        Align to Object -- Align according to object transform.
   :type direction: enum in [``'VIEW_ON_EQUATOR'``, ``'VIEW_ON_POLES'``, ``'ALIGN_TO_OBJECT'``], (optional)
   :arg align: Align, How to determine rotation around the pole

      * ``POLAR_ZX``
        Polar ZX -- Polar 0 is X.
      * ``POLAR_ZY``
        Polar ZY -- Polar 0 is Y.
   :type align: enum in [``'POLAR_ZX'``, ``'POLAR_ZY'``], (optional)
   :arg pole: Pole, How to handle faces at the poles

      * ``PINCH``
        Pinch -- UVs are pinched at the poles.
      * ``FAN``
        Fan -- UVs are fanned at the poles.
   :type pole: enum in [``'PINCH'``, ``'FAN'``], (optional)
   :arg seam: Preserve Seams, Separate projections by islands isolated by seams
   :type seam: boolean, (optional)
   :arg correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account
   :type correct_aspect: boolean, (optional)
   :arg clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
   :type clip_to_bounds: boolean, (optional)
   :arg scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
   :type scale_to_bounds: boolean, (optional)

.. function:: stitch(*, use_limit=False, snap_islands=True, limit=0.01, static_island=0, active_object_index=0, midpoint_snap=False, clear_seams=True, mode='VERTEX', stored_mode='VERTEX', selection=None, objects_selection_count=(0, 0, 0, 0, 0, 0))

   Stitch selected UV vertices by proximity

   :arg use_limit: Use Limit, Stitch UVs within a specified limit distance
   :type use_limit: boolean, (optional)
   :arg snap_islands: Snap Islands, Snap islands together (on edge stitch mode, rotates the islands too)
   :type snap_islands: boolean, (optional)
   :arg limit: Limit, Limit distance in normalized coordinates
   :type limit: float in [0, inf], (optional)
   :arg static_island: Static Island, Island that stays in place when stitching islands
   :type static_island: int in [0, inf], (optional)
   :arg active_object_index: Active Object, Index of the active object
   :type active_object_index: int in [0, inf], (optional)
   :arg midpoint_snap: Snap at Midpoint, UVs are stitched at midpoint instead of at static island
   :type midpoint_snap: boolean, (optional)
   :arg clear_seams: Clear Seams, Clear seams of stitched edges
   :type clear_seams: boolean, (optional)
   :arg mode: Operation Mode, Use vertex or edge stitching
   :type mode: enum in [``'VERTEX'``, ``'EDGE'``], (optional)
   :arg stored_mode: Stored Operation Mode, Use vertex or edge stitching
   :type stored_mode: enum in [``'VERTEX'``, ``'EDGE'``], (optional)
   :arg selection: Selection
   :type selection: :class:`bpy_prop_collection` of :class:`SelectedUvElement`, (optional)
   :arg objects_selection_count: Objects Selection Count
   :type objects_selection_count: int array of 6 items in [0, inf], (optional)

.. function:: unwrap(*, method='CONFORMAL', fill_holes=False, correct_aspect=True, use_subsurf_data=False, margin_method='SCALED', margin=0.001, no_flip=False, iterations=10, use_weights=False, weight_group="uv_importance", weight_factor=1.0)

   Unwrap the mesh of the object being edited

   :arg method: Method, Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower)
   :type method: enum in [``'ANGLE_BASED'``, ``'CONFORMAL'``, ``'MINIMUM_STRETCH'``], (optional)
   :arg fill_holes: Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
   :type fill_holes: boolean, (optional)
   :arg correct_aspect: Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account
   :type correct_aspect: boolean, (optional)
   :arg use_subsurf_data: Use Subdivision Surface, Map UVs taking vertex position after Subdivision Surface modifier has been applied
   :type use_subsurf_data: boolean, (optional)
   :arg margin_method: Margin Method

      * ``SCALED``
        Scaled -- Use scale of existing UVs to multiply margin.
      * ``ADD``
        Add -- Just add the margin, ignoring any UV scale.
      * ``FRACTION``
        Fraction -- Specify a precise fraction of final UV output.
   :type margin_method: enum in [``'SCALED'``, ``'ADD'``, ``'FRACTION'``], (optional)
   :arg margin: Margin, Space between islands
   :type margin: float in [0, 1], (optional)
   :arg no_flip: No Flip, Prevent flipping UV's, flipping may lower distortion depending on the position of pins
   :type no_flip: boolean, (optional)
   :arg iterations: Iterations, Number of iterations when "Minimum Stretch" method is used
   :type iterations: int in [0, 10000], (optional)
   :arg use_weights: Importance Weights, Whether to take into account per-vertex importance weights
   :type use_weights: boolean, (optional)
   :arg weight_group: Weight Group, Vertex group name for importance weights (modulating the deform)
   :type weight_group: string, (optional, never None)
   :arg weight_factor: Weight Factor, How much influence the weightmap has for weighted parameterization, 0 being no influence
   :type weight_factor: float in [-10000, 10000], (optional)

.. function:: weld()

   Weld selected UV vertices together

