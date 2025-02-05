#!/usr/bin/python3
"""
Module 8-rectangle

This module defines a class `Rectangle` that represents a rectangle. 
The class allows the creation of rectangles with specified width and height.
It includes validation to ensure that both width and height are positive integers.
"""


class Rectangle:
    """
    A class that represents a rectangle.

    Attributes:
    -----------
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

    Methods:
    --------
    __init__(self, width, height):
        Initializes the rectangle with width and height.
        
    __str__(self):
        Returns a string representation of the rectangle in the format:
        "Rectangle(width, height)"
    
    Exceptions:
    -----------
    TypeError: Raised if width or height is not an integer.
    ValueError: Raised if width or height is less than or equal to 0.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height.

        Parameters:
        -----------
        width (int): The width of the rectangle. Must be a positive integer.
        height (int): The height of the rectangle. Must be a positive integer.

        Raises:
        -------
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than or equal to 0.
        """
        # Validation for width
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        
        # Validation for height
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.width = width
        self.height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        --------
        str: A string in the format "Rectangle(width, height)".
        """
        return "Rectangle({}, {})".format(self.width, self.height)
