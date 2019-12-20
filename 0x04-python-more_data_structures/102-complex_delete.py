#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    for key, x in list(a_dictionary.items()):
        if x is value:
            del a_dictionary[key]
    return a_dictionary
