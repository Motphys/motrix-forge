# Copyright (C) 2020-2026 Motphys Technology Co., Ltd. All Rights Reserved.
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This file is part of Motrix Forge.
#
# Motrix Forge is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Motrix Forge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Motrix Forge. If not, see <https://www.gnu.org/licenses/>.
# ==============================================================================

"""Build the manual and synchronize static output for GitHub or GitLab Pages."""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1]


def git(directory, *args):
    return subprocess.check_output(
        ["git", "-c", f"safe.directory={Path(directory).resolve().as_posix()}", "-C", str(directory), *args],
        text=True,
        encoding="utf-8",
    ).strip()


def find_target(repository, branch):
    for record in git(repository, "worktree", "list", "--porcelain", "-z").split("\0\0"):
        fields = record.split("\0")
        if f"branch refs/heads/{branch}" in fields:
            return Path(next(field[9:] for field in fields if field.startswith("worktree ")))
    raise ValueError(f"No {branch} worktree found. Create the orphan {branch} worktree first.")


def validate_target(repository, target, site, branch):
    target = target.resolve(strict=True)
    site = site.resolve()
    if target == repository or target.is_relative_to(repository) or repository.is_relative_to(target):
        raise ValueError("The page worktree must be separate from the development checkout.")
    if target == site or target.is_relative_to(site) or site.is_relative_to(target):
        raise ValueError("Build output and the page worktree must not overlap.")
    if not (target / ".git").is_file():
        raise ValueError("Target is not a linked Git worktree.")
    if git(target, "symbolic-ref", "HEAD") != f"refs/heads/{branch}":
        raise ValueError(f"Target must have the {branch} branch checked out.")
    source_common = Path(git(repository, "rev-parse", "--path-format=absolute", "--git-common-dir")).resolve()
    target_common = Path(git(target, "rev-parse", "--path-format=absolute", "--git-common-dir")).resolve()
    if source_common != target_common:
        raise ValueError("Target belongs to a different repository.")
    if git(target, "status", "--porcelain", "--untracked-files=all"):
        raise ValueError("The page worktree has pending changes. Commit or preserve them before synchronizing.")
    # Check every path before any cleanup; never follow a link outside the target.
    for path in target.rglob("*"):
        if (
            path.is_symlink()
            or getattr(path, "is_junction", lambda: False)()
            or not path.resolve().is_relative_to(target)
        ):
            raise ValueError(f"Unsafe link in target: {path}")
    return target


def synchronize(site, target, platform):
    if not (site / "index.html").is_file():
        raise ValueError("Build output is missing index.html.")
    # validate_target has checked the absolute target and every descendant.
    # Keep the linked worktree's .git file, including for an unborn branch.
    for path in target.iterdir():
        if path.name == ".git":
            continue
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
    shutil.copytree(site, target, dirs_exist_ok=True)
    (target / ".nojekyll").touch()
    shutil.copy2(DOCS / ".gitattributes", target / ".gitattributes")
    if platform == "gitlab":
        shutil.copy2(DOCS / "deployment/gitlab-pages.yml", target / ".gitlab-ci.yml")
    else:
        workflows = target / ".github/workflows"
        workflows.mkdir(parents=True, exist_ok=True)
        shutil.copy2(DOCS / "deployment/github-pages.yml", workflows / "pages.yml")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--platform",
        choices=("github", "gitlab"),
        default="github",
        help="Publishing platform (default: github; gh-pages branch, or page for gitlab)",
    )
    parser.add_argument("--target", type=Path, help="Override the automatically discovered page worktree")
    parser.add_argument(
        "--dry-run", action="store_true", help="Validate paths and show the plan without building or copying"
    )
    args = parser.parse_args()
    repository = Path(git(DOCS, "rev-parse", "--show-toplevel")).resolve()
    site = DOCS / "site"
    branch = "gh-pages" if args.platform == "github" else "page"
    target = validate_target(repository, args.target or find_target(repository, branch), site, branch)
    print(f"Publish: {args.platform} ({branch})", flush=True)
    print(f"Build: {DOCS}", flush=True)
    print(f"Static output target: {target}", flush=True)
    if args.dry_run:
        print("Dry run: no files changed.")
        return
    subprocess.run([sys.executable, str(DOCS / "scripts/docs.py"), "build", "--strict"], check=True)
    # Reject unresolved LFS pointers instead of publishing them as images/videos.
    for path in site.rglob("*"):
        if path.is_file():
            with path.open("rb") as stream:
                if stream.read(128).startswith(b"version https://git-lfs.github.com/spec/"):
                    raise ValueError(f"Unresolved Git LFS asset: {path}. Run git lfs pull first.")
    # Recheck immediately before cleanup in case the worktree changed during build.
    validate_target(repository, target, site, branch)
    synchronize(site, target, args.platform)
    print("Static site and Pages configuration synchronized. No commit or push performed.")
    if args.platform == "github":
        print("GitHub Settings > Pages > Build and deployment: select GitHub Actions.")
    for args in (("add", "--all"), ("commit", "-m", "Publish documentation site"), ("push", "-u", "origin", branch)):
        print(subprocess.list2cmdline(["git", "-C", str(target), *args]))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
