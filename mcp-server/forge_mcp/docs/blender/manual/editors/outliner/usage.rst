
*****
Usage
*****

Relations Management
====================

.. figure:: /images/editors_outliner_usage_relations.png
   :align: right

   Linking objects to a collection.

You can move an object (or collection) to a different parent collection by dragging and dropping.

You can link an object (or collection) to a parent collection by dragging and then holding
:kbd:`Ctrl` while dropping. This way, you can make the object (or child collection) part of
multiple parent collections at the same time.

You can parent an object to another by dragging and then holding :kbd:`Shift` while dropping.

.. note::

   Drag and drop will attempt to operate on the entire selection. Selected data-blocks
   that are incompatible with the operation will remain unmodified.


Modifiers, Constraints, and Visual Effects
==========================================

You can manage :doc:`Modifiers </modeling/modifiers/index>`, :doc:`Constraints </animation/constraints/index>`, and
:doc:`Visual Effects </grease_pencil/visual_effects/index>` from the Outliner in a couple of ways:

- You can drag and drop individual items to change their order within the :ref:`stack <modifier-stack>` or to copy
  them to another object.
- You can drag and drop the group item (e.g. *Modifiers*) to copy the whole stack to another object.
  The target object's existing stack will be replaced.
- You can apply and delete items using the context menu.


Drag & Dropping to 3D Viewport
==============================

Dragging an object from the Outliner to the :doc:`3D Viewport </editors/3dview/index>`
creates a :doc:`duplicate </scene_layout/object/editing/duplicate>` -- a new object with its own copy
of the underlying object data.

Dragging object data from the Outliner to the 3D Viewport creates a
:doc:`linked duplicate </scene_layout/object/editing/duplicate_linked>` -- a new object that references
the same underlying object data.
