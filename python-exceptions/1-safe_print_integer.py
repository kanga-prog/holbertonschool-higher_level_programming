#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Essayer de convertir la valeur en entier
        print("{:d}".format(int(value)))
        return True
    except (ValueError, TypeError):
        return False
