#!/usr/bin/python3
"""
Module containing the append_after function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text toine containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The specific string to search for in each line.
        new_string (str): Thes containing the search string.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)


if __name__ == "__main__":
    filename = "append_after_100.txt"
    search_string = "Python"
    new_string = "\"C is fun!\"\n"
    append_after(filename, search_string, new_string)
