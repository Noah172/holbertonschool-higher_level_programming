#!/usr/bin/python3
for c in range(0, 10):
    for cc in range(c + 1, 10):
        if c == 8 and cc == 9:
            print("{}{}".format(c, cc))
        else:
            print("{}{}".format(c, cc), end=", ")
