#!/usr/bin/python3
""" Defines a function def pascal_triangle(n):
that returns a list of lists of integers representing the
Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """ Defines a function def pascal_triangle(n):
    that returns a list of lists of integers representing the
    Pascal’s triangle of n:
    """
    if n is None or n <= 0:
        return []
    if n == 1:
        return [[1]]
    triangle_vals = []
    for x in range(0, n):
        triangle_sides = [1]
        y = x
        idx = 0
        while y > 0:
            prev = triangle_vals[-1]
            if idx < len(prev) - 1:
                triangle_sides.append(prev[idx] + prev[idx + 1])
            else:
                triangle_sides.append(prev[idx])
            idx += 1
            y -= 1
        triangle_vals.append(triangle_sides)
    return triangle_vals


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))