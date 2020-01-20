#!/usr/bin/python3
class MyList(list):
    """class prints the list"""

    def print_sorted(self):
        """that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
