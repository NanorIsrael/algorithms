#!/usr/bin/python3
""" Defines a function that returns the dictionary
 description with simple data structure 
 (list, dictionary, string, integer and boolean) 
 for JSON serialization of an object
"""

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Defines a function that returns the dictionary
        description with simple data structure 
        (list, dictionary, string, integer and boolean) 
        for JSON serialization of an object
        """
        json = []
        if isinstance(attrs, list):
            for attr in attrs:
                if type(attr) == str:
                    if hasattr(self, attr):
                        json.append((attr, self.__getattribute__(attr)))
        else:
            for attr in self.__dict__:
                if attr is not None:
                    json.append((attr, self.__getattribute__(attr)))

        return dict(json)

    def reload_from_json(self, json):
        self.__dict__ = json
    



import os
import sys

read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))


save_to_json_file(j_student_1, path)
read_file(path)
print("\nSaved to disk")


print("Fake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))


print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

new_student_1.reload_from_json(j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
