#!/usr/bin/python3
"""Defines a class square"""

class Square:
    """class Square that defines a square by: (based on 0-square.py)
        Private instance attribute: size
        Instantiation with size (no type/value verification)
        You are not allowed to import any module"""    

    def __init__(self, size=0):
        self.__size = size


# Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)