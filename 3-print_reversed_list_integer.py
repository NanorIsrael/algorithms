#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_size = len(my_list)
    while list_size > 0:
        list_size -= 1
        print("{:d}".format(my_list[list_size]))


print_reversed_list_integer([1, 2, 3, 4, 5])