import sys
input = sys.stdin.readline
from collections import deque
DRX = [-1, -1, -1, 0, 0, 1, 1]
DRY = [-1, 0, 1, -1, 1, -1, 1]

def solve():
    n = int(input())
    board = [list(input()) for _ in range(n)]
    
    result = 0
    queue = deque()
    visited = [[False] * n for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            if board[x][y] == 'F':
                queue.append((x, y))
                visited[x][y] = True
                
    while queue:
        xx, yy = queue.popleft()
        
        for i in range(7):
            nx = DRX[i] + xx
            ny = DRY[i] + yy
            if 0 <= nx < n and 0 <= ny < n and\
                    board[nx][ny] == '.' and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))
                result += 1
    
    print(result)

solve()