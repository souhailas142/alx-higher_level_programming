#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        rslt = []
        for nbr in my_list:
            rslt.append(True) if nbr % 2 == 0 else rslt.append(False)
        return rslt
