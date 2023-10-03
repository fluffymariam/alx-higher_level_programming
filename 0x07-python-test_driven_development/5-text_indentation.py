#!/usr/bin/python3

"""
Prints a ts after each of these characters: ., ? and :.
"""

def text_indentation(text):
    """
    Prints r each of these characters: ., ? and :.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    chars = [".", "?", ":"]
    for char in text:
        print(char, end="")
        if char in chars:
            print("\n")

