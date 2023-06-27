#!/usr/bin/python3
"""Defines a class square"""

class Square:
    """class Square that defines a square by: (based on 1-square.py)
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >= 0"""    

    def __init__(self, size=0):
        if type(size) != int :
            raise ValueError("size must be an integer")
        if size < 0 :
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """calculates the area of a square"""
        return self.__size ** 2



my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
