#!/usr/bin/python3
"""
Return the number of characters written
"""


def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as filet3:
        return filet3.write(text)
