#!/usr/bin/python3
"""
Simple rectangle module.

Provides a Rectangle class that stores width and height and can
compute its area and perimeter with full validation.
"""


class Rectangle:
    """Represent a 2‑D rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # ---- width property -------------------------------------------------
    @property
    def width(self):
        """Width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # ---- height property ------------------------------------------------
    @property
    def height(self):
        """Height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # ---- public methods -------------------------------------------------
    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter.  
        If either dimension is zero, the perimeter is zero.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
