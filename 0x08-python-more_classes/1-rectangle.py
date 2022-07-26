#!/usr/bin/python3
class Rectangle:
    """ Real definition of a triangle """
    def __init__(self, width = 0, height = 0):
        """ initializes a triangle with private attributes """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            self.__width = int(value)
        except TypeError:
            print("width must be an integer")
        except ValueError:
            print("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            self.__height = int(value)
        except TypeError:
            print("height must be an integer")
        except ValueError:
            print("height must be >= 0")
