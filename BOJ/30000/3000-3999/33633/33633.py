from collections import deque

def solve():
    n = int(input())
    
    res = []
    visited = {1: True}
    queue = deque([(1, 1)])
    while queue:
        value, index = queue.popleft()
        
        if index == n:
            res.append(value)
            continue
        
        index += 1
        nv = value * 2
        if nv > 0 and nv not in visited:
            visited[nv] = True
            queue.append((nv, index))
        
        nv = (value - 1) // 3
        if (value - 1) % 3 == 0 and nv > 1 and nv & 1 and nv not in visited:
            visited[nv] = True
            queue.append((nv, index))
    
    res.sort()
    print(len(res))
    print(*res, sep='\n')

solve()