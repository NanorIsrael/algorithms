#!/usr/bin/python3

"""
This module defines a function
that prints a square with the character #.

>>> print_square(2)
##
##
"""


def print_square(size):
    if size is None:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    rows = size
    columns = size
    for col in range(columns):
        for row in range(rows):
            print("#", end="")
        print()

