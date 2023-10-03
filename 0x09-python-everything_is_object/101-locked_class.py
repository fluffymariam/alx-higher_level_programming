#!/usr/bin/env python3
"""
This module defines the LockedClass class.
"""


class LockedClass:
    """
    A class that prevecreating new instance attributes,
    except if the new instance attribute is called first_name.
    """
    __slots__ = ['first_name']
