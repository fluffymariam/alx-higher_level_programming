#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.
"""


import sys
import os.path


# Importing custom functions
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# File name for saving the list
filename = "add_item.json"

# Initialize an empty list if the file doesn't exist
if not os.path.exists(filename):
    save_to_json_file([], filename)

# Load the existing list from the file
my_list = load_from_json_file(filename)

# Add command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
