#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Vérifier si la clé existe déjà dans le dictionnaire
    if key in a_dictionary:
        # Si la clé existe, remplacer la valeur
        a_dictionary[key] = value
    else:
        # Si la clé n'existe pas, ajouter la nouvelle clé avec sa valeur
        a_dictionary.update({key: value})
    return a_dictionary
