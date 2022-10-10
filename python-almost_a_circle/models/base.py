#!/usr/bin/python3
"""
Module contains class Base

1.  Contains private class __nb_objects, and class constructor __init__
15. Add the static method `def to_json_string(list_dictionaries):`
    that returns the JSON string representation of list_dictionaries
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
