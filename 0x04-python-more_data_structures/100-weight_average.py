#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        summ = 0
        div = 0
        for couple in my_list:
            mul = couple[0] * couple[1]
            summ += mul
            div += couple[1]
        return (summ / div)
    else: 
        return (0)
