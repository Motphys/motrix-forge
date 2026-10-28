# 配置 Forge

Forge 的插件级偏好设置集中在 **Edit → Preferences → Add-ons → Forge**。在 Add-ons 中搜索 Forge 并展开设置，可以看到 **General**、**MCP Server** 和 **Dependencies** 三个页签。

这些设置控制插件的显示、连接和依赖环境。模型本身的质量、关节、几何尺寸等参数在场景对象的 Forge Properties 中编辑，见[属性编辑](forge_docs/07_properties.md)。

## General：通用设置

<div style="flex: 1; text-align: center; ">
    <img
        src="../assets/images/setting_01.png"
        width="684"
        alt="通用设置"
    >
</div>

### CoACD Name Template

控制 CoACD 生成的凸包名称，默认是 `?_hull_#`：

| 占位符 | 含义 | 示例 |
| --- | --- | --- |
| `?` | 原始网格对象名 | `arm` |
| `#` | 凸包编号，从 1 开始，至少三位数字 | `001`、`002` |

例如，源对象名为 `arm`，默认模板会生成 `arm_hull_001`、`arm_hull_002`。修改模板影响之后的分解，不会重命名已有凸包；**Select Hulls** 也使用当前模板匹配，因此改模板后可能无法再选中按旧模板命名的对象。模板必须保留 `?`。

分解操作与输出规则见 [CoACD](forge_docs/09_coacd.md)。

### Viewport Previews

| 参数 | 默认值 | 作用 |
| --- | --- | --- |
| Collider Preview | 开启 | 在所有 3D 视图绘制 Collider 的半透明表面 |
| Inertial Preview | 开启 | 在所有 3D 视图绘制与质量和惯量等效的长方体 |

修改开关会立即刷新视口。两种预览都要求当前视图开启 **Overlays** 及其中的 **Extras**。关闭 Collider Preview 后，碰撞体原生线框仍保留；关闭 Inertial Preview 后，仍保留可选择的 Empty 长方体。

这些开关只影响显示，不改变碰撞几何、质量、惯量或导出内容。Inertial 长方体的尺寸由质量和惯量决定，不由 **Gizmo display size** 控制。

## MCP Server：Blender 侧 Bridge

该页配置运行在 Blender 中的 TCP Bridge。它与 Agent 侧的 stdio MCP Server 是两个独立进程。启动与连接流程见[第 1 章](forge_docs/01_mcp_server.md)及 [MCP 安装指南](../reference/MCP_INSTALL.zh-CN.md)。

<div style="flex: 1; text-align: center; ">
    <img
        src="../assets/images/setting_02.png"
        width="684"
        alt="MCP Bridge 设置"
    >
</div>

### 连接参数

| 参数 | 默认值 | 范围与说明 |
| --- | --- | --- |
| Host | `localhost` | Blender Bridge 的监听地址，不是 Agent 机器的地址 |
| Port | `9876` | 整数，`1024–65535`；应与 Agent 侧连接端口一致 |
| Authentication Token | 空 | 密码样式显示的共享令牌；配置后客户端必须使用相同值，监听非回环地址时必须设置 |

Agent 侧的 `FORGE_MCP_HOST`、`FORGE_MCP_PORT` 和 `FORGE_MCP_TOKEN` 应与 Bridge 配置对应。跨机器时，客户端使用 Blender 机器可访问的地址。

修改 Host、Port 或 Token 后，在 Forge 侧栏先点击 **Stop MCP Bridge**，再点击 **Start MCP Bridge**，让运行中的 Bridge 读取新配置。若端口被占用，启动会失败并报告错误。

### Polling：轮询频率

以下时间单位均为秒，用于交互模式下 Blender 主线程的轮询计时，不是网络请求超时。

| 参数 | 默认值 | 允许范围 | 作用 |
| --- | --- | --- | --- |
| Active interval | `0.05` | `0.01–1.0` | 有请求或工作时的轮询间隔；越小响应越及时，但 CPU 开销越高 |
| Idle interval | `1.0` | `0.1–10.0` | 空闲状态的轮询间隔；越大空闲开销越低，但下一次请求可能等待更久 |
| Idle delay | `5.0` | `1.0–60.0` | 没有工作后，切换到空闲间隔前等待的时间 |

通常可保留默认值。修改后停止并重新启动 Bridge，新的轮询配置才会应用到该服务。

### Startup：自动启动

| 参数 | 默认值 | 范围与说明 |
| --- | --- | --- |
| Auto-start server | 开启 | 插件启动时自动启动 Blender 侧 Bridge；关闭后可通过侧栏手动启动 |
| Auto-start delay | `2.0` 秒 | `0.0–30.0` 秒；插件启动后执行自动启动前的等待时间 |

关闭 Auto-start server 不会立即停止已经运行的 Bridge；需要停止时仍应点击 **Stop MCP Bridge**。Auto-start delay 控制启动等待时间，不是 Agent 请求的延迟。

Bridge 需要 Blender 允许在线访问。未允许时不会监听端口；根据当前 Blender 版本，在 Preferences 的网络设置中启用在线访问，后台运行时使用 `--online-mode`。启动失败原因会显示在该页的 **Debug** 区域中。

### Debug：日志与启动错误

| 项目 | 默认值 | 作用 |
| --- | --- | --- |
| Log requests to console | 关闭 | 将请求和响应日志写入 Blender 控制台，便于排查通信和工具调用问题 |
| 启动错误信息 | 无 | 启动失败时显示原因，例如端口被占用或未允许在线访问；这是状态提示，不是可编辑配置 |

日志开关即时生效，无需重启 Bridge。收到请求时立即输出请求记录，执行结束后输出响应；延迟操作先显示 `Forge response: deferred`。日志写入 Blender **系统控制台**（标准错误流），不是 3D 视图切换出的 **Python Console**。Windows 可通过 **Window → Toggle System Console** 打开；从终端启动 Blender 时，在该终端查看。没有收到请求时不会持续输出日志。安装依赖失败的 PIP 输出也应在系统控制台查看。

## Dependencies：依赖管理

该页检查和管理 **Blender 使用的 Python 环境**，与仓库及文档工具共用的根目录 `.venv` 不是同一环境。

<div style="flex: 1; text-align: center; ">
    <img
        src="../assets/images/setting_03.png"
        width="684"
        alt="依赖管理设置"
    >
</div>

| 依赖 | 用途 |
| --- | --- |
| pip | 安装、升级外部 Python 包 |
| tetgen | Mesh 四面体化和惯量计算；参数化 Box、Sphere、Cylinder、Capsule 惯量不需要它 |
| CoACD | 将复杂网格分解为凸包 |

每个依赖会显示 `package is available` 或 `package is not available` 及对应状态图标，并提供 **Visit package website** 链接。

### PIP 按钮

- 已有 PIP：显示 **Upgrade PIP**，升级 `pip setuptools wheel`。
- 没有 PIP、但有 ensurepip：显示 **Install PIP**。
- PIP 和 ensurepip 都不可用：显示 **Installation instructions**，打开安装说明。

### 安装或升级功能依赖

操作入口为 **Edit → Preferences → Add-ons → Forge → Dependencies**。按所需功能安装 TetGen 或 CoACD；参数化基本形状的惯量计算不需要 TetGen。

> **依赖安装权限：** 安装或升级 Blender 的 Python 依赖可能需要管理员权限。在 Windows 上，如果提示权限不足或无法写入安装目录，请关闭 Blender，右键其快捷方式选择 **以管理员身份运行**，再重试依赖安装或升级。完成后关闭该实例，以普通方式重新启动 Blender。

1. 如果缺少 PIP，先安装 PIP，并按提示重启 Blender。
2. 缺少 tetgen 或 CoACD 时，点击 **Install with PIP**；已可用时显示 **Upgrade with PIP**。
3. 安装或升级完成后重启 Blender，重新检查依赖状态。
4. 如果失败，查看控制台，检查网络和 Blender Python 目录的写入权限。

界面中的安装和升级操作都使用 PIP 的升级模式。根目录执行 `uv sync` 不会替代 Blender 内的依赖安装。

## 保存与生效

| 修改内容 | 生效方式 |
| --- | --- |
| Collider / Inertial Preview | 立即刷新视口 |
| CoACD Name Template | 下一次分解或选择凸包时使用 |
| Host / Port / Token、Polling | 停止并重新启动 MCP Bridge |
| 日志开关 | 即时生效，无需重启 MCP Bridge |
| 自动启动选项与延迟 | 在后续插件启动流程中使用 |
| 安装或升级 Python 依赖 | 完成后重启 Blender |

偏好设置由 Blender 的偏好保存机制管理。若关闭了偏好自动保存，请在 Preferences 中执行 **Save Preferences**，以便下次启动继续使用。
