#!/usr/bin/python3
"""This module defines a function that prints a text with 2 new lines
 after each of these characters: ., ? and :

>>> text_indentation('JohnDoe')
My name is John Doe
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")







# def text_indentation(text):
#     if not isinstance(text, str):
#         raise TypeError("text must be a string")
#     for char in text:
#         if  char in ['.', '?', ':']:
#             print(char, end='')
#             print('')
#             print('')
#             continue
#         print(char, end='')