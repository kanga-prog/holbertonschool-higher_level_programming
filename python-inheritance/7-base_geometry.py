#!/usr/bin/python3
"""
Module

"""


class BaseGeometry:
    """
    A class representing basic geometry.

    This class provides methods for validating integers\
          and raising an exception
    for the `area()` method, which is not implemented in the base class.
    """
    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.

        This method is meant to be overridden in subclasses, as the calculation
        of the area depends on the specific geometry.
        Raises:
            Exception: Always raises an exception stating\
                  that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is a positive integer.

        Args:
            name (str): The name of the variable being validated.
            value (int): The value to be validated.
        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        The method checks if the value is an integer and \
            if it is greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
