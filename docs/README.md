# Forge documentation site

This directory contains the MkDocs site content, shared media, theme, and scripts. Preview and build use the repository root `.venv`; documentation dependencies are declared in the root `pyproject.toml` and locked in `uv.lock`.

```text
docs/
├── content/             Site Markdown, styles, scripts, and screenshots
│   ├── cn/              Chinese pages
│   ├── en/              English pages
│   ├── reference/       Portable MCP guides and English-only skill snapshots
│   ├── introduction.md  English introduction (built as index.html)
│   ├── introduction.zh-CN.md Chinese introduction
│   └── assets/          Shared static assets for both languages
│       ├── Logo.png     Site logo (case-sensitive filename)
│       ├── images/      Introduction, installation, and preferences images
│       │   └── manual/ Manual chapter screenshots
│       ├── videos/     Demonstration videos
│       ├── posters/    Video preview images
│       ├── stylesheets/ Site CSS
│       └── javascripts/ Site JavaScript
├── theme/               Page templates
├── scripts/             Preview, build hooks, source synchronization, and page preparation
├── deployment/          GitHub Actions and GitLab Pages templates for static branches
├── tests/               Documentation UI script tests
└── mkdocs.yml
```

## Preview and build

At the bottom of the sidebar, theme and language controls appear side by side, with GitHub and official website image links below them. Set the link destinations with `extra.github_url` and `extra.website_url` in `mkdocs.yml`. The labels follow the page language; on narrow screens, open the navigation menu to access these controls and links.

From the full repository root:

```powershell
uv sync
python docs/scripts/docs.py serve
python docs/scripts/docs.py build --strict
```

From this directory, after installing dependencies at the repository root:

```powershell
python scripts/docs.py serve
python scripts/docs.py build --strict
```

Open <http://127.0.0.1:8000>. The helper uses the root `.venv`; generated HTML goes to `site/` here. Markdown, media, styles, and templates rebuild automatically. Restart the server after editing `scripts/docs_hooks.py`.

To build in CI, run `uv sync` and `uv run python docs/scripts/docs.py build --strict` from the repository root. Fetch Git LFS assets before building. The current release workflow builds locally and synchronizes HTML to the `gh-pages` worktree with `scripts/prepare_pages.py`. Use `--platform gitlab` for the `page` worktree; the GitLab CI template only packages and publishes that static output.

## Refresh MCP references and media

The website builds exclusively from files in this directory. MCP runtime guides remain in their original source locations; the site keeps portable copies under `content/reference/`. Shared repository images are copied into `content/assets/images/`, and HD videos into `content/assets/videos/`.

After changing these originals, run this optional command in the full Forge checkout:

```powershell
python docs/scripts/sync_sources.py
```

Review and commit the resulting documentation changes. This synchronization rewrites links to the portable copies; it does not bundle workspace configuration files. It is not required for preview or build, and cannot run without the full source checkout.

## Video preview images

Each case study video has a `poster` attribute in both `content/cn/examples.md` and `content/en/examples.md`. Its PNG cover lives under `content/assets/posters/`, with the same basename as the video: `forge_pipeline.png`, `arbitrary_robotic_arm.png`, or `forge_with_agent.png`.

Replace the PNG to update a cover. If its filename changes, update the corresponding `poster` paths in both language pages. These covers are maintained inside the documentation project and are not overwritten by `sync_sources.py`.

素材统一放在 `content/assets/`，中英文共用：一般图片放 `images/`，手册截图放 `images/manual/`，视频放 `videos/`，封面放 `posters/`。新增素材应使用相对于当前 Markdown 文件的路径，并保持文件名大小写一致。替换 Logo 时更新 `content/assets/Logo.png`；同名替换视频封面即可生效，资源同步脚本不会覆盖封面和文档专用截图。

浏览器标签页图标使用独立的 `content/assets/favicon.ico`，替换 Logo 时也应同步更新该图标。

## Prepare the static page branch

Keep all source edits in the development branch. The separate orphan `gh-pages` branch at `../motrix-forge-pages` contains only built HTML and assets, plus deployment metadata. With its linked worktree already created, run from the repository root:

```powershell
python docs/scripts/prepare_pages.py --dry-run
python docs/scripts/prepare_pages.py
```

The script discovers the worktree checked out on `gh-pages`, validates that it belongs to the same repository and has no pending changes, builds with `--strict`, and replaces its old static output while preserving `.git`. It adds `.nojekyll`, Git LFS attributes, and `.github/workflows/pages.yml` from `deployment/github-pages.yml`. The workflow downloads LFS assets before uploading the static site to GitHub Pages. Unresolved LFS pointers stop synchronization. Use `--target <path>` to specify the worktree explicitly. The script prints commit and push commands; it never runs them. Commit or preserve pending changes before the next synchronization.

Before pushing `gh-pages`, configure GitHub **Settings → Pages → Build and deployment → Source** to use **GitHub Actions**. If the `github-pages` environment restricts deployment branches, allow `gh-pages` under **Settings → Environments → github-pages**. Push the generated site and workflow together; the action downloads LFS assets and deploys the existing HTML without rebuilding Markdown.

For the existing GitLab workflow, run `python docs/scripts/prepare_pages.py --platform gitlab`. This selects the `page` worktree and copies Git LFS attributes and `.gitlab-ci.yml` from `deployment/gitlab-pages.yml`.

For GitLab, push the generated `page` branch and let its Pages CI job package the existing HTML into `public/`. No Python or Markdown build runs in CI. The project needs an available Runner and Pages enabled on its GitLab instance. View the pipeline status and then **Deploy → Pages** for the site URL and access settings. The supplied CI template uses `pages: true` (GitLab 17.6+); adapt it to the installed GitLab version if necessary. On older installations, the legacy job named `pages` with `artifacts.paths: [public]` can be used without `pages: true`.

## 中文说明

GitLab Pages 视频分段请求需要产物打包设置 `FF_USE_FASTZIP: "true"` 和 `ARTIFACT_COMPRESSION_LEVEL: "fastest"`，发布模板已包含这两项。修改后需重新运行 Pages 流水线，生成新的产物才会生效。参考 [GitLab 官方媒体播放说明](https://docs.gitlab.com/user/project/pages/introduction/#cannot-play-media-content-on-safari)。

文档依赖统一声明在根目录的 `pyproject.toml` 中，通过 `uv sync` 安装到根目录 `.venv`。在仓库根目录运行 `python docs/scripts/docs.py serve`；进入 `docs/` 后运行 `python scripts/docs.py serve`，两者均使用根目录环境。构建结果为 `docs/site/`。

修改原始 MCP 文档、skills 或演示资源后，先执行 `python docs/scripts/sync_sources.py`，检查同步结果。预览和构建只读取 `docs/` 内的文件。

GitHub 发布目录使用 `../motrix-forge-pages` 中独立的孤立 `gh-pages` 分支。执行 `python docs/scripts/prepare_pages.py` 会自动定位其 worktree，构建并同步静态网站、清理旧产物，保留 `.git`，添加 `.nojekyll`，保留 LFS 属性，并写入 `.github/workflows/pages.yml`，由 Action 拉取 LFS 实际资源后上传 Pages 产物。脚本不提交、不推送，可以先加 `--dry-run` 检查目标。目标目录有未提交修改时会停止，先提交或保存修改再重新同步。推送前，在 GitHub **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**；如果 `github-pages` 环境限制部署分支，需要允许 `gh-pages`。

GitLab 发布使用 `python docs/scripts/prepare_pages.py --platform gitlab`，对应 `page` 分支，保留原有 LFS 属性和 GitLab Pages 配置。

将脚本输出的提交、推送命令执行后，在 GitLab 查看流水线及 **Deploy → Pages**。自建 GitLab 需要管理员启用 Pages，项目需要可运行该任务的 Runner；访问权限在 Pages 设置中配置。
