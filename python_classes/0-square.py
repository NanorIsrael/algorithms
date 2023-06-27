#!/usr/bin/python3

class Square:
    """an empty class Square that defines a square"""    
    pass


Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
