#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number = -number  # Prendre la valeur absolue pour gérer les négatifs
    last_digit = number % 10  # Extraire le dernier chiffre
    print(last_digit, end="")  # Affiche le dernier chiffre sans nouvelle ligne
    return last_digit  # Retourne la valeur du dernier chiffre
