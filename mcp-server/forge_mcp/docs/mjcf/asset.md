# asset

**Path**: `asset`
**Tag**: `asset`
**Parent**: `mujoco`
**Children**: `asset/material`, `asset/mesh`, `asset/texture`, `asset/hfield`, `asset/gsplat`, `asset/model`, `asset/lidar`
**Rust Type**: `model::asset::Asset`

This is a grouping element for defining assets. It does not have
 attributes. Assets are created in the model so that they can be
 referenced from other model elements. Assets opened from a file can
 be identified in two different ways: filename extensions or the
 `content_type` attribute. The parser will attempt to open a file
 specified by the content type provided, and only defaults to the
 filename extension if no `content_type` attribute is specified. The
 content type is ignored if the asset is not loaded from a file.

## asset/material

**Path**: `asset/material`
**Tag**: `material`
**Parent**: `asset`
**Children**: `asset/material/layer`
**Rust Type**: `model::asset::Material`

This element creates a material asset. It can be referenced from
 skins, geoms, sites and tendons to set their appearance. Note that
 all these elements also have a local rgba attribute, which is more
 convenient when only colors need to be adjusted, because it does not
 require creating materials and referencing them. Materials are useful
 for adjusting appearance properties beyond color. However once a
 material is created, it is more natural to specify the color using
 the material, so that all appearance properties are grouped together.

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

## asset/mesh

**Path**: `asset/mesh`
**Tag**: `mesh`
**Parent**: `asset`
**Children**: none
**Rust Type**: `model::asset::Mesh`

This element creates a mesh asset, which can then be referenced from geoms.
 If the referencing geom type is \"mesh\" the mesh is instantiated in the
 model, otherwise a geometric primitive is automatically fitted to it.

 The parser works with triangulated meshes. They can be loaded from binary
 STL files, OBJ files, glTF/GLB files or COLLADA (.dae) files, or vertex and
 face data can be specified directly in the XML. The legacy MSH binary mesh
 format is not supported; convert such meshes to OBJ or glTF. While any
 collection of triangles can be loaded as a mesh and rendered, collision
 detection works with the convex hull of the mesh. The mesh appearance
 (including texture mapping) is controlled by the material and rgba attributes
 of the referencing geom.

 Meshes can have explicit texture coordinates instead of relying on the
 automated texture mapping mechanism. When provided, these explicit
 coordinates have priority. Texture coordinates can be specified with OBJ and
 glTF files, as well as explicitly in the XML with the texcoord attribute, but
 not via STL files.

 The size of the mesh is determined by the 3D coordinates of the vertex data
 multiplied by the components of the scale attribute. Scaling is applied
 separately for each coordinate axis. Negative scaling values can be used to
 flip the mesh.

Note

 Vertex data in source assets is often relative to coordinate frames whose
 origin is not inside the mesh. This is resolved by centering the mesh at
 compile time. The translation and rotation offsets are saved for use when
 re-applying the transform. Positioning and orienting is done by the
 referencing geom, while sizing (scale) is done by the mesh asset itself.

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

## asset/texture

**Path**: `asset/texture`
**Tag**: `texture`
**Parent**: `asset`
**Children**: none
**Rust Type**: `model::asset::Texture`

This element creates a texture asset, which is then referenced from a
 material asset, which is finally referenced from a model element that
 needs to be textured.

 The texture data can be loaded from files or can be generated by the
 compiler as a procedural texture. Because different texture types require
 different parameters, only a subset of the attributes below are used for
 any given texture. Currently, three file formats are supported for loading
 textures: PNG, KTX, and a custom MSH texture format. The loader will
 use the extension of the file name to determine which format to use,
 defaulting to the custom format if the extension is not recognized.

Note

 As with all other assets, a texture must have a name in order to be
 referenced. However if the texture is loaded from a single file with the
 file attribute, the explicit name can be omitted and the file name (without
 the path and extension) becomes the texture name. If the name after parsing
 is empty and the texture type is not \"skybox\", the compiler will generate
 an error.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the texture, used for referencing. If omitted, the texture name  equals the file name without the path and extension. |
| `file` | `string` | no | — | If this attribute is specified, and the builtin attribute is set to  \"none\", the texture data is loaded from a single file. See the  texturedir attribute of the compiler element regarding the file path. |
| `builtin` | `string` | yes | `"none"` | Controls the generation of procedural textures. If the value is  different from \"none\", the texture is treated as procedural and any file  names are ignored. Choice: `none`, `gradient`, `checker`, `flat`, `dynamic`. |
| `type` | `string` | yes | `"cube"` | This attribute determines how the texture is represented and mapped to  objects. It also determines which of the remaining attributes are  relevant. Choice: `cube`, `2d`, `skybox`, `envhdr`, `envdiff`, `envspec`, `probe`. |
| `rgb1` | `real(3)` | yes | `"0.8 0.8 0.8"` | The first color used for procedural texture generation. This color is  also used to fill missing sides of cube and skybox textures loaded from  files. The components should be in the range [0 1]. |
| `rgb2` | `real(3)` | yes | `"0.5 0.5 0.5"` | The second color used for procedural texture generation. |
| `width` | `real` | yes | `0.0` | The width of a procedural texture, i.e., the number of columns in the  image. Larger values usually result in higher quality images. For  textures loaded from files, this attribute is ignored. |
| `height` | `real` | no | — | The height of the procedural texture, i.e., the number of rows in the  image. For cube and skybox textures, this attribute is ignored and the  height is set to 6 times the width. For textures loaded from files, this  attribute is ignored. |
| `colorspace` | `string` | no | — | This attribute determines the color space of the texture. When set,  overrides the color space information embedded in the image file. Choice: `sRGB`, `linear`. |
| `mark` | `string` | no | — | Procedural textures can be marked with the markrgb color, on top of the  colors determined by the builtin type. \"edge\" means that the edges of  all texture images are marked. \"cross\" means that a cross is marked in  the middle of each image. \"random\" means that randomly chosen pixels are  marked. All markings are one-pixel wide. Choice: `none`, `edge`, `cross`, `random`. |
| `markrgb` | `real(3)` | no | — | The color used for procedural texture markings. |
| `nchannel` | `int` | yes | `3` | The number of channels in the texture image file. This allows loading  4-channel textures (RGBA) or single-channel textures (e.g., for  Physics-Based Rendering properties such as roughness or metallic). |
| `gridsize` | `real(2)` | no | — |  |
| `gridlayout` | `string` | no | — |  |

## asset/hfield

**Path**: `asset/hfield`
**Tag**: `hfield`
**Parent**: `asset`
**Children**: none
**Rust Type**: `model::asset::HField`

This element creates a height field asset, which can then be referenced
 from geoms with type \"hfield\". A height field, also known as a terrain map,
 is a 2D matrix of elevation data. The data can be specified by loading from
 a PNG file (where pixel intensity maps to elevation), loading from a binary
 file in a custom format, or by providing inline elevation data via the
 elevation attribute.

 Regardless of which method is used to specify the elevation data, the
 compiler always normalizes it to the range [0 1].

 The position and orientation of the height field is determined by the geom
 that references it. The spatial extent is specified by the height field
 asset itself via the size attribute, and cannot be modified by the
 referencing geom (the geom size parameters are ignored in this case).

Note

 For collision detection, a height field is treated as a union of triangular
 prisms. The number of possible contacts between a height field and a geom
 is limited to 50; any contacts beyond that are discarded. To avoid
 penetration due to discarded contacts, the spatial features of the height
 field should be large compared to the geoms it collides with. Collisions
 between height fields and other height fields or planes are not supported.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the height field, used for referencing. If the name is omitted  and a file name is specified, the height field name equals the file name  without the path and extension. |
| `content_type` | `string` | no | — | If the file attribute is specified, this sets the Media Type (formerly  known as MIME type) of the file to be loaded. Any filename extensions  will be overloaded. Currently \"image/png\" and  \"image/vnd.mujoco.hfield\" are supported. |
| `file` | `string` | no | — | If this attribute is specified, the elevation data is loaded from the  given file. If the file extension is \".png\" (not case-sensitive), the  file is treated as a PNG file. Otherwise it is treated as a binary file  in the custom format. The number of rows and columns in the data are  determined from the file contents. Loading data from a file and setting  nrow or ncol to non-zero values results in a compile error. |
| `nrow` | `int` | yes | `0` | Specifies the number of rows in the elevation data matrix. A value of 0 means  that the data will be loaded from a file, which will be used to infer  the size of the matrix. |
| `ncol` | `int` | yes | `0` | This attribute specifies the number of columns in the elevation data  matrix. |
| `elevation` | `real(n)` | no | — | This attribute specifies the elevation data matrix. Values are  automatically normalized to lie between 0 and 1 by first subtracting  the minimum value and then dividing by the (maximum-minimum) difference.  If not provided, values are set to 0. Note that the row order in the model  is flipped with respect to the order in XML, i.e., it is bottom-to-top. |
| `size` | `real(4)` | yes | `""` | The four numbers here are (radius_x, radius_y, elevation_z, base_z).  The height field is centered at the referencing geom's local frame.  Elevation is in the +Z direction. The first two numbers specify the X  and Y extent (or \"radius\") of the rectangle over which the height field  is defined. The third number is the maximum elevation; it scales the  elevation data which is normalized to [0-1], so the minimum elevation  is at Z=0 and the maximum is at Z=elevation_z. The last number is the  depth of a box in the -Z direction serving as a \"base\" for the height  field, ensuring non-zero thickness at places where the normalized  elevation data is zero. |

## asset/gsplat [PRO]

**Path**: `asset/gsplat`
**Tag**: `gsplat`
**Parent**: `asset`
**Children**: none
**Rust Type**: `model::asset::GaussianCloud`

This element creates a reusable Gaussian cloud asset.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | yes | `""""` | [PRO] Name used by body and world Gaussian cloud instances. |
| `file` | `string` | yes | `""""` | [PRO] Gaussian cloud file path. |
| `content_type` | `string` | no | — | [PRO] Optional media type of the Gaussian cloud file. |

## asset/model

**Path**: `asset/model`
**Tag**: `model`
**Parent**: `asset`
**Children**: none
**Rust Type**: `model::asset::Model`

This element specifies other MJCF models which may be used for attachment
 in the current model.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the sub-model, used for referencing in attach. If unspecified,  the model name from the sub-model's root element is used. |
| `file` | `string` | yes | `""""` | The file from which the sub-model will be loaded. The sub-model must be  a valid MJCF model. |

## asset/lidar [MPEX]

**Path**: `asset/lidar`
**Tag**: `lidar`
**Parent**: `asset`
**Children**: none
**Rust Type**: `model::sensor::sensors::LidarAsset`

A reusable lidar model profile referenced by `sensor/lidar`.

Note

 This is a MotrixSim extension to MJCF. It contains reusable model and scan attributes. Sensor
 identity, mounting site, asset reference, self-filter policy, and scan rate remain on the sensor
 instance.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | yes | `""""` | [MPEX] Name used by sensor instances to reference this profile. |
| `cutoff` | `real` | yes | `100.0` | [MPEX] Maximum ray distance in meters. |
| `pattern` | `string` | yes | `"grid"` | [MPEX] Geometric scan pattern. Choice: `grid`, `rings`. |
| `hscan` | `int` | yes | `1` | [MPEX] Number of horizontal azimuth samples for grid and rings patterns. |
| `vscan` | `int` | yes | `1` | [MPEX] Number of vertical elevation samples for the grid pattern. |
| `hrange` | `real(2)` | yes | `"0.0 0.0"` | [MPEX] Horizontal azimuth range in degrees. |
| `vrange` | `real(2)` | yes | `"0.0 0.0"` | [MPEX] Vertical elevation range in degrees for the grid pattern. |
| `elevations` | `real(n)` | no | — | [MPEX] Elevation angles in degrees for the rings pattern. |
| `reportrate` | `real` | no | — | [MPEX] Number of horizontal columns reported per second, used to derive `hscan` from `hz`. |
| `hzrange` | `real(2)` | no | — | [MPEX] Supported inclusive full-scan frequency range in hertz; equal endpoints fix the frequency. |

