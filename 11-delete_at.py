#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    list_size = len(my_list)
    filtered_data = []
    if idx < 0:
        return (my_list)
    if idx > list_size:
        return (my_list)
    del my_list[idx]
    return (my_list)
    

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)