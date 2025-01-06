import sys, math
input = sys.stdin.readline

def fraction(a, b):
    gcd = math.gcd(a, b)
    return a // gcd, b // gcd

def solve(index):
    input()
    p, e, t = map(int, input().split())
    Padal = [*map(int, input().split())]
    Extra = sorted([*map(int, input().split())])
    Tire = [*map(int, input().split())]
    
    extrafraction = set()
    for x in range(e - 1):
        for y in range(x + 1, e):
            xx, yy = fraction(Extra[x], Extra[y])
            extrafraction.add((xx, yy))
            extrafraction.add((yy, xx))
            
    def isinPQ(P, Q):
        for xx in range(p):
            for yy in range(t):
                a, b = fraction(P * Tire[yy], Q * Padal[xx])
                if (a, b) in extrafraction:
                    return 'Yes'
        return 'No'
    
    result = []
    m = int(input())
    for x in range(m):
        P, Q = map(int, input().split())
        result.append(isinPQ(P, Q))
    
    print(f"Case #{index}:")
    print(*result, sep='\n')

for x in range(int(input())):
    solve(x + 1)