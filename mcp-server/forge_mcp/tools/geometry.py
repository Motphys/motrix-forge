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

"""Destructive mesh-processing tools."""

from __future__ import annotations

from typing import Literal

from .. import call_blender, mcp
from ..blender import op_call
from ._hints import DESTRUCTIVE


@mcp.tool(annotations=DESTRUCTIVE, name="forge_coacd")
def coacd(
    name: str,
    threshold: float = 0.05,
    max_convex_hull: int = -1,
    preprocess_mode: Literal["Auto", "On", "Off"] = "Auto",
    preprocess_resolution: int = 50,
    resolution: int = 2000,
    mcts_nodes: int = 20,
    mcts_iterations: int = 100,
    mcts_max_depth: int = 3,
    pca: bool = False,
    merge: bool = True,
    decimate: bool = False,
    max_ch_vertex: int = 128,
    extrude: bool = False,
    extrude_margin: float = 0.01,
    apx_mode: Literal["CH", "Box"] = "CH",
    seed: int = 0,
) -> dict:
    """Run CoACD on one Forge `visual` object and create collider hull objects beside it.

    `name` is the name of the source `VISUAL` object to decompose (it is
    selected automatically, so no separate selection is needed). Not the hull
    name template — generated hull names follow the addon preference
    `coacd_name_template` and are returned in `created`. The source object
    remains; processing can take several minutes.
    """
    return call_blender(
        op_call(
            "coacds",
            select=[name],
            threshold=threshold,
            max_convex_hull=max_convex_hull,
            preprocess_mode=preprocess_mode,
            preprocess_resolution=preprocess_resolution,
            resolution=resolution,
            mcts_nodes=mcts_nodes,
            mcts_iterations=mcts_iterations,
            mcts_max_depth=mcts_max_depth,
            pca=pca,
            merge=merge,
            decimate=decimate,
            max_ch_vertex=max_ch_vertex,
            extrude=extrude,
            extrude_margin=extrude_margin,
            apx_mode=apx_mode,
            seed=seed,
        )
    )
