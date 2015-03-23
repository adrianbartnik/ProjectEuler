"""
Project Euler Problem #10
==========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def fast_nth_prime(n,limit=2125000):
    sum = 0
    if limit % 2 != 0:
        limit += 1
    primes = [True] * limit
    primes[0],primes[1] = [None] * 2
    count = 0 # how many primes have we found?
    for ind,val in enumerate(primes):
        if val is True:
            # sieve out non-primes by multiples of known primes
            primes[ind*2::ind] = [False] * (((limit - 1)//ind) - 1)
            if ind >= 2000000:
                return sum
            sum += ind
            count += 1
    return False

print fast_nth_prime(100000)
