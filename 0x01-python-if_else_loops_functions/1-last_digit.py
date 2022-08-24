#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)

lastd = number % 10 if number > 0 else int(repr(number)[-1]) * -1
if (lastd > 5):
    print("Last digit of {:d} is {:d} and is greater than 5"
            .format(number, lastd))
elif(lastd == 0):
    print("Last digit of {:d} is {:d} and is greater than 5"
            .format(number, lastd))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
            .format(number, lastd))
