#!/usr/bin/python3
"""Defines a class MyInt that inherits from int and inveoperators."""


class MyInt(int):
    """
    Represents a custom integer that inverts == and != operators.
    """

    def __eq__(self, other):
        """
        Overrides the == operator.
        Args:
            other: The object to compare with.

        Returns:
            bool: True if self and other are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator.
        Args:
            other: The object to compare with.

        Returns:
            bool: True if self and other are equal, False otherwise.
        """
        return super().__eq__(other)
