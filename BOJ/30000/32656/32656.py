import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    a, b, x = map(int, input().split())
    
    def bfs(x):
        dist = [-1] * (n + 1)
        dist[x] = 0
        queue = deque([(0, x)])
        while queue:
            d, vertex = queue.popleft()
            for next in graph[vertex]:
                if dist[next] == -1:
                    dist[next] = d + 1
                    queue.append((d + 1, next))
        return dist

    distA = bfs(a)
    distB = bfs(b)
    
    count = 0
    if distA[x] < distB[x]:
        for i in range(1, n + 1):
            if distA[x] <= distA[i] and distB[x] <= distB[i]:
                if distB[x] - distA[x] == distB[i] - distA[i]:
                    count += 1
    else:
        for i in range(1, n + 1):
            if distA[x] <= distA[i] and distB[x] <= distB[i]:
                if distA[x] - distB[x] == distA[i] - distB[i]:
                    count += 1
    
    print(count)
    
solve()