#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Crée une nouvelle matrice avec les carrés des éléments
    new_matrix = []
    for row in matrix:
        new_matrix.append([element ** 2 for element in row])
    return new_matrix
