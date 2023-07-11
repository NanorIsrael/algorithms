#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle and BaseGeometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__width = size
        self.__height = size

    def area(self):
        """Calculates the area of the square
        """
        return self.width * self.height

    def __str__(self):
        return "[Square] {}/{}".format(self.width, self.height)