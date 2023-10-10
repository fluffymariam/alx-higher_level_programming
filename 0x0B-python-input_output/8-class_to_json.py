#!/usr/bin/python3
"""
Module for converting a Class object to a JSON dictionary representation.
"""


def class_to_json(obj):
    """
    Returns the dictionary descriperialization of an object.

    Args:
        obj: An instance of a Class object.

    Returns:
        dict: The dictionary repre attributes.

    """
    return obj.__dict__
