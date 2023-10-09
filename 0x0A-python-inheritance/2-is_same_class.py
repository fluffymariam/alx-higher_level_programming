#!/usr/bin/python3
"""
Defines a function that checks if an object is an instance class.
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is an instance of a_class.
    Args:
        obj: The object to check.
        a_class: The specified class.
    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
