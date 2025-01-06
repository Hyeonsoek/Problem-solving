import sys
from collections import deque
DRX = [0, 0, 1, -1]
DRY = [1, -1, 0, 0]
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    board = [[*map(int, input().strip())] for _ in range(n)]
    x, y, v = map(int, input().split())
    
    queue = deque([(x, y)])
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    
    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            nx, ny = xx + DRX[i], yy + DRY[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                visited[nx][ny] = True
                board[nx][ny] = v
                queue.append((nx, ny))
    board[x][y] = v
    
    for i in range(n):
        print(*board[i], sep = '')

solve()