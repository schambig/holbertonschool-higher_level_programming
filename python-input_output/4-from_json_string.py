#!/usr/bin/python3
"""
Contains function that returns python data structure from JSON string
"""
import json


def from_json_string(my_str):
    """function that returns an object (Python data strcuture)
    represented by a JSON string"""
    return(json.loads(my_str))
