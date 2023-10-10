#!/usr/bin/python3
"""
ass with serialization and deserialization methods.
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
            attrs (list): A list oing attribute names to be retrieved.
                          If None, retrieve all attributes.

        Returns:
            dict: A dictionary conibutes of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)
        return filtered_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of m a dictionary.

        Args:
            json (dict): A dictionays and their values.

        """
        for key, value in json.items():
            setattr(self, key, value)
