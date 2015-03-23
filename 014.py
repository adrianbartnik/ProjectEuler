"""
Project Euler Problem #14
==========================

The following iterative sequence is defined for the set of positive
integers:

n n/2 (n is even)
n 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                         13 40 20 10 5 16 8 4 2 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

values = {}

def prob(n):
    if n == 1:
        return 1
    v = values.get(n)
    if v:
        return v 
    elif n % 2 == 0:
        return 1 + prob(n/2)
    else:
        return 1 + prob(3*n + 1)

max,v = 0, 0
for x in range(2,1000001):
    values[x] = prob(x)
    if values[x] > max:
        max = values[x]
        v = x

print v
