#!/usr/bin/python3
class Rectangle:
    """
    creating class Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, height=0, width=0):
        """
        using it sefl
        args:
        height: the height of the rectangle
        width: the width of the rectangle
        """
        type(self).number_of_instances += 1
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
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """return a string representation of the rectangle to be able
        to recreate a new instance by using eval() (see example below)
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Print the message Bye rectangle...
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area
        Args:
            rect_1 (Rectangle): rectangle 1
            rect_2 (Rectangle): rectangle 2
        Raises:
        Returns:
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

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
