Paint Operators
===============

.. module:: bpy.ops.paint

.. function:: add_simple_uvs()

   Add cube map UVs on mesh

.. function:: add_texture_paint_slot(*, type='BASE_COLOR', slot_type='IMAGE', name="Untitled", color=(0.0, 0.0, 0.0, 1.0), width=1024, height=1024, alpha=True, generated_type='BLANK', float=False, domain='POINT', data_type='FLOAT_COLOR')

   Add a paint slot

   :arg type: Material Layer Type, Material layer type of new paint slot
   :type type: enum in [``'BASE_COLOR'``, ``'SPECULAR'``, ``'ROUGHNESS'``, ``'METALLIC'``, ``'NORMAL'``, ``'BUMP'``, ``'DISPLACEMENT'``], (optional)
   :arg slot_type: Slot Type, Type of new paint slot
   :type slot_type: enum in [``'IMAGE'``, ``'COLOR_ATTRIBUTE'``], (optional)
   :arg name: Name, Name for new paint slot source
   :type name: string, (optional, never None)
   :arg color: Color, Default fill color
   :type color: float array of 4 items in [0, inf], (optional)
   :arg width: Width, Image width
   :type width: int in [1, inf], (optional)
   :arg height: Height, Image height
   :type height: int in [1, inf], (optional)
   :arg alpha: Alpha, Create an image with an alpha channel
   :type alpha: boolean, (optional)
   :arg generated_type: Generated Type, Fill the image with a grid for UV map testing
   :type generated_type: enum in :ref:`rna_enum_image_generated_type_items`, (optional)
   :arg float: 32-bit Float, Create image with 32-bit floating-point bit depth
   :type float: boolean, (optional)
   :arg domain: Domain, Type of element that attribute is stored on
   :type domain: enum in :ref:`rna_enum_color_attribute_domain_items`, (optional)
   :arg data_type: Data Type, Type of data stored in attribute
   :type data_type: enum in :ref:`rna_enum_color_attribute_type_items`, (optional)

.. function:: brush_colors_flip()

   Swap primary and secondary brush colors

.. function:: face_select_all(*, action='TOGGLE')

   Change selection for all faces

   :arg action: Action, Selection action to execute

      * ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
      * ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: enum in [``'TOGGLE'``, ``'SELECT'``, ``'DESELECT'``, ``'INVERT'``], (optional)

.. function:: face_select_hide(*, unselected=False)

   Hide selected faces

   :arg unselected: Unselected, Hide unselected rather than selected objects
   :type unselected: boolean, (optional)

.. function:: face_select_less(*, face_step=True)

   Deselect Faces connected to existing selection

   :arg face_step: Face Step, Also deselect faces that only touch on a corner
   :type face_step: boolean, (optional)

.. function:: face_select_linked()

   Select linked faces

.. function:: face_select_linked_pick(*, deselect=False)

   Select linked faces under the cursor

   :arg deselect: Deselect, Deselect rather than select items
   :type deselect: boolean, (optional)

.. function:: face_select_loop(*, select=True, extend=False)

   Select face loop under the cursor

   :arg select: Select, If false, faces will be deselected
   :type select: boolean, (optional)
   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)

.. function:: face_select_more(*, face_step=True)

   Select Faces connected to existing selection

   :arg face_step: Face Step, Also select faces that only touch on a corner
   :type face_step: boolean, (optional)

.. function:: face_vert_reveal(*, select=True)

   Reveal hidden faces and vertices

   :arg select: Select, Specifies whether the newly revealed geometry should be selected
   :type select: boolean, (optional)

.. function:: grab_clone(*, delta=(0.0, 0.0))

   Move the clone source image

   :arg delta: Delta, Delta offset of clone image in 0.0 to 1.0 coordinates
   :type delta: :class:`mathutils.Vector` of 2 items in [-inf, inf], (optional)

.. function:: hide_show(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, action='HIDE', area='Inside', use_front_faces_only=False)

   Hide/show some vertices

   :arg xmin: X Min
   :type xmin: int in [-inf, inf], (optional)
   :arg xmax: X Max
   :type xmax: int in [-inf, inf], (optional)
   :arg ymin: Y Min
   :type ymin: int in [-inf, inf], (optional)
   :arg ymax: Y Max
   :type ymax: int in [-inf, inf], (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)
   :arg action: Visibility Action, Whether to hide or show vertices

      * ``HIDE``
        Hide -- Hide vertices.
      * ``SHOW``
        Show -- Show vertices.
   :type action: enum in [``'HIDE'``, ``'SHOW'``], (optional)
   :arg area: Visibility Area, Which vertices to hide or show

      * ``OUTSIDE``
        Outside -- Hide or show vertices outside the selection.
      * ``Inside``
        Inside -- Hide or show vertices inside the selection.
   :type area: enum in [``'OUTSIDE'``, ``'Inside'``], (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)

.. function:: hide_show_all(*, action='HIDE')

   Hide/show all vertices

   :arg action: Visibility Action, Whether to hide or show vertices

      * ``HIDE``
        Hide -- Hide vertices.
      * ``SHOW``
        Show -- Show vertices.
   :type action: enum in [``'HIDE'``, ``'SHOW'``], (optional)

.. function:: hide_show_lasso_gesture(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, action='HIDE', area='Inside', use_front_faces_only=False)

   Hide/show some vertices

   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
   :type use_smooth_stroke: boolean, (optional)
   :arg smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
   :type smooth_stroke_factor: float in [0.5, 0.99], (optional)
   :arg smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
   :type smooth_stroke_radius: int in [10, 200], (optional)
   :arg action: Visibility Action, Whether to hide or show vertices

      * ``HIDE``
        Hide -- Hide vertices.
      * ``SHOW``
        Show -- Show vertices.
   :type action: enum in [``'HIDE'``, ``'SHOW'``], (optional)
   :arg area: Visibility Area, Which vertices to hide or show

      * ``OUTSIDE``
        Outside -- Hide or show vertices outside the selection.
      * ``Inside``
        Inside -- Hide or show vertices inside the selection.
   :type area: enum in [``'OUTSIDE'``, ``'Inside'``], (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)

.. function:: hide_show_line_gesture(*, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5, action='HIDE', area='Inside', use_front_faces_only=False, use_limit_to_segment=False)

   Hide/show some vertices

   :arg xstart: X Start
   :type xstart: int in [-inf, inf], (optional)
   :arg xend: X End
   :type xend: int in [-inf, inf], (optional)
   :arg ystart: Y Start
   :type ystart: int in [-inf, inf], (optional)
   :arg yend: Y End
   :type yend: int in [-inf, inf], (optional)
   :arg flip: Flip
   :type flip: boolean, (optional)
   :arg cursor: Cursor, Mouse cursor style to use during the modal operator
   :type cursor: int in [0, inf], (optional)
   :arg action: Visibility Action, Whether to hide or show vertices

      * ``HIDE``
        Hide -- Hide vertices.
      * ``SHOW``
        Show -- Show vertices.
   :type action: enum in [``'HIDE'``, ``'SHOW'``], (optional)
   :arg area: Visibility Area, Which vertices to hide or show

      * ``OUTSIDE``
        Outside -- Hide or show vertices outside the selection.
      * ``Inside``
        Inside -- Hide or show vertices inside the selection.
   :type area: enum in [``'OUTSIDE'``, ``'Inside'``], (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)
   :arg use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
   :type use_limit_to_segment: boolean, (optional)

.. function:: hide_show_masked(*, action='HIDE')

   Hide/show all masked vertices above a threshold

   :arg action: Visibility Action, Whether to hide or show vertices

      * ``HIDE``
        Hide -- Hide vertices.
      * ``SHOW``
        Show -- Show vertices.
   :type action: enum in [``'HIDE'``, ``'SHOW'``], (optional)

.. function:: hide_show_polyline_gesture(*, path=None, action='HIDE', area='Inside', use_front_faces_only=False)

   Hide/show some vertices

   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg action: Visibility Action, Whether to hide or show vertices

      * ``HIDE``
        Hide -- Hide vertices.
      * ``SHOW``
        Show -- Show vertices.
   :type action: enum in [``'HIDE'``, ``'SHOW'``], (optional)
   :arg area: Visibility Area, Which vertices to hide or show

      * ``OUTSIDE``
        Outside -- Hide or show vertices outside the selection.
      * ``Inside``
        Inside -- Hide or show vertices inside the selection.
   :type area: enum in [``'OUTSIDE'``, ``'Inside'``], (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)

.. function:: image_from_view(*, filepath="")

   Make an image from biggest 3D view for reprojection

   :arg filepath: File Path, Name of the file
   :type filepath: string, (optional, never None)

.. function:: image_paint(*, stroke=None, mode='NORMAL', pen_flip=False)

   Paint a stroke into the image

   :arg stroke: Stroke
   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg mode: Stroke Mode, Action taken when a paint stroke is made

      * ``NORMAL``
        Regular -- Apply brush normally.
      * ``INVERT``
        Invert -- Invert action of brush for duration of stroke.
      * ``SMOOTH``
        Smooth -- Switch brush to smooth mode for duration of stroke.
      * ``ERASE``
        Erase -- Switch brush to erase mode for duration of stroke.
   :type mode: enum in [``'NORMAL'``, ``'INVERT'``, ``'SMOOTH'``, ``'ERASE'``], (optional)
   :arg pen_flip: Pen Flip, Whether a tablet's eraser mode is being used
   :type pen_flip: boolean, (optional)

.. function:: mask_box_gesture(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, use_front_faces_only=False, mode='VALUE', value=1.0)

   Mask within a rectangle defined by the cursor

   :arg xmin: X Min
   :type xmin: int in [-inf, inf], (optional)
   :arg xmax: X Max
   :type xmax: int in [-inf, inf], (optional)
   :arg ymin: Y Min
   :type ymin: int in [-inf, inf], (optional)
   :arg ymax: Y Max
   :type ymax: int in [-inf, inf], (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)
   :arg mode: Mode

      * ``VALUE``
        Value -- Set mask to the level specified by the 'value' property.
      * ``VALUE_INVERSE``
        Value Inverted -- Set mask to the level specified by the inverted 'value' property.
      * ``INVERT``
        Invert -- Invert the mask.
   :type mode: enum in [``'VALUE'``, ``'VALUE_INVERSE'``, ``'INVERT'``], (optional)
   :arg value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
   :type value: float in [0, 1], (optional)

.. function:: mask_flood_fill(*, mode='VALUE', value=0.0)

   Fill the whole mask with a given value, or invert its values

   :arg mode: Mode

      * ``VALUE``
        Value -- Set mask to the level specified by the 'value' property.
      * ``VALUE_INVERSE``
        Value Inverted -- Set mask to the level specified by the inverted 'value' property.
      * ``INVERT``
        Invert -- Invert the mask.
   :type mode: enum in [``'VALUE'``, ``'VALUE_INVERSE'``, ``'INVERT'``], (optional)
   :arg value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
   :type value: float in [0, 1], (optional)

.. function:: mask_lasso_gesture(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, use_front_faces_only=False, mode='VALUE', value=1.0)

   Mask within a shape defined by the cursor

   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
   :type use_smooth_stroke: boolean, (optional)
   :arg smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
   :type smooth_stroke_factor: float in [0.5, 0.99], (optional)
   :arg smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
   :type smooth_stroke_radius: int in [10, 200], (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)
   :arg mode: Mode

      * ``VALUE``
        Value -- Set mask to the level specified by the 'value' property.
      * ``VALUE_INVERSE``
        Value Inverted -- Set mask to the level specified by the inverted 'value' property.
      * ``INVERT``
        Invert -- Invert the mask.
   :type mode: enum in [``'VALUE'``, ``'VALUE_INVERSE'``, ``'INVERT'``], (optional)
   :arg value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
   :type value: float in [0, 1], (optional)

.. function:: mask_line_gesture(*, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5, use_front_faces_only=False, use_limit_to_segment=False, mode='VALUE', value=1.0)

   Mask to one side of a line defined by the cursor

   :arg xstart: X Start
   :type xstart: int in [-inf, inf], (optional)
   :arg xend: X End
   :type xend: int in [-inf, inf], (optional)
   :arg ystart: Y Start
   :type ystart: int in [-inf, inf], (optional)
   :arg yend: Y End
   :type yend: int in [-inf, inf], (optional)
   :arg flip: Flip
   :type flip: boolean, (optional)
   :arg cursor: Cursor, Mouse cursor style to use during the modal operator
   :type cursor: int in [0, inf], (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)
   :arg use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
   :type use_limit_to_segment: boolean, (optional)
   :arg mode: Mode

      * ``VALUE``
        Value -- Set mask to the level specified by the 'value' property.
      * ``VALUE_INVERSE``
        Value Inverted -- Set mask to the level specified by the inverted 'value' property.
      * ``INVERT``
        Invert -- Invert the mask.
   :type mode: enum in [``'VALUE'``, ``'VALUE_INVERSE'``, ``'INVERT'``], (optional)
   :arg value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
   :type value: float in [0, 1], (optional)

.. function:: mask_polyline_gesture(*, path=None, use_front_faces_only=False, mode='VALUE', value=1.0)

   Mask within a shape defined by the cursor

   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
   :type use_front_faces_only: boolean, (optional)
   :arg mode: Mode

      * ``VALUE``
        Value -- Set mask to the level specified by the 'value' property.
      * ``VALUE_INVERSE``
        Value Inverted -- Set mask to the level specified by the inverted 'value' property.
      * ``INVERT``
        Invert -- Invert the mask.
   :type mode: enum in [``'VALUE'``, ``'VALUE_INVERSE'``, ``'INVERT'``], (optional)
   :arg value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
   :type value: float in [0, 1], (optional)

.. function:: project_image(*, image='')

   Project an edited render from the active camera back onto the object

   :arg image: Image
   :type image: enum in [], (optional)

.. function:: sample_color(*, location=(0, 0), merged=False, palette=False)

   Use the mouse to sample a color in the image

   :arg location: Location
   :type location: int array of 2 items in [0, inf], (optional)
   :arg merged: Sample Merged, Sample the output display color
   :type merged: boolean, (optional)
   :arg palette: Add to Palette
   :type palette: boolean, (optional)

.. function:: texture_paint_toggle()

   Toggle texture paint mode in 3D view

.. function:: vert_select_all(*, action='TOGGLE')

   Change selection for all vertices

   :arg action: Action, Selection action to execute

      * ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
      * ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: enum in [``'TOGGLE'``, ``'SELECT'``, ``'DESELECT'``, ``'INVERT'``], (optional)

.. function:: vert_select_hide(*, unselected=False)

   Hide selected vertices

   :arg unselected: Unselected, Hide unselected rather than selected vertices
   :type unselected: boolean, (optional)

.. function:: vert_select_less(*, face_step=True)

   Deselect Vertices connected to existing selection

   :arg face_step: Face Step, Also deselect faces that only touch on a corner
   :type face_step: boolean, (optional)

.. function:: vert_select_linked()

   Select linked vertices

.. function:: vert_select_linked_pick(*, select=True)

   Select linked vertices under the cursor

   :arg select: Select, Whether to select or deselect linked vertices under the cursor
   :type select: boolean, (optional)

.. function:: vert_select_more(*, face_step=True)

   Select Vertices connected to existing selection

   :arg face_step: Face Step, Also select faces that only touch on a corner
   :type face_step: boolean, (optional)

.. function:: vert_select_ungrouped(*, extend=False)

   Select vertices without a group

   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)

.. function:: vertex_color_brightness_contrast(*, brightness=0.0, contrast=0.0)

   Adjust vertex color brightness/contrast

   :arg brightness: Brightness
   :type brightness: float in [-100, 100], (optional)
   :arg contrast: Contrast
   :type contrast: float in [-100, 100], (optional)

.. function:: vertex_color_dirt(*, blur_strength=1.0, blur_iterations=1, clean_angle=3.14159, dirt_angle=0.0, dirt_only=False, normalize=True)

   Generate a dirt map gradient based on cavity

   :arg blur_strength: Blur Strength, Blur strength per iteration
   :type blur_strength: float in [0.01, 1], (optional)
   :arg blur_iterations: Blur Iterations, Number of times to blur the colors (higher blurs more)
   :type blur_iterations: int in [0, 40], (optional)
   :arg clean_angle: Highlight Angle, Less than 90 limits the angle used in the tonal range
   :type clean_angle: float in [0, 3.14159], (optional)
   :arg dirt_angle: Dirt Angle, Less than 90 limits the angle used in the tonal range
   :type dirt_angle: float in [0, 3.14159], (optional)
   :arg dirt_only: Dirt Only, Don't calculate cleans for convex areas
   :type dirt_only: boolean, (optional)
   :arg normalize: Normalize, Normalize the colors, increasing the contrast
   :type normalize: boolean, (optional)
   :File: `startup\bl_operators\vertexpaint_dirt.py\:179 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\vertexpaint_dirt.py#L179>`__


.. function:: vertex_color_from_weight()

   Convert active weight into gray scale vertex colors

.. function:: vertex_color_hsv(*, h=0.5, s=1.0, v=1.0)

   Adjust vertex color Hue/Saturation/Value

   :arg h: Hue
   :type h: float in [0, 1], (optional)
   :arg s: Saturation
   :type s: float in [0, 2], (optional)
   :arg v: Value
   :type v: float in [0, 2], (optional)

.. function:: vertex_color_invert()

   Invert RGB values

.. function:: vertex_color_levels(*, offset=0.0, gain=1.0)

   Adjust levels of vertex colors

   :arg offset: Offset, Value to add to colors
   :type offset: float in [-1, 1], (optional)
   :arg gain: Gain, Value to multiply colors by
   :type gain: float in [0, inf], (optional)

.. function:: vertex_color_set(*, use_alpha=True)

   Fill the active vertex color layer with the current paint color

   :arg use_alpha: Affect Alpha, Set color completely opaque instead of reusing existing alpha
   :type use_alpha: boolean, (optional)

.. function:: vertex_color_smooth()

   Smooth colors across vertices

.. function:: vertex_paint(*, stroke=None, mode='NORMAL', pen_flip=False, override_location=False)

   Paint a stroke in the active color attribute layer

   :arg stroke: Stroke
   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg mode: Stroke Mode, Action taken when a paint stroke is made

      * ``NORMAL``
        Regular -- Apply brush normally.
      * ``INVERT``
        Invert -- Invert action of brush for duration of stroke.
      * ``SMOOTH``
        Smooth -- Switch brush to smooth mode for duration of stroke.
      * ``ERASE``
        Erase -- Switch brush to erase mode for duration of stroke.
   :type mode: enum in [``'NORMAL'``, ``'INVERT'``, ``'SMOOTH'``, ``'ERASE'``], (optional)
   :arg pen_flip: Pen Flip, Whether a tablet's eraser mode is being used
   :type pen_flip: boolean, (optional)
   :arg override_location: Override Location, Override the given `location` array by recalculating object space positions from the provided `mouse_event` positions
   :type override_location: boolean, (optional)

.. function:: vertex_paint_toggle()

   Toggle the vertex paint mode in 3D view

.. function:: visibility_filter(*, action='GROW', iterations=1, auto_iteration_count=True)

   Edit the visibility of the current mesh

   :arg action: Action

      * ``GROW``
        Grow Visibility -- Grow the visibility by one face based on mesh topology.
      * ``SHRINK``
        Shrink Visibility -- Shrink the visibility by one face based on mesh topology.
   :type action: enum in [``'GROW'``, ``'SHRINK'``], (optional)
   :arg iterations: Iterations, Number of times that the filter is going to be applied
   :type iterations: int in [1, 100], (optional)
   :arg auto_iteration_count: Auto Iteration Count, Use an automatic number of iterations based on the number of vertices of the sculpt
   :type auto_iteration_count: boolean, (optional)

.. function:: visibility_invert()

   Invert the visibility of all vertices

.. function:: weight_from_bones(*, type='AUTOMATIC')

   Set the weights of the groups matching the attached armature's selected bones, using the distance between the vertices and the bones

   :arg type: Type, Method to use for assigning weights

      * ``AUTOMATIC``
        Automatic -- Automatic weights from bones.
      * ``ENVELOPES``
        From Envelopes -- Weights from envelopes with user defined radius.
   :type type: enum in [``'AUTOMATIC'``, ``'ENVELOPES'``], (optional)

.. function:: weight_gradient(*, type='LINEAR', xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5)

   Draw a line to apply a weight gradient to selected vertices

   :arg type: Type
   :type type: enum in [``'LINEAR'``, ``'RADIAL'``], (optional)
   :arg xstart: X Start
   :type xstart: int in [-inf, inf], (optional)
   :arg xend: X End
   :type xend: int in [-inf, inf], (optional)
   :arg ystart: Y Start
   :type ystart: int in [-inf, inf], (optional)
   :arg yend: Y End
   :type yend: int in [-inf, inf], (optional)
   :arg flip: Flip
   :type flip: boolean, (optional)
   :arg cursor: Cursor, Mouse cursor style to use during the modal operator
   :type cursor: int in [0, inf], (optional)

.. function:: weight_paint(*, stroke=None, mode='NORMAL', pen_flip=False, override_location=False)

   Paint a stroke in the current vertex group's weights

   :arg stroke: Stroke
   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg mode: Stroke Mode, Action taken when a paint stroke is made

      * ``NORMAL``
        Regular -- Apply brush normally.
      * ``INVERT``
        Invert -- Invert action of brush for duration of stroke.
      * ``SMOOTH``
        Smooth -- Switch brush to smooth mode for duration of stroke.
      * ``ERASE``
        Erase -- Switch brush to erase mode for duration of stroke.
   :type mode: enum in [``'NORMAL'``, ``'INVERT'``, ``'SMOOTH'``, ``'ERASE'``], (optional)
   :arg pen_flip: Pen Flip, Whether a tablet's eraser mode is being used
   :type pen_flip: boolean, (optional)
   :arg override_location: Override Location, Override the given `location` array by recalculating object space positions from the provided `mouse_event` positions
   :type override_location: boolean, (optional)

.. function:: weight_paint_toggle()

   Toggle weight paint mode in 3D view

.. function:: weight_sample()

   Use the mouse to sample a weight in the 3D view

.. function:: weight_sample_group()

   Select one of the vertex groups available under current mouse position

.. function:: weight_set()

   Fill the active vertex group with the current paint weight

