# actuator

**Path**: `actuator`
**Tag**: `actuator`
**Parent**: `mujoco`
**Children**: `actuator/adhesion`, `actuator/general`, `actuator/motor`, `actuator/position`, `actuator/velocity`
**Rust Type**: `model::actuator::Actuator`

This is a grouping element for actuator definitions. The first 13 common attributes of all
 actuator-related elements are the same and are documented under the general actuator type.

## actuator/adhesion

**Path**: `actuator/adhesion`
**Tag**: `adhesion`
**Parent**: `actuator`
**Children**: none
**Rust Type**: `model::actuator::Adhesion`

This element defines an active adhesion actuator which injects forces at contacts in the
 normal direction. The transmission target is a body, and adhesive forces are injected into
 all contacts involving geoms which belong to this body. The force is divided equally
 between multiple contacts.

 When the gap attribute is not used, this actuator requires active contacts and cannot
 apply a force at a distance, more like the active adhesion on the feet of geckos and
 insects rather than an industrial vacuum gripper. In order to enable suction at a
 distance, inflate the body's geoms by margin and add a corresponding gap which activates
 contacts only after gap penetration distance.

Note

 An adhesion actuator's length is always 0. ctrlrange is required and must be nonnegative
 (no repulsive forces are allowed). The body attribute is required.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Element name. |
| `class` | `string` | no | — | Active defaults class for setting unspecified attributes. |
| `group` | `int` | yes | `0` | Integer group to which the actuator belongs. This attribute can be used for custom  tags. It is also used by the visualizer to enable and disable the rendering of  entire groups of actuators. |
| `ctrllimited` | `string` | yes | `"auto"` | If true, the control input to this actuator is automatically clamped to ctrlrange  at runtime. If false, control input clamping is disabled. If \"auto\" and autolimits  is set in compiler, control clamping will automatically be set to true if ctrlrange  is defined without explicitly setting this attribute to \"true\". Note that control  input clamping can also be globally disabled with the clampctrl attribute of  option/flag. Choice: `false`, `true`, `auto`. |
| `forcelimited` | `string` | yes | `"auto"` | If true, the force output of this actuator is automatically clamped to forcerange  at runtime. If false, force clamping is disabled. If \"auto\" and autolimits is set  in compiler, force clamping will automatically be set to true if forcerange is  defined without explicitly setting this attribute to \"true\". Choice: `false`, `true`, `auto`. |
| `ctrlrange` | `real(2)` | no | — | Range for clamping the control input. The first value must be smaller than the  second value. Setting this attribute without specifying ctrllimited is an error if  autolimits is \"false\" in compiler. |
| `forcerange` | `real(2)` | no | — | Range for clamping the force output. The first value must be no greater than the  second value. Setting this attribute without specifying forcelimited is an error if  autolimits is \"false\" in compiler. |
| `gear` | `real(n)` | yes | `"1. 0. 0. 0. 0. 0."` | Scales the length (and consequently moment arms, velocity and force) of the  actuator, for all transmission types. It is different from the gain in the force  generation mechanism, because the gain only scales the force output and does not  affect the length, moment arms and velocity. For actuators with scalar  transmission, only the first element of this vector is used. The remaining  elements are needed for joint, jointinparent and site transmissions where this  attribute is used to specify 3D force and torque axes. |
| `joint` | `string` | no | — | If specified, the actuator acts on the given joint. For hinge and slide joints,  the actuator length equals the joint position/angle times the first element of  gear. For ball joints, the first three elements of gear define a 3D rotation axis  in the child frame around which the actuator produces torque. For free joints,  gear defines a 3D translation axis in the world frame followed by a 3D rotation  axis in the child frame. |
| `tendon` | `string` | no | — | If specified, the actuator acts on the given tendon. The actuator length equals  the tendon length times the gear ratio. Both spatial and fixed tendons can be  used. |
| `body` | `string` | no | — | The actuator acts on all contacts involving this body's geoms. This attribute is  required. |
| `gain` | `real` | yes | `1.0` | Gain of the adhesion actuator, in units of force. The total adhesion force applied by  the actuator is the control value multiplied by the gain. This force is distributed  equally between all the contacts involving geoms belonging to the target body. |

## actuator/general

**Path**: `actuator/general`
**Tag**: `general`
**Parent**: `actuator`
**Children**: none
**Rust Type**: `model::actuator::General`

This element creates a general actuator, providing full access to all actuator components
 and allowing the user to specify them independently.

 The general actuator combines three independently configurable subsystems: activation
 dynamics (dyntype/dynprm), gain (gaintype/gainprm), and bias (biastype/biasprm). The
 output force is computed as: scalar_force = gain_term * (act or ctrl) + bias_term, where
 the activation state is used when present and the control input otherwise.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Element name. |
| `class` | `string` | no | — | Active defaults class for setting unspecified attributes. |
| `group` | `int` | yes | `0` | Integer group to which the actuator belongs. This attribute can be used for custom  tags. It is also used by the visualizer to enable and disable the rendering of  entire groups of actuators. |
| `ctrllimited` | `string` | yes | `"auto"` | If true, the control input to this actuator is automatically clamped to ctrlrange  at runtime. If false, control input clamping is disabled. If \"auto\" and autolimits  is set in compiler, control clamping will automatically be set to true if ctrlrange  is defined without explicitly setting this attribute to \"true\". Note that control  input clamping can also be globally disabled with the clampctrl attribute of  option/flag. Choice: `false`, `true`, `auto`. |
| `forcelimited` | `string` | yes | `"auto"` | If true, the force output of this actuator is automatically clamped to forcerange  at runtime. If false, force clamping is disabled. If \"auto\" and autolimits is set  in compiler, force clamping will automatically be set to true if forcerange is  defined without explicitly setting this attribute to \"true\". Choice: `false`, `true`, `auto`. |
| `ctrlrange` | `real(2)` | no | — | Range for clamping the control input. The first value must be smaller than the  second value. Setting this attribute without specifying ctrllimited is an error if  autolimits is \"false\" in compiler. |
| `forcerange` | `real(2)` | no | — | Range for clamping the force output. The first value must be no greater than the  second value. Setting this attribute without specifying forcelimited is an error if  autolimits is \"false\" in compiler. |
| `gear` | `real(n)` | yes | `"1. 0. 0. 0. 0. 0."` | Scales the length (and consequently moment arms, velocity and force) of the  actuator, for all transmission types. It is different from the gain in the force  generation mechanism, because the gain only scales the force output and does not  affect the length, moment arms and velocity. For actuators with scalar  transmission, only the first element of this vector is used. The remaining  elements are needed for joint, jointinparent and site transmissions where this  attribute is used to specify 3D force and torque axes. |
| `joint` | `string` | no | — | If specified, the actuator acts on the given joint. For hinge and slide joints,  the actuator length equals the joint position/angle times the first element of  gear. For ball joints, the first three elements of gear define a 3D rotation axis  in the child frame around which the actuator produces torque. For free joints,  gear defines a 3D translation axis in the world frame followed by a 3D rotation  axis in the child frame. |
| `tendon` | `string` | no | — | If specified, the actuator acts on the given tendon. The actuator length equals  the tendon length times the gear ratio. Both spatial and fixed tendons can be  used. |
| `dyntype` | `string` | yes | `"none"` | Activation dynamics type for the actuator. Determines how the internal activation  state evolves in response to control input. Available types are: none (no internal  state), integrator (act_dot = ctrl), filter (act_dot = (ctrl - act) / dynprm[0]),  filterexact (like filter but with exact integration). Choice: `none`, `integrator`, `filter`, `filterexact`, `muscle`, `user`. |
| `gaintype` | `string` | yes | `"fixed"` | The gain type determines the gain_term in the force generation formula. Available  types are: fixed (gain_term = gainprm[0]), affine (gain_term = gainprm[0] +  gainprm[1]*length + gainprm[2]*velocity). Choice: `fixed`, `affine`, `muscle`, `user`. |
| `biastype` | `string` | yes | `"none"` | The bias type determines the bias_term in the force generation formula. Available  types are: none (bias_term = 0), affine (bias_term = biasprm[0] +  biasprm[1]*length + biasprm[2]*velocity). Choice: `none`, `affine`, `muscle`, `user`. |
| `dynprm` | `real(n)` | yes | `"1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0."` | Activation dynamics parameters. The built-in activation types (except for muscle)  use only the first parameter, but additional parameters are provided in case user  callbacks implement a more elaborate model. The length of this array is not enforced  by the parser, so the user can enter as many parameters as needed. |
| `gainprm` | `real(n)` | yes | `"1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0."` | Gain parameters. The built-in gain types (except for muscle) use only the first  parameter, but additional parameters are provided in case user callbacks implement a  more elaborate model. The length of this array is not enforced by the parser, so the  user can enter as many parameters as needed. |
| `biasprm` | `real(n)` | yes | `"0.; 10"` | Bias parameters. The affine bias type uses three parameters. The length of this array  is not enforced by the parser, so the user can enter as many parameters as needed. |
| `actearly` | `bool` | yes | `false` | If true, force computation will use the next value of the activation variable rather  than the current one. Setting this flag reduces the delay between the control and  accelerations by one time-step. |
| `actlimited` | `string` | yes | `"auto"` | If true, the activation associated with this actuator is automatically clamped to actrange at runtime.  If false, activation clamping is disabled. If \"auto\" and autolimits is set in compiler, activation clamping will  be set to true if actrange is defined without explicitly setting this attribute to \"true\". Choice: `false`, `true`, `auto`. |
| `actrange` | `real(2)` | no | — | Range for clamping the activation. The first value must be smaller than the second value.  Setting this attribute without specifying actlimited is an error if autolimits is \"false\" in compiler. |

## actuator/motor

**Path**: `actuator/motor`
**Tag**: `motor`
**Parent**: `actuator`
**Children**: none
**Rust Type**: `model::actuator::Motor`

This element creates a direct-drive actuator. It is one of the actuator shortcuts that
 maps to a general actuator with fixed gain, no activation dynamics, and no bias
 (dyntype=none, gaintype=fixed, biastype=none). The control input is transmitted directly
 as force or torque scaled by the gear ratio and gainprm[0].

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Element name. |
| `class` | `string` | no | — | Active defaults class for setting unspecified attributes. |
| `group` | `int` | yes | `0` | Integer group to which the actuator belongs. This attribute can be used for custom  tags. It is also used by the visualizer to enable and disable the rendering of  entire groups of actuators. |
| `ctrllimited` | `string` | yes | `"auto"` | If true, the control input to this actuator is automatically clamped to ctrlrange  at runtime. If false, control input clamping is disabled. If \"auto\" and autolimits  is set in compiler, control clamping will automatically be set to true if ctrlrange  is defined without explicitly setting this attribute to \"true\". Note that control  input clamping can also be globally disabled with the clampctrl attribute of  option/flag. Choice: `false`, `true`, `auto`. |
| `forcelimited` | `string` | yes | `"auto"` | If true, the force output of this actuator is automatically clamped to forcerange  at runtime. If false, force clamping is disabled. If \"auto\" and autolimits is set  in compiler, force clamping will automatically be set to true if forcerange is  defined without explicitly setting this attribute to \"true\". Choice: `false`, `true`, `auto`. |
| `ctrlrange` | `real(2)` | no | — | Range for clamping the control input. The first value must be smaller than the  second value. Setting this attribute without specifying ctrllimited is an error if  autolimits is \"false\" in compiler. |
| `forcerange` | `real(2)` | no | — | Range for clamping the force output. The first value must be no greater than the  second value. Setting this attribute without specifying forcelimited is an error if  autolimits is \"false\" in compiler. |
| `gear` | `real(n)` | yes | `"1. 0. 0. 0. 0. 0."` | Scales the length (and consequently moment arms, velocity and force) of the  actuator, for all transmission types. It is different from the gain in the force  generation mechanism, because the gain only scales the force output and does not  affect the length, moment arms and velocity. For actuators with scalar  transmission, only the first element of this vector is used. The remaining  elements are needed for joint, jointinparent and site transmissions where this  attribute is used to specify 3D force and torque axes. |
| `joint` | `string` | no | — | If specified, the actuator acts on the given joint. For hinge and slide joints,  the actuator length equals the joint position/angle times the first element of  gear. For ball joints, the first three elements of gear define a 3D rotation axis  in the child frame around which the actuator produces torque. For free joints,  gear defines a 3D translation axis in the world frame followed by a 3D rotation  axis in the child frame. |
| `tendon` | `string` | no | — | If specified, the actuator acts on the given tendon. The actuator length equals  the tendon length times the gear ratio. Both spatial and fixed tendons can be  used. |

## actuator/position

**Path**: `actuator/position`
**Tag**: `position`
**Parent**: `actuator`
**Children**: none
**Rust Type**: `model::actuator::Position`

This element creates a position servo with an optional first-order filter. It is an
 actuator shortcut that configures a general actuator with gaintype=fixed (gainprm=kp),
 biastype=affine (biasprm = [0, -kp, -kv]), and optionally dyntype=filterexact when a
 non-zero timeconst is specified.

Note

 This actuator cannot be combined with both ctrlrange and inheritrange simultaneously;
 exactly one must be used if range clamping is desired.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Element name. |
| `class` | `string` | no | — | Active defaults class for setting unspecified attributes. |
| `group` | `int` | yes | `0` | Integer group to which the actuator belongs. This attribute can be used for custom  tags. It is also used by the visualizer to enable and disable the rendering of  entire groups of actuators. |
| `ctrllimited` | `string` | yes | `"auto"` | If true, the control input to this actuator is automatically clamped to ctrlrange  at runtime. If false, control input clamping is disabled. If \"auto\" and autolimits  is set in compiler, control clamping will automatically be set to true if ctrlrange  is defined without explicitly setting this attribute to \"true\". Note that control  input clamping can also be globally disabled with the clampctrl attribute of  option/flag. Choice: `false`, `true`, `auto`. |
| `forcelimited` | `string` | yes | `"auto"` | If true, the force output of this actuator is automatically clamped to forcerange  at runtime. If false, force clamping is disabled. If \"auto\" and autolimits is set  in compiler, force clamping will automatically be set to true if forcerange is  defined without explicitly setting this attribute to \"true\". Choice: `false`, `true`, `auto`. |
| `ctrlrange` | `real(2)` | no | — | Range for clamping the control input. The first value must be smaller than the  second value. Setting this attribute without specifying ctrllimited is an error if  autolimits is \"false\" in compiler. |
| `forcerange` | `real(2)` | no | — | Range for clamping the force output. The first value must be no greater than the  second value. Setting this attribute without specifying forcelimited is an error if  autolimits is \"false\" in compiler. |
| `gear` | `real(n)` | yes | `"1. 0. 0. 0. 0. 0."` | Scales the length (and consequently moment arms, velocity and force) of the  actuator, for all transmission types. It is different from the gain in the force  generation mechanism, because the gain only scales the force output and does not  affect the length, moment arms and velocity. For actuators with scalar  transmission, only the first element of this vector is used. The remaining  elements are needed for joint, jointinparent and site transmissions where this  attribute is used to specify 3D force and torque axes. |
| `joint` | `string` | no | — | If specified, the actuator acts on the given joint. For hinge and slide joints,  the actuator length equals the joint position/angle times the first element of  gear. For ball joints, the first three elements of gear define a 3D rotation axis  in the child frame around which the actuator produces torque. For free joints,  gear defines a 3D translation axis in the world frame followed by a 3D rotation  axis in the child frame. |
| `tendon` | `string` | no | — | If specified, the actuator acts on the given tendon. The actuator length equals  the tendon length times the gear ratio. Both spatial and fixed tendons can be  used. |
| `kp` | `real` | yes | `1.0` | Position feedback gain. Used internally as gainprm[0] and also negated into  biasprm[1] to produce a restoring force proportional to position error. |
| `kv` | `real` | no | — | Damping applied by the actuator. Used internally as biasprm[2] (negated) to produce  a force proportional to velocity. When using this attribute, it is recommended to use  the implicitfast or implicit integrators. This explicit damping value is exclusive with  dampratio. |
| `dampratio` | `real` | no | — | Damping ratio of the position actuator. When specified, the actual damping is computed  at runtime from the current joint inertia as  `2 * dampratio * sqrt(kp * mass / gear[0]^2)`. This attribute is exclusive with kv. |
| `inheritrange` | `real` | no | — | Automatically sets the actuator's ctrlrange to match the transmission target's range.  A positive value X sets the ctrlrange around the midpoint of the target range, scaled  by X. For example if the target joint has range [0, 1], then a value of 1.0 will set  ctrlrange to [0, 1]; values of 0.8 and 1.2 will set the ctrlrange to [0.1, 0.9] and  [-0.1, 1.1], respectively. Values smaller than 1 are useful for not hitting the  limits; values larger than 1 are useful for maintaining control authority at the  limits. This attribute is exclusive with ctrlrange and available only for joint and  tendon transmissions which have range defined. |
| `timeconst` | `real` | yes | `0.0` | Time-constant of optional first-order filter. If larger than 0, the actuator will use  the filterexact dynamics type, if 0 (the default), the actuator will use the none dynamics type. |

## actuator/velocity

**Path**: `actuator/velocity`
**Tag**: `velocity`
**Parent**: `actuator`
**Children**: none
**Rust Type**: `model::actuator::Velocity`

This element creates a velocity servo. It is an actuator shortcut that configures a
 general actuator with gaintype=fixed (gainprm=kv), biastype=affine (biasprm = [0, 0,
 -kv]), and dyntype=none. The actuator produces a force proportional to the difference
 between the reference velocity (ctrl) and the actual velocity.

Note

 In order to create a PD controller, one has to define two actuators: a position servo and
 a velocity servo. This is because MJCF actuators are SISO (single-input single-output)
 while a PD controller takes two control inputs (reference position and reference velocity).
 When using this actuator, it is recommended to use the implicitfast or implicit integrators.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Element name. |
| `class` | `string` | no | — | Active defaults class for setting unspecified attributes. |
| `group` | `int` | yes | `0` | Integer group to which the actuator belongs. This attribute can be used for custom  tags. It is also used by the visualizer to enable and disable the rendering of  entire groups of actuators. |
| `ctrllimited` | `string` | yes | `"auto"` | If true, the control input to this actuator is automatically clamped to ctrlrange  at runtime. If false, control input clamping is disabled. If \"auto\" and autolimits  is set in compiler, control clamping will automatically be set to true if ctrlrange  is defined without explicitly setting this attribute to \"true\". Note that control  input clamping can also be globally disabled with the clampctrl attribute of  option/flag. Choice: `false`, `true`, `auto`. |
| `forcelimited` | `string` | yes | `"auto"` | If true, the force output of this actuator is automatically clamped to forcerange  at runtime. If false, force clamping is disabled. If \"auto\" and autolimits is set  in compiler, force clamping will automatically be set to true if forcerange is  defined without explicitly setting this attribute to \"true\". Choice: `false`, `true`, `auto`. |
| `ctrlrange` | `real(2)` | no | — | Range for clamping the control input. The first value must be smaller than the  second value. Setting this attribute without specifying ctrllimited is an error if  autolimits is \"false\" in compiler. |
| `forcerange` | `real(2)` | no | — | Range for clamping the force output. The first value must be no greater than the  second value. Setting this attribute without specifying forcelimited is an error if  autolimits is \"false\" in compiler. |
| `gear` | `real(n)` | yes | `"1. 0. 0. 0. 0. 0."` | Scales the length (and consequently moment arms, velocity and force) of the  actuator, for all transmission types. It is different from the gain in the force  generation mechanism, because the gain only scales the force output and does not  affect the length, moment arms and velocity. For actuators with scalar  transmission, only the first element of this vector is used. The remaining  elements are needed for joint, jointinparent and site transmissions where this  attribute is used to specify 3D force and torque axes. |
| `joint` | `string` | no | — | If specified, the actuator acts on the given joint. For hinge and slide joints,  the actuator length equals the joint position/angle times the first element of  gear. For ball joints, the first three elements of gear define a 3D rotation axis  in the child frame around which the actuator produces torque. For free joints,  gear defines a 3D translation axis in the world frame followed by a 3D rotation  axis in the child frame. |
| `tendon` | `string` | no | — | If specified, the actuator acts on the given tendon. The actuator length equals  the tendon length times the gear ratio. Both spatial and fixed tendons can be  used. |
| `kv` | `real` | yes | `1.0` | Velocity feedback gain. Used internally as gainprm[0] and also negated into  biasprm[2] to produce a damping force proportional to velocity. |

