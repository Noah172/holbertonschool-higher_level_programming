#!/usr/bin/python3
def number_of_lines(filename=""):
    nl = 0
    with open(filename) as f:
       for l in f:
           nl += 1
    return nl
