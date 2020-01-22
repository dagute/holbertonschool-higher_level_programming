#!/usr/bin/python3
"""Read n lines"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for x in range(0, nb_lines):
                print(f.readline(), end="")
