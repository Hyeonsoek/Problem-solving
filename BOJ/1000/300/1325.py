import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for x in range(m):
    a, b = map(int, input().split())
    graph[b-1].append(a-1)

def bfs(node):
    count = 0
    visited = [False] * n
    visited[node] = True
    
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        count += 1
        
        for nbr in graph[cur]:
            if not visited[nbr]:
                visited[nbr] = True
                queue.append(nbr)
    
    return count

maxValue = 0
result = []
for x in range(n):
    count = bfs(x)
    maxValue = max(maxValue, count)
    result.append(count)

print(*( x + 1 for x in range(n) if maxValue == result[x] ))