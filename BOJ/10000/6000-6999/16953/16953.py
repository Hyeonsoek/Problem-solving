from collections import deque
MAX = 10 ** 9

def solve():
    a, b = map(int, input().split())
    
    visited = {}
    visited[a] = True
    queue = deque([(1, a)])
    while queue:
        dist, vertex = queue.popleft()
        
        if vertex == b:
            return dist
        
        double = vertex * 2
        if double < MAX and double not in visited:
            visited[double] = True
            queue.append((dist + 1, double))
        
        one = int(str(vertex) + '1')
        if one < MAX and one not in visited:
            visited[one] = True
            queue.append((dist + 1, one))
    
    return -1

print(solve())