#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len_lst = 0
    c = 0
    for item in my_list:
        len_lst += 1
    try:
        if x == 0:
            return (c)
        if x >= len_lst:
            for item in my_list:
                print("{}".format(item), end="")
            print()
            return (len_lst)
        else:
            for index, item in enumerate(my_list):
                if index == x:
                    break
                print("{}".format(item), end="")
                c += 1
            print()
            return (c)
    except BaseException:
        pass