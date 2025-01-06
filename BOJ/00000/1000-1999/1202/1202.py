import sys
from heapq import *
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    data = defaultdict(list)
    for _ in range(n):
        m, v = map(int, input().split())
        data[m].append(v)

    result = 0
    index = 0
    heap = []
    mass = sorted(data.keys())
    masslen = len(mass)
    capacity = sorted([int(input()) for _ in range(k)])
    for x in range(k):
        while index < masslen and mass[index] <= capacity[x]:
            for m in data[mass[index]]:
                heappush(heap, -m)
            index += 1
        
        if heap:
            result += -heappop(heap)
        
    print(result)

solve()