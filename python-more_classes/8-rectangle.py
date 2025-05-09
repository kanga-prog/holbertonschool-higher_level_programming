#!/usr/bin/python3

"""
ce module traite d'un rectangle que nous \
allons manipuler avec certains fonctions en python
"""


class Rectangle:

    """
    Classe représentant un rectangle avec des attributs\
            privés width et height.
    Permet de calculer l'aire et le périmètre du rectangle,\
            ainsi que d'afficher
    une représentation visuelle du rectangle avec un symbole\
            personnalisable.
    Lors de la suppression d'une instance, un message de\
            confirmation est affiché.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise une instance de la classe Rectangle.

        Args:
            width (int): La largeur du rectangle. Défaut à 0.
            height (int): La hauteur du rectangle. Défaut à 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        Définit la largeur du rectangle. Vérifie que\
                la valeur est un entier et est >= 0.

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
        Définit la hauteur du rectangle. Vérifie que la\
                valeur est un entier et est >= 0.

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
        avec le caractère ou la chaîne stockée dans print_symbol.
        Si la largeur ou la hauteur est égale à 0, retourne une chaîne vide.

        Returns:
            str: La représentation visuelle du rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self._width] * self._height)

    def __repr__(self):
        """
        Retourne une représentation sous forme de chaîne du rectangle
        permettant de recréer une instance du rectangle en utilisant eval().

        Returns:
            str: La chaîne de caractères permettant de recréer l'instance.
        """
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """
        Méthode appelée lors de la suppression d'une instance de Rectangle.
        Affiche un message de suppression de l'instance.

        Returns:
            None
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare deux rectangles et retourne le plus grand ou celui ayant
        la même aire.

        Args:
            rect_1 (Rectangle): Le premier rectangle à comparer.
            rect_2 (Rectangle): Le deuxième rectangle à comparer.

        Returns:
            Rectangle: Le rectangle ayant l'aire la plus grande ou égale.
        Raises:
            TypeError: Si l'un des arguments n'est pas une instance de\
                    Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
