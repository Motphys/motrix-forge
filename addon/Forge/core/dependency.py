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

"""
Lazy dependency manager for Forge's external Python packages (pip, tetgen, coacd).

Eliminates the module-level side effects that previously ran on every ``import utils``.
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger("Forge Tool")


def require_gltf_addon(operation: str) -> None:
    """Require the loaded glTF add-on and its registered import/export operator."""
    import addon_utils
    import bpy

    message = (
        f"glTF/GLB {operation} requires the glTF 2.0 add-on (io_scene_gltf2). "
        "Enable it in Edit > Preferences > Add-ons."
    )
    if not addon_utils.check("io_scene_gltf2")[1]:
        raise RuntimeError(message)
    try:
        namespace = bpy.ops.import_scene if operation == "import" else bpy.ops.export_scene
        namespace.gltf.get_rna_type()
    except (AttributeError, RuntimeError) as exc:
        raise RuntimeError(message + " Its operator is unavailable; reload the add-on.") from exc


class Dependency:
    """Definition of an external dependency package."""

    def __init__(self, package: str, url: str):
        """Initialize a dependency definition with package name and PyPI URL."""
        self.package = package
        self.url = url
        self._module: Any = None
        self.pip_installable = False

    @property
    def module(self):
        """Return the imported module object, or None if not yet imported."""
        return self._module

    @module.setter
    def module(self, mod):
        """Set the imported module object after a successful import."""
        self._module = mod

    @property
    def message(self) -> str:
        """Return a human-readable availability message for this dependency.

        Returns:
            A string indicating whether the package is available.
        """
        return f"{self.package} package is {'' if self._module else 'not '}available"


class DependencyManager:
    """Lazy container for external dependency checks.

    Usage::

        mgr = DependencyManager()
        if mgr.tetgen:
            ...
        settings.dependencies = mgr  # dict-like access via .items()
    """

    def __init__(self):
        """Initialize the manager with no cached pip state and an empty dependency registry."""
        self._pip: Any = None
        self._ensurepip: Any = None
        self._pip_checked = False
        self._deps: dict[str, Dependency] = {}

    # ── Lazy accessors ───────────────────────────────────────────────

    @property
    def pip(self):
        """Return the pip module if available, triggering lazy discovery on first access."""
        self._ensure_pip_checked()
        return self._pip

    @property
    def ensurepip(self):
        """Return the ensurepip module if available, triggering lazy discovery on first access."""
        self._ensure_pip_checked()
        return self._ensurepip

    @property
    def tetgen(self):
        """Return the tetgen module if installed, or None; triggers lazy discovery on first access."""
        return self._get_dep("tetgen")

    @property
    def coacd(self):
        """Return the CoACD module if installed, or None; triggers lazy discovery on first access."""
        return self._get_dep("coacd")

    # ── Internal ─────────────────────────────────────────────────────

    def _ensure_pip_checked(self):
        """Attempt to import pip (and ensurepip as a fallback) exactly once, caching results."""
        if self._pip_checked:
            return
        self._pip_checked = True
        dep = self._add("pip", "https://pypi.org/project/pip/")
        try:
            import pip as _pip_mod

            dep.module = _pip_mod
            self._pip = _pip_mod
        except ImportError:
            print(dep.message)
            self._pip = None

        if self._pip is None:
            try:
                import ensurepip as _ep

                self._ensurepip = _ep
            except ImportError:
                self._ensurepip = None
                print("Ensurepip module is not available, user will not be able to install PIP automatically")
        else:
            self._ensurepip = None
            print("PIP is already installed, no need to call ensurepip")

    def _get_dep(self, name: str) -> Any:
        """Return the module object for *name*, initializing it lazily if not yet registered."""
        if name not in self._deps:
            self._init_dep(name)
        return self._deps[name].module

    def get_dep(self, name: str) -> Dependency:
        """Return the Dependency object for *name* (must already be registered)."""
        return self._deps[name]

    def _init_dep(self, name: str):
        """Register and attempt to import the named dependency (tetgen, coacd, or pip)."""
        if name == "tetgen":
            dep = self._add("tetgen", "https://pypi.org/project/tetgen/")
            dep.pip_installable = True
            try:
                import tetgen as _mod

                dep.module = _mod
            except ImportError:
                pass
        elif name == "coacd":
            dep = self._add("CoACD", "https://pypi.org/project/coacd/")
            dep.pip_installable = True
            try:
                import coacd as _mod  # type: ignore

                dep.module = _mod
            except ImportError:
                pass
        elif name == "pip":
            self._ensure_pip_checked()

    def _add(self, package: str, url: str) -> Dependency:
        """Register a new Dependency and store it keyed by lowercased package name."""
        dep = Dependency(package, url)
        self._deps[package.lower()] = dep
        return dep

    # ── Dict-like access for settings.draw_package ───────────────────
    def init(self):
        """Eagerly trigger lazy discovery of pip, tetgen, and coacd."""
        self._ensure_pip_checked()
        self._get_dep("tetgen")
        self._get_dep("coacd")

    def items(self):
        """Return the internal (name, Dependency) pairs for dict-like iteration."""
        return self._deps.items()

    def __getitem__(self, key: str) -> Dependency:
        """Return the Dependency for *key* (supports dict-style access)."""
        return self._deps[key]

    def __contains__(self, key: str) -> bool:
        """Return True if *key* names a registered dependency."""
        return key in self._deps


# ── Singleton + injection into settings ────────────────────────────
# Kept for backward compatibility with settings.py and other callers.
# Only the first import triggers the eager checks.

_INSTANCE = DependencyManager()
_INSTANCE.init()


def get_dependency_manager() -> DependencyManager:
    """Return the module-level singleton DependencyManager that was eagerly initialized."""
    return _INSTANCE


def register():
    """Register the dependency manager and log the status of all detected dependencies.

    Logs which packages are available at the INFO level. Intended to be called
    during Blender addon registration.
    """
    good_names = [d.package for d in _INSTANCE.items() if d.module is not None and d.package is not None]
    if good_names:
        logger.info("Dependencies available: %s.", ", ".join(good_names))
    else:
        logger.info("No dependencies are available.")
