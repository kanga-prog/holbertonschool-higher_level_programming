#!/usr/bin/python3


"""
Module qui contient la fonction add_integer.
Cette fonction additionne deux nombres entiers et retourne le résultat.
Si les entrées sont des flottants, elles sont converties en entiers.
Si une entrée n'est pas un entier ou un flottant, une exception est levée.
"""


def add_integer(a, b=98):
    """
    Returns the sum of two integers, a and b. If a or b are floats,
    they will be cast to integers.

    Args:
        a: Premier nombre, peut être un entier ou un flottant.
        b: Deuxième nombre, par défaut 98, peut être un entier ou un flottant.

    Returns:
        La somme des deux nombres sous forme d'entier.

    Raises:
        TypeError: Si a ou b ne sont pas des entiers ou des flottants.
    """

    # Vérification des types de a et b
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    # Conversion en entiers si les entrées sont des flottants
    a = int(a)
    b = int(b)
    return a + b
