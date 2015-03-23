"""
Project Euler Problem 28
========================

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24 25
                              20  7  8  9 10
                              19  6  1  2 11
                              18  5  4  3 12
                              17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the
same way?
"""
import math

total, end = 0, int(math.floor(1001 / 2) + 1)

for i in range(0, end):
    total += (1 + 2*i)**2

for i in range(2, end + 1):
    total += 4*i**2 -10*i+7

for i in range(1, end):
    total += 4*i**2 +1

for i in range(2, end + 1):
    total += 4*i**2-6*i+3

# Way easier if one looks at each layer ( 4 corner points) seperatly and comes up with a formula
print total
