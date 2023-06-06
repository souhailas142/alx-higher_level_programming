#!/usr/bin/python3
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz", end=(" " if n != 100 else " \n"))
    elif n % 5 == 0:
        print("Buzz", end=(" " if n != 100 else " \n"))
    elif n % 3 == 0:
        print("Fizz", end=(" " if n != 100 else " \n"))
    else:
        print("{}".format(n), end=(" " if n != 100 else " \n"))
