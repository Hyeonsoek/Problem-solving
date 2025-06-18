import sys
from math import ceil
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    
    v = 0
    prefixF = [0] * (n + 1)
    prefixB = [0] * (n + 1)
    for i in range(n):
        value = 1 if arr[i] == 1 else 0
        prefixF[i] = value
        prefixB[i + 1] = value
        v += value
        
    if ceil(n / 2) <= v:
        return 0
    
    for i in range(1, n + 1):
        prefixF[i] += prefixF[i - 1]
        
    for i in range(1, n + 1):
        if v - prefixF[i - 1] == 0:
            break
        if v - prefixF[i - 1] >= ceil((n - i) / 2):
            return 1
    
    for i in reversed(range(n)):
        prefixB[i] += prefixB[i + 1]

    for i in reversed(range(n)):
        if v - prefixB[i + 1] == 0:
            break
        if v - prefixB[i + 1] >= ceil(i / 2):
            return 1
    
    return 2
    
print(solve())