#!/usr/bin/python3
"""
Definesf a subclass
that in from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a subclass inherited from a_class.
    Args:
        obj: The object to check.
        a_class: The specified class.
    Returns:
        True if obj is an instance of a subclass inherited from a_class,
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
