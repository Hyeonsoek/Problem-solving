from itertools import *
MAX = 1000000

def solve():
    n, m, l = map(int, input().split())
    arr = []
    for _ in range(n):
        ai, bi, pi = map(int, input().split())
        arr.append((ai, bi, pi))
    
    result = MAX
    for count in range(1, n + 1):
        for comb in combinations(arr, count):
            la, lb = 0, 0
            price = 0
            for ai, bi, pi in comb:
                la += ai
                lb += bi
                price += pi
                
            if price <= m and la <= l <= lb:
                result = min(result, price)
    
    return result if result != MAX else "IMPOSSIBLE"

t = int(input())
for x in range(1, t + 1):
    print(f'Case #{x}: {solve()}')