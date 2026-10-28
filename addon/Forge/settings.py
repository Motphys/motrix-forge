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

import logging
import os
import subprocess
import sys

import bpy
from bpy.props import BoolProperty, EnumProperty, FloatProperty, IntProperty, StringProperty
from bpy.types import AddonPreferences, Context, Operator

from .core import dependency as deps
from .mcp.constants import DEFAULT_HOST, DEFAULT_PORT, TIMER_ACTIVE_INTERVAL

logger = logging.getLogger("Forge Tool")

PYPATH = sys.executable

# ── Inject into settings (backward compat) ──────────────────────────
dependencies = deps.get_dependency_manager()
pip = dependencies.pip
ensurepip = dependencies.ensurepip
preview_collections = {}


def Load_Icon():
    import bpy.utils.previews

    pcoll = bpy.utils.previews.new()

    addon_dir = os.path.dirname(__file__)
    icon_path = os.path.join(addon_dir, "icons", "forge.png")

    if os.path.exists(icon_path):
        pcoll.load("forge", icon_path, "IMAGE")
        preview_collections["forge"] = pcoll


def Unload_Icon():
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()


def Get_Logo_Icon_ID():
    pcoll = preview_collections.get("forge")

    if pcoll:
        icon = pcoll.get("forge")
        if icon:
            return icon.icon_id
        else:
            0


def Get_Icon(package):
    """Icon for dependency availability display."""
    return "CANCEL" if package is None else "CHECKMARK"


def Draw_Package(box, package):
    """Draw a dependency row in the addon preferences panel."""
    mgr = dependencies
    dependency = mgr.get_dep(package)
    col = box.column(align=True)
    col.label(text=dependency.message, icon=Get_Icon(dependency.module))
    row = col.row(align=True)
    row.operator("wm.url_open", text="Visit package website").url = dependency.url
    if dependency.module is None and dependency.pip_installable and mgr.pip:
        row.operator(Forge_OT_PipInstall.bl_idname, text="Install with PIP").package = dependency.package
    elif dependency.pip_installable and mgr.pip:
        _op = row.operator(Forge_OT_PipInstall.bl_idname, text="Upgrade with PIP").package = dependency.package
    return row


class Forge_OT_PipInstall(Operator):
    """Install the package by calling pip install"""

    bl_idname = "forge.pip_install"
    bl_label = "Install the package"
    bl_options = {"REGISTER", "INTERNAL"}

    package: bpy.props.StringProperty(name="Package names")  # type: ignore

    def execute(self, context: Context):
        """Execute pip install for the specified package(s).

        Runs ``pip install --upgrade`` with the operator's ``package``
        property, reports success/failure, and prompts the user to restart
        Blender after a first install.
        """
        # https://github.com/robertguetzkow/blender-python-examples/tree/master/add_ons/install_dependencies
        environ_copy = dict(os.environ)
        environ_copy["PYTHONNOUSERSITE"] = "1"  # is set to disallow pip from checking the user site-packages
        cmd = [PYPATH, "-m", "pip", "install", "--upgrade"] + self.package.split(" ")
        ok = subprocess.call(cmd, env=environ_copy) == 0
        if ok:
            first_install = self.package in dependencies and dependencies[self.package] is None
            if first_install:
                self.report({"INFO"}, "%s installed successfully. Please restart Blender to see effect." % self.package)
            else:
                self.report({"INFO"}, "%s upgraded successfully. Please restart Blender to see effect." % self.package)
            return {"FINISHED"}
        else:
            self.report({"ERROR"}, "Cannot install %s, see console output for details" % self.package)
            return {"CANCELLED"}


class Forge_OT_EnsurePip(Operator):
    """Install PIP by using ensurepip module"""

    bl_idname = "forge.ensure_pip"
    bl_label = "Install PIP"
    bl_options = {"REGISTER", "INTERNAL"}

    def execute(self, context: Context):
        """Execute ensurepip to bootstrap pip for the Blender Python environment.

        Runs ``python -m ensurepip``, reports success/failure, and warns the
        user if Blender appears to be installed as a snap package (which
        does not allow writing files).
        """
        environ_copy = dict(os.environ)
        environ_copy["PYTHONNOUSERSITE"] = "1"  # is set to disallow pip from checking the user site-packages
        cmd = [PYPATH, "-m", "ensurepip"]
        ok = subprocess.call(cmd, env=environ_copy) == 0
        if ok:
            if "snap" in sys.executable:
                msg = """It seems that your Blender is a snap package. Suchpackages does not support writing any files.
                ReinstallBlender to be able to use external Python packages"""
                self.report({"WARNING"}, msg)
            else:
                self.report({"INFO"}, "PIP installed successfully. Please restart Blender to see effect.")
            return {"FINISHED"}
        else:
            self.report({"ERROR"}, "Cannot install PIP, see console output for details")
            return {"CANCELLED"}


# Default for `Forge_prefs.coacd_name_template`, and the fallback the operators
# use when `get_addon_prefs()` has nothing to return — the documented headless
# case, where the operator classes are registered without an add-on entry and the
# preferences collection therefore has no "Forge" key to read.
DEFAULT_COACD_NAME_TEMPLATE = "?_hull_#"


def _redraw_viewports(self, context):
    """Refresh previews in every window when a global display toggle changes."""
    for window in context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == "VIEW_3D":
                area.tag_redraw()


def _update_mcp_logging(self, context):
    """Apply the logging preference to the bridge without restarting it."""
    from .mcp.utils import get_server

    server = get_server()
    if server is not None:
        server.logging = self.use_log


class Forge_prefs(AddonPreferences):
    """Forge addon preferences displayed in Blender's Add-on Preferences panel.

    Provides configuration tabs for General settings (CoACD name template and viewport previews),
    Dependencies (pip, tetgen, coacd), and MCP server (host, port, polling
    intervals, auto-start, and debug logging).
    """

    bl_idname = __package__

    prefs_tabs: EnumProperty(
        items=(
            ("General", "General", "General Settings"),
            ("MCP", "MCP Server", "MCP Server"),
            ("Dependencies", "Dependencies", "Dependencies"),
        ),
        default="General",
    )  # type: ignore

    coacd_name_template: StringProperty(
        name="CoACD Name Template",
        description="Name template used for generated hulls.\n? = original mesh name\n# = hull id",
        default=DEFAULT_COACD_NAME_TEMPLATE,
    )  # type: ignore

    show_collider_preview: BoolProperty(
        name="Collider Preview",
        description="Draw GPU collider surfaces in all 3D viewports",
        default=True,
        update=_redraw_viewports,
    )  # type: ignore

    show_inertial_preview: BoolProperty(
        name="Inertial Preview",
        description="Draw GPU inertia boxes in all 3D viewports",
        default=True,
        update=_redraw_viewports,
    )  # type: ignore

    autostart_error: StringProperty(
        name="Autostart error",
        description="Store a startup error message",
        default="",
    )  # type: ignore

    host: StringProperty(
        name="Host",
        default=DEFAULT_HOST,
        description="TCP host address for the MCP server to connect to",
    )  # type: ignore
    port: IntProperty(
        name="Port",
        default=DEFAULT_PORT,
        min=1024,
        max=65535,
        description="TCP port for the MCP server to connect to",
    )  # type: ignore
    token: StringProperty(
        name="Authentication Token",
        default="",
        subtype="PASSWORD",
        description="Shared token required by MCP clients; mandatory when binding outside localhost",
    )  # type: ignore
    autostart: BoolProperty(
        name="Auto-start server",
        default=True,
        description="Start the TCP server automatically when Blender starts",
    )  # type: ignore
    autostart_delay: FloatProperty(
        name="Auto-start delay",
        default=2.0,
        min=0.0,
        max=30.0,
        subtype="TIME_ABSOLUTE",
        description="Time to wait after Blender startup before starting the server",
    )  # type: ignore
    active_interval: FloatProperty(
        name="Active interval",
        default=TIMER_ACTIVE_INTERVAL,
        min=0.01,
        max=1.0,
        subtype="TIME_ABSOLUTE",
        description="Timer interval when processing requests (lower = more responsive but higher CPU)",
    )  # type: ignore
    idle_interval: FloatProperty(
        name="Idle interval",
        default=1.0,
        min=0.1,
        max=10.0,
        subtype="TIME_ABSOLUTE",
        description="Timer interval when idle (higher = lower CPU usage)",
    )  # type: ignore
    idle_delay_interval: FloatProperty(
        name="Idle delay",
        default=5.0,
        min=1.0,
        max=60.0,
        subtype="TIME_ABSOLUTE",
        description="Time of inactivity before switching to idle interval",
    )  # type: ignore
    use_log: BoolProperty(  # type: ignore
        name="Log requests to console",
        default=False,
        description="Log requests and responses to Blender's system console; takes effect immediately",
        update=_update_mcp_logging,
    )  # type: ignore

    def draw(self, context: Context):
        """Draw the addon preferences UI with tabbed sections.

        Renders the preference tabs (General, Dependencies, MCP) and their
        corresponding controls: CoACD name template, pip/package management,
        MCP host/port/polling configuration, auto-start settings, and debug
        logging options.
        """

        layout = self.layout
        row = layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)

        if self.prefs_tabs == "General":
            col = layout.column()
            col.prop(self, "coacd_name_template")
            box = layout.box()
            box.label(text="Viewport Previews", icon="HIDE_OFF")
            box.prop(self, "show_collider_preview")
            box.prop(self, "show_inertial_preview")

        elif self.prefs_tabs == "Dependencies":
            box = layout.box()
            row = Draw_Package(box, "pip")
            if pip is not None:
                row.operator(Forge_OT_PipInstall.bl_idname, text="Upgrade PIP").package = "pip setuptools wheel"
            else:
                if ensurepip is not None:
                    row.operator(Forge_OT_EnsurePip.bl_idname, text="Install PIP")
                else:
                    row.operator(
                        "wm.url_open", text="Installation instructions"
                    ).url = "https://pip.pypa.io/en/stable/installing/"
            Draw_Package(box, "tetgen")
            Draw_Package(box, "coacd")

        elif self.prefs_tabs == "MCP":
            box = layout.box()
            box.prop(self, "host")
            box.prop(self, "port")
            box.prop(self, "token")

            box = box.box()
            box.label(text="Polling", icon="TIME")
            box.prop(self, "active_interval")
            box.prop(self, "idle_interval")
            box.prop(self, "idle_delay_interval")

            box = layout.box()
            box.label(text="Startup", icon="PLAY")
            box.prop(self, "autostart")
            box.prop(self, "autostart_delay")

            box = layout.box()
            box.label(text="Debug", icon="CONSOLE")
            box.prop(self, "use_log")

            if self.autostart_error:
                box.label(text=self.autostart_error, icon="ERROR")


def get_addon_prefs() -> Forge_prefs | None:
    """Read current addon preferences.

    Exported for external callers as ``settings.get_addon_prefs()``.
    """

    addon_name = os.path.splitext(__name__)[0]
    preferences = bpy.context.preferences
    try:
        return preferences.addons[addon_name].preferences
    except KeyError:
        # During headless tests (and while the add-on is being enabled),
        # Blender may not have created the preferences entry yet.
        return None


classes = (
    Forge_prefs,
    Forge_OT_PipInstall,
    Forge_OT_EnsurePip,
)
