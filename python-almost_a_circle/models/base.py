#!/usr/bin/python3
"""
Module contains class Base

1.  Contains private class __nb_objects, and class constructor __init__
15. Add the static method `def to_json_string(list_dictionaries):`
    that returns the JSON string representation of list_dictionaries
16. Add the class method `def save_to_file(cls, list_objs):`
    that writes the JSON string representation of list_objs to a file
17. Add  the static method `def from_json_string(json_string):`
    that returns the list of the JSON string representation json_string
"""


import json


class Base:
    """
    defines class Base
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id, increment class attribute if no id and set as id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ list of dictionaries to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file """
        filename = "{}.json".format(cls.__name__)

        list_dic = []
        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as fd:
            fd.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Square":
            uwu = cls(6)
        elif cls.__name__ == "Rectangle":
            uwu = cls(6, 6)
        uwu.update(**dictionary)
        return uwu
