#!/usr/bin/python3
"""
Defines a function that checks if an obed class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of or inherits from a_class.
    Args:
        obj: The object to check.
        a_class: The specified class.
    Returns:
        True if obj is an instanc
    """
    return isinstance(obj, a_class)
