Object(ID)
==========

.. currentmodule:: bpy.types


Basic Object Operations Example
+++++++++++++++++++++++++++++++

This script demonstrates basic operations on object like creating new
object, placing it into a view layer, selecting it and making it active.

.. literalinclude:: ..\examples\bpy.types.Object.py
   :lines: 9-

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Object(ID)

   Object data-block defining an object in a scene

   .. attribute:: active_material

      Active material being displayed

      :type: :class:`Material`

   .. attribute:: active_material_index

      Index of active material slot

      :type: int in [0, inf], default 0

   .. attribute:: active_selection_set

      Index of the currently active selection set

      :type: int in [-inf, inf], default 0

   .. data:: active_shape_key

      Current shape key

      :type: :class:`ShapeKey`, (readonly)

   .. attribute:: active_shape_key_index

      Current shape key index

      :type: int in [-32768, 32767], default 0

   .. attribute:: add_rest_position_attribute

      Add a "rest_position" attribute that is a copy of the position attribute before shape keys and modifiers are evaluated

      :type: boolean, default False

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. data:: animation_visualization

      Animation data for this data-block

      :type: :class:`AnimViz`, (readonly, never None)

   .. data:: bound_box

      Object's bounding box in object-space coordinates, all values are -1.0 when not available

      :type: float multi-dimensional array of 8 * 3 items in [-inf, inf], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), (readonly)

   .. data:: collision

      Settings for using the object as a collider in physics simulation

      :type: :class:`CollisionSettings`, (readonly)

   .. attribute:: color

      Object color and alpha, used when the Object Color mode is enabled

      :type: float array of 4 items in [0, inf], default (1.0, 1.0, 1.0, 1.0)

   .. data:: constraints

      Constraints affecting the transformation of the object

      :type: :class:`ObjectConstraints` :class:`bpy_prop_collection` of :class:`Constraint`, (readonly)

   .. data:: cycles

      Cycles object settings

      :type: :class:`CyclesObjectSettings`, (readonly)

   .. attribute:: data

      Object data

      :type: :class:`ID`

   .. attribute:: delta_location

      Extra translation added to the location of the object

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: delta_rotation_euler

      Extra rotation added to the rotation of the object (when using Euler rotations)

      :type: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: delta_rotation_quaternion

      Extra rotation added to the rotation of the object (when using Quaternion rotations)

      :type: :class:`mathutils.Quaternion` rotation of 4 items in [-inf, inf], default (1.0, 0.0, 0.0, 0.0)

   .. attribute:: delta_scale

      Extra scaling added to the scale of the object

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (1.0, 1.0, 1.0)

   .. attribute:: dimensions

      Absolute bounding box dimensions of the object.
      Warning: Assigning to it or its members multiple consecutive times will not work correctly, as this needs up-to-date evaluated data

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. data:: display

      Object display settings for 3D viewport

      :type: :class:`ObjectDisplay`, (readonly, never None)

   .. attribute:: display_bounds_type

      Object boundary display type

      * ``BOX``
        Box -- Display bounds as box.
      * ``SPHERE``
        Sphere -- Display bounds as sphere.
      * ``CYLINDER``
        Cylinder -- Display bounds as cylinder.
      * ``CONE``
        Cone -- Display bounds as cone.
      * ``CAPSULE``
        Capsule -- Display bounds as capsule.

      :type: enum in [``'BOX'``, ``'SPHERE'``, ``'CYLINDER'``, ``'CONE'``, ``'CAPSULE'``], default ``'BOX'``

   .. attribute:: display_type

      How to display object in viewport

      * ``BOUNDS``
        Bounds -- Display the bounds of the object.
      * ``WIRE``
        Wire -- Display the object as a wireframe.
      * ``SOLID``
        Solid -- Display the object as a solid (if solid drawing is enabled in the viewport).
      * ``TEXTURED``
        Textured -- Display the object with textures (if textures are enabled in the viewport).

      :type: enum in [``'BOUNDS'``, ``'WIRE'``, ``'SOLID'``, ``'TEXTURED'``], default ``'TEXTURED'``

   .. attribute:: empty_display_size

      Size of display for empties in the viewport

      :type: float in [0.0001, 1000], default 1.0

   .. attribute:: empty_display_type

      Viewport display style for empties

      :type: enum in :ref:`rna_enum_object_empty_drawtype_items`, default ``'PLAIN_AXES'``

   .. attribute:: empty_image_depth

      Determine which other objects will occlude the image

      :type: enum in [``'DEFAULT'``, ``'FRONT'``, ``'BACK'``], default ``'DEFAULT'``

   .. attribute:: empty_image_offset

      Origin offset distance

      :type: float array of 2 items in [-inf, inf], default (-0.5, -0.5)

   .. attribute:: empty_image_side

      Show front/back side

      :type: enum in [``'DOUBLE_SIDED'``, ``'FRONT'``, ``'BACK'``], default ``'DOUBLE_SIDED'``

   .. data:: field

      Settings for using the object as a field in physics simulation

      :type: :class:`FieldSettings`, (readonly)

   .. attribute:: hide_probe_plane

      Globally disable in planar light probes

      :type: boolean, default False

   .. attribute:: hide_probe_sphere

      Globally disable in spherical light probes

      :type: boolean, default False

   .. attribute:: hide_probe_volume

      Globally disable in volume probes

      :type: boolean, default False

   .. attribute:: hide_render

      Globally disable in renders

      :type: boolean, default False

   .. attribute:: hide_select

      Disable selection in viewport

      :type: boolean, default False

   .. attribute:: hide_viewport

      Globally disable in viewports

      :type: boolean, default False

   .. data:: image_user

      Parameters defining which layer, pass and frame of the image is displayed

      :type: :class:`ImageUser`, (readonly, never None)

   .. attribute:: instance_collection

      Instance an existing collection

      :type: :class:`Collection`

   .. attribute:: instance_faces_scale

      Scale the face instance objects

      :type: float in [0.001, 10000], default 1.0

   .. attribute:: instance_type

      If not None, object instancing method to use

      * ``NONE``
        None.
      * ``VERTS``
        Vertices -- Instantiate child objects on all vertices.
      * ``FACES``
        Faces -- Instantiate child objects on all faces.
      * ``COLLECTION``
        Collection -- Enable collection instancing.

      :type: enum in [``'NONE'``, ``'VERTS'``, ``'FACES'``, ``'COLLECTION'``], default ``'NONE'``

   .. data:: is_from_instancer

      Object comes from a instancer

      :type: boolean, default False, (readonly)

   .. data:: is_from_set

      Object comes from a background set

      :type: boolean, default False, (readonly)

   .. attribute:: is_holdout

      Render objects as a holdout or matte, creating a hole in the image with zero alpha, to fill out in compositing with real footage or another render

      :type: boolean, default False

   .. data:: is_instancer

      :type: boolean, default False, (readonly)

   .. attribute:: is_shadow_catcher

      Only render shadows and reflections on this object, for compositing renders into real footage. Objects with this setting are considered to already exist in the footage, objects without it are synthetic objects being composited into it.

      :type: boolean, default False

   .. data:: light_linking

      Light linking settings

      :type: :class:`ObjectLightLinking`, (readonly, never None)

   .. attribute:: lightgroup

      Lightgroup that the object belongs to

      :type: string, default "", (never None)

   .. data:: lineart

      Line Art settings for the object

      :type: :class:`ObjectLineArt`, (readonly)

   .. attribute:: location

      Location of the object

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: lock_location

      Lock editing of location when transforming

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: lock_rotation

      Lock editing of rotation when transforming

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: lock_rotation_w

      Lock editing of 'angle' component of four-component rotations when transforming

      :type: boolean, default False

   .. attribute:: lock_rotations_4d

      Lock editing of four component rotations by components (instead of as Eulers)

      :type: boolean, default True

   .. attribute:: lock_scale

      Lock editing of scale when transforming

      :type: boolean array of 3 items, default (False, False, False)

   .. data:: material_slots

      Material slots in the object

      :type: :class:`bpy_prop_collection` of :class:`MaterialSlot`, (readonly)

   .. attribute:: matrix_basis

      Matrix access to location, rotation and scale (including deltas), before constraints and parenting are applied

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: matrix_local

      Parent relative transformation matrix.
      Warning: Only takes into account object parenting, so e.g. in case of bone parenting you get a matrix relative to the Armature object, not to the actual parent bone

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: matrix_parent_inverse

      Inverse of object's parent matrix at time of parenting

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0))

   .. attribute:: matrix_world

      Worldspace transformation matrix

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. data:: mode

      Object interaction mode

      :type: enum in :ref:`rna_enum_object_mode_items`, default ``'OBJECT'``, (readonly)

   .. data:: modifiers

      Modifiers affecting the geometric data of the object

      :type: :class:`ObjectModifiers` :class:`bpy_prop_collection` of :class:`Modifier`, (readonly)

   .. data:: motion_path

      Motion Path for this element

      :type: :class:`MotionPath`, (readonly)

   .. attribute:: parent

      Parent object

      :type: :class:`Object`

   .. attribute:: parent_bone

      Name of parent bone in case of a bone parenting relation

      :type: string, default "", (never None)

   .. attribute:: parent_type

      Type of parent relation

      * ``OBJECT``
        Object -- The object is parented to an object.
      * ``ARMATURE``
        Armature.
      * ``LATTICE``
        Lattice -- The object is parented to a lattice.
      * ``VERTEX``
        Vertex -- The object is parented to a vertex.
      * ``VERTEX_3``
        3 Vertices.
      * ``BONE``
        Bone -- The object is parented to a bone.

      :type: enum in [``'OBJECT'``, ``'ARMATURE'``, ``'LATTICE'``, ``'VERTEX'``, ``'VERTEX_3'``, ``'BONE'``], default ``'OBJECT'``

   .. attribute:: parent_vertices

      Indices of vertices in case of a vertex parenting relation

      :type: int array of 3 items in [0, inf], default (0, 0, 0)

   .. data:: particle_systems

      Particle systems emitted from the object

      :type: :class:`ParticleSystems` :class:`bpy_prop_collection` of :class:`ParticleSystem`, (readonly)

   .. attribute:: pass_index

      Index number for the "Object Index" render pass

      :type: int in [0, 32767], default 0

   .. data:: pose

      Current pose for armatures

      :type: :class:`Pose`, (readonly)

   .. data:: rigid_body

      Settings for rigid body simulation

      :type: :class:`RigidBodyObject`, (readonly)

   .. data:: rigid_body_constraint

      Constraint constraining rigid bodies

      :type: :class:`RigidBodyConstraint`, (readonly)

   .. attribute:: rotation_axis_angle

      Angle of Rotation for Axis-Angle rotation representation

      :type: float array of 4 items in [-inf, inf], default (0.0, 0.0, 1.0, 0.0)

   .. attribute:: rotation_euler

      Rotation in Eulers

      :type: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: rotation_mode

      The kind of rotation to apply, values from other rotation modes aren't used

      :type: enum in :ref:`rna_enum_object_rotation_mode_items`, default ``'XYZ'``

   .. attribute:: rotation_quaternion

      Rotation in Quaternions

      :type: :class:`mathutils.Quaternion` rotation of 4 items in [-inf, inf], default (1.0, 0.0, 0.0, 0.0)

   .. attribute:: scale

      Scaling of the object

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (1.0, 1.0, 1.0)

   .. data:: selection_sets

      List of groups of bones for easy selection

      :type: :class:`bpy_prop_collection` of :class:`SelectionSet`, (readonly)

   .. data:: shader_effects

      Effects affecting display of object

      :type: :class:`ObjectShaderFx` :class:`bpy_prop_collection` of :class:`ShaderFx`, (readonly)

   .. attribute:: shadow_terminator_geometry_offset

      Offset rays from the surface to reduce shadow terminator artifact on low poly geometry. Only affects triangles at grazing angles to light

      :type: float in [0, inf], default 0.1

   .. attribute:: shadow_terminator_normal_offset

      Offset rays from the surface to reduce shadow terminator artifact on low poly geometry. Only affect triangles that are affected by the geometry offset

      :type: float in [0, inf], default 0.0

   .. attribute:: shadow_terminator_shading_offset

      Push the shadow terminator towards the light to hide artifacts on low poly geometry

      :type: float in [0, inf], default 0.0

   .. attribute:: show_all_edges

      Display all edges for mesh objects

      :type: boolean, default False

   .. attribute:: show_axis

      Display the object's origin and axes

      :type: boolean, default False

   .. attribute:: show_bounds

      Display the object's bounds

      :type: boolean, default False

   .. attribute:: show_empty_image_only_axis_aligned

      Only display the image when it is aligned with the view axis

      :type: boolean, default False

   .. attribute:: show_empty_image_orthographic

      Display image in orthographic mode

      :type: boolean, default True

   .. attribute:: show_empty_image_perspective

      Display image in perspective mode

      :type: boolean, default True

   .. attribute:: show_in_front

      Make the object display in front of others

      :type: boolean, default False

   .. attribute:: show_instancer_for_render

      Make instancer visible when rendering

      :type: boolean, default True

   .. attribute:: show_instancer_for_viewport

      Make instancer visible in the viewport

      :type: boolean, default True

   .. attribute:: show_name

      Display the object's name

      :type: boolean, default False

   .. attribute:: show_only_shape_key

      Only show the active shape key at full value

      :type: boolean, default False

   .. attribute:: show_texture_space

      Display the object's texture space

      :type: boolean, default False

   .. attribute:: show_transparent

      Display material transparency in the object

      :type: boolean, default False

   .. attribute:: show_wire

      Display the object's wireframe over solid shading

      :type: boolean, default False

   .. data:: soft_body

      Settings for soft body simulation

      :type: :class:`SoftBodySettings`, (readonly)

   .. attribute:: track_axis

      Axis that points in the 'forward' direction (applies to Instance Vertices when Align to Vertex Normal is enabled)

      :type: enum in :ref:`rna_enum_object_axis_items`, default ``'POS_X'``

   .. data:: type

      Type of object

      :type: enum in :ref:`rna_enum_object_type_items`, default ``'EMPTY'``, (readonly)

   .. attribute:: up_axis

      Axis that points in the upward direction (applies to Instance Vertices when Align to Vertex Normal is enabled)

      :type: enum in [``'X'``, ``'Y'``, ``'Z'``], default ``'X'``

   .. attribute:: use_camera_lock_parent

      View Lock 3D viewport camera transformation affects the object's parent instead

      :type: boolean, default False

   .. data:: use_dynamic_topology_sculpting

      :type: boolean, default False, (readonly)

   .. attribute:: use_empty_image_alpha

      Use alpha blending instead of alpha test (can produce sorting artifacts)

      :type: boolean, default False

   .. attribute:: use_grease_pencil_lights

      Lights affect Grease Pencil object

      :type: boolean, default True

   .. attribute:: use_instance_faces_scale

      Scale instance based on face size

      :type: boolean, default False

   .. attribute:: use_instance_vertices_rotation

      Rotate instance according to vertex normal

      :type: boolean, default False

   .. attribute:: use_mesh_mirror_x

      Enable mesh symmetry in the X axis

      :type: boolean, default False

   .. attribute:: use_mesh_mirror_y

      Enable mesh symmetry in the Y axis

      :type: boolean, default False

   .. attribute:: use_mesh_mirror_z

      Enable mesh symmetry in the Z axis

      :type: boolean, default False

   .. attribute:: use_parent_final_indices

      Use the final evaluated indices rather than the original mesh indices

      :type: boolean, default False

   .. attribute:: use_shape_key_edit_mode

      Display shape keys in edit mode (for meshes only)

      :type: boolean, default False

   .. attribute:: use_simulation_cache

      Cache frames during simulation nodes playback

      :type: boolean, default True

   .. data:: vertex_groups

      Vertex groups of the object

      :type: :class:`VertexGroups` :class:`bpy_prop_collection` of :class:`VertexGroup`, (readonly)

   .. attribute:: visible_camera

      Object visibility to camera rays

      :type: boolean, default True

   .. attribute:: visible_diffuse

      Object visibility to diffuse rays

      :type: boolean, default True

   .. attribute:: visible_glossy

      Object visibility to glossy rays

      :type: boolean, default True

   .. attribute:: visible_shadow

      Object visibility to shadow rays

      :type: boolean, default True

   .. attribute:: visible_transmission

      Object visibility to transmission rays

      :type: boolean, default True

   .. attribute:: visible_volume_scatter

      Object visibility to volume scattering rays

      :type: boolean, default True

   .. data:: children

      All the children of this object.
      
      :type: tuple of :class:`Object`
      
      .. note:: Takes ``O(len(bpy.data.objects))`` time.

      (readonly)

   .. data:: children_recursive

      A list of all children from this object.
      
      :type: list of :class:`Object`
      
      .. note:: Takes ``O(len(bpy.data.objects))`` time.

      (readonly)

   .. data:: users_collection

      The collections this object is in.
      
      :type: tuple of :class:`Collection`
      
      .. note:: Takes ``O(len(bpy.data.collections) + len(bpy.data.scenes))`` time.

      (readonly)

   .. data:: users_scene

      The scenes this object is in.
      
      :type: tuple of :class:`Scene`
      
      .. note:: Takes ``O(len(bpy.data.scenes) * len(bpy.data.objects))`` time.

      (readonly)

   .. method:: select_get(*, view_layer=None)

      Test if the object is selected. The selection state is per view layer.

      :arg view_layer: Use this instead of the active view layer
      :type view_layer: :class:`ViewLayer`, (optional)
      :return: Object selected
      :rtype: boolean

   .. method:: select_set(state, *, view_layer=None)

      Select or deselect the object. The selection state is per view layer.

      :arg state: Selection state to define
      :type state: boolean
      :arg view_layer: Use this instead of the active view layer
      :type view_layer: :class:`ViewLayer`, (optional)

   .. method:: hide_get(*, view_layer=None)

      Test if the object is hidden for viewport editing. This hiding state is per view layer.

      :arg view_layer: Use this instead of the active view layer
      :type view_layer: :class:`ViewLayer`, (optional)
      :return: Object hidden
      :rtype: boolean

   .. method:: hide_set(state, *, view_layer=None)

      Hide the object for viewport editing. This hiding state is per view layer.

      :arg state: Hide state to define
      :type state: boolean
      :arg view_layer: Use this instead of the active view layer
      :type view_layer: :class:`ViewLayer`, (optional)

   .. method:: visible_get(*, view_layer=None, viewport=None)

      Test if the object is visible in the 3D viewport, taking into account all visibility settings

      :arg view_layer: Use this instead of the active view layer
      :type view_layer: :class:`ViewLayer`, (optional)
      :arg viewport: Use this instead of the active 3D viewport
      :type viewport: :class:`SpaceView3D`, (optional)
      :return: Object visible
      :rtype: boolean

   .. method:: holdout_get(*, view_layer=None)

      Test if object is masked in the view layer

      :arg view_layer: Use this instead of the active view layer
      :type view_layer: :class:`ViewLayer`, (optional)
      :return: Object holdout
      :rtype: boolean

   .. method:: indirect_only_get(*, view_layer=None)

      Test if object is set to contribute only indirectly (through shadows and reflections) in the view layer

      :arg view_layer: Use this instead of the active view layer
      :type view_layer: :class:`ViewLayer`, (optional)
      :return: Object indirect only
      :rtype: boolean

   .. method:: local_view_get(viewport)

      Get the local view state for this object

      :arg viewport: Viewport in local view
      :type viewport: :class:`SpaceView3D`
      :return: Object local view state
      :rtype: boolean

   .. method:: local_view_set(viewport, state)

      Set the local view state for this object

      :arg viewport: Viewport in local view
      :type viewport: :class:`SpaceView3D`
      :arg state: Local view state to define
      :type state: boolean

   .. method:: visible_in_viewport_get(viewport)

      Check for local view and local collections for this viewport and object

      :arg viewport: Viewport in local collections
      :type viewport: :class:`SpaceView3D`
      :return: Object viewport visibility
      :rtype: boolean

   .. method:: convert_space(*, pose_bone=None, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), from_space='WORLD', to_space='WORLD')

      Convert (transform) the given matrix from one space to another

      :arg pose_bone: Bone to use to define spaces (may be None, in which case only the two 'WORLD' and 'LOCAL' spaces are usable)
      :type pose_bone: :class:`PoseBone`, (optional)
      :arg matrix: The matrix to transform
      :type matrix: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], (optional)
      :arg from_space: The space in which 'matrix' is currently

         * ``WORLD``
           World Space -- The most global space in Blender.
         * ``POSE``
           Pose Space -- The pose space of a bone (its armature's object space).
         * ``LOCAL_WITH_PARENT``
           Local With Parent -- The rest pose local space of a bone (this matrix includes parent transforms).
         * ``LOCAL``
           Local Space -- The local space of an object/bone.
      :type from_space: enum in [``'WORLD'``, ``'POSE'``, ``'LOCAL_WITH_PARENT'``, ``'LOCAL'``], (optional)
      :arg to_space: The space to which you want to transform 'matrix'

         * ``WORLD``
           World Space -- The most global space in Blender.
         * ``POSE``
           Pose Space -- The pose space of a bone (its armature's object space).
         * ``LOCAL_WITH_PARENT``
           Local With Parent -- The rest pose local space of a bone (this matrix includes parent transforms).
         * ``LOCAL``
           Local Space -- The local space of an object/bone.
      :type to_space: enum in [``'WORLD'``, ``'POSE'``, ``'LOCAL_WITH_PARENT'``, ``'LOCAL'``], (optional)
      :return: The transformed matrix
      :rtype: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf]

   .. method:: calc_matrix_camera(depsgraph, *, x=1, y=1, scale_x=1.0, scale_y=1.0)

      Generate the camera projection matrix of this object (mostly useful for Camera and Light types)

      :arg depsgraph: Depsgraph to get evaluated data from
      :type depsgraph: :class:`Depsgraph`
      :arg x: Width of the render area
      :type x: int in [0, inf], (optional)
      :arg y: Height of the render area
      :type y: int in [0, inf], (optional)
      :arg scale_x: Width scaling factor
      :type scale_x: float in [1e-06, inf], (optional)
      :arg scale_y: Height scaling factor
      :type scale_y: float in [1e-06, inf], (optional)
      :return: The camera projection matrix
      :rtype: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf]

   .. method:: camera_fit_coords(depsgraph, coordinates)

      Compute the coordinate (and scale for ortho cameras) given object should be to 'see' all given coordinates

      :arg depsgraph: Depsgraph to get evaluated data from
      :type depsgraph: :class:`Depsgraph`
      :arg coordinates: Coordinates to fit in
      :type coordinates: float array of 1 items in [-inf, inf], (never None)
      :return:
         `co_return`, The location to aim to be able to see all given points, :class:`mathutils.Vector` of 3 items in [-inf, inf]

         `scale_return`, The ortho scale to aim to be able to see all given points (if relevant), float in [-inf, inf]

      :rtype: (:class:`mathutils.Vector` of 3 items in [-inf, inf], float in [-inf, inf])

   .. method:: crazyspace_eval(depsgraph, scene)

      Compute orientation mapping between vertices of an original object and object with shape keys and deforming modifiers applied.The evaluation is to be freed with the crazyspace_eval_free function

      :arg depsgraph: Dependency Graph, Evaluated dependency graph
      :type depsgraph: :class:`Depsgraph`
      :arg scene: Scene, Scene of the object
      :type scene: :class:`Scene`

   .. method:: crazyspace_displacement_to_deformed(*, vertex_index=0, displacement=(0.0, 0.0, 0.0))

      Convert displacement vector from non-deformed object space to deformed object space

      :arg vertex_index: vertex_index
      :type vertex_index: int in [-inf, inf], (optional)
      :arg displacement: displacement
      :type displacement: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
      :return: displacement_deformed
      :rtype: :class:`mathutils.Vector` of 3 items in [-inf, inf]

   .. method:: crazyspace_displacement_to_original(*, vertex_index=0, displacement=(0.0, 0.0, 0.0))

      Free evaluated state of crazyspace

      :arg vertex_index: vertex_index
      :type vertex_index: int in [-inf, inf], (optional)
      :arg displacement: displacement
      :type displacement: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
      :return: displacement_original
      :rtype: :class:`mathutils.Vector` of 3 items in [-inf, inf]

   .. method:: crazyspace_eval_clear()

      crazyspace_eval_clear


   .. method:: to_mesh(*, preserve_all_data_layers=False, depsgraph=None)

      Create a Mesh data-block from the current state of the object. The object owns the data-block. To force free it use to_mesh_clear(). The result is temporary and cannot be used by objects from the main database.

      :arg preserve_all_data_layers: Preserve all data layers in the mesh, like UV maps and vertex groups. By default Blender only computes the subset of data layers needed for viewport display and rendering, for better performance.
      :type preserve_all_data_layers: boolean, (optional)
      :arg depsgraph: Dependency Graph, Evaluated dependency graph which is required when preserve_all_data_layers is true
      :type depsgraph: :class:`Depsgraph`, (optional)
      :return: Mesh created from object
      :rtype: :class:`Mesh`

   .. method:: to_mesh_clear()

      Clears mesh data-block created by to_mesh()


   .. method:: to_curve(depsgraph, *, apply_modifiers=False)

      Create a Curve data-block from the current state of the object. This only works for curve and text objects. The object owns the data-block. To force free it, use to_curve_clear(). The result is temporary and cannot be used by objects from the main database.

      :arg depsgraph: Dependency Graph, Evaluated dependency graph
      :type depsgraph: :class:`Depsgraph`
      :arg apply_modifiers: Apply the deform modifiers on the control points of the curve. This is only supported for curve objects.
      :type apply_modifiers: boolean, (optional)
      :return: Curve created from object
      :rtype: :class:`Curve`

   .. method:: to_curve_clear()

      Clears curve data-block created by to_curve()


   .. method:: find_armature()

      Find armature influencing this object as a parent or via a modifier

      :return: Armature object influencing this object or nullptr
      :rtype: :class:`Object`

   .. method:: shape_key_add(*, name="Key", from_mix=True)

      Add shape key to this object

      :arg name: Unique name for the new keyblock
      :type name: string, (optional, never None)
      :arg from_mix: Create new shape from existing mix of shapes
      :type from_mix: boolean, (optional)
      :return: New shape keyblock
      :rtype: :class:`ShapeKey`

   .. method:: shape_key_remove(key)

      Remove a Shape Key from this object

      :arg key: Keyblock to be removed
      :type key: :class:`ShapeKey`, (never None)

   .. method:: shape_key_clear()

      Remove all Shape Keys from this object


   .. method:: ray_cast(origin, direction, *, distance=1.70141e+38, depsgraph=None)

      Cast a ray onto evaluated geometry, in object space (using context's or provided depsgraph to get evaluated mesh if needed)

      :arg origin: Origin of the ray, in object space
      :type origin: :class:`mathutils.Vector` of 3 items in [-inf, inf]
      :arg direction: Direction of the ray, in object space
      :type direction: :class:`mathutils.Vector` of 3 items in [-inf, inf]
      :arg distance: Maximum distance
      :type distance: float in [0, inf], (optional)
      :arg depsgraph: Depsgraph to use to get evaluated data, when called from original object (only needed if current Context's depsgraph is not suitable)
      :type depsgraph: :class:`Depsgraph`, (optional)
      :return:
         `result`, Whether the ray successfully hit the geometry, boolean

         `location`, The hit location of this ray cast, :class:`mathutils.Vector` of 3 items in [-inf, inf]

         `normal`, The face normal at the ray cast hit location, :class:`mathutils.Vector` of 3 items in [-inf, inf]

         `index`, The face index, -1 when original data isn't available, int in [-inf, inf]

      :rtype: (boolean, :class:`mathutils.Vector` of 3 items in [-inf, inf], :class:`mathutils.Vector` of 3 items in [-inf, inf], int in [-inf, inf])

   .. method:: closest_point_on_mesh(origin, *, distance=1.84467e+19, depsgraph=None)

      Find the nearest point on evaluated geometry, in object space (using context's or provided depsgraph to get evaluated mesh if needed)

      :arg origin: Point to find closest geometry from (in object space)
      :type origin: :class:`mathutils.Vector` of 3 items in [-inf, inf]
      :arg distance: Maximum distance
      :type distance: float in [0, inf], (optional)
      :arg depsgraph: Depsgraph to use to get evaluated data, when called from original object (only needed if current Context's depsgraph is not suitable)
      :type depsgraph: :class:`Depsgraph`, (optional)
      :return:
         `result`, Whether closest point on geometry was found, boolean

         `location`, The location on the object closest to the point, :class:`mathutils.Vector` of 3 items in [-inf, inf]

         `normal`, The face normal at the closest point, :class:`mathutils.Vector` of 3 items in [-inf, inf]

         `index`, The face index, -1 when original data isn't available, int in [-inf, inf]

      :rtype: (boolean, :class:`mathutils.Vector` of 3 items in [-inf, inf], :class:`mathutils.Vector` of 3 items in [-inf, inf], int in [-inf, inf])

   .. method:: is_modified(scene, settings)

      Determine if this object is modified from the base mesh data

      :arg scene: Scene in which to check the object
      :type scene: :class:`Scene`, (never None)
      :arg settings: Modifier settings to apply

         * ``PREVIEW``
           Preview -- Apply modifier preview settings.
         * ``RENDER``
           Render -- Apply modifier render settings.
      :type settings: enum in [``'PREVIEW'``, ``'RENDER'``]
      :return: Whether the object is modified
      :rtype: boolean

   .. method:: is_deform_modified(scene, settings)

      Determine if this object is modified by a deformation from the base mesh data

      :arg scene: Scene in which to check the object
      :type scene: :class:`Scene`, (never None)
      :arg settings: Modifier settings to apply

         * ``PREVIEW``
           Preview -- Apply modifier preview settings.
         * ``RENDER``
           Render -- Apply modifier render settings.
      :type settings: enum in [``'PREVIEW'``, ``'RENDER'``]
      :return: Whether the object is deform-modified
      :rtype: boolean

   .. method:: update_from_editmode()

      Load the objects edit-mode data into the object data

      :return: Success
      :rtype: boolean

   .. method:: cache_release()

      Release memory used by caches associated with this object. Intended to be used by render engines only.


   .. method:: evaluated_geometry()

      Get the evaluated geometry set of this evaluated object. This only works for
      objects that contain geometry data like meshes and curves but not e.g. cameras.
      
      :return: The evaluated geometry.
      :rtype: :class:`bpy.types.GeometrySet`

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

   * :mod:`bpy.context.active_object`
   * :mod:`bpy.context.edit_object`
   * :mod:`bpy.context.editable_objects`
   * :mod:`bpy.context.image_paint_object`
   * :mod:`bpy.context.object`
   * :mod:`bpy.context.objects_in_mode`
   * :mod:`bpy.context.objects_in_mode_unique_data`
   * :mod:`bpy.context.particle_edit_object`
   * :mod:`bpy.context.pose_object`
   * :mod:`bpy.context.sculpt_object`
   * :mod:`bpy.context.selectable_objects`
   * :mod:`bpy.context.selected_editable_objects`
   * :mod:`bpy.context.selected_objects`
   * :mod:`bpy.context.vertex_paint_object`
   * :mod:`bpy.context.visible_objects`
   * :mod:`bpy.context.weight_paint_object`
   * :class:`Action.flip_with_pose`
   * :class:`ActionConstraint.target`
   * :class:`ArmatureModifier.object`
   * :class:`ArrayModifier.curve`
   * :class:`ArrayModifier.end_cap`
   * :class:`ArrayModifier.offset_object`
   * :class:`ArrayModifier.start_cap`
   * :class:`BlendData.objects`
   * :class:`BlendDataMeshes.new_from_object`
   * :class:`BlendDataObjects.new`
   * :class:`BlendDataObjects.remove`
   * :class:`BoidRuleAvoid.object`
   * :class:`BoidRuleFollowLeader.object`
   * :class:`BoidRuleGoal.object`
   * :class:`BooleanModifier.object`
   * :class:`CameraDOFSettings.focus_object`
   * :class:`CastModifier.object`
   * :class:`ChildOfConstraint.target`
   * :class:`ClampToConstraint.target`
   * :class:`Collection.all_objects`
   * :class:`Collection.objects`
   * :class:`CollectionObjects.link`
   * :class:`CollectionObjects.unlink`
   * :class:`Constraint.space_object`
   * :class:`ConstraintTarget.target`
   * :class:`ConstraintTargetBone.target`
   * :class:`CopyLocationConstraint.target`
   * :class:`CopyRotationConstraint.target`
   * :class:`CopyScaleConstraint.target`
   * :class:`CopyTransformsConstraint.target`
   * :class:`Curve.bevel_object`
   * :class:`Curve.taper_object`
   * :class:`CurveModifier.object`
   * :class:`Curves.surface`
   * :class:`CyclesRenderSettings.dicing_camera`
   * :class:`DampedTrackConstraint.target`
   * :class:`DataTransferModifier.object`
   * :class:`Depsgraph.objects`
   * :class:`DepsgraphObjectInstance.instance_object`
   * :class:`DepsgraphObjectInstance.object`
   * :class:`DepsgraphObjectInstance.parent`
   * :class:`DisplaceModifier.texture_coords_object`
   * :class:`DynamicPaintSurface.output_exists`
   * :class:`FieldSettings.source_object`
   * :class:`FloorConstraint.target`
   * :class:`FluidDomainSettings.guide_parent`
   * :class:`FollowPathConstraint.target`
   * :class:`FollowTrackConstraint.camera`
   * :class:`FollowTrackConstraint.depth_object`
   * :class:`GPencilSculptGuide.reference_object`
   * :class:`GeometryNodeInputObject.object`
   * :class:`GreasePencilArmatureModifier.object`
   * :class:`GreasePencilArrayModifier.offset_object`
   * :class:`GreasePencilBuildModifier.object`
   * :class:`GreasePencilHookModifier.object`
   * :class:`GreasePencilLatticeModifier.object`
   * :class:`GreasePencilLayer.parent`
   * :class:`GreasePencilLineartModifier.light_contour_object`
   * :class:`GreasePencilLineartModifier.source_camera`
   * :class:`GreasePencilLineartModifier.source_object`
   * :class:`GreasePencilMirrorModifier.object`
   * :class:`GreasePencilOutlineModifier.object`
   * :class:`GreasePencilShrinkwrapModifier.auxiliary_target`
   * :class:`GreasePencilShrinkwrapModifier.target`
   * :class:`GreasePencilTintModifier.object`
   * :class:`GreasePencilWeightProximityModifier.object`
   * :class:`HookModifier.object`
   * :class:`KinematicConstraint.pole_target`
   * :class:`KinematicConstraint.target`
   * :class:`LatticeModifier.object`
   * :class:`LayerObjects.active`
   * :class:`LayerObjects.selected`
   * :class:`LimitDistanceConstraint.target`
   * :class:`LineStyleAlphaModifier_DistanceFromObject.target`
   * :class:`LineStyleColorModifier_DistanceFromObject.target`
   * :class:`LineStyleThicknessModifier_DistanceFromObject.target`
   * :class:`LockedTrackConstraint.target`
   * :class:`MaskModifier.armature`
   * :class:`MeshDeformModifier.object`
   * :class:`MeshToVolumeModifier.object`
   * :class:`MirrorModifier.mirror_object`
   * :class:`NodeSocketObject.default_value`
   * :class:`NodeTreeInterfaceSocketObject.default_value`
   * :class:`NormalEditModifier.target`
   * :class:`Object.find_armature`
   * :class:`Object.parent`
   * :class:`ObjectBase.object`
   * :class:`ObjectSolverConstraint.camera`
   * :class:`ParticleEdit.object`
   * :class:`ParticleEdit.shape_object`
   * :class:`ParticleHairKey.co_object`
   * :class:`ParticleHairKey.co_object_set`
   * :class:`ParticleInstanceModifier.object`
   * :class:`ParticleSettings.instance_object`
   * :class:`ParticleSettingsTextureSlot.object`
   * :class:`ParticleSystem.co_hair`
   * :class:`ParticleSystem.parent`
   * :class:`ParticleSystem.reactor_target_object`
   * :class:`ParticleTarget.object`
   * :class:`PivotConstraint.target`
   * :class:`PoseBone.custom_shape`
   * :class:`RenderEngine.bake`
   * :class:`RenderEngine.camera_model_matrix`
   * :class:`RenderEngine.camera_override`
   * :class:`RenderEngine.camera_shift_x`
   * :class:`RenderEngine.use_spherical_stereo`
   * :class:`RigidBodyConstraint.object1`
   * :class:`RigidBodyConstraint.object2`
   * :class:`RigidBodyWorld.convex_sweep_test`
   * :class:`BakeSettings.cage_object`
   * :class:`Scene.camera`
   * :class:`Scene.objects`
   * :class:`Scene.ray_cast`
   * :class:`Scene.uvedit_aspect`
   * :class:`SceneStrip.scene_camera`
   * :class:`ScrewModifier.object`
   * :class:`Sculpt.gravity_object`
   * :class:`ShaderFxShadow.object`
   * :class:`ShaderFxSwirl.object`
   * :class:`ShaderNodeTexCoord.object`
   * :class:`ShaderNodeTexPointDensity.object`
   * :class:`ShrinkwrapConstraint.target`
   * :class:`ShrinkwrapModifier.auxiliary_target`
   * :class:`ShrinkwrapModifier.target`
   * :class:`SimpleDeformModifier.origin`
   * :class:`SpaceView3D.camera`
   * :class:`SpaceView3D.lock_object`
   * :class:`SplineIKConstraint.target`
   * :class:`StretchToConstraint.target`
   * :class:`SurfaceDeformModifier.target`
   * :class:`TextCurve.follow_curve`
   * :class:`TimelineMarker.camera`
   * :class:`TrackToConstraint.target`
   * :class:`TransformConstraint.target`
   * :class:`UVProjector.object`
   * :class:`UVWarpModifier.object_from`
   * :class:`UVWarpModifier.object_to`
   * :class:`VertexWeightEditModifier.mask_tex_map_object`
   * :class:`VertexWeightMixModifier.mask_tex_map_object`
   * :class:`VertexWeightProximityModifier.mask_tex_map_object`
   * :class:`VertexWeightProximityModifier.target`
   * :class:`ViewLayer.objects`
   * :class:`VolumeDisplaceModifier.texture_map_object`
   * :class:`VolumeToMeshModifier.object`
   * :class:`WarpModifier.object_from`
   * :class:`WarpModifier.object_to`
   * :class:`WarpModifier.texture_coords_object`
   * :class:`WaveModifier.start_position_object`
   * :class:`WaveModifier.texture_coords_object`
   * :class:`XrSessionSettings.base_pose_object`

