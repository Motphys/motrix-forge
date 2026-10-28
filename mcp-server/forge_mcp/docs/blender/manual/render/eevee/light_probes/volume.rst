******************
Light Probe Volume
******************

A volume probe records the light incoming from all directions at many locations inside a volume.

The light is then filtered and only the diffuse light is recorded.
The capture point positions are visible as an overlay when the Irradiance Volume object is selected.

If an object is not inside any Irradiance Volume, or if the indirect lighting has not been baked,
the world's diffuse lighting will be used to shade it.

.. tip::

   - When lighting indoor environments, try to align grids with the room shape.
   - Try not to put too much resolution in empty areas or areas with a low amount of lighting variation.
   - Bad samples can be fixed by adding a smaller grid near the problematic area.
   - Large scenes may require using many volumes with different level of details.


Properties
==========

.. reference::

   :Panel:     :menuselection:`Object Data --> Probe`

Intensity
   Intensity factor of the recorded lighting.
   Making this parameter anything other than 1.0 is not physically correct.
   To be used for tweaking, animating or artistic purposes.

.. rubric:: Sampling Bias

Normal Bias
   Offset sampling of the irradiance grid in the surface normal direction to reduce light bleeding.
   Can lead to specular appearance of diffuse surface if set too high.

View Bias
   Offset sampling of the irradiance grid in the viewing direction to reduce light bleeding.
   Can lead to view dependent result if set too high. Prefer this if camera is static.

Facing Bias
   When set to zero, avoids capturing points behind the shaded surface to bleed light onto
   the shaded surface. This produces non-smooth interpolation when the capture resolution is high.
   Increasing this bias will make the interpolation smoother but also introduce some light bleeding.


.. rubric:: Validity & Dilation

During the baking process, a validity score is assigned to each capture point.
This score is based on the number of back-faces hit when capturing the incoming lighting.
Only materials with *Single Sided* turned on for Light Probe Volumes will reduce the validity score.

Validity Threshold
   Capture points with validity below this threshold will be ignored during lighting interpolation.
   This remove the influence of capture points trapped inside closed geometry, reducing the artifacts they produced.

Dilation Threshold
   Capture points with validity below this threshold will have their data replaced using valid neighbors.

Radius
   Radius in capture points in which to search for a valid neighbor.


.. _eevee-lightprobe-volume-bake:

Bake
----

Light probe volume light data is static and needs to be manually baked.
Once baked, the data is stored inside the object data-block and can be moved, animated and linked
between blender files.

.. note::

   Baking uses the render visibility of the objects in the scene.

During baking, the scene is converted into a different representation to accelerate light transport.
This representation can be very memory intensive and prevents baking if it cannot fit inside the GPU memory.
There are a few way to deal with this issue:

- Larger scenes should be divided into smaller sections or use different level of details.
- Reduce *Surfel Resolution*.
- Turn off the light probe volume visibility option on objects that have little to no effect in the bake.

.. tip::

   The internal scene representation can be inspected using the ``Debug Value`` 3, 4 and 5.

Resolution
----------

Resolution X, Y, Z
   Spatial resolution for volumetric light probes is determined per probe.
   The local volume is divided into a regular grid of the specified dimensions.
   The lighting will be captured for each cell in this grid.

Bake Samples
   Number of ray directions to evaluate when baking.
   This increases the baking time proportionally to the size of the scene representation.

Surfel Resolution
   Number of surfels to spawn in one local unit distance.
   Higher values increase quality, but have a huge impact on memory usage.

   .. tip::

      A good value is twice the maximum *Resolution*.


Capture
-------

Capture Distance
   Distance around the light probe volume that will be captured during the bake.
   A distance of 0 will only considered the inside of the volume.

World Contribution
   Bake incoming light from the world instead of just visibility for more accurate lighting,
   but lose correct blending to surrounding irradiance volumes.

Indirect Light Contribution
   Capture light bounces from light source.

Emission Contribution
   Capture emissive surfaces when baking.


Clamping
^^^^^^^^

Direct Light
   Clamp incoming direct light. 0.0 disables direct light clamping.
   Here direct light refers to the light that bounces only once (from the light object)
   or light coming from emissive materials.

Indirect Light
   Clamp incoming indirect light. 0.0 disables indirect light clamping.
   Here indirect light refers to the light that bounces off a surface after the first bounce (from the light object)
   or during the first bounce if the light comes from emissive materials.

.. tip::

   Setting *Clamp Indirect* to a very small non-zero value will effectively only record the first light bounce
   leading.


Offset
^^^^^^

In order to reduce artifacts caused by bad capture point positioning,
the bake process adjusts their location before capturing light.
It moves the capture points slightly away from surrounding surfaces and tries to move them out of objects
if they are not too far bellow the surface.

Surface Offset
   Distance to move the capture points away from surfaces.

Search Distance
   Distance to search for valid capture positions if the capture point is near the back-face of a single-sided object.

.. note::

   Only materials with *Single Sided* turned on for Light Probe Volumes will move capture point position.


Viewport Display
----------------

Data
   Show the captured light using small diffuse spheres of the given size.

Influence
   Show the influence bounds in the 3D Viewport. The inner sphere is where the falloff starts.

Clipping
   Show the clipping distance in the 3D Viewport.
