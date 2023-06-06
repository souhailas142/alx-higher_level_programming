#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
print(f"Last digit of {number}", end=" ")
if n < 0:
    number *= -1
last_digit = number % 10
print(f"is {(-last_digit) if n < 0 else last_digit}", end=" ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")
