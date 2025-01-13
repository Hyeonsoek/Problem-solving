import sys
from heapq import *
input = sys.stdin.readline

def solve():
    n, l = map(int, input().split())
    arr = [*map(int, input().split())]
    
    minvalue = sys.maxsize
    deleted = set()
    queue = []
    result = [0] * n
    for i in range(l):
        minvalue = min(arr[i], minvalue)
        result[i] = minvalue
        heappush(queue, (arr[i], i))
    
    for i in range(l, n):
        deleted.add(i - l)
        heappush(queue, (arr[i], i))
        
        while queue:
            v, index = heappop(queue)
            if index not in deleted:
                break
        
        result[i] = v
        heappush(queue, (v, index))
    
    print(*result)

solve()