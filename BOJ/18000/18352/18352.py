import sys
from heapq import *
input = sys.stdin.readline

def solve():
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    visited = [sys.maxsize] * (n + 1)
    visited[x] = 0
    
    queue = [(0, x)]
    while queue:
        dist, vertex = heappop(queue)
        
        for next in graph[vertex]:
            ndist = dist + 1
            if visited[next] > ndist:
                visited[next] = ndist
                heappush(queue, (ndist, next))
    
    result = []
    for i in range(1, n + 1):
        if visited[i] == k:
            result.append(i)
    
    if result:
        print(*result, sep='\n')
    else:
        print(-1)

solve()