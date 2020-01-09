#!/usr/bin/pyrthon3
""" This class defines a Square size."""


class Square:

    """ A Square Class, has a private instance attribute: Size """

    def __init__(self, size=0):
        """ Size definition

        Args:
            size (int): Private instance attribute: size.
        """
        sif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        pass
