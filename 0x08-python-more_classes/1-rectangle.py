#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """This class defines a rectangle with width and height attributes."""
    
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.
        
        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter method to retrieve the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width attribute.
        
        Args:
            value (int): The value to set as the width.
        
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height attribute.
        
        Args:
            value (int): The value to set as the height.
        
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

