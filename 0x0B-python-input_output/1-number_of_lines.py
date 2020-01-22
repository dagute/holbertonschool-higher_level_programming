#!/usr/bin/python3
"""Number of lines"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    n = 0
    with open(filename, 'r') as f:
        for line in f:
            n += 1
    return n
