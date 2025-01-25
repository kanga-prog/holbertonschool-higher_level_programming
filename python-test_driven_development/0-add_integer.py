#!/usr/bin/python3

def add_integer(a, b=98):


    """
    Returns the sum of two integers, a and b. If a or b are floats,
    they will be cast to integers.

    Args:
        a: First number, can be an integer or a float.
        b: Second number, default 98, can be an integer or a float.

    Returns:
        The sum of the two numbers as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
        OverflowError: If a or b are too large for a float.
    """
    # Vérification des types
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    # Vérification de l'overflow des floats
    if abs(a) > float('inf') or abs(b) > float('inf'):
        raise OverflowError("a or b is too large to be processed as a float")
    # Conversion en entiers
    a = int(a)
    b = int(b)
    return a + b
