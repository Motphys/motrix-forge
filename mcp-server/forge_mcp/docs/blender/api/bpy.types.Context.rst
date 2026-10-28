Context(bpy_struct)
===================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Context(bpy_struct)

   Current windowmanager and data context

   .. data:: area

      :type: :class:`Area`, (readonly)

   .. data:: asset

      :type: :class:`AssetRepresentation`, (readonly)

   .. data:: blend_data

      :type: :class:`BlendData`, (readonly)

   .. data:: collection

      :type: :class:`Collection`, (readonly)

   .. data:: engine

      :type: string, default "", (readonly, never None)

   .. data:: gizmo_group

      :type: :class:`GizmoGroup`, (readonly)

   .. data:: layer_collection

      :type: :class:`LayerCollection`, (readonly)

   .. data:: mode

      :type: enum in :ref:`rna_enum_context_mode_items`, default ``'EDIT_MESH'``, (readonly)

   .. data:: preferences

      :type: :class:`Preferences`, (readonly)

   .. data:: region

      :type: :class:`Region`, (readonly)

   .. data:: region_data

      :type: :class:`RegionView3D`, (readonly)

   .. data:: region_popup

      The temporary region for pop-ups (including menus and pop-overs)

      :type: :class:`Region`, (readonly)

   .. data:: scene

      :type: :class:`Scene`, (readonly)

   .. data:: screen

      :type: :class:`Screen`, (readonly)

   .. data:: space_data

      The current space, may be None in background-mode, when the cursor is outside the window or when using menu-search

      :type: :class:`Space`, (readonly)

   .. data:: tool_settings

      :type: :class:`ToolSettings`, (readonly)

   .. data:: view_layer

      :type: :class:`ViewLayer`, (readonly)

   .. data:: window

      :type: :class:`Window`, (readonly)

   .. data:: window_manager

      :type: :class:`WindowManager`, (readonly)

   .. data:: workspace

      :type: :class:`WorkSpace`, (readonly)

   .. method:: evaluated_depsgraph_get()

      Get the dependency graph for the current scene and view layer, to access to data-blocks with animation and modifiers applied. If any data-blocks have been edited, the dependency graph will be updated. This invalidates all references to evaluated data-blocks from the dependency graph.

      :return: Evaluated dependency graph
      :rtype: :class:`Depsgraph`

   .. method:: copy()

      Get context members as a dictionary.
      
              :rtype: dict[str, Any]

   .. method:: path_resolve(path, coerce=True)

      Returns the property from the path, raise an exception when not found.
      
      :arg path: patch which this property resolves.
      :type path: str
      :arg coerce: optional argument, when True, the property will be converted into its Python representation.
      :type coerce: bool

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct` subclass


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The class or default when not found.
      :rtype: type


   .. method:: temp_override(*, window=None, area=None, region=None, **keywords)
   
      Context manager to temporarily override members in the context.
   
      :arg window: Window override or None.
      :type window: :class:`bpy.types.Window`
      :arg screen: Screen override or None.
   
         .. note:: Switching to or away from full-screen areas & temporary screens isn't supported. Passing in these screens will raise an exception, actions that leave the context such screens won't restore the prior screen.
   
         .. note:: Changing the screen has wider implications than other arguments as it will also change the works-space and potentially the scene (when pinned).
   
      :type screen: :class:`bpy.types.Screen`
      :arg area: Area override or None.
      :type area: :class:`bpy.types.Area`
      :arg region: Region override or None.
      :type region: :class:`bpy.types.Region`
      :arg keywords: Additional keywords override context members.
      :return: The context manager .
      :rtype: ContextTempOverride


      Overriding the context can be used to temporarily activate another ``window`` / ``area`` & ``region``,
      as well as other members such as the ``active_object`` or ``bone``.

      Notes:

      - When overriding window, area and regions: the arguments must be consistent,
        so any region argument that's passed in must be contained by the current area or the area passed in.
        The same goes for the area needing to be contained in the current window.

      - Temporary context overrides may be nested, when this is done, members will be added to the existing overrides.

      - Context members are restored outside the scope of the context-manager.
        The only exception to this is when the data is no longer available.

        In the event windowing data was removed (for example), the state of the context is left as-is.
        While this isn't likely to happen, explicit window operation such as closing windows or loading a new file
        remove the windowing data that was set before the temporary context was created.


      Overriding the context can be useful to set the context after loading files
      (which would otherwise by None). For example:

      .. literalinclude:: ..\examples\bpy.types.Context.temp_override.2.py
         :lines: 6-


      This example shows how it's possible to add an object to the scene in another window.

      .. literalinclude:: ..\examples\bpy.types.Context.temp_override.3.py
         :lines: 4-


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.id_properties_clear`
   * :class:`bpy_struct.id_properties_ensure`
   * :class:`bpy_struct.id_properties_ui`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_overridable_library`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.pop`
   * :class:`bpy_struct.property_overridable_library_set`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.rna_ancestors`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   * :class:`AssetShelf.draw_context_menu`
   * :class:`AssetShelf.poll`
   * :class:`FileHandler.poll_drop`
   * :class:`Gizmo.draw`
   * :class:`Gizmo.draw_select`
   * :class:`Gizmo.exit`
   * :class:`Gizmo.invoke`
   * :class:`Gizmo.modal`
   * :class:`Gizmo.test_select`
   * :class:`GizmoGroup.draw_prepare`
   * :class:`GizmoGroup.invoke_prepare`
   * :class:`GizmoGroup.poll`
   * :class:`GizmoGroup.refresh`
   * :class:`GizmoGroup.setup`
   * :class:`Header.draw`
   * :class:`KeyingSetInfo.generate`
   * :class:`KeyingSetInfo.iterator`
   * :class:`KeyingSetInfo.poll`
   * :class:`Macro.draw`
   * :class:`Macro.poll`
   * :class:`Menu.draw`
   * :class:`Menu.poll`
   * :class:`Node.draw_buttons`
   * :class:`Node.draw_buttons_ext`
   * :class:`Node.init`
   * :class:`Node.socket_value_update`
   * :class:`NodeInternal.draw_buttons`
   * :class:`NodeInternal.draw_buttons_ext`
   * :class:`NodeSocket.draw`
   * :class:`NodeSocket.draw_color`
   * :class:`NodeSocketStandard.draw`
   * :class:`NodeSocketStandard.draw_color`
   * :class:`NodeTree.get_from_context`
   * :class:`NodeTree.interface_update`
   * :class:`NodeTree.poll`
   * :class:`NodeTreeInterfaceSocket.draw`
   * :class:`NodeTreeInterfaceSocketBool.draw`
   * :class:`NodeTreeInterfaceSocketBundle.draw`
   * :class:`NodeTreeInterfaceSocketClosure.draw`
   * :class:`NodeTreeInterfaceSocketCollection.draw`
   * :class:`NodeTreeInterfaceSocketColor.draw`
   * :class:`NodeTreeInterfaceSocketFloat.draw`
   * :class:`NodeTreeInterfaceSocketFloatAngle.draw`
   * :class:`NodeTreeInterfaceSocketFloatColorTemperature.draw`
   * :class:`NodeTreeInterfaceSocketFloatDistance.draw`
   * :class:`NodeTreeInterfaceSocketFloatFactor.draw`
   * :class:`NodeTreeInterfaceSocketFloatFrequency.draw`
   * :class:`NodeTreeInterfaceSocketFloatPercentage.draw`
   * :class:`NodeTreeInterfaceSocketFloatTime.draw`
   * :class:`NodeTreeInterfaceSocketFloatTimeAbsolute.draw`
   * :class:`NodeTreeInterfaceSocketFloatUnsigned.draw`
   * :class:`NodeTreeInterfaceSocketFloatWavelength.draw`
   * :class:`NodeTreeInterfaceSocketGeometry.draw`
   * :class:`NodeTreeInterfaceSocketImage.draw`
   * :class:`NodeTreeInterfaceSocketInt.draw`
   * :class:`NodeTreeInterfaceSocketIntFactor.draw`
   * :class:`NodeTreeInterfaceSocketIntPercentage.draw`
   * :class:`NodeTreeInterfaceSocketIntUnsigned.draw`
   * :class:`NodeTreeInterfaceSocketMaterial.draw`
   * :class:`NodeTreeInterfaceSocketMatrix.draw`
   * :class:`NodeTreeInterfaceSocketMenu.draw`
   * :class:`NodeTreeInterfaceSocketObject.draw`
   * :class:`NodeTreeInterfaceSocketRotation.draw`
   * :class:`NodeTreeInterfaceSocketShader.draw`
   * :class:`NodeTreeInterfaceSocketString.draw`
   * :class:`NodeTreeInterfaceSocketStringFilePath.draw`
   * :class:`NodeTreeInterfaceSocketTexture.draw`
   * :class:`NodeTreeInterfaceSocketVector.draw`
   * :class:`NodeTreeInterfaceSocketVector2D.draw`
   * :class:`NodeTreeInterfaceSocketVector4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorAcceleration.draw`
   * :class:`NodeTreeInterfaceSocketVectorAcceleration2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorAcceleration4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorDirection.draw`
   * :class:`NodeTreeInterfaceSocketVectorDirection2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorDirection4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorEuler.draw`
   * :class:`NodeTreeInterfaceSocketVectorEuler2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorEuler4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorFactor.draw`
   * :class:`NodeTreeInterfaceSocketVectorFactor2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorFactor4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorPercentage.draw`
   * :class:`NodeTreeInterfaceSocketVectorPercentage2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorPercentage4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorTranslation.draw`
   * :class:`NodeTreeInterfaceSocketVectorTranslation2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorTranslation4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorVelocity.draw`
   * :class:`NodeTreeInterfaceSocketVectorVelocity2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorVelocity4D.draw`
   * :class:`NodeTreeInterfaceSocketVectorXYZ.draw`
   * :class:`NodeTreeInterfaceSocketVectorXYZ2D.draw`
   * :class:`NodeTreeInterfaceSocketVectorXYZ4D.draw`
   * :class:`Operator.cancel`
   * :class:`Operator.check`
   * :class:`Operator.description`
   * :class:`Operator.draw`
   * :class:`Operator.execute`
   * :class:`Operator.invoke`
   * :class:`Operator.modal`
   * :class:`Operator.poll`
   * :class:`Panel.draw`
   * :class:`Panel.draw_header`
   * :class:`Panel.draw_header_preset`
   * :class:`Panel.poll`
   * :class:`RenderEngine.draw`
   * :class:`RenderEngine.view_draw`
   * :class:`RenderEngine.view_update`
   * :class:`UIList.draw_filter`
   * :class:`UIList.draw_item`
   * :class:`UIList.filter_items`
   * :class:`XrSessionState.action_binding_create`
   * :class:`XrSessionState.action_create`
   * :class:`XrSessionState.action_set_create`
   * :class:`XrSessionState.action_state_get`
   * :class:`XrSessionState.active_action_set_set`
   * :class:`XrSessionState.controller_aim_location_get`
   * :class:`XrSessionState.controller_aim_rotation_get`
   * :class:`XrSessionState.controller_grip_location_get`
   * :class:`XrSessionState.controller_grip_rotation_get`
   * :class:`XrSessionState.controller_pose_actions_set`
   * :class:`XrSessionState.haptic_action_apply`
   * :class:`XrSessionState.haptic_action_stop`
   * :class:`XrSessionState.is_running`
   * :class:`XrSessionState.reset_to_base_pose`

