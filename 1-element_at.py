#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return (None)
    if idx >= len(my_list):
        return (None)
    return (my_list[idx])

element_at([1, 2, 3, 4, 5], 3)