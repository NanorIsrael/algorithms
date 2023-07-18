#!/usr/bin/python3
"""Defines a base class"""

import json


class Base:
    """Defines a base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the dictionary representation of list"""
        if list_dictionaries:
            json_list = json.dumps(list_dictionaries)
            return json_list
        else:
            return '[]'

    @staticmethod
    def from_json_string(json_string):
        """Returns the string list representation back to a list"""
        if json_string:
            json_list = json.loads(json_string)
            return json_list
        else:
            return []
        
    @classmethod
    def save_to_file(cls, list_objs):
        """Stores the list representation of a dictionary in a file"""
       
        with open(''+ cls.__name__ + '.json', 'w') as my_file:
            if list_objs:
                list_obj = []
                for rect in list_objs:
                    dict_rect = rect.to_dictionary()
                    list_obj.append(dict_rect)
                json_list = cls.to_json_string(list_obj)
                my_file.write(json_list)
            else:
                json_list = cls.to_json_string([])
                my_file.write(json_list)
    
    @classmethod
    def create(cls, **dictionary):
        """Coverts a json string to a dictionary"""

        dummy_i = cls(1, 1, 1, 1)
        dummy_i.update(**dictionary)
        return dummy_i

    @classmethod
    def load_from_file(cls):
        try:
            with open(''+ cls.__name__ + '.json', 'r', encoding='UTF8') as my_file:
                file_content = my_file.read()
                result = cls.from_json_string(file_content)
                instance_list = []
                for dict_obj in result:
                    instance = cls.create(**dict_obj)
                    instance_list.append(instance)
                return instance_list
        except:
            return []