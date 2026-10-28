# extension

**Path**: `extension`
**Tag**: `extension`
**Parent**: `mujoco`
**Children**: `extension/plugin`
**Rust Type**: `model::extension::Extension`

This element is used to declare plugins and their instances.

## extension/plugin

**Path**: `extension/plugin`
**Tag**: `plugin`
**Parent**: `extension`
**Children**: `extension/plugin/instance`
**Rust Type**: `model::extension::PluginDeclear`

A plugin declaration.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `plugin` | `string` | yes | `""""` | Name of the plugin. |

### extension/plugin/instance

**Path**: `extension/plugin/instance`
**Tag**: `instance`
**Parent**: `extension/plugin`
**Children**: `extension/plugin/instance/config`
**Rust Type**: `model::extension::PluginInstance`

An instance of a plugin.

#### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | yes | `""""` | Name of the plugin instance. |

#### extension/plugin/instance/config

**Path**: `extension/plugin/instance/config`
**Tag**: `config`
**Parent**: `extension/plugin/instance`
**Children**: none
**Rust Type**: `model::extension::PluginConfig`

A configuration key-value pair for a plugin instance.

##### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `key` | `string` | yes | `""""` | Key of the configuration. |
| `value` | `string` | yes | `""""` | Value of the configuration. |

