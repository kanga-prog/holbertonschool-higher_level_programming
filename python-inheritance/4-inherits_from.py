#!/usr/bin/python3
"""
Module de verification d'appartenance d'objet a class ou sous class.

"""


def inherits_from(obj, a_class):
    """
    Function to check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object's class is a subclass of a_class, and not
              the class itself; otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
