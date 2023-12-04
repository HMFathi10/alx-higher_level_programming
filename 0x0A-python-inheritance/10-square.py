#!/usr/bin/python3
""" module subclass square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ return area """
        return self.__size ** 2