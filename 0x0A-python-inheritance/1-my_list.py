#!/usr/bin/python3
"""My list"""


class MyList(list):
    """that inherits from list"""
    def print_sorted(self):
        print(sorted(self))
