#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Instantiate arg:size."""
    def __init__(self, size =0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
