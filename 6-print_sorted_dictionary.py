#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary)
    for i, k in enumerate(new_dict):
        print('{}: {}'.format(k, a_dictionary[k]))

# a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
# print_sorted_dictionary(a_dictionary)