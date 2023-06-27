#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """class Square that defines a square by:
    (based on 4-square.py)
    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a 
    TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the
    message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self):
    that returns the current square area
    Public instance method: def my_print(self):
    that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line"""    

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
    
    def my_print(self):
        """prints the area of a square"""
        idx = 1
        if self.__size == 0:
            print()
            return
        while (idx > 0 and idx <= self.area()):
            print("#" * self.__size)
            idx += self.__size



my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")