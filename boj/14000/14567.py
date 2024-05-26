import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    cache = [0] * (n + 1)

    queue = deque()
    for x in range(1, n + 1):
        if not indegree[x]:
            queue.append((x, 1))
            
    for x in range(1, n + 1):
        if not queue:
            continue
        
        node, height = queue.popleft()
        cache[node] = max(cache[node], height)
        
        for next in graph[node]:
            indegree[next] -= 1
            if not indegree[next]:
                queue.append((next, height + 1))

    print(*cache[1:])
    
solve()

# 1 -> 2, 3
# 2 -> 5
# 4 -> 5
# 1 2 2 1 3 1