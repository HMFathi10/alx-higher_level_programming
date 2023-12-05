#!/usr/bin/python3
""" Module that contains a function that reads from a file """


def read_file(filename=""):
    """ Read File function

    Args:
        filename: file name

        Raises
            Exception: when the file can not be opend
    """

    with open(filename, "r", encoding="utf-8") as myFile:
        data = myFile.read()
        print(data, end='')
