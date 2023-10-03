#!/usr/bin/python3
"""
Prints the name in the format: My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format: My name is <first name> <last name>

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name. Defaults to "".
    
    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
