Poselib Operators
=================

.. module:: bpy.ops.poselib

.. function:: apply_pose_asset(*, blend_factor=1.0, flipped=False)

   Apply the given Pose Action to the rig

   :arg blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it
   :type blend_factor: float in [-inf, inf], (optional)
   :arg flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
   :type flipped: boolean, (optional)

.. function:: asset_delete()

   Delete the selected Pose Asset

.. function:: asset_modify(*, mode='ADJUST')

   Update the selected pose asset in the asset library from the currently selected bones. The mode defines how the asset is updated

   :arg mode: Overwrite Mode, Specify which parts of the pose asset are overwritten

      * ``ADJUST``
        Adjust -- Update existing channels in the pose asset but don't remove or add any channels.
      * ``REPLACE``
        Replace with Selection -- Completely replace all channels in the pose asset with the current selection.
      * ``ADD``
        Add Selected Bones -- Add channels of the selection to the pose asset. Existing channels will be updated.
      * ``REMOVE``
        Remove Selected Bones -- Remove channels of the selection from the pose asset.
   :type mode: enum in [``'ADJUST'``, ``'REPLACE'``, ``'ADD'``, ``'REMOVE'``], (optional)

.. function:: blend_pose_asset(*, blend_factor=0.0, flipped=False, release_confirm=False)

   Blend the given Pose Action to the rig

   :arg blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it
   :type blend_factor: float in [-inf, inf], (optional)
   :arg flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
   :type flipped: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)

.. function:: convert_old_object_poselib()

   Create a pose asset for each pose marker in this legacy pose library data-block

   :File: `addons_core\pose_library\operators.py\:342 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\pose_library\operators.py#L342>`__

.. function:: convert_old_poselib()

   Create a pose asset for each pose marker in the current action

   :File: `addons_core\pose_library\operators.py\:308 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\pose_library\operators.py#L308>`__

.. function:: copy_as_asset()

   Create a new pose asset on the clipboard, to be pasted into an Asset Browser

   :File: `addons_core\pose_library\operators.py\:116 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\pose_library\operators.py#L116>`__

.. function:: create_pose_asset(*, pose_name="", asset_library_reference='', catalog_path="", activate_new_action=False)

   Create a new asset from the selected bones in the scene

   :arg pose_name: Pose Name, Name for the new pose asset
   :type pose_name: string, (optional, never None)
   :arg asset_library_reference: Library, Asset library used to store the new pose
   :type asset_library_reference: enum in [], (optional)
   :arg catalog_path: Catalog, Catalog to use for the new asset
   :type catalog_path: string, (optional, never None)
   :arg activate_new_action: Activate New Action, This property is deprecated and will be removed in the future
   :type activate_new_action: boolean, (optional)

.. function:: paste_asset()

   Paste the Asset that was previously copied using Copy As Asset

   :File: `addons_core\pose_library\operators.py\:190 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\pose_library\operators.py#L190>`__

.. function:: pose_asset_select_bones(*, select=True, flipped=False)

   Select those bones that are used in this pose

   :arg select: Select
   :type select: boolean, (optional)
   :arg flipped: Flipped
   :type flipped: boolean, (optional)
   :File: `addons_core\pose_library\operators.py\:228 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\pose_library\operators.py#L228>`__


.. function:: restore_previous_action()

   Switch back to the previous Action, after creating a pose asset

   :File: `addons_core\pose_library\operators.py\:65 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\pose_library\operators.py#L65>`__

