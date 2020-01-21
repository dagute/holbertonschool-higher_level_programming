#!/usr/bin/python3
"""Can I"""


def add_attribute(obj, key, value):
    """adds a new attribute to an object if it’s possible"""
    if not hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
