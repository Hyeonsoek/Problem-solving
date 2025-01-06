import sys
from collections import deque
direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    
    sx, sy = 0, 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == 'I':
                sx, sy = x, y
    
    count = 0
    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True
    queue = deque([(sx, sy)])
    
    while queue:
        nx, ny = queue.popleft()
        
        if board[nx][ny] == 'P':
            count += 1
        
        for xd, yd in direct:
            xx = nx + xd
            yy = ny + yd
            if 0 <= xx < n and 0 <= yy < m and\
                    not visited[xx][yy] and board[xx][yy] != 'X':
                visited[xx][yy] = True
                queue.append((xx, yy))
    
    return count if count else "TT"

print(solve())