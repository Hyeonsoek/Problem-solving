import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    parent = [x for x in range(n + 1)]
    
    def find(u):
        if parent[u] == u:
            return u
        parent[u] = find(parent[u])
        return parent[u]

    def merge(u, v):
        u = find(u)
        v = find(v)
        
        if u == v:
            return False
        
        parent[u] = v
        return True
    
    edges = []
    for _ in range(m):
        i, j, w = map(int, input().split())
        edges.append((w, i, j))
    edges.sort(reverse=True)
    
    graph = [[] for _ in range(n + 1)]
    for w, i, j in edges:
        if merge(i, j):
            graph[j].append((i, w))
            graph[i].append((j, w))
    
    for x in range(k):
        i, j = map(int, input().split())
        
        visited = [0] * (n + 1)
        visited[i] = 1
        queue = deque([(i, 0)])
        while queue:
            vertex, length = queue.popleft()
            
            if vertex == j:
                print(length)
                break
            
            for next, w in graph[vertex]:
                if not visited[next]:
                    visited[next] = 1
                    queue.append((next, min(length, w) if length else w))

solve()