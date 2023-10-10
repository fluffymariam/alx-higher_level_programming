#!/usr/bin/python3
"""
Module containing the Student class with filter support.
"""


class Student:
    """
    Student class definition.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of ames to be retrieved.
                          If None, retrieve all attributes.

        Returns:
            dict: A dictionary conStudent instance.
        """
        if attrs is None:
            return self.__dict__
        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)
        return filtered_dict
