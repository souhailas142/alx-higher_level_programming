#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        if idx < 0 or idx > len(my_list):
            return my_list
        else:
            i = 0
            while i < len(my_list):
                if i == idx:
                    del my_list[i]
                i += 1
            return my_list
