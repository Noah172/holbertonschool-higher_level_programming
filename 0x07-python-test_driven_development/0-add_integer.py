#!/usr/bin/python3
""" a function that adds 2 integuers. Example:
    >>> add_integuer(2, 4)
    6
    """
def add_integer(a, b=98):
     # return the addition of the two integuers
    if not isinstance(a, int) and not isinstance(a, float):
        print("a must be an integer", end="")
        raise TypeError
    if not isinstance(b, int) and not isinstance(b, float):
        print("b must be an integer", end="")
        raise TypeError
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    r = a +b
    return r
