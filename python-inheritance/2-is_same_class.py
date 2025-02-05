#!/usr/bin/python3

"""
Ce module contient une fonction `is_same_class` qui permet de vérifier si un objet
est exactement une instance d'une classe donnée.

La fonction compare l'objet avec la classe spécifiée et retourne `True` si l'objet
est une instance directe de cette classe, sans tenir compte des sous-classes.

Cette fonctionnalité est utile lorsque vous avez besoin de savoir si un objet
appartient à une classe particulière et non à une sous-classe.

La fonction ne prend pas en compte l'héritage, elle vérifie uniquement l'appartenance
directe à la classe.

Exemple d'utilisation :

    >>> is_same_class(1, int)
    True
    >>> is_same_class(1, float)
    False
    >>> is_same_class("hello", str)
    True
"""

def is_same_class(obj, a_class):
    """
    Vérifie si un objet est exactement une instance d'une classe spécifiée.

    Arguments:
        obj: L'objet à vérifier.
        a_class: La classe à comparer avec l'objet.

    Retourne:
        True si l'objet est une instance de la classe spécifiée,
        False sinon.

    Exemple:
        >>> is_same_class(1, int)
        True
        >>> is_same_class(1, float)
        False
        >>> is_same_class("hello", str)
        True
    """
    if obj.__class__ is a_class:
        return True
    else:
        return False
