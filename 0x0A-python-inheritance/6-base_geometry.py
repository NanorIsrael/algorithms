#!/usr/bin/python3
"""Defines an empty class BaseGeometry
"""

class BaseGeometry:
    """Defines an empty class BaseGeometry
    """
    def __init__(self):
        pass

    def area(self):
        """Defines an empty class BaseGeometry
         """
        raise Exception("area() is not implemented")




bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
