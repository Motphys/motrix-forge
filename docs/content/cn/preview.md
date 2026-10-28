# 本地预览

本站读取 `docs/content` 中的 Markdown 并构建 HTML。预览服务会监听文档和图片修改，重新构建并刷新浏览器。在各语言的 `forge_docs/` 目录中新增章节后，会自动加入对应语言的导航。

## 启动

在仓库根目录执行（使用项目支持的 Python 版本）：

```powershell
uv sync
python docs/scripts/docs.py serve
```

`uv sync` 将根目录 `pyproject.toml` 中的文档依赖安装到共享的根目录 `.venv`，启动脚本使用该环境运行 MkDocs。打开 <http://127.0.0.1:8000>；按 `Ctrl+C` 停止。

也可先进入 `docs/`，执行 `python scripts/docs.py serve`，仍使用仓库根目录的 `.venv`。

自定义端口：

```powershell
python docs/scripts/docs.py serve --dev-addr 127.0.0.1:8080
```

## 构建

```powershell
python docs/scripts/docs.py build --strict
```

输出位于 `docs/site/`，包含 HTML、图片、样式和搜索索引。站点的内容、资源、主题和配置均在 `docs/` 内，构建依赖使用共享的根目录 `.venv`。

## 准备发布

开发分支保留 Markdown 源码，孤立的 `gh-pages` 分支仅保存构建后的静态网站与发布配置。其 worktree 位于 `../motrix-forge-pages`，在仓库根目录执行：

```powershell
python docs/scripts/prepare_pages.py
```

脚本会严格构建并同步静态文件，保留目标目录的 `.git`，添加 `.nojekyll`，保留 LFS 属性，并写入 GitHub Actions 工作流，由 Action 拉取 LFS 实际资源后上传 Pages 产物。目标存在未提交修改或构建产物含未解析的 LFS 指针时会停止。它不自动提交或推送，完成后会列出需要执行的 Git 命令。推送前，在 GitHub **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**；如果 `github-pages` 环境限制部署分支，需要允许 `gh-pages`。

GitLab 发布时添加 `--platform gitlab`，使用 `page` worktree，并复制 GitLab Pages 配置和 LFS 属性。提交、推送 `page` 后，GitLab 流水线将静态文件打包到 `public/` 并发布。模板位于 `docs/deployment/gitlab-pages.yml`，需要 GitLab 实例启用 Pages 并有可用的 Runner。

## 语言与布局

左侧显示当前语言的章节，右侧显示当前页面的目录。在左下角切换 **简体中文 / English** 会跳到当前章节的对应译文。搜索结果也按当前语言筛选。窄屏可使用顶部菜单打开章节导航。

点击左侧分组标题或箭头可折叠、展开章节列表，也支持键盘操作。进入页面时自动展开当前页面所在分组，其他分组的状态会在页面跳转和语言切换后保留。同一浏览器标签页内的导航滚动位置也会保留。

窄屏顶部右侧的目录按钮会从右侧展开本页目录，点击标题跳转后自动收起。两侧导航不会同时展开；点击遮罩、关闭按钮或按 `Esc` 可以收起目录，恢复宽屏后重新显示常驻目录。

点击正文图片可放大预览；也可用键盘选中图片后按 `Enter` 或空格打开。点击放大的图片、图片外的遮罩、右上角关闭按钮或按 `Esc` 退出，返回原来的阅读位置。图片预览支持浅色、黑色主题和窄屏显示。

正文优先在视窗中央显示；空间不足时，两侧导航收起为菜单以保留阅读宽度。侧栏底部和窄屏顶部均可切换 **浅色 / 黑色主题**。首次访问跟随系统主题，手动选择后会记住偏好，在刷新和中英文切换后继续生效。

## 内容维护

- 中文章节位于 `docs/content/cn/forge_docs/`，英文位于 `docs/content/en/forge_docs/`；同名文件构成翻译对。
- 中英文共用 `docs/content/assets/` 中的素材；手册截图放在 `assets/images/manual/`，其他图片放在 `assets/images/`，视频和封面分别放在 `assets/videos/`、`assets/posters/`。
- `.md` 和无扩展名链接均支持；构建时转换成 HTML 链接并保留锚点。
- 原始 Markdown 的章节跳转保留供 Obsidian 阅读；网页使用统一导航。
- MCP 文档和 skills 的站点副本位于 `docs/content/reference/`，演示资源位于 `docs/content/assets/`。原文件变更后，在完整仓库中执行 `python docs/scripts/sync_sources.py` 更新副本；预览和构建不再读取外部原文件。
- 从 Git LFS 仓库新克隆后，运行 `git lfs pull` 获取真实图片。
- 修改 `docs/scripts/docs_hooks.py` 后需要重启预览服务。

构建与预览命令参见 [MkDocs CLI](https://www.mkdocs.org/user-guide/cli/)。
