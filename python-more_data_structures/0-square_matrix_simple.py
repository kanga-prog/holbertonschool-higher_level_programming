#!/usr/bin/python3

# Définition d'une fonction pour calculer le carré
def carre(x):
    return x**2

def square_matrix_simple(matrix=[]):
    # Utilisation de la fonction 'carre' à la place de 'lambda'
    new_matrix = [list(map(carre, row)) for row in matrix]
    return new_matrix
