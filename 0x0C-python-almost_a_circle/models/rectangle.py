#!/usr/bin/python3
from models.base import Base
"""importing the attibutes from base"""


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get and Set"""
        return self.__width

    @property
    def height(self):
        """Get and Set"""
        return self.__height

    @property
    def x(self):
        """Get and Set"""
        return self.__x

    @property
    def y(self):
        """Get and Set"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set value
        Args:
            value (int): width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set value
        Args:
            value (int): height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set value
        Args:
            value (int): x of the rectangle
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set value
        Args:
            value (int): y of the rectangle
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value
