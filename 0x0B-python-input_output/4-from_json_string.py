#!/usr/bin/python3
""" Module that contains a function that returns an object representation """
import json
from io import StringIO


def from_json_string(my_str):
    """ Convert string to json object

    Args:
        my_str: string
    """
    return (json.loads(my_str))
