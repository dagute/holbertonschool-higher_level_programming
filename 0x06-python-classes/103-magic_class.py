#!/usr/bin/python3
import math
"""Bytecode Python"""


class MagicClass:
    """class MagicClass"""
    def __init__(self, radius=0):
        """init"""
        self.__radius = 0
        if (type(radius) is not int) and (type(radius) is not float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """area"""
        return self._radius ** 2 * math.pi

        def circumference(self):
            """perimeter"""
            return 2 * math.pi * self.__radius
