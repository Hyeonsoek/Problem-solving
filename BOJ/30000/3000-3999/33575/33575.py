import sys
input = sys.stdin.readline

def solve():
    n, m, a, b = map(int, input().split())
    trr = [*map(int, input().split())]
    arr = set(map(int, input().split()))
    brr = set(map(int, input().split()))
    
    v, p = 0, 0
    for i in range(n):
        if trr[i] in arr:
            p += 1
        else:
            if p >= 3:
                v += p
            p = 0
    
    if p >= 3:
        v += p
        
    p = 0
    
    for i in range(n):
        if trr[i] in brr:
            p += 1
        else:
            if p >= 3:
                v -= p
            p = 0
    
    if p >= 3:
        v -= p
    
    print(v)

solve()