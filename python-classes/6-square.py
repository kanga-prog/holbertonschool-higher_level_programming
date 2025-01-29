#!/usr/bin/python3

""" ce mode decrit les carasteristique d'un carré """


class Square:
    """
    Cette classe définit un carré par la taille de son côté et sa position.
    Attributes:
        __size (int): La taille du côté du carré\
                (doit être un entier supérieur ou égal à 0).
        __position (tuple): Position du carré dans\
                la console (doit être un tuple de 2 entiers positifs).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise une instance de la classe Square\
                avec une taille et une position données.

        Args:
            size (int): La taille du côté du carré. Par défaut, c'est 0.
            position (tuple): La position du carré dans\
                    la console, donnée sous forme de tuple (x, y).
                              Par défaut, c'est (0, 0).
        """
        self.size = size  # Utilisation du setter pour initialiser 'size'
        self.position = position

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

    @property
    def position(self):
        """
        Récupère la position du carré dans la console.

        Returns:
            tuple: Un tuple (x, y) représentant la position du carré.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Définit la position du carré.

        Args:
            value (tuple): Un tuple (x, y) représentant\
                    la position du carré dans la console.

        Raises:
            TypeError: Si 'value' n'est pas un tuple de 2 entiers positifs.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: L'aire du carré, qui est la taille du côté au carré.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Affiche le carré en utilisant le caractère\
                '#' dans stdout avec la position spécifiée.

        Si la taille est 0, affiche une ligne vide.

        Si position[1] > 0, les lignes de carrés\
                sont précédées de position[1] espaces.
        Si position[0] > 0, chaque ligne commence\
                avec position[0] espaces avant les '#'.
        """
        if self.__size == 0:
            print("")
        else:
            for y in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
