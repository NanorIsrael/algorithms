#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """class Square that defines a square by: (based on 3-square.py)
    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError exception 
    with the message size must be an integer
    if size is less than 0, raise a ValueError exception 
    with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self): that returns the current square area"""    

    def __init__(self, size=0):
        if type(size) != int :
            raise ValueError("size must be an integer")
        if size < 0 :
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """calculates the area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """returns the of a square"""
        return self.__size
    @size.setter
    def size(self, value):
         """sets the size of a square"""
        if type(value) != int :
            raise ValueError("size must be an integer")
        if value < 0 :
            raise ValueError("size must be >= 0")
        self.__size = value


my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
