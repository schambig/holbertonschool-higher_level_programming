#!/usr/bin/python3
"""
Contains function that returns JSON representation of obj (string)
"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
