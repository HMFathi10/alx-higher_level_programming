#!/usr/bin/python3
""" Module that contains a function that creates an Object from a JSON File """
import json


def load_from_json_file(filename):
    """ unction that creates an Object from a “JSON file”

    Args:
        filename: text file name
    """
    with open(filename, 'r', encoding='utf-8') as myFile:
        return json.load(myFile)
