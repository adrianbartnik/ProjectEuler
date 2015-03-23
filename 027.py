"""
Project Euler Problem 27
========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                               e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""
import numpy as np

n = 1000000

primes = np.ones(n+1, dtype=np.bool)
for i in np.arange(2, n**0.5 +1, dtype=np.uint32):
    if primes[i]:
        primes[i*i::i] = False
primes = np.nonzero(primes)[0][2:]

max_a, max_b, max_count = -10000, -10000, -1

for a in range(-1000,1001):
    for b in range(-1000,1001):
        if b not in primes or (a - b) % 2 == 1:
            continue
        # print i
        for j in range(0, 1000):
            if a % 100 == 0:
                print j, a, b
            if(j**2 + a * j + b) not in primes:
                if j > max_count:
                    max_count = j
                    max_a = a
                    max_b = b
                break

print max_count, max_a, max_b
