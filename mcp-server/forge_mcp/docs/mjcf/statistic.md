# statistic

**Path**: `statistic`
**Tag**: `statistic`
**Parent**: `mujoco`
**Children**: none
**Rust Type**: `model::others::SceneStatistic`

This element is used to override model statistics computed by the compiler.

 These statistics are not only informational but are also used to scale various components of
 the rendering and perturbation. An override mechanism is provided in the XML because it is
 sometimes easier to adjust a small number of model statistics than a larger number of visual
 parameters.

## Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `extent` | `real` | no | — | Replaces the extent value computed by the compiler. The computed value is half the side of  the bounding box of the model in the initial configuration. At runtime this value is  multiplied by some of the attributes of the `map` element. When the model is first loaded,  the free camera's initial distance from the center is 1.5 times the extent. Must be  strictly positive. |
| `center` | `real(3)` | no | — | Replaces the center value computed by the compiler. The computed value is the center of the  bounding box of the entire model in the initial configuration. This 3D vector is used to  center the view of the free camera when the model is first loaded. |

