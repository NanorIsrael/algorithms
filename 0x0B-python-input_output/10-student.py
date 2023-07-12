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

    def to_json(self, attrs=None):
        """ Defines a function that returns the dictionary
        description with simple data structure 
        (list, dictionary, string, integer and boolean) 
        for JSON serialization of an obje
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




student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)
