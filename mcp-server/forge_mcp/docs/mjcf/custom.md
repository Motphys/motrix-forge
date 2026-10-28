# custom

**Path**: `custom`
**Tag**: `custom`
**Parent**: `mujoco`
**Children**: `custom/numeric`, `custom/text`
**Rust Type**: `model::custom::Custom`

This element is used to add custom numeric and text data to the model.

## custom/numeric

**Path**: `custom/numeric`
**Tag**: `numeric`
**Parent**: `custom`
**Children**: none
**Rust Type**: `model::custom::Numeric`

A custom numeric array.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | yes | `""""` | Name of the custom array. |
| `size` | `int` | no | — | Size of the array. |
| `data` | `real(n)` | yes | `""` | Array data. |

## custom/text

**Path**: `custom/text`
**Tag**: `text`
**Parent**: `custom`
**Children**: none
**Rust Type**: `model::custom::Text`

A custom text field.

### Attributes

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `name` | `string` | yes | `""""` | Name of the custom text. |
| `data` | `string` | yes | `""""` | Text data. |

