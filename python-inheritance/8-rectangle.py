#!/usr/bin/python3

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
    
    area(self):
        Calculates the area of the rectangle.
    
    integer_validator(self, name, value):
        Validates the value to ensure it is a positive integer.

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
            raise TypeError("height must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        
        # Validation for height
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def integer_validator(self, name, value):
        """Validates if value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
