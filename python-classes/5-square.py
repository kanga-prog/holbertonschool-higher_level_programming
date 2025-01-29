#!/usr/bin/python3

""" ce module defini les caracteritique d'un carre
"""


class Square:
    """
    Cette classe définit un carré par la taille de son côté.

    Attributes:
        __size (int): La taille du côté du carré\
                (doit être un entier supérieur ou égal à 0).
    """

    def __init__(self, size=0):
        """
        Initialise une instance de la classe Square avec une taille donnée.

        Args:
            size (int): La taille du côté du carré. Par défaut, c'est 0.
        """
        self.size = size  # Utilisation du setter pour initialiser 'size'

    @property
    def size(self):
        """
        Récupère la taille du côté du carré.

        Returns:
            int: La taille du côté du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la taille du côté du carré.

        Args:
            value (int): La taille du côté du carré.

        Raises:
            TypeError: Si la taille n'est pas un entier.
            ValueError: Si la taille est inférieure à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: L'aire du carré, qui est la taille du côté au carré.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Affiche le carré en utilisant le caractère '#' dans stdout.

        Si la taille est 0, affiche une ligne vide.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
