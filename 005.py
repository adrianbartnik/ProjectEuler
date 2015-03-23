"""
Project Euler Problem #5
=========================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

number = 2520
found = False

while not found:
    number = number + 2520
    found = True
    for x in range(11, 21):
        if number % x != 0:
            found = False
            break

print number
