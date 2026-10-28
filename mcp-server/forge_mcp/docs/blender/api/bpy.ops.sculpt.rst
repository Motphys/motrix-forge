Sculpt Operators
================

.. module:: bpy.ops.sculpt

.. function:: brush_stroke(*, stroke=None, mode='NORMAL', pen_flip=False, override_location=False, ignore_background_click=False)

   Sculpt a stroke into the geometry

   :arg stroke: Stroke
   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg mode: Stroke Mode, Action taken when a paint stroke is made

      * ``NORMAL``
        Regular -- Apply brush normally.
      * ``INVERT``
        Invert -- Invert action of brush for duration of stroke.
      * ``SMOOTH``
        Smooth -- Switch brush to smooth mode for duration of stroke.
      * ``ERASE``
        Erase -- Switch brush to erase mode for duration of stroke.
   :type mode: enum in [``'NORMAL'``, ``'INVERT'``, ``'SMOOTH'``, ``'ERASE'``], (optional)
   :arg pen_flip: Pen Flip, Whether a tablet's eraser mode is being used
   :type pen_flip: boolean, (optional)
   :arg override_location: Override Location, Override the given `location` array by recalculating object space positions from the provided `mouse_event` positions
   :type override_location: boolean, (optional)
   :arg ignore_background_click: Ignore Background Click, Clicks on the background do not start the stroke
   :type ignore_background_click: boolean, (optional)

.. function:: cloth_filter(*, start_mouse=(0, 0), area_normal_radius=0.25, strength=1.0, iteration_count=1, event_history=None, type='GRAVITY', force_axis={'X', 'Y', 'Z'}, orientation='LOCAL', cloth_mass=1.0, cloth_damping=0.0, use_face_sets=False, use_collisions=False)

   Applies a cloth simulation deformation to the entire mesh

   :arg start_mouse: Starting Mouse
   :type start_mouse: int array of 2 items in [0, 16384], (optional)
   :arg area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
   :type area_normal_radius: float in [0.001, 5], (optional)
   :arg strength: Strength, Filter strength
   :type strength: float in [-10, 10], (optional)
   :arg iteration_count: Repeat, How many times to repeat the filter
   :type iteration_count: int in [1, 10000], (optional)
   :type event_history: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg type: Filter Type, Operation that is going to be applied to the mesh

      * ``GRAVITY``
        Gravity -- Applies gravity to the simulation.
      * ``INFLATE``
        Inflate -- Inflates the cloth.
      * ``EXPAND``
        Expand -- Expands the cloth's dimensions.
      * ``PINCH``
        Pinch -- Pulls the cloth to the cursor's start position.
      * ``SCALE``
        Scale -- Scales the mesh as a soft body using the origin of the object as scale.
   :type type: enum in [``'GRAVITY'``, ``'INFLATE'``, ``'EXPAND'``, ``'PINCH'``, ``'SCALE'``], (optional)
   :arg force_axis: Force Axis, Apply the force in the selected axis

      * ``X``
        X -- Apply force in the X axis.
      * ``Y``
        Y -- Apply force in the Y axis.
      * ``Z``
        Z -- Apply force in the Z axis.
   :type force_axis: enum set in {``'X'``, ``'Y'``, ``'Z'``}, (optional)
   :arg orientation: Orientation, Orientation of the axis to limit the filter force

      * ``LOCAL``
        Local -- Use the local axis to limit the force and set the gravity direction.
      * ``WORLD``
        World -- Use the global axis to limit the force and set the gravity direction.
      * ``VIEW``
        View -- Use the view axis to limit the force and set the gravity direction.
   :type orientation: enum in [``'LOCAL'``, ``'WORLD'``, ``'VIEW'``], (optional)
   :arg cloth_mass: Cloth Mass, Mass of each simulation particle
   :type cloth_mass: float in [0, 2], (optional)
   :arg cloth_damping: Cloth Damping, How much the applied forces are propagated through the cloth
   :type cloth_damping: float in [0, 1], (optional)
   :arg use_face_sets: Use Face Sets, Apply the filter only to the Face Set under the cursor
   :type use_face_sets: boolean, (optional)
   :arg use_collisions: Use Collisions, Collide with other collider objects in the scene
   :type use_collisions: boolean, (optional)

.. function:: color_filter(*, start_mouse=(0, 0), area_normal_radius=0.25, strength=1.0, iteration_count=1, event_history=None, type='FILL', fill_color=(1.0, 1.0, 1.0))

   Applies a filter to modify the active color attribute

   :arg start_mouse: Starting Mouse
   :type start_mouse: int array of 2 items in [0, 16384], (optional)
   :arg area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
   :type area_normal_radius: float in [0.001, 5], (optional)
   :arg strength: Strength, Filter strength
   :type strength: float in [-10, 10], (optional)
   :arg iteration_count: Repeat, How many times to repeat the filter
   :type iteration_count: int in [1, 10000], (optional)
   :type event_history: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg type: Filter Type

      * ``FILL``
        Fill -- Fill with a specific color.
      * ``HUE``
        Hue -- Change hue.
      * ``SATURATION``
        Saturation -- Change saturation.
      * ``VALUE``
        Value -- Change value.
      * ``BRIGHTNESS``
        Brightness -- Change brightness.
      * ``CONTRAST``
        Contrast -- Change contrast.
      * ``SMOOTH``
        Smooth -- Smooth colors.
      * ``RED``
        Red -- Change red channel.
      * ``GREEN``
        Green -- Change green channel.
      * ``BLUE``
        Blue -- Change blue channel.
   :type type: enum in [``'FILL'``, ``'HUE'``, ``'SATURATION'``, ``'VALUE'``, ``'BRIGHTNESS'``, ``'CONTRAST'``, ``'SMOOTH'``, ``'RED'``, ``'GREEN'``, ``'BLUE'``], (optional)
   :arg fill_color: Fill Color
   :type fill_color: :class:`mathutils.Color` of 3 items in [0, inf], (optional)

.. function:: detail_flood_fill()

   Flood fill the mesh with the selected detail setting

.. function:: dynamic_topology_toggle()

   Dynamic topology alters the mesh topology while sculpting

.. function:: dyntopo_detail_size_edit()

   Modify the detail size of dyntopo interactively

.. function:: expand(*, target='MASK', falloff_type='GEODESIC', invert=False, use_mask_preserve=False, use_falloff_gradient=False, use_modify_active=False, use_reposition_pivot=True, max_geodesic_move_preview=10000, use_auto_mask=False, normal_falloff_smooth=2)

   Generic sculpt expand operator

   :arg target: Data Target, Data that is going to be modified in the expand operation
   :type target: enum in [``'MASK'``, ``'FACE_SETS'``, ``'COLOR'``], (optional)
   :arg falloff_type: Falloff Type, Initial falloff of the expand operation
   :type falloff_type: enum in [``'GEODESIC'``, ``'TOPOLOGY'``, ``'TOPOLOGY_DIAGONALS'``, ``'NORMALS'``, ``'SPHERICAL'``, ``'BOUNDARY_TOPOLOGY'``, ``'BOUNDARY_FACE_SET'``, ``'ACTIVE_FACE_SET'``], (optional)
   :arg invert: Invert, Invert the expand active elements
   :type invert: boolean, (optional)
   :arg use_mask_preserve: Preserve Previous, Preserve the previous state of the target data
   :type use_mask_preserve: boolean, (optional)
   :arg use_falloff_gradient: Falloff Gradient, Expand Using a linear falloff
   :type use_falloff_gradient: boolean, (optional)
   :arg use_modify_active: Modify Active, Modify the active Face Set instead of creating a new one
   :type use_modify_active: boolean, (optional)
   :arg use_reposition_pivot: Reposition Pivot, Reposition the sculpt transform pivot to the boundary of the expand active area
   :type use_reposition_pivot: boolean, (optional)
   :arg max_geodesic_move_preview: Max Vertex Count for Geodesic Move Preview, Maximum number of vertices in the mesh for using geodesic falloff when moving the origin of expand. If the total number of vertices is greater than this value, the falloff will be set to spherical when moving
   :type max_geodesic_move_preview: int in [0, inf], (optional)
   :arg use_auto_mask: Auto Create, Fill in mask if nothing is already masked
   :type use_auto_mask: boolean, (optional)
   :arg normal_falloff_smooth: Normal Smooth, Blurring steps for normal falloff
   :type normal_falloff_smooth: int in [0, 10], (optional)

.. function:: face_set_box_gesture(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, use_front_faces_only=False)

   Add a face set in a rectangle defined by the cursor

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
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)

.. function:: face_set_change_visibility(*, mode='TOGGLE')

   Change the visibility of the Face Sets of the sculpt

   :arg mode: Mode

      * ``TOGGLE``
        Toggle Visibility -- Hide all Face Sets except for the active one.
      * ``SHOW_ACTIVE``
        Show Active Face Set -- Show Active Face Set.
      * ``HIDE_ACTIVE``
        Hide Active Face Sets -- Hide Active Face Sets.
   :type mode: enum in [``'TOGGLE'``, ``'SHOW_ACTIVE'``, ``'HIDE_ACTIVE'``], (optional)

.. function:: face_set_edit(*, active_face_set=1, mode='GROW', strength=1.0, modify_hidden=False)

   Edits the current active Face Set

   :arg active_face_set: Active Face Set
   :type active_face_set: int in [0, inf], (optional)
   :arg mode: Mode

      * ``GROW``
        Grow Face Set -- Grows the Face Sets boundary by one face based on mesh topology.
      * ``SHRINK``
        Shrink Face Set -- Shrinks the Face Sets boundary by one face based on mesh topology.
      * ``DELETE_GEOMETRY``
        Delete Geometry -- Deletes the faces that are assigned to the Face Set.
      * ``FAIR_POSITIONS``
        Fair Positions -- Creates a smooth as possible geometry patch from the Face Set minimizing changes in vertex positions.
      * ``FAIR_TANGENCY``
        Fair Tangency -- Creates a smooth as possible geometry patch from the Face Set minimizing changes in vertex tangents.
   :type mode: enum in [``'GROW'``, ``'SHRINK'``, ``'DELETE_GEOMETRY'``, ``'FAIR_POSITIONS'``, ``'FAIR_TANGENCY'``], (optional)
   :arg strength: Strength
   :type strength: float in [0, 1], (optional)
   :arg modify_hidden: Modify Hidden, Apply the edit operation to hidden geometry
   :type modify_hidden: boolean, (optional)

.. function:: face_set_extract(*, add_boundary_loop=True, smooth_iterations=4, apply_shrinkwrap=True, add_solidify=True)

   Create a new mesh object from the selected Face Set

   :arg add_boundary_loop: Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier
   :type add_boundary_loop: boolean, (optional)
   :arg smooth_iterations: Smooth Iterations, Smooth iterations applied to the extracted mesh
   :type smooth_iterations: int in [0, inf], (optional)
   :arg apply_shrinkwrap: Project to Sculpt, Project the extracted mesh into the original sculpt
   :type apply_shrinkwrap: boolean, (optional)
   :arg add_solidify: Extract as Solid, Extract the mask as a solid object with a solidify modifier
   :type add_solidify: boolean, (optional)

.. function:: face_set_lasso_gesture(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, use_front_faces_only=False)

   Add a face set in a shape defined by the cursor

   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
   :type use_smooth_stroke: boolean, (optional)
   :arg smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
   :type smooth_stroke_factor: float in [0.5, 0.99], (optional)
   :arg smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
   :type smooth_stroke_radius: int in [10, 200], (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)

.. function:: face_set_line_gesture(*, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5, use_front_faces_only=False, use_limit_to_segment=False)

   Add a face set to one side of a line defined by the cursor

   :arg xstart: X Start
   :type xstart: int in [-inf, inf], (optional)
   :arg xend: X End
   :type xend: int in [-inf, inf], (optional)
   :arg ystart: Y Start
   :type ystart: int in [-inf, inf], (optional)
   :arg yend: Y End
   :type yend: int in [-inf, inf], (optional)
   :arg flip: Flip
   :type flip: boolean, (optional)
   :arg cursor: Cursor, Mouse cursor style to use during the modal operator
   :type cursor: int in [0, inf], (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)
   :arg use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
   :type use_limit_to_segment: boolean, (optional)

.. function:: face_set_polyline_gesture(*, path=None, use_front_faces_only=False)

   Add a face set in a shape defined by the cursor

   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)

.. function:: face_sets_create(*, mode='MASKED')

   Create a new Face Set

   :arg mode: Mode

      * ``MASKED``
        Face Set from Masked -- Create a new Face Set from the masked faces.
      * ``VISIBLE``
        Face Set from Visible -- Create a new Face Set from the visible vertices.
      * ``ALL``
        Face Set Full Mesh -- Create an unique Face Set with all faces in the sculpt.
      * ``SELECTION``
        Face Set from Edit Mode Selection -- Create an Face Set corresponding to the Edit Mode face selection.
   :type mode: enum in [``'MASKED'``, ``'VISIBLE'``, ``'ALL'``, ``'SELECTION'``], (optional)

.. function:: face_sets_init(*, mode='LOOSE_PARTS', threshold=0.5)

   Initializes all Face Sets in the mesh

   :arg mode: Mode

      * ``LOOSE_PARTS``
        Face Sets from Loose Parts -- Create a Face Set per loose part in the mesh.
      * ``MATERIALS``
        Face Sets from Material Slots -- Create a Face Set per Material Slot.
      * ``NORMALS``
        Face Sets from Mesh Normals -- Create Face Sets for Faces that have similar normal.
      * ``UV_SEAMS``
        Face Sets from UV Seams -- Create Face Sets using UV Seams as boundaries.
      * ``CREASES``
        Face Sets from Edge Creases -- Create Face Sets using Edge Creases as boundaries.
      * ``BEVEL_WEIGHT``
        Face Sets from Bevel Weight -- Create Face Sets using Bevel Weights as boundaries.
      * ``SHARP_EDGES``
        Face Sets from Sharp Edges -- Create Face Sets using Sharp Edges as boundaries.
      * ``FACE_SET_BOUNDARIES``
        Face Sets from Face Set Boundaries -- Create a Face Set per isolated Face Set.
   :type mode: enum in [``'LOOSE_PARTS'``, ``'MATERIALS'``, ``'NORMALS'``, ``'UV_SEAMS'``, ``'CREASES'``, ``'BEVEL_WEIGHT'``, ``'SHARP_EDGES'``, ``'FACE_SET_BOUNDARIES'``], (optional)
   :arg threshold: Threshold, Minimum value to consider a certain attribute a boundary when creating the Face Sets
   :type threshold: float in [0, 1], (optional)

.. function:: face_sets_randomize_colors()

   Generates a new set of random colors to render the Face Sets in the viewport

.. function:: mask_by_color(*, contiguous=False, invert=False, preserve_previous_mask=False, threshold=0.35, location=(0, 0))

   Creates a mask based on the active color attribute

   :arg contiguous: Contiguous, Mask only contiguous color areas
   :type contiguous: boolean, (optional)
   :arg invert: Invert, Invert the generated mask
   :type invert: boolean, (optional)
   :arg preserve_previous_mask: Preserve Previous Mask, Preserve the previous mask and add or subtract the new one generated by the colors
   :type preserve_previous_mask: boolean, (optional)
   :arg threshold: Threshold, How much changes in color affect the mask generation
   :type threshold: float in [0, 1], (optional)
   :arg location: Location, Region coordinates of sampling
   :type location: int array of 2 items in [0, 32767], (optional)

.. function:: mask_filter(*, filter_type='SMOOTH', iterations=1, auto_iteration_count=True)

   Applies a filter to modify the current mask

   :arg filter_type: Type, Filter that is going to be applied to the mask
   :type filter_type: enum in [``'SMOOTH'``, ``'SHARPEN'``, ``'GROW'``, ``'SHRINK'``, ``'CONTRAST_INCREASE'``, ``'CONTRAST_DECREASE'``], (optional)
   :arg iterations: Iterations, Number of times that the filter is going to be applied
   :type iterations: int in [1, 100], (optional)
   :arg auto_iteration_count: Auto Iteration Count, Use an automatic number of iterations based on the number of vertices of the sculpt
   :type auto_iteration_count: boolean, (optional)

.. function:: mask_from_boundary(*, mix_mode='MIX', mix_factor=1.0, settings_source='OPERATOR', boundary_mode='MESH', propagation_steps=1)

   Creates a mask based on the boundaries of the surface

   :arg mix_mode: Mode, Mix mode
   :type mix_mode: enum in [``'MIX'``, ``'MULTIPLY'``, ``'DIVIDE'``, ``'ADD'``, ``'SUBTRACT'``], (optional)
   :arg mix_factor: Mix Factor
   :type mix_factor: float in [0, 5], (optional)
   :arg settings_source: Settings, Use settings from here

      * ``OPERATOR``
        Operator -- Use settings from operator properties.
      * ``BRUSH``
        Brush -- Use settings from brush.
      * ``SCENE``
        Scene -- Use settings from scene.
   :type settings_source: enum in [``'OPERATOR'``, ``'BRUSH'``, ``'SCENE'``], (optional)
   :arg boundary_mode: Mode, Boundary type to mask

      * ``MESH``
        Mesh -- Calculate the boundary mask based on disconnected mesh topology islands.
      * ``FACE_SETS``
        Face Sets -- Calculate the boundary mask between face sets.
   :type boundary_mode: enum in [``'MESH'``, ``'FACE_SETS'``], (optional)
   :arg propagation_steps: Propagation Steps
   :type propagation_steps: int in [1, 20], (optional)

.. function:: mask_from_cavity(*, mix_mode='MIX', mix_factor=1.0, settings_source='OPERATOR', factor=0.5, blur_steps=2, use_curve=False, invert=False)

   Creates a mask based on the curvature of the surface

   :arg mix_mode: Mode, Mix mode
   :type mix_mode: enum in [``'MIX'``, ``'MULTIPLY'``, ``'DIVIDE'``, ``'ADD'``, ``'SUBTRACT'``], (optional)
   :arg mix_factor: Mix Factor
   :type mix_factor: float in [0, 5], (optional)
   :arg settings_source: Settings, Use settings from here

      * ``OPERATOR``
        Operator -- Use settings from operator properties.
      * ``BRUSH``
        Brush -- Use settings from brush.
      * ``SCENE``
        Scene -- Use settings from scene.
   :type settings_source: enum in [``'OPERATOR'``, ``'BRUSH'``, ``'SCENE'``], (optional)
   :arg factor: Factor, The contrast of the cavity mask
   :type factor: float in [0, 5], (optional)
   :arg blur_steps: Blur, The number of times the cavity mask is blurred
   :type blur_steps: int in [0, 25], (optional)
   :arg use_curve: Custom Curve
   :type use_curve: boolean, (optional)
   :arg invert: Cavity (Inverted)
   :type invert: boolean, (optional)

.. function:: mask_init(*, mode='RANDOM_PER_VERTEX')

   Creates a new mask for the entire mesh

   :arg mode: Mode
   :type mode: enum in [``'RANDOM_PER_VERTEX'``, ``'RANDOM_PER_FACE_SET'``, ``'RANDOM_PER_LOOSE_PART'``], (optional)

.. function:: mesh_filter(*, start_mouse=(0, 0), area_normal_radius=0.25, strength=1.0, iteration_count=1, event_history=None, type='INFLATE', deform_axis={'X', 'Y', 'Z'}, orientation='LOCAL', surface_smooth_shape_preservation=0.5, surface_smooth_current_vertex=0.5, sharpen_smooth_ratio=0.35, sharpen_intensify_detail_strength=0.0, sharpen_curvature_smooth_iterations=0)

   Applies a filter to modify the current mesh

   :arg start_mouse: Starting Mouse
   :type start_mouse: int array of 2 items in [0, 16384], (optional)
   :arg area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
   :type area_normal_radius: float in [0.001, 5], (optional)
   :arg strength: Strength, Filter strength
   :type strength: float in [-10, 10], (optional)
   :arg iteration_count: Repeat, How many times to repeat the filter
   :type iteration_count: int in [1, 10000], (optional)
   :type event_history: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg type: Filter Type, Operation that is going to be applied to the mesh

      * ``SMOOTH``
        Smooth -- Smooth mesh.
      * ``SCALE``
        Scale -- Scale mesh.
      * ``INFLATE``
        Inflate -- Inflate mesh.
      * ``SPHERE``
        Sphere -- Morph into sphere.
      * ``RANDOM``
        Random -- Randomize vertex positions.
      * ``RELAX``
        Relax -- Relax mesh.
      * ``RELAX_FACE_SETS``
        Relax Face Sets -- Smooth the edges of all the Face Sets.
      * ``SURFACE_SMOOTH``
        Surface Smooth -- Smooth the surface of the mesh, preserving the volume.
      * ``SHARPEN``
        Sharpen -- Sharpen the cavities of the mesh.
      * ``ENHANCE_DETAILS``
        Enhance Details -- Enhance the high frequency surface detail.
      * ``ERASE_DISPLACEMENT``
        Erase Displacement -- Deletes the displacement of the Multires Modifier.
   :type type: enum in [``'SMOOTH'``, ``'SCALE'``, ``'INFLATE'``, ``'SPHERE'``, ``'RANDOM'``, ``'RELAX'``, ``'RELAX_FACE_SETS'``, ``'SURFACE_SMOOTH'``, ``'SHARPEN'``, ``'ENHANCE_DETAILS'``, ``'ERASE_DISPLACEMENT'``], (optional)
   :arg deform_axis: Deform Axis, Apply the deformation in the selected axis

      * ``X``
        X -- Deform in the X axis.
      * ``Y``
        Y -- Deform in the Y axis.
      * ``Z``
        Z -- Deform in the Z axis.
   :type deform_axis: enum set in {``'X'``, ``'Y'``, ``'Z'``}, (optional)
   :arg orientation: Orientation, Orientation of the axis to limit the filter displacement

      * ``LOCAL``
        Local -- Use the local axis to limit the displacement.
      * ``WORLD``
        World -- Use the global axis to limit the displacement.
      * ``VIEW``
        View -- Use the view axis to limit the displacement.
   :type orientation: enum in [``'LOCAL'``, ``'WORLD'``, ``'VIEW'``], (optional)
   :arg surface_smooth_shape_preservation: Shape Preservation, How much of the original shape is preserved when smoothing
   :type surface_smooth_shape_preservation: float in [0, 1], (optional)
   :arg surface_smooth_current_vertex: Per Vertex Displacement, How much the position of each individual vertex influences the final result
   :type surface_smooth_current_vertex: float in [0, 1], (optional)
   :arg sharpen_smooth_ratio: Smooth Ratio, How much smoothing is applied to polished surfaces
   :type sharpen_smooth_ratio: float in [0, 1], (optional)
   :arg sharpen_intensify_detail_strength: Intensify Details, How much creases and valleys are intensified
   :type sharpen_intensify_detail_strength: float in [0, 10], (optional)
   :arg sharpen_curvature_smooth_iterations: Curvature Smooth Iterations, How much smooth the resulting shape is, ignoring high frequency details
   :type sharpen_curvature_smooth_iterations: int in [0, 10], (optional)

.. function:: optimize()

   Recalculate the sculpt BVH to improve performance

.. function:: paint_mask_extract(*, mask_threshold=0.5, add_boundary_loop=True, smooth_iterations=4, apply_shrinkwrap=True, add_solidify=True)

   Create a new mesh object from the current paint mask

   :arg mask_threshold: Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh
   :type mask_threshold: float in [0, 1], (optional)
   :arg add_boundary_loop: Add Boundary Loop, Add an extra edge loop to better preserve the shape when applying a subdivision surface modifier
   :type add_boundary_loop: boolean, (optional)
   :arg smooth_iterations: Smooth Iterations, Smooth iterations applied to the extracted mesh
   :type smooth_iterations: int in [0, inf], (optional)
   :arg apply_shrinkwrap: Project to Sculpt, Project the extracted mesh into the original sculpt
   :type apply_shrinkwrap: boolean, (optional)
   :arg add_solidify: Extract as Solid, Extract the mask as a solid object with a solidify modifier
   :type add_solidify: boolean, (optional)

.. function:: paint_mask_slice(*, mask_threshold=0.5, fill_holes=True, new_object=True)

   Slices the paint mask from the mesh

   :arg mask_threshold: Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh
   :type mask_threshold: float in [0, 1], (optional)
   :arg fill_holes: Fill Holes, Fill holes after slicing the mask
   :type fill_holes: boolean, (optional)
   :arg new_object: Slice to New Object, Create a new object from the sliced mask
   :type new_object: boolean, (optional)

.. function:: project_line_gesture(*, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5, use_front_faces_only=False, use_limit_to_segment=False)

   Project the geometry onto a plane defined by a line

   :arg xstart: X Start
   :type xstart: int in [-inf, inf], (optional)
   :arg xend: X End
   :type xend: int in [-inf, inf], (optional)
   :arg ystart: Y Start
   :type ystart: int in [-inf, inf], (optional)
   :arg yend: Y End
   :type yend: int in [-inf, inf], (optional)
   :arg flip: Flip
   :type flip: boolean, (optional)
   :arg cursor: Cursor, Mouse cursor style to use during the modal operator
   :type cursor: int in [0, inf], (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)
   :arg use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
   :type use_limit_to_segment: boolean, (optional)

.. function:: sample_color()

   Sample the vertex color of the active vertex

.. function:: sample_detail_size(*, location=(0, 0), mode='DYNTOPO')

   Sample the mesh detail on clicked point

   :arg location: Location, Screen coordinates of sampling
   :type location: int array of 2 items in [0, 32767], (optional)
   :arg mode: Detail Mode, Target sculpting workflow that is going to use the sampled size

      * ``DYNTOPO``
        Dyntopo -- Sample dyntopo detail.
      * ``VOXEL``
        Voxel -- Sample mesh voxel size.
   :type mode: enum in [``'DYNTOPO'``, ``'VOXEL'``], (optional)

.. function:: sculptmode_toggle()

   Toggle sculpt mode in 3D view

.. function:: set_persistent_base()

   Reset the copy of the mesh that is being sculpted on

.. function:: set_pivot_position(*, mode='UNMASKED', mouse_x=0.0, mouse_y=0.0)

   Sets the sculpt transform pivot position

   :arg mode: Mode

      * ``ORIGIN``
        Origin -- Sets the pivot to the origin of the sculpt.
      * ``UNMASKED``
        Unmasked -- Sets the pivot position to the average position of the unmasked vertices.
      * ``BORDER``
        Mask Border -- Sets the pivot position to the center of the border of the mask.
      * ``ACTIVE``
        Active Vertex -- Sets the pivot position to the active vertex position.
      * ``SURFACE``
        Surface -- Sets the pivot position to the surface under the cursor.
   :type mode: enum in [``'ORIGIN'``, ``'UNMASKED'``, ``'BORDER'``, ``'ACTIVE'``, ``'SURFACE'``], (optional)
   :arg mouse_x: Mouse Position X, Position of the mouse used for "Surface" and "Active Vertex" mode
   :type mouse_x: float in [0, inf], (optional)
   :arg mouse_y: Mouse Position Y, Position of the mouse used for "Surface" and "Active Vertex" mode
   :type mouse_y: float in [0, inf], (optional)

.. function:: symmetrize(*, merge_tolerance=0.0005)

   Symmetrize the topology modifications

   :arg merge_tolerance: Merge Distance, Distance within which symmetrical vertices are merged
   :type merge_tolerance: float in [0, inf], (optional)

.. function:: trim_box_gesture(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, use_front_faces_only=False, location=(0, 0), trim_mode='DIFFERENCE', use_cursor_depth=False, trim_orientation='VIEW', trim_extrude_mode='FIXED', trim_solver='MANIFOLD')

   Execute a boolean operation on the mesh and a rectangle defined by the cursor

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
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)
   :arg location: Location, Mouse location
   :type location: int array of 2 items in [-inf, inf], (optional)
   :arg trim_mode: Trim Mode

      * ``DIFFERENCE``
        Difference -- Use a difference boolean operation.
      * ``UNION``
        Union -- Use a union boolean operation.
      * ``JOIN``
        Join -- Join the new mesh as separate geometry, without performing any boolean operation.
   :type trim_mode: enum in [``'DIFFERENCE'``, ``'UNION'``, ``'JOIN'``], (optional)
   :arg use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
   :type use_cursor_depth: boolean, (optional)
   :arg trim_orientation: Shape Orientation

      * ``VIEW``
        View -- Use the view to orientate the trimming shape.
      * ``SURFACE``
        Surface -- Use the surface normal to orientate the trimming shape.
   :type trim_orientation: enum in [``'VIEW'``, ``'SURFACE'``], (optional)
   :arg trim_extrude_mode: Extrude Mode

      * ``PROJECT``
        Project -- Align trim geometry with the perspective of the current view for a tapered shape.
      * ``FIXED``
        Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
   :type trim_extrude_mode: enum in [``'PROJECT'``, ``'FIXED'``], (optional)
   :arg trim_solver: Solver

      * ``EXACT``
        Exact -- Slower solver with the best results for coplanar faces.
      * ``FLOAT``
        Float -- Simple solver with good performance, without support for overlapping geometry.
      * ``MANIFOLD``
        Manifold -- Fastest solver that works only on manifold meshes but gives better results.
   :type trim_solver: enum in [``'EXACT'``, ``'FLOAT'``, ``'MANIFOLD'``], (optional)

.. function:: trim_lasso_gesture(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, use_front_faces_only=False, location=(0, 0), trim_mode='DIFFERENCE', use_cursor_depth=False, trim_orientation='VIEW', trim_extrude_mode='FIXED', trim_solver='MANIFOLD')

   Execute a boolean operation on the mesh and a shape defined by the cursor

   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
   :type use_smooth_stroke: boolean, (optional)
   :arg smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
   :type smooth_stroke_factor: float in [0.5, 0.99], (optional)
   :arg smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
   :type smooth_stroke_radius: int in [10, 200], (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)
   :arg location: Location, Mouse location
   :type location: int array of 2 items in [-inf, inf], (optional)
   :arg trim_mode: Trim Mode

      * ``DIFFERENCE``
        Difference -- Use a difference boolean operation.
      * ``UNION``
        Union -- Use a union boolean operation.
      * ``JOIN``
        Join -- Join the new mesh as separate geometry, without performing any boolean operation.
   :type trim_mode: enum in [``'DIFFERENCE'``, ``'UNION'``, ``'JOIN'``], (optional)
   :arg use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
   :type use_cursor_depth: boolean, (optional)
   :arg trim_orientation: Shape Orientation

      * ``VIEW``
        View -- Use the view to orientate the trimming shape.
      * ``SURFACE``
        Surface -- Use the surface normal to orientate the trimming shape.
   :type trim_orientation: enum in [``'VIEW'``, ``'SURFACE'``], (optional)
   :arg trim_extrude_mode: Extrude Mode

      * ``PROJECT``
        Project -- Align trim geometry with the perspective of the current view for a tapered shape.
      * ``FIXED``
        Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
   :type trim_extrude_mode: enum in [``'PROJECT'``, ``'FIXED'``], (optional)
   :arg trim_solver: Solver

      * ``EXACT``
        Exact -- Slower solver with the best results for coplanar faces.
      * ``FLOAT``
        Float -- Simple solver with good performance, without support for overlapping geometry.
      * ``MANIFOLD``
        Manifold -- Fastest solver that works only on manifold meshes but gives better results.
   :type trim_solver: enum in [``'EXACT'``, ``'FLOAT'``, ``'MANIFOLD'``], (optional)

.. function:: trim_line_gesture(*, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5, use_front_faces_only=False, use_limit_to_segment=False, location=(0, 0), trim_mode='DIFFERENCE', use_cursor_depth=False, trim_orientation='VIEW', trim_extrude_mode='FIXED', trim_solver='MANIFOLD')

   Remove a portion of the mesh on one side of a line

   :arg xstart: X Start
   :type xstart: int in [-inf, inf], (optional)
   :arg xend: X End
   :type xend: int in [-inf, inf], (optional)
   :arg ystart: Y Start
   :type ystart: int in [-inf, inf], (optional)
   :arg yend: Y End
   :type yend: int in [-inf, inf], (optional)
   :arg flip: Flip
   :type flip: boolean, (optional)
   :arg cursor: Cursor, Mouse cursor style to use during the modal operator
   :type cursor: int in [0, inf], (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)
   :arg use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
   :type use_limit_to_segment: boolean, (optional)
   :arg location: Location, Mouse location
   :type location: int array of 2 items in [-inf, inf], (optional)
   :arg trim_mode: Trim Mode

      * ``DIFFERENCE``
        Difference -- Use a difference boolean operation.
      * ``UNION``
        Union -- Use a union boolean operation.
      * ``JOIN``
        Join -- Join the new mesh as separate geometry, without performing any boolean operation.
   :type trim_mode: enum in [``'DIFFERENCE'``, ``'UNION'``, ``'JOIN'``], (optional)
   :arg use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
   :type use_cursor_depth: boolean, (optional)
   :arg trim_orientation: Shape Orientation

      * ``VIEW``
        View -- Use the view to orientate the trimming shape.
      * ``SURFACE``
        Surface -- Use the surface normal to orientate the trimming shape.
   :type trim_orientation: enum in [``'VIEW'``, ``'SURFACE'``], (optional)
   :arg trim_extrude_mode: Extrude Mode

      * ``PROJECT``
        Project -- Align trim geometry with the perspective of the current view for a tapered shape.
      * ``FIXED``
        Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
   :type trim_extrude_mode: enum in [``'PROJECT'``, ``'FIXED'``], (optional)
   :arg trim_solver: Solver

      * ``EXACT``
        Exact -- Slower solver with the best results for coplanar faces.
      * ``FLOAT``
        Float -- Simple solver with good performance, without support for overlapping geometry.
      * ``MANIFOLD``
        Manifold -- Fastest solver that works only on manifold meshes but gives better results.
   :type trim_solver: enum in [``'EXACT'``, ``'FLOAT'``, ``'MANIFOLD'``], (optional)

.. function:: trim_polyline_gesture(*, path=None, use_front_faces_only=False, location=(0, 0), trim_mode='DIFFERENCE', use_cursor_depth=False, trim_orientation='VIEW', trim_extrude_mode='FIXED', trim_solver='MANIFOLD')

   Execute a boolean operation on the mesh and a polygonal shape defined by the cursor

   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)
   :arg location: Location, Mouse location
   :type location: int array of 2 items in [-inf, inf], (optional)
   :arg trim_mode: Trim Mode

      * ``DIFFERENCE``
        Difference -- Use a difference boolean operation.
      * ``UNION``
        Union -- Use a union boolean operation.
      * ``JOIN``
        Join -- Join the new mesh as separate geometry, without performing any boolean operation.
   :type trim_mode: enum in [``'DIFFERENCE'``, ``'UNION'``, ``'JOIN'``], (optional)
   :arg use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
   :type use_cursor_depth: boolean, (optional)
   :arg trim_orientation: Shape Orientation

      * ``VIEW``
        View -- Use the view to orientate the trimming shape.
      * ``SURFACE``
        Surface -- Use the surface normal to orientate the trimming shape.
   :type trim_orientation: enum in [``'VIEW'``, ``'SURFACE'``], (optional)
   :arg trim_extrude_mode: Extrude Mode

      * ``PROJECT``
        Project -- Align trim geometry with the perspective of the current view for a tapered shape.
      * ``FIXED``
        Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
   :type trim_extrude_mode: enum in [``'PROJECT'``, ``'FIXED'``], (optional)
   :arg trim_solver: Solver

      * ``EXACT``
        Exact -- Slower solver with the best results for coplanar faces.
      * ``FLOAT``
        Float -- Simple solver with good performance, without support for overlapping geometry.
      * ``MANIFOLD``
        Manifold -- Fastest solver that works only on manifold meshes but gives better results.
   :type trim_solver: enum in [``'EXACT'``, ``'FLOAT'``, ``'MANIFOLD'``], (optional)

.. function:: uv_sculpt_grab(*, use_invert=False)

   Grab UVs

   :arg use_invert: Invert, Invert action for the duration of the stroke
   :type use_invert: boolean, (optional)

.. function:: uv_sculpt_pinch(*, use_invert=False)

   Pinch UVs

   :arg use_invert: Invert, Invert action for the duration of the stroke
   :type use_invert: boolean, (optional)

.. function:: uv_sculpt_relax(*, use_invert=False, relax_method='COTAN')

   Relax UVs

   :arg use_invert: Invert, Invert action for the duration of the stroke
   :type use_invert: boolean, (optional)
   :arg relax_method: Relax Method, Algorithm used for UV relaxation

      * ``LAPLACIAN``
        Laplacian -- Use Laplacian method for relaxation.
      * ``HC``
        HC -- Use HC method for relaxation.
      * ``COTAN``
        Geometry -- Use Geometry (cotangent) relaxation, making UVs follow the underlying 3D geometry.
   :type relax_method: enum in [``'LAPLACIAN'``, ``'HC'``, ``'COTAN'``], (optional)

