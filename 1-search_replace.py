#!/usr/bin/python3

# def search_replace(my_list, search, replace):
#     new_list = []
#     for num in my_list:
#         if num != search:
#             new_list.append(num)
#         else:
#             new_list.append(replace)
#     return new_list


def search_replace(my_list, search, replace):
    return [num if num != search else replace for num in my_list]

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)