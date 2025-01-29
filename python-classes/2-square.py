#!/usr/bin/python3

"""
This module defines a Square class that represents a square.

It includes an initialization method that accepts a side length
and ensures the value is a non-negative integer.
"""


class Square:

    """
    Représente un carré.

    Attributes:
        size (int): La taille du côté du carré\
             (doit être un entier supérieur ou égal à 0).

    Methods:
        __init__(self, size=0): Initialise un carré avec une taille donnée.
    """

    def __init__(self, size=0):
        """
        Initialise une instance de la classe Square.

        Args:
            size (int): La taille du côté du carré.\
                 Doit être un entier et supérieur ou égal à 0.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
