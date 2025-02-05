#!/usr/bin/python3

class BaseGeometry:
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)  # Validate the width
        self.integer_validator("height", height)  # Validate the height
        self.__width = width  # Private width attribute
        self.__height = height  # Private height attribute

    def __str__(self):
        return f"[Rectangle] {self.__width} - {self.__height}"
    
    # Optional: You can add area method or other methods here if needed.
