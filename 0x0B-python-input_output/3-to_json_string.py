#!/usr/bin/python3
""" Module that contains a function that returns the JSON representation """
import json
from io import StringIO

def to_json_string(my_obj):
    """ Convert object to string

    Args:
        my_obj: object
    """
    io = StringIO()
    json.dump(my_obj, io)
    return (io.getvalue())
