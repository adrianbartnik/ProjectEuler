"""
Project Euler Problem 39
========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""
from collections import Counter

# def triangle(n):
#     s = 0
#     for a in xrange(1, n):
#         aq = a**2
#         nq = n - a
#         for b in xrange(a, n - a + 1):
#             bq = b**2
#             nq = n - a - b
#             for c in xrange(b, n - a - b + 1):
#                 if c**2 == aq + bq and c == nq:
#                     s += 1
#     return s

def genall():
    l = []
    for a in xrange(1, 1000):
        aq = a**2
        for b in xrange(a, 1000 - a + 1):
            bq = b**2
            for c in xrange(b, 1000 - a - b + 1):
                if c**2 == aq + bq:
                    l.append((a,b,c))
    return l

print Counter([sum(x) for x in genall()])
