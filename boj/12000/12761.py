from collections import deque

def solve():
    a, b, n, m = map(int, input().split())
    
    nextdist = [-1, 1, -a, a, -b, b]
    
    MIN = 0
    MAX = 100001
        
    visited = [0] * MAX
    visited[n] = 1
    
    queue = deque([(n, 0)])
    while queue:
        vertex, dist = queue.popleft()
        
        if vertex == m:
            print(dist)
            return
        
        for nbr in nextdist:
            if MIN <= nbr + vertex < MAX and not visited[nbr + vertex]:
                visited[nbr + vertex] = 1
                queue.append((nbr + vertex, dist + 1))
        
        for nbr in [vertex * a, vertex * b]:
            if MIN <= nbr < MAX and not visited[nbr]:
                visited[nbr] = 1
                queue.append((nbr, dist + 1))
    
solve()