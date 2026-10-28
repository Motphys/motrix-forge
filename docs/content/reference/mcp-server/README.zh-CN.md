# Forge MCP 服务端参考

[English README](README.md)

本页介绍 Agent 侧 MCP Server 的运行架构、环境变量、Skills 与文档加载机制、工具分类以及开发调试。首次安装、客户端配置、启动和连接排查统一见 [MCP 安装与连接](../MCP_INSTALL.zh-CN.md)。

## 运行架构

```text
AI Agent ──stdio──> Forge MCP Server ──TCP──> Blender Forge MCP Bridge
```

MCP Server 运行在 Agent 侧；Bridge 运行在拥有场景的 Blender 进程中。场景查询和建模操作经由 Bridge 执行，Skills 读取和文档搜索使用服务本地的文件，不要求 Blender 正在运行。Blender 端的设置和依赖见[配置 Forge](../../cn/preferences.md)。

## 客户端启动与进程管理

完成[安装与连接](../MCP_INSTALL.zh-CN.md)中的环境准备后，按以下流程使用：

1. 在 Blender 中启用 Forge，并启动 **MCP Bridge**。
2. 在包含客户端配置的工作区目录启动 Claude Code 或 Codex。
3. 客户端读取工作区配置，自动启动和管理 Forge MCP Server，通过 stdio 与其通信。
4. 在客户端查看 MCP 连接状态，确认 `forge` 已连接，再执行 Forge 操作。

修改环境变量、Skills 或文档文件后，通过客户端重新连接或重启 MCP 服务。仅重启 Blender Bridge 不会重新加载服务端文档。

## 运行时配置

| 环境变量 | 默认值 | 说明 |
| --- | --- | --- |
| `FORGE_MCP_HOST` | `localhost` | Blender bridge 主机 |
| `FORGE_MCP_PORT` | `9876` | Blender bridge 端口 |
| `FORGE_MCP_TOKEN` | 空 | Blender 监听非 localhost 时使用的共享 Token |
| `FORGE_MCP_TIMEOUT` | `1800` | 响应超时时间（秒） |
| `FORGE_MCP_SKILL_GATE` | `soft` | `soft` 执行并附带一次阅读提示；`strict` 要求先读取对应 skill；`off` 关闭检查 |
| `FORGE_SKILLS_DIR` | 自动搜索 | `forge_skill` 使用的 skill 文档目录 |
| `FORGE_DOCS_DIR` | 自动搜索 | `forge_search_docs` 使用的 MJCF 文档目录 |
| `FORGE_BLENDER_DOCS_DIR` | 自动搜索 | Blender API/manual RST 文档根目录 |
| `FORGE_TOOLS` | 全部 | 按类别或名称过滤工具；`readonly` 只保留只读工具；无效的非空过滤条件会使服务启动失败 |

## Skills 与文档自动加载

启动时服务会加载第一个包含文档的目录：

1. `FORGE_SKILLS_DIR`；
2. 源码目录 `forge_mcp/skills/`；
3. 上层目录中的旧版 `skills/`；
4. 当前目录的 `./skills`。

加载的 skill 摘要会注入 MCP server instructions，并通过 `forge_skill` 按需读取：

```text
forge_skill(name="create")
forge_skill(name="modify")
forge_skill(name="operators")
forge_skill(name="custom_material")
```

可以传入 `section` 只读取一个章节，例如：`forge_skill(name="create", section="joint")`。

MJCF 文档位于 `forge_mcp/docs/mjcf/*.md`，通过 `forge_search_docs` 建立段落级搜索索引，也作为 MCP resources 暴露：`mjcf://<element>` 和 `mjcf://index`。

Blender RST 文档位于 `forge_mcp/docs/blender/`，包括 `api/` 和 `manual/`。可用 `source="mjcf"`、`"blender"`、`"blender_api"` 或 `"blender_manual"` 限定搜索：

```python
forge_search_docs(query="bpy.ops.mesh.bevel", source="blender_api")
forge_search_docs(query="bevel modifier", source="blender_manual", max_results=5)
forge_search_docs(query="condim", source="mjcf")
```

Forge 建模应先读取相应的 `create` 或 `modify` skill。实际检查行为由 `FORGE_MCP_SKILL_GATE` 控制：默认 `soft` 不阻止操作，而是在成功调用后附带一次阅读提示；`strict` 才会拒绝尚未读取所需 skill 的操作。`forge_execute` 对显式调用 `bpy.ops.forge.*` 或通过 `Forge_*` 属性组写入采用相同策略；普通 Blender 建模脚本不受这一 Forge 检查限制。完整创作规则见[英文 MCP Skills](../../en/mcp_skills.md)。

`forge_execute` 会自动向脚本注入 `bpy` 和 `mathutils`。脚本必须把 JSON 可序列化的字典赋给 `result`，例如 `result = {"scene": bpy.context.scene.name}`。

## 工具概览

`forge_mcp.tools` 按模块注册工具，主要包括：

- `create.py`：创建 link、joint、geometry、material、sensor、camera 等 MJCF 元素；
- `modify.py`：修改模型、geometry、collider、site、joint、actuator 等类型；
- `utilities.py`：场景信息、批量重命名、按 tag 选择等；
- `scene.py`：对象信息、测量、变换、属性设置、重命名、删除和执行操作；
- `geometry.py`：对 Forge visual mesh 执行 CoACD 凸分解；
- `io.py`：MJCF 导入/导出及 blend 文件保存；
- `capture.py`：截取 Blender 区域或窗口；
- `blendfile.py`：blend 文件摘要、缺失外部文件和链接库检查；
- `docs.py`：MJCF 与 Blender 文档全文搜索；
- `skill.py`：读取 skill 全文或指定章节。

所有工具都带有 MCP `ToolAnnotations`。写操作、删除、导入、CoACD 和保存等高风险操作会标记相应的 destructive hint 或 approval hint。

## 开发与测试

在完整仓库根目录执行：

```bash
uv sync
uv run pytest tests/mcp/unit tests/mcp/integration
```

`uv sync` 把 `forge-mcp` 以可编辑模式安装到根 `.venv`，并安装插件测试依赖。也可使用 `uv sync --all-packages`。端到端测试需要 Blender，见[开发 Forge](../../cn/development.md)。

仅开发服务包时，可在独立源码目录创建环境：

```bash
cd mcp-server
uv venv --python 3.11
uv pip install --editable .
```

保留 `forge_mcp/skills/` 和 `forge_mcp/docs/`。安装脚本与客户端启动步骤只在[安装与连接](../MCP_INSTALL.zh-CN.md)维护。
