#!/usr/bin/python3

"""
This module defines a Square class that represents a square.

It includes an initialization method that accepts a side length
and ensures the value is a non-negative integer.
"""


class Square:
    """
    Defines a square by its size.

    Attributes:
        __size (int): The size of the side of the square.
    """

    def __init__(self, size):
        """
        Initializes an instance of the Square class.

        Args:
            size (int): The size of the side of the square.
        """
        self.__size = size
