import sys
from heapq import *
input = sys.stdin.readline

def solve():
    n, c = map(int, input().split())
    portal = [[] for _ in range(n)]
    
    for _ in range(c):
        t, a, b = map(int, input().split())
        portal[a].append((b, t))
    
    dist = [sys.maxsize] * n
    dist[0] = 0
    queue = [(0, 0)]
    while queue:
        count, node = heappop(queue)
        
        if dist[node] < count:
            continue
        
        if portal[node]:
            for b, t in portal[node]:
                if dist[b] > count:
                    dist[b] = count
                    heappush(queue, (count, b))
                
                if t and node + 1 < n and dist[node + 1] > count + 1:
                    dist[node + 1] = count + 1
                    heappush(queue, (count + 1, node + 1))
        else:
            if node + 1 < n and dist[node + 1] > count + 1:
                dist[node + 1] = count + 1
                heappush(queue, (count + 1, node + 1))
        
    if dist[n - 1] == sys.maxsize:
        return -1
    return dist[n - 1]

print(solve())