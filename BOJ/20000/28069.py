from collections import deque
MAX = 1_000_000

def solve():
    n, k = map(int, input().split())
    
    visited = [0] * (n + 1)
    visited[0] = 1
    
    costs = [MAX for _ in range(n + 1)]
    costs[0] = 0
    
    queue = deque([(0, 0)]) #count, node
    while queue:
        count, node = queue.popleft()
    
        for dist in [1, int(node / 2)]:
            next = node + dist
            if next <= n and costs[next] > count + 1:
                visited[next] = 1
                costs[next] = count + 1
                queue.append((count + 1, next))
    
    return k >= costs[n]

print("minigimbob" if solve() else "water")