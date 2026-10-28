Surface Operators
=================

.. module:: bpy.ops.surface

.. function:: primitive_nurbs_surface_circle_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Nurbs surface Circle

   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: primitive_nurbs_surface_curve_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Nurbs surface Curve

   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: primitive_nurbs_surface_cylinder_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Nurbs surface Cylinder

   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: primitive_nurbs_surface_sphere_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Nurbs surface Sphere

   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: primitive_nurbs_surface_surface_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Nurbs surface Patch

   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: primitive_nurbs_surface_torus_add(*, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Nurbs surface Torus

   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

