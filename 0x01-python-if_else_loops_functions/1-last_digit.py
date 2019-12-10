#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lnum = number % 10
else:
    lnum = ((number * -1) % 10) * -1
print("Last digit of {:d} is {:d} ".format(number, lnum), end='')
if lnum == 0:
    print("and is 0")
elif lnum > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
