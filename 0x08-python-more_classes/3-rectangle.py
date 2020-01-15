#!/usr/bin/python3
class Rectangle:
    """
    creating class Rectangle
    """
    def __init__(self, height=0, width=0):
        """
        using it sefl
        args:
        height: the height of the rectangle
        width: the width of the rectangle
        """
        self.__height = height
        self.__width = width

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        P = (self.__width * 2) + (self.__height * 2)
        return P
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__width):
            for j in range(self.__height):
                rectangle.append("#")
            rectangle.append("\n")
        return ("".join(rectangle))

    @property
    def height(self):
        return self.__height
    
    @property
    def width(self):
        return self.__width
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
