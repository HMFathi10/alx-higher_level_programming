#!/usr/bin/python3
""" Module that contains a function that writes to a file """


def append_write(filename="", text=""):
    """ Append Write File function

    Args:
        filename: file name
        text: text

        Raises
            Exception: when the file can not be opend
    """

    with open(filename, "a", encoding="utf-8") as myFile:
        data = myFile.write(text)
        return len(text)
