#!/usr/bin/python3
""" Class Rectangle that defines a rectangle
"""


class Rectangle:
    """ Class Rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Return rectangle perimeter """
        if self.__width is 0 or self.__height is 0:
            return 0
        return ((self.__width + self.__height) * 2)
