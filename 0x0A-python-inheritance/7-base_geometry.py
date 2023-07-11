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

    def integer_validator(self, name, value):
        """Validates class Rectangle parameter values
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            pass
