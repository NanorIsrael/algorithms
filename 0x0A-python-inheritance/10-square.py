#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle and BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('8-retangle').Rectangle

class Square(Rectangle, BaseGeometry):
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
        return self.__width * self.__height


