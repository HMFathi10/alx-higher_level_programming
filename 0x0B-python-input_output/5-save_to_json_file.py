#!/usr/bin/python3
""" Module that contains a function that writes an Object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """  Writes an Object to a text file

    Args:
        my_obj: object
        filename: text file name
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        json.dump(my_obj, myFile)
