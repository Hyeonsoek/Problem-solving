import sys
from collections import defaultdict
input = sys.stdin.readline
output = sys.stdout.write

def solve():
    n = int(input())
    s = set()
    maxright = {}
    minleft = {}

    for _ in range(n):
        l, r = map(int, input().split())
        s.add((l, r))
        
        maxright[l] = max(maxright[l], r) if l in maxright else r
        minleft[r] = min(minleft[r], l) if r in minleft else l

    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        if (l, r) in s:
            output('1\n')
        elif (l in maxright and maxright[l] > r) and (r in minleft and minleft[r] < l):
            output('2\n')
        else:
            output('-1\n')

solve()