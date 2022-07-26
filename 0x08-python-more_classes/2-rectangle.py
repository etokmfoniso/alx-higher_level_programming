#!/usr/bin/python3
"""Class to define the Area and Perimeter of a rectangle"""

class Rectangle:
    """ Define instances of a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle object
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private setting/getting the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set/get the height"""
        return self.__height

    @width.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of a rectangle"""
        return (self.width) * (self.height)

    def perimeter(self):
        """returns the perimeter of a rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2(self.width + self.height)
