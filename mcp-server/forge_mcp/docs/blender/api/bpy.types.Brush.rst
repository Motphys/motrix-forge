Brush(ID)
=========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Brush(ID)

   Brush data-block for storing brush settings for painting and sculpting

   .. attribute:: area_radius_factor

      Ratio between the brush radius and the radius that is going to be used to sample the area center

      :type: float in [0, 2], default 0.5

   .. attribute:: auto_smooth_factor

      Amount of smoothing to automatically apply to each stroke

      :type: float in [0, 1], default 0.0

   .. attribute:: automasking_boundary_edges_propagation_steps

      Distance where boundary edge automasking is going to protect vertices from the fully masked edge

      :type: int in [1, 20], default 1

   .. attribute:: automasking_cavity_blur_steps

      The number of times the cavity mask is blurred

      :type: int in [0, 25], default 0

   .. data:: automasking_cavity_curve

      Curve used for the sensitivity

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: automasking_cavity_factor

      The contrast of the cavity mask

      :type: float in [0, 5], default 1.0

   .. attribute:: automasking_start_normal_falloff

      Extend the angular range with a falloff gradient

      :type: float in [0.0001, 1], default 0.25

   .. attribute:: automasking_start_normal_limit

      The range of angles that will be affected

      :type: float in [0.0001, 3.14159], default 0.349066

   .. attribute:: automasking_view_normal_falloff

      Extend the angular range with a falloff gradient

      :type: float in [0.0001, 1], default 0.25

   .. attribute:: automasking_view_normal_limit

      The range of angles that will be affected

      :type: float in [0.0001, 3.14159], default 1.5708

   .. attribute:: blend

      Brush blending mode

      * ``MIX``
        Mix -- Use Mix blending mode while painting.
      * ``DARKEN``
        Darken -- Use Darken blending mode while painting.
      * ``MUL``
        Multiply -- Use Multiply blending mode while painting.
      * ``COLORBURN``
        Color Burn -- Use Color Burn blending mode while painting.
      * ``LINEARBURN``
        Linear Burn -- Use Linear Burn blending mode while painting.
      * ``LIGHTEN``
        Lighten -- Use Lighten blending mode while painting.
      * ``SCREEN``
        Screen -- Use Screen blending mode while painting.
      * ``COLORDODGE``
        Color Dodge -- Use Color Dodge blending mode while painting.
      * ``ADD``
        Add -- Use Add blending mode while painting.
      * ``OVERLAY``
        Overlay -- Use Overlay blending mode while painting.
      * ``SOFTLIGHT``
        Soft Light -- Use Soft Light blending mode while painting.
      * ``HARDLIGHT``
        Hard Light -- Use Hard Light blending mode while painting.
      * ``VIVIDLIGHT``
        Vivid Light -- Use Vivid Light blending mode while painting.
      * ``LINEARLIGHT``
        Linear Light -- Use Linear Light blending mode while painting.
      * ``PINLIGHT``
        Pin Light -- Use Pin Light blending mode while painting.
      * ``DIFFERENCE``
        Difference -- Use Difference blending mode while painting.
      * ``EXCLUSION``
        Exclusion -- Use Exclusion blending mode while painting.
      * ``SUB``
        Subtract -- Use Subtract blending mode while painting.
      * ``HUE``
        Hue -- Use Hue blending mode while painting.
      * ``SATURATION``
        Saturation -- Use Saturation blending mode while painting.
      * ``COLOR``
        Color -- Use Color blending mode while painting.
      * ``LUMINOSITY``
        Value -- Use Value blending mode while painting.
      * ``ERASE_ALPHA``
        Erase Alpha -- Erase alpha while painting.
      * ``ADD_ALPHA``
        Add Alpha -- Add alpha while painting.

      :type: enum in [``'MIX'``, ``'DARKEN'``, ``'MUL'``, ``'COLORBURN'``, ``'LINEARBURN'``, ``'LIGHTEN'``, ``'SCREEN'``, ``'COLORDODGE'``, ``'ADD'``, ``'OVERLAY'``, ``'SOFTLIGHT'``, ``'HARDLIGHT'``, ``'VIVIDLIGHT'``, ``'LINEARLIGHT'``, ``'PINLIGHT'``, ``'DIFFERENCE'``, ``'EXCLUSION'``, ``'SUB'``, ``'HUE'``, ``'SATURATION'``, ``'COLOR'``, ``'LUMINOSITY'``, ``'ERASE_ALPHA'``, ``'ADD_ALPHA'``], default ``'MIX'``

   .. attribute:: blur_kernel_radius

      Radius of kernel used for soften and sharpen in pixels

      :type: int in [1, 10000], default 2

   .. attribute:: blur_mode

      :type: enum in [``'BOX'``, ``'GAUSSIAN'``], default ``'GAUSSIAN'``

   .. attribute:: boundary_deform_type

      Deformation type that is used in the brush

      :type: enum in [``'BEND'``, ``'EXPAND'``, ``'INFLATE'``, ``'GRAB'``, ``'TWIST'``, ``'SMOOTH'``], default ``'BEND'``

   .. attribute:: boundary_falloff_type

      How the brush falloff is applied across the boundary

      * ``CONSTANT``
        Constant -- Applies the same deformation in the entire boundary.
      * ``RADIUS``
        Brush Radius -- Applies the deformation in a localized area limited by the brush radius.
      * ``LOOP``
        Loop -- Applies the brush falloff in a loop pattern.
      * ``LOOP_INVERT``
        Loop and Invert -- Applies the falloff radius in a loop pattern, inverting the displacement direction in each pattern repetition.

      :type: enum in [``'CONSTANT'``, ``'RADIUS'``, ``'LOOP'``, ``'LOOP_INVERT'``], default ``'CONSTANT'``

   .. attribute:: boundary_offset

      Offset of the boundary origin in relation to the brush radius

      :type: float in [0, 30], default 0.0

   .. data:: brush_capabilities

      Brush's capabilities

      :type: :class:`BrushCapabilities`, (readonly, never None)

   .. attribute:: cloth_constraint_softbody_strength

      How much the cloth preserves the original shape, acting as a soft body

      :type: float in [0, 1], default 0.0

   .. attribute:: cloth_damping

      How much the applied forces are propagated through the cloth

      :type: float in [0.01, 1], default 0.01

   .. attribute:: cloth_deform_type

      Deformation type that is used in the brush

      :type: enum in [``'DRAG'``, ``'PUSH'``, ``'PINCH_POINT'``, ``'PINCH_PERPENDICULAR'``, ``'INFLATE'``, ``'GRAB'``, ``'EXPAND'``, ``'SNAKE_HOOK'``], default ``'DRAG'``

   .. attribute:: cloth_force_falloff_type

      Shape used in the brush to apply force to the cloth

      :type: enum in [``'RADIAL'``, ``'PLANE'``], default ``'RADIAL'``

   .. attribute:: cloth_mass

      Mass of each simulation particle

      :type: float in [0.01, 2], default 1.0

   .. attribute:: cloth_sim_falloff

      Area to apply deformation falloff to the effects of the simulation

      :type: float in [0, 1], default 0.75

   .. attribute:: cloth_sim_limit

      Factor added relative to the size of the radius to limit the cloth simulation effects

      :type: float in [0.1, 10], default 2.5

   .. attribute:: cloth_simulation_area_type

      Part of the mesh that is going to be simulated when the stroke is active

      * ``LOCAL``
        Local -- Simulates only a specific area around the brush limited by a fixed radius.
      * ``GLOBAL``
        Global -- Simulates the entire mesh.
      * ``DYNAMIC``
        Dynamic -- The active simulation area moves with the brush.

      :type: enum in [``'LOCAL'``, ``'GLOBAL'``, ``'DYNAMIC'``], default ``'LOCAL'``

   .. attribute:: color

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. attribute:: color_type

      Use single color or gradient when painting

      * ``COLOR``
        Color -- Paint with a single color.
      * ``GRADIENT``
        Gradient -- Paint with a gradient.

      :type: enum in [``'COLOR'``, ``'GRADIENT'``], default ``'COLOR'``

   .. attribute:: crease_pinch_factor

      How much the crease brush pinches

      :type: float in [0, 1], default 0.5

   .. attribute:: cursor_color_add

      Color of cursor when adding

      :type: float array of 4 items in [0, inf], default (1.0, 0.39, 0.39, 0.9)

   .. attribute:: cursor_color_subtract

      Color of cursor when subtracting

      :type: float array of 4 items in [0, inf], default (0.39, 0.39, 1.0, 0.9)

   .. attribute:: cursor_overlay_alpha

      :type: int in [0, 100], default 33

   .. data:: curve

      Editable falloff curve

      :type: :class:`CurveMapping`, (readonly, never None)

   .. attribute:: curve_preset

      :type: enum in :ref:`rna_enum_brush_curve_preset_items`, default ``'CUSTOM'``

   .. data:: curve_random_hue

      Curve used for modulating effect

      :type: :class:`CurveMapping`, (readonly)

   .. data:: curve_random_saturation

      Curve used for modulating effect

      :type: :class:`CurveMapping`, (readonly)

   .. data:: curve_random_value

      Curve used for modulating effect

      :type: :class:`CurveMapping`, (readonly)

   .. data:: curves_sculpt_settings

      :type: :class:`BrushCurvesSculptSettings`, (readonly)

   .. attribute:: curves_sculpt_tool

      :type: enum in :ref:`rna_enum_brush_curves_sculpt_brush_type_items`, default ``'COMB'``

   .. attribute:: dash_ratio

      Ratio of samples in a cycle that the brush is enabled

      :type: float in [0, 1], default 1.0

   .. attribute:: dash_samples

      Length of a dash cycle measured in stroke samples

      :type: int in [1, 10000], default 20

   .. attribute:: deform_target

      How the deformation of the brush will affect the object

      * ``GEOMETRY``
        Geometry -- Brush deformation displaces the vertices of the mesh.
      * ``CLOTH_SIM``
        Cloth Simulation -- Brush deforms the mesh by deforming the constraints of a cloth simulation.

      :type: enum in [``'GEOMETRY'``, ``'CLOTH_SIM'``], default ``'GEOMETRY'``

   .. attribute:: density

      Amount of random elements that are going to be affected by the brush

      :type: float in [0, 1], default 0.0

   .. attribute:: direction

      * ``ADD``
        Add -- Add effect of brush.
      * ``SUBTRACT``
        Subtract -- Subtract effect of brush.

      :type: enum in [``'ADD'``, ``'SUBTRACT'``], default ``'ADD'``

   .. attribute:: disconnected_distance_max

      Maximum distance to search for disconnected loose parts in the mesh

      :type: float in [0, 10], default 0.1

   .. attribute:: elastic_deform_type

      Deformation type that is used in the brush

      :type: enum in [``'GRAB'``, ``'GRAB_BISCALE'``, ``'GRAB_TRISCALE'``, ``'SCALE'``, ``'TWIST'``], default ``'GRAB'``

   .. attribute:: elastic_deform_volume_preservation

      Poisson ratio for elastic deformation. Higher values preserve volume more, but also lead to more bulging.

      :type: float in [0, 0.9], default 0.0

   .. attribute:: falloff_angle

      Paint most on faces pointing towards the view according to this angle

      :type: float in [0, 1.5708], default 0.0

   .. attribute:: falloff_shape

      Use projected or spherical falloff

      * ``SPHERE``
        Sphere -- Apply brush influence in a Sphere, outwards from the center.
      * ``PROJECTED``
        Projected -- Apply brush influence in a 2D circle, projected from the view.

      :type: enum in [``'SPHERE'``, ``'PROJECTED'``], default ``'SPHERE'``

   .. attribute:: fill_threshold

      Threshold above which filling is not propagated

      :type: float in [0, 100], default 0.2

   .. attribute:: flow

      Amount of paint that is applied per stroke sample

      :type: float in [0, 1], default 0.0

   .. attribute:: gpencil_sculpt_tool

      :type: enum in :ref:`rna_enum_brush_gpencil_sculpt_types_items`, default ``'SMOOTH'``

   .. data:: gpencil_settings

      :type: :class:`BrushGpencilSettings`, (readonly)

   .. attribute:: gpencil_tool

      :type: enum in :ref:`rna_enum_brush_gpencil_types_items`, default ``'DRAW'``

   .. attribute:: gpencil_vertex_tool

      :type: enum in :ref:`rna_enum_brush_gpencil_vertex_types_items`, default ``'DRAW'``

   .. attribute:: gpencil_weight_tool

      :type: enum in :ref:`rna_enum_brush_gpencil_weight_types_items`, default ``'WEIGHT'``

   .. attribute:: grad_spacing

      Spacing before brush gradient goes full circle

      :type: int in [1, 10000], default 0

   .. data:: gradient

      :type: :class:`ColorRamp`, (readonly)

   .. attribute:: gradient_fill_mode

      :type: enum in [``'LINEAR'``, ``'RADIAL'``], default ``'LINEAR'``

   .. attribute:: gradient_stroke_mode

      :type: enum in [``'PRESSURE'``, ``'SPACING_REPEAT'``, ``'SPACING_CLAMP'``], default ``'PRESSURE'``

   .. attribute:: hardness

      How close the brush falloff starts from the edge of the brush

      :type: float in [0, 1], default 0.0

   .. data:: has_unsaved_changes

      Indicates that there are any user visible changes since the brush has been imported or read from the file

      :type: boolean, default False, (readonly)

   .. attribute:: height

      Affectable height of brush (i.e. the layer height for the layer tool)

      :type: float in [0, 1], default 0.5

   .. attribute:: hue_jitter

      Color jitter effect on hue

      :type: float in [0, 1], default 0.0

   .. attribute:: icon_filepath

      File path to brush icon

      :type: string, default "", (never None, blend relative ``//`` prefix supported)

   .. data:: image_paint_capabilities

      :type: :class:`BrushCapabilitiesImagePaint`, (readonly, never None)

   .. attribute:: image_tool

      :type: enum in :ref:`rna_enum_brush_image_brush_type_items`, default ``'DRAW'``

   .. attribute:: input_samples

      Number of input samples to average together to smooth the brush stroke

      :type: int in [1, 64], default 1

   .. attribute:: invert_density_pressure

      Invert the modulation of pressure in density

      :type: boolean, default False

   .. attribute:: invert_flow_pressure

      Invert the modulation of pressure in flow

      :type: boolean, default False

   .. attribute:: invert_hardness_pressure

      Invert the modulation of pressure in hardness

      :type: boolean, default False

   .. attribute:: invert_to_scrape_fill

      Use Scrape or Fill brush when inverting this brush instead of inverting its displacement direction

      :type: boolean, default False

   .. attribute:: invert_wet_mix_pressure

      Invert the modulation of pressure in wet mix

      :type: boolean, default False

   .. attribute:: invert_wet_persistence_pressure

      Invert the modulation of pressure in wet persistence

      :type: boolean, default False

   .. attribute:: jitter

      Jitter the position of the brush while painting

      :type: float in [0, 1000], default 0.0

   .. attribute:: jitter_absolute

      Jitter the position of the brush in pixels while painting

      :type: int in [0, 1000000], default 0

   .. attribute:: jitter_unit

      Jitter in screen space or relative to brush size

      * ``VIEW``
        View -- Jittering happens in screen space, in pixels.
      * ``BRUSH``
        Brush -- Jittering happens relative to the brush size.

      :type: enum in [``'VIEW'``, ``'BRUSH'``], default ``'BRUSH'``

   .. attribute:: mask_overlay_alpha

      :type: int in [0, 100], default 33

   .. attribute:: mask_stencil_dimension

      Dimensions of mask stencil in viewport

      :type: :class:`mathutils.Vector` of 2 items in [-inf, inf], default (256.0, 256.0)

   .. attribute:: mask_stencil_pos

      Position of mask stencil in viewport

      :type: :class:`mathutils.Vector` of 2 items in [-inf, inf], default (256.0, 256.0)

   .. attribute:: mask_texture

      :type: :class:`Texture`

   .. data:: mask_texture_slot

      :type: :class:`BrushTextureSlot`, (readonly)

   .. attribute:: mask_tool

      :type: enum in [``'DRAW'``, ``'SMOOTH'``], default ``'DRAW'``

   .. attribute:: multiplane_scrape_angle

      Angle between the planes of the crease

      :type: float in [0, 160], default 0.0

   .. attribute:: normal_radius_factor

      Ratio between the brush radius and the radius that is going to be used to sample the normal

      :type: float in [0, 2], default 0.5

   .. attribute:: normal_weight

      How much grab will pull vertices out of surface during a grab

      :type: float in [0, 1], default 0.0

   .. attribute:: paint_curve

      Active paint curve

      :type: :class:`PaintCurve`

   .. attribute:: plane_depth

      The maximum distance below the plane for affected vertices. Increasing the depth affects vertices farther below the plane.

      :type: float in [0, 1], default 0.0

   .. attribute:: plane_height

      The maximum distance above the plane for affected vertices. Increasing the height affects vertices farther above the plane.

      :type: float in [0, 1], default 1.0

   .. attribute:: plane_inversion_mode

      Inversion Mode

      * ``INVERT_DISPLACEMENT``
        Invert Displacement -- Displace the vertices away from the plane..
      * ``SWAP_DEPTH_AND_HEIGHT``
        Swap Height and Depth -- Swap the roles of Height and Depth..

      :type: enum in [``'INVERT_DISPLACEMENT'``, ``'SWAP_DEPTH_AND_HEIGHT'``], default ``'INVERT_DISPLACEMENT'``

   .. attribute:: plane_offset

      Adjust plane on which the brush acts towards or away from the object surface

      :type: float in [-2, 2], default 0.0

   .. attribute:: plane_trim

      If a vertex is further away from offset plane than this, then it is not affected

      :type: float in [0, 1], default 0.5

   .. attribute:: pose_deform_type

      Deformation type that is used in the brush

      :type: enum in [``'ROTATE_TWIST'``, ``'SCALE_TRANSLATE'``, ``'SQUASH_STRETCH'``], default ``'ROTATE_TWIST'``

   .. attribute:: pose_ik_segments

      Number of segments of the inverse kinematics chain that will deform the mesh

      :type: int in [1, 20], default 1

   .. attribute:: pose_offset

      Offset of the pose origin in relation to the brush radius

      :type: float in [0, 2], default 0.0

   .. attribute:: pose_origin_type

      Method to set the rotation origins for the segments of the brush

      * ``TOPOLOGY``
        Topology -- Sets the rotation origin automatically using the topology and shape of the mesh as a guide.
      * ``FACE_SETS``
        Face Sets -- Creates a pose segment per face sets, starting from the active face set.
      * ``FACE_SETS_FK``
        Face Sets FK -- Simulates an FK deformation using the Face Set under the cursor as control.

      :type: enum in [``'TOPOLOGY'``, ``'FACE_SETS'``, ``'FACE_SETS_FK'``], default ``'TOPOLOGY'``

   .. attribute:: pose_smooth_iterations

      Smooth iterations applied after calculating the pose factor of each vertex

      :type: int in [0, 100], default 4

   .. attribute:: rake_factor

      How much grab will follow cursor rotation

      :type: float in [0, 10], default 0.0

   .. attribute:: rate

      Interval between paints for Airbrush

      :type: float in [0.0001, 10000], default 0.1

   .. attribute:: saturation_jitter

      Color jitter effect on saturation

      :type: float in [0, 1], default 0.0

   .. data:: sculpt_capabilities

      :type: :class:`BrushCapabilitiesSculpt`, (readonly, never None)

   .. attribute:: sculpt_plane

      :type: enum in [``'AREA'``, ``'VIEW'``, ``'X'``, ``'Y'``, ``'Z'``], default ``'AREA'``

   .. attribute:: sculpt_tool

      :type: enum in :ref:`rna_enum_brush_sculpt_brush_type_items`, default ``'DRAW'``

   .. attribute:: secondary_color

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: sharp_threshold

      Threshold below which, no sharpening is done

      :type: float in [0, 100], default 0.0

   .. attribute:: show_multiplane_scrape_planes_preview

      Preview the scrape planes in the cursor during the stroke

      :type: boolean, default False

   .. attribute:: size

      Radius of the brush in pixels

      :type: int in [1, 5000], default 35

   .. attribute:: slide_deform_type

      Deformation type that is used in the brush

      :type: enum in [``'DRAG'``, ``'PINCH'``, ``'EXPAND'``], default ``'DRAG'``

   .. attribute:: smear_deform_type

      Deformation type that is used in the brush

      :type: enum in [``'DRAG'``, ``'PINCH'``, ``'EXPAND'``], default ``'DRAG'``

   .. attribute:: smooth_deform_type

      Deformation type that is used in the brush

      * ``LAPLACIAN``
        Laplacian -- Smooths the surface and the volume.
      * ``SURFACE``
        Surface -- Smooths the surface of the mesh, preserving the volume.

      :type: enum in [``'LAPLACIAN'``, ``'SURFACE'``], default ``'LAPLACIAN'``

   .. attribute:: smooth_stroke_factor

      Higher values give a smoother stroke

      :type: float in [0.5, 0.99], default 0.9

   .. attribute:: smooth_stroke_radius

      Minimum distance from last point before stroke continues

      :type: int in [10, 200], default 75

   .. attribute:: snake_hook_deform_type

      Deformation type that is used in the brush

      * ``FALLOFF``
        Radius Falloff -- Applies the brush falloff in the tip of the brush.
      * ``ELASTIC``
        Elastic -- Modifies the entire mesh using elastic deform.

      :type: enum in [``'FALLOFF'``, ``'ELASTIC'``], default ``'FALLOFF'``

   .. attribute:: spacing

      Spacing between brush daubs as a percentage of brush diameter

      :type: int in [1, 1000], default 10

   .. attribute:: stabilize_normal

      Stabilize the orientation of the brush plane.

      :type: float in [0, 1], default 0.0

   .. attribute:: stabilize_plane

      Stabilize the center of the brush plane.

      :type: float in [0, 1], default 0.0

   .. attribute:: stencil_dimension

      Dimensions of stencil in viewport

      :type: :class:`mathutils.Vector` of 2 items in [-inf, inf], default (256.0, 256.0)

   .. attribute:: stencil_pos

      Position of stencil in viewport

      :type: :class:`mathutils.Vector` of 2 items in [-inf, inf], default (256.0, 256.0)

   .. attribute:: strength

      How powerful the effect of the brush is when applied

      :type: float in [0, 10], default 1.0

   .. attribute:: stroke_method

      * ``DOTS``
        Dots -- Apply paint on each mouse move step.
      * ``DRAG_DOT``
        Drag Dot -- Allows a single dot to be carefully positioned.
      * ``SPACE``
        Space -- Limit brush application to the distance specified by spacing.
      * ``AIRBRUSH``
        Airbrush -- Keep applying paint effect while holding mouse (spray).
      * ``ANCHORED``
        Anchored -- Keep the brush anchored to the initial location.
      * ``LINE``
        Line -- Draw a line with dabs separated according to spacing.
      * ``CURVE``
        Curve -- Define the stroke curve with a Bézier curve (dabs are separated according to spacing).

      :type: enum in [``'DOTS'``, ``'DRAG_DOT'``, ``'SPACE'``, ``'AIRBRUSH'``, ``'ANCHORED'``, ``'LINE'``, ``'CURVE'``], default ``'DOTS'``

   .. attribute:: surface_smooth_current_vertex

      How much the position of each individual vertex influences the final result

      :type: float in [0, 1], default 0.0

   .. attribute:: surface_smooth_iterations

      Number of smoothing iterations per brush step

      :type: int in [1, 10], default 0

   .. attribute:: surface_smooth_shape_preservation

      How much of the original shape is preserved when smoothing

      :type: float in [0, 1], default 0.0

   .. attribute:: texture

      :type: :class:`Texture`

   .. attribute:: texture_overlay_alpha

      :type: int in [0, 100], default 33

   .. attribute:: texture_sample_bias

      Value added to texture samples

      :type: float in [-1, 1], default 0.0

   .. data:: texture_slot

      :type: :class:`BrushTextureSlot`, (readonly)

   .. attribute:: tilt_strength_factor

      How much the tilt of the pen will affect the brush. Negative values indicate inverting the tilt directions.

      :type: float in [-1, 1], default 0.0

   .. attribute:: tip_roundness

      Roundness of the brush tip

      :type: float in [0, 1], default 1.0

   .. attribute:: tip_scale_x

      Scale of the brush tip in the X axis

      :type: float in [0.0001, 1], default 1.0

   .. attribute:: topology_rake_factor

      Automatically align edges to the brush direction to generate cleaner topology and define sharp features. Best used on low-poly meshes as it has a performance impact.

      :type: float in [0, 1], default 0.0

   .. attribute:: unprojected_radius

      Radius of brush in Blender units

      :type: float in [0.001, inf], default 0.05

   .. attribute:: use_accumulate

      Accumulate stroke daubs on top of each other

      :type: boolean, default False

   .. attribute:: use_adaptive_space

      Space daubs according to surface orientation instead of screen space

      :type: boolean, default False

   .. attribute:: use_airbrush

      Keep applying paint effect while holding mouse (spray)

      :type: boolean, default False

   .. attribute:: use_alpha

      When this is disabled, lock alpha while painting

      :type: boolean, default True

   .. attribute:: use_anchor

      Keep the brush anchored to the initial location

      :type: boolean, default False

   .. attribute:: use_automasking_boundary_edges

      Do not affect non manifold boundary edges

      :type: boolean, default False

   .. attribute:: use_automasking_boundary_face_sets

      Do not affect vertices that belong to a Face Set boundary

      :type: boolean, default False

   .. attribute:: use_automasking_cavity

      Do not affect vertices on peaks, based on the surface curvature

      :type: boolean, default False

   .. attribute:: use_automasking_cavity_inverted

      Do not affect vertices within crevices, based on the surface curvature

      :type: boolean, default False

   .. attribute:: use_automasking_custom_cavity_curve

      Use custom curve

      :type: boolean, default False

   .. attribute:: use_automasking_face_sets

      Affect only vertices that share Face Sets with the active vertex

      :type: boolean, default False

   .. attribute:: use_automasking_start_normal

      Affect only vertices with a similar normal to where the stroke starts

      :type: boolean, default False

   .. attribute:: use_automasking_topology

      Affect only vertices connected to the active vertex under the brush

      :type: boolean, default False

   .. attribute:: use_automasking_view_normal

      Affect only vertices with a normal that faces the viewer

      :type: boolean, default False

   .. attribute:: use_automasking_view_occlusion

      Only affect vertices that are not occluded by other faces (slower performance)

      :type: boolean, default False

   .. attribute:: use_cloth_collision

      Collide with objects during the simulation

      :type: boolean, default False

   .. attribute:: use_cloth_pin_simulation_boundary

      Lock the position of the vertices in the simulation falloff area to avoid artifacts and create a softer transition with unaffected areas

      :type: boolean, default False

   .. attribute:: use_color_as_displacement

      Handle each pixel color as individual vector for displacement (area plane mapping only)

      :type: boolean, default False

   .. attribute:: use_color_jitter

      Jitter brush color

      :type: boolean, default False

   .. attribute:: use_connected_only

      Affect only topologically connected elements

      :type: boolean, default False

   .. attribute:: use_cursor_overlay

      Show cursor in viewport

      :type: boolean, default False

   .. attribute:: use_cursor_overlay_override

      Don't show overlay during a stroke

      :type: boolean, default False

   .. attribute:: use_curve

      Define the stroke curve with a Bézier curve. Dabs are separated according to spacing.

      :type: boolean, default False

   .. attribute:: use_custom_icon

      Set the brush icon from an image file

      :type: boolean, default False

   .. attribute:: use_density_pressure

      Use pressure to modulate density

      :type: boolean, default False

   .. attribute:: use_edge_to_edge

      Drag anchor brush from edge-to-edge

      :type: boolean, default False

   .. attribute:: use_flow_pressure

      Use pressure to modulate flow

      :type: boolean, default False

   .. attribute:: use_frontface

      Brush only affects vertices that face the viewer

      :type: boolean, default False

   .. attribute:: use_frontface_falloff

      Blend brush influence by how much they face the front

      :type: boolean, default False

   .. attribute:: use_grab_active_vertex

      Apply the maximum grab strength to the active vertex instead of the cursor location

      :type: boolean, default False

   .. attribute:: use_grab_silhouette

      Grabs trying to automask the silhouette of the object

      :type: boolean, default False

   .. attribute:: use_hardness_pressure

      Use pressure to modulate hardness

      :type: boolean, default False

   .. attribute:: use_inverse_smooth_pressure

      Lighter pressure causes more smoothing to be applied

      :type: boolean, default False

   .. attribute:: use_line

      Draw a line with dabs separated according to spacing

      :type: boolean, default False

   .. attribute:: use_locked_size

      Measure brush size relative to the view or the scene

      * ``VIEW``
        View -- Measure brush size relative to the view.
      * ``SCENE``
        Scene -- Measure brush size relative to the scene.

      :type: enum in [``'VIEW'``, ``'SCENE'``], default ``'VIEW'``

   .. attribute:: use_multiplane_scrape_dynamic

      The angle between the planes changes during the stroke to fit the surface under the cursor

      :type: boolean, default False

   .. attribute:: use_offset_pressure

      Enable tablet pressure sensitivity for offset

      :type: boolean, default False

   .. attribute:: use_original_normal

      When locked keep using normal of surface where stroke was initiated

      :type: boolean, default False

   .. attribute:: use_original_plane

      When locked keep using the plane origin of surface where stroke was initiated

      :type: boolean, default False

   .. attribute:: use_paint_antialiasing

      Smooths the edges of the strokes

      :type: boolean, default True

   .. attribute:: use_paint_grease_pencil

      Use this brush in Grease Pencil drawing mode

      :type: boolean, default False

   .. attribute:: use_paint_image

      Use this brush in texture paint mode

      :type: boolean, default True

   .. attribute:: use_paint_sculpt

      Use this brush in sculpt mode

      :type: boolean, default True

   .. attribute:: use_paint_sculpt_curves

      Use this brush in sculpt curves mode

      :type: boolean, default False

   .. attribute:: use_paint_uv_sculpt

      Use this brush in UV sculpt mode

      :type: boolean, default False

   .. attribute:: use_paint_vertex

      Use this brush in vertex paint mode

      :type: boolean, default True

   .. attribute:: use_paint_weight

      Use this brush in weight paint mode

      :type: boolean, default True

   .. attribute:: use_persistent

      Sculpt on a persistent layer of the mesh

      :type: boolean, default False

   .. attribute:: use_plane_trim

      Limit the distance from the offset plane that a vertex can be affected

      :type: boolean, default False

   .. attribute:: use_pose_ik_anchored

      Keep the position of the last segment in the IK chain fixed

      :type: boolean, default False

   .. attribute:: use_pose_lock_rotation

      Do not rotate the segment when using the scale deform mode

      :type: boolean, default False

   .. attribute:: use_pressure_area_radius

      Enable tablet pressure sensitivity for area radius

      :type: boolean, default False

   .. attribute:: use_pressure_jitter

      Enable tablet pressure sensitivity for jitter

      :type: boolean, default False

   .. attribute:: use_pressure_masking

      Pen pressure makes texture influence smaller

      :type: enum in [``'NONE'``, ``'RAMP'``, ``'CUTOFF'``], default ``'NONE'``

   .. attribute:: use_pressure_size

      Enable tablet pressure sensitivity for size

      :type: boolean, default False

   .. attribute:: use_pressure_spacing

      Enable tablet pressure sensitivity for spacing

      :type: boolean, default False

   .. attribute:: use_pressure_strength

      Enable tablet pressure sensitivity for strength

      :type: boolean, default True

   .. attribute:: use_primary_overlay

      Show texture in viewport

      :type: boolean, default False

   .. attribute:: use_primary_overlay_override

      Don't show overlay during a stroke

      :type: boolean, default False

   .. attribute:: use_random_press_hue

      Use pressure to modulate randomness

      :type: boolean, default False

   .. attribute:: use_random_press_sat

      Use pressure to modulate randomness

      :type: boolean, default False

   .. attribute:: use_random_press_val

      Use pressure to modulate randomness

      :type: boolean, default False

   .. attribute:: use_restore_mesh

      Allow a single dot to be carefully positioned

      :type: boolean, default False

   .. attribute:: use_scene_spacing

      Calculate the brush spacing using view or scene distance

      * ``VIEW``
        View -- Calculate brush spacing relative to the view.
      * ``SCENE``
        Scene -- Calculate brush spacing relative to the scene using the stroke location.

      :type: enum in [``'VIEW'``, ``'SCENE'``], default ``'VIEW'``

   .. attribute:: use_secondary_overlay

      Show texture in viewport

      :type: boolean, default False

   .. attribute:: use_secondary_overlay_override

      Don't show overlay during a stroke

      :type: boolean, default False

   .. attribute:: use_smooth_stroke

      Brush lags behind mouse and follows a smoother path

      :type: boolean, default False

   .. attribute:: use_space

      Limit brush application to the distance specified by spacing

      :type: boolean, default True

   .. attribute:: use_space_attenuation

      Automatically adjust strength to give consistent results for different spacings

      :type: boolean, default True

   .. attribute:: use_stroke_random_hue

      Use randomness at stroke level

      :type: boolean, default False

   .. attribute:: use_stroke_random_sat

      Use randomness at stroke level

      :type: boolean, default False

   .. attribute:: use_stroke_random_val

      Use randomness at stroke level

      :type: boolean, default False

   .. attribute:: use_vertex_grease_pencil

      Use this brush in Grease Pencil vertex color mode

      :type: boolean, default False

   .. attribute:: use_wet_mix_pressure

      Use pressure to modulate wet mix

      :type: boolean, default False

   .. attribute:: use_wet_persistence_pressure

      Use pressure to modulate wet persistence

      :type: boolean, default False

   .. attribute:: value_jitter

      Color jitter effect on value

      :type: float in [0, 1], default 0.0

   .. data:: vertex_paint_capabilities

      :type: :class:`BrushCapabilitiesVertexPaint`, (readonly, never None)

   .. attribute:: vertex_tool

      :type: enum in :ref:`rna_enum_brush_vertex_brush_type_items`, default ``'DRAW'``

   .. attribute:: weight

      Vertex weight when brush is applied

      :type: float in [0, 1], default 1.0

   .. data:: weight_paint_capabilities

      :type: :class:`BrushCapabilitiesWeightPaint`, (readonly, never None)

   .. attribute:: weight_tool

      :type: enum in :ref:`rna_enum_brush_weight_brush_type_items`, default ``'DRAW'``

   .. attribute:: wet_mix

      Amount of paint that is picked from the surface into the brush color

      :type: float in [0, 1], default 0.0

   .. attribute:: wet_paint_radius_factor

      Ratio between the brush radius and the radius that is going to be used to sample the color to blend in wet paint

      :type: float in [0, 2], default 0.5

   .. attribute:: wet_persistence

      Amount of wet paint that stays in the brush after applying paint to the surface

      :type: float in [0, 1], default 0.0

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct` subclass


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`ID.name`
   * :class:`ID.name_full`
   * :class:`ID.id_type`
   * :class:`ID.session_uid`
   * :class:`ID.is_evaluated`
   * :class:`ID.original`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.use_extra_user`
   * :class:`ID.is_embedded_data`
   * :class:`ID.is_missing`
   * :class:`ID.is_runtime_data`
   * :class:`ID.is_editable`
   * :class:`ID.tag`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.library_weak_reference`
   * :class:`ID.asset_data`
   * :class:`ID.override_library`
   * :class:`ID.preview`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.id_properties_clear`
   * :class:`bpy_struct.id_properties_ensure`
   * :class:`bpy_struct.id_properties_ui`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_overridable_library`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.pop`
   * :class:`bpy_struct.property_overridable_library_set`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.rna_ancestors`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`
   * :class:`ID.rename`
   * :class:`ID.evaluated_get`
   * :class:`ID.copy`
   * :class:`ID.asset_mark`
   * :class:`ID.asset_clear`
   * :class:`ID.asset_generate_preview`
   * :class:`ID.override_create`
   * :class:`ID.override_hierarchy_create`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`
   * :class:`ID.preview_ensure`
   * :class:`ID.bl_rna_get_subclass`
   * :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   * :mod:`bpy.context.brush`
   * :class:`BlendData.brushes`
   * :class:`BlendDataBrushes.create_gpencil_data`
   * :class:`BlendDataBrushes.new`
   * :class:`BlendDataBrushes.remove`
   * :class:`Paint.brush`
   * :class:`Paint.eraser_brush`

