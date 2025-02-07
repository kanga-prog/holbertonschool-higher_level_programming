#!/usr/bin/python3

"""
Ce module contient une classe `MyList` qui hérite de la classe intégrée `list`.

La classe `MyList` ajoute une méthode permettant d'afficher la liste triée
sans modifier l'ordre des éléments dans la liste d'origine.

Cette fonctionnalité est utile lorsqu'on veut afficher une version triée de la
liste sans affecter la liste originale.
"""


class MyList(list):
    """
    Une classe qui hérite de la classe intégrée `list`.
    Cette classe fournit une méthode `print_sorted` qui permet d'afficher la
    liste triée sans modifier la liste d'origine. La méthode utilise la
    fonction `sorted()` pour obtenir une version triée de la liste.
    """

    def print_sorted(self):
        """
        Affiche la liste dans un ordre croissant sans modifier\
              la liste d'origine.
        La méthode utilise la fonction `sorted()` pour retourner une nouvelle
        liste triée. L'ordre de la liste originale reste inchangé.
        Exemple:
            >>> my_list = MyList([3, 1, 4, 5, 2])
            >>> my_list.print_sorted()
            [1, 2, 3, 4, 5]
            >>> print(my_list)
            [3, 1, 4, 5, 2]
        """
        print(sorted(self))
