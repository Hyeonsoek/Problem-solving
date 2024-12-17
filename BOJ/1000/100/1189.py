from copy import deepcopy
from collections import deque

def solve():
    r, c, k = map(int, input().split())
    board = [list(input()) for _ in range(r)]

    result = 0

    visited = [[0] * c for _ in range(r)]
    visited[r-1][0] = 1

    queue = deque([(r - 1, 0, 1, deepcopy(visited))])
    while queue:
        sx, sy, dist, visited = queue.popleft()
        
        if sx == 0 and sy == c - 1:
            if dist == k:
                result += 1
            continue
        
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            xx, yy = sx + dx, sy + dy
            if 0 <= xx < r and 0 <= yy < c and\
                    board[xx][yy] != 'T' and not visited[xx][yy]:
                visited[xx][yy] = True
                queue.append((xx, yy, dist + 1, deepcopy(visited)))
                visited[xx][yy] = False
                
    print(result)
    
solve()