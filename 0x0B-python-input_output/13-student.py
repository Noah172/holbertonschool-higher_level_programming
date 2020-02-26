#!/usr/bin/python3
"""
Student class
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        adict = {}
        if type(attrs) == list:
            for att in attrs:
                if type(att) != str:
                    adict = self.__dict__
                    break
                try:
                    adict[att] = getattr(self, att)
                except:
                    pass
        else:
            adict = self.__dict__
        return adict

    def reload_from_json(self, json):
        for i, j in json.items():
            self.__setattr__(i, j)
