#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    rslt = 0
    for nbr in my_set:
        rslt += nbr
    return rslt
