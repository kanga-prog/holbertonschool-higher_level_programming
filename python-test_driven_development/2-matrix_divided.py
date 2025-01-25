#!/usr/bin/python3

def matrix_divided(matrix, div):
    # Validate matrix: check if it's a list of lists
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")
    # Validate rows: check if each row has the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # Validate divisor: it should be a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Validate divisor: check if divisor is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Create the new matrix with elements divided by div
    new_matrix = []
    for row in matrix:
        new_matrix.append([round(element / div, 2) for element in row])
    return new_matrix
