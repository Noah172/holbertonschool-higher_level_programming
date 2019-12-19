#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ks = sorted(a_dictionary.keys())
    for i in ks:
        print("{}: {}".format(i, a_dictionary.get(i)))
