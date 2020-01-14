#!/usr/bin/python3
"""How many instances"""


class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation  of a rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        if not isinstance(self.print_symbol, str):
            self.print_symbol = str(self.print_symbol)
        newone = ""
        for width in range(self.__height - 1):
            newone += (self.print_symbol * self.__width) + '\n'
        newone += (self.print_symbol * self.__width)
        return newone

    def __repr__(self):
        """define repr"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """define delete"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
