"""
Project Euler Problem #3
=========================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math

factors = []
number = 600851475143

for x in range(1, int(math.sqrt(number))):
    if number % x == 0:
        factors.append(x)
        number = number / x

print factors[4]
