ID Property Access (idprop.types)
=================================

.. module:: idprop.types

.. class:: idprop.types.IDPropertyArray


   .. method:: to_list()
   
      Return the array as a list.


   .. attribute:: typecode

      The type of the data in the array {'f': float, 'd': double, 'i': int, 'b': bool}.




.. class:: idprop.types.IDPropertyGroup


   .. method:: clear()
   
      Clear all members from this group.


   .. method:: get(key, default=None)
   
      Return the value for key, if it exists, else default.


   .. method:: items()
   
      Iterate through the items in the dict; behaves like dictionary method items.


   .. method:: keys()
   
      Return the keys associated with this group as a list of strings.


   .. method:: pop(key, default)
   
      Remove an item from the group, returning a Python representation.
   
      :raises KeyError: When the item doesn't exist.
   
      :arg key: Name of item to remove.
      :type key: str
      :arg default: Value to return when key isn't found, otherwise raise an exception.
      :type default: Any


   .. method:: to_dict()
   
      Return a purely Python version of the group.


   .. method:: update(other)
   
      Update key, values.
   
      :arg other: Updates the values in the group with this.
      :type other: :class:`IDPropertyGroup` | dict[str, Any]


   .. method:: values()
   
      Return the values associated with this group.


   .. attribute:: name

      The name of this Group.




.. class:: idprop.types.IDPropertyGroupIterItems




.. class:: idprop.types.IDPropertyGroupIterKeys




.. class:: idprop.types.IDPropertyGroupIterValues




.. class:: idprop.types.IDPropertyGroupViewItems




.. class:: idprop.types.IDPropertyGroupViewKeys




.. class:: idprop.types.IDPropertyGroupViewValues




