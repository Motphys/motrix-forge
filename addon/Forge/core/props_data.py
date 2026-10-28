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
Property-definition dictionaries for Forge.

Each model entity type (Link, Joint,
Actuator, …) has up to three companion dicts:

* ``{TYPE}_PROPS`` — list of property *keys*
* ``{TYPE}_PROPS_NAME`` — key → display name mapping
* ``{TYPE}_PROPS_DEFAULT`` — key → default value mapping

These are referenced by property-group declarations and by the export /
serialization pipeline so it can skip writing default-valued attributes.
"""

# ═══════════════════════════════════════════════════════════════════════
# Link
# ═══════════════════════════════════════════════════════════════════════

LINK_PROPS = [
    "mocap",
    "gravcomp",
]

LINK_PROPS_NAME = {
    "mocap": "Mocap",
    "gravcomp": "Gravity compensation",
}

LINK_PROPS_DEFAULT = {
    "mocap": False,
    "gravcomp": 0.0,
}

# ═══════════════════════════════════════════════════════════════════════
# Joint
# ═══════════════════════════════════════════════════════════════════════

JOINT_TYPE_PROPS = {
    "FREE": [
        "stiffness",
        "armature",
        "damping",
        "frictionloss",
    ],
    # No `ref` / `springref`: MJCF's ball joint does not carry them, so they are
    # left out of the export, the import and the properties panel rather than
    # being read and written as dead values.
    "BALL": [
        "springdamper",
        "solreflimit",
        "solimplimit",
        "solreffriction",
        "solimpfriction",
        "stiffness",
        "range",
        "limited",
        "margin",
        "armature",
        "damping",
        "frictionloss",
    ],
    "SLIDE": [
        "springdamper",
        "solreflimit",
        "solimplimit",
        "solreffriction",
        "solimpfriction",
        "stiffness",
        "range",
        "limited",
        "actuatorfrcrange",
        "actuatorfrclimited",
        "margin",
        "ref",
        "springref",
        "armature",
        "damping",
        "frictionloss",
    ],
    "HINGE": [
        "springdamper",
        "solreflimit",
        "solimplimit",
        "solreffriction",
        "solimpfriction",
        "stiffness",
        "range",
        "limited",
        "actuatorfrcrange",
        "actuatorfrclimited",
        "margin",
        "ref",
        "springref",
        "armature",
        "damping",
        "frictionloss",
    ],
}

JOINT_PROPS_NAME = {
    "springdamper": "Spring damper",
    "solreflimit": "Reference limit",
    "solimplimit": "Impedance limit",
    "solreffriction": "Reference friction",
    "solimpfriction": "Impedance friction",
    "stiffness": "Stiffness",
    "range": "Joint range",
    "limited": "Limited",
    "actuatorfrcrange": "Actuator force range",
    "actuatorfrclimited": "Actuator Limited",
    "margin": "Margin",
    "ref": "Reference position",
    "springref": "Spring reference",
    "armature": "Armature",
    "damping": "Damping",
    "frictionloss": "Friction loss",
}

JOINT_PROPS_DEFAULT = {
    "springdamper": (0.0, 0.0),
    "solreflimit": (0.02, 1),
    "solimplimit": (0.9, 0.95, 0.001),
    "solreffriction": (0.02, 1),
    "solimpfriction": (0.9, 0.95, 0.001),
    "stiffness": 0.0,
    "range": (0.0, 0.0),
    "limited": "AUTO",
    "actuatorfrcrange": (0.0, 0.0),
    "actuatorfrclimited": "AUTO",
    "margin": 0.0,
    "ref": 0.0,
    "springref": 0.0,
    "armature": 0.0,
    "damping": 0.0,
    "frictionloss": 0.0,
}

# ═══════════════════════════════════════════════════════════════════════
# Equality
# ═══════════════════════════════════════════════════════════════════════

EQUALITY_TYPE_PROPS = {
    "CONNECT": [
        "active",
        "anchor",
        "solref",
        "solimp",
    ],
    "WELD": [
        "active",
        "anchor",
        "solref",
        "solimp",
        "relpose",
    ],
    "JOINT": [
        "active",
        "solref",
        "solimp",
        "polycoef",
    ],
}

EQUALITY_PROPS_NAME = {
    "active": "Active",
    "anchor": "Anchor",
    "relpose": "Relative pose",
    "polycoef": "Polynomial coefficients",
    "solref": "Solver reference",
    "solimp": "Solver impedance",
}

EQUALITY_PROPS_DEFAULT = {
    "active": True,
    "anchor": (0.0, 0.0, 0.0),
    "solref": (0.02, 1.0),
    "solimp": (0.9, 0.95, 0.001, 0.5, 2.0),
    "relpose": (0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    "polycoef": (0.0, 1.0, 0.0, 0.0, 0.0),
}

# ═══════════════════════════════════════════════════════════════════════
# Tendon
# ═══════════════════════════════════════════════════════════════════════

TENDON_TYPE_PROPS = {
    "FIXED": [
        "range",
        "limited",
        "solreflimit",
        "solimplimit",
        "springlength",
        "stiffness",
        "damping",
    ],
}

TENDON_PROPS_NAME = {
    "range": "Range",
    "limited": "Limited",
    "solreflimit": "Solver reference limit",
    "solimplimit": "Solver impedance limit",
    "springlength": "Spring length",
    "stiffness": "Stiffness",
    "damping": "Damping",
}

TENDON_PROPS_DEFAULT = {
    "range": (0.0, 0.0),
    "limited": "AUTO",
    "solreflimit": (0.02, 1),
    "solimplimit": (0.9, 0.95, 0.001, 0.5, 2),
    "springlength": (-1.0, -1.0),
    "stiffness": 0.0,
    "damping": 0.0,
}

# ═══════════════════════════════════════════════════════════════════════
# Actuator
# ═══════════════════════════════════════════════════════════════════════

ACTUATOR_TYPE_PROPS = {
    "GENERAL": [
        "ctrllimited",
        "ctrlrange",
        "forcelimited",
        "forcerange",
        "gear",
        "gaintype",
        "biastype",
        "dynprm",
        "gainprm",
        "biasprm",
    ],
    "MOTOR": [
        "ctrllimited",
        "ctrlrange",
        "forcelimited",
        "forcerange",
        "gear",
        "gaintype",
        "biastype",
        "dynprm",
        "gainprm",
        "biasprm",
    ],
    "POSITION": [
        "ctrllimited",
        "ctrlrange",
        "forcelimited",
        "forcerange",
        "gear",
        "gaintype",
        "biastype",
        "dynprm",
        "gainprm",
        "biasprm",
        "kp",
        "kv",
        "inheritrange",
    ],
    "VELOCITY": [
        "ctrllimited",
        "ctrlrange",
        "forcelimited",
        "forcerange",
        "gear",
        "gaintype",
        "biastype",
        "dynprm",
        "gainprm",
        "biasprm",
        "kv",
    ],
    "ADHESION": [
        "ctrllimited",
        "ctrlrange",
        "forcelimited",
        "forcerange",
        "gain",
    ],
}

ACTUATOR_PROPS_NAME = {
    "ctrllimited": "Ctrl limited",
    "ctrlrange": "Ctrl range",
    "forcelimited": "Force limited",
    "forcerange": "Force range",
    "gear": "Gear",
    "gaintype": "Gain type",
    "biastype": "Bias type",
    "dynprm": "Dynamics",
    "gainprm": "Gain",
    "biasprm": "Bias",
    "kp": "kp",
    "kv": "kv",
    "inheritrange": "Inheritrange",
    "gain": "Gain",
}

ACTUATOR_PROPS_DEFAULT = {
    "ctrllimited": "AUTO",
    "ctrlrange": (0.0, 0.0),
    "forcelimited": "AUTO",
    "forcerange": (0.0, 0.0),
    "gear": (1.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    "gaintype": "FIXED",
    "biastype": "NONE",
    "dynprm": (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    "gainprm": (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    "biasprm": (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    "kp": 1.0,
    "kv": 0.0,
    "inheritrange": 0.0,
    "gain": 1.0,
}

# ═══════════════════════════════════════════════════════════════════════
# Light / Camera
# ═══════════════════════════════════════════════════════════════════════

LIGHT_TYPE_PROPS = {
    "POINT": [
        "mode",
        "target",
    ],
    "SPOT": [
        "mode",
        "target",
    ],
    "DIRECTIONAL": [],
}

CAMERA_PROPS = [
    "mode",
    "target",
]

# ═══════════════════════════════════════════════════════════════════════
# Sensor
# ═══════════════════════════════════════════════════════════════════════

SENSOR_TYPE_PROPS = {
    "Touch": {
        "site": "target",
    },
    "Accelerometer": {
        "site": "target",
    },
    "Velocimeter": {
        "site": "target",
    },
    "Gyro": {
        "site": "target",
    },
    "Jointpos": {
        "joint": "target",
    },
    "Jointvel": {
        "joint": "target",
    },
    "Framepos": {
        "objtype": "target_type",
        "objname": "target",
        "reftype": "ref_type",
        "refname": "ref",
    },
    "Framequat": {
        "objtype": "target_type",
        "objname": "target",
        "reftype": "ref_type",
        "refname": "ref",
    },
    "Framexaxis": {
        "objtype": "target_type",
        "objname": "target",
        "reftype": "ref_type",
        "refname": "ref",
    },
    "Frameyaxis": {
        "objtype": "target_type",
        "objname": "target",
        "reftype": "ref_type",
        "refname": "ref",
    },
    "Framezaxis": {
        "objtype": "target_type",
        "objname": "target",
        "reftype": "ref_type",
        "refname": "ref",
    },
    "Framelinvel": {
        "objtype": "target_type",
        "objname": "target",
        "reftype": "ref_type",
        "refname": "ref",
    },
    "Frameangvel": {
        "objtype": "target_type",
        "objname": "target",
        "reftype": "ref_type",
        "refname": "ref",
    },
    "Subtreecom": {
        "body": "target",
    },
    "Subtreelinvel": {
        "body": "target",
    },
    "Subtreeangmom": {
        "body": "target",
    },
    "Contact": {
        "body1": "target",
        "body2": "ref",
        "geom1": "target",
        "geom2": "ref",
        "subtree1": "target",
        "subtree2": "ref",
        "site": "target",
        "num": "num",
        "data": "data",
        "reduce": "reduce",
    },
}

SENSOR_PROPS_NAME = {
    "noise": "Noise",
    "cutoff": "Cutoff",
    "num": "Max contacts",
    "data": "Data type",
    "reduce": "Reduction",
}

SENSOR_PROPS_DEFAULT = {
    "noise": 0.0,
    "cutoff": 0.0,
    "num": 1,
    "data": {"found"},
    "reduce": "NONE",
}

SENSOR_CONTACT_DATA = {
    "found": 1,
    "force": 3,
    "torque": 3,
    "dist": 1,
    "pos": 3,
    "normal": 3,
    "tangent": 3,
}

# ═══════════════════════════════════════════════════════════════════════
# Site / Inertial / Replicate / Geom
# ═══════════════════════════════════════════════════════════════════════

SITE_PROPS = [
    "group",
]

INERTIAL_PROPS = [
    "mass",
    "diaginertia",
    "fullinertia",
]

INERTIAL_PROPS_NAME = {
    "mass": "Mass",
    "diaginertia": "Diagonal inertia",
    "fullinertia": "Full inertia",
}

INERTIAL_PROPS_DEFAULT = {
    "mass": 0.0,
    "diaginertia": [0.0, 0.0, 0.0],
    "fullinertia": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}

REPLICATE_PROPS = [
    "count",
    "sep",
    "offset",
    "euler",
]

REPLICATE_PROPS_REF = {
    "count": "Socket_0",
    "offset": "Socket_2",
    "euler": "Socket_3",
}

REPLICATE_PROPS_NAME = {
    "count": "Replicate Count",
    "sep": "Separator",
    "offset": "Offset",
    "euler": "Euler",
}

REPLICATE_PROPS_DEFAULT = {
    "count": 0,
    "sep": "",
    "offset": [0.0, 0.0, 0.0],
    "euler": [0.0, 0.0, 0.0],
}

GEOM_PROPS = [
    "group",
    "condim",
    "contype",
    "conaffinity",
    "priority",
    "friction",
    "mass",
    "density",
    "solmix",
    "solref",
    "solimp",
    "margin",
    "gap",
]

GEOM_PROPS_NAME = {
    "group": "Group",
    "condim": "Contact dimension",
    "contype": "Contact type",
    "conaffinity": "Contact affinity",
    "priority": "Priority",
    "friction": "Friction",
    "mass": "Mass",
    "density": "Density",
    "solmix": "Solver mix",
    "solref": "Solver reference",
    "solimp": "Solver impedance",
    "margin": "Margin",
    "gap": "Gap",
}

GEOM_PROPS_DEFAULT = {
    "group": 0,
    "condim": 3,
    "contype": 1,
    "conaffinity": 1,
    "priority": 0,
    "friction": (1.0, 0.005, 0.0001),
    "mass": 0,
    "density": 1000,
    "solmix": 1,
    "solref": (0.02, 1),
    "solimp": (0.9, 0.95, 0.001, 0.5, 2),
    "margin": 0,
    "gap": 0,
}

# ═══════════════════════════════════════════════════════════════════════
# Contact (exclude / pair)
# ═══════════════════════════════════════════════════════════════════════

CONTACT_TYPE_PROPS = {
    "EXCLUDE": [],
    "PAIR": [
        "condim",
        "friction",
        "solref",
        "solreffriction",
        "margin",
        "gap",
    ],
}

CONTACT_PROPS_NAME = {
    "condim": "Contact dimension",
    "friction": "Friction",
    "solref": "Reference",
    "solreffriction": "Reference friction",
    "margin": "Margin",
    "gap": "Gap",
}

CONTACT_PROPS_DEFAULT = {
    "condim": 3,
    "friction": (1.0, 1.0, 0.005, 0.0001, 0.0001),
    "solref": (0.02, 1.0),
    "solreffriction": (0.0, 0.0),
    "margin": 0.0,
    "gap": 0.0,
}

# ═══════════════════════════════════════════════════════════════════════
# Compiler
# ═══════════════════════════════════════════════════════════════════════

COMPILER_PROPS = [
    "autolimits",
    "angle",
    "eulerseq",
    "assetdir",
    "meshdir",
    "texturedir",
]

COMPILER_PROPS_NAME = {
    "autolimits": "Auto limits",
    "angle": "Angle Type",
    "eulerseq": "Euler Sequence",
    "assetdir": "Asset subpath",
    "meshdir": "Mesh subpath",
    "texturedir": "Texture subpath",
}

COMPILER_PROPS_DEFAULT = {
    "autolimits": True,
    "angle": "DEGREE",
    "eulerseq": "XYZ",
    "assetdir": "",
    "meshdir": "",
    "texturedir": "",
}

# ═══════════════════════════════════════════════════════════════════════
# Visual (config sub-groups: Global / Headlight / Map / Rgba)
# ═══════════════════════════════════════════════════════════════════════

VISUAL_CONFIG_PROPS = {
    "Global": [
        "orthographic",
        "fovy",
        "azimuth",
        "elevation",
    ],
    "Headlight": [
        "active",
        "ambient",
        "diffuse",
        "specular",
    ],
    "Map": [
        "fogstart",
        "fogend",
        "znear",
        "zfar",
    ],
    "Rgba": [
        "fog",
        "haze",
        "joint",
        "bv",
        "contactforce",
    ],
    "Quality": [
        "shadowsize",
        "pointshadowsize",
    ],
    "Ssgi": [
        "active",
        "resolutionscale",
        "raycount",
        "stepcount",
        "thickness",
        "intensity",
        "gidenoiseoffset",
        "rraycount",
        "rdenoiseoffset",
    ],
    "Tonemapping": [
        "method",
    ],
}

VISUAL_PROPS_NAME = {
    "Global": {
        "orthographic": "Orthographic",
        "fovy": "Field of view",
        "azimuth": "Azimuth",
        "elevation": "Elevation",
    },
    "Headlight": {
        "active": "Active",
        "ambient": "Ambient",
        "diffuse": "Diffuse",
        "specular": "Specular",
    },
    "Map": {
        "fogstart": "Fog start",
        "fogend": "Fog end",
        "znear": "Z near",
        "zfar": "Z far",
    },
    "Rgba": {
        "fog": "Fog",
        "haze": "Haze",
        "joint": "Joint",
        "bv": "Bounding volume",
        "contactforce": "Contact force",
    },
    "Quality": {
        "shadowsize": "Shadow size",
        "pointshadowsize": "Point shadow size",
    },
    "Ssgi": {
        "active": "Active",
        "resolutionscale": "Resolution scale",
        "raycount": "Ray count",
        "stepcount": "Step count",
        "thickness": "Thickness",
        "intensity": "Intensity",
        "gidenoiseoffset": "GI denoise offset",
        "rraycount": "Reflection ray count",
        "rdenoiseoffset": "Reflection denoise offset",
    },
    "Tonemapping": {
        "method": "Method",
    },
}

VISUAL_PROPS_DEFAULT = {
    "Global": {
        "orthographic": False,
        "fovy": 0.7853981633974483,
        "azimuth": 1.5707963267948966,
        "elevation": -0.7853981633974483,
    },
    "Headlight": {
        "active": 0,
        "ambient": (0.1, 0.1, 0.1),
        "diffuse": (0.4, 0.4, 0.4),
        "specular": (0.5, 0.5, 0.5),
    },
    "Map": {
        "fogstart": 5000.0,
        "fogend": 5000.0,
        "znear": 0.01,
        "zfar": 50.0,
    },
    "Rgba": {
        "fog": (0.75, 0.75, 0.75, 1.0),
        "haze": (1.0, 1.0, 1.0, 1.0),
        "joint": (0.2, 0.6, 0.8, 1.0),
        "bv": (0.0, 1.0, 0.0, 0.5),
        "contactforce": (0.7, 0.9, 0.9, 1.0),
    },
    "Quality": {
        "shadowsize": 1024,
        "pointshadowsize": 512,
    },
    "Ssgi": {
        "active": False,
        "resolutionscale": 2,
        "raycount": 2,
        "stepcount": 8,
        "thickness": 0.25,
        "intensity": 1.0,
        "gidenoiseoffset": 3,
        "rraycount": 64,
        "rdenoiseoffset": 3,
    },
    "Tonemapping": {
        "method": "none",
    },
}

# ═══════════════════════════════════════════════════════════════════════
# Option / Flag / Statistic
# ═══════════════════════════════════════════════════════════════════════

OPTION_PROPS = [
    "timestep",
    "gravity",
    "iterations",
    "tolerance",
    "o_solref",
    "o_solimp",
    "o_friction",
    "o_margin",
    "flag",
]

OPTION_PROPS_NAME = {
    "timestep": "Timestep",
    "gravity": "Gravity",
    "iterations": "Iterations",
    "tolerance": "Tolerance",
    "o_solref": "Overwrite Solver reference",
    "o_solimp": "Overwrite Solver impedance",
    "o_friction": "Overwrite Friction",
    "o_margin": "Overwrite Margin",
    "flag": "Flag",
}

OPTION_PROPS_DEFAULT = {
    "timestep": 0.002,
    "gravity": [0.0, 0.0, -9.81],
    "iterations": 100,
    "tolerance": 1e-8,
    "o_solref": (0.02, 1),
    "o_solimp": (0.9, 0.95, 0.001, 0.5, 2),
    "o_friction": (1.0, 0.005, 0.0001),
    "o_margin": 0,
}

FLAG_PROPS = [
    "constraint",
    "equality",
    "frictionloss",
    "limit",
    "contact",
    "gravity",
    "actuation",
    "refsafe",
    "override",
]

FLAG_PROPS_NAME = {
    "constraint": "Constraint",
    "equality": "Equality",
    "frictionloss": "Friction loss",
    "limit": "Limit",
    "contact": "Contact",
    "gravity": "Gravity",
    "actuation": "Actuation",
    "refsafe": "Reference safe",
    "override": "Override",
}

FLAG_PROPS_DEFAULT = {
    "constraint": True,
    "equality": True,
    "frictionloss": True,
    "limit": True,
    "contact": True,
    "gravity": True,
    "actuation": True,
    "refsafe": True,
    "override": False,
}

STATISTIC_PROPS = [
    "extent",
    "center",
]

STATISTIC_PROPS_NAME = {
    "extent": "Extent",
    "center": "Center",
}

STATISTIC_PROPS_DEFAULT = {
    "extent": 0.0,
    "center": (0.0, 0.0, 0.0),
}
