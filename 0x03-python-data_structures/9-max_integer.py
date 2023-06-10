#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        _max = my_list[0]
        for nbr in my_list:
            if nbr > _max:
                _max = nbr
        return _max
    else:
        return "None"
