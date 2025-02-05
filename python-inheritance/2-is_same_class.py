"""
Ce module traite d'une fonction qui verifie si un objet appartient\
      a une class et renvoie true si c'est vrais et faux si c'est faux
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        True if the object is an instance of the specified class, 
        False otherwise.

    Example:
        >>> is_same_class(1, int)
        True
        >>> is_same_class(1, float)
        False
        >>> is_same_class("hello", str)
        True
    """
    if type(obj) == a_class:
        return True
    else:
        return False
