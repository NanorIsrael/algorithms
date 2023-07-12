#!/usr/bin/python3
""" Defines a function
that creates an Object from a “JSON file”
"""

import json
from pathlib import Path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(A):
    item_list = []
    my_file = Path("add_item.json")

    if not my_file.exists():
        save_to_json_file(A, my_file)

    else:
        item_list = load_from_json_file("add_item.json")

        for x in A:
            item_list.append(x)
        save_to_json_file(item_list, "add_item.json")

if __name__ == "__main__":
    import sys
    add_item(sys.argv[1:])
