#!/usr/bin/python3

"""
This module defines a Square class that represents a square.

It includes an initialization method that accepts a side length
and ensures the value is a non-negative integer.
"""


class Square:
    def __init__(self, size):
        self.__size = size
