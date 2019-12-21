#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = sorted(a_dictionary.keys())
    neo = {}
    for i in keys:
        neo[i] = a_dictionary[i] * 2
    return neo
