#!/usr/bin/python3
"""Square class"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        for x in range(self.__size):
            print("#" * self.__size)
        if self.size == 0:
            print()
