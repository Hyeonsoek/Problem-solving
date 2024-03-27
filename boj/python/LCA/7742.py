import sys
import collections
MAX_DEPTH = 17
input = sys.stdin.readline

def solve():
    n, q = map(int, input().split())
    indegree = [False] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(n - 1):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))
        graph[end].append((start, cost))
        indegree[end] |= True
        
    start = 0
    for x in range(1, n + 1):
        if not indegree[x]:
            start = x
            break
    
    depths = [0] * (n + 1)
    parent = [[0] * MAX_DEPTH for _ in range(n + 1)]
    distance = [[0] * MAX_DEPTH for _ in range(n + 1)]
    
    def bfs(start):
        visited = [False] * (n + 1)
        visited[start] = True
        
        queue = collections.deque([(start, 1)])
        while queue:
            node, depth = queue.popleft()
            
            depths[node] = depth
            
            for next, cost in graph[node]:
                if not visited[next]:
                    parent[next][0] = node
                    distance[next][0] = cost
                    visited[next] = True
                    queue.append((next, depth + 1))
    
    def LCA(u, v):
        result = 0
        if depths[u] < depths[v]:
            u, v = v, u
            
        for depth in range(MAX_DEPTH - 1, -1, -1):
            if depths[u] - depths[v] >= 1 << depth:
                result += distance[u][depth]
                u = parent[u][depth]
        
        if u != v:
            for depth in range(MAX_DEPTH - 1, -1, -1):
                if parent[u][depth] and parent[u][depth] != parent[v][depth]:
                    result += distance[u][depth] + distance[v][depth]
                    u = parent[u][depth]
                    v = parent[v][depth]
                    
            result += distance[u][0] + distance[v][0]
        
        return result

    bfs(start)
    
    for depth in range(1, MAX_DEPTH):
        for node in range(1, n + 1):
            if parent[node][depth - 1]:
                parent[node][depth] = parent[parent[node][depth - 1]][depth - 1]
                distance[node][depth] = distance[node][depth - 1] + distance[parent[node][depth - 1]][depth - 1]
    
    for _ in range(q):
        sys.stdout.write(f'{LCA(*map(int, input().split()))}\n')

solve()