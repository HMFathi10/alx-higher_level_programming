#!/usr/bin/python3
"""
This module composed by a function that prints the square.
"""


def print_square(size):
    """
        Print the square

        Args:
            size: the square size
        
        Raises:
            TypeError: If size is not integer
                If size is float and less than zero
            ValueError: If size in less than zero
    """

    if type(size) is float and int(size) < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        print("#" * size)
