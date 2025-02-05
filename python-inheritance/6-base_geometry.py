#!/usr/bin/python3

"""
Ce module
"""


class BaseGeometry:
    """
    A base class for geometric shapes.

    This class defines the method area() which should be implemented
    by any subclass. It raises an Exception if called directly.
    """
    def area(self):
        """
        Raises an exception indicating that the method is not implemented.

        This method should be implemented by a subclass that inherits from
        BaseGeometry to provide specific functionality for calculating area.
        """
        raise Exception("area() is not implemented")
