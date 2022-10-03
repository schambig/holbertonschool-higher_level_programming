#!/usr/bin/python3
"""Contains class Student that initializes public instance attributes
first_name, last_name, and age,and has public method to_json that returns
dictionary representation of requested attributes or all if none were requested
"""


class Student:
    """My class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            k = {}
            for a in attrs:
                if a in self.__dict__:
                    k[a] = self.__dict__[a]
            return k
        return self.__dict__
