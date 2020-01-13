#!/usr/bin/python3
def print_square(size):
    if isinstance(size, float):
        print("size must be an integer", end="")
        raise TypeError
    if size < 0:
        print("size must be >= 0", end="")
        raise TypeError
    if not isinstance(size, int):
        print("size must be an integer", end="")
        raise ValueError
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
