#!/usr/bin/python3
"""
    Module that creates a square class that inherits from Rectangle
"""

# Import Rectangle from 9-rectangle.py (assumed)
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that defines a square, inheriting from Rectangle.

    A square is a specific type of rectangle where width and height are equal.
    This class validates the size of the square and calculates the area.

    Attributes:
        size (int): The size of the square (equal width and height).

    Methods:
        area(): Returns the area of the square (size * size).
        __str__(): Returns a string representation of the square in the
                   format '[Square] <size>/<size>'.
    """

    def __init__(self, size):
        """
        Initializes the Square object with size.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If the size is not a positive integer.
        """
        # Validate the size using the integer_validator from Rectangle
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # Initialize the parent class (Rectangle)

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
