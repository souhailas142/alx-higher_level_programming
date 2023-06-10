#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    firstC = sentence[0] if length > 1 else "None"
    return (length, firstC)
