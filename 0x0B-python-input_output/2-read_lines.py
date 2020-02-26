#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    nl = 0
    with open(filename, encoding='utf-8') as f:
        for l in f:
            nl += 1
            if nl <= nb_lines:
                print(f.read(nl))
