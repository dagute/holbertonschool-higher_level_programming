#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, second):
        return self.__size < second.__size

    def __le__(self, second):
        return self.__size <= second.__size

    def __gt__(self, second):
        return self.__size > second.__size

    def __ge__(self, second):
        return self.__size >= second.__size

    def __eq__(self, second):
        return self.__size == second.__size

    def __ne__(self, second):
        return self.__size != second.__size
