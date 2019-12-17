#!/usr/bin/env python3
def no_c(my_string):
    nope = ""
    for i in range(0, len(my_string)):
        if my_string[i] == 'C' and  my_string[i] == 'c':
            continue
        nope += my_string[i]
    return nope
