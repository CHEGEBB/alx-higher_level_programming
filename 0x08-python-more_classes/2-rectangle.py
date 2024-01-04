#!/usr/bin/python3
''''Defines a Rectangle class.'''


class Rectangle:
    '''class rectangle'''
    def __init__(self, width=0, height=0):
        '''private instance attribute width and height'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''getter for width to retrieve width'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getter for width to retrieve width'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Return the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Return the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * self.__width + 2 * self.__height)
