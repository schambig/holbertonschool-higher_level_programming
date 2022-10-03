#!/usr/bin/python3
"Contains function that creates a Python obj from JSON file"
import json


def load_from_json_file(filename):
    """function that writes an Object to a text file,
    using a JSON representation"""
    with open(filename, 'r') as f:
        return json.load(f)
