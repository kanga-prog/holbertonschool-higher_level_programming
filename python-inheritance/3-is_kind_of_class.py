#!/usr/bin/python3
"""
Ce module traite d'une fonction qui verifie l'existance\
      d'un objet dans une classe et sa souclass
"""


def is_kind_of_class(obj, a_class):
    """
    Function to check if an object is an instance of, or if it is an instance
    of a class that inherited from, the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is an instance of a_class or an instance of
              a subclass of a_class; otherwise, False.
    """
    return isinstance(obj, a_class)
