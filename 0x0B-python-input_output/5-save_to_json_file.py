#!/usr/bin/python3
"""
Module for saving an object to a text file using JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be saved to the file.
        filename (str): The name of the file where the object will be saved.

    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
