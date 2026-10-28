FluidDomainSettings(bpy_struct)
===============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FluidDomainSettings(bpy_struct)

   Fluid domain settings

   .. attribute:: adapt_margin

      Margin added around fluid to minimize boundary interference

      :type: int in [2, 24], default 4

   .. attribute:: adapt_threshold

      Minimum amount of fluid a cell can contain before it is considered empty

      :type: float in [0, 1], default 0.02

   .. attribute:: additional_res

      Maximum number of additional cells

      :type: int in [0, 512], default 0

   .. attribute:: alpha

      Buoyant force based on smoke density (higher value results in faster rising smoke)

      :type: float in [-5, 5], default 1.0

   .. attribute:: beta

      Buoyant force based on smoke heat (higher value results in faster rising smoke)

      :type: float in [-5, 5], default 1.0

   .. attribute:: burning_rate

      Speed of the burning reaction (higher value results in smaller flames)

      :type: float in [0.01, 4], default 0.75

   .. attribute:: cache_data_format

      Select the file format to be used for caching volumetric data

      * ``UNI``
        Uni Cache -- Uni file format (.uni).
      * ``OPENVDB``
        OpenVDB -- OpenVDB file format (.vdb).
      * ``RAW``
        Raw Cache -- Raw file format (.raw).

      :type: enum in [``'UNI'``, ``'OPENVDB'``, ``'RAW'``], default ``'OPENVDB'``

   .. attribute:: cache_directory

      Directory that contains fluid cache files

      :type: string, default "", (never None, blend relative ``//`` prefix supported)

   .. attribute:: cache_frame_end

      Frame on which the simulation stops (last frame baked)

      :type: int in [-1048574, 1048574], default 250

   .. attribute:: cache_frame_offset

      Frame offset that is used when loading the simulation from the cache. It is not considered when baking the simulation, only when loading it.

      :type: int in [-1048574, 1048574], default 0

   .. attribute:: cache_frame_pause_data

      :type: int in [-inf, inf], default 0

   .. attribute:: cache_frame_pause_guide

      :type: int in [-inf, inf], default 0

   .. attribute:: cache_frame_pause_mesh

      :type: int in [-inf, inf], default 0

   .. attribute:: cache_frame_pause_noise

      :type: int in [-inf, inf], default 0

   .. attribute:: cache_frame_pause_particles

      :type: int in [-inf, inf], default 0

   .. attribute:: cache_frame_start

      Frame on which the simulation starts (first frame baked)

      :type: int in [-1048574, 1048574], default 1

   .. attribute:: cache_mesh_format

      Select the file format to be used for caching surface data

      * ``UNI``
        Uni Cache -- Uni file format (.uni).
      * ``OPENVDB``
        OpenVDB -- OpenVDB file format (.vdb).
      * ``RAW``
        Raw Cache -- Raw file format (.raw).

      :type: enum in [``'UNI'``, ``'OPENVDB'``, ``'RAW'``], default ``'UNI'``

   .. attribute:: cache_noise_format

      Select the file format to be used for caching noise data

      * ``UNI``
        Uni Cache -- Uni file format (.uni).
      * ``OPENVDB``
        OpenVDB -- OpenVDB file format (.vdb).
      * ``RAW``
        Raw Cache -- Raw file format (.raw).

      :type: enum in [``'UNI'``, ``'OPENVDB'``, ``'RAW'``], default ``'OPENVDB'``

   .. attribute:: cache_particle_format

      Select the file format to be used for caching particle data

      * ``UNI``
        Uni Cache -- Uni file format (.uni).
      * ``OPENVDB``
        OpenVDB -- OpenVDB file format (.vdb).
      * ``RAW``
        Raw Cache -- Raw file format (.raw).

      :type: enum in [``'UNI'``, ``'OPENVDB'``, ``'RAW'``], default ``'OPENVDB'``

   .. attribute:: cache_resumable

      Additional data will be saved so that the bake jobs can be resumed after pausing. Because more data will be written to disk it is recommended to avoid enabling this option when baking at high resolutions.

      :type: boolean, default False

   .. attribute:: cache_type

      Change the cache type of the simulation

      * ``REPLAY``
        Replay -- Use the timeline to bake the scene.
      * ``MODULAR``
        Modular -- Bake every stage of the simulation separately.
      * ``ALL``
        All -- Bake all simulation settings at once.

      :type: enum in [``'REPLAY'``, ``'MODULAR'``, ``'ALL'``], default ``'REPLAY'``

   .. data:: cell_size

      Cell Size

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: cfl_condition

      Maximal velocity per cell (greater CFL numbers will minimize the number of simulation steps and the computation time.)

      :type: float in [0, 10], default 2.0

   .. attribute:: clipping

      Value under which voxels are considered empty space to optimize rendering

      :type: float in [0, 1], default 1e-06

   .. data:: color_grid

      Smoke color grid

      :type: float array of 32 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), (readonly)

   .. data:: color_ramp

      :type: :class:`ColorRamp`, (readonly)

   .. attribute:: color_ramp_field

      Simulation field to color map

      :type: enum in [``'NONE'``], default ``'NONE'``

   .. attribute:: color_ramp_field_scale

      Multiplier for scaling the selected field to color map

      :type: float in [0.001, 100000], default 1.0

   .. attribute:: delete_in_obstacle

      Delete fluid inside obstacles

      :type: boolean, default False

   .. data:: density_grid

      Smoke density grid

      :type: float array of 32 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), (readonly)

   .. attribute:: display_interpolation

      Interpolation method to use for smoke/fire volumes in solid mode

      * ``LINEAR``
        Linear -- Good smoothness and speed.
      * ``CUBIC``
        Cubic -- Smoothed high quality interpolation, but slower.
      * ``CLOSEST``
        Closest -- No interpolation.

      :type: enum in [``'LINEAR'``, ``'CUBIC'``, ``'CLOSEST'``], default ``'LINEAR'``

   .. attribute:: display_thickness

      Thickness of smoke display in the viewport

      :type: float in [0.001, 1000], default 1.0

   .. attribute:: dissolve_speed

      Determine how quickly the smoke dissolves (lower value makes smoke disappear faster)

      :type: int in [1, 10000], default 5

   .. data:: domain_resolution

      Smoke Grid Resolution

      :type: int array of 3 items in [-inf, inf], default (0, 0, 0), (readonly)

   .. attribute:: domain_type

      Change domain type of the simulation

      * ``GAS``
        Gas -- Create domain for gases.
      * ``LIQUID``
        Liquid -- Create domain for liquids.

      :type: enum in [``'GAS'``, ``'LIQUID'``], default ``'GAS'``

   .. attribute:: effector_group

      Limit effectors to this collection

      :type: :class:`Collection`

   .. data:: effector_weights

      :type: :class:`EffectorWeights`, (readonly)

   .. attribute:: export_manta_script

      Generate and export Mantaflow script from current domain settings during bake. This is only needed if you plan to analyze the cache (e.g. view grids, velocity vectors, particles) in Mantaflow directly (outside of Blender) after baking the simulation.

      :type: boolean, default False

   .. data:: flame_grid

      Smoke flame grid

      :type: float array of 32 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), (readonly)

   .. attribute:: flame_ignition

      Minimum temperature of the flames (higher value results in faster rising flames)

      :type: float in [0.5, 5], default 1.5

   .. attribute:: flame_max_temp

      Maximum temperature of the flames (higher value results in faster rising flames)

      :type: float in [1, 10], default 3.0

   .. attribute:: flame_smoke

      Amount of smoke created by burning fuel

      :type: float in [0, 8], default 1.0

   .. attribute:: flame_smoke_color

      Color of smoke emitted from burning fuel

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.7, 0.7, 0.7)

   .. attribute:: flame_vorticity

      Additional vorticity for the flames

      :type: float in [0, 2], default 0.5

   .. attribute:: flip_ratio

      PIC/FLIP Ratio. A value of 1.0 will result in a completely FLIP based simulation. Use a lower value for simulations which should produce smaller splashes.

      :type: float in [0, 1], default 0.97

   .. attribute:: fluid_group

      Limit fluid objects to this collection

      :type: :class:`Collection`

   .. attribute:: force_collection

      Limit forces to this collection

      :type: :class:`Collection`

   .. attribute:: fractions_distance

      Determines how far apart fluid and obstacle are (higher values will result in fluid being further away from obstacles, smaller values will let fluid move towards the inside of obstacles)

      :type: float in [-5, 5], default 0.5

   .. attribute:: fractions_threshold

      Determines how much fluid is allowed in an obstacle cell (higher values will tag a boundary cell as an obstacle easier and reduce the boundary smoothening effect)

      :type: float in [0.001, 1], default 0.05

   .. attribute:: gravity

      Gravity in X, Y and Z direction

      :type: :class:`mathutils.Vector` of 3 items in [-1000.1, 1000.1], default (0.0, 0.0, -9.81)

   .. attribute:: gridlines_cell_filter

      Cell type to be highlighted

      * ``NONE``
        None -- Highlight the cells regardless of their type.
      * ``FLUID``
        Fluid -- Highlight only the cells of type Fluid.
      * ``OBSTACLE``
        Obstacle -- Highlight only the cells of type Obstacle.
      * ``EMPTY``
        Empty -- Highlight only the cells of type Empty.
      * ``INFLOW``
        Inflow -- Highlight only the cells of type Inflow.
      * ``OUTFLOW``
        Outflow -- Highlight only the cells of type Outflow.

      :type: enum in [``'NONE'``, ``'FLUID'``, ``'OBSTACLE'``, ``'EMPTY'``, ``'INFLOW'``, ``'OUTFLOW'``], default ``'NONE'``

   .. attribute:: gridlines_color_field

      Simulation field to color map onto gridlines

      * ``NONE``
        None -- None.
      * ``FLAGS``
        Flags -- Flag grid of the fluid domain.
      * ``RANGE``
        Highlight Range -- Highlight the voxels with values of the color mapped field within the range.

      :type: enum in [``'NONE'``, ``'FLAGS'``, ``'RANGE'``], default ``'NONE'``

   .. attribute:: gridlines_lower_bound

      Lower bound of the highlighting range

      :type: float in [-inf, inf], default 0.0

   .. attribute:: gridlines_range_color

      Color used to highlight the range

      :type: float array of 4 items in [0, inf], default (1.0, 0.0, 0.0, 1.0)

   .. attribute:: gridlines_upper_bound

      Upper bound of the highlighting range

      :type: float in [-inf, inf], default 1.0

   .. attribute:: guide_alpha

      Guiding weight (higher value results in greater lag)

      :type: float in [1, 100], default 2.0

   .. attribute:: guide_beta

      Guiding size (higher value results in larger vortices)

      :type: int in [1, 50], default 5

   .. attribute:: guide_parent

      Use velocities from this object for the guiding effect (object needs to have fluid modifier and be of type domain))

      :type: :class:`Object`

   .. attribute:: guide_source

      Choose where to get guiding velocities from

      * ``DOMAIN``
        Domain -- Use a fluid domain for guiding (domain needs to be baked already so that velocities can be extracted). Guiding domain can be of any type (i.e. gas or liquid)..
      * ``EFFECTOR``
        Effector -- Use guiding (effector) objects to create fluid guiding (guiding objects should be animated and baked once set up completely).

      :type: enum in [``'DOMAIN'``, ``'EFFECTOR'``], default ``'DOMAIN'``

   .. attribute:: guide_vel_factor

      Guiding velocity factor (higher value results in greater guiding velocities)

      :type: float in [0, 100], default 2.0

   .. attribute:: has_cache_baked_any

      :type: boolean, default False

   .. attribute:: has_cache_baked_data

      :type: boolean, default False

   .. attribute:: has_cache_baked_guide

      :type: boolean, default False

   .. attribute:: has_cache_baked_mesh

      :type: boolean, default False

   .. attribute:: has_cache_baked_noise

      :type: boolean, default False

   .. attribute:: has_cache_baked_particles

      :type: boolean, default False

   .. data:: heat_grid

      Smoke heat grid

      :type: float array of 32 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), (readonly)

   .. attribute:: highres_sampling

      Method for sampling the high resolution flow

      :type: enum in [``'FULLSAMPLE'``, ``'LINEAR'``, ``'NEAREST'``], default ``'FULLSAMPLE'``

   .. attribute:: is_cache_baking_any

      :type: boolean, default False

   .. attribute:: is_cache_baking_data

      :type: boolean, default False

   .. attribute:: is_cache_baking_guide

      :type: boolean, default False

   .. attribute:: is_cache_baking_mesh

      :type: boolean, default False

   .. attribute:: is_cache_baking_noise

      :type: boolean, default False

   .. attribute:: is_cache_baking_particles

      :type: boolean, default False

   .. attribute:: mesh_concave_lower

      Lower mesh concavity bound (high values tend to smoothen and fill out concave regions)

      :type: float in [0, 10], default 0.4

   .. attribute:: mesh_concave_upper

      Upper mesh concavity bound (high values tend to smoothen and fill out concave regions)

      :type: float in [0, 10], default 3.5

   .. attribute:: mesh_generator

      Which particle level set generator to use

      * ``IMPROVED``
        Final -- Use improved particle level set (slower but more precise and with mesh smoothening options).
      * ``UNION``
        Preview -- Use union particle level set (faster but lower quality).

      :type: enum in [``'IMPROVED'``, ``'UNION'``], default ``'IMPROVED'``

   .. attribute:: mesh_particle_radius

      Particle radius factor (higher value results in larger (meshed) particles). Needs to be adjusted after changing the mesh scale.

      :type: float in [0, 10], default 2.0

   .. attribute:: mesh_scale

      The mesh simulation is scaled up by this factor (compared to the base resolution of the domain). For best meshing, it is recommended to adjust the mesh particle radius alongside this value.

      :type: int in [1, 100], default 2

   .. attribute:: mesh_smoothen_neg

      Negative mesh smoothening

      :type: int in [0, 100], default 1

   .. attribute:: mesh_smoothen_pos

      Positive mesh smoothening

      :type: int in [0, 100], default 1

   .. attribute:: noise_pos_scale

      Scale of noise (higher value results in larger vortices)

      :type: float in [0.0001, 10], default 2.0

   .. attribute:: noise_scale

      The noise simulation is scaled up by this factor (compared to the base resolution of the domain)

      :type: int in [1, 100], default 2

   .. attribute:: noise_strength

      Strength of noise

      :type: float in [0, 10], default 1.0

   .. attribute:: noise_time_anim

      Animation time of noise

      :type: float in [0.0001, 10], default 0.1

   .. attribute:: openvdb_cache_compress_type

      Compression method to be used

      * ``ZIP``
        Zip -- Effective but slow compression.
      * ``BLOSC``
        Blosc -- Multithreaded compression, similar in size and quality as 'Zip'.
      * ``NONE``
        None -- Do not use any compression.

      :type: enum in [``'ZIP'``, ``'BLOSC'``, ``'NONE'``], default ``'BLOSC'``

   .. attribute:: openvdb_data_depth

      Bit depth for fluid particles and grids (lower bit values reduce file size)

      :type: enum in [``'NONE'``], default ``'NONE'``

   .. attribute:: particle_band_width

      Particle (narrow) band width (higher value results in thicker band and more particles)

      :type: float in [0, 1000], default 3.0

   .. attribute:: particle_max

      Maximum number of particles per cell (ensures that each cell has at most this amount of particles)

      :type: int in [0, 1000], default 16

   .. attribute:: particle_min

      Minimum number of particles per cell (ensures that each cell has at least this amount of particles)

      :type: int in [0, 1000], default 8

   .. attribute:: particle_number

      Particle number factor (higher value results in more particles)

      :type: int in [1, 5], default 2

   .. attribute:: particle_radius

      Particle radius factor. Increase this value if the simulation appears to leak volume, decrease it if the simulation seems to gain volume.

      :type: float in [0, 10], default 1.0

   .. attribute:: particle_randomness

      Randomness factor for particle sampling

      :type: float in [0, 10], default 0.1

   .. attribute:: particle_scale

      The particle simulation is scaled up by this factor (compared to the base resolution of the domain)

      :type: int in [1, 100], default 1

   .. attribute:: resolution_max

      Resolution used for the fluid domain. Value corresponds to the longest domain side (resolution for other domain sides is calculated automatically).

      :type: int in [6, 10000], default 32

   .. attribute:: show_gridlines

      Show gridlines

      :type: boolean, default False

   .. attribute:: show_velocity

      Visualize vector fields

      :type: boolean, default False

   .. attribute:: simulation_method

      Change the underlying simulation method

      * ``FLIP``
        FLIP -- Use FLIP as the simulation method (more splashy behavior).
      * ``APIC``
        APIC -- Use APIC as the simulation method (more energetic and stable behavior).

      :type: enum in [``'FLIP'``, ``'APIC'``], default ``'FLIP'``

   .. attribute:: slice_axis

      * ``AUTO``
        Auto -- Adjust slice direction according to the view direction.
      * ``X``
        X -- Slice along the X axis.
      * ``Y``
        Y -- Slice along the Y axis.
      * ``Z``
        Z -- Slice along the Z axis.

      :type: enum in [``'AUTO'``, ``'X'``, ``'Y'``, ``'Z'``], default ``'AUTO'``

   .. attribute:: slice_depth

      Position of the slice

      :type: float in [0, 1], default 0.5

   .. attribute:: slice_per_voxel

      How many slices per voxel should be generated

      :type: float in [0, 100], default 5.0

   .. attribute:: sndparticle_boundary

      How particles that left the domain are treated

      * ``DELETE``
        Delete -- Delete secondary particles that are inside obstacles or left the domain.
      * ``PUSHOUT``
        Push Out -- Push secondary particles that left the domain back into the domain.

      :type: enum in [``'DELETE'``, ``'PUSHOUT'``], default ``'DELETE'``

   .. attribute:: sndparticle_bubble_buoyancy

      Amount of buoyancy force that rises bubbles (high value results in bubble movement mainly upwards)

      :type: float in [0, 100], default 0.5

   .. attribute:: sndparticle_bubble_drag

      Amount of drag force that moves bubbles along with the fluid (high value results in bubble movement mainly along with the fluid)

      :type: float in [0, 100], default 0.6

   .. attribute:: sndparticle_combined_export

      Determines which particle systems are created from secondary particles

      * ``OFF``
        Off -- Create a separate particle system for every secondary particle type.
      * ``SPRAY_FOAM``
        Spray + Foam -- Spray and foam particles are saved in the same particle system.
      * ``SPRAY_BUBBLES``
        Spray + Bubbles -- Spray and bubble particles are saved in the same particle system.
      * ``FOAM_BUBBLES``
        Foam + Bubbles -- Foam and bubbles particles are saved in the same particle system.
      * ``SPRAY_FOAM_BUBBLES``
        Spray + Foam + Bubbles -- Create one particle system that contains all three secondary particle types.

      :type: enum in [``'OFF'``, ``'SPRAY_FOAM'``, ``'SPRAY_BUBBLES'``, ``'FOAM_BUBBLES'``, ``'SPRAY_FOAM_BUBBLES'``], default ``'OFF'``

   .. attribute:: sndparticle_life_max

      Highest possible particle lifetime

      :type: float in [0, 10000], default 25.0

   .. attribute:: sndparticle_life_min

      Lowest possible particle lifetime

      :type: float in [0, 10000], default 10.0

   .. attribute:: sndparticle_potential_max_energy

      Upper clamping threshold that indicates the fluid speed where cells no longer emit more particles (higher value results in generally less particles)

      :type: float in [0, 1000], default 5.0

   .. attribute:: sndparticle_potential_max_trappedair

      Upper clamping threshold for marking fluid cells where air is trapped (higher value results in less marked cells)

      :type: float in [0, 1000], default 20.0

   .. attribute:: sndparticle_potential_max_wavecrest

      Upper clamping threshold for marking fluid cells as wave crests (higher value results in less marked cells)

      :type: float in [0, 1000], default 8.0

   .. attribute:: sndparticle_potential_min_energy

      Lower clamping threshold that indicates the fluid speed where cells start to emit particles (lower values result in generally more particles)

      :type: float in [0, 1000], default 1.0

   .. attribute:: sndparticle_potential_min_trappedair

      Lower clamping threshold for marking fluid cells where air is trapped (lower value results in more marked cells)

      :type: float in [0, 1000], default 5.0

   .. attribute:: sndparticle_potential_min_wavecrest

      Lower clamping threshold for marking fluid cells as wave crests (lower value results in more marked cells)

      :type: float in [0, 1000], default 2.0

   .. attribute:: sndparticle_potential_radius

      Radius to compute potential for each cell (higher values are slower but create smoother potential grids)

      :type: int in [1, 4], default 2

   .. attribute:: sndparticle_sampling_trappedair

      Maximum number of particles generated per trapped air cell per frame

      :type: int in [0, 10000], default 40

   .. attribute:: sndparticle_sampling_wavecrest

      Maximum number of particles generated per wave crest cell per frame

      :type: int in [0, 10000], default 200

   .. attribute:: sndparticle_update_radius

      Radius to compute position update for each particle (higher values are slower but particles move less chaotic)

      :type: int in [1, 4], default 2

   .. data:: start_point

      Start point

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: surface_tension

      Surface tension of liquid (higher value results in greater hydrophobic behavior)

      :type: float in [0, 100], default 0.0

   .. attribute:: sys_particle_maximum

      Maximum number of fluid particles that are allowed in this simulation

      :type: int in [0, inf], default 0

   .. data:: temperature_grid

      Smoke temperature grid, range 0 to 1 represents 0 to 1000K

      :type: float array of 32 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), (readonly)

   .. attribute:: time_scale

      Adjust simulation speed

      :type: float in [0.0001, 10], default 1.0

   .. attribute:: timesteps_max

      Maximum number of simulation steps to perform for one frame

      :type: int in [1, 100], default 4

   .. attribute:: timesteps_min

      Minimum number of simulation steps to perform for one frame

      :type: int in [1, 100], default 1

   .. attribute:: use_adaptive_domain

      Adapt simulation resolution and size to fluid

      :type: boolean, default False

   .. attribute:: use_adaptive_timesteps

      Automatically decide when to perform multiple simulation steps per frame

      :type: boolean, default True

   .. attribute:: use_bubble_particles

      Create bubble particle system

      :type: boolean, default False

   .. attribute:: use_collision_border_back

      Enable collisions with back domain border

      :type: boolean, default False

   .. attribute:: use_collision_border_bottom

      Enable collisions with bottom domain border

      :type: boolean, default False

   .. attribute:: use_collision_border_front

      Enable collisions with front domain border

      :type: boolean, default False

   .. attribute:: use_collision_border_left

      Enable collisions with left domain border

      :type: boolean, default False

   .. attribute:: use_collision_border_right

      Enable collisions with right domain border

      :type: boolean, default False

   .. attribute:: use_collision_border_top

      Enable collisions with top domain border

      :type: boolean, default False

   .. attribute:: use_color_ramp

      Render a simulation field while mapping its voxels values to the colors of a ramp or using a predefined color code

      :type: boolean, default False

   .. attribute:: use_diffusion

      Enable fluid diffusion settings (e.g. viscosity, surface tension)

      :type: boolean, default False

   .. attribute:: use_dissolve_smoke

      Let smoke disappear over time

      :type: boolean, default False

   .. attribute:: use_dissolve_smoke_log

      Dissolve smoke in a logarithmic fashion. Dissolves quickly at first, but lingers longer.

      :type: boolean, default True

   .. attribute:: use_flip_particles

      Create liquid particle system

      :type: boolean, default False

   .. attribute:: use_foam_particles

      Create foam particle system

      :type: boolean, default False

   .. attribute:: use_fractions

      Fractional obstacles improve and smoothen the fluid-obstacle boundary

      :type: boolean, default False

   .. attribute:: use_guide

      Enable fluid guiding

      :type: boolean, default False

   .. attribute:: use_mesh

      Enable fluid mesh (using amplification)

      :type: boolean, default True

   .. attribute:: use_noise

      Enable fluid noise (using amplification)

      :type: boolean, default False

   .. attribute:: use_slice

      Perform a single slice of the domain object

      :type: boolean, default False

   .. attribute:: use_speed_vectors

      Caches velocities of mesh vertices. These will be used (automatically) when rendering with motion blur enabled.

      :type: boolean, default False

   .. attribute:: use_spray_particles

      Create spray particle system

      :type: boolean, default False

   .. attribute:: use_tracer_particles

      Create tracer particle system

      :type: boolean, default False

   .. attribute:: use_viscosity

      Simulate fluids with high viscosity using a special solver

      :type: boolean, default False

   .. attribute:: vector_display_type

      * ``NEEDLE``
        Needle -- Display vectors as needles.
      * ``STREAMLINE``
        Streamlines -- Display vectors as streamlines.
      * ``MAC``
        MAC Grid -- Display vector field as MAC grid.

      :type: enum in [``'NEEDLE'``, ``'STREAMLINE'``, ``'MAC'``], default ``'NEEDLE'``

   .. attribute:: vector_field

      Vector field to be represented by the display vectors

      * ``FLUID_VELOCITY``
        Fluid Velocity -- Velocity field of the fluid domain.
      * ``GUIDE_VELOCITY``
        Guide Velocity -- Guide velocity field of the fluid domain.
      * ``FORCE``
        Force -- Force field of the fluid domain.

      :type: enum in [``'FLUID_VELOCITY'``, ``'GUIDE_VELOCITY'``, ``'FORCE'``], default ``'FLUID_VELOCITY'``

   .. attribute:: vector_scale

      Multiplier for scaling the vectors

      :type: float in [0, 1000], default 1.0

   .. attribute:: vector_scale_with_magnitude

      Scale vectors with their magnitudes

      :type: boolean, default False

   .. attribute:: vector_show_mac_x

      Show X-component of MAC Grid

      :type: boolean, default True

   .. attribute:: vector_show_mac_y

      Show Y-component of MAC Grid

      :type: boolean, default True

   .. attribute:: vector_show_mac_z

      Show Z-component of MAC Grid

      :type: boolean, default True

   .. data:: velocity_grid

      Smoke velocity grid

      :type: float array of 32 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), (readonly)

   .. attribute:: velocity_scale

      Factor to control the amount of motion blur

      :type: float in [0, inf], default 1.0

   .. attribute:: viscosity_base

      Viscosity setting: value that is multiplied by 10 to the power of (exponent*-1)

      :type: float in [0, 10], default 1.0

   .. attribute:: viscosity_exponent

      Negative exponent for the viscosity value (to simplify entering small values e.g. 5*10^-6)

      :type: int in [0, 10], default 6

   .. attribute:: viscosity_value

      Viscosity of liquid (higher values result in more viscous fluids, a value of 0 will still apply some viscosity)

      :type: float in [0, 10], default 0.05

   .. attribute:: vorticity

      Amount of turbulence and rotation in smoke

      :type: float in [0, 4], default 0.0

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

References
----------

.. hlist::
   :columns: 2

   * :class:`FluidModifier.domain_settings`

