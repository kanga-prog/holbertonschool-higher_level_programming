#!/usr/bin/python3
"""
    Module that creates a square
"""

Rectangle = __import__('10-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that defines a square, inheriting from Rectangle.

    A square is a specific type of rectangle where width and height are equal.
    This class validates the size of the square and calculates the area.

    Attributes:
        size (int): The size of the square (equal width and height).
    """

    def __init__(self, size):
        """
        Initializes the Square object with size.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If the size is not a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Rectangle] {self.__size}/{self.__size}"
