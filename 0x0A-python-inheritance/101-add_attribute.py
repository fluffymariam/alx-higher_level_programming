#!/usr/bin/python3
"""
Defines a function add_attribute.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.
    Raises a TypeError exception if the object can't have new attribute.

    Args:
        obj: The object to which the new attribute should be added.
        attribute: The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object can't have new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
