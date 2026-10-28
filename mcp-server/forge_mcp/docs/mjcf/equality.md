# equality

**Path**: `equality`
**Tag**: `equality`
**Parent**: `mujoco`
**Children**: `equality/connect`, `equality/joint`, `equality/weld`
**Rust Type**: `model::equality::EqualitySet`

This is a grouping element for equality constraints. It does not have attributes. Several
 attributes are common to all equality constraint types and are documented once under the connect
 element.

## equality/connect

**Path**: `equality/connect`
**Tag**: `connect`
**Parent**: `equality`
**Children**: none
**Rust Type**: `model::equality::EqualityConnect`

This element creates an equality constraint that connects two bodies at a point. The
 constraint effectively defines a ball joint outside the kinematic tree.

 Connect constraints can be specified in one of two ways. The first uses body1 and anchor
 (both required) and optionally body2; when using this specification the constraint is
 assumed to be satisfied at the configuration in which the model is defined.
 The second uses site1 and site2 (both required); when using this specification the two
 sites will be pulled together by the constraint regardless of their position in the default
 configuration.

Note

 The body-based and site-based specifications are mutually exclusive and cannot be combined.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the equality constraint. |
| `class` | `string` | no | — | Defaults class for setting unspecified attributes. |
| `active` | `bool` | yes | `true` | If this attribute is set to \"true\", the constraint is active and the constraint  solver will try to enforce it. This value is used to initialize the runtime constraint activation state, which is user-settable at  runtime. |
| `solref` | `real(n)` | no | — | Solver reference parameters for equality constraints.  → See [solver parameters](#solver-attrs-solref). |
| `solimp` | `real(5)` | yes | `"0.9 0.95 0.001 0.5 2.0"` | Solver impedance parameters for equality constraints.  → See [solver parameters](#solver-attrs-solimp). |
| `body1` | `string` | no | — | Name of the first body participating in the constraint. Either this attribute and  anchor must be specified, or site1 and site2 must be specified. |
| `body2` | `string` | no | — | Name of the second body participating in the constraint. If this attribute is omitted,  the second body is the world body. |
| `anchor` | `real(3)` | no | — | Coordinates of the 3D anchor point where the two bodies are connected, in the local  coordinate frame of body1. The constraint is assumed to be satisfied in the  configuration at which the model is defined, which lets the compiler  compute the associated anchor point for body2. |
| `site1` | `string` | no | — | Name of a site belonging to the first body participating in the constraint. When  specified, site2 must also be specified. The (site1, site2) specification is a more  flexible alternative to the body-based specification: the sites are not required to  overlap at the default configuration (if they do not overlap they will snap together  at the beginning of the simulation), and changing the site positions at runtime will  correctly change the position of the constraint. |
| `site2` | `string` | no | — | Name of a site belonging to the second body participating in the constraint. When  specified, site1 must also be specified. See the site1 description for more details. |

## equality/joint

**Path**: `equality/joint`
**Tag**: `joint`
**Parent**: `equality`
**Children**: none
**Rust Type**: `model::equality::EqualityJoint`

This element constrains the position or angle of one joint to be a quartic polynomial of
 another joint. Only scalar joint types (slide and hinge) can be used.

 If joint values of joint1 and joint2 are respectively y and x, and their reference
 positions (corresponding to the joint values in the initial model configuration) are y0
 and x0, the constraint enforced is:
 y - y0 = a0 + a1*(x - x0) + a2*(x - x0)^2 + a3*(x - x0)^3 + a4*(x - x0)^4

Note

 Omitting joint2 is equivalent to setting x = x0, in which case the constraint reduces to
 y = y0 + a0.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the equality constraint. |
| `class` | `string` | no | — | Defaults class for setting unspecified attributes. |
| `active` | `bool` | yes | `true` | If this attribute is set to \"true\", the constraint is active and the constraint  solver will try to enforce it. This value is used to initialize the runtime constraint activation state, which is user-settable at  runtime. |
| `solref` | `real(n)` | no | — | Solver reference parameters for equality constraints.  → See [solver parameters](#solver-attrs-solref). |
| `solimp` | `real(5)` | yes | `"0.9 0.95 0.001 0.5 2.0"` | Solver impedance parameters for equality constraints.  → See [solver parameters](#solver-attrs-solimp). |
| `joint1` | `string` | yes | `""""` | Name of the first joint. |
| `joint2` | `string` | no | — | Name of the second joint. If this attribute is omitted, the first joint is fixed to a  constant. |
| `polycoef` | `real(n)` | no | — | Coefficients a0 through a4 of the quartic polynomial relating the positions of joint1  and joint2. If the joint values of joint1 and joint2 are respectively y and x, and  their reference positions are y0 and x0, the constraint is:  y - y0 = a0 + a1*(x - x0) + a2*(x - x0)^2 + a3*(x - x0)^3 + a4*(x - x0)^4. |

## equality/weld

**Path**: `equality/weld`
**Tag**: `weld`
**Parent**: `equality`
**Children**: none
**Rust Type**: `model::equality::EqualityWeld`

This element creates a weld equality constraint. It attaches two bodies to each other,
 removing all relative degrees of freedom between them via the constraint solver. The two
 bodies are not required to be close to each other. The relative body position and
 orientation being enforced by the constraint solver is the one in which the model was
 defined.

 Weld constraints can be specified in one of two ways. The first uses body1 (and optionally
 anchor, relpose, body2); when using this specification the constraint is assumed to be
 satisfied at the configuration in which the model is defined. The second uses site1 and
 site2 (both required); when using this specification the frames of the two sites will be
 aligned by the constraint regardless of their position in the default configuration.

Note

 Two bodies can also be welded together rigidly by defining one body as a child of the
 other body without any joint elements in the child body. The weld equality constraint
 provides a soft (constraint-based) alternative. The body-based and site-based
 specifications are mutually exclusive and cannot be combined. Welding a body to the world
 and toggling the constraint activation state at runtime can be used to fix a body temporarily.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the equality constraint. |
| `class` | `string` | no | — | Defaults class for setting unspecified attributes. |
| `active` | `bool` | yes | `true` | If this attribute is set to \"true\", the constraint is active and the constraint  solver will try to enforce it. This value is used to initialize the runtime constraint activation state, which is user-settable at  runtime. |
| `solref` | `real(n)` | no | — | Solver reference parameters for equality constraints.  → See [solver parameters](#solver-attrs-solref). |
| `solimp` | `real(5)` | yes | `"0.9 0.95 0.001 0.5 2.0"` | Solver impedance parameters for equality constraints.  → See [solver parameters](#solver-attrs-solimp). |
| `body1` | `string` | no | — | Name of the first body participating in the constraint. Either this attribute must be  specified or site1 and site2 must be specified. |
| `body2` | `string` | no | — | Name of the second body. If this attribute is omitted, the second body is the world  body. Welding a body to the world and changing the corresponding component of  the runtime constraint activation state can be used to fix the body temporarily. |
| `anchor` | `real(3)` | yes | `"0.0 0.0 0.0"` | Coordinates of the weld point relative to body2. If relpose is not specified, the  meaning of this parameter is the same as for connect constraints except that it is  relative to body2. If relpose is specified, body1 will use the pose to compute its  anchor point. |
| `site1` | `string` | no | — | Name of a site belonging to the first body participating in the constraint. When  specified, site2 must also be specified. The (site1, site2) specification is a more  flexible alternative to the body-based specification: the sites are not required to  overlap at the default configuration (if they do not, the sites will snap together  at the beginning of the simulation), and changing the site position and orientation at  runtime will correctly change the position and orientation of the constraint. Note that torquescale still takes effect even when  using the site-based specification. |
| `site2` | `string` | no | — | Name of a site belonging to the second body participating in the constraint. When  specified, site1 must also be specified. See the site1 description for more details. |
| `relpose` | `real(7)` | yes | `"0.0 1.0 0.0 0.0 0.0 0.0 0.0"` | This attribute specifies the relative pose (3D position followed by 4D quaternion  orientation) of body2 relative to body1. If the quaternion part (the last 4  components) are all zeros, as in the default setting, this attribute is ignored and  the relative pose is the one corresponding to the model reference pose in qpos0. |
| `torquescale` | `real` | yes | `1.0` | A constant that scales the angular residual (angular constraint violation). Intuitively  this coefficient defines how much the weld cares about rotational displacements versus  translational displacements. Setting this value to 0 makes the weld behave like a  connect constraint. This value has units of length and can be understood as the  diameter of a flat patch of glue sticking the two bodies together. |

