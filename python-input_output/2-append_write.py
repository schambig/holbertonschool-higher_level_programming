#!/usr/bin/python3
"""Defines a file-appending function"""


def append_write(filename="", text=""):
    """appends to text file and returns num chars added"""
    with open(filename, 'a', encoding="utf-8") as f:
        return(f.write(text))
