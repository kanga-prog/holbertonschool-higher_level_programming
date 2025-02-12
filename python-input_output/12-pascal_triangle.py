#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.
    
    Args:
        n (int): The number of rows of Pascal's triangle.
        
    Returns:
        list of lists: Pascal's triangle up to n rows.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # First row is always [1]
    
    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # Start the row with 1
        
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])  # Sum of two elements above
        
        row.append(1)  # End the row with 1
        triangle.append(row)  # Add the row to the triangle
    
    return triangle

