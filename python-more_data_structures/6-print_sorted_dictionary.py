#!/usr/bin/python3


def kanga(a_dictionary):
    # Retourne les clés triées du dictionnaire
    return sorted(a_dictionary.keys())


def print_sorted_dictionary(a_dictionary):
    # Obtenez les clés triées via la fonction kanga
    sorted_keys = kanga(a_dictionary)

    # Afficher chaque clé et sa valeur
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
