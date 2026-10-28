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
Central operator registry — re-exports all operator classes from split modules.

This module exists so that existing import sites continue to work:

* ``from ..ops import forge_operator``  →  ``forge_operator.classes`` (registration)
* ``from ..ops import forge_operator as ops``  →  ``ops.Forge_OT_*.bl_idname``

Operator implementations live in sibling modules:

* ``creation.py``  — Forge_OT_Geometry_Creation, Forge_OT_Collider_Creation, …
* ``definition.py``  — Forge_OT_Type_Define, Forge_OT_Geometry_Define, …
* ``io_ops.py``  — Forge_OT_Import, Forge_OT_Export, Forge_OT_Attach, …
* ``utilities.py``  — Forge_OT_Batch_Rename, Forge_OT_SelectByTAG, …
* ``materials.py``  — Forge_OT_Material_Creation
* ``properties_operators.py``  — Forge_OT_PROPERTIES_* (all popup editors)
"""

# ── Creation / element operators ──────────────────────────────────────
from .creation import (
    Forge_OT_Actuator_Creation,
    Forge_OT_Camera_Creation,
    Forge_OT_Change_Gizmo_Size,
    Forge_OT_Collider_Creation,
    Forge_OT_Contact_Creation,
    Forge_OT_Equality_Creation,
    Forge_OT_Frame_Creation,
    Forge_OT_Geometry_Creation,
    Forge_OT_HeightField_Creation,
    Forge_OT_Inertial_Creation,
    Forge_OT_Joint_Creation,
    Forge_OT_Light_Creation,
    Forge_OT_Link_Creation,
    Forge_OT_Link_MarkRoot,
    Forge_OT_Mesh_Check,
    Forge_OT_Plane_Creation,
    Forge_OT_Replicate_Creation,
    Forge_OT_Sensor_Creation,
    Forge_OT_Site_Creation,
    Forge_OT_Tendon_Creation,
)

# ── Define / type-change operators ────────────────────────────────────
from .definition import (
    Forge_OT_Actuator_Define,
    Forge_OT_Collider_Define,
    Forge_OT_Geometry_Define,
    Forge_OT_Joint_Define,
    Forge_OT_Parent_Define,
    Forge_OT_Site_Define,
    Forge_OT_Type_Define,
)

# ── Import / Export / Attach / Include ────────────────────────────────
from .io_ops import (
    Forge_OT_Attach,
    Forge_OT_Export,
    Forge_OT_Import,
    Forge_OT_Include,
    Forge_OT_SelectExportPath,
    Forge_OT_SelectImportPath,
    Forge_OT_SelectTempFile,
    Forge_OT_SelectTempInclude,
    Forge_OT_SelectTempLink,
)

# ── Material library operators ────────────────────────────────────────
from .materials import Forge_OT_Checker_Material_Creation, Forge_OT_Material_Assign, Forge_OT_Material_Creation

# ── Property-editor popup operators ───────────────────────────────────
from .properties_operators import (
    Forge_OT_PROPERTIES_Actuator,
    Forge_OT_PROPERTIES_Camera,
    Forge_OT_PROPERTIES_Contact,
    Forge_OT_PROPERTIES_Equality,
    Forge_OT_PROPERTIES_Global,
    Forge_OT_PROPERTIES_HeightField,
    Forge_OT_PROPERTIES_Joint,
    Forge_OT_PROPERTIES_Light,
    Forge_OT_PROPERTIES_Link,
    Forge_OT_PROPERTIES_Plane,
    Forge_OT_PROPERTIES_Replicate,
    Forge_OT_PROPERTIES_Sensor,
    Forge_OT_PROPERTIES_Shape,
    Forge_OT_PROPERTIES_Shape_Site,
    Forge_OT_PROPERTIES_Tendon,
    Forge_OT_PROPERTIES_Visual,
)

# ── Utility operators ─────────────────────────────────────────────────
from .utilities import (
    Forge_OT_Batch_Rename,
    Forge_OT_Instance_Mark,
    Forge_OT_InstanceSet,
    Forge_OT_SelectByModelType,
    Forge_OT_SelectByTAG,
    Forge_OT_SelectHulls,
)

# ═══════════════════════════════════════════════════════════════════════
# Registration order (preserved from original single-file layout)
# ═══════════════════════════════════════════════════════════════════════

classes = (
    Forge_OT_Change_Gizmo_Size,
    Forge_OT_Instance_Mark,
    Forge_OT_InstanceSet,
    Forge_OT_SelectTempLink,
    Forge_OT_SelectTempFile,
    Forge_OT_SelectTempInclude,
    Forge_OT_SelectImportPath,
    Forge_OT_SelectExportPath,
    Forge_OT_Import,
    Forge_OT_Export,
    Forge_OT_SelectByTAG,
    Forge_OT_SelectByModelType,
    Forge_OT_Type_Define,
    Forge_OT_Batch_Rename,
    Forge_OT_Geometry_Creation,
    Forge_OT_Geometry_Define,
    Forge_OT_Collider_Creation,
    Forge_OT_Collider_Define,
    Forge_OT_Site_Creation,
    Forge_OT_Site_Define,
    Forge_OT_Link_Creation,
    Forge_OT_PROPERTIES_Link,
    Forge_OT_Link_MarkRoot,
    Forge_OT_Inertial_Creation,
    Forge_OT_Mesh_Check,
    Forge_OT_Joint_Creation,
    Forge_OT_Joint_Define,
    Forge_OT_Parent_Define,
    Forge_OT_PROPERTIES_Shape,
    Forge_OT_PROPERTIES_Shape_Site,
    Forge_OT_PROPERTIES_Joint,
    Forge_OT_Actuator_Creation,
    Forge_OT_Actuator_Define,
    Forge_OT_PROPERTIES_Actuator,
    Forge_OT_Tendon_Creation,
    Forge_OT_Equality_Creation,
    Forge_OT_PROPERTIES_Tendon,
    Forge_OT_PROPERTIES_Equality,
    Forge_OT_Sensor_Creation,
    Forge_OT_Contact_Creation,
    Forge_OT_PROPERTIES_Contact,
    Forge_OT_PROPERTIES_Sensor,
    Forge_OT_Light_Creation,
    Forge_OT_PROPERTIES_Light,
    Forge_OT_Camera_Creation,
    Forge_OT_PROPERTIES_Camera,
    Forge_OT_HeightField_Creation,
    Forge_OT_PROPERTIES_HeightField,
    Forge_OT_Plane_Creation,
    Forge_OT_Material_Creation,
    Forge_OT_Checker_Material_Creation,
    Forge_OT_Material_Assign,
    Forge_OT_PROPERTIES_Plane,
    Forge_OT_PROPERTIES_Global,
    Forge_OT_PROPERTIES_Visual,
    Forge_OT_Frame_Creation,
    Forge_OT_Replicate_Creation,
    Forge_OT_PROPERTIES_Replicate,
    Forge_OT_Attach,
    Forge_OT_Include,
    Forge_OT_SelectHulls,
)
