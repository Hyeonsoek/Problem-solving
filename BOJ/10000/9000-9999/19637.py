import sys
from bisect import *
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    names = []
    values = []
    for _ in range(n):
        name, value = input().split()
        names.append(name)
        values.append(int(value))

    for _ in range(m):
        print(names[bisect_left(values, int(input()))])
        
solve()