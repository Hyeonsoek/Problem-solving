import sys
from collections import deque
input = map(int, sys.stdin.read().split())

def solve():
    n, m = next(input), next(input)
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        a, b = next(input), next(input)
        graph[a].append(b)
    
    visited = {}
    for i in range(n):
        visited[i] = [0] * (n + 1)
        visited[i][i] = 1
        queue = deque([i])
        while queue:
            vertex = queue.popleft()
            
            for nv in graph[vertex]:
                if not visited[i][nv]:
                    visited[i][nv] = 1
                    queue.append(nv)
    
    q = next(input)
    result = []
    for _ in range(q):
        u, v = next(input), next(input)
        result.append(visited[u][v])
    
    print(*result, sep='\n')

solve()