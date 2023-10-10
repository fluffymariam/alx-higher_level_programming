#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves it to a JSON file
"""


import sys
import json
from os.path import exists

def save_to_json_file(my_list, filename):
    with open(filename, 'w') as json_file:
        json.dump(my_list, json_file)

def load_from_json_file(filename):
    if exists(filename):
        with open(filename, 'r') as json_file:
            return json.load(json_file)
    return []

if __name__ == "__main__":
    filename = "add_item.json"
    my_list = load_from_json_file(filename)

    # Add command-line arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(my_list, filename)
