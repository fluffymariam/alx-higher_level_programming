#!/usr/bin/python3
"""
Module for writing a string to a text file (UTF8).
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text he number of characters written.

    Args:
        filename (str): The name of the file to be written.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written.

    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
