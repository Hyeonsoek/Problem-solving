import sys, math
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    gcdrecord = defaultdict(int)
    for _ in range(n):
        a, b = map(int, input().split())
        for x in range(1, k + 1):
            gcd = math.gcd(a, b)
            gcdrecord[a // gcd, b // gcd] += 1
            a += 2 * (m * x - a)
    
    print(max(gcdrecord.values()))

solve()