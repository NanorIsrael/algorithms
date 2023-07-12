#!/usr/bin/python3
""" Defines a function
that creates an Object from a “JSON file”
"""

import json
def load_from_json_file(filename):
    """ Defines a function that creates
    an Object from a “JSON file”
    """
    with open(filename, 'r', encoding='UTF8') as my_file:
        return json.load(my_file)
