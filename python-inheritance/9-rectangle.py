#!/usr/bin/python3

# Import BaseGeometry from 7-base_geometry.py
BaseGeometry = __import__('8-rectangle').Rectangle

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        # Validate the width and height with the integer_validator from BaseGeometry
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        # Return the area of the rectangle
        return self.__width * self.__height

    def __str__(self):
        # Return the string representation of the rectangle
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        # Return the official string representation of the rectangle (for debugging)
        return self.__str__()

