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

"""Shared test configuration for writable, isolated temporary files."""

import tempfile
from pathlib import Path


def pytest_configure(config):
    """Use the checkout for temporary files unless --basetemp is explicit."""
    if config.option.basetemp is None:
        # Restricted sessions may not allow writes to the system temp directory.
        directory = tempfile.TemporaryDirectory(prefix=".pytest-tmp-", dir=Path(__file__).resolve().parents[1])
        config.option.basetemp = Path(directory.name)
        config.add_cleanup(directory.cleanup)
