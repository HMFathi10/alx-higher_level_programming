#!/usr/bin/python3
"""class MyList that inherits from list
"""


class MyList(list):
    """inherits from list"""
    def __init__(self):
        list.__init__()

    def print_sorted(self):
        """prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
