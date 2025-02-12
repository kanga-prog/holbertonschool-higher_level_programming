#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student instance.

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

        Args:    attrs (list): A list of attributes to retrieve.
        Returns:
            dict: A dictionary with the student attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
