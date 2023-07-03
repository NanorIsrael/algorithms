#!/usr/bin/python3
"""This module defines a function that prints a text with 2 new lines
 after each of these characters: ., ? and :

>>> text_indentation('JohnDoe')
My name is John Doe
"""
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if  char in ['.', '?', ':']:
            print(char, end='')
            print('$')
            print('$')
            continue
        print(char, end='')

# text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
# Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
# Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
# Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
# Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
# rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
# stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
# cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
# beatiorem! Iam ruinas videres""")