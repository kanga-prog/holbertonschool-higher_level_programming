#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Créer une copie de la matrice pour éviter de modifier l'originale
    new_matrix = [list(map(lambda x: x**2, row)) for row in matrix]
    return new_matrix
