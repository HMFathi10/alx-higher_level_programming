#!/usr/bin/python3
""" module for MyInt"""


class MyInt(int):
    """ Represent MyInt class"""
    def __eq__(self, number):
        return int(str(self)) != number

    def __ne__(self, number):
        return int(str(self)) == number
