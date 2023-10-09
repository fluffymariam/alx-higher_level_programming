#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square object, inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a square instance.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
