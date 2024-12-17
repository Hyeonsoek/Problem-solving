from sys import stdin
from math import log2
input = stdin.readline

T = int(input())
for _ in range(T):
    a, b = sorted(map(int, input().split()))
    
    ha, hb = int(log2(a)), int(log2(b))
    b //= 2 ** (hb - ha)
    
    for _ in range(ha):
        if a == b:
            break
        
        a //= 2
        b //= 2
    
    print(a * 10)