"""
Project Euler Problem #4
=========================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def chec_pal(number):
    s = str(number)
    if len(s) == 1:
        return True
    elif len(s) == 2: 
        return s[0] == s[-1]
    else: 
        return s[0] == s[-1] and chec_pal(s[1:-1])

candiates = []

for x in range(1, 1000):
    for y in range(1, 1000):
        erg = x * y
        if chec_pal(erg):
            candiates.append(erg)
print max(candiates)        
