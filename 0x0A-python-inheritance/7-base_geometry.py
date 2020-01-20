#!/usr/bin/python3
class BaseGeometry:
    """ raises an Exception with the message area() is not implemented
    """
    def area(self):
        """rising a exeption"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
