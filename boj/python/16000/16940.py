import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n = int(input())
    graph = [set() for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    
    visited = [0] * (n + 1)
    visited[1] = 1
    
    order = deque(map(int, input().split()))
    queue = deque([order.popleft()])
    while queue:
        vertex = queue.popleft()
        
        count = 0
        for x in graph[vertex]:
            if not visited[x]:
                count += 1
        
        for _ in range(count):
            next = order.popleft()
            if next not in graph[vertex]:
                return 0
            
            if not visited[next]:
                visited[next] = 1
                queue.append(next)
    
    for x in range(1, n + 1):
        if visited[x] == 0:
            return 0
    
    return 1

print(solve())