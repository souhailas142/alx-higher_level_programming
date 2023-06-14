#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rslt = 0;
    prev_nbr = 0
    for c in reversed(roman_string):
        nbr = roman_numeral[c]
        if nbr >= prev_nbr:
            rslt += nbr
        else:
            rslt -= nbr
        prev_nbr = nbr
    return rslt         
