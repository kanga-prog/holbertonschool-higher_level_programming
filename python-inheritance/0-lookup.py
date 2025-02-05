#!/usr/bin/python3

"""
Module lookup
--------------

This module contains a function `lookup` that returns a list of the
available attributes and methods of the provided object using the
built-in `dir()` function.
"""


def lookup(obj):

    """
    This function returns a list of available attributes \
        and methods of the given object.
    It uses the built-in dir() function to gather and\
          return all the attributes and
    methods that belong to the object, including special\
          methods like __init__ and __str__.
    Args:
        obj (object): The object whose attributes and\
              methods are to be retrieved.
    Returns:
        list: A list of strings representing the attributes\
            and methods of the object.
    """
    return dir(obj)
