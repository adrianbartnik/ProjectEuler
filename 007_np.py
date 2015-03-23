import numpy as np

n = 1000000

primes = np.ones(n+1, dtype=np.bool)
for i in np.arange(2, n**0.5 +1, dtype=np.uint32):
    if primes[i]:
        primes[i*i::i] = False
print np.nonzero(primes)[0][2:][10000]
