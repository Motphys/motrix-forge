# compiler

**Path**: `compiler`
**Tag**: `compiler`
**Parent**: `mujoco`
**Children**: none
**Rust Type**: `model::compiler::Compiler`

This element is used to set options for the built-in parser and
 compiler. After parsing and compilation it no longer has any effect. The
 settings here are global and apply to the entire model.

## Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `angle` | `string` | yes | `"degree"` | This attribute specifies whether the angles in the MJCF model are  expressed in units of degrees or radians. The compiler converts degrees  into radians internally. For URDF models the parser sets this attribute  to \"radian\" internally, regardless of the XML setting. Choice: `radian`, `degree`. |
| `eulerseq` | `string` | yes | `"xyz"` | This attribute specifies the sequence of Euler rotations for all  euler attributes of elements that have spatial frames. This must be a  string with exactly 3 characters from the set {x, y, z, X, Y, Z}. The  character at position n determines the axis around which the n-th  rotation is performed. Lower case letters denote axes that rotate with  the frame (intrinsic), while upper case letters denote axes that remain  fixed in the parent frame (extrinsic). The \"rpy\" convention used in  URDF corresponds to \"XYZ\" in MJCF. Choice: `zyx`, `zxy`, `yxz`, `yzx`, `xyz`, `xzy`. |
| `meshdir` | `string` | no | — | This attribute instructs the compiler where to look for mesh and height  field files. The full path to a file is determined as follows. If the  strippath attribute is \"true\", all path information from the file name  is removed. The following checks are then applied in order: (1) if the  file name contains an absolute path, it is used without further changes;  (2) if this attribute is set and contains an absolute path, the full  path is the string given here appended with the file name; (3) the full  path is the path to the main MJCF model file, appended with the value  of this attribute if specified, appended with the file name. |
| `assetdir` | `string` | no | — | This attribute sets the values of both meshdir and texturedir. Values  in the latter attributes take precedence over assetdir. |
| `texturedir` | `string` | no | — | This attribute is used to instruct the compiler where to look for  texture files. It works in the same way as meshdir. |
| `autolimits` | `bool` | yes | `true` | This attribute affects the behavior of attributes such as \"limited\" (on  body-joint or tendon), \"forcelimited\", \"ctrllimited\", and \"actlimited\"  (on actuator). If \"true\", these attributes are unnecessary and their  value will be inferred from the presence of their corresponding \"range\"  attribute. If \"false\", no such inference will happen: for a joint to be  limited, both limited=\"true\" and range=\"min max\" must be specified. In  this mode, it is an error to specify a range without a limit. |
| `fitaabb` | `bool` | yes | `false` | The compiler is able to replace a mesh with a geometric primitive fitted  to that mesh. If this attribute is \"true\", the fitting procedure uses the  axis-aligned bounding box (AABB) of the mesh, choosing the smallest  primitive whose AABB contains the mesh AABB. Otherwise it uses the  equivalent-inertia box of the mesh. The type of geometric primitive used  for fitting is specified separately for each geom. |
| `compress` | `bool` | yes | `false` | [MPEX] Motphys Only: Whether to compress textures at load time. When `true`, D2  textures are runtime-compressed to a GPU block-compressed format (BC3 on  native) to reduce GPU memory (~1/4). Off by default to keep texture  ready/display latency low. |

