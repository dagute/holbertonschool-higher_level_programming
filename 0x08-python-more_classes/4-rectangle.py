#!/usr/bin/python3
"""String representation"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation  of a rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return(self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """String representation"""
        if self.__width == 0 or self.__height == 0:
            return newone
        newone = ""
        for width in range(self.__height - 1):
            newone += ("#" * self.__width) + '\n'
        newone += ("#" * self.__width)
        return newone

    def __repr__(self):
        """defining repr"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
