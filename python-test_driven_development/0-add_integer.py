#!/usr/bin/python3

def add_integer(a, b=98):
    """Returns the sum of two integers, a and b.
    If a or b are floats, they will be cast to integers.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    # Vérification des types de a et b
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    # Cast des valeurs a et b en entiers
    a = int(a)
    b = int(b)
    return a + b
