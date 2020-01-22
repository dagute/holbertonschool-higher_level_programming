#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    def class_to_json(obj):
        """define class to json"""
        if hasattr(obj, "__slots__"):
            return obj.__slots__
        if hasattr(obj, "__dict__"):
            return obj.__dict__
