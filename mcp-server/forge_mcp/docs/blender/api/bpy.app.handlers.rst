Application Handlers (bpy.app.handlers)
=======================================

.. module:: bpy.app.handlers

This module contains callback lists


Basic Handler Example
+++++++++++++++++++++

This script shows the most simple example of adding a handler.

.. literalinclude:: ..\examples\bpy.app.handlers.py
   :lines: 8-


Persistent Handler Example
++++++++++++++++++++++++++

By default handlers are freed when loading new files, in some cases you may
want the handler stay running across multiple files (when the handler is
part of an add-on for example).

For this the :data:`bpy.app.handlers.persistent` decorator needs to be used.

.. literalinclude:: ..\examples\bpy.app.handlers.1.py
   :lines: 12-


Note on Altering Data
+++++++++++++++++++++

Altering data from handlers should be done carefully. While rendering the
``frame_change_pre`` and ``frame_change_post`` handlers are called from one
thread and the viewport updates from a different thread. If the handler changes
data that is accessed by the viewport, this can cause a crash of Blender. In
such cases, lock the interface (Render → Lock Interface or
:data:`bpy.types.RenderSettings.use_lock_interface`) before starting a render.

Below is an example of a mesh that is altered from a handler:

.. literalinclude:: ..\examples\bpy.app.handlers.2.py
   :lines: 16-

.. data:: animation_playback_post

   on ending animation playback. Accepts two arguments: The scene datablock and the dependency graph being updated


.. data:: animation_playback_pre

   on starting animation playback. Accepts two arguments: The scene datablock and the dependency graph being updated


.. data:: annotation_post

   on drawing an annotation (after)


.. data:: annotation_pre

   on drawing an annotation (before)


.. data:: blend_import_post

   on linking or appending data (after), get a single `BlendImportContext` parameter


.. data:: blend_import_pre

   on linking or appending data (before), get a single `BlendImportContext` parameter


.. data:: composite_cancel

   on a compositing background job (cancel). Accepts one argument: the scene datablock


.. data:: composite_post

   on a compositing background job (after). Accepts one argument: the scene datablock


.. data:: composite_pre

   on a compositing background job (before). Accepts one argument: the scene datablock


.. data:: depsgraph_update_post

   on depsgraph update (post). Accepts two arguments: The scene datablock and the dependency graph being updated


.. data:: depsgraph_update_pre

   on depsgraph update (pre). Accepts two arguments: The scene datablock and the dependency graph being updated


.. data:: frame_change_post

   Called after frame change for playback and rendering, after the data has been evaluated for the new frame. Accepts two arguments: The scene datablock and the dependency graph being updated


.. data:: frame_change_pre

   Called after frame change for playback and rendering, before any data is evaluated for the new frame. This makes it possible to change data and relations (for example swap an object to another mesh) for the new frame. Note that this handler is **not** to be used as 'before the frame changes' event. The dependency graph is not available in this handler, as data and relations may have been altered and the dependency graph has not yet been updated for that. Accepts two arguments: The scene datablock and the dependency graph being updated


.. data:: load_factory_preferences_post

   on loading factory preferences (after)


.. data:: load_factory_startup_post

   on loading factory startup (after)


.. data:: load_post

   on loading a new blend file (after). Accepts one argument: the file being loaded, an empty string for the startup-file.


.. data:: load_post_fail

   on failure to load a new blend file (after). Accepts one argument: the file being loaded, an empty string for the startup-file.


.. data:: load_pre

   on loading a new blend file (before).Accepts one argument: the file being loaded, an empty string for the startup-file.


.. data:: object_bake_cancel

   on canceling a bake job; will be called in the main thread. Accepts one argument: the object datablock being baked


.. data:: object_bake_complete

   on completing a bake job; will be called in the main thread. Accepts one argument: the object datablock being baked


.. data:: object_bake_pre

   before starting a bake job. Accepts one argument: the object datablock being baked


.. data:: redo_post

   on loading a redo step (after)


.. data:: redo_pre

   on loading a redo step (before)


.. data:: render_cancel

   on canceling a render job. Accepts one argument: the scene datablock being rendered


.. data:: render_complete

   on completion of render job. Accepts one argument: the scene datablock being rendered


.. data:: render_init

   on initialization of a render job. Accepts one argument: the scene datablock being rendered


.. data:: render_post

   on render (after)


.. data:: render_pre

   on render (before)


.. data:: render_stats

   on printing render statistics. Accepts one argument: the render stats (render/saving time plus in background mode frame/used [peak] memory).


.. data:: render_write

   on writing a render frame (directly after the frame is written)


.. data:: save_post

   on saving a blend file (after). Accepts one argument: the file being saved, an empty string for the startup-file.


.. data:: save_post_fail

   on failure to save a blend file (after). Accepts one argument: the file being saved, an empty string for the startup-file.


.. data:: save_pre

   on saving a blend file (before). Accepts one argument: the file being saved, an empty string for the startup-file.


.. data:: translation_update_post

   on translation settings update


.. data:: undo_post

   on loading an undo step (after)


.. data:: undo_pre

   on loading an undo step (before)


.. data:: version_update

   on ending the versioning code


.. data:: xr_session_start_pre

   on starting an xr session (before)


.. data:: persistent

   Function decorator for callback functions not to be removed when loading new files


