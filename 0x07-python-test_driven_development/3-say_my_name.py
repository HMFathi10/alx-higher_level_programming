#!/usr/bin/python3
"""
This module composed by a function that prints the name.
"""


def say_my_name(first_name, last_name=""):
    """
        Print the name

        Args:
            first_name: the first name
            last_name: the last name
        
        Raises:
             TypeError: If the first name not string
             If the first name is None
             If the last name not string
             If the last name is None
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
