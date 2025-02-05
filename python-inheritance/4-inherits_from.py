#!/usr/bin/python3
""""
ce module traitre de l'apartenance d'un objet a une class ou une sous class

"""

def inherits_from(obj, a_class):
    """
    Function to check if an object is an instance of a class that inherited 
    (directly or indirectly) from the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is an instance of a class that inherited from 
              a_class (directly or indirectly), otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
