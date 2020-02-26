#!/usr/bin/python3
"""
Creates an object from a JSON file
"""


import json


def load_from_json_file(filename):
    with open(filename, encoding='utf-8') as filet8:
        obj = json.load(filet8)
    return obj
