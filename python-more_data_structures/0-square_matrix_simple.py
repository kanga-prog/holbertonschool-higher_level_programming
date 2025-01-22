#!/usr/bin/python3

# Définition d'une fonction pour calculer le carré
def kanga(x):
    return x**2


def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(kanga, row)) for row in matrix]
    return new_matrix
