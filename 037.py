"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from itertools import chain
import numpy as np
import timeit

n = 1000000

primes = np.ones(n+1, dtype=np.bool)
for i in np.arange(2, n**0.5 +1, dtype=np.uint32):
    if primes[i]:
        primes[i*i::i] = False

primes = np.nonzero(primes)[0][2:]

# vfunc = np.vectorize(str)
# primes = vfunc(primes)

def isprime(t):
    if t == 1:
        return False
    if t == 2:
        return True
    if t % 2 == 0:
        return False
    i = 3
    while i <= math.sqrt(t):
        if t % i == 0:
            return False
        i += 2
    return True

def check(n):
    n = str(n)
    return all(np.in1d([n[i:] for i in xrange(0,len(n))] + [n[:i+1] for i in xrange(0,len(n))], primes, assume_unique=True))
    # return set(list(chain.from_iterable((n[i:],n[:i+1]) for i in xrange(0,len(n))))).issubset(primes)

# print check(3797)
# print timeit.timeit(check, number=100)

result = [x for x in primes if check(x)]
print sum(result)
print result
