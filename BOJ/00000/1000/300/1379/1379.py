import sys
from heapq import *
input = sys.stdin.readline

def solve():
    n = int(input())
    count = list(range(1, n + 1))
    heapify(count)
    
    start, end = [], []
    for _ in range(n):
        i, s, e = map(int, input().split())
        start.append((s, i))
        end.append((e, i))
    start.sort(); end.sort()
    
    sx = 0
    index = {}
    for x in range(n):
        while sx < n and start[sx][0] < end[x][0]:
            index[start[sx][1]] = heappop(count)
            sx += 1
        heappush(count, index[end[x][1]])
    
    print(max(index.values()))
    for x in range(n):
        print(index[x + 1])

solve()