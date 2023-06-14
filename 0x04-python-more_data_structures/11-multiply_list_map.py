#!/usr/bin/python3
def multiply(nbr):
    return nbr * 2
def multiply_list_map(my_list=[], number=0):
    new_list = map(multiply, my_list)
    return list(new_list)
