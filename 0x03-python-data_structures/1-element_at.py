#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    if idx < 0 or idx > len(my_list):
        return "None"
    for item in my_list:
        if i == idx:
            return item
        i += 1
