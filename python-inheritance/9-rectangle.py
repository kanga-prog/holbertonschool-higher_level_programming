#!/usr/bin/python3

# Import BaseGeometry from 7-base_geometry.py
BaseGeometry = __import__('8-rectangle').Rectangle

class Rectangle(BaseGeometry):
    """
    A Rectangle class that inherits from BaseGeometry.

    This class defines a rectangle with a specified width and height. It 
    validates the width and height using the integer_validator method from 
    the BaseGeometry class. It includes methods to calculate the area of the 
    rectangle and return a string representation of the rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        area(): Returns the area of the rectangle (width * height).
        __str__(): Returns a string representation of the rectangle in the 
                   format '[Rectangle] <width>/<height>'.
        __repr__(): Returns the official string representation of the 
                    rectangle (same as __str__ for debugging).
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle object with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            ValueError: If the width or height is not a positive integer.
        """
        # Validate the width and height with the integer_validator from BaseGeometry
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle in the format '[Rectangle] <width>/<height>'.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """
        Returns the official string representation of the rectangle.

        This method is mainly used for debugging and is identical to __str__.

        Returns:
            str: The official string representation of the rectangle.
        """
        return self.__str__()
