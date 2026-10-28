# option

**Path**: `option`
**Tag**: `option`
**Parent**: `mujoco`
**Children**: `option/flag`
**Rust Type**: `model::option::MjcfOption`

Global simulation options that control physics behavior and solver settings.

 These are simulation options and do not affect the compilation process in any way; they are
 simply copied into the low level model. Even though these options can be modified at runtime,
 it is nevertheless a good idea to adjust them properly through the XML.

Note

 The most important parameter affecting the speed-accuracy trade-off is `timestep`. Stability
 is determined not only by the time step but also by the solver parameters; in particular,
 softer constraints can be simulated with larger time steps.

## Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `timestep` | `real` | yes | `0.002` | The simulation time step in seconds. This is the single most important parameter affecting  the speed-accuracy trade-off which is inherent in every physics simulation. Smaller values  result in better accuracy and stability. To achieve real-time performance, the time step  must be larger than the CPU time per step (or 4 times larger when using the RK4  integrator). Models with many floating objects (resulting in many contacts) are more  demanding computationally. When fine-tuning a challenging model, it is recommended to  experiment with both time step and solver parameter settings jointly. In  optimization-related applications where real-time is insufficient, the time step should be  made as large as possible. |
| `gravity` | `real(3)` | yes | `"0.0 0.0 -9.81"` | Gravitational acceleration vector. In the default world orientation the Z-axis points up,  which is the convention used throughout the simulation stack and is not recommended to  deviate from. |
| `iterations` | `int` | yes | `100` | Maximum number of iterations of the constraint solver. When the warmstart flag is enabled  (which is the default), accurate results are obtained with fewer iterations. Larger and  more complex systems with many interacting constraints require more iterations. Note that  the solver computes convergence statistics during simulation, which can be accessed via the  simulation data. |
| `tolerance` | `real` | yes | `1e-8` | Tolerance threshold used for early termination of the iterative solver. For PGS, the  threshold is applied to the cost improvement between two iterations. For CG and Newton, it  is applied to the smaller of the cost improvement and the gradient norm. Set the tolerance  to 0 to disable early termination. |
| `o_solref` | `real(n)` | no | — | These attributes replace the solref, solimp and friction parameters of all active contact  pairs when contact override is enabled. |
| `o_solimp` | `real(n)` | no | — | These attributes replace the solref, solimp and friction parameters of all active contact  pairs when contact override is enabled. |
| `o_friction` | `real(n)` | no | — | These attributes replace the solref, solimp and friction parameters of all active contact  pairs when contact override is enabled. |
| `o_margin` | `real` | yes | `0.0` | This attribute replaces the margin parameter of all active contact pairs when Contact  override is enabled. Otherwise the element-specific margin attribute of geom or pair is  used depending on how the contact pair was generated. The related gap parameter does not  have a global override. |
| `sdf_iterations` | `int` | yes | `10` | Number of iterations used for Signed Distance Field collisions (per initial poing) |
| `sdf_initpoints` | `int` | yes | `40` | Number of starting points used for finding contacts with Signed Distance Field collisions |

## option/flag

**Path**: `option/flag`
**Tag**: `flag`
**Parent**: `option`
**Children**: none
**Rust Type**: `model::option::Flag`

Flags that enable and disable different parts of the simulation pipeline.

 The actual flags used at runtime are represented as the bits of two integers, used to disable
 standard features and enable optional features respectively. The reason for this separation is
 that setting both integers to 0 restores the default.

Note

 In the XML, the separation between disableflags and enableflags is not made explicit, except
 for the default attribute values — which are \"enable\" for flags corresponding to standard
 features, and \"disable\" for flags corresponding to optional features.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `constraint` | `string` | yes | `"enable"` | When set to disable, all standard computations related to the constraint solver are  skipped and no constraint forces are applied. Note that the equality, frictionloss, limit,  and contact flags each disable computations for a specific type of constraint; both this  flag and the type-specific flag must be set to enable for a given computation to be  performed. Choice: `disable`, `enable`. |
| `equality` | `string` | yes | `"enable"` | When set to disable, all standard computations related to equality constraints are skipped. Choice: `disable`, `enable`. |
| `frictionloss` | `string` | yes | `"enable"` | When set to disable, all standard computations related to friction loss constraints are  skipped. Choice: `disable`, `enable`. |
| `limit` | `string` | yes | `"enable"` | When set to disable, all standard computations related to joint and tendon limit  constraints are skipped. Choice: `disable`, `enable`. |
| `contact` | `string` | yes | `"enable"` | When set to disable, collision detection and all standard computations related to contact  constraints are skipped. Choice: `disable`, `enable`. |
| `gravity` | `string` | yes | `"enable"` | When set to disable, the gravitational acceleration vector is replaced with (0 0 0) at  runtime, without changing the stored value. Once the flag is re-enabled, the stored value  is used again. Choice: `disable`, `enable`. |
| `actuation` | `string` | yes | `"enable"` | When set to disable, all standard computations related to actuator forces are skipped,  including the actuator dynamics. As a result, no actuator forces are applied to the  simulation. Choice: `disable`, `enable`. |
| `refsafe` | `string` | yes | `"enable"` | Choice: `disable`, `enable`. |
| `override` | `string` | yes | `"disable"` | When set to enable, activates the Contact override mechanism, which causes the global  o_margin, o_solref, o_solimp, and o_friction values to replace the corresponding  per-contact parameters for all active contact pairs. Choice: `disable`, `enable`. |

