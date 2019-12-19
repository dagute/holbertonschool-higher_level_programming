#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new = {}
    for key in a_dictionary:
        d = a_dictionary[key] * 2
        new[key] = d
    return new
