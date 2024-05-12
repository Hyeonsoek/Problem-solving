import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n = int(input())

    A, B, C, D = [], [], [], []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
        
    AB = defaultdict(int)

    for x in range(n):
        for y in range(n):
            AB[A[x] + B[y]] += 1

    result = 0
    for x in range(n):
        for y in range(n):
            value = C[x] + D[y]
            if -value in AB:
                result += AB[-value]
        
    print(result)

solve()