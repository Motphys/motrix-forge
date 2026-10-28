# tendon

**Path**: `tendon`
**Tag**: `tendon`
**Parent**: `mujoco`
**Children**: `tendon/fixed`
**Rust Type**: `model::tendon::Tendon`

Grouping element for tendon definitions.

 Tendons can be used to impose length limits, simulate spring, damping and dry friction forces,
 as well as attach actuators to them. When used in equality constraints, tendons can also
 represent different forms of mechanical coupling.

## tendon/fixed

**Path**: `tendon/fixed`
**Tag**: `fixed`
**Parent**: `tendon`
**Children**: `tendon/fixed/joint`
**Rust Type**: `model::tendon::Fixed`

Abstract tendon whose length is defined as a linear combination of joint positions.

 The tendon length and its gradient are the only quantities needed for simulation. The
 length is computed by multiplying the position or angle of each included joint by the
 corresponding coefficient value and summing the results. The attributes of fixed tendons
 are a subset of the attributes of spatial tendons and have the same meaning.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `group` | `int` | yes | `0` | Integer group to which the tendon belongs. This attribute can be used for custom  tags. It is also used by the visualizer to enable and disable the rendering of  entire groups of tendons. |
| `limited` | `string` | yes | `"auto"` | If this attribute is \"true\", the length limits defined by the range attribute are  imposed by the constraint solver. If this attribute is \"auto\", and autolimits is  set in compiler, length limits will be enabled if range is defined. Choice: `false`, `true`, `auto`. |
| `range` | `real(2)` | no | — | Range of allowed tendon lengths. Setting this attribute without specifying limited  is an error, unless autolimits is set in compiler. |
| `solreflimit` | `real(n)` | no | — | Solver reference parameters for tendon limits.  → See [solver parameters](#solver-attrs-solref). |
| `solimplimit` | `real(5)` | yes | `"0.9 0.95 0.001 0.5 2.0"` | Solver impedance parameters for tendon limits.  → See [solver parameters](#solver-attrs-solimp). |
| `frictionloss` | `real` | yes | `0.0` | Friction loss caused by dry friction. To enable friction loss, set this attribute  to a positive value. |
| `solreffriction` | `real(2)` | yes | `"0.02 1.0"` | Solver reference parameters for tendon dry friction.  → See [solver parameters](#solver-attrs-solref). |
| `solimpfriction` | `real(5)` | yes | `"0.9 0.95 0.001 0.5 2.0"` | Solver impedance parameters for tendon dry friction.  → See [solver parameters](#solver-attrs-solimp). |
| `margin` | `real` | yes | `0.0` | The limit constraint becomes active when the absolute value of the difference  between the tendon length and either limit of the specified range falls below this  margin. Similar to contacts, the margin parameter is subtracted from the difference  between the range limit and the tendon length. The resulting constraint distance is  always negative when the constraint is active. |
| `width` | `real` | yes | `0.003` | Radius of the cross-section area of the spatial tendon, used for rendering. Parts  of the tendon that wrap around geom obstacles are rendered with reduced width. |
| `rgba` | `real(4)` | yes | `"0.5 0.5 0.5 1."` | Color and transparency of the tendon. When this value is different from the  internal default, it overrides the corresponding material properties. If a material  is unspecified and rgba has the default value, limited tendons whose length exceeds  the limit are recolored based on the constraint impedance. |
| `springlength` | `real(n)` | yes | `""` | Spring resting position, can take either one or two values. If one value is given,  it corresponds to the length of the tendon at rest. If it is -1, the tendon resting  length is determined from the model reference configuration. If two non-decreasing  values are given, they define a dead-band range: if the tendon length is between  the two values the force is zero, and outside this range the force behaves like a  regular spring with the rest-point corresponding to the nearest springlength value. |
| `stiffness` | `real` | no | — | Stiffness coefficient. A positive value generates a spring force (linear in  position) acting along the tendon. |
| `damping` | `real` | no | — | Damping coefficient. A positive value generates a damping force (linear in  velocity) acting along the tendon. Unlike joint damping which is integrated  implicitly by the Euler method, tendon damping is not integrated implicitly, thus  joint damping should be used if possible. |
| `name` | `string` | no | — | Name of the tendon. |
| `class` | `string` | no | — | Defaults class for setting unspecified attributes. |

### tendon/fixed/joint

**Path**: `tendon/fixed/joint`
**Tag**: `joint`
**Parent**: `tendon/fixed`
**Children**: none
**Rust Type**: `model::tendon::Joint`

A joint contributing to the length computation of a fixed tendon.

 This element adds a joint to the computation of the fixed tendon length. The position or angle
 of each included joint is multiplied by the corresponding coef value, and added up to obtain
 the tendon length.

#### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `joint` | `string` | yes | `""""` | Name of the joint to be added to the fixed tendon. Only scalar joints (slide and hinge)  can be referenced here. |
| `coef` | `real` | yes | `0.0` | Scalar coefficient multiplying the position or angle of the specified joint. |

