#!/usr/bin/python3

"""
This module defines a function that prints 
My name is <first name> <last name>.

>>> say_my_name('John','Doe')
My name is John Doe
"""


def say_my_name(first_name, last_name=""):
    """Return a function that prints 
    My name is <first name> <last name>.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
