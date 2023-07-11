#!/usr/bin/python3
"""
>>> print(print_ops(["5", "-2", "4", "C", "D", "9", "+", "+"]))
27
>>> print(print_ops(["5", "-2", "C", "D", "+",]))
30
>>> print(print_ops([]))
0
"""
def print_ops(ops):
    if ops is None or len(ops) == 0:
        return 0

    result = 0
    prev = ops[0]
    new_val = 0
    counter = 0
    num_list = []
    for  val in ops:
        if val in ['+', '-', 'C', 'D']:
            if val == '+':
                new_val = num_list[-1] + num_list[-2]
                num_list.append(new_val)
            if val == '-':
                new_val = num_list[-1] - num_list[-2]
                num_list.append(new_val)
            if val == 'C':
                del num_list[-1]
            if val == 'D':
                new_val = num_list[-1] * 2
                num_list.append(new_val)
        else:
            prev = int(val)
            num_list.append(prev)
        counter += 1
    for x in num_list:
        result += x
    return result

my_ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]


