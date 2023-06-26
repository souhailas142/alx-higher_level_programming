#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len_lst = 0
    c = 0
    for item in my_list:
        len_lst += 1
    try:
        if x == 0:
            return (c)
        for index, item in enumerate(my_list):
            if index == x:
                break
            print("{:d}".format(item), end="")
            c += 1
        print()
        return (c)
    except:
        pass
