#!/usr/bin/python3
""" module subclass square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""
    def __init__(self, size):
        """"
        Init function for Square

        Attributes:
            size (int): The size of the square
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ return area """
        return self.__size ** 2
    def __str__(self):
        """
        str funtion to print with/height

        Returns:
            Return width/height
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
