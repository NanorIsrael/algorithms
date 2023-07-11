#!/usr/bin/python3
"""Defines a that returns True if the object is an instance
 of a class that inherited (directly or indirectly) from the
  specified class ; otherwise False

"""


def inherits_from(obj, a_class):
    """that returns True if the object is an instance of a class
     that inherited (directly or indirectly) from the specified
      class ; otherwise False
 
    """
    return (isinstance(obj, a_class) and
           any(
               issubclass(type(obj), subclass) 
               for subclass in a_class.__subclasses__()
               ))



a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
