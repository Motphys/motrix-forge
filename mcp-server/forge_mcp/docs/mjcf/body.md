# body

**Path**: `body`
**Tag**: `body`
**Parent**: `mujoco`
**Children**: `body/inertial`, `body/joint`, `body/freejoint`, `body`, `body/attach`, `body/camera`, `body/frame`, `body/geom`, `body/gsplat`, `body/light`, `body/replicate`, `body/site`
**Rust Type**: `model::body::Body`

This element is used to construct the kinematic tree via nesting. The element worldbody is used
 for the top-level body, while the element body is used for all other bodies.

 Bodies form the nodes of the kinematic tree. Each body can have child bodies, joints, geoms,
 sites, cameras, and lights. The inertial properties of a body can be specified explicitly via
 the inertial child element, or inferred automatically from the geoms attached to the body.

## Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the body. |
| `childclass` | `string` | no | — | If this attribute is present, all descendant elements that admit a defaults class will use  the class specified here, unless they specify their own class or another body or frame with  a childclass attribute is encountered along the chain of nested bodies and frames. |
| `pos` | `real(3)` | no | — | The 3D position of the body frame, in the parent coordinate frame. If undefined it defaults  to (0,0,0). |
| `quat` | `real(4)` | no | — | Orientation of the body frame as unit quaternion.  → See [rotation representation](#rotation-attrs-quat). |
| `euler` | `real(3)` | no | — | Orientation of the body frame as Euler angles.  → See [rotation representation](#rotation-attrs-euler). |
| `axisangle` | `real(4)` | no | — | Orientation of the body frame as an axis-angle pair.  → See [rotation representation](#rotation-attrs-axisangle). |
| `xyaxes` | `real(6)` | no | — | Orientation of the body frame via X and Y axes.  → See [rotation representation](#rotation-attrs-xyaxes). |
| `zaxis` | `real(3)` | no | — | Orientation of the body frame via Z axis direction.  → See [rotation representation](#rotation-attrs-zaxis). |
| `mocap` | `bool` | yes | `false` | If this attribute is \"true\", the body is labeled as a mocap body. This is allowed only for  bodies that are children of the world body and have no joints. Such bodies are fixed from  the viewpoint of the dynamics, but nevertheless the forward kinematics set their position  and orientation via the mocap system at each time step. This mechanism  can be used to stream motion capture data into the simulation. Mocap bodies can also be  moved via mouse perturbations in the interactive visualizer, even in dynamic simulation  mode, which can be useful for creating props with adjustable position and orientation. |
| `gravcomp` | `real` | yes | `0.0` | Gravity compensation force, specified as fraction of body weight. This attribute creates an  upwards force applied to the body's center of mass, countering the force of gravity. A  value of 1 creates an upward force equal to the body's weight and compensates for gravity  exactly. Values greater than 1 will create a net upwards force or buoyancy effect. |

## body/inertial

**Path**: `body/inertial`
**Tag**: `inertial`
**Parent**: `body`
**Children**: none
**Rust Type**: `model::body::inertial::Inertia`

This element specifies the mass and inertial properties of the body. If this element is not
 included in a given body, the inertial properties are inferred from the geoms attached to the
 body. When a compiled MJCF model is saved, the XML writer saves the inertial properties
 explicitly using this element, even if they were inferred from geoms. The inertial frame is
 such that its center coincides with the center of mass of the body, and its axes coincide with
 the principal axes of inertia of the body. Thus the inertia matrix is diagonal in this frame.

Note

 The presence of the `inertial` element itself disables the automatic inertia inference
 mechanism from geoms. Even when inertial properties could be inferred from geoms, `pos` is
 required whenever this element is present.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `pos` | `real(3)` | yes | `""` | Position of the inertial frame. This attribute is required even when the inertial  properties can be inferred from geoms. This is because the presence of the inertial  element itself disables the automatic inference mechanism. |
| `quat` | `real(4)` | no | — | Orientation of the inertial frame as unit quaternion.  → See [rotation representation](#rotation-attrs-quat). |
| `euler` | `real(3)` | no | — | Orientation of the inertial frame as Euler angles.  → See [rotation representation](#rotation-attrs-euler). |
| `axisangle` | `real(4)` | no | — | Orientation of the inertial frame as an axis-angle pair.  → See [rotation representation](#rotation-attrs-axisangle). |
| `xyaxes` | `real(6)` | no | — | Orientation of the inertial frame via X and Y axes.  → See [rotation representation](#rotation-attrs-xyaxes). |
| `zaxis` | `real(3)` | no | — | Orientation of the inertial frame via Z axis direction.  → See [rotation representation](#rotation-attrs-zaxis). |
| `mass` | `real` | yes | `0.0` | Mass of the body. Negative values are not allowed. The inertia matrix in generalized  coordinates must be positive-definite, which can sometimes be achieved even if some bodies  have zero mass. In general however there is no reason to use massless bodies. |
| `diaginertia` | `real(3)` | no | — | Diagonal inertia matrix, expressing the body inertia relative to the inertial frame. If  this attribute is omitted, the `fullinertia` attribute becomes required. |
| `fullinertia` | `real(6)` | no | — | Full inertia matrix M. Since M is 3-by-3 and symmetric, it is specified using only 6  numbers in the following order: M(1,1), M(2,2), M(3,3), M(1,2), M(1,3), M(2,3). The  compiler computes the eigenvalue decomposition of M and sets the frame orientation and  diagonal inertia accordingly. If non-positive eigenvalues are encountered (i.e., if M is  not positive definite) a compile error is generated. |

## body/joint

**Path**: `body/joint`
**Tag**: `joint`
**Parent**: `body`
**Children**: none
**Rust Type**: `model::body::joint::Joint`

This element creates a joint. A joint creates motion degrees of freedom between the body where
 it is defined and the body's parent. If multiple joints are defined in the same body, the
 corresponding spatial transformations (of the body frame relative to the parent frame) are
 applied in order. If no joints are defined, the body is welded to its parent. Joints cannot be
 defined in the world body. At runtime the positions and orientations of all joints defined in
 the model are stored in the DOF positions array, in the order in which they appear in the
 kinematic tree. The linear and angular velocities are stored in the DOF velocities array. These
 two vectors have different dimensionality when free or ball joints are used, because such joints
 represent rotations as unit quaternions.

Note

 Free joints do not have a position within the body frame and cannot have limits. Ball joints
 cannot be combined with other rotational joints in the same body. The axis attribute is ignored
 for free and ball joints.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the joint. |
| `class` | `string` | no | — | Defaults class for setting unspecified attributes. |
| `group` | `int` | yes | `0` |  |
| `type` | `string` | yes | `"hinge"` | Type of the joint. The keywords have the following meaning: the free type creates a free  \"joint\" with three translational and three rotational degrees of freedom making the body  floating; the ball type creates a ball joint with three rotational degrees of freedom; the  slide type creates a sliding or prismatic joint with one translational degree of freedom;  the hinge type creates a hinge joint with one rotational degree of freedom. Choice: `free`, `ball`, `slide`, `hinge`. |
| `axis` | `real(3)` | yes | `"0.0 0.0 1.0"` | This attribute specifies the axis of rotation for hinge joints and the direction of  translation for slide joints. It is ignored for free and ball joints. The vector specified  here is automatically normalized to unit length as long as its length is greater than  10E-14; otherwise a compile error is generated. |
| `pos` | `real(3)` | yes | `"0.0 0.0 0.0"` | Position of the joint, specified in the frame of the body where the joint is defined. For  free joints this attribute is ignored. |
| `ref` | `real` | yes | `0.0` | The reference position or angle of the joint. This attribute is only used for slide and  hinge joints. It defines the joint value corresponding to the initial model configuration.  Note that the initial configuration itself is unmodified, only the value of the joint at  this configuration. The amount of spatial transformation that the joint applies at runtime  equals the current joint value stored in the DOF positions minus this reference value. |
| `margin` | `real` | yes | `0.0` | The distance threshold below which limits become active. The constraint solver normally  generates forces as soon as a constraint becomes active, even if the margin parameter makes  that happen at a distance. This attribute together with solreflimit and solimplimit can be  used to model a soft joint limit. |
| `range` | `real(2)` | no | — | The joint limits. Limits can be imposed on all joint types except for free joints. For  hinge and ball joints, the range is specified in degrees or radians depending on the angle  attribute of the compiler element. For ball joints, the limit is imposed on the angle of  rotation (relative to the reference configuration) regardless of the axis of rotation. Only  the second range parameter is used for ball joints; the first range parameter should be set  to 0. Setting this attribute without specifying limited is an error if autolimits is  \"false\" in the compiler element. |
| `limited` | `string` | yes | `"auto"` | This attribute specifies if the joint has limits. It interacts with the range attribute. If  this attribute is \"false\", joint limits are disabled. If this attribute is \"true\", joint  limits are enabled. If this attribute is \"auto\", and autolimits is set in the compiler  element, joint limits will be enabled if range is defined. Choice: `false`, `true`, `auto`. |
| `actuatorfrcrange` | `real(2)` | no | — | Range for clamping total actuator forces acting on this joint. It is available only for  scalar joints (hinge and slider) and ignored for ball and free joints. The compiler expects  the first value to be smaller than the second value. Setting this attribute without  specifying actuatorfrclimited is an error if compiler-autolimits is \"false\". |
| `actuatorfrclimited` | `string` | yes | `"auto"` | This attribute specifies whether actuator forces acting on the joint should be clamped. It  is available only for scalar joints (hinge and slider) and ignored for ball and free  joints. This attribute interacts with the actuatorfrcrange attribute. If this attribute  is \"false\", actuator force clamping is disabled. If it is \"true\", actuator force  clamping is enabled. If this attribute is \"auto\", and autolimits is set in the compiler  element, actuator force clamping will be enabled if actuatorfrcrange is defined. Choice: `false`, `true`, `auto`. |
| `springdamper` | `real(2)` | no | — | When both numbers are positive, the compiler will override any stiffness and damping values  specified with the attributes below, and will instead set them automatically so that the  resulting mass-spring-damper for this joint has the desired time constant (first value) and  damping ratio (second value). This is done by taking into account the joint inertia in the  model reference configuration. Note that the format is the same as the solref parameter of  the constraint solver. |
| `solreflimit` | `real(n)` | no | — | Solver reference parameters for joint limits.  → See [solver parameters](#solver-attrs-solref). |
| `solimplimit` | `real(5)` | yes | `"0.9 0.95 0.001 0.5 2.0"` | Solver impedance parameters for joint limits.  → See [solver parameters](#solver-attrs-solimp). |
| `stiffness` | `real` | no | — | Joint stiffness. If this value is positive, a spring will be created with equilibrium  position given by springref. The spring force is computed along with the other passive  forces. |
| `springref` | `real` | yes | `0.0` | The joint position or angle in which the joint spring (if any) achieves equilibrium. All  spring reference values specified with this attribute are collected into the spring  reference configuration, which is also used to compute the spring reference lengths of  all tendons. |
| `armature` | `real` | yes | `0.0` | Additional inertia associated with movement of the joint that is not due to body mass. This  added inertia is usually due to a rotor (a.k.a armature) spinning faster than the joint  itself due to a geared transmission. Because the gear ratio appears twice, multiplying both  forces and lengths, the effect is known as \"reflected inertia\" and the equivalent value is  the inertia of the spinning body multiplied by the square of the gear ratio. The value  applies to all degrees of freedom created by this joint. Besides increasing the realism of  joints with geared transmission, positive armature significantly improves simulation  stability, even for small values, and is a recommended possible fix when encountering  stability issues. |
| `damping` | `real` | no | — | Damping applied to all degrees of freedom created by this joint. Unlike friction loss which  is computed by the constraint solver, damping is simply a force linear in velocity. It is  included in the passive forces. Despite this simplicity, larger damping values can make  numerical integrators unstable, which is why the Euler integrator handles damping  implicitly. |
| `frictionloss` | `real` | yes | `0.0` | Friction loss due to dry friction. This value is the same for all degrees of freedom  created by this joint. Semantically friction loss does not make sense for free joints, but  the compiler allows it. To enable friction loss, set this attribute to a positive value. |
| `solreffriction` | `real(2)` | yes | `"0.02 1.0"` |  |
| `solimpfriction` | `real(5)` | yes | `"0.9 0.95 0.001 0.5 2.0"` |  |
| `hardlimit` | `bool` | no | — | [MPEX] If true, the limit constraint is hard. |

## body/freejoint

**Path**: `body/freejoint`
**Tag**: `freejoint`
**Parent**: `body`
**Children**: none
**Rust Type**: `model::body::joint::FreeJoint`

This element creates a free joint whose only attributes are name and group. The freejoint
 element is an XML shortcut for:

 ```xml
 <joint type="free" stiffness="0" damping="0" frictionloss="0" armature="0"/>
 ```

 While this joint can evidently be created with the joint element, default joint settings
 could affect it. This is usually undesirable as physical free bodies do not have nonzero
 stiffness, damping, friction or armature. To avoid this complication, the freejoint element
 was introduced, ensuring joint defaults are not inherited. If the XML model is saved, it will
 appear as a regular joint of type free.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the joint. |
| `group` | `int` | no | — | Integer group to which the joint belongs. This attribute can be used for custom tags. It is  also used by the visualizer to enable and disable the rendering of entire groups of joints. |

## body/attach

**Path**: `body/attach`
**Tag**: `attach`
**Parent**: `body`
**Children**: none
**Rust Type**: `model::attach::Attach`

The `attach` element is used to attach an external MJCF model's body subtree
 to the current body. This is useful for modular model composition.

 Unlike `include` which merges the entire external model at the root level,
 `attach` inserts a specific body's children into the current body hierarchy.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `model` | `string` | yes | `""""` | The model defined in asset element. |
| `body` | `string` | no | — | Name of the body in the sub-model to attach here.  `None` means attaching the whole world body. |
| `prefix` | `string` | yes | `""""` | Prefix to prepend to all names in the sub-model. (e.g. bodys, joints, actuators, meshes...)  Empty string (\"\") is allowed, but be careful of naming collisions. |

## body/camera

**Path**: `body/camera`
**Tag**: `camera`
**Parent**: `body`
**Children**: none
**Rust Type**: `model::body::camera::Camera`

This element creates a camera, which moves with the body where it is defined. To create a fixed
 camera, define it in the world body. The cameras created here are in addition to the default
 free camera which is always defined and is adjusted via the visual element. The cameras have
 a viewpoint that is always centered in front of the projection surface. The viewpoint coincides
 with the center of the camera frame. The camera is looking along the -Z axis of its frame.
 The +X axis points to the right, and the +Y axis points up. Thus the frame position and
 orientation are the key adjustments that need to be made here.

Note

 The `xyaxes` orientation attribute is semantically convenient for cameras, as the X and Y axes
 correspond to the directions \"right\" and \"up\" in pixel space, respectively.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the camera. |
| `class` | `string` | no | — | Defaults class for setting unspecified attributes. |
| `mode` | `string` | yes | `"fixed"` | This attribute specifies how the camera position and orientation in world coordinates are  computed in forward kinematics (which in turn determine what the camera sees). \"fixed\"  means that the position and orientation specified below are fixed relative to the body  where the camera is defined. \"track\" means that the camera position is at a constant  offset from the body in world coordinates, while the camera orientation is constant in  world coordinates. These constants are determined by applying forward kinematics in  qpos0 and treating the camera as fixed. Tracking can be used for example to position a  camera above a body, point it down so it sees the body, and have it always remain above  the body no matter how the body translates and rotates. \"trackcom\" is similar to  \"track\" but the constant spatial offset is defined relative to the center of mass of  the kinematic subtree starting at the body in which the camera is defined. This can be  used to keep an entire mechanism in view. Note that the subtree center of mass for the  world body is the center of mass of the entire model. So if a camera is defined in the  world body in mode \"trackcom\", it will track the entire model. \"targetbody\" means that  the camera position is fixed in the body frame, while the camera orientation is  adjusted so that it always points towards the targeted body (which is specified with  the target attribute below). This can be used for example to model an eye that fixates  a moving object; the object will be the target, and the camera/eye will be defined in  the body corresponding to the head. \"targetbodycom\" is the same as \"targetbody\" but the  camera is oriented towards the center of mass of the subtree starting at the target  body. Choice: `fixed`, `track`, `trackcom`, `targetbody`, `targetbodycom`. |
| `target` | `string` | no | — | When the camera mode is \"targetbody\" or \"targetbodycom\", this attribute becomes required.  It specifies which body should be targeted by the camera. In all other modes this  attribute is ignored. |
| `orthographic` | `bool` | yes | `false` | Whether the camera uses a perspective (the default) or orthographic projection. Setting  this attribute to orthographic changes the semantic of the fovy attribute. |
| `fovy` | `real` | yes | `45.0` | Vertical field-of-view of the camera. If the camera uses a perspective projection, the  field-of-view is expressed in degrees, regardless of the global compiler/angle setting. If  the camera uses an orthographic projection, the field-of-view is expressed in units of  length; note that in this case the default of 45 is too large for most scenes and should  likely be reduced. In either case, the horizontal field of view is computed automatically  given the window size and the vertical field of view. |
| `pos` | `real(3)` | yes | `"0.0 0.0 0.0"` | Position of the camera frame. |
| `quat` | `real(4)` | no | — | Orientation of the camera frame as unit quaternion.  → See [rotation representation](#rotation-attrs-quat). |
| `euler` | `real(3)` | no | — | Orientation of the camera frame as Euler angles.  → See [rotation representation](#rotation-attrs-euler). |
| `axisangle` | `real(4)` | no | — | Orientation of the camera frame as an axis-angle pair.  → See [rotation representation](#rotation-attrs-axisangle). |
| `xyaxes` | `real(6)` | no | — | Orientation of the camera frame via X and Y axes. Semantically convenient for cameras:  X and Y correspond to \"right\" and \"up\" in pixel space, respectively.  → See [rotation representation](#rotation-attrs-xyaxes). |
| `zaxis` | `real(3)` | no | — | Orientation of the camera frame via Z axis direction.  → See [rotation representation](#rotation-attrs-zaxis). |
| `resolution` | `real(2)` | yes | `"1 1"` |  |
| `trackposspeed` | `real` | yes | `0.0` | [MPEX] Motphys-only extension. When not zero, the camera will move to target pose with this speed. |
| `trackrotspeed` | `real` | yes | `0.0` | [MPEX] Motphys-only extension. When not zero, the camera will rotate to target pose with this  speed. |
| `depth` | `bool` | yes | `false` | [MPEX] Motphys-only extension. When enabled, the camera renders depth information only. |
| `znear` | `real` | yes | `0.0` | [MPEX] Motphys-only extension. The near clipping plane distance. If not specified, it will be  automatically computed. |
| `zfar` | `real` | yes | `0.0` | [MPEX] Motphys-only extension. The far clipping plane distance. If not specified, it will be  automatically computed. |

## body/frame

**Path**: `body/frame`
**Tag**: `frame`
**Parent**: `body`
**Children**: none
**Rust Type**: `model::meta::Frame`

This element introduces a local coordinate frame without making it a distinct physical body.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the frame. |
| `childclass` | `string` | no | — | Child class for setting unspecified attributes. |
| `pos` | `real(3)` | yes | `"0.0 0.0 0.0"` | Position of the frame. |
| `quat` | `real(4)` | no | — | Orientation of the frame as quaternion. |
| `euler` | `real(3)` | no | — | Orientation of the frame as euler angles. |
| `axisangle` | `real(4)` | no | — | Orientation of the frame as axis-angle. |
| `xyaxes` | `real(6)` | no | — | Orientation of the frame as xy-axes. |
| `zaxis` | `real(3)` | no | — | Orientation of the frame as z-axis. |

## body/geom

**Path**: `body/geom`
**Tag**: `geom`
**Parent**: `body`
**Children**: none
**Rust Type**: `model::body::geom::Geom`

A geometric element attached rigidly to the body within which it is defined.

 Multiple geoms can be attached to the same body. At runtime they determine the appearance
 and collision properties of the body. At compile time they can also determine the inertial
 properties of the body, depending on the presence of the `inertial` element and the setting
 of the `inertiafromgeom` attribute of `compiler`. Inertial properties are computed by summing
 the masses and inertias of all geoms attached to the body whose geom group falls within the
 range specified by the `inertiagrouprange` attribute of `compiler`. The geom masses and
 inertias are computed using the geom shape, a specified density or a geom mass which implies
 a density, and the assumption of uniform density.

 Geoms are not strictly required for physics simulation. One can create and simulate a model
 that only has bodies and joints — such a model can even be visualized using equivalent inertia
 boxes to represent bodies, with only contact forces missing.

Note

 The following MJCF attributes are not currently supported:
 - `shellinertia`: Treat geom as a thin shell for inertia computation
 - `fitscale`: Scale factor for auto-fitting mesh geoms
 - `fluidshape`: Enable fluid interaction with ellipsoid shape
 - `fluidcoef`: Fluid interaction coefficients
 - `user`: User data array

 The following motrixsim-specific attribute is available:
 - `hard`: Enable hard contact mode

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the geom. |
| `class` | `string` | no | — | Defaults class for setting unspecified attributes. |
| `type` | `string` | yes | `"sphere"` | Type of geometric shape. The keywords have the following meaning: the plane type defines  a plane which is infinite for collision detection purposes; it can only be attached to the  world body or static children of the world. The sphere type defines a sphere centered at  the geom's position, using one size parameter for the radius. The capsule type defines a  capsule — a cylinder capped with two half-spheres — oriented along the Z axis of the  geom's frame. The cylinder type defines a right circular cylinder oriented along the Z  axis of the geom's frame. The box type defines a box whose half-sizes along X, Y and Z  are given by the three size parameters. The mesh type defines a mesh referenced by the  mesh attribute. The hfield type defines a height field referenced by the hfield  attribute. Choice: `plane`, `hfield`, `sphere`, `capsule`, `cylinder`, `box`, `ellipsoid`, `mesh`, `sdf`. |
| `contype` | `int` | yes | `1` | This attribute and the next specify 32-bit integer bitmasks used for contact filtering of  dynamically generated contact pairs. Two geoms can collide if the contype of one geom is  compatible with the conaffinity of the other geom or vice versa. Compatible means that the  two bitmasks have a common bit set to 1. |
| `condim` | `int` | yes | `3` | The dimensionality of the contact space for a dynamically generated contact pair is set to  the maximum of the condim values of the two participating geoms. The allowed values and  their meaning are: 1 for frictionless contact; 3 for regular frictional contact opposing  slip in the tangent plane; 4 for frictional contact opposing slip in the tangent plane and  rotation around the contact normal, useful for modeling soft contacts; 6 for frictional  contact opposing slip in the tangent plane, rotation around the contact normal, and  rotation around the two axes of the tangent plane, the latter being useful for preventing  objects from rolling indefinitely. |
| `conaffinity` | `int` | yes | `1` | Bitmask for contact filtering; see contype above. |
| `mesh` | `string` | no | — | If the geom type is \"mesh\", this attribute is required and references the mesh asset to be  instantiated. This attribute can also be specified if the geom type corresponds to a  geometric primitive such as sphere, capsule, cylinder, ellipsoid, or box, in which case  the primitive is automatically fitted to the referenced mesh asset. In the compiled model  the geom is represented as a regular geom of the specified primitive type with no  reference to the mesh used for fitting. |
| `group` | `int` | yes | `0` | This attribute specifies an integer group to which the geom belongs. The only effect on  the physics is at compile time, when body masses and inertias are inferred from geoms  selected based on their group via the `inertiagrouprange` attribute of `compiler`. At  runtime this attribute is used by the visualizer to enable and disable the rendering of  entire geom groups. By default, groups 0, 1 and 2 are visible while all other groups are  invisible. The group attribute can also be used as a tag for custom computations. |
| `size` | `real(n)` | no | — | Geom size parameters. The number of required parameters and their meaning depends on the  geom type as documented under the type attribute. All required size parameters must be  positive. Note that when a non-mesh geom type references a mesh, a geometric primitive of  that type is fitted to the mesh and the geom size parameters are ignored. When using the  fromto attribute, only the first size parameter is used (specifying the radius or  half-size perpendicular to the elongation direction). |
| `priority` | `int` | yes | `0` | The geom priority determines how the properties of two colliding geoms are combined to  form the properties of the contact. This interacts with the solmix attribute. When the  priorities of the two geoms differ, the contact parameters of the higher-priority geom  are used. When priorities are equal, the parameters are mixed according to solmix. |
| `material` | `string` | no | — | If specified, this attribute applies a material to the geom. Otherwise, if unspecified  and the type of the geom is a mesh, the compiler will apply the mesh asset material if  present. The material determines the visual properties of the geom. The only exception is  color: if the rgba attribute is different from its internal default, rgba takes precedence  while the remaining material properties are still applied. |
| `rgba` | `real(4)` | yes | `"0.5 0.5 0.5 1.0"` | Instead of creating material assets and referencing them, this attribute can be used to  set color and transparency only. This is not as flexible as the material mechanism, but  is more convenient and is often sufficient. If the value of this attribute is different  from the internal default, it takes precedence over the material. |
| `friction` | `real(n)` | yes | `"1.0 0.005 0.0001"` | Contact friction parameters for dynamically generated contact pairs. The first number is  the sliding friction, acting along both axes of the tangent plane. The second number is  the torsional friction, acting around the contact normal. The third number is the rolling  friction, acting around both axes of the tangent plane. The friction parameters for the  contact pair are combined depending on the solmix and priority attributes. |
| `mass` | `real` | no | — | If this attribute is specified, the density attribute below is ignored and the geom  density is computed from the given mass, using the geom shape and the assumption of  uniform density. The computed density is then used to obtain the geom inertia. The geom  mass and inertia are only used during compilation to infer the body mass and inertia if  necessary; at runtime only the body inertial properties affect the simulation. |
| `density` | `real` | yes | `1000` | Material density used to compute the geom mass and inertia. The computation is based on  the geom shape and the assumption of uniform density. This attribute is used only when  the mass attribute above is unspecified. The density has semantics of mass per unit volume  (unless shellinertia is true, in which case it has semantics of mass per unit area). |
| `margin` | `real` | yes | `0` | Distance threshold below which contacts are detected and included in the global array  the contact data. A contact is considered active only if the distance between the two geom  surfaces is below margin minus gap. Constraint impedance can be a function of distance,  and the quantity this function is applied to is the distance between the two geoms minus  the margin plus the gap. |
| `gap` | `real` | yes | `0` | This attribute is used to enable the generation of inactive contacts, i.e., contacts that  are ignored by the constraint solver but are included in the contact data for the purpose  of custom computations. When this value is positive, geom distances between margin and  margin minus gap correspond to such inactive contacts. |
| `fromto` | `real(6)` | no | — | This attribute can only be used with capsule, box, cylinder and ellipsoid geoms. It  provides an alternative specification of the geom length as well as the frame position  and orientation. The six numbers are the 3D coordinates of one point followed by the 3D  coordinates of another point. The elongated part of the geom connects these two points,  with the +Z axis of the geom's frame oriented from the first towards the second point,  while in the perpendicular direction the geom sizes are both equal to the first value of  the size attribute. The frame position is in the middle between the end points. If this  attribute is specified, the remaining position and orientation-related attributes are  ignored. Note that the fromto semantics of capsule are unique: the two end points specify  the segment around which the radius defines the capsule surface. |
| `pos` | `real(3)` | yes | `"0. 0. 0."` | Position of the geom, specified in the frame of the body where the geom is defined. |
| `quat` | `real(4)` | no | — | Orientation of the geom frame as unit quaternion.  → See [rotation representation](#rotation-attrs-quat). |
| `euler` | `real(3)` | no | — | Orientation of the geom frame as Euler angles.  → See [rotation representation](#rotation-attrs-euler). |
| `axisangle` | `real(4)` | no | — | Orientation of the geom frame as an axis-angle pair.  → See [rotation representation](#rotation-attrs-axisangle). |
| `xyaxes` | `real(6)` | no | — | Orientation of the geom frame via X and Y axes.  → See [rotation representation](#rotation-attrs-xyaxes). |
| `zaxis` | `real(3)` | no | — | Orientation of the geom frame via Z axis direction.  → See [rotation representation](#rotation-attrs-zaxis). |
| `solmix` | `real` | yes | `1.0` | This attribute specifies the weight used for averaging of contact parameters, and  interacts with the priority attribute. When two geoms with equal priority collide, their  contact parameters are mixed using solmix as the weight for one geom and (1 - solmix)  for the other. |
| `solref` | `real(2)` | yes | `"0.02 1.0"` | Solver reference parameters for contact simulation.  → See [solver parameters](#solver-attrs-solref). |
| `solimp` | `real(5)` | yes | `"0.9 0.95 0.001 0.5 2.0"` | Solver impedance parameters for contact simulation.  → See [solver parameters](#solver-attrs-solimp). |
| `hfield` | `string` | no | — | This attribute must be specified if and only if the geom type is \"hfield\". It references  the height field asset to be instantiated at the position and orientation of the geom  frame. |

## body/gsplat [PRO]

**Path**: `body/gsplat`
**Tag**: `gsplat`
**Parent**: `body`
**Children**: none
**Rust Type**: `model::body::gsplat::GaussianSplat`

A Gaussian cloud instance attached to the world or a body.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | [PRO] Optional instance name. |
| `asset` | `string` | yes | `""""` | [PRO] Gaussian cloud asset name. |
| `pos` | `real(3)` | yes | `"0.0 0.0 0.0"` | [PRO] Position of the Gaussian cloud frame. |
| `quat` | `real(4)` | no | — | [PRO] Orientation of the Gaussian cloud frame as unit quaternion. |
| `euler` | `real(3)` | no | — | [PRO] Orientation of the Gaussian cloud frame as Euler angles. |
| `axisangle` | `real(4)` | no | — | [PRO] Orientation of the Gaussian cloud frame as an axis-angle pair. |
| `xyaxes` | `real(6)` | no | — | [PRO] Orientation of the Gaussian cloud frame via X and Y axes. |
| `zaxis` | `real(3)` | no | — | [PRO] Orientation of the Gaussian cloud frame via Z axis direction. |
| `scale` | `real(3)` | yes | `"1.0 1.0 1.0"` | [PRO] Per-axis instance scale. |
| `opacity` | `real` | yes | `1.0` | [PRO] Opacity multiplier. |
| `splatscale` | `real` | yes | `1.0` | [PRO] Gaussian covariance scale multiplier. |
| `group` | `int` | yes | `0` | [PRO] Visibility group. |

## body/light

**Path**: `body/light`
**Tag**: `light`
**Parent**: `body`
**Children**: none
**Rust Type**: `model::body::light::Light`

This element creates a light, which moves with the body where it is defined. To create a fixed
 light, define it in the world body. The lights created here are in addition to the headlight
 which is always defined and is configured via the visual element. Lights shine along the
 direction specified by the dir attribute. They do not have a full spatial frame with three
 orthogonal axes.

 MJCF supports multiple lighting models (e.g. Phong lighting with shadow mapping and
 physically-based rendering). Attributes may be applied or ignored depending on the lighting
 model being used by the renderer.

Note
 To create a fixed light that does not move with any body, define it in the world body.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the light. |
| `class` | `string` | no | — | Defaults class for setting unspecified attributes. |
| `mode` | `string` | yes | `"fixed"` | This attribute specifies how the light position and orientation in world coordinates are  computed in forward kinematics, which in turn determines what the light illuminates.  \"fixed\" means that the position and orientation specified below are fixed relative to the  body where the light is defined. \"track\" means that the light position is at a constant  offset from the body in world coordinates, while the orientation is constant in world  coordinates. \"trackcom\" is similar to \"track\" but the constant spatial offset is defined  relative to the center of mass of the kinematic subtree starting at the body in which the  light is defined. \"targetbody\" means that the light position is fixed in the body frame,  while the orientation is adjusted so that it always points towards the targeted body  specified with the target attribute. \"targetbodycom\" is the same as \"targetbody\" but the  light is oriented towards the center of mass of the subtree starting at the target body. Choice: `fixed`, `track`, `trackcom`, `targetbody`, `targetbodycom`. |
| `target` | `string` | no | — | This attribute specifies which body should be targeted in \"targetbody\" and \"targetbodycom\"  modes. In all other modes this attribute is ignored. |
| `type` | `string` | yes | `"spot"` | Determines the type of light. The built-in renderer supports spot, point and directional  lights. Choice: `spot`, `point`, `directional`. |
| `directional` | `bool` | yes | `false` | This is a deprecated legacy attribute. Please use the type attribute instead. If set to  \"true\", and no type is specified, this will change the light type to be directional. |
| `castshadow` | `bool` | yes | `true` | If this attribute is \"true\" the light will cast shadows. More precisely, the geoms  illuminated by the light will cast shadows, however this is a property of lights rather  than geoms. Since each shadow-casting light causes one extra rendering pass through all  geoms, this attribute should be used with caution. Higher quality shadows are achieved by  increasing the value of the shadowsize attribute of quality, as well as positioning  spotlights closer to the surface on which shadows appear, and limiting the volume in which  shadows are cast. For spotlights this volume is a cone, whose angle is the cutoff attribute  multiplied by the shadowscale attribute of map. For directional lights this volume is a  box, whose half-sizes in the directions orthogonal to the light are the model extent  multiplied by the shadowclip attribute of map. Internally the shadow-mapping mechanism  renders the scene from the light viewpoint into a depth texture, and then renders again  from the camera viewpoint, using the depth texture to create shadows. |
| `dir` | `real(3)` | yes | `"0.0 0.0 -1.0"` | Direction of the light. |
| `pos` | `real(3)` | yes | `"0.0 0.0 0.0"` | Position of the light. This attribute only affects the rendering for spotlights, but it  should also be defined for directional lights because they are rendered as decorative  elements. |
| `cutoff` | `real` | yes | `45.0` | Cutoff angle for spotlights, always in degrees regardless of the global angle setting. |
| `range` | `real` | yes | `10.0` | The effective range of the light. Objects further than this distance from the light  position will not be illuminated by this light. This only applies to spotlights. |
| `bulbradius` | `real` | yes | `0.02` | The radius of the light source which can affect shadow softness depending on the renderer.  This only applies to spotlights. |
| `attenuation` | `real(3)` | yes | `"1.0 0.0 0.0"` | The constant, linear and quadratic attenuation coefficients for Phong lighting. The default  corresponds to no attenuation. |
| `intensity` | `real` | yes | `0.0` | The intensity of the light source, measured in candela, used for physically-based lighting  models. This is unused by the default Phong lighting model. |
| `ambient` | `real(3)` | yes | `"0.0 0.0 0.0"` | The ambient color of the light, used by the default Phong lighting model. |
| `diffuse` | `real(3)` | yes | `"0.7 0.7 0.7"` | The color of the light. For the Phong (default) lighting model, this defines the diffuse  color of the light. |
| `specular` | `real(3)` | yes | `"0.3 0.3 0.3"` | The specular color of the light, used by the default Phong lighting model. |
| `innerangle` | `real` | yes | `35.0` | ----------Motphys Only----------  Cutoff angle for spotlights in degrees as inner angle. Motphys-only extension. |
| `nearz` | `real` | yes | `0.1` | The distance from the light to the near Z plane in the shadow map. Motphys-only extension. |

## body/replicate

**Path**: `body/replicate`
**Tag**: `replicate`
**Parent**: `body`
**Children**: none
**Rust Type**: `model::meta::Replicate`

This element is used to replicate a sub-tree of the model.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `count` | `int` | yes | `0` | Number of times to replicate the child nodes. |
| `sep` | `string` | no | — | Separator used to generate new names for the replicated elements. |
| `offset` | `real(3)` | no | — | Translation offset between consecutive replications. |
| `euler` | `real(3)` | no | — | Rotation offset between consecutive replications. |

## body/site

**Path**: `body/site`
**Tag**: `site`
**Parent**: `body`
**Children**: none
**Rust Type**: `model::body::site::Site`

A site is a simplified and restricted kind of geom. Semantically, sites represent locations of
 interest relative to the body frames. Sites do not participate in collisions and computation of
 body masses and inertias. The geometric shapes that can be used to render sites are limited to a
 subset of the available geom types. However, sites can be used in some places where geoms are
 not allowed: mounting sensors, specifying via-points of spatial tendons, and constructing
 slider-crank transmissions for actuators.

Note

 Sites do not participate in collision detection. Only a subset of geom types are supported for
 rendering: sphere, capsule, ellipsoid, cylinder, and box.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the site. |
| `class` | `string` | no | — | Defaults class for setting unspecified attributes. |
| `type` | `string` | yes | `"sphere"` | Type of geometric shape. This is used for rendering, and also determines the active sensor  zone for touch sensors. Choice: `sphere`, `capsule`, `cylinder`, `box`. |
| `group` | `int` | yes | `0` | Integer group to which the site belongs. This attribute can be used for custom tags. It is  also used by the visualizer to enable and disable the rendering of entire groups of sites. |
| `material` | `string` | no | — | Material used to specify the visual properties of the site. |
| `rgba` | `real(4)` | yes | `"0.5 0.5 0.5 1.0"` | Color and transparency. If this value is different from the internal default, it overrides  the corresponding material properties. |
| `size` | `real(n)` | no | — | Sizes of the geometric shape representing the site. |
| `fromto` | `real(6)` | no | — | This attribute can only be used with capsule, cylinder, ellipsoid and box sites. It  provides an alternative specification of the site length as well as the frame position and  orientation. The six numbers are the 3D coordinates of one point followed by the 3D  coordinates of another point. The elongated part of the site connects these two points,  with the +Z axis of the site's frame oriented from the first towards the second point. The  frame position is in the middle between the two points. If this attribute is specified, the  remaining position and orientation-related attributes are ignored. |
| `pos` | `real(3)` | yes | `"0.0 0.0 0.0"` | Position of the site frame. |
| `quat` | `real(4)` | no | — | Orientation of the site frame as unit quaternion.  → See [rotation representation](#rotation-attrs-quat). |
| `euler` | `real(3)` | no | — | Orientation of the site frame as Euler angles.  → See [rotation representation](#rotation-attrs-euler). |
| `axisangle` | `real(4)` | no | — | Orientation of the site frame as an axis-angle pair.  → See [rotation representation](#rotation-attrs-axisangle). |
| `xyaxes` | `real(6)` | no | — | Orientation of the site frame via X and Y axes.  → See [rotation representation](#rotation-attrs-xyaxes). |
| `zaxes` | `real(3)` | no | — | Orientation of the site frame via Z axis direction.  → See [rotation representation](#rotation-attrs-zaxis). |

