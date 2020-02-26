#!/usr/bin/python3
"""
Writes to a file, append or creates it
"""


def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as filet4:
        return filet4.write(text)
