#!/usr/bin/python3
""" Defines a function that returns the dictionary
 description with simple data structure 
 (list, dictionary, string, integer and boolean) 
 for JSON serialization of an obje
"""

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Defines a function that returns the dictionary
        description with simple data structure 
        (list, dictionary, string, integer and boolean) 
        for JSON serialization of an obje
        """
        keys = []
        for attr in self.__dict__:
            if attr is not None:
                keys.append((attr, self.__getattribute__(attr)))

        return dict(keys)



students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))