# keyframe

**Path**: `keyframe`
**Tag**: `keyframe`
**Parent**: `mujoco`
**Children**: `keyframe/key`
**Rust Type**: `model::keyframe::Keyframe`

This element is a grouping element for keyframes.

## keyframe/key

**Path**: `keyframe/key`
**Tag**: `key`
**Parent**: `keyframe`
**Children**: none
**Rust Type**: `model::keyframe::Key`

This element sets the data of a keyframe.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the keyframe. |
| `time` | `real` | no | — | Simulation time. |
| `qpos` | `string` | no | — | Joint positions. |
| `qvel` | `string` | no | — | Joint velocities. |
| `ctrl` | `string` | no | — | Actuator controls. |

