#!/usr/bin/python3
""" This class defines a Square it a size."""


class Square:
    def __init__(self, size=0):
        """ Size definition. """
        self.__size = size

    def area(self):
        """ the area of the square """
        return self.__size ** 2

    def my_print(self):
        """Custom print to the stdout a square composed of #."""
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print("")

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
