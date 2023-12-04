#!/usr/bin/python3
"""
module only sub class of
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
       that inherited (directly or indirectly) from the specified class;
       otherwise False.
       """
    return type(obj) != a_class and issubclass(obj.__class__, a_class)
