Extensions Operators
====================

.. module:: bpy.ops.extensions

.. function:: package_disable()

   Turn off this extension

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3582 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3582>`__

.. function:: package_install(*, repo_directory="", repo_index=-1, pkg_id="", enable_on_install=True, url="", do_legacy_replace=False)

   Download and install the extension

   :arg repo_directory: Repo Directory
   :type repo_directory: string, (optional, never None)
   :arg repo_index: Repo Index
   :type repo_index: int in [-inf, inf], (optional)
   :arg pkg_id: Package ID
   :type pkg_id: string, (optional, never None)
   :arg enable_on_install: Enable on Install, Enable after installing
   :type enable_on_install: boolean, (optional)
   :arg url: URL
   :type url: string, (optional, never None)
   :arg do_legacy_replace: Do Legacy Replace
   :type do_legacy_replace: boolean, (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1500 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1500>`__


.. function:: package_install_files(*, filter_glob="*.zip;*.py", directory="", files=None, filepath="", repo='', enable_on_install=True, target='', overwrite=True, url="")

   Install extensions from files into a locally managed repository

   :arg filter_glob: filter_glob
   :type filter_glob: string, (optional, never None)
   :arg directory: Directory
   :type directory: string, (optional, never None)
   :arg files: files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :arg repo: User Repository, The user repository to install extensions into
   :type repo: enum in [], (optional)
   :arg enable_on_install: Enable on Install, Enable after installing
   :type enable_on_install: boolean, (optional)
   :arg target: Legacy Target Path, Path to install legacy add-on packages to
   :type target: enum in [], (optional)
   :arg overwrite: Legacy Overwrite, Remove existing add-ons with the same ID
   :type overwrite: boolean, (optional)
   :arg url: URL
   :type url: string, (optional, never None)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1500 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1500>`__


.. function:: package_install_marked(*, enable_on_install=True)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg enable_on_install: Enable on Install, Enable after installing
   :type enable_on_install: boolean, (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1500 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1500>`__


.. function:: package_mark_clear(*, pkg_id="", repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg pkg_id: Package ID
   :type pkg_id: string, (optional, never None)
   :arg repo_index: Repo Index
   :type repo_index: int in [-inf, inf], (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3669 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3669>`__


.. function:: package_mark_clear_all()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3716 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3716>`__

.. function:: package_mark_set(*, pkg_id="", repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg pkg_id: Package ID
   :type pkg_id: string, (optional, never None)
   :arg repo_index: Repo Index
   :type repo_index: int in [-inf, inf], (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3655 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3655>`__


.. function:: package_mark_set_all()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3680 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3680>`__

.. function:: package_obsolete_marked()

   Zeroes package versions, useful for development - to test upgrading

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3773 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3773>`__

.. function:: package_show_clear(*, pkg_id="", repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg pkg_id: Package ID
   :type pkg_id: string, (optional, never None)
   :arg repo_index: Repo Index
   :type repo_index: int in [-inf, inf], (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3742 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3742>`__


.. function:: package_show_set(*, pkg_id="", repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg pkg_id: Package ID
   :type pkg_id: string, (optional, never None)
   :arg repo_index: Repo Index
   :type repo_index: int in [-inf, inf], (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3728 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3728>`__


.. function:: package_show_settings(*, pkg_id="", repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg pkg_id: Package ID
   :type pkg_id: string, (optional, never None)
   :arg repo_index: Repo Index
   :type repo_index: int in [-inf, inf], (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3756 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3756>`__


.. function:: package_theme_disable(*, pkg_id="", repo_index=-1)

   Turn off this theme

   :arg pkg_id: Package ID
   :type pkg_id: string, (optional, never None)
   :arg repo_index: Repo Index
   :type repo_index: int in [-inf, inf], (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3610 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3610>`__


.. function:: package_theme_enable(*, pkg_id="", repo_index=-1)

   Turn off this theme

   :arg pkg_id: Package ID
   :type pkg_id: string, (optional, never None)
   :arg repo_index: Repo Index
   :type repo_index: int in [-inf, inf], (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3595 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3595>`__


.. function:: package_uninstall(*, repo_directory="", repo_index=-1, pkg_id="")

   Disable and uninstall the extension

   :arg repo_directory: Repo Directory
   :type repo_directory: string, (optional, never None)
   :arg repo_index: Repo Index
   :type repo_index: int in [-inf, inf], (optional)
   :arg pkg_id: Package ID
   :type pkg_id: string, (optional, never None)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1500 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1500>`__


.. function:: package_uninstall_marked()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1500 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1500>`__

.. function:: package_uninstall_system()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3573 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3573>`__

.. function:: package_upgrade_all(*, use_active_only=False)

   Upgrade all the extensions to their latest version for all the remote repositories

   :arg use_active_only: Active Only, Only sync the active repository
   :type use_active_only: boolean, (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1500 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1500>`__


.. function:: repo_enable_from_drop(*, repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg repo_index: Repo Index
   :type repo_index: int in [-inf, inf], (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1830 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1830>`__


.. function:: repo_lock_all()

   Lock repositories - to test locking

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3842 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3842>`__

.. function:: repo_refresh_all(*, use_active_only=False)

   Scan extension & legacy add-ons for changes to modules & meta-data (similar to restarting). Any issues are reported as warnings

   :arg use_active_only: Active Only, Only refresh the active repository
   :type use_active_only: boolean, (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1743 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1743>`__


.. function:: repo_sync(*, repo_directory="", repo_index=-1)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg repo_directory: Repo Directory
   :type repo_directory: string, (optional, never None)
   :arg repo_index: Repo Index
   :type repo_index: int in [-inf, inf], (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1500 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1500>`__


.. function:: repo_sync_all(*, use_active_only=False)

   Refresh the list of extensions for all the remote repositories

   :arg use_active_only: Active Only, Only sync the active repository
   :type use_active_only: boolean, (optional)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1500 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1500>`__


.. function:: repo_unlock()

   Remove the repository file-system lock

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:1917 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L1917>`__

.. function:: repo_unlock_all()

   Unlock repositories - to test unlocking

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3868 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3868>`__

.. function:: status_clear()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3641 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3641>`__

.. function:: status_clear_errors()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3630 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3630>`__

.. function:: userpref_allow_online()

   Allow internet access. Blender may access configured online extension repositories. Installed third party add-ons may access the internet for their own functionality

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3993 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3993>`__

.. function:: userpref_allow_online_popup()

   Allow internet access. Blender may access configured online extension repositories. Installed third party add-ons may access the internet for their own functionality

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:4007 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L4007>`__

.. function:: userpref_show_for_update()

   Open extensions preferences

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3933 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3933>`__

.. function:: userpref_show_online()

   Show system preferences "Network" panel to allow online access

   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3973 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3973>`__

.. function:: userpref_tags_set(*, value=False, data_path="")

   Set the value of all tags

   :arg value: Value, Enable or disable all tags
   :type value: boolean, (optional)
   :arg data_path: Data Path
   :type data_path: string, (optional, never None)
   :File: `addons_core\bl_pkg\bl_extension_ops.py\:3902 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\bl_pkg\bl_extension_ops.py#L3902>`__


