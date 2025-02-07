#!/usr/bin/python3

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class that defines the blueprint for shape objects.

    Subclasses must implement the `area` and `perimeter` methods to calculate
    the area and perimeter of the shape.

    Methods:
        area(): Abstract method to compute the area of the shape.
        perimeter(): Abstract method to compute the perimeter of the shape.
    """
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Class representing a circle, derived from the Shape abstract class.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        area(): Calculates the area of the circle.
        perimeter(): Calculates the perimeter (circumference) of the circle.
    """
    def __init__(self, radius):
        """
        Initialize the Circle with the given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class representing a rectangle, derived from the Shape abstract class.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Methods:
        area(): Calculates the area of the rectangle.
        perimeter(): Calculates the perimeter of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize the Rectangle with the given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a given shape.

    This function demonstrates the use of duck \
        typing. It does not explicitly check
    the type of the object passed but assumes \
        the object has `area` and `perimeter`
    methods, which it calls to display the area and perimeter.

    Args:
        shape (Shape): An object of a class that \
            inherits from the Shape abstract class.

    Raises:
        AttributeError: If the object does not have the\
              `area` or `perimeter` methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
