#!/usr/bin/python3

""" un rectangle """

class Rectangle:

    """
    Classe représentant un rectangle avec des attributs width et height.
    Permet de calculer l'aire et le périmètre du rectangle, ainsi\
            que d'afficher
    une représentation visuelle du rectangle avec des symboles.
    """

    def __init__(self, width=0, height=0):
        """
        Initialise une instance de la classe Rectangle.

        Args:
            width (int): La largeur du rectangle. Défaut à 0.
            height (int): La hauteur du rectangle. Défaut à 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Récupère la largeur du rectangle.

        Returns:
            int: La largeur du rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Définit la largeur du rectangle. Vérifie que la\
                valeur est un entier et est >= 0.

        Args:
            value (int): La valeur de la largeur à définir.

        Raises:
            TypeError: Si la largeur n'est pas un entier.
            ValueError: Si la largeur est inférieure à 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Récupère la hauteur du rectangle.

        Returns:
            int: La hauteur du rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Définit la hauteur du rectangle. Vérifie que la valeur\
                est un entier et est >= 0.

        Args:
            value (int): La valeur de la hauteur à définir.

        Raises:
            TypeError: Si la hauteur n'est pas un entier.
            ValueError: Si la hauteur est inférieure à 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            int: L'aire du rectangle (width * height).
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            int: Le périmètre du rectangle. Si la largeur ou la hauteur
                 est égale à 0, retourne 0.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne du rectangle
        avec le caractère '#' utilisé pour afficher le rectangle.

        Returns:
            str: La représentation visuelle du rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join([ "#" * self._width ] * self._height)

    def __repr__(self):
        """
        Retourne une représentation sous forme de chaîne du rectangle
        permettant de recréer une instance du rectangle en utilisant eval().

        Returns:
            str: La chaîne de caractères permettant de recréer l'instance.
        """
        return "<3-Rectangle.{} object at {:#x}>"\
            .format(self.__class__.__name__, id(self))
