#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rlist = []
    rlist = my_list[:]
    for i in range(0, len(rlist)):
        if rlist[i] == search:
            rlist[i] = replace
    return rlist
