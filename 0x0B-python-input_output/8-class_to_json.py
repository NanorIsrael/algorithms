#!/usr/bin/python3
""" Defines a function that returns the dictionary
 description with simple data structure 
 (list, dictionary, string, integer and boolean) 
 for JSON serialization of an obje
"""

def class_to_json(obj):
    """ Defines a function that returns the dictionary
    description with simple data structure 
    (list, dictionary, string, integer and boolean) 
    for JSON serialization of an obje
    """
    keys = []
    for attr in obj.__dict__:
        if attr is not None:
            keys.append((attr, obj.__getattribute__(attr)))

    return dict(keys)









class MyClass:
    """ My class
    """

    score = 0

    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)


m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

mj = class_to_json(1)
print(type(mj))
print(mj)
mj = class_to_json([])
print(type(mj))
print(mj)
mj = class_to_json("hello")
print(type(mj))
print(mj)