"""
This module defines a function that takes in two
integers and return their sum.

>>> add_integer(1, 99)
100
"""
def add_integer(a, b=98):
    """Return the factorial of n, an exact integer >= 0.

    """
    # a, b = int(a), int(b)
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
