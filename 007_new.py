import math

# limit = int(raw_input("Enter limit"))
limit = 1000000
primes = [False] * 2 + (limit - 1) * [True]

for i in range(2, int(limit**0.5 + 1)):
    for j in range(i**2, limit + 1, i):
        primes[j] = False

# print [number for number, prime in enumerate(primes) if prime]
print [number for number, prime in enumerate(primes) if prime][10000]
