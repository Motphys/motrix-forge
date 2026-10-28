# Local preview

The site builds HTML directly from `docs/content`. The preview server watches Markdown and images and refreshes the browser after edits. New chapter Markdown files are discovered automatically in each language's chapter directory.

## Start

Run from the repository root using the project's supported Python version:

```powershell
uv sync
python docs/scripts/docs.py serve
```

`uv sync` installs documentation dependencies from the root `pyproject.toml` into the shared root `.venv`. The helper uses that environment for MkDocs. Open <http://127.0.0.1:8000>; press `Ctrl+C` to stop.

Alternatively, enter `docs/` and run `python scripts/docs.py serve`; it still uses the repository root `.venv`.

Custom port:

```powershell
python docs/scripts/docs.py serve --dev-addr 127.0.0.1:8080
```

## Build

```powershell
python docs/scripts/docs.py build --strict
```

The generated `docs/site/` contains HTML, images, styles, and a search index. All site content, media, templates, and configuration are inside `docs/`; build dependencies come from the shared root `.venv`. Build output and `.venv` are ignored by Git.

## Prepare a release

Keep Markdown sources in the development branch. The orphan `gh-pages` branch contains only the built static site and deployment metadata. With its worktree at `../motrix-forge-pages`, run from the repository root:

```powershell
python docs/scripts/prepare_pages.py
```

The script builds with strict validation, synchronizes static files while preserving the target's `.git`, adds `.nojekyll`, Git LFS attributes, and a GitHub Actions workflow that downloads LFS assets before deploying the static site. It stops if the target has pending changes or the build contains unresolved LFS pointers. It never commits or pushes; it prints the Git commands to run next. Before pushing `gh-pages`, configure GitHub **Settings → Pages → Build and deployment → Source** to use **GitHub Actions**. If the `github-pages` environment restricts deployment branches, allow `gh-pages`.

For GitLab, add `--platform gitlab` to select the `page` worktree and copy the GitLab Pages configuration and LFS attributes. After committing and pushing `page`, the GitLab pipeline packages the static files into `public/` and publishes them. The template is `docs/deployment/gitlab-pages.yml`; the GitLab instance must have Pages enabled and an available Runner.

## Language and layout

The left sidebar shows chapters in the current language. The right sidebar contains headings from the current page. Use the language selector at the bottom left to switch between **English** and **简体中文** on the same chapter. Search results are filtered by language. On smaller screens, open chapter navigation with the menu button at the top.

Click a sidebar group heading or its arrow to collapse or expand its chapters; keyboard activation is supported. The current page's group opens automatically, while other group states are remembered across page navigation and language changes. The navigation scroll position is also preserved within the same browser tab.

On smaller screens, the contents button at the top right opens the current page outline as a right-hand drawer. Choosing a heading closes it automatically. Only one navigation drawer opens at a time. Click the backdrop or close button, or press `Esc`, to dismiss it. The outline returns to its persistent sidebar on wider screens.

Click an article image to enlarge it, or focus it and press `Enter` or Space. Click the enlarged image or backdrop, use the close button, or press `Esc` to return to your reading position. The preview supports both themes and smaller screens.

The article stays centered in the viewport. When space is limited, navigation collapses to preserve reading width. Switch between **Light / Dark theme** at the bottom of the sidebar or in the compact top bar. The first visit follows your system theme; a manual choice is remembered across reloads and language changes.

## Authoring

Edit chapters in the language directories and keep shared screenshots in `assets/images/manual/`. Both `.md` and extensionless Obsidian links are resolved during the build, with anchors preserved. Portable MCP guide and skill snapshots live in `docs/content/reference/`, and demonstration media in `docs/content/assets/`. Refresh these copies with `python docs/scripts/sync_sources.py` in the full checkout after changing the originals. Preview and builds read no files outside `docs/`. Workspace configuration files are not published. After cloning an LFS repository, run `git lfs pull` to fetch actual images and videos.

Use matching filenames in `cn/forge_docs/` and `en/forge_docs/` to pair translations. Source Markdown keeps its original navigation for Obsidian; the website uses a shared page layout. Restart the preview server after changing `docs/scripts/docs_hooks.py`.

Preview and static builds use the [MkDocs CLI](https://www.mkdocs.org/user-guide/cli/).
