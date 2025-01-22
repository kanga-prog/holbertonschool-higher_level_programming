#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Vérifie si la clé existe dans le dictionnaire
    if key in a_dictionary:
        # Si elle existe, la supprimer
        del a_dictionary[key]
    # Retourne le dictionnaire (qu'il ait été modifié ou non)
    return a_dictionary
