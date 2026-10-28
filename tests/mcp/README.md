# forge-mcp 测试

三层测试:Tier 1/2 不需要 Blender,秒级,可进 CI;Tier 3 需要 Blender 4.5。

## Tier 1 — 单元测试(`tests/unit/`)

直接 import `forge_mcp.*`,不 spawn 任何进程,覆盖 server 纯逻辑:

- `test_skills.py` — skills 加载、section 切分/精确匹配/子串/歧义/未命中。
- `test_docs.py` — MJCF 文档加载、`search_docs` 命中/回退/空查询/截断。
- `test_tool_filter.py` — `FORGE_TOOLS` 过滤(readonly / create / modify / 别名 / 子串 / 无效条件拒绝)。
- `test_blender_templates.py` — selection order、shape socket、递归删除、场景配置、tendon、材质、CoACD、I/O 生成代码回归。
- `test_resources.py` — `mjcf://` 资源注册与读取。
- `test_tools_skill.py` — `forge_skill` 工具整篇/按节/未知 skill/section。

## Tier 2 — 协议集成测试(`tests/integration/test_protocol.py`)

用官方 mcp 客户端库 spawn 真实 server(stdio),走完整 JSON-RPC 帧:

- initialize(serverInfo / instructions)、list_tools(55)、list_resources(16)。
- read_resource(`mjcf://body` / `mjcf://index` / 未知 URI 报错)。
- call_tool(`forge_skill` 整篇 / section / 未知 section / 未知 skill / 缺参数;`forge_search_docs`)。
- `FORGE_TOOLS` 参数化(readonly → 8 / create → 21（20 个 create + `forge_skill`）/ bogus → 启动失败)。

## 运行 Tier 1 + Tier 2

```bash
uv run --directory mcp-server pytest tests/mcp/unit tests/mcp/integration
```

## Tier 3 — 端到端测试(`tests/e2e/driver.py`)

驱动脚本会:

1. spawn 一个**一次性** headless Blender 4.5(`--factory-startup`),按
   `tests/forge/conftest.py` 的方式注册 Forge 属性组、相关操作符和
   Forge Library,并在 `FORGE_E2E_PORT`(默认 `9877`,**绝不占用** live 的 `9876`)
   启动 MCP TCP bridge;
2. spawn forge-mcp(stdio),`FORGE_MCP_PORT` 指向该 bridge;
3. 通过 mcp 客户端逐个调用真实 `forge_*` 工具并断言(每个场景前
   `read_homefile(use_factory_startup=True)` 重置 + 取消选中，并校验重置结果)。
4. 在同一个 background Blender 中导入最小 MJCF，再导出为新 MJCF，验证
   后台同步 I/O 的完整 MCP 往返。

```bash
python tests/mcp/e2e/driver.py            # 或: --blender PATH --port N
```

Blender 路径**自动发现**:优先 PATH 上的 `blender`,再扫标准安装目录
(`Program Files / Program Files (x86)` 下的 `Blender Foundation\Blender*`),
优先 4.x。也可用 `--blender PATH` / `FORGE_BLENDER` 显式指定。

要求:Blender 4.5，以及仓库内的 `addon` 目录。

Blender 侧的回归套件(`tests/forge/`)继续按仓库既有命令在 Blender 4.5
内运行(bundled pytest)。

## 注意事项

- `read_homefile(use_factory_startup=True)` 会默认选中 Cube,创建类 op 的 poll 要求"无选中",
  所以每个场景前先取消选中(driver 已处理)。
- 端口冲突:用独立端口 + 轮询探测,失败重试。
- Blender 5.2 无 bundled pytest / 缺 tetgen,一律用 4.5 验证。
