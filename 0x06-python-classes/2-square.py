#!/usr/bin/python3
""" This class defines a Square it a size."""


class Square:

    """ A Square Class, has a private instance attribute: Size """

    def __init__(self, size=0):
        """ Size definition. """
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        pass
