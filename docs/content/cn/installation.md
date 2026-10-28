# 安装 Forge

本页介绍 Blender 插件的安装和首次使用。只使用 Blender 界面建模时，不需要安装 MCP Server 或根目录的开发环境。

## 环境要求

| 用途 | 要求 |
| --- | --- |
| 使用 Forge 插件 | Windows、macOS 或 Linux；支持 Blender 4.5 LTS（4.5.6 起）和 Blender 5.2 LTS |
| 功能依赖 | 按需配置，见[配置 Forge → Dependencies](preferences.md#dependencies依赖管理) |
| Agent 自动化（可选） | Agent 侧安装 uv，并配置支持 stdio MCP 的客户端 |

>使用 Forge 需要具备基本的 Blender 操作经验。

## 1. 准备安装包

使用与目标源码版本一致的 Forge ZIP 安装包，或从当前仓库打包 `addon/Forge`。ZIP 根目录应直接包含 `blender_manifest.toml`、`__init__.py`、`core/`、`ops/` 和 `lib/`，不要把整个仓库作为插件安装。

PowerShell 打包示例，在仓库根目录执行：

```powershell
git lfs pull
Compress-Archive -Path addon/Forge/* -DestinationPath Forge.zip -Force
```

`git lfs pull` 用于获取插件所需的真实资源文件，包括 `lib/assets/Shapes.blend`。已有完整安装包时不需要重新打包。

## 2. 在 Blender 中安装

1. 打开 **Edit → Preferences → Add-ons → Install from Disk**。
2. 选择 Forge ZIP 并安装。
3. 在 Add-ons 列表中搜索 **Forge**，确认已启用。
4. 回到 3D View，按 `N` 打开侧栏，切换到 **Forge** 页签。

<div style="flex: 1; text-align: center; ">
    <img
        src="../assets/images/Addons.png"
        width="668"
        alt="从磁盘安装并启用 Forge 插件"
    >
</div>

安装完成后，根据需要在[配置 Forge → Dependencies](preferences.md#dependencies依赖管理)中安装功能依赖。依赖用途、PIP 操作、安装步骤和重启要求统一在该页说明。

## 3. 确认可以开始建模

1. 新建或打开一个 Blender 场景，进入 **Object Mode**。
2. 打开 Forge 侧栏，确认 **Model Define** 中的创建和定义分组可见。
3. 未选中对象时点击 **Create link(s)**，再创建 Visual 或 Collider。
4. 选中对象，确认 **Object Properties → Forge Properties** 可以显示对应模型数据。

接下来阅读[界面总览](forge_docs/00_ui_overview.md)和[推荐建模流程](forge_docs/00_ui_overview.md#05-推荐建模流程)。

## 4. 接入 Agent（可选）

需要 Agent 查询或修改场景时，再配置 MCP：

1. 在拥有场景的 Blender 实例中启用 Forge。
2. 在 Forge 面板或设置中启动 **MCP Bridge**；默认地址为 `localhost:9876`。
3. 按 [MCP 安装指南](../reference/MCP_INSTALL.zh-CN.md)配置 Agent 侧服务和客户端。

MCP Server 与 Blender 插件是独立组件。两者的安装、启动位置和依赖不同。

## 安装问题

| 现象 | 检查内容 |
| --- | --- |
| 无法识别 ZIP | 检查是否打包了 `addon/Forge` 的内容，以及 ZIP 根目录是否有 `blender_manifest.toml` |
| 看不到 Forge 页签 | 确认插件启用，当前是 3D View，且已按 `N` 展开侧栏 |
| 缺少 Shapes.blend 或图标 | 获取 Git LFS 资源后重新打包安装 |
| 依赖安装失败 | 参阅[配置 Forge：依赖安装说明](preferences.md#安装或升级功能依赖) |
| 按钮灰色 | 检查 Object Mode、对象类型和选择数量；见[操作前置条件](forge_docs/00_ui_overview.md#03-按钮灰色的含义) |

准备修改源码时，继续阅读[开发 Forge](development.md)。
