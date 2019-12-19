#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0

    addition = set(my_list)
    return sum(addition)
