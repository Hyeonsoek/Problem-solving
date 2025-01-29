from collections import *

def solve():
    n, k = map(int, input().split())
    arr = []
    data = defaultdict(set)
    for _ in range(n):
        i, g, s, b = map(int, input().split())
        arr.append((g, s, b, i))
        data[g, s, b].add(i)
    arr.sort(reverse=True)
    
    j = 1
    for g, s, b, i in arr:
        if i == k or k in data[g, s, b]:
            break
        j += 1
    
    print(j)

solve()