from sys import stdin
from bisect import bisect_left
from collections import defaultdict
input = stdin.readline

n, h = map(int, input().split())
down, up = [], []

for x in range(n):
    hi = int(input())
    up.append(hi) if x & 1 else down.append(hi)

down.sort()
up.sort()

answer = 500001
memo = defaultdict(int)
for x in range(1, h + 1):
    bdown = bisect_left(down, x)
    bup = bisect_left(up, h - x + 1)
    
    count = n - (bdown + bup)
    memo[count] += 1
    
    if answer > count:
        answer = count

print(answer, memo[answer])