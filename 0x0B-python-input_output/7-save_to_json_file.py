#!/usr/bin/python3
"""
Write a JSON object
"""


import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode='w') as filet7:
        filet7.write(json.dumps(my_obj))
