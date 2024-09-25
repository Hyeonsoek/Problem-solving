import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    height = [0, 0] + [-1] * (n - 1)
    order = [0] * (n + 1) 
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    
    for x in range(1, n + 1):
        graph[x].sort()
    
    o = 1
    visited = [0] * (n + 1)
    visited[r] = 1
    queue = deque([(r, 0)]) #start, height
    while queue:
        node, h = queue.popleft()
        height[node] = h
        order[node], o = o, o + 1
        for next in graph[node]:
            if not visited[next]:
                visited[next] = 1
                queue.append((next, h + 1))
    
    reuslt = 0
    for x in range(1, n + 1):
        reuslt += height[x] * order[x]
    
    print(reuslt)

solve()