#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for _list in matrix:
        i = 0
        for item in _list:
            print("{:d}".format(item), end=(" " if i < (len(_list) - 1) else ""))
            i += 1
        print()
