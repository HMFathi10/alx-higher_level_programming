#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square

        Args:
            size (int): size of the square (optional)
            position (int, int): the position of the new #

        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ return the position

        Returns:
            postion
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the area

        Returns:
            area
        """
        return self.__size**2

    def my_print(self):
        """ Print the square"""

        if not self.__size:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for sp in range(0, self.__position[0])]
            [print("#", end="") for ch in range(0, self.__size)]
            print("")
