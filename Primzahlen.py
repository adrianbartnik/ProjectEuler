"""
Project Euler Problem #7
=========================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6^th prime is 13.

What is the 10001^st prime number?
"""
import math

limit = 1000000

numbers = [1] * limit
primes = []

for x in range(2, limit - 1):
    if numbers[x]:
        primes.append(x)
        for v in range(0,limit - 1,x):
            numbers[v] = 0

print primes[10000]
