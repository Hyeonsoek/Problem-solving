from itertools import *

def solve(o):
    n, *arr = map(int, input().split())
    
    cache = {}
    for x in range(1, n + 1):
        for comb in combinations(arr, x):
            sumvalue = sum(comb)
            if sumvalue in cache:
                print(f"Case #{o}:")
                print(*cache[sumvalue])
                print(*comb)
                return
            cache[sum(comb)] = comb

for x in range(int(input())):
    solve(x+1)