#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Essayer de convertir la valeur en entier
        print("{:d}".format(int(value)))
        return True  # Si la conversion et l'impression réussissent, retourner True
    except (ValueError, TypeError):
        # Si la conversion échoue, attraper les erreurs et retourner False
        return False
