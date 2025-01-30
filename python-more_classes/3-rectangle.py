#!/usr/bin/python3

class Rectangle:

    """
    A class to represent a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
        __str__(): Returns a string representation of the rectangle.
        __repr__(): Returns a string with a representation of the object.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width attribute."""
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute.

        Args:
            value (int): The value to set the width.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self._height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute.

        Args:
            value (int): The value to set the height.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if either
                 width or height is 0.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'.

        Returns:
            str: A string representing the rectangle, or an empty
                 string if either width or height is 0.
        """
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join(["#" * self._width] * self._height)

    def __repr__(self):
        """
        Returns a string with a representation of the object.

        Returns:
            str: A string representing the object with its memory address.
        """
        return f"<{self.__class__.__name__} object at {hex(id(self))}>"
