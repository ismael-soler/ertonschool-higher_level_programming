#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)

if (number < 0):
    print(f"Last digit of {number} is -{last_digit}", end=" ")
else:
    print(f"Last digit of {number} is {last_digit}", end=" ")
if (number > 5):
    print(f"and is greater than 5")
elif (number == 0):
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
