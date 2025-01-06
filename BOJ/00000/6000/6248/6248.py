import sys
from heapq import *
input = sys.stdin.readline

def solve():
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a].append((b, t))
        graph[b].append((a, t))
    
    dist = [sys.maxsize] * (n + 1)
    dist[x] = dist[0] = 0
    
    queue = [(0, x)]
    while queue:
        cost, vertex = heappop(queue)
        
        if dist[vertex] < cost:
            continue
        
        for next, vercost in graph[vertex]:
            nextcost = cost + vercost
            if dist[next] > nextcost:
                dist[next] = nextcost
                heappush(queue, (nextcost, next))
    
    print(max(dist) * 2)

solve()