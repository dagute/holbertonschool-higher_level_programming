#!/usr/bin/python3
"""defines a square"""


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)

    def __str__(self):
        """define str"""
        new = ""
        if self.__size == 0:
            return new
        for x in range(self.__position[1]):
            new += "\n"
        for x in range(self.__size - 1):
            new += " " * self.__position[0] + "#" * self.__size + "\n"
        new += " " * self.position[0] + "#" * self.__size
        return new
