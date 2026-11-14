Extensions Operators
====================

.. module:: bpy.ops.extensions

.. function:: package_disable()

   Turn off this extension

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3588 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3588>`__

.. function:: package_install(*, repo_directory="", repo_index=-1, pkg_id="", enable_on_install=True, url="", do_legacy_replace=False)

   Download and install the extension

   :param repo_directory: Repo Directory, (optional, never None)
   :type repo_directory: str
   :param repo_index: Repo Index, (in [-inf, inf], optional)
   :type repo_index: int
   :param pkg_id: Package ID, (optional, never None)
   :type pkg_id: str
   :param enable_on_install: Enable on Install, Enable after installing (optional)
   :type enable_on_install: bool
   :param url: URL, (optional, never None)
   :type url: str
   :param do_legacy_replace: Do Legacy Replace, (optional)
   :type do_legacy_replace: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1511 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1511>`__


.. function:: package_install_files(*, filter_glob="*.zip;*.py", directory="", files=None, filepath="", repo='', enable_on_install=True, target='', overwrite=True, url="")

   Install extensions from files into a locally managed repository

   :param filter_glob: filter_glob, (optional, never None)
   :type filter_glob: str
   :param directory: Directory, (optional, never None)
   :type directory: str
   :param files: files, (optional)
   :type files: :class:`bpy_prop_collection`\ [:class:`OperatorFileListElement`] | None
   :param filepath: filepath, (optional, never None)
   :type filepath: str
   :param repo: User Repository, The user repository to install extensions into (optional)
   :type repo: str
   :param enable_on_install: Enable on Install, Enable after installing (optional)
   :type enable_on_install: bool
   :param target: Legacy Target Path, Path to install legacy add-on packages to (optional)
   :type target: str
   :param overwrite: Legacy Overwrite, Remove existing add-ons with the same ID (optional)
   :type overwrite: bool
   :param url: URL, (optional, never None)
   :type url: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1511 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1511>`__


.. function:: package_install_marked(*, enable_on_install=True)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param enable_on_install: Enable on Install, Enable after installing (optional)
   :type enable_on_install: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1511 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1511>`__


.. function:: package_mark_clear(*, pkg_id="", repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param pkg_id: Package ID, (optional, never None)
   :type pkg_id: str
   :param repo_index: Repo Index, (in [-inf, inf], optional)
   :type repo_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3675 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3675>`__


.. function:: package_mark_clear_all()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3722 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3722>`__

.. function:: package_mark_set(*, pkg_id="", repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param pkg_id: Package ID, (optional, never None)
   :type pkg_id: str
   :param repo_index: Repo Index, (in [-inf, inf], optional)
   :type repo_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3661 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3661>`__


.. function:: package_mark_set_all()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3686 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3686>`__

.. function:: package_obsolete_marked()

   Zeroes package versions, useful for development - to test upgrading

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3779 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3779>`__

.. function:: package_show_clear(*, pkg_id="", repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param pkg_id: Package ID, (optional, never None)
   :type pkg_id: str
   :param repo_index: Repo Index, (in [-inf, inf], optional)
   :type repo_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3748 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3748>`__


.. function:: package_show_set(*, pkg_id="", repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param pkg_id: Package ID, (optional, never None)
   :type pkg_id: str
   :param repo_index: Repo Index, (in [-inf, inf], optional)
   :type repo_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3734 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3734>`__


.. function:: package_show_settings(*, pkg_id="", repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param pkg_id: Package ID, (optional, never None)
   :type pkg_id: str
   :param repo_index: Repo Index, (in [-inf, inf], optional)
   :type repo_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3762 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3762>`__


.. function:: package_theme_disable(*, pkg_id="", repo_index=-1)

   Reset to the default theme if this theme is active

   :param pkg_id: Package ID, (optional, never None)
   :type pkg_id: str
   :param repo_index: Repo Index, (in [-inf, inf], optional)
   :type repo_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3616 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3616>`__


.. function:: package_theme_enable(*, pkg_id="", repo_index=-1)

   Turn on this theme

   :param pkg_id: Package ID, (optional, never None)
   :type pkg_id: str
   :param repo_index: Repo Index, (in [-inf, inf], optional)
   :type repo_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3602 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3602>`__


.. function:: package_uninstall(*, repo_directory="", repo_index=-1, pkg_id="")

   Disable and uninstall the extension

   :param repo_directory: Repo Directory, (optional, never None)
   :type repo_directory: str
   :param repo_index: Repo Index, (in [-inf, inf], optional)
   :type repo_index: int
   :param pkg_id: Package ID, (optional, never None)
   :type pkg_id: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1511 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1511>`__


.. function:: package_uninstall_marked()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1511 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1511>`__

.. function:: package_uninstall_system()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3579 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3579>`__

.. function:: package_upgrade_all(*, use_active_only=False)

   Upgrade installed extensions to their latest version from remote repositories

   :param use_active_only: Active Only, Only upgrade the active repository (optional)
   :type use_active_only: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1511 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1511>`__


.. function:: repo_enable_from_drop(*, repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param repo_index: Repo Index, (in [-inf, inf], optional)
   :type repo_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1844 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1844>`__


.. function:: repo_lock_all()

   Lock repositories - to test locking

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3848 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3848>`__

.. function:: repo_refresh_all(*, use_active_only=False)

   Refresh extension & legacy add-ons, reloading modules & meta-data (similar to restarting)

   :param use_active_only: Active Only, Only refresh the active repository (optional)
   :type use_active_only: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1753 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1753>`__


.. function:: repo_sync(*, repo_directory="", repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :param repo_directory: Repo Directory, (optional, never None)
   :type repo_directory: str
   :param repo_index: Repo Index, (in [-inf, inf], optional)
   :type repo_index: int
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1511 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1511>`__


.. function:: repo_sync_all(*, use_active_only=False)

   Refresh the list of extensions for all the remote repositories

   :param use_active_only: Active Only, Only sync the active repository (optional)
   :type use_active_only: bool
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1511 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1511>`__


.. function:: repo_unlock()

   Remove the repository file-system lock

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1931 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1931>`__

.. function:: repo_unlock_all()

   Unlock repositories - to test unlocking

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3874 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3874>`__

.. function:: status_clear()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3647 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3647>`__

.. function:: status_clear_errors()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3636 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3636>`__

.. function:: userpref_allow_online()

   Allow Blender to access the internet. Add-ons that follow this setting will only connect to the internet if enabled. However, Blender cannot prevent third-party add-ons from violating this rule.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:4000 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L4000>`__

.. function:: userpref_allow_online_popup()

   Allow Blender to access the internet. Add-ons that follow this setting will only connect to the internet if enabled. However, Blender cannot prevent third-party add-ons from violating this rule.

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:4015 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L4015>`__

.. function:: userpref_show_for_update()

   Open extensions preferences

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3939 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3939>`__

.. function:: userpref_show_online()

   Show system preferences "Network" panel to allow online access

   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3979 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3979>`__

.. function:: userpref_tags_set(*, value=False, data_path="")

   Set the value of all tags

   :param value: Value, Enable or disable all tags (optional)
   :type value: bool
   :param data_path: Data Path, (optional, never None)
   :type data_path: str
   :return: Result of the operator call.
   :rtype: set[Literal[:ref:`rna_enum_operator_return_items`]]
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3908 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3908>`__


