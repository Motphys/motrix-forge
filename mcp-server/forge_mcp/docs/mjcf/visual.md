# visual

**Path**: `visual`
**Tag**: `visual`
**Parent**: `mujoco`
**Children**: `visual/headlight`, `visual/global`, `visual/quality`, `visual/map`, `visual/rgba`, `visual/probe`, `visual/ssao`, `visual/ssgi`, `visual/tonemapping`
**Rust Type**: `model::visual::Visual`

Settings that affect the visualizer.

 The settings here affect the visualizer, or more precisely the abstract phase of visualization
 which yields a list of geometric entities for subsequent rendering. The settings here are
 global, in contrast with the element-specific visual settings. The global and element-specific
 settings refer to non-overlapping properties. Some of the global settings affect properties such
 as triangulation of geometric primitives that cannot be set per element. Other global settings
 affect the properties of decorative objects, i.e., objects such as contact points and force
 arrows which do not correspond to model elements. The visual settings are grouped semantically
 into several subsections.

 This element is a good candidate for the file include mechanism. One can create an XML file
 with coordinated visual settings corresponding to a \"theme\", and then include this file in
 multiple models.

## visual/headlight

**Path**: `visual/headlight`
**Tag**: `headlight`
**Parent**: `visual`
**Children**: none
**Rust Type**: `model::visual::HeadLight`

Properties of the headlight used during visualization.

 There is always a built-in headlight, in addition to any lights explicitly defined in the
 model. The headlight is a directional light centered at the current camera and pointed in
 the direction in which the camera is looking. It does not cast shadows (which would be
 invisible anyway).

Note

 Lights are additive, so if explicit lights are defined in the model, the intensity of the
 headlight would normally need to be reduced.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `ambient` | `real(3)` | yes | `""` | The ambient component of the headlight, in the sense of OpenGL. The alpha component is  set to 1 and cannot be adjusted. |
| `diffuse` | `real(3)` | yes | `""` | The diffuse component of the headlight, in the sense of OpenGL. |
| `specular` | `real(3)` | yes | `""` | The specular component of the headlight, in the sense of OpenGL. |
| `active` | `int` | yes | `0` | Enables or disables the headlight. A value of 0 means disabled; any other value means  enabled. |

## visual/global

**Path**: `visual/global`
**Tag**: `global`
**Parent**: `visual`
**Children**: none
**Rust Type**: `model::visual::VisualGlobal`

Miscellaneous global settings for the visualizer.

 While all visual settings are global, the settings here could not be fit into any of the
 other subsections. So this is effectively a miscellaneous subsection.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `orthographic` | `bool` | yes | `false` | Whether the free camera uses a perspective projection (false) or an orthographic  projection (true). Setting this attribute changes the semantic of the fovy attribute. |
| `fovy` | `real` | yes | `0.0` | The vertical field of view of the free camera, i.e., the camera that is always available  in the visualizer even if no cameras are explicitly defined in the model. If the camera  uses a perspective projection, the field-of-view is expressed in degrees, regardless of  the global compiler/angle setting. If the camera uses an orthographic projection, the  field-of-view is expressed in units of length. In either case, the horizontal field of  view is computed automatically given the window size and the vertical field of view. |
| `azimuth` | `real` | yes | `0.0` | The initial azimuth of the free camera around the vertical z-axis, in degrees. A value  of 0 corresponds to looking in the positive x direction, while the value of 90  corresponds to looking in the positive y direction. The look-at point itself is specified  by the statistic/center attribute, while the distance from the look-at point is  controlled by the statistic/extent attribute. |
| `elevation` | `real` | yes | `0.0` | The initial elevation of the free camera with respect to the lookat point. Since this is  a rotation around a vector parallel to the camera's X-axis (right in pixel space),  negative numbers correspond to moving the camera up from the horizontal plane, and  vice-versa. The look-at point itself is specified by the statistic/center attribute,  while the distance from the look-at point is controlled by the statistic/extent  attribute. |

## visual/quality

**Path**: `visual/quality`
**Tag**: `quality`
**Parent**: `visual`
**Children**: none
**Rust Type**: `model::visual::Quality`

Settings that affect the quality of rendering.

 Larger values result in higher quality but possibly slower speed.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `shadowsize` | `int` | yes | `1024` | This attribute specifies the size of the square texture used for directional and spot light  shadow mapping. Higher values result is smoother shadows. The size of the area over  which a light can cast shadows also affects smoothness, so these settings should be  adjusted jointly. |
| `pointshadowsize` | `int` | yes | `512` | This attribute specifies the size of the square texture used for point light shadow  mapping. Higher values result is smoother shadows. The size of the area over which a  light can cast shadows also affects smoothness, so these settings should be adjusted  jointly. |

## visual/map

**Path**: `visual/map`
**Tag**: `map`
**Parent**: `visual`
**Children**: none
**Rust Type**: `model::visual::Mapping`

Scaling quantities and fog settings that affect both visualization and built-in mouse
 perturbations.

 This element is used to specify scaling quantities that affect both the visualization and
 built-in mouse perturbations. Unlike the scaling quantities in the scale element which are
 specific to spatial extent, the quantities here are miscellaneous.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `fogstart` | `real` | yes | `0.0` | The start position of the linear fog, as a multiplier of the model extent. The visualizer  can simulate linear fog, in the sense of OpenGL. The start position of the fog is the  model extent multiplied by the value of this attribute. |
| `fogend` | `real` | yes | `0.0` | The end position of the linear fog, as a multiplier of the model extent. The end position  of the fog is the model extent multiplied by the value of this attribute. |
| `znear` | `real` | yes | `0.0` | The distance to the near clipping plane as a multiplier of the model extent. Setting it  too close causes loss of resolution in the depth buffer, while setting it too far causes  objects of interest to be clipped. Must be strictly positive. |
| `zfar` | `real` | yes | `0.0` | The distance to the far clipping plane as a multiplier of the model extent. |
| `envmapintensity` | `real` | yes | `0.0` | [MPEX] Intensity of the environment map. |

## visual/rgba

**Path**: `visual/rgba`
**Tag**: `rgba`
**Parent**: `visual`
**Children**: none
**Rust Type**: `model::visual::VisualColor`

Color and transparency settings for various decorative objects in the visualizer.

 The settings in this element control the color and transparency (rgba) of various decorative
 objects. All values should be in the range [0 1]. An alpha value of 0 disables the rendering
 of the corresponding object.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `fog` | `real(4)` | yes | `""` | When fog is enabled, the color of all pixels fades towards the color specified here. The  spatial extent of the fading is controlled by the fogstart and fogend attributes of the  map element. |
| `haze` | `real(4)` | no | — | Haze color at the horizon, used to transition between an infinite plane and a skybox  smoothly. To create a seamless transition, make sure the skybox colors near the horizon  are similar to the plane color/texture, and set the haze color somewhere in that color  gamut. |
| `joint` | `real(4)` | yes | `""` | Color of the arrows used to render joint axes. If a joint is limited and the joint value  exceeds the limit, the constraint impedance is used to mix this color and the constraint  color. |
| `bv` | `real(4)` | yes | `""` | Color used to render bounding volumes. |
| `contactforce` | `real(4)` | yes | `""` | Color of the arrows used to render contact forces. When splitting of contact forces into  normal and tangential components is enabled, this color is used to render the normal  components. |

## visual/probe [MPEX]

**Path**: `visual/probe`
**Tag**: `probe`
**Parent**: `visual`
**Children**: none
**Rust Type**: `model::visual::Probe`

Reflection probe settings.

 Defines an image-based lighting probe used for reflections in the visualizer.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `texture` | `string` | no | — | [MPEX] Texture asset name used as the reflection source for this probe. |
| `position` | `real(3)` | yes | `"0.0 0.0 0.0"` | [MPEX] Position of the probe in world space. |
| `scale` | `real(3)` | yes | `"1.0 1.0 1.0"` | [MPEX] Scale of the probe's influence volume. |

## visual/ssao [MPEX]

**Path**: `visual/ssao`
**Tag**: `ssao`
**Parent**: `visual`
**Children**: none
**Rust Type**: `model::visual::Ssao`

Screen-space ambient occlusion (SSAO) settings.

 Controls SSAO post-processing effect in the visualizer.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `active` | `bool` | yes | `false` | [MPEX] Whether SSAO post-processing is active. |

## visual/ssgi [MPEX]

**Path**: `visual/ssgi`
**Tag**: `ssgi`
**Parent**: `visual`
**Children**: none
**Rust Type**: `model::visual::Ssgi`

Screen-space global illumination (SSGI) settings.

 Controls SSGI post-processing effect in the visualizer.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `active` | `bool` | yes | `false` | [MPEX] Whether SSGI post-processing is active. |
| `resolutionscale` | `int` | yes | `0` | [MPEX] Control the quality of the fast GI lighting.  Higher resolution scale uses less memory (buffer size = 1 / resolutionscale).  Value in 1, 2, 4 input other value will set as 2 |
| `raycount` | `int` | yes | `0` | [MPEX] Amount of GI ray to trace for each pixel |
| `stepcount` | `int` | yes | `0` | [MPEX] Amount of screen sample per GI ray |
| `thickness` | `real` | yes | `0.0` | [MPEX] Geometric thickness of the surfaces when computing fast GI and ambient occlusion.  Reduces light leaking and missing contact occlusion. |
| `intensity` | `real` | yes | `0.0` | [MPEX] GI intensity. |
| `gidenoiseoffset` | `int` | yes | `0` | [MPEX] GI denoise pixel offset size, 0 mean no denoise. |
| `rraycount` | `int` | yes | `0` | [MPEX] Amount of screen sample per reflection ray |
| `rdenoiseoffset` | `int` | yes | `0` | [MPEX] Reflection denoise pixel offset size, 0 mean no denoise. |

## visual/tonemapping [MPEX]

**Path**: `visual/tonemapping`
**Tag**: `tonemapping`
**Parent**: `visual`
**Children**: none
**Rust Type**: `model::visual::Tonemapping`

Tonemapping settings.

 Controls the tonemapping method applied during rendering.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `method` | `string` | yes | `"none"` | [MPEX] The tonemapping method to apply during rendering. Choice: `none`, `aces`. |

