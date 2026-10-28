# MJCF XML Reference

Motrixsim 支持的 MJCF XML 元素参考。`Path` 是本文档的元素唯一主键。标记 [MPEX] 的为 Motphys 扩展，标记 [PRO] 的为 Motphys Pro-only 扩展。

## Element Hierarchy

- `mujoco` — Top-level element
  - [`extension`](./extension.md)
    - `extension/plugin`
  - [`compiler`](./compiler.md)
  - [`asset`](./asset.md)
    - `asset/material`, `asset/mesh`, `asset/texture`, `asset/hfield`, `asset/gsplat` [PRO], `asset/model`, `asset/lidar` [MPEX]
  - [`default`](./default.md)
    - `default/default`, `default/geom`, `default/joint`, `default/light`, `default/mesh`, `default/material`, `default/general`, `default/motor`, `default/position`, `default/velocity`, `default/adhesion`, `default/camera`, `default/site`, `default/pair`, `default/tendon`, `default/equality`
  - [`body`](./body.md)
    - `body/inertial`, `body/joint`, `body/freejoint`, `body`, `body/attach`, `body/camera`, `body/frame`, `body/geom`, `body/gsplat` [PRO], `body/light`, `body/replicate`, `body/site`
  - [`option`](./option.md)
    - `option/flag`
  - [`actuator`](./actuator.md)
    - `actuator/adhesion`, `actuator/general`, `actuator/motor`, `actuator/position`, `actuator/velocity`
  - [`visual`](./visual.md)
    - `visual/headlight`, `visual/global`, `visual/quality`, `visual/map`, `visual/rgba`, `visual/probe` [MPEX], `visual/ssao` [MPEX], `visual/ssgi` [MPEX], `visual/tonemapping` [MPEX]
  - [`equality`](./equality.md)
    - `equality/connect`, `equality/joint`, `equality/weld`
  - [`contact`](./contact.md)
    - `contact/pair`, `contact/exclude`
  - [`tendon`](./tendon.md)
    - `tendon/fixed`
  - [`custom`](./custom.md)
    - `custom/numeric`, `custom/text`
  - [`sensor`](./sensor.md)
    - `sensor/touch`, `sensor/accelerometer`, `sensor/velocimeter`, `sensor/gyro`, `sensor/force`, `sensor/torque`, `sensor/jointpos`, `sensor/jointvel`, `sensor/jointactuatorfrc`, `sensor/ballquat`, `sensor/ballangvel`, `sensor/jointlimitpos`, `sensor/jointlimitvel`, `sensor/jointlimitfrc`, `sensor/tendonpos`, `sensor/tendonvel`, `sensor/tendonlimitpos`, `sensor/tendonlimitvel`, `sensor/tendonlimitfrc`, `sensor/actuatorpos`, `sensor/actuatorvel`, `sensor/actuatorfrc`, `sensor/framepos`, `sensor/framequat`, `sensor/framexaxis`, `sensor/frameyaxis`, `sensor/framezaxis`, `sensor/framelinvel`, `sensor/frameangvel`, `sensor/framelinacc`, `sensor/frameangacc`, `sensor/subtreecom`, `sensor/subtreelinvel`, `sensor/subtreeangmom`, `sensor/distance`, `sensor/normal`, `sensor/fromto`, `sensor/contact`, `sensor/lidar` [MPEX]
  - [`statistic`](./statistic.md)
  - [`keyframe`](./keyframe.md)
    - `keyframe/key`

## Path Registry

| Path | Tag | File | Parent | Children |
|------|-----|------|--------|----------|
| `actuator` | `actuator` | `actuator.md` | `mujoco` | `actuator/adhesion`, `actuator/general`, `actuator/motor`, `actuator/position`, `actuator/velocity` |
| `actuator/adhesion` | `adhesion` | `actuator.md` | `actuator` | none |
| `actuator/general` | `general` | `actuator.md` | `actuator` | none |
| `actuator/motor` | `motor` | `actuator.md` | `actuator` | none |
| `actuator/position` | `position` | `actuator.md` | `actuator` | none |
| `actuator/velocity` | `velocity` | `actuator.md` | `actuator` | none |
| `asset` | `asset` | `asset.md` | `mujoco` | `asset/material`, `asset/mesh`, `asset/texture`, `asset/hfield`, `asset/gsplat`, `asset/model`, `asset/lidar` |
| `asset/gsplat` | `gsplat` | `asset.md` | `asset` | none |
| `asset/hfield` | `hfield` | `asset.md` | `asset` | none |
| `asset/lidar` | `lidar` | `asset.md` | `asset` | none |
| `asset/material` | `material` | `asset.md` | `asset` | `asset/material/layer` |
| `asset/mesh` | `mesh` | `asset.md` | `asset` | none |
| `asset/model` | `model` | `asset.md` | `asset` | none |
| `asset/texture` | `texture` | `asset.md` | `asset` | none |
| `body` | `body` | `body.md` | `mujoco` | `body/inertial`, `body/joint`, `body/freejoint`, `body`, `body/attach`, `body/camera`, `body/frame`, `body/geom`, `body/gsplat`, `body/light`, `body/replicate`, `body/site` |
| `body/attach` | `attach` | `body.md` | `body` | none |
| `body/camera` | `camera` | `body.md` | `body` | none |
| `body/frame` | `frame` | `body.md` | `body` | none |
| `body/freejoint` | `freejoint` | `body.md` | `body` | none |
| `body/geom` | `geom` | `body.md` | `body` | none |
| `body/gsplat` | `gsplat` | `body.md` | `body` | none |
| `body/inertial` | `inertial` | `body.md` | `body` | none |
| `body/joint` | `joint` | `body.md` | `body` | none |
| `body/light` | `light` | `body.md` | `body` | none |
| `body/replicate` | `replicate` | `body.md` | `body` | none |
| `body/site` | `site` | `body.md` | `body` | none |
| `compiler` | `compiler` | `compiler.md` | `mujoco` | none |
| `contact` | `contact` | `contact.md` | `mujoco` | `contact/pair`, `contact/exclude` |
| `contact/exclude` | `exclude` | `contact.md` | `contact` | none |
| `contact/pair` | `pair` | `contact.md` | `contact` | none |
| `custom` | `custom` | `custom.md` | `mujoco` | `custom/numeric`, `custom/text` |
| `custom/numeric` | `numeric` | `custom.md` | `custom` | none |
| `custom/text` | `text` | `custom.md` | `custom` | none |
| `default` | `default` | `default.md` | `mujoco` | `default/default`, `default/geom`, `default/joint`, `default/light`, `default/mesh`, `default/material`, `default/general`, `default/motor`, `default/position`, `default/velocity`, `default/adhesion`, `default/camera`, `default/site`, `default/pair`, `default/tendon`, `default/equality` |
| `default/adhesion` | `adhesion` | `default.md` | `default` | none |
| `default/camera` | `camera` | `default.md` | `default` | none |
| `default/default` | `default` | `default.md` | `default` | none |
| `default/equality` | `equality` | `default.md` | `default` | none |
| `default/general` | `general` | `default.md` | `default` | none |
| `default/geom` | `geom` | `default.md` | `default` | none |
| `default/joint` | `joint` | `default.md` | `default` | none |
| `default/light` | `light` | `default.md` | `default` | none |
| `default/material` | `material` | `default.md` | `default` | none |
| `default/mesh` | `mesh` | `default.md` | `default` | none |
| `default/motor` | `motor` | `default.md` | `default` | none |
| `default/pair` | `pair` | `default.md` | `default` | none |
| `default/position` | `position` | `default.md` | `default` | none |
| `default/site` | `site` | `default.md` | `default` | none |
| `default/tendon` | `tendon` | `default.md` | `default` | none |
| `default/velocity` | `velocity` | `default.md` | `default` | none |
| `equality` | `equality` | `equality.md` | `mujoco` | `equality/connect`, `equality/joint`, `equality/weld` |
| `equality/connect` | `connect` | `equality.md` | `equality` | none |
| `equality/joint` | `joint` | `equality.md` | `equality` | none |
| `equality/weld` | `weld` | `equality.md` | `equality` | none |
| `extension` | `extension` | `extension.md` | `mujoco` | `extension/plugin` |
| `extension/plugin` | `plugin` | `extension.md` | `extension` | `extension/plugin/instance` |
| `extension/plugin/instance` | `instance` | `extension.md` | `extension/plugin` | `extension/plugin/instance/config` |
| `extension/plugin/instance/config` | `config` | `extension.md` | `extension/plugin/instance` | none |
| `keyframe` | `keyframe` | `keyframe.md` | `mujoco` | `keyframe/key` |
| `keyframe/key` | `key` | `keyframe.md` | `keyframe` | none |
| `mujoco` | `mujoco` | `index.md` | `none` | `extension`, `compiler`, `asset`, `default`, `body`, `option`, `actuator`, `visual`, `equality`, `contact`, `tendon`, `custom`, `sensor`, `statistic`, `keyframe` |
| `option` | `option` | `option.md` | `mujoco` | `option/flag` |
| `option/flag` | `flag` | `option.md` | `option` | none |
| `sensor` | `sensor` | `sensor.md` | `mujoco` | `sensor/touch`, `sensor/accelerometer`, `sensor/velocimeter`, `sensor/gyro`, `sensor/force`, `sensor/torque`, `sensor/jointpos`, `sensor/jointvel`, `sensor/jointactuatorfrc`, `sensor/ballquat`, `sensor/ballangvel`, `sensor/jointlimitpos`, `sensor/jointlimitvel`, `sensor/jointlimitfrc`, `sensor/tendonpos`, `sensor/tendonvel`, `sensor/tendonlimitpos`, `sensor/tendonlimitvel`, `sensor/tendonlimitfrc`, `sensor/actuatorpos`, `sensor/actuatorvel`, `sensor/actuatorfrc`, `sensor/framepos`, `sensor/framequat`, `sensor/framexaxis`, `sensor/frameyaxis`, `sensor/framezaxis`, `sensor/framelinvel`, `sensor/frameangvel`, `sensor/framelinacc`, `sensor/frameangacc`, `sensor/subtreecom`, `sensor/subtreelinvel`, `sensor/subtreeangmom`, `sensor/distance`, `sensor/normal`, `sensor/fromto`, `sensor/contact`, `sensor/lidar` |
| `sensor/accelerometer` | `accelerometer` | `sensor.md` | `sensor` | none |
| `sensor/contact` | `contact` | `sensor.md` | `sensor` | none |
| `sensor/frameangvel` | `frameangvel` | `sensor.md` | `sensor` | none |
| `sensor/framelinvel` | `framelinvel` | `sensor.md` | `sensor` | none |
| `sensor/framepos` | `framepos` | `sensor.md` | `sensor` | none |
| `sensor/framequat` | `framequat` | `sensor.md` | `sensor` | none |
| `sensor/framexaxis` | `framexaxis` | `sensor.md` | `sensor` | none |
| `sensor/frameyaxis` | `frameyaxis` | `sensor.md` | `sensor` | none |
| `sensor/framezaxis` | `framezaxis` | `sensor.md` | `sensor` | none |
| `sensor/gyro` | `gyro` | `sensor.md` | `sensor` | none |
| `sensor/jointpos` | `jointpos` | `sensor.md` | `sensor` | none |
| `sensor/jointvel` | `jointvel` | `sensor.md` | `sensor` | none |
| `sensor/lidar` | `lidar` | `sensor.md` | `sensor` | none |
| `sensor/subtreeangmom` | `subtreeangmom` | `sensor.md` | `sensor` | none |
| `sensor/subtreecom` | `subtreecom` | `sensor.md` | `sensor` | none |
| `sensor/subtreelinvel` | `subtreelinvel` | `sensor.md` | `sensor` | none |
| `sensor/touch` | `touch` | `sensor.md` | `sensor` | none |
| `sensor/velocimeter` | `velocimeter` | `sensor.md` | `sensor` | none |
| `statistic` | `statistic` | `statistic.md` | `mujoco` | none |
| `tendon` | `tendon` | `tendon.md` | `mujoco` | `tendon/fixed` |
| `tendon/fixed` | `fixed` | `tendon.md` | `tendon` | `tendon/fixed/joint` |
| `tendon/fixed/joint` | `joint` | `tendon.md` | `tendon/fixed` | none |
| `visual` | `visual` | `visual.md` | `mujoco` | `visual/headlight`, `visual/global`, `visual/quality`, `visual/map`, `visual/rgba`, `visual/probe`, `visual/ssao`, `visual/ssgi`, `visual/tonemapping` |
| `visual/global` | `global` | `visual.md` | `visual` | none |
| `visual/headlight` | `headlight` | `visual.md` | `visual` | none |
| `visual/map` | `map` | `visual.md` | `visual` | none |
| `visual/probe` | `probe` | `visual.md` | `visual` | none |
| `visual/quality` | `quality` | `visual.md` | `visual` | none |
| `visual/rgba` | `rgba` | `visual.md` | `visual` | none |
| `visual/ssao` | `ssao` | `visual.md` | `visual` | none |
| `visual/ssgi` | `ssgi` | `visual.md` | `visual` | none |
| `visual/tonemapping` | `tonemapping` | `visual.md` | `visual` | none |
