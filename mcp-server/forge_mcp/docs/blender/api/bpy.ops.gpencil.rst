Gpencil Operators
=================

.. module:: bpy.ops.gpencil

.. function:: annotate(*, mode='DRAW', arrowstyle_start='NONE', arrowstyle_end='NONE', use_stabilizer=False, stabilizer_factor=0.75, stabilizer_radius=35, stroke=None, wait_for_input=True)

   Make annotations on the active data

   :arg mode: Mode, Way to interpret mouse movements

      * ``DRAW``
        Draw Freehand -- Draw freehand stroke(s).
      * ``DRAW_STRAIGHT``
        Draw Straight Lines -- Draw straight line segment(s).
      * ``DRAW_POLY``
        Draw Poly Line -- Click to place endpoints of straight line segments (connected).
      * ``ERASER``
        Eraser -- Erase Annotation strokes.
   :type mode: enum in [``'DRAW'``, ``'DRAW_STRAIGHT'``, ``'DRAW_POLY'``, ``'ERASER'``], (optional)
   :arg arrowstyle_start: Start Arrow Style, Stroke start style

      * ``NONE``
        None -- Don't use any arrow/style in corner.
      * ``ARROW``
        Arrow -- Use closed arrow style.
      * ``ARROW_OPEN``
        Open Arrow -- Use open arrow style.
      * ``ARROW_OPEN_INVERTED``
        Segment -- Use perpendicular segment style.
      * ``DIAMOND``
        Square -- Use square style.
   :type arrowstyle_start: enum in [``'NONE'``, ``'ARROW'``, ``'ARROW_OPEN'``, ``'ARROW_OPEN_INVERTED'``, ``'DIAMOND'``], (optional)
   :arg arrowstyle_end: End Arrow Style, Stroke end style

      * ``NONE``
        None -- Don't use any arrow/style in corner.
      * ``ARROW``
        Arrow -- Use closed arrow style.
      * ``ARROW_OPEN``
        Open Arrow -- Use open arrow style.
      * ``ARROW_OPEN_INVERTED``
        Segment -- Use perpendicular segment style.
      * ``DIAMOND``
        Square -- Use square style.
   :type arrowstyle_end: enum in [``'NONE'``, ``'ARROW'``, ``'ARROW_OPEN'``, ``'ARROW_OPEN_INVERTED'``, ``'DIAMOND'``], (optional)
   :arg use_stabilizer: Stabilize Stroke, Helper to draw smooth and clean lines. Press Shift for an invert effect (even if this option is not active)
   :type use_stabilizer: boolean, (optional)
   :arg stabilizer_factor: Stabilizer Stroke Factor, Higher values gives a smoother stroke
   :type stabilizer_factor: float in [0, 1], (optional)
   :arg stabilizer_radius: Stabilizer Stroke Radius, Minimum distance from last point before stroke continues
   :type stabilizer_radius: int in [0, 200], (optional)
   :arg stroke: Stroke
   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg wait_for_input: Wait for Input, Wait for first click instead of painting immediately
   :type wait_for_input: boolean, (optional)

.. function:: annotation_active_frame_delete()

   Delete the active frame for the active Annotation Layer

.. function:: annotation_add()

   Add new Annotation data-block

.. function:: data_unlink()

   Unlink active Annotation data-block

.. function:: layer_annotation_add()

   Add new Annotation layer or note for the active data-block

.. function:: layer_annotation_move(*, type='UP')

   Move the active Annotation layer up/down in the list

   :arg type: Type
   :type type: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: layer_annotation_remove()

   Remove active Annotation layer

.. function:: tint_flip()

   Switch tint colors

   :File: `startup\bl_ui\properties_grease_pencil_common.py\:709 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_ui\properties_grease_pencil_common.py#L709>`__

