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
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be and integer")
    a = int(a)
    b = int(b)
    return a + b
