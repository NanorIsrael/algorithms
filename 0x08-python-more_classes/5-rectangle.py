#!/usr/bin/python3

"""This module defines an empty class Rectangle that defines a rectangle
"""
class Rectangle:

    """This module defines an empty class Rectangle t
    hat defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of this Rectangle instance.
            Returns:
            The width of this Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of this Rectangle instance.
        Args:
        value (int): The new width of this Rectangle.
        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of this Rectangle instance.
        Returns:
         The height of this Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of this Rectangle instance.
        Args:
        value (int): The new height of this Rectangle.
        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    
    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height
    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        rows = self.__width
        columns = self.__height

        if rows == 0 or columns == 0:
            return ("")

        rect = []
        idx = 0
        while idx < columns:
            rect.append("#" * rows)
            idx += 1
        return ("\n").join(rect)

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
    def __del__(self):
        """Print the message Bye rectangle... when an instance of Rectangle 
        is deleted"""
        del self
        print('Bye rectangle...')


my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
