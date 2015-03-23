"""
Project Euler Problem #15
==========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""

x, y = 21, 21
grid = [[0] * y] * x
grid[0][0] = 1

for i in range(0,x):
    for j in range(0,y):
        if(0 <= i - 1 < x and 0 <= j - 1 < y):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        elif(0 <= i - 1 < x and not (0 <= j - 1 < y)):
            grid[i][j] = grid[i - 1][j]
        if(not (0 <= i - 1 < x) and 0 <= j - 1 < y):
            grid[i][j] = grid[i][j - 1]

print grid[x - 1][y - 1]
