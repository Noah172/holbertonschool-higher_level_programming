#!/usr/bin/env python3
def no_c(my_string):
    nope = ""
    n = len(my_string)
    for i in range(0, n):
        if my_string[i] == 'C' or my_string[i] == 'c':
            continue
        nope += my_string[i]
    return nope
