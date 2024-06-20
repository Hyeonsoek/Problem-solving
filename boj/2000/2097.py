from math import *

def solve():
    n = int(input())

    if n <= 4:
        return 4
    
    for x in range(2, int(ceil(n ** .5)) + 1):
        if x * x >= n:
            return 4 * x - 4
        if x * x + x >= n:
            return 4 * x - 2

print(solve())