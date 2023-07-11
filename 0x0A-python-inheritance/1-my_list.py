#!/usr/bin/python3
"""Defines a class MyList that inherits from list
"""

class MyList(list):
    """Defines a class MyList that inherits from list
    """
    def __init__(self):
         super().__init__(self)

    def print_sorted(self):
        """Defines a class MyList that inherits from list
    """
        A = self[:]
        A.sort()
        print(A)

