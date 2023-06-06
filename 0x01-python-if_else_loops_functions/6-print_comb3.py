#!/usr/bin/python3
nbr1 = 0
while (nbr1 < 10):
    nbr2 = nbr1 + 1
    while (nbr2 < 10):
        print("{}{}".format(nbr1, nbr2), end=(", " if nbr1 != 8 else "\n"))
        nbr2 += 1
    nbr1 += 1
