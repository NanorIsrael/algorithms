#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        sum = 0
        sum = a / b
    except ZeroDivisionError:
        sum = None
    finally:
        print("Inside result: {}".format(sum))
    return sum


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
