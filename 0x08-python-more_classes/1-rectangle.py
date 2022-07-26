#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """ Real definition of a triangle """

    def __init__(self, width = 0, height = 0):
        """ initializes a triangle with private attributes 
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__vwidth = value

    @property
    def height(self):
        """Get/Set the height of the triangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
