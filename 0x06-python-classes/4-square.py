#!/usr/bin/python3
""" This class defines a Square it a size."""


class Square:

    """ A Square Class, has a private instance attribute: Size """

    def __init__(self, size=0):
        """ Size definition. """
        self.__size = size
    
    def area(self):
        """ the area of the square """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            print("size must be an integer", end="")
            raise TypeError
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val
