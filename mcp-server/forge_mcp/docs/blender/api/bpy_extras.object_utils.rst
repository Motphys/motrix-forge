bpy_extras submodule (bpy_extras.object_utils)
==============================================

.. module:: bpy_extras.object_utils

.. function:: add_object_align_init(context, operator)

   Return a matrix using the operator settings and view context.
   
   :arg context: The context to use.
   :type context: :class:`bpy.types.Context`
   :arg operator: The operator, checked for location and rotation properties.
   :type operator: :class:`bpy.types.Operator`
   :return: the matrix from the context and settings.
   :rtype: :class:`mathutils.Matrix`

.. function:: object_data_add(context, obdata, operator=None, name=None)

   Add an object using the view context and preference to initialize the
   location, rotation and layer.
   
   :arg context: The context to use.
   :type context: :class:`bpy.types.Context`
   :arg obdata: Valid object data to used for the new object or None.
   :type obdata: :class:`bpy.types.ID` | None
   :arg operator: The operator, checked for location and rotation properties.
   :type operator: :class:`bpy.types.Operator`
   :arg name: Optional name
   :type name: str
   :return: the newly created object in the scene.
   :rtype: :class:`bpy.types.Object`

.. function:: object_add_grid_scale(context)

   Return scale which should be applied on object
   data to align it to grid scale

.. function:: object_add_grid_scale_apply_operator(operator, context)

   Scale an operators distance values by the grid size.

.. function:: world_to_camera_view(scene, obj, coord)

   Returns the camera space coords for a 3d point.
   (also known as: normalized device coordinates - NDC).
   
   Where (0, 0) is the bottom left and (1, 1)
   is the top right of the camera frame.
   values outside 0-1 are also supported.
   A negative 'z' value means the point is behind the camera.
   
   Takes shift-x/y, lens angle and sensor size into account
   as well as perspective/ortho projections.
   
   :arg scene: Scene to use for frame size.
   :type scene: :class:`bpy.types.Scene`
   :arg obj: Camera object.
   :type obj: :class:`bpy.types.Object`
   :arg coord: World space location.
   :type coord: :class:`mathutils.Vector`
   :return: a vector where X and Y map to the view plane and
      Z is the depth on the view axis.
   :rtype: :class:`mathutils.Vector`

.. function:: object_report_if_active_shape_key_is_locked(obj, operator)

   Checks if the active shape key of the specified object is locked, and reports an error if so.
   
   If the object has no shape keys, there is nothing to lock, and the function returns False.
   
   :arg obj: Object to check.
   :type obj: :class:`bpy.types.Object`
   :arg operator: Currently running operator to report the error through. Use None to suppress emitting the message.
   :type operator: :class:`bpy.types.Operator`
   :return: True if the shape key was locked.

.. class:: bpy_extras.object_utils.AddObjectHelper


   .. method:: align_update_callback(_context)



