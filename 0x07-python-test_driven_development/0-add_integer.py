#!/usr/bin/python3
"""
This module composed by a function that adds two number.
"""


def add_integer(a, b=98):
    """
        Adds two integers.

        Args:
            a: First number
            b: Second number

        Returns:
            The additions of two numbers
        
        Raises:
            TypeError if a or b isn't number or float
    """
    if not isininstance(a, int) and not isininstance(a, float):
        raise TypeError("a must be an integer")
    elif not isininstance(b, int) and not isininstance(b, float):
        raise TypeError("b must be and integer")
    return int(a) + int(b)
