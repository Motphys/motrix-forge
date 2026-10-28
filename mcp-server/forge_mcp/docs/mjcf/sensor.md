# sensor

**Path**: `sensor`
**Tag**: `sensor`
**Parent**: `mujoco`
**Children**: `sensor/touch`, `sensor/accelerometer`, `sensor/velocimeter`, `sensor/gyro`, `sensor/force`, `sensor/torque`, `sensor/jointpos`, `sensor/jointvel`, `sensor/jointactuatorfrc`, `sensor/ballquat`, `sensor/ballangvel`, `sensor/jointlimitpos`, `sensor/jointlimitvel`, `sensor/jointlimitfrc`, `sensor/tendonpos`, `sensor/tendonvel`, `sensor/tendonlimitpos`, `sensor/tendonlimitvel`, `sensor/tendonlimitfrc`, `sensor/actuatorpos`, `sensor/actuatorvel`, `sensor/actuatorfrc`, `sensor/framepos`, `sensor/framequat`, `sensor/framexaxis`, `sensor/frameyaxis`, `sensor/framezaxis`, `sensor/framelinvel`, `sensor/frameangvel`, `sensor/framelinacc`, `sensor/frameangacc`, `sensor/subtreecom`, `sensor/subtreelinvel`, `sensor/subtreeangmom`, `sensor/distance`, `sensor/normal`, `sensor/fromto`, `sensor/contact`, `sensor/lidar`
**Rust Type**: `model::sensor::sensor_set::SensorSet`

This element is a grouping element for sensors.

## sensor/touch

**Path**: `sensor/touch`
**Tag**: `touch`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorSite`

Common sensor data for sensors that attach to a site.

 This type is shared by site-based sensors such as touch, accelerometer, velocimeter,
 gyro, force, torque, and magnetometer. The active sensing zone or measurement origin
 is defined by the named site, and the sensor uses the site's position and orientation.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `site` | `string` | yes | `""""` | The name of the site where the sensor is mounted. The sensor is centered and aligned  with the site local frame. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/accelerometer

**Path**: `sensor/accelerometer`
**Tag**: `accelerometer`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorSite`

Common sensor data for sensors that attach to a site.

 This type is shared by site-based sensors such as touch, accelerometer, velocimeter,
 gyro, force, torque, and magnetometer. The active sensing zone or measurement origin
 is defined by the named site, and the sensor uses the site's position and orientation.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `site` | `string` | yes | `""""` | The name of the site where the sensor is mounted. The sensor is centered and aligned  with the site local frame. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/velocimeter

**Path**: `sensor/velocimeter`
**Tag**: `velocimeter`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorSite`

Common sensor data for sensors that attach to a site.

 This type is shared by site-based sensors such as touch, accelerometer, velocimeter,
 gyro, force, torque, and magnetometer. The active sensing zone or measurement origin
 is defined by the named site, and the sensor uses the site's position and orientation.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `site` | `string` | yes | `""""` | The name of the site where the sensor is mounted. The sensor is centered and aligned  with the site local frame. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/gyro

**Path**: `sensor/gyro`
**Tag**: `gyro`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorSite`

Common sensor data for sensors that attach to a site.

 This type is shared by site-based sensors such as touch, accelerometer, velocimeter,
 gyro, force, torque, and magnetometer. The active sensing zone or measurement origin
 is defined by the named site, and the sensor uses the site's position and orientation.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `site` | `string` | yes | `""""` | The name of the site where the sensor is mounted. The sensor is centered and aligned  with the site local frame. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/jointpos

**Path**: `sensor/jointpos`
**Tag**: `jointpos`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorJoint`

Common sensor data for sensors that attach to a scalar joint.

 This type is shared by joint-based sensors such as jointpos, jointvel, ballquat,
 ballangvel, jointlimitpos, jointlimitvel, jointlimitfrc, and jointactuatorfrc. Only
 scalar joints (slide or hinge) can be referenced by most of these sensors; ball joints
 are used by ballquat and ballangvel.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `joint` | `string` | yes | `""""` | The name of the joint to which the sensor is attached. For most joint sensors only  scalar joints (slide or hinge) can be referenced; for ballquat and ballangvel the  referenced joint must be a ball joint. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/jointvel

**Path**: `sensor/jointvel`
**Tag**: `jointvel`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorJoint`

Common sensor data for sensors that attach to a scalar joint.

 This type is shared by joint-based sensors such as jointpos, jointvel, ballquat,
 ballangvel, jointlimitpos, jointlimitvel, jointlimitfrc, and jointactuatorfrc. Only
 scalar joints (slide or hinge) can be referenced by most of these sensors; ball joints
 are used by ballquat and ballangvel.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `joint` | `string` | yes | `""""` | The name of the joint to which the sensor is attached. For most joint sensors only  scalar joints (slide or hinge) can be referenced; for ballquat and ballangvel the  referenced joint must be a ball joint. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/framepos

**Path**: `sensor/framepos`
**Tag**: `framepos`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorFrame`

Common sensor data for sensors that track a spatial coordinate frame.

 This type is shared by frame-based sensors such as framepos, framequat, framexaxis,
 frameyaxis, framezaxis, framelinvel, and frameangvel. The sensor reports properties
 of the spatial frame of the specified object, either in global coordinates or
 optionally with respect to a given frame-of-reference.

Note

 Both `ref_type` and `ref_name` must be set together; providing one without the other
 is invalid. If neither is given, the sensor values are measured with respect to the
 global frame.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `objtype` | `string` | yes | `"body"` | The type of object to which the sensor is attached. This must be an object type  that has a spatial frame. \"body\" refers to the inertial frame of the body, while  \"xbody\" refers to the regular frame of the body (usually centered at the joint  with the parent body). Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `objname` | `string` | yes | `""""` | The name of the object to which the sensor is attached. |
| `reftype` | `string` | no | — | The type of object to which the frame-of-reference is attached. The semantics are  identical to the objtype attribute. If reftype and refname are both given, the  sensor values will be measured with respect to this frame. Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `refname` | `string` | no | — | The name of the object to which the frame-of-reference is attached. If reftype and  refname are both given, the sensor values will be measured with respect to the  frame defined by this object. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/framequat

**Path**: `sensor/framequat`
**Tag**: `framequat`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorFrame`

Common sensor data for sensors that track a spatial coordinate frame.

 This type is shared by frame-based sensors such as framepos, framequat, framexaxis,
 frameyaxis, framezaxis, framelinvel, and frameangvel. The sensor reports properties
 of the spatial frame of the specified object, either in global coordinates or
 optionally with respect to a given frame-of-reference.

Note

 Both `ref_type` and `ref_name` must be set together; providing one without the other
 is invalid. If neither is given, the sensor values are measured with respect to the
 global frame.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `objtype` | `string` | yes | `"body"` | The type of object to which the sensor is attached. This must be an object type  that has a spatial frame. \"body\" refers to the inertial frame of the body, while  \"xbody\" refers to the regular frame of the body (usually centered at the joint  with the parent body). Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `objname` | `string` | yes | `""""` | The name of the object to which the sensor is attached. |
| `reftype` | `string` | no | — | The type of object to which the frame-of-reference is attached. The semantics are  identical to the objtype attribute. If reftype and refname are both given, the  sensor values will be measured with respect to this frame. Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `refname` | `string` | no | — | The name of the object to which the frame-of-reference is attached. If reftype and  refname are both given, the sensor values will be measured with respect to the  frame defined by this object. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/framexaxis

**Path**: `sensor/framexaxis`
**Tag**: `framexaxis`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorFrame`

Common sensor data for sensors that track a spatial coordinate frame.

 This type is shared by frame-based sensors such as framepos, framequat, framexaxis,
 frameyaxis, framezaxis, framelinvel, and frameangvel. The sensor reports properties
 of the spatial frame of the specified object, either in global coordinates or
 optionally with respect to a given frame-of-reference.

Note

 Both `ref_type` and `ref_name` must be set together; providing one without the other
 is invalid. If neither is given, the sensor values are measured with respect to the
 global frame.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `objtype` | `string` | yes | `"body"` | The type of object to which the sensor is attached. This must be an object type  that has a spatial frame. \"body\" refers to the inertial frame of the body, while  \"xbody\" refers to the regular frame of the body (usually centered at the joint  with the parent body). Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `objname` | `string` | yes | `""""` | The name of the object to which the sensor is attached. |
| `reftype` | `string` | no | — | The type of object to which the frame-of-reference is attached. The semantics are  identical to the objtype attribute. If reftype and refname are both given, the  sensor values will be measured with respect to this frame. Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `refname` | `string` | no | — | The name of the object to which the frame-of-reference is attached. If reftype and  refname are both given, the sensor values will be measured with respect to the  frame defined by this object. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/frameyaxis

**Path**: `sensor/frameyaxis`
**Tag**: `frameyaxis`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorFrame`

Common sensor data for sensors that track a spatial coordinate frame.

 This type is shared by frame-based sensors such as framepos, framequat, framexaxis,
 frameyaxis, framezaxis, framelinvel, and frameangvel. The sensor reports properties
 of the spatial frame of the specified object, either in global coordinates or
 optionally with respect to a given frame-of-reference.

Note

 Both `ref_type` and `ref_name` must be set together; providing one without the other
 is invalid. If neither is given, the sensor values are measured with respect to the
 global frame.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `objtype` | `string` | yes | `"body"` | The type of object to which the sensor is attached. This must be an object type  that has a spatial frame. \"body\" refers to the inertial frame of the body, while  \"xbody\" refers to the regular frame of the body (usually centered at the joint  with the parent body). Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `objname` | `string` | yes | `""""` | The name of the object to which the sensor is attached. |
| `reftype` | `string` | no | — | The type of object to which the frame-of-reference is attached. The semantics are  identical to the objtype attribute. If reftype and refname are both given, the  sensor values will be measured with respect to this frame. Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `refname` | `string` | no | — | The name of the object to which the frame-of-reference is attached. If reftype and  refname are both given, the sensor values will be measured with respect to the  frame defined by this object. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/framezaxis

**Path**: `sensor/framezaxis`
**Tag**: `framezaxis`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorFrame`

Common sensor data for sensors that track a spatial coordinate frame.

 This type is shared by frame-based sensors such as framepos, framequat, framexaxis,
 frameyaxis, framezaxis, framelinvel, and frameangvel. The sensor reports properties
 of the spatial frame of the specified object, either in global coordinates or
 optionally with respect to a given frame-of-reference.

Note

 Both `ref_type` and `ref_name` must be set together; providing one without the other
 is invalid. If neither is given, the sensor values are measured with respect to the
 global frame.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `objtype` | `string` | yes | `"body"` | The type of object to which the sensor is attached. This must be an object type  that has a spatial frame. \"body\" refers to the inertial frame of the body, while  \"xbody\" refers to the regular frame of the body (usually centered at the joint  with the parent body). Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `objname` | `string` | yes | `""""` | The name of the object to which the sensor is attached. |
| `reftype` | `string` | no | — | The type of object to which the frame-of-reference is attached. The semantics are  identical to the objtype attribute. If reftype and refname are both given, the  sensor values will be measured with respect to this frame. Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `refname` | `string` | no | — | The name of the object to which the frame-of-reference is attached. If reftype and  refname are both given, the sensor values will be measured with respect to the  frame defined by this object. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/framelinvel

**Path**: `sensor/framelinvel`
**Tag**: `framelinvel`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorFrame`

Common sensor data for sensors that track a spatial coordinate frame.

 This type is shared by frame-based sensors such as framepos, framequat, framexaxis,
 frameyaxis, framezaxis, framelinvel, and frameangvel. The sensor reports properties
 of the spatial frame of the specified object, either in global coordinates or
 optionally with respect to a given frame-of-reference.

Note

 Both `ref_type` and `ref_name` must be set together; providing one without the other
 is invalid. If neither is given, the sensor values are measured with respect to the
 global frame.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `objtype` | `string` | yes | `"body"` | The type of object to which the sensor is attached. This must be an object type  that has a spatial frame. \"body\" refers to the inertial frame of the body, while  \"xbody\" refers to the regular frame of the body (usually centered at the joint  with the parent body). Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `objname` | `string` | yes | `""""` | The name of the object to which the sensor is attached. |
| `reftype` | `string` | no | — | The type of object to which the frame-of-reference is attached. The semantics are  identical to the objtype attribute. If reftype and refname are both given, the  sensor values will be measured with respect to this frame. Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `refname` | `string` | no | — | The name of the object to which the frame-of-reference is attached. If reftype and  refname are both given, the sensor values will be measured with respect to the  frame defined by this object. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/frameangvel

**Path**: `sensor/frameangvel`
**Tag**: `frameangvel`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorFrame`

Common sensor data for sensors that track a spatial coordinate frame.

 This type is shared by frame-based sensors such as framepos, framequat, framexaxis,
 frameyaxis, framezaxis, framelinvel, and frameangvel. The sensor reports properties
 of the spatial frame of the specified object, either in global coordinates or
 optionally with respect to a given frame-of-reference.

Note

 Both `ref_type` and `ref_name` must be set together; providing one without the other
 is invalid. If neither is given, the sensor values are measured with respect to the
 global frame.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `objtype` | `string` | yes | `"body"` | The type of object to which the sensor is attached. This must be an object type  that has a spatial frame. \"body\" refers to the inertial frame of the body, while  \"xbody\" refers to the regular frame of the body (usually centered at the joint  with the parent body). Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `objname` | `string` | yes | `""""` | The name of the object to which the sensor is attached. |
| `reftype` | `string` | no | — | The type of object to which the frame-of-reference is attached. The semantics are  identical to the objtype attribute. If reftype and refname are both given, the  sensor values will be measured with respect to this frame. Choice: `body`, `xbody`, `geom`, `site`, `camera`. |
| `refname` | `string` | no | — | The name of the object to which the frame-of-reference is attached. If reftype and  refname are both given, the sensor values will be measured with respect to the  frame defined by this object. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/subtreecom

**Path**: `sensor/subtreecom`
**Tag**: `subtreecom`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorBody`

Common sensor data for sensors that are rooted at a body.

 This type is shared by body-rooted sensors such as subtreecom, subtreelinvel, and
 subtreeangmom. These sensors return properties of the kinematic subtree rooted at
 the specified body, computed in global coordinates.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `body` | `string` | yes | `""""` | The name of the body where the kinematic subtree is rooted. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/subtreelinvel

**Path**: `sensor/subtreelinvel`
**Tag**: `subtreelinvel`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorBody`

Common sensor data for sensors that are rooted at a body.

 This type is shared by body-rooted sensors such as subtreecom, subtreelinvel, and
 subtreeangmom. These sensors return properties of the kinematic subtree rooted at
 the specified body, computed in global coordinates.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `body` | `string` | yes | `""""` | The name of the body where the kinematic subtree is rooted. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/subtreeangmom

**Path**: `sensor/subtreeangmom`
**Tag**: `subtreeangmom`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorBody`

Common sensor data for sensors that are rooted at a body.

 This type is shared by body-rooted sensors such as subtreecom, subtreelinvel, and
 subtreeangmom. These sensors return properties of the kinematic subtree rooted at
 the specified body, computed in global coordinates.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `body` | `string` | yes | `""""` | The name of the body where the kinematic subtree is rooted. |
| `name` | `string` | no | — | Name of the sensor. |
| `noise` | `real` | yes | `0.0` | The standard deviation of zero-mean Gaussian noise added to the sensor output. Noise  is added in the same units as the sensor output. |
| `cutoff` | `real` | yes | `0.0` | The cutoff value for the sensor output. If the sensor output exceeds this value in  absolute terms, it is clipped to this value. |
| `user` | `real(n)` | yes | `""` | User-defined scalar data associated with the sensor. These values are not used by  the simulator and are passed through to the model without change. |

## sensor/contact

**Path**: `sensor/contact`
**Tag**: `contact`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorContact`

Sensor data for a contact sensor that detects and reports properties of contact events.

 The contact sensor detects contacts between pairs of
 geoms, bodies, or subtrees, or contacts associated with a site. Multiple filtering
 attributes can be specified to narrow the set of contacts detected. The sensor can
 report various contact properties such as whether contact was found, the contact force,
 torque, distance, position, normal, or tangent direction.

Note

 Exactly one of the following filter groups may be used at a time: (geom1, geom2),
 (body1, body2), (subtree1, subtree2), or site. These groups are mutually exclusive
 and cannot be combined.

 The following describes how motrixsim's contact sensor output differs from MuJoCo:
 - `found`: Reports the total **count** of matching contacts, not a 0/1 boolean.
 - `site` filter: Parsed but **not yet supported** at runtime; the sensor will be ignored.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | Name of the sensor. |
| `geom1` | `string` | no | — | Name of the first geom used to filter contacts. Must be paired with geom2; cannot  be combined with body, subtree, or site filters. |
| `geom2` | `string` | no | — | Name of the second geom used to filter contacts. Must be paired with geom1; cannot  be combined with body, subtree, or site filters. |
| `body1` | `string` | no | — | Name of the first body used to filter contacts. Must be paired with body2; cannot  be combined with geom, subtree, or site filters. |
| `body2` | `string` | no | — | Name of the second body used to filter contacts. Must be paired with body1; cannot  be combined with geom, subtree, or site filters. |
| `subtree1` | `string` | no | — | Name of the first body subtree used to filter contacts. All contacts involving any  geom in this subtree will be considered. Must be paired with subtree2; cannot be  combined with geom, body, or site filters. |
| `subtree2` | `string` | no | — | Name of the second body subtree used to filter contacts. Must be paired with  subtree1; cannot be combined with geom, body, or site filters. |
| `site` | `string` | no | — | Name of the site used to filter contacts. Contacts associated with this site will  be considered. Cannot be combined with geom, body, or subtree filters. |
| `num` | `int` | yes | `1` | The maximum number of contacts to detect and report. When more contacts are found  than this value, only the first contacts (up to this limit) are used, unless a  reduction method is specified. |
| `data` | `real(n)` | yes | `"found"` | The type or types of contact data to report in the sensor output. Multiple data  types may be listed in sequence. |
| `reduce` | `string` | yes | `"none"` | The method used to reduce multiple contacts to a single output value. Choice: `none`, `mindist`, `maxforce`, `netforce`. |

## sensor/lidar [MPEX]

**Path**: `sensor/lidar`
**Tag**: `lidar`
**Parent**: `sensor`
**Children**: none
**Rust Type**: `model::sensor::sensors::SensorLidar`

A multi-beam lidar sensor attached to a site.

Note

 This is a MotrixSim extension to MJCF. Model and scan attributes are defined by the referenced
 `asset/lidar` profile; the sensor instance contains only identity, mounting, filtering, and
 runtime-adjustable scan rate.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | no | — | [MPEX] Name of the sensor. |
| `asset` | `string` | yes | `""""` | [MPEX] Name of the required `asset/lidar` profile. |
| `site` | `string` | yes | `""""` | [MPEX] The site whose local frame defines the ray origins and directions. This attribute is  required on sensor instances and is not supplied by `asset/lidar`. |
| `exclude` | `string` | yes | `"parentbody"` | [MPEX] Self-filter policy for colliders belonging to the sensor's parent hierarchy. Choice: `none`, `parentbody`, `parentsubtree`. |
| `hz` | `real` | no | — | [MPEX] Full-scan rate in hertz. If omitted, the complete pattern is sampled every physics step. |

