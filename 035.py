"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import math
import numpy as np
import itertools
import timeit
import collections

n = 1000000

primes = np.ones(n+1, dtype=np.bool)

for i in np.arange(2, n**0.5 +1, dtype=np.uint32):
    if primes[i]:
        primes[i*i::i] = False

primes = np.nonzero(primes)[0][2:]

def circular(n):
    digits = int(math.log10(n)) + 1
    power = 10**(digits - 1)
    for i in range(0, digits):
        if not n in primes:
            return False
        n = (n%10) * power + n / 10
    return True

def circular2(): #timeit gives 106 ms
    i = 131
    l = itertools.permutations(str(i))
    return set([int(''.join(x)) for x in l]).issubset(primes)

circulars = [i for i in primes if circular(i)]

# print timeit.timeit(circularList, number=100)

# I should have used rotate or something similar. It would have been faster, than my current solution.
print len(circulars)
