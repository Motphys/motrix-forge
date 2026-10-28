# 开发 Forge

Forge 的 Blender 插件、Agent 侧 MCP 服务和文档站点位于同一个仓库，共用根目录的 `.venv`。根据修改范围选择验证方式。

## 工程结构

```shell
Motrix-Forge/
├── addon/
│   └── Forge/              # Blender 插件源码、资源与 MCP Bridge
├── docs/                   # 独立的中英文文档站点
├── mcp-server/
│   └── forge_mcp/          # Agent 侧 stdio MCP 服务、工具、Skills 与文档索引
├── tests/
│   ├── forge/              # Blender 插件测试
│   └── mcp/                # MCP 单元、协议集成及端到端测试
├── pyproject.toml          # 根开发环境与 uv workspace 配置
├── run_tests.py            # Forge Blender 测试入口
└── run_all_tests.py        # 全部测试套件入口
```

插件负责在 Blender 中实际操作场景，MCP Server 负责对外提供工具接口，通过 TCP 调用插件的 MCP Bridge。文档工具也使用根目录的 `.venv`，依赖统一声明在根目录的 `pyproject.toml` 中。

## 准备开发环境

根项目声明的 Python 版本范围是 **3.11 ≤ 版本 < 3.14**（`>=3.11,<3.14`）。安装 uv 后，在仓库根目录执行：

```bash
git lfs pull
uv sync
```

`uv sync` 创建共享的 `.venv`，安装根开发依赖，并以可编辑模式安装 workspace 成员 `mcp-server` 中的 `forge-mcp`。修改服务源码后，不需要反复重新安装该包。

插件测试还需要本机安装受支持的 Blender；Blender 内的功能依赖安装方法见[配置 Forge：依赖管理](preferences.md#dependencies依赖管理)。

## Python 代码检查与格式化

在仓库根目录运行以下命令。`ruff.toml` 和 `addon/ruff.toml` 将 Ruff 的文件发现范围限制为 `.py` 脚本，Markdown、Notebook 等其他文件不在处理范围内。

```bash
uv run ruff format .
uv run ruff check .
uv run ruff format --check .
```

`format` 执行格式化；`check` 检查代码规则，`format --check` 检查格式，后两者均不修改文件。

## 运行测试

在仓库根目录根据修改范围选择：

| 修改范围 | 验证入口 |
| --- | --- |
| MCP 工具逻辑与协议，不启动 Blender | `uv run pytest tests/mcp/unit tests/mcp/integration` |
| Forge 插件 | `uv run python run_tests.py` |
| MCP 与 Blender 的实际调用 | `uv run python tests/mcp/e2e/driver.py` |
| 所有测试套件 | `uv run python run_all_tests.py` |

`run_tests.py` 查找 Blender 4.5+，优先使用发现的最新版本，并通过独立的后台 Blender 进程运行插件测试。需要指定可执行文件时，在 PowerShell 中设置：

```powershell
$env:BLENDER_PATH = 'C:\Program Files\Blender Foundation\Blender 4.5\blender.exe'
uv run python run_tests.py
```

把示例路径替换为实际安装位置。仅筛选相关插件测试时，可以继续传入 pytest 参数：

```bash
uv run python run_tests.py -k inertia
```

`run_all_tests.py` 还包含完整模型矩阵的端到端测试，各套件顺序执行。

## 验证界面改动

1. 将当前 `addon/Forge` 打包并安装到用于测试的 Blender，确认启用的是当前源码版本。
2. 重启 Blender，打开用于复现的模型。
3. 检查改动涉及的 Operator、属性面板、Gizmo 或导入导出行为。
4. 同步更新受影响的中文和英文操作文档。

后台测试可验证数据和操作逻辑；涉及布局、交互或视口预览的改动还需要在 Blender 界面中检查。

## 修改文档站点

先在仓库根目录执行 `uv sync` 安装依赖，再使用共享的根目录 `.venv` 预览站点：

```powershell
python docs/scripts/docs.py serve
```

打开 <http://127.0.0.1:8000>。修改 Markdown、图片、样式或模板后自动重新构建；修改 `docs/scripts/docs_hooks.py` 后需重启预览服务。

构建发布前使用的静态 HTML：

```powershell
python docs/scripts/docs.py build --strict
```

结果位于被 Git 忽略的 `docs/site/`，不用手工维护 HTML。中文与英文页面使用对应文件名；新增操作章节放在各语言的 `forge_docs/` 中，构建时自动加入导航。详见[本地预览](preview.md)。

## 提交前检查

- 根据修改范围运行相关测试，记录验证环境和结果。
- 页面或功能说明同时维护中英文版本，检查语言切换、图片和锚点链接。
- 不将 `.venv` 或生成的 `docs/site/` 加入提交。
- 反馈问题时提供 Blender 版本、源码 commit、复现步骤、预期与实际结果及相关日志。

开始了解插件操作时，可以继续阅读[使用手册目录](forge_docs.md)。
