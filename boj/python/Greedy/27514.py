import heapq
from math import log2

dicts = {x:[] for x in range(63)}

n = int(input())
arr = list(map(int, input().split()))

for x in range(n):
    if arr[x] > 0:
        key = int(log2(arr[x]))
        heapq.heappush(dicts[key], x)

for key in range(62):
    while len(dicts[key]) >= 2:
        first = heapq.heappop(dicts[key])
        second = heapq.heappop(dicts[key])
        
        heapq.heappush(dicts[key+1], first)

for key in range(62, -1, -1):
    if dicts[key]:
        print(2 ** key)
        break