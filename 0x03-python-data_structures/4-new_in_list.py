#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    i = 0
    for item in my_list:
        new_list.append(item)
    if idx < 0 or idx > len(new_list):
        return new_list
    while i < len(new_list):
        if i == idx:
            new_list[i] = element
        i += 1
    return new_list
