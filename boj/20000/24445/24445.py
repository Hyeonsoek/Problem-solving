import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for x in range(1, n + 1):
        graph[x].sort(reverse=True)
        
    index = 2
    visited = [0] * (n + 1)
    visited[r] = 1
    queue = deque([r])
    while queue:
        node = queue.popleft()
        
        for next in graph[node]:
            if visited[next] == 0:
                queue.append(next)
                visited[next] = index
                index += 1
    
    print(*visited[1:],sep='\n')

solve()