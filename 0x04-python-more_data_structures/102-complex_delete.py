#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_keys = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            delete_keys.append(key)
    for k in delete_keys:
        a_dictionary.pop(k)
    return a_dictionary
