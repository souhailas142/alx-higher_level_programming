#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst = []
    for key, value in a_dictionary.items():
        lst.append("{}: {}".format(key, value))
    for el in sorted(lst):
        print(el)
