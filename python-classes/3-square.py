#!/usr/bin/python3

"""Module for defining the Square class.

This module defines a Square class with a private instance attribute
`size`, a method `area()` to compute its area, and input validation to
ensure that the `size` is an integer greater than or equal to 0.
"""

class Square:
    """Represents a square with a given size.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes the square with a given size.
        area(self): Returns the area of the square.
    """

    def __init__(self, size=0):
        """Initializes the square with a given size.

        Args:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

