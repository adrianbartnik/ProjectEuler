"""
Project Euler Problem 31
========================

In England the currency is made up of pound, -L-, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

It is possible to make -L-2 in the following way:

  1 * -L-1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can -L-2 be made using any number of coins?
"""

def countWays(amount, possibleCoins):
    total = 0

    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif len(possibleCoins) == 0:
        return 0
    else:
        for i in range(0, len(possibleCoins)):
            coin = possibleCoins[i]
            tmpAmount = amount

            while tmpAmount >= coin:
                tmpAmount -= coin

                total += countWays(tmpAmount, possibleCoins[i + 1:]) 

        return total

# Better solution described on project euler website
print countWays(200, [200, 100, 50, 20, 10, 5, 2, 1])
