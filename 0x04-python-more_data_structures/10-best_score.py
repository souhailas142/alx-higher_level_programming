#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = next(iter(a_dictionary))
        max_sc = a_dictionary.get(best)
        for key in a_dictionary:
            if a_dictionary[key] > max_sc:
                max_sc = a_dictionary[key]
                best = key
        return best
    else:
        return "None"
