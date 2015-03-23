"""
Project Euler Problem 36
========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""
from numpy import binary_repr

def palindromic(n):
    n = list(str(n)) 
    for i in range(0,len(n)/2):
        if n[i] != n[-i - 1]:
            return False
    return True

# print palindromic(123454321)

print sum([ele for ele in range(1,1000001) if palindromic(ele) and palindromic(binary_repr(ele)) ])
