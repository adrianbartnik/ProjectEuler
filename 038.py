"""
Project Euler Problem 38
========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def digits(n):
    l = []
    for i in str(n):
        l.append(int(i))
    return l

def makeNumber(n):
    s = 0
    for i in range(1, len(n) + 1):
        s += n[-i] * 10 ** (i-1)
    return s

def pandigital(n):
    s = [1,2,3,4,5,6,7,8,9]
    l = []
    for i in xrange(1, 10):
        l = l + digits(n * i) 
        if len(l) > 9:
            return False
        if len(l) == 9:
            if i == 1:
                return False
            for x in s:
                if not x in l:
                    return False
            return makeNumber(l)

print [(pandigital(x), x) for x in xrange(1, 9999) if pandigital(x)]
