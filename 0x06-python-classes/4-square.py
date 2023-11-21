#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """Initialize square

        Args:
            size(int): size of the square (optional)

        """
        self.__size = size

    @property
    def size(self):
        """ return the size

        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size

        Args:
            value(int): new size value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value  #: size of the square

    def area(self):
        """returns the area

        Returns:
            area
        """
        return self.__size**2
