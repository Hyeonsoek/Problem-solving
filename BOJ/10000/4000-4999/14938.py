import sys
from heapq import *
input = sys.stdin.readline

def solve():
    n, m, r = map(int, input().split())
    item = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(r):
        a, b, l = map(int, input().split())
        graph[a].append((b, l))
        graph[b].append((a, l))
    
    result = 0
    for x in range(1, n + 1):
        queue = [(0, x)]
        distance = [sys.maxsize] * (n + 1)
        distance[x] = 0
        while queue:
            cost, node = heappop(queue)
            
            if cost > distance[node]:
                continue
            
            for nbr, weight in graph[node]:
                nbrDist = weight + cost
                if nbrDist < distance[nbr]:
                    distance[nbr] = nbrDist
                    heappush(queue, (nbrDist, nbr))
        
        count = 0
        for xx in range(1, n + 1):
            if distance[xx] <= m:
                count += item[xx-1]
        
        result = max(result, count)
    
    print(result)
    
solve()