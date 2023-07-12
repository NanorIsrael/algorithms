#!/usr/bin/python3
""" writes a string to a text file (UTF8) and 
returns the number of characters written:
"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
     and returns the number of characters written:
    """
    if not isinstance(filename, str):
        return

    if not isinstance(text, str):
        return

    if filename is None or len(filename) == 0:
        return ""
    with open(filename, mode='w', encoding='UTF8') as my_file:
        data = my_file.write(text)

    return data

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
