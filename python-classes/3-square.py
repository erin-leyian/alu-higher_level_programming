#!/usr/bin/python3
"""Module that defines a Square class (task 3-square.py)."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int, optional): Length of a side of the square.
                Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
