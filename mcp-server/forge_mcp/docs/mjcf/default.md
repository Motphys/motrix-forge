# default

**Path**: `default`
**Tag**: `default`
**Parent**: `mujoco`
**Children**: `default/default`, `default/geom`, `default/joint`, `default/light`, `default/mesh`, `default/material`, `default/general`, `default/motor`, `default/position`, `default/velocity`, `default/adhesion`, `default/camera`, `default/site`, `default/pair`, `default/tendon`, `default/equality`
**Rust Type**: `model::default_::DefaultClass`

This element is used to define default settings for various model elements.
 For each `Option` field, generate a `apply_default` method to merge with default class
 You should compile this struct into `DefaultMap` which is input of `apply_default`

## Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `class` | `string` | no | — | Name of the default class. |

## default/default

**Path**: `default/default`
**Tag**: `default`
**Parent**: `default`
**Children**: none
**Defaults Target**: `default`
**Rust Type**: `model::default_::DefaultClass`

This block documents the defaults context for `default`. The element semantics and attributes are inherited from the defaults target.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `class` | `string` | no | — | Name of the default class. |

## default/geom

**Path**: `default/geom`
**Tag**: `geom`
**Parent**: `default`
**Children**: none
**Defaults Target**: `body/geom`
**Rust Type**: `model::body::geom::Geom`

This block documents the defaults context for `body/geom`. The element semantics and attributes are inherited from the defaults target.

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

## default/joint

**Path**: `default/joint`
**Tag**: `joint`
**Parent**: `default`
**Children**: none
**Defaults Target**: `body/joint`
**Rust Type**: `model::body::joint::Joint`

This block documents the defaults context for `body/joint`. The element semantics and attributes are inherited from the defaults target.

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

## default/light

**Path**: `default/light`
**Tag**: `light`
**Parent**: `default`
**Children**: none
**Defaults Target**: `body/light`
**Rust Type**: `model::body::light::Light`

This block documents the defaults context for `body/light`. The element semantics and attributes are inherited from the defaults target.

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

## default/mesh

**Path**: `default/mesh`
**Tag**: `mesh`
**Parent**: `default`
**Children**: none
**Defaults Target**: `asset/mesh`
**Rust Type**: `model::asset::Mesh`

This block documents the defaults context for `asset/mesh`. The element semantics and attributes are inherited from the defaults target.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | yes | — | Name of the mesh, used for referencing. If omitted, the mesh name equals  the file name without the path and extension. |
| `class` | `string` | no | — | Defaults class for setting unspecified attributes (only scale in this case). |
| `file` | `string` | no | — | The file from which the mesh will be loaded. The path is determined as  described in the meshdir attribute of the compiler element. The file  extension must be \"stl\", \"obj\", \"gltf\", \"glb\", or \"dae\" (not case  sensitive) specifying the file type. If the file name is omitted, the  vertex attribute becomes required. |
| `scale` | `real(3)` | no | — | This attribute specifies the scaling that will be applied to the vertex  data along each coordinate axis. Negative values are allowed, resulting  in flipping the mesh along the corresponding axis. |
| `vertex` | `string` | no | — | Vertex 3D position data. You can specify position data in the XML using  this attribute, or using a binary file, but not both. |
| `texcoord` | `string` | no | — | Vertex 2D texture coordinates, which are numbers between 0 and 1. If  specified, the number of texture coordinate pairs must equal the number  of vertices. |
| `normal` | `string` | no | — | Vertex 3D normal data. If specified, the number of normals must equal  the number of vertices. The model compiler normalizes the normals  automatically. |
| `face` | `string` | no | — | Faces of the mesh. Each face is a sequence of 3 vertex indices, in  counter-clockwise order. The indices must be integers between 0 and  nvert-1. |
| `refpos` | `real(3)` | no | — | Reference position relative to which the 3D vertex coordinates are  defined. This vector is subtracted from the positions. |
| `refquat` | `real(4)` | no | — | Reference orientation relative to which the 3D vertex coordinates and  normals are defined. The conjugate of this quaternion is used to rotate  the positions and normals. The model compiler normalizes the quaternion  automatically. |
| `acd` | `bool` | yes | `false` | [MPEX] Override whether this mesh asset participates in convex decomposition. |

## default/material

**Path**: `default/material`
**Tag**: `material`
**Parent**: `default`
**Children**: none
**Defaults Target**: `asset/material`
**Rust Type**: `model::asset::Material`

This block documents the defaults context for `asset/material`. The element semantics and attributes are inherited from the defaults target.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the material, used for referencing. |
| `class` | `string` | no | — | Defaults class for setting unspecified attributes. |
| `rgba` | `real(4)` | yes | `"1. 1. 1. 1."` | Color and transparency of the material. All components should be in the  range [0 1]. Note that the texture color (if assigned) and the color  specified here are multiplied component-wise. Thus the default value of  \"1 1 1 1\" has the effect of leaving the texture unchanged. When the  material is applied to a model element which defines its own local rgba  attribute, the local definition has precedence. The remaining material  properties always apply. |
| `texture` | `string` | no | — | If this attribute is specified, the material has a texture associated  with it. Referencing the material from a model element will cause the  texture to be applied to that element. The value of this attribute is  the name of a texture asset, not a texture file name. Textures cannot  be loaded in the material definition; instead they must be loaded  explicitly via the texture element and then referenced here. The  texture referenced here is used for specifying the RGB values. For  advanced rendering (e.g., Physics-Based Rendering), more texture types  need to be specified. In that case, this texture attribute should be  omitted, and the texture types should be specified using layer child  elements. The built-in renderer supports PBR, so these advanced  rendering features can be rendered directly once the corresponding  texture types are provided via the layer child elements. |
| `texuniform` | `bool` | yes | `false` | For cube textures, this attribute controls how cube mapping is applied.  The value \"false\" means apply cube mapping directly, using the actual  size of the object. The value \"true\" maps the texture to a unit object  before scaling it to its actual size. For 2d textures, this attribute  interacts with texrepeat: when \"false\", the 2d texture is repeated N  times over the object; when \"true\", the texture is repeated N times  over one spatial unit, regardless of object size. |
| `texrepeat` | `real(2)` | yes | `"1. 1."` | This attribute applies to textures of type \"2d\". It specifies how many  times the texture image is repeated, relative to either the object size  or the spatial unit, as determined by the texuniform attribute. |
| `reflectance` | `real` | yes | `0.0` | This attribute should be in the range [0 1]. It controls the specular  reflectance of the material in the built-in physically-based renderer:  the larger the value, the stronger the reflection. Unlike a planar  mirror, it is a per-material property and applies to every geom that  references this material, regardless of the geom shape. |
| `metallic` | `real` | yes | `0.0` | This attribute corresponds to uniform metallicity coefficient applied to  the entire material, used by the built-in physically-based renderer. If a  non-negative value is specified, this metallic value should be multiplied by the  metallic texture sampled value to obtain the final metallicity of the material. |
| `roughness` | `real` | yes | `0.0` | This attribute corresponds to uniform roughness coefficient applied to  the entire material, used by the built-in physically-based renderer. If a  non-negative value is specified, this roughness value should be multiplied by the  roughness texture sampled value to obtain the final roughness of the material. |
| `emission` | `real(4)` | yes | `"0. 0. 0. 0."` | Emissive color of the material in RGBA format. The emissive contribution  is this color scaled by the emissionintensity attribute. Use  emissionintensity to control the overall strength of the emission. |
| `emissionintensity` | `real` | yes | `0.0` | [MPEX] Emission intensity multiplier applied on top of the emission color. |
| `detailpara` | `real(4)` | yes | `"1. 1. 1. 1."` | [MPEX] Detail normal map parameters packed as four  floats: x = detail normal map u scale, y = detail normal map v scale,  z = normal strength, w = padding. |
| `depthbias` | `int` | yes | `0` | [MPEX] Depth bias for rendering. |
| `castshadow` | `bool` | yes | `true` | [MPEX] Whether geometries using this material cast shadows. |

## default/general

**Path**: `default/general`
**Tag**: `general`
**Parent**: `default`
**Children**: none
**Defaults Target**: `actuator/general`
**Rust Type**: `model::actuator::General`

This block documents the defaults context for `actuator/general`. The element semantics and attributes are inherited from the defaults target.

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

## default/motor

**Path**: `default/motor`
**Tag**: `motor`
**Parent**: `default`
**Children**: none
**Defaults Target**: `actuator/motor`
**Rust Type**: `model::actuator::Motor`

This block documents the defaults context for `actuator/motor`. The element semantics and attributes are inherited from the defaults target.

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

## default/position

**Path**: `default/position`
**Tag**: `position`
**Parent**: `default`
**Children**: none
**Defaults Target**: `actuator/position`
**Rust Type**: `model::actuator::Position`

This block documents the defaults context for `actuator/position`. The element semantics and attributes are inherited from the defaults target.

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

## default/velocity

**Path**: `default/velocity`
**Tag**: `velocity`
**Parent**: `default`
**Children**: none
**Defaults Target**: `actuator/velocity`
**Rust Type**: `model::actuator::Velocity`

This block documents the defaults context for `actuator/velocity`. The element semantics and attributes are inherited from the defaults target.

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

## default/adhesion

**Path**: `default/adhesion`
**Tag**: `adhesion`
**Parent**: `default`
**Children**: none
**Defaults Target**: `actuator/adhesion`
**Rust Type**: `model::actuator::Adhesion`

This block documents the defaults context for `actuator/adhesion`. The element semantics and attributes are inherited from the defaults target.

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

## default/camera

**Path**: `default/camera`
**Tag**: `camera`
**Parent**: `default`
**Children**: none
**Defaults Target**: `body/camera`
**Rust Type**: `model::body::camera::Camera`

This block documents the defaults context for `body/camera`. The element semantics and attributes are inherited from the defaults target.

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

## default/site

**Path**: `default/site`
**Tag**: `site`
**Parent**: `default`
**Children**: none
**Defaults Target**: `body/site`
**Rust Type**: `model::body::site::Site`

This block documents the defaults context for `body/site`. The element semantics and attributes are inherited from the defaults target.

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

## default/pair

**Path**: `default/pair`
**Tag**: `pair`
**Parent**: `default`
**Children**: none
**Defaults Target**: `contact/pair`
**Rust Type**: `model::contact::Pair`

This block documents the defaults context for `contact/pair`. The element semantics and attributes are inherited from the defaults target.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of this contact pair. |
| `class` | `string` | no | — | Defaults class for setting unspecified attributes. |
| `geom1` | `string` | yes | `""""` | The name of the first geom in the pair. |
| `geom2` | `string` | yes | `""""` | The name of the second geom in the pair. The contact force vector computed by the solver  points from the first towards the second geom by convention.  The forces applied to the system are of course equal and opposite, so the order of geoms  does not affect the physics. |
| `condim` | `int` | yes | `3` | The dimensionality of the contacts generated by this geom pair. |
| `friction` | `real(n)` | yes | `"1.0 1.0 0.005 0.0001 0.0001"` | The friction coefficients of the contacts generated by this geom pair. Making the first two  coefficients different results in anisotropic tangential friction. Making the last two  coefficients different results in anisotropic rolling friction. At most five components can  be authored. Missing prefix components are inherited from the selected class, parent  defaults or built-in defaults. The current runtime consumes the first tangential, torsional  and first rolling components as sliding, spinning and rolling coefficients, respectively.  The second tangential and second rolling components are currently preserved but not  consumed. |
| `solref` | `real(2)` | yes | `"0.02 1.0"` | Solver reference parameters for contact simulation. Exactly two values must be authored.  → See [solver parameters](#solver-attrs-solref). |
| `solimp` | `real(5)` | yes | `"0.9 0.95 0.001 0.5 2.0"` | Solver impedance parameters for contact simulation. Exactly five values must be authored. |
| `solreffriction` | `real(2)` | yes | `"0.0 0.0"` | Solver reference parameters for friction dimensions. Exactly two values must be authored.  In MJCF, this attribute has the same semantics as other solref attributes, with two  important distinctions: the default value of \"0 0\" means \"use the same values as  solref\", and this attribute only takes effect for elliptic friction cones, since  pyramidal cones mix normal and frictional forces.  → See [solver parameters](#solver-attrs-solref).  MotrixSim currently compiles \"0 0\" as no independent friction model and preserves non-zero  values as an independent model, but the pyramidal-friction runtime does not consume either  form. |
| `margin` | `real` | yes | `0.0` | Distance threshold below which contacts are detected and included in the global array  the contact data. |
| `gap` | `real` | yes | `0.0` | Used to enable the generation of inactive contacts, i.e., contacts that are ignored by the  constraint solver but are included in the contact data for the purpose of custom  computations. When this value is positive, geom distances between margin and margin-gap  correspond to such inactive contacts. |

## default/tendon

**Path**: `default/tendon`
**Tag**: `tendon`
**Parent**: `default`
**Children**: none
**Defaults Target**: `tendon`
**Rust Type**: `model::tendon::Tendon`

This block documents the defaults context for `tendon`. The element semantics and attributes are inherited from the defaults target.

## default/equality

**Path**: `default/equality`
**Tag**: `equality`
**Parent**: `default`
**Children**: none
**Defaults Target**: `equality`
**Rust Type**: `model::equality::EqualitySet`

This block documents the defaults context for `equality`. The element semantics and attributes are inherited from the defaults target.

